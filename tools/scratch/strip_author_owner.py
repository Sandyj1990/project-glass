#!/usr/bin/env python3
"""
Strip Hero "Author/Date/Version" line and Footer "Owner · ... · v..." line
from every page on the register. Per user feedback (May 2026): page-level
metadata belongs in git history, not on the page itself.

Patterns handled:
  - Hero:  <div class="mb-6"><div class="text-sm" ...><strong>Author:</strong>...
            (and the same inner-div standalone, without the mb-6 wrapper)
  - Footer: <div>Owner · ... · v0.X.Y</div>
            and the surrounding flex container's class list is simplified
            from "flex flex-col md:flex-row justify-between gap-4 text-sm"
            down to just "text-sm" so the remaining copyright line doesn't
            stretch awkwardly.
"""
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]

# --- Hero author lines ---
# Two shapes observed:
#   A. <div class="mb-6"><div class="text-sm" ...><strong>Author:</strong>...</div></div>
#   B. <div class="text-sm" ...><strong>Author:</strong>...</div>
HERO_OUTER_RE = re.compile(
    r'<div class="mb-6">\s*'
    r'<div class="text-sm"[^>]*>\s*<strong>Author:</strong>[^<]*'
    r'(?:<strong>Date:</strong>[^<]*)?'
    r'(?:<strong>Version:</strong>[^<]*)?'
    r'</div>\s*</div>\s*\n?',
    re.DOTALL,
)
HERO_INNER_RE = re.compile(
    r'<div class="text-sm"[^>]*>\s*<strong>Author:</strong>[^<]*'
    r'(?:<strong>Date:</strong>[^<]*)?'
    r'(?:<strong>Version:</strong>[^<]*)?'
    r'</div>\s*\n?',
    re.DOTALL,
)

# --- Footer owner line + parent class simplification ---
FOOTER_BLOCK_RE = re.compile(
    r'(<footer[^>]*>)'
    r'<div class="max-w-7xl mx-auto px-6'
    r' flex flex-col md:flex-row justify-between gap-4 text-sm"'
    r'( style="opacity: 0\.7;")?'
    r'>\s*'
    r'(<div>©[^<]*</div>)\s*'
    r'<div>Owner ·[^<]*</div>\s*'
    r'</div></footer>',
)

REPLACEMENT_FOOTER = (
    r'\1<div class="max-w-7xl mx-auto px-6 text-sm"\2>'
    r'\3'
    r'</div></footer>'
)


def process(path: Path) -> tuple[bool, list[str]]:
    text = path.read_text()
    original = text
    actions: list[str] = []

    # Hero — try outer wrapper first (more specific), then inner-only.
    new = HERO_OUTER_RE.sub('', text)
    if new != text:
        actions.append('hero(outer)')
        text = new
    else:
        new = HERO_INNER_RE.sub('', text)
        if new != text:
            actions.append('hero(inner)')
            text = new

    # Footer
    new = FOOTER_BLOCK_RE.sub(REPLACEMENT_FOOTER, text)
    if new != text:
        actions.append('footer')
        text = new

    if text != original:
        path.write_text(text)
        return True, actions
    return False, []


def main() -> None:
    # Pages we should touch: every .html under repo root *except* scratch / docs / dump folders.
    skip_prefixes = {
        'tools/scratch',
        'docs/',
        '.claude/',
        'node_modules/',
    }
    paths: list[Path] = []
    for p in REPO.rglob('*.html'):
        rel = p.relative_to(REPO).as_posix()
        if any(rel.startswith(pref) for pref in skip_prefixes):
            continue
        paths.append(p)

    changed_count = 0
    for p in sorted(paths):
        rel = p.relative_to(REPO).as_posix()
        changed, actions = process(p)
        if changed:
            changed_count += 1
            print(f'changed  {rel:60s}  [{", ".join(actions)}]')
        # Don't print unchanged files; too noisy.
    print(f'\n{changed_count} of {len(paths)} files modified')


if __name__ == '__main__':
    main()
