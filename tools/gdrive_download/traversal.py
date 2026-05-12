"""Recursively enumerate all files under a Drive folder."""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field
from typing import Iterator

from .rate_limiter import with_backoff

log = logging.getLogger(__name__)

FOLDER_MIME = "application/vnd.google-apps.folder"

LIST_FIELDS = (
    "nextPageToken, files(id, name, mimeType, size, modifiedTime, md5Checksum, "
    "shortcutDetails)"
)


@dataclass
class DriveFile:
    id: str
    name: str
    mime_type: str
    size: int | None
    modified_time: str | None
    md5: str | None
    remote_path: str
    parent_path: list[str] = field(default_factory=list)

    @property
    def is_folder(self) -> bool:
        return self.mime_type == FOLDER_MIME


_INVALID_FILENAME_CHARS = re.compile(r'[<>:"/\\|?*\x00-\x1f]')


def sanitize(name: str) -> str:
    """Make a Drive filename safe for the local filesystem."""
    cleaned = _INVALID_FILENAME_CHARS.sub("_", name).strip(". ")
    return cleaned or "_unnamed"


@with_backoff
def _list_page(service, *, q: str, page_token: str | None):
    return (
        service.files()
        .list(
            q=q,
            fields=LIST_FIELDS,
            pageSize=1000,
            orderBy="name",
            pageToken=page_token,
            supportsAllDrives=True,
            includeItemsFromAllDrives=True,
        )
        .execute()
    )


def list_folder(service, folder_id: str) -> Iterator[dict]:
    """Yield raw file dicts for one folder (non-recursive)."""
    q = f"'{folder_id}' in parents and trashed = false"
    page_token: str | None = None
    while True:
        resp = _list_page(service, q=q, page_token=page_token)
        for f in resp.get("files", []):
            yield f
        page_token = resp.get("nextPageToken")
        if not page_token:
            break


def walk(service, root_folder_id: str, root_name: str = "") -> list[DriveFile]:
    """Recursively walk a folder; return a flat list of DriveFile entries.

    Folders themselves are NOT returned — only leaf files. Local directories
    are created on demand by the downloader from each file's remote_path.
    """
    results: list[DriveFile] = []

    def _recurse(folder_id: str, parent_path: list[str]) -> None:
        for raw in list_folder(service, folder_id):
            name = raw["name"]
            safe_name = sanitize(name)
            mime = raw["mimeType"]
            current_path = parent_path + [safe_name]
            if mime == FOLDER_MIME:
                log.debug("Entering folder: %s", "/".join(current_path))
                _recurse(raw["id"], current_path)
            else:
                size = int(raw["size"]) if raw.get("size") else None
                results.append(
                    DriveFile(
                        id=raw["id"],
                        name=name,
                        mime_type=mime,
                        size=size,
                        modified_time=raw.get("modifiedTime"),
                        md5=raw.get("md5Checksum"),
                        remote_path="/".join(current_path),
                        parent_path=parent_path,
                    )
                )

    _recurse(root_folder_id, [sanitize(root_name)] if root_name else [])
    return results


@with_backoff
def get_folder_metadata(service, folder_id: str) -> dict:
    return (
        service.files()
        .get(fileId=folder_id, fields="id, name, mimeType", supportsAllDrives=True)
        .execute()
    )
