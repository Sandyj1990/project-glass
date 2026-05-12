"""CLI entry point for the Google Drive folder downloader."""

from __future__ import annotations

import argparse
import logging
import re
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from .auth import get_credentials
from .downloader import DownloadError, SkippedFile, download_file
from .manifest import (
    STATUS_COMPLETED,
    STATUS_FAILED,
    STATUS_IN_PROGRESS,
    STATUS_SKIPPED,
    Manifest,
)
from .traversal import DriveFile, get_folder_metadata, walk

log = logging.getLogger("gdrive_download")


_FOLDER_ID_RE = re.compile(r"[-\w]{20,}")


def parse_folder_arg(value: str) -> str:
    """Accept either a raw folder ID or a Drive URL containing one."""
    value = value.strip()
    # Common URL shapes:
    #   https://drive.google.com/drive/folders/<ID>
    #   https://drive.google.com/drive/u/0/folders/<ID>
    #   https://drive.google.com/drive/folders/<ID>?usp=sharing
    m = re.search(r"/folders/([-\w]{20,})", value)
    if m:
        return m.group(1)
    if _FOLDER_ID_RE.fullmatch(value):
        return value
    raise argparse.ArgumentTypeError(f"Could not extract a Drive folder ID from {value!r}")


def build_arg_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="gdrive_download",
        description="Recursively download a Google Drive folder.",
    )
    p.add_argument(
        "--folder-id",
        required=True,
        type=parse_folder_arg,
        help="Drive folder ID or full Drive folder URL.",
    )
    p.add_argument(
        "--output",
        default="./drive_download",
        help="Local output directory (default: ./drive_download).",
    )
    p.add_argument(
        "--credentials",
        default="./credentials.json",
        help="Path to OAuth Desktop credentials JSON (default: ./credentials.json).",
    )
    p.add_argument(
        "--service-account",
        default=None,
        help="Path to a service account key JSON. Mutually exclusive with --use-adc.",
    )
    p.add_argument(
        "--use-adc",
        action="store_true",
        help="Use Application Default Credentials (e.g. from `gcloud auth application-default login`).",
    )
    p.add_argument("--token", default="./token.json", help="Where to cache OAuth tokens.")
    p.add_argument("--workers", type=int, default=4, help="Parallel download threads.")
    p.add_argument(
        "--chunk-size", type=int, default=10 * 1024 * 1024, help="Download chunk size in bytes."
    )
    p.add_argument(
        "--dry-run",
        action="store_true",
        help="List files that would be downloaded without writing anything.",
    )
    p.add_argument(
        "--log-level",
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        help="Logging verbosity.",
    )
    return p


def _build_service(creds):
    # cache_discovery=False avoids a noisy warning when oauth2client isn't installed.
    return build("drive", "v3", credentials=creds, cache_discovery=False)


def _human_size(n: int | None) -> str:
    if n is None:
        return "?"
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if n < 1024:
            return f"{n:.1f} {unit}" if unit != "B" else f"{n} B"
        n /= 1024
    return f"{n:.1f} PB"


class _ServiceFactory:
    """Thread-local Drive service builder.

    The googleapiclient `build()` result and underlying httplib2.Http are not
    safe to share across threads, so each worker gets its own.
    """

    def __init__(self, creds):
        self._creds = creds
        self._local = threading.local()

    def get(self):
        svc = getattr(self._local, "svc", None)
        if svc is None:
            svc = _build_service(self._creds)
            self._local.svc = svc
        return svc


