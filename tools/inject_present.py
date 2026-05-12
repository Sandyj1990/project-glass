"""Inject the Presentation Mode wiring (`<link rel="stylesheet" href="/present.css">`
and `<script src="/present.js" defer></script>`) into the <head> of every register
page that already loads /style.css.

Idempotent — re-running on already-converted pages is a no-op. Skips files
that don't load /style.css (asset folders, partial fragments, generated
artifacts).

`--check` is the canonical guard. It fails (exit 1) on:
  · DRIFT       a page that loads /style.css but is missing the present.* wiring.
  · NO-SLIDES   a page that's wired but has zero `<section>` direct children of
                <body> (the deck would open empty and the button would be dead).

Usage:
  python tools/inject_present.py          # rewrite all pages
  python tools/inject_present.py --dry    # report what would change
  python tools/inject_present.py --check  # exit non-zero on drift OR no-slides (CI / build gate)
  python tools/inject_present.py --only jcp/index.html [...]
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXCLUDE_DIRS = {".venv", "node_modules", ".git", ".vercel", "tools"}

# The marker we anchor to: every register page imports /style.css in <head>.
STYLE_LINK_RE = re.compile(r'<link rel="stylesheet" href="/style\.css">')
PRESENT_BLOCK = (
    '<link rel="stylesheet" href="/style.css">\n'
    '<link rel="stylesheet" href="/present.css">\n'
    '<script src="/present.js" defer></script>'
)
ALREADY_PRESENT_RE = re.compile(r'<link rel="stylesheet" href="/present\.css">')

# Counts top-level <section> tags. We approximate "direct child of <body>" by
# matching `<section` at column 0 — every register page's sections start at the
# left margin (no indentation), and nested sections are always indented inside
# their parent. Cheap, no HTML parser dep, matches the actual page convention.
TOP_LEVEL_SECTION_RE = re.compile(r'^<section\b', re.MULTILINE)
MIN_SLIDES = 1


def is_excluded(path: Path) -> bool:
    return any(part in EXCLUDE_DIRS for part in path.parts)


def count_slides(text: str) -> int:
    return len(TOP_LEVEL_SECTION_RE.findall(text))


def patch(html_path: Path, dry: bool = False) -> tuple[str, bool, int]:
    """Returns (status, changed, slide_count). slide_count is the post-patch count."""
    text = html_path.read_text()
    if not STYLE_LINK_RE.search(text):
        return ("no-style-link", False, 0)

    slides = count_slides(text)

    if ALREADY_PRESENT_RE.search(text):
        return ("unchanged", False, slides)

    new_text = STYLE_LINK_RE.sub(PRESENT_BLOCK, text, count=1)
    if new_text == text:
        return ("unchanged", False, slides)

    if not dry:
        html_path.write_text(new_text)
    return ("patched", True, slides)


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--dry", action="store_true", help="report only; no writes")
    p.add_argument("--check", action="store_true", help="report drift + no-slides; exit non-zero (CI / build gate)")
    p.add_argument("--only", nargs="*", help="restrict to specific paths (relative to repo root)")
    args = p.parse_args()
    if args.check:
        args.dry = True

    if args.only:
        targets = [ROOT / x for x in args.only]
    else:
        targets = [p for p in ROOT.rglob("index.html") if not is_excluded(p.relative_to(ROOT))]
        root_index = ROOT / "index.html"
        if root_index.exists() and root_index not in targets:
            targets.insert(0, root_index)

    counts = {"patched": 0, "unchanged": 0, "no-style-link": 0, "missing": 0, "no-slides": 0}
    no_slide_pages: list[Path] = []
    for t in sorted(set(targets)):
        if not t.exists():
            print(f"  MISSING            {t.relative_to(ROOT)}")
            counts["missing"] += 1
            continue
        result, _changed, slides = patch(t, dry=args.dry)
        rel = t.relative_to(ROOT)
        if result == "patched":
            counts["patched"] += 1
            print(f"  patched            {rel}")
        elif result == "unchanged":
            counts["unchanged"] += 1
        elif result == "no-style-link":
            counts["no-style-link"] += 1
        # Slide-count guard fires on every wired page (patched or unchanged).
        if result in ("patched", "unchanged") and slides < MIN_SLIDES:
            counts["no-slides"] += 1
            no_slide_pages.append(rel)
            print(f"  no-slides ({slides})    {rel}")

    print()
    print(f"  patched:        {counts['patched']}")
    print(f"  unchanged:      {counts['unchanged']}")
    print(f"  no-style-link:  {counts['no-style-link']}")
    print(f"  no-slides:      {counts['no-slides']}")
    if counts["missing"]:
        print(f"  missing:        {counts['missing']}")
    if args.dry:
        print("\n(dry run — no files written)")

    failed = False
    if args.check and counts["patched"] > 0:
        print(
            f"\nDRIFT DETECTED · {counts['patched']} page(s) missing the "
            f"present.css / present.js wiring.\n"
            "Run `python tools/inject_present.py` to sync."
        )
        failed = True
    if args.check and counts["no-slides"] > 0:
        print(
            f"\nNO-SLIDES DETECTED · {counts['no-slides']} page(s) have the "
            f"present.* wiring but zero top-level <section> elements:"
        )
        for r in no_slide_pages:
            print(f"  · {r}")
        print(
            "\nPresentation Mode treats `<section>` direct children of <body> "
            "as slides. A page with none opens an empty deck and the Present "
            "button becomes a no-op.\n"
            "Fix: structure the page's body as a sequence of top-level <section> "
            "blocks (the register convention), or remove the present.* wiring "
            "if this page genuinely shouldn't be presentable."
        )
        failed = True
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
