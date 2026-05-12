"""One-shot: inject `<meta name="robots" content="noindex, nofollow, ...">`
into every `index.html`'s `<head>`, and strip any `<meta name="description">`
tags. The register is internal-circulation only — these tags are the
defence-in-depth layer behind /robots.txt and the X-Robots-Tag header in
/vercel.json.

Idempotent — running it again leaves already-treated pages byte-equal. Skips
anything under tools/, .git/, .venv/, node_modules/, .vercel/.

Usage:
  python tools/inject_meta_robots.py          # rewrite all pages
  python tools/inject_meta_robots.py --dry    # report what would change
  python tools/inject_meta_robots.py --check  # exit non-zero on drift (CI)
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXCLUDE_DIRS = {".venv", "node_modules", ".git", ".vercel", "tools"}

ROBOTS_TAG = '<meta name="robots" content="noindex, nofollow, noarchive, nosnippet, noimageindex" />'

# Match either viewport or charset meta — we anchor the robots tag right
# after the first one we find.
ANCHOR_RE = re.compile(
    r'(<meta\s+name="viewport"[^>]*/?>|<meta\s+charset="[^"]*"\s*/?>)',
    re.IGNORECASE,
)
EXISTING_ROBOTS_RE = re.compile(
    r'<meta\s+name="robots"[^>]*/?>\s*\n?',
    re.IGNORECASE,
)
DESCRIPTION_RE = re.compile(
    r'<meta\s+name="description"[^>]*/?>\s*\n?',
    re.IGNORECASE,
)


def is_excluded(rel: Path) -> bool:
    return any(part in EXCLUDE_DIRS for part in rel.parts)


def patch(html_path: Path, dry: bool = False) -> tuple[str, bool]:
    text = html_path.read_text()
    original = text

    # Strip any existing robots meta (so we re-inject the canonical one) and
    # any description meta tags.
    text = EXISTING_ROBOTS_RE.sub("", text)
    text = DESCRIPTION_RE.sub("", text)

    # Inject the canonical robots meta right after viewport (preferred) or
    # charset (fallback).
    m = ANCHOR_RE.search(text)
    if not m:
        return ("no-anchor", False)

    insert_at = m.end()
    text = text[:insert_at] + "\n" + ROBOTS_TAG + text[insert_at:]

    if text == original:
        return ("unchanged", False)

    if not dry:
        html_path.write_text(text)
    return ("patched", True)


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--dry", action="store_true", help="report only; no writes")
    p.add_argument("--check", action="store_true", help="report drift and exit non-zero")
    args = p.parse_args()
    if args.check:
        args.dry = True

    targets = [
        p for p in ROOT.rglob("index.html")
        if not is_excluded(p.relative_to(ROOT))
    ]
    root_index = ROOT / "index.html"
    if root_index.exists() and root_index not in targets:
        targets.insert(0, root_index)

    counts = {"patched": 0, "unchanged": 0, "no-anchor": 0}
    for t in sorted(set(targets)):
        result, changed = patch(t, dry=args.dry)
        rel = t.relative_to(ROOT)
        if result == "patched":
            counts["patched"] += 1
            print(f"  patched   {rel}")
        elif result == "no-anchor":
            counts["no-anchor"] += 1
            print(f"  NO-ANCHOR {rel}  (no <meta charset> or <meta viewport> in <head>)")
        else:
            counts["unchanged"] += 1

    print()
    print(f"  patched:   {counts['patched']}")
    print(f"  unchanged: {counts['unchanged']}")
    if counts["no-anchor"]:
        print(f"  no-anchor: {counts['no-anchor']}")
    if args.dry:
        print("\n(dry run — no files written)")
    if args.check and counts["patched"] > 0:
        print(
            f"\nDRIFT DETECTED · {counts['patched']} page(s) lack the canonical "
            f"meta robots tag. Run `python tools/inject_meta_robots.py` to sync."
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