def _process_one(
    factory: _ServiceFactory,
    file: DriveFile,
    output_root: Path,
    chunk_size: int,
    manifest: Manifest,
    counter: dict,
    counter_lock: threading.Lock,
    total: int,
) -> None:
    with counter_lock:
        counter["i"] += 1
        idx = counter["i"]
    prefix = f"[{idx}/{total}]"

    if manifest.is_completed(file.id, file.md5):
        log.info("%s Skipped:    %s (already downloaded)", prefix, file.remote_path)
        return

    manifest.upsert(
        file.id,
        remotePath=file.remote_path,
        mimeType=file.mime_type,
        size=file.size,
        status=STATUS_IN_PROGRESS,
    )
    log.info("%s Downloading: %s (%s)", prefix, file.remote_path, _human_size(file.size))
    started = time.monotonic()
    try:
        local_path, md5 = download_file(factory.get(), file, output_root, chunk_size)
        elapsed = time.monotonic() - started
        manifest.upsert(
            file.id,
            localPath=str(local_path),
            md5Checksum=md5,
            status=STATUS_COMPLETED,
            downloadedAt=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        )
        log.info(
            "%s Completed:   %s (%s, %.1fs)",
            prefix,
            file.remote_path,
            _human_size(local_path.stat().st_size),
            elapsed,
        )
    except SkippedFile as e:
        manifest.upsert(file.id, status=STATUS_SKIPPED, error=str(e))
        log.warning("%s Skipped:    %s (%s)", prefix, file.remote_path, e)
    except (DownloadError, HttpError, OSError) as e:
        manifest.upsert(file.id, status=STATUS_FAILED, error=str(e))
        log.error("%s Failed:     %s (%s)", prefix, file.remote_path, e)


def main(argv: list[str] | None = None) -> int:
    args = build_arg_parser().parse_args(argv)

    if args.use_adc and args.service_account:
        print("error: --use-adc and --service-account are mutually exclusive", file=sys.stderr)
        return 2

    logging.basicConfig(
        level=getattr(logging, args.log_level),
        format="%(asctime)s %(levelname)-5s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    output_root = Path(args.output).resolve()
    output_root.mkdir(parents=True, exist_ok=True)

    log.info("Authenticating...")
    try:
        creds = get_credentials(
            use_adc=args.use_adc,
            service_account_path=args.service_account,
            credentials_path=args.credentials,
            token_path=args.token,
        )
    except FileNotFoundError as e:
        log.error("%s", e)
        return 2

    main_service = _build_service(creds)

    log.info("Reading root folder metadata...")
    try:
        meta = get_folder_metadata(main_service, args.folder_id)
    except HttpError as e:
        log.error("Could not read folder %s: %s", args.folder_id, e)
        return 1
    if meta.get("mimeType") != "application/vnd.google-apps.folder":
        log.error("ID %s is not a folder (mimeType=%s)", args.folder_id, meta.get("mimeType"))
        return 1
    root_name = meta.get("name", "drive_root")
    log.info("Walking folder tree under %r ...", root_name)
    files = walk(main_service, args.folder_id, root_name=root_name)
    log.info("Discovered %d files.", len(files))

    if args.dry_run:
        for f in files:
            print(f"{f.mime_type:50s}  {_human_size(f.size):>10s}  {f.remote_path}")
        log.info("Dry run complete. %d files would be processed.", len(files))
        return 0

    manifest = Manifest(output_root / "manifest.json", args.folder_id)
    factory = _ServiceFactory(creds)
    counter = {"i": 0}
    counter_lock = threading.Lock()
    total = len(files)

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = [
            pool.submit(
                _process_one,
                factory,
                f,
                output_root,
                args.chunk_size,
                manifest,
                counter,
                counter_lock,
                total,
            )
            for f in files
        ]
        try:
            for fut in as_completed(futures):
                fut.result()
        except KeyboardInterrupt:
            log.warning("Interrupted by user. Cancelling pending downloads...")
            pool.shutdown(wait=False, cancel_futures=True)
            manifest.save()
            return 130

    manifest.save()
    summary = manifest.summary()
    log.info(
        "Download complete: %d succeeded, %d skipped, %d failed (see %s)",
        summary.get(STATUS_COMPLETED, 0),
        summary.get(STATUS_SKIPPED, 0),
        summary.get(STATUS_FAILED, 0),
        manifest.path,
    )
    return 0 if summary.get(STATUS_FAILED, 0) == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
