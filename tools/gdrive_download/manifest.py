"""Manifest: persistent state for resumable downloads."""

from __future__ import annotations

import json
import threading
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

STATUS_PENDING = "pending"
STATUS_IN_PROGRESS = "in_progress"
STATUS_COMPLETED = "completed"
STATUS_FAILED = "failed"
STATUS_SKIPPED = "skipped"


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


class Manifest:
    def __init__(self, path: Path, root_folder_id: str):
        self.path = path
        self._lock = threading.Lock()
        if path.exists():
            self.data = json.loads(path.read_text())
        else:
            self.data = {
                "rootFolderId": root_folder_id,
                "startedAt": _now_iso(),
                "files": {},
            }
            self._save_unlocked()

    def _save_unlocked(self) -> None:
        tmp = self.path.with_suffix(self.path.suffix + ".tmp")
        tmp.write_text(json.dumps(self.data, indent=2))
        tmp.replace(self.path)

    def save(self) -> None:
        with self._lock:
            self._save_unlocked()

    def get(self, file_id: str) -> dict[str, Any] | None:
        with self._lock:
            return self.data["files"].get(file_id)

    def is_completed(self, file_id: str, remote_md5: str | None = None) -> bool:
        entry = self.get(file_id)
        if not entry or entry.get("status") != STATUS_COMPLETED:
            return False
        local_path = entry.get("localPath")
        if not local_path or not Path(local_path).exists():
            return False
        if remote_md5 and entry.get("md5Checksum"):
            return entry["md5Checksum"] == remote_md5
        return True

    def upsert(self, file_id: str, **fields: Any) -> None:
        with self._lock:
            existing = self.data["files"].get(file_id, {})
            existing.update(fields)
            self.data["files"][file_id] = existing
            self._save_unlocked()

    def summary(self) -> dict[str, int]:
        counts = {
            STATUS_COMPLETED: 0,
            STATUS_FAILED: 0,
            STATUS_SKIPPED: 0,
            STATUS_PENDING: 0,
            STATUS_IN_PROGRESS: 0,
        }
        with self._lock:
            for entry in self.data["files"].values():
                status = entry.get("status", STATUS_PENDING)
                counts[status] = counts.get(status, 0) + 1
        return counts
