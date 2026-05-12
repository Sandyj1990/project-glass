# gdrive_download

Recursively download a Google Drive folder, exporting Google Workspace files
(Docs/Sheets/Slides/Drawings) to standard formats. Resumable, parallel,
manifest-tracked.

## Install

```bash
cd gdrive_download
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Authenticate (pick one)

### A. OAuth Desktop App (default)

1. Download `credentials.json` from your GCP OAuth client and place it next to
   the script.
2. Run any command — a browser window will open for consent. The token is
   cached in `token.json`.

### B. Service account key

```bash
python -m gdrive_download \
  --folder-id "<URL or ID>" \
  --service-account /path/to/sa-key.json
```

Note: a service account only sees files explicitly shared with its email, or
shared-drives it has been added to.

### C. Application Default Credentials (gcloud)

```bash
# cloud-platform must be included alongside drive.readonly — gcloud requires it.
gcloud auth application-default login \
  --scopes=https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/drive.readonly

python -m gdrive_download --folder-id "<URL or ID>" --use-adc
```

## Usage

```bash
# From the repo root:
python -m gdrive_download \
  --folder-id "https://drive.google.com/drive/folders/1A2B3C..." \
  --output ./out \
  --workers 4

# Dry run — list files only:
python -m gdrive_download --folder-id "<URL>" --dry-run
```

The `--folder-id` flag accepts either a raw Drive folder ID or a full Drive
URL — paste either form.

## Resume

Re-running with the same `--output` directory uses `manifest.json` to skip
already-downloaded files (verified via MD5 for binary files).
