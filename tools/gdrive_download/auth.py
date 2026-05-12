"""Authentication for Google Drive API.

Supports three methods (in order of CLI precedence):
  1. Application Default Credentials (--use-adc)
  2. Service Account key file (--service-account)
  3. OAuth Desktop App flow (--credentials, default)
"""

from __future__ import annotations

import os
from pathlib import Path

import google.auth
from google.auth.transport.requests import Request
from google.oauth2 import service_account
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]


def load_oauth_credentials(credentials_path: str, token_path: str = "token.json") -> Credentials:
    creds: Credentials | None = None
    token_file = Path(token_path)

    if token_file.exists():
        creds = Credentials.from_authorized_user_file(str(token_file), SCOPES)

    if creds and creds.valid:
        return creds

    if creds and creds.expired and creds.refresh_token:
        try:
            creds.refresh(Request())
            token_file.write_text(creds.to_json())
            return creds
        except Exception:
            # Refresh failed — fall through to full consent flow.
            pass

    if not Path(credentials_path).exists():
        raise FileNotFoundError(
            f"OAuth credentials not found at {credentials_path}. "
            "Either provide --credentials, --service-account, or --use-adc."
        )

    flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
    creds = flow.run_local_server(port=0)
    token_file.write_text(creds.to_json())
    return creds


def load_service_account_credentials(key_path: str):
    if not Path(key_path).exists():
        raise FileNotFoundError(f"Service account key not found at {key_path}")
    return service_account.Credentials.from_service_account_file(key_path, scopes=SCOPES)


def load_adc_credentials():
    creds, _ = google.auth.default(scopes=SCOPES)
    return creds


def get_credentials(
    use_adc: bool = False,
    service_account_path: str | None = None,
    credentials_path: str = "credentials.json",
    token_path: str = "token.json",
):
    """Resolve credentials per CLI precedence: ADC > service account > OAuth."""
    if use_adc:
        return load_adc_credentials()
    if service_account_path:
        return load_service_account_credentials(service_account_path)
    return load_oauth_credentials(credentials_path, token_path)
