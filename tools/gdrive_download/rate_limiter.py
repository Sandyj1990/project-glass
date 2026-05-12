"""Exponential backoff with jitter for transient Drive API errors."""

from __future__ import annotations

import logging
import random
import time
from functools import wraps

from googleapiclient.errors import HttpError

log = logging.getLogger(__name__)

BASE_DELAY = 1.0
MAX_DELAY = 64.0
MAX_RETRIES = 5

RETRYABLE_STATUSES = {429, 500, 502, 503, 504}
RETRYABLE_403_REASONS = {"rateLimitExceeded", "userRateLimitExceeded"}


def _is_retryable(error: HttpError) -> bool:
    status = error.resp.status
    if status in RETRYABLE_STATUSES:
        return True
    if status == 403:
        try:
            details = error.error_details if hasattr(error, "error_details") else []
        except Exception:
            details = []
        reason_match = any(
            d.get("reason") in RETRYABLE_403_REASONS for d in details if isinstance(d, dict)
        )
        if reason_match:
            return True
        # Fall back to message inspection.
        msg = str(error).lower()
        if "ratelimitexceeded" in msg or "userratelimitexceeded" in msg:
            return True
    return False


def with_backoff(func):
    """Decorator that retries on transient HttpError with exponential backoff + jitter."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        attempt = 0
        while True:
            try:
                return func(*args, **kwargs)
            except HttpError as e:
                if not _is_retryable(e) or attempt >= MAX_RETRIES:
                    raise
                delay = min(BASE_DELAY * (2**attempt), MAX_DELAY)
                delay += random.uniform(0, delay * 0.25)
                log.warning(
                    "Transient error (status=%s) on attempt %d/%d, backing off %.1fs",
                    e.resp.status,
                    attempt + 1,
                    MAX_RETRIES,
                    delay,
                )
                time.sleep(delay)
                attempt += 1
            except (TimeoutError, ConnectionError) as e:
                if attempt >= MAX_RETRIES:
                    raise
                delay = min(BASE_DELAY * (2**attempt), MAX_DELAY)
                delay += random.uniform(0, delay * 0.25)
                log.warning(
                    "Network error (%s) on attempt %d/%d, backing off %.1fs",
                    type(e).__name__,
                    attempt + 1,
                    MAX_RETRIES,
                    delay,
                )
                time.sleep(delay)
                attempt += 1

    return wrapper
