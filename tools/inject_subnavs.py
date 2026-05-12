"""One-shot: inject per-track subnav chip strips into hub + sub-pages.

Each row in TARGETS is `(html_path, track, active_href)`. The script either
replaces an existing `<div class="flex flex-wrap gap-2 mb-8">…subnav-link…</div>`
strip with the canonical render from site_chrome.subnav_html(), or — if no
existing strip — inserts one immediately after the breadcrumb.

Idempotent. Safe to re-run.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from site_chrome import subnav_html  # noqa: E402

# (relative_path, track, active_href)
TARGETS = [
    # JCP
    ("jcp/index.html",                                              "jcp",     "/jcp"),
    ("jcp/cataloging/index.html",                                   "jcp",     "/jcp/cataloging"),
    ("jcp/7eleven/index.html",                                      "jcp",     "/jcp/7eleven"),
    ("jcp/release-notes/index.html",                                "jcp",     "/jcp/release-notes"),
    # /jcp/channels/index.html is built by build_jcp_channels_page.py and
    # already calls subnav_html("jcp", "/jcp/channels") inline — re-run that
    # script when SUBNAV["jcp"] changes.
    ("rcpl/index.html",                                              "jcp",     "/rcpl"),
    # Granary
    ("granary/index.html",                                          "granary", "/granary"),
    ("granary/research/transforming-retail-forecasting/index.html", "granary", "/granary/research"),
    # Impetus capability galleries
    ("impetus/index.html",          "impetus", "/impetus"),
    ("impetus/brands/index.html",   "impetus", "/impetus/brands"),
    ("impetus/photoshoots/index.html", "impetus", "/impetus/photoshoots"),
    ("impetus/category-intel/index.html", "impetus", "/impetus/category-intel"),
    ("impetus/autonomy/index.html",       "impetus", "/impetus/autonomy"),
    # PixelBin
    ("pixelbin/index.html",         "pixelbin", "/pixelbin"),
    ("pixelbin/glamar/index.html",  "pixelbin", "/pixelbin/glamar"),
    ("pixelbin/videos/index.html",  "pixelbin", "/pixelbin/videos"),
]

EXISTING_STRIP = re.compile(
    r'<div class="flex flex-wrap gap-2 mb-8"><a href="/(?:impetus|jcp|granary|pixelbin)[^"]*" class="subnav-link[^>]*>.*?</div>',
    re.DOTALL,
)
CRUMB = re.compile(r'(<div class="crumb mb-6"[^>]*>.*?</div>)', re.DOTALL)


def patch(path: Path, track: str, active_href: str) -> str:
    text = path.read_text()
    new_strip = subnav_html(track, active_href)
    if EXISTING_STRIP.search(text):
        new_text, n = EXISTING_STRIP.subn(new_strip, text, count=1)
        if new_text == text:
            return "unchanged"
        path.write_text(new_text)
        return "replaced existing strip"
    # No existing subnav — insert after the breadcrumb.
    if not CRUMB.search(text):
        return "no-crumb (manual)"
    new_text, n = CRUMB.subn(rf"\1\n  {new_strip}", text, count=1)
    if new_text == text:
        return "no-change-after-insert"
    path.write_text(new_text)
    return "inserted after crumb"


def main() -> int:
    counts = {}
    for rel, track, active in TARGETS:
        p = ROOT / rel
        if not p.exists():
            print(f"  MISSING                {rel}")
            counts["missing"] = counts.get("missing", 0) + 1
            continue
        result = patch(p, track, active)
        counts[result] = counts.get(result, 0) + 1
        print(f"  {result:25s} {rel}")
    print()
    for k, v in sorted(counts.items()):
        print(f"  {k}: {v}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
