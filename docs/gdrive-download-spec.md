# Google Drive Folder Download Integration — Technical Spec

## Overview

A Python CLI tool that recursively downloads entire Google Drive folders to a local directory, including exporting Google Workspace files (Docs, Sheets, Slides) to standard formats. Designed for large folder trees with robust error handling and resumability.

---

## Authentication

**Method:** OAuth 2.0 — Desktop Application flow (installed app)

### Setup

1. Create a project in [Google Cloud Console](https://console.cloud.google.com/)
2. Enable the **Google Drive API**
3. Create OAuth 2.0 credentials → Application type: **Desktop app**
4. Download the credentials JSON file as `credentials.json`

### Scopes

```
https://www.googleapis.com/auth/drive.readonly
```

Read-only access is sufficient. No write operations are needed.

### Token Lifecycle

- On first run, open a local browser window for user consent
- Store the resulting access + refresh tokens in `token.json`
- On subsequent runs, load `token.json` and silently refresh if expired
- If the refresh token is revoked or expired, re-run the full consent flow

### Dependencies

```
google-api-python-client >= 2.100.0
google-auth-oauthlib >= 1.1.0
google-auth-httplib2 >= 0.2.0
google-auth >= 2.23.0
```

---

## Alternative Authentication (No GCP Console Access)

If you cannot create an OAuth client in the Google Cloud Console (common in enterprise setups where GCP access is locked down), the tool should support these fallback authentication methods, ordered from most to least practical.

### Option 1: Request Credentials from a GCP Admin

Most orgs have a cloud/platform team that manages GCP projects. Request a **Desktop App OAuth client** scoped to `drive.readonly`. They provide the `credentials.json` file — you never need console access yourself.

This is the cleanest path. No code changes needed; the tool works as specified above.

### Option 2: Service Account (Shared by Team)

If your org has a service account with Drive API access (common for automation), use its JSON key file.

**Caveat:** Service accounts can only access files **explicitly shared with them** or files on a **Shared Drive** they've been added to. They do **not** see your personal "My Drive" unless you share folders with the service account's email address.

**CLI flag:**

```
--service-account <PATH_TO_service_account.json>
```

**Python implementation:**

```python
from google.oauth2 import service_account

creds = service_account.Credentials.from_service_account_file(
    service_account_path,
    scopes=['https://www.googleapis.com/auth/drive.readonly'],
)
```

**Required for Shared Drive access:** Set `supportsAllDrives=true` and `includeItemsFromAllDrives=true` on all `files.list` and `files.get` calls (see Open Question #1).

### Option 3: Application Default Credentials via gcloud CLI

If you have `gcloud` installed and authenticated (many enterprise environments set this up by default), you can use **Application Default Credentials (ADC)** without needing your own OAuth client or credentials file.

**Setup:**

```bash
gcloud auth application-default login \
  --scopes=https://www.googleapis.com/auth/drive.readonly
```

This stores a token at `~/.config/gcloud/application_default_credentials.json`. The Python client picks it up automatically:

```python
import google.auth

creds, project = google.auth.default(
    scopes=['https://www.googleapis.com/auth/drive.readonly']
)
```

**CLI flag:**

```
--use-adc
```

When set, skip the OAuth flow and `credentials.json` lookup entirely. No `token.json` is created — gcloud manages the token lifecycle.

This is the recommended option if `gcloud` is already configured.

### Auth Method Selection Logic

The tool should select the auth method in this order of precedence:

1. `--use-adc` flag → use Application Default Credentials
2. `--service-account <path>` flag → use service account
3. `--credentials <path>` flag (default) → use OAuth Desktop flow

Exactly one method is used per run. Conflicting flags should produce an error.

### Comparison Table

| Method                  | Requires GCP Console? | Accesses My Drive? | Accesses Shared Drives? | Token Refresh    |
|-------------------------|----------------------|--------------------|--------------------------|------------------|
| OAuth Desktop App       | Yes (one-time)       | Yes                | Yes (with permission)    | Auto via refresh token |
| Service Account         | No (admin provisions)| Only shared folders| Yes (when added)         | Auto via JWT     |
| Application Default Creds | No                 | Yes (as gcloud user)| Yes (as gcloud user)    | Managed by gcloud|

---

## Core Functionality

### 1. Folder Traversal

Recursively enumerate all files and sub-folders under a given root folder ID.

**API call:** `files.list`

```
GET https://www.googleapis.com/drive/v3/files
```

**Query parameters:**

| Parameter   | Value                                                        |
|-------------|--------------------------------------------------------------|
| `q`         | `'<folderId>' in parents and trashed = false`                |
| `fields`    | `nextPageToken, files(id, name, mimeType, size, modifiedTime)` |
| `pageSize`  | `1000`                                                       |
| `orderBy`   | `name`                                                       |

**Pagination:** Follow `nextPageToken` until exhausted.

**Recursion:** When a result has `mimeType == 'application/vnd.google-apps.folder'`, recurse into it.

### 2. Binary File Downloads

For non-Google-Workspace files (PDFs, images, ZIPs, etc.), download the raw bytes.

**API call:** `files.get` with `alt=media`

```
GET https://www.googleapis.com/drive/v3/files/<fileId>?alt=media
```

**Implementation notes:**

- Use `MediaIoBaseDownload` with chunked transfer (default chunk: 100 MB recommended for large files, 10 MB for smaller ones)
- Stream to disk — do not buffer entire file in memory
- Preserve the original filename and directory structure locally

### 3. Google Workspace File Exports

Google Workspace files have no raw bytes — they must be exported to a standard format.

**API call:** `files.export`

```
GET https://www.googleapis.com/drive/v3/files/<fileId>/export?mimeType=<exportMime>
```

**Export mapping:**

| Google Workspace Type                        | mimeType                                        | Export As       | Extension |
|----------------------------------------------|------------------------------------------------|-----------------|-----------|
| `application/vnd.google-apps.document`       | `application/vnd.openxmlformats-officedocument.wordprocessingml.document` | Word (.docx)    | `.docx`   |
| `application/vnd.google-apps.spreadsheet`    | `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`       | Excel (.xlsx)   | `.xlsx`   |
| `application/vnd.google-apps.presentation`   | `application/vnd.openxmlformats-officedocument.presentationml.presentation` | PowerPoint (.pptx) | `.pptx` |
| `application/vnd.google-apps.drawing`        | `application/pdf`                               | PDF             | `.pdf`    |
| `application/vnd.google-apps.form`           | _skip_ (not exportable to a useful format)      | —               | —         |

**Limit:** Export is capped at **10 MB**. If the export exceeds this, log a warning and skip the file.

### 4. Skipped Types

The following Google-internal types should be logged and skipped:

- `application/vnd.google-apps.shortcut` — resolve the target or skip
- `application/vnd.google-apps.form`
- `application/vnd.google-apps.map`
- `application/vnd.google-apps.site`

---

## Rate Limiting & Quotas

Google Drive API enforces the following default quotas:

| Quota                        | Limit                     |
|------------------------------|---------------------------|
| Queries per 100 seconds      | 12,000 (project-wide)     |
| Queries per 100 seconds/user | 20,000                    |
| Download bandwidth           | 10 GB per user per day    |

### Strategy

- Use **exponential backoff** with jitter on `403 (rateLimitExceeded)` and `429` responses
- Base delay: 1 second, max delay: 64 seconds, max retries: 5
- On `500` / `503`, retry with backoff (transient server errors)
- Track request count per second; preemptively throttle if approaching limits

---

## Resumability & Fault Tolerance

### Download Manifest

Maintain a local JSON manifest (`manifest.json`) at the root of the output directory:

```json
{
  "rootFolderId": "1A2B3C...",
  "startedAt": "2026-04-29T10:00:00Z",
  "files": {
    "<fileId>": {
      "remotePath": "Reports/Q1/summary.docx",
      "localPath": "output/Reports/Q1/summary.docx",
      "size": 245760,
      "status": "completed",
      "md5Checksum": "abc123...",
      "downloadedAt": "2026-04-29T10:01:12Z"
    }
  }
}
```

**Status values:** `pending`, `in_progress`, `completed`, `failed`, `skipped`

### Resume Behavior

On re-run with the same output directory:

1. Load `manifest.json`
2. Skip files with `status: completed` whose `md5Checksum` matches the remote file (if available)
3. Re-attempt files with `status: failed` or `in_progress`
4. Discover and download any newly added files

### Integrity Verification

- For binary files, compare `md5Checksum` from `files.get` metadata with the local file's MD5
- For exported Workspace files, MD5 is not available — verify file size is non-zero and file is openable

---

## CLI Interface

```
python gdrive_download.py \
  --folder-id <GOOGLE_DRIVE_FOLDER_ID> \
  --output <LOCAL_OUTPUT_DIR> \
  --credentials <PATH_TO_credentials.json> \
  --workers <PARALLEL_DOWNLOADS> \
  --chunk-size <BYTES> \
  --dry-run
```

| Flag            | Default            | Description                                              |
|-----------------|--------------------|----------------------------------------------------------|
| `--folder-id`   | _(required)_       | Google Drive folder ID to download                       |
| `--output`      | `./drive_download`  | Local directory to write files into                      |
| `--credentials` | `./credentials.json`| Path to OAuth credentials JSON                           |
| `--workers`     | `4`                | Number of parallel download threads                      |
| `--chunk-size`  | `10485760` (10 MB) | Chunk size in bytes for streamed downloads               |
| `--dry-run`     | `false`            | List files that would be downloaded without downloading   |
| `--log-level`   | `INFO`             | Logging verbosity: DEBUG, INFO, WARNING, ERROR           |

---

## Parallelism

- Use `concurrent.futures.ThreadPoolExecutor` with `--workers` threads
- Folder traversal runs single-threaded first to build the full file tree
- Downloads are dispatched to the thread pool after traversal completes
- Each thread gets its own `httplib2.Http` instance (not thread-safe otherwise)
- The manifest is updated with a threading lock after each file completes

---

## Logging

Use Python `logging` module with structured output:

```
2026-04-29 10:01:05 INFO  [1/342] Downloading: Reports/Q1/summary.docx (240 KB)
2026-04-29 10:01:06 INFO  [1/342] Completed:   Reports/Q1/summary.docx (240 KB, 1.2s)
2026-04-29 10:01:07 WARN  [5/342] Skipped:     Forms/survey (unsupported type: application/vnd.google-apps.form)
2026-04-29 10:01:10 ERROR [12/342] Failed:      Data/big_export.xlsx (export exceeded 10MB limit)
```

At the end of a run, print a summary:

```
Download complete: 330 succeeded, 4 skipped, 8 failed (see manifest.json for details)
```

---

## Error Handling

| Error                         | Action                                                    |
|-------------------------------|-----------------------------------------------------------|
| `401 Unauthorized`            | Refresh token; if refresh fails, re-run auth flow         |
| `403 Rate Limit Exceeded`     | Exponential backoff + retry                               |
| `403 Forbidden`               | Log "no access" warning, mark as `skipped`                |
| `404 Not Found`               | Log warning, mark as `skipped` (file may have been deleted)|
| `416 Range Not Satisfiable`   | Restart download from byte 0                              |
| `500 / 503 Server Error`      | Exponential backoff + retry (max 5 attempts)              |
| Export > 10 MB                | Log warning, mark as `failed`                             |
| Network timeout               | Retry with backoff                                        |
| Disk full                     | Catch `OSError`, abort gracefully, save manifest          |
| Filename conflicts            | Append `_1`, `_2`, etc. to the local filename             |

---

## File Structure

```
gdrive_download/
├── gdrive_download.py       # CLI entry point
├── auth.py                  # OAuth flow + token management
├── traversal.py             # Recursive folder listing
├── downloader.py            # Binary download + Workspace export
├── manifest.py              # Manifest read/write/resume logic
├── rate_limiter.py          # Backoff + throttle utilities
├── requirements.txt
└── README.md
```

---

## Testing Notes

- Use a dedicated test folder in Google Drive with known file types and sizes
- Include at least one Google Doc, Sheet, Slide, and Drawing for export coverage
- Include a file > 100 MB to validate chunked downloads
- Include a deeply nested folder (5+ levels) to validate recursion
- Test resume by interrupting a download mid-run and re-running
- Mock the Drive API with `unittest.mock` or `responses` library for unit tests

---

## Open Questions

1. **Shared Drive support** — Should the tool handle Shared Drives (requires `supportsAllDrives=true` and `includeItemsFromAllDrives=true` on API calls)?
2. **Shortcut resolution** — Should `application/vnd.google-apps.shortcut` files resolve to their target and download, or be skipped?
3. **Alternative export formats** — Should users be able to override the default export mapping (e.g., export Docs as PDF instead of DOCX)?
4. **Progress bar** — Add `tqdm` or `rich` progress bars for interactive use?
