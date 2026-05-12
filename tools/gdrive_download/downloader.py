"""Download binary files and export Google Workspace files."""

from __future__ import annotations

import hashlib
import io
import logging
from pathlib import Path

from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload

from .rate_limiter import with_backoff
from .traversal import DriveFile

log = logging.getLogger(__name__)

# Google Workspace export mapping: source mimeType -> (export mimeType, extension).
EXPORT_MAP: dict[str, tuple[str, str]] = {
    "application/vnd.google-apps.document": (
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        ".docx",
    ),
    "application/vnd.google-apps.spreadsheet": (
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        ".xlsx",
    ),
    "application/vnd.google-apps.presentation": (
        "application/vnd.openxmlformats-officedocument.presentationml.presentation",
        ".pptx",
    ),
    "application/vnd.google-apps.drawing": ("application/pdf", ".pdf"),
}

SKIP_TYPES = {
    "application/vnd.google-apps.form",
    "application/vnd.google-apps.map",
    "application/vnd.google-apps.site",
    "application/vnd.google-apps.shortcut",
}

EXPORT_SIZE_LIMIT = 10 * 1024 * 1024  # 10 MB


class DownloadError(Exception):
    pass


class SkippedFile(Exception):
    pass


def _resolve_local_path(output_root: Path, remote_path: str) -> Path:
    """Combine output root with the remote path. Resolve filename collisions."""
    target = output_root / remote_path
    if not target.exists():
        return target
    stem = target.stem
    suffix = target.suffix
    parent = target.parent
    i = 1
    while True:
        candidate = parent / f"{stem}_{i}{suffix}"
        if not candidate.exists():
            return candidate
        i += 1


def _md5_of(path: Path) -> str:
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


@with_backoff
def _download_binary(service, file_id: str, dest: Path, chunk_size: int) -> None:
    request = service.files().get_media(fileId=file_id, supportsAllDrives=True)
    dest.parent.mkdir(parents=True, exist_ok=True)
    with open(dest, "wb") as fh:
        downloader = MediaIoBaseDownload(fh, request, chunksize=chunk_size)
        done = False
        while not done:
            _, done = downloader.next_chunk()


@with_backoff
def _export_workspace(service, file_id: str, export_mime: str, dest: Path) -> None:
    request = service.files().export_media(fileId=file_id, mimeType=export_mime)
    dest.parent.mkdir(parents=True, exist_ok=True)
    buf = io.BytesIO()
    downloader = MediaIoBaseDownload(buf, request)
    done = False
    while not done:
        _, done = downloader.next_chunk()
    dest.write_bytes(buf.getvalue())


def download_file(
    service,
    file: DriveFile,
    output_root: Path,
    chunk_size: int,
) -> tuple[Path, str | None]:
    """Download or export a single file.

    Returns (local_path, md5_or_none). Raises SkippedFile or DownloadError.
    """
    if file.mime_type in SKIP_TYPES:
        raise SkippedFile(f"unsupported type: {file.mime_type}")

    if file.mime_type in EXPORT_MAP:
        export_mime, ext = EXPORT_MAP[file.mime_type]
        # Append the export extension if not already present.
        remote_path = file.remote_path
        if not remote_path.lower().endswith(ext):
            remote_path = remote_path + ext
        local_path = _resolve_local_path(output_root, remote_path)

        # Workspace files have no size pre-known; check post-export.
        try:
            _export_workspace(service, file.id, export_mime, local_path)
        except HttpError as e:
            msg = str(e).lower()
            if "exportsizelimit" in msg or "this file is too large to be exported" in msg:
                raise DownloadError("export exceeded 10MB limit")
            raise

        if local_path.stat().st_size == 0:
            local_path.unlink(missing_ok=True)
            raise DownloadError("export produced empty file")
        if local_path.stat().st_size > EXPORT_SIZE_LIMIT:
            log.warning("Exported file %s exceeds 10MB; keeping anyway", local_path)
        return local_path, None

    # Binary download path.
    local_path = _resolve_local_path(output_root, file.remote_path)
    _download_binary(service, file.id, local_path, chunk_size)

    md5 = None
    if file.md5:
        local_md5 = _md5_of(local_path)
        if local_md5 != file.md5:
            raise DownloadError(f"md5 mismatch (expected {file.md5}, got {local_md5})")
        md5 = local_md5
    return local_path, md5
