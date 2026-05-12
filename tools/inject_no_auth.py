"""Strip any reference to the legacy client-side `/auth.js` gate from every
HTML page. The gate is now enforced server-side by `middleware.ts` per
docs/glass-security-spec.md (§3.1). Direct edits to a page that re-add the
script tag would silently weaken the security posture, so the build gate
runs `--check` to fail the deploy on any reintroduction.

Idempotent — re-running on already-stripped pages is a no-op.

Usage:
  python tools/inject_no_auth.py          # strip from every HTML
  python tools/inject_no_auth.py --dry    # report what would change
  python tools/inject_no_auth.py --check  # exit non-zero if any HTML still references /auth.js (CI / build gate)
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXCLUDE_DIRS = {"tools", ".venv", "node_modules", ".git", ".vercel", "lib"}

PATTERN = re.compile(
    r'^[ \t]*<script\s+[^>]*src=["\']/auth\.js["\'][^>]*>\s*</script>\s*\n?',
    re.IGNORECASE | re.MULTILINE,
)


def html_files() -> list[Path]:
    out: list[Path] = []
    for p in ROOT.rglob("index.html"):
        if any(part in EXCLUDE_DIRS for part in p.relative_to(ROOT).parts[:-1]):
            continue
        out.append(p)
    return sorted(out)


def has_auth_ref(text: str) -> bool:
    return bool(PATTERN.search(text)) or "/auth.js" in text


def strip(text: str) -> str:
    return PATTERN.sub("", text)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--dry", action="store_true", help="report what would change")
    g.add_argument("--check", action="store_true", help="exit 1 if any HTML still references /auth.js")
    args = ap.parse_args()

    files = html_files()
    offenders: list[Path] = []
    changed: list[Path] = []

    for p in files:
        text = p.read_text(encoding="utf-8")
        if not has_auth_ref(text):
            continue
        if args.check:
            offenders.append(p)
            continue
        new = strip(text)
        if "/auth.js" in new:
            offenders.append(p)
            continue
        if args.dry:
            changed.append(p)
        else:
            p.write_text(new, encoding="utf-8")
            changed.append(p)

    if args.check:
        if offenders:
            print(f"DRIFT · {len(offenders)} file(s) still reference /auth.js — re-run `python tools/inject_no_auth.py` to strip:")
            for p in offenders:
                print(f"  {p.relative_to(ROOT)}")
            return 1
        print(f"OK · 0 of {len(files)} HTML files reference /auth.js")
        return 0

    if offenders:
        print(f"WARN · {len(offenders)} file(s) reference /auth.js in a form this tool can't auto-strip:")
        for p in offenders:
            print(f"  {p.relative_to(ROOT)}")

    verb = "would strip" if args.dry else "stripped"
    print(f"{verb} <script src=/auth.js> from {len(changed)} of {len(files)} HTML files")
    return 1 if offenders else 0


if __name__ == "__main__":
    sys.exit(main())
