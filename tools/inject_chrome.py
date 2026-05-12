"""One-shot: rewrite <nav class="topnav">…</nav> and <footer …>…</footer>
blocks across every checked-in index.html using the canonical chrome from
tools/site_chrome.py.

Idempotent — running it again on already-converted pages leaves them
byte-equal. Skips files that don't have a topnav block (asset folders,
generated artifacts).

Usage:
  python tools/inject_chrome.py          # rewrite all pages
  python tools/inject_chrome.py --dry    # report what would change
  python tools/inject_chrome.py --check  # exit non-zero on drift (CI / pre-commit)
  python tools/inject_chrome.py --only jcp/channels/index.html [...]
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from site_chrome import topnav, footer, derive_active  # noqa: E402

EXCLUDE_DIRS = {".venv", "node_modules", ".git", ".vercel", "tools"}

# These match the entire <nav class="topnav"> ... </nav> and <footer ...> ...
# </footer> blocks. The closing tag is fixed so DOTALL is safe — no nested
# nav/footer in the body.
NAV_RE = re.compile(r'<nav class="topnav">.*?</nav>', re.DOTALL)
FOOTER_RE = re.compile(r'<footer\b[^>]*>.*?</footer>', re.DOTALL)


def page_path_from_file(html_path: Path) -> str:
    """Convert /repo/foo/bar/index.html → '/foo/bar/'. Used for active-state
    derivation."""
    rel = html_path.relative_to(ROOT)
    parts = rel.parts
    if parts == ("index.html",):
        return "/"
    if parts[-1] == "index.html":
        return "/" + "/".join(parts[:-1]) + "/"
    return "/" + "/".join(parts)


def is_excluded(path: Path) -> bool:
    return any(part in EXCLUDE_DIRS for part in path.parts)


def patch(html_path: Path, dry: bool = False) -> tuple[str, bool]:
    text = html_path.read_text()
    if "<nav class=\"topnav\">" not in text:
        return ("no-nav", False)

    page_path = page_path_from_file(html_path)
    new_nav = topnav(active=derive_active(page_path))
    new_footer = footer()

    new_text, n_nav = NAV_RE.subn(new_nav, text, count=1)
    new_text, n_footer = FOOTER_RE.subn(new_footer, new_text, count=1)

    if new_text == text:
        return ("unchanged", False)

    if not dry:
        html_path.write_text(new_text)
    bits = []
    if n_nav:
        bits.append("nav")
    if n_footer:
        bits.append("footer")
    return (f"patched ({'+'.join(bits)})", True)


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--dry", action="store_true", help="report only; no writes")
    p.add_argument("--check", action="store_true", help="report drift and exit non-zero (CI / pre-commit guard)")
    p.add_argument("--only", nargs="*", help="restrict to specific paths (relative to repo root)")
    args = p.parse_args()
    # --check implies --dry (no writes when verifying)
    if args.check:
        args.dry = True

    if args.only:
        targets = [ROOT / x for x in args.only]
    else:
        targets = [p for p in ROOT.rglob("index.html") if not is_excluded(p.relative_to(ROOT))]
        # Also allow patching the root index.html.
        root_index = ROOT / "index.html"
        if root_index.exists() and root_index not in targets:
            targets.insert(0, root_index)

    counts = {"patched": 0, "unchanged": 0, "no-nav": 0, "missing": 0}
    for t in sorted(set(targets)):
        if not t.exists():
            print(f"  MISSING       {t.relative_to(ROOT)}")
            counts["missing"] += 1
            continue
        result, changed = patch(t, dry=args.dry)
        rel = t.relative_to(ROOT)
        if result.startswith("patched"):
            counts["patched"] += 1
            print(f"  {result:25s} {rel}")
        elif result == "unchanged":
            counts["unchanged"] += 1
        elif result == "no-nav":
            counts["no-nav"] += 1

    print()
    print(f"  patched:   {counts['patched']}")
    print(f"  unchanged: {counts['unchanged']}")
    print(f"  no-nav:    {counts['no-nav']}")
    if counts["missing"]:
        print(f"  missing:   {counts['missing']}")
    if args.dry:
        print("\n(dry run — no files written)")
    if args.check and counts["patched"] > 0:
        print(
            f"\nDRIFT DETECTED · {counts['patched']} page(s) diverge from "
            f"the canonical in tools/site_chrome.py.\n"
            "Run `python tools/inject_chrome.py` to sync."
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
