"""Renderer skeleton for new website sections.

Copy this to tools/build_<section>.py and adapt:
  - Update SECTION_SLUG, SECTION_TITLE, SECTION_LABEL
  - Implement render_page() body for the section's data shape
  - Implement render_index() body for the section's parent index

Reads:   data/<section>/<slug>.yaml × N
Writes:  <section>/<slug>/index.html × N + <section>/index.html

Run:
    .venv/bin/python tools/build_<section>.py            # all
    .venv/bin/python tools/build_<section>.py <slug>     # one

References:
  - tools/build_impetus.py — full-fat working example (574 lines)
  - .claude/skills/website-tone-of-voice — copy register all output strings must pass
"""
from __future__ import annotations

import html
import re
import sys
from pathlib import Path

import yaml

# ============================================================================
# CONFIG · update per section
# ============================================================================

SECTION_SLUG = "<section>"                 # /<section>/...
SECTION_TITLE = "<Section Display Name>"
SECTION_LABEL = "<TRACK NN OR FRONTIER NN> · <SECTION SLUG IN CAPS>"
VERSION = "v0.8.4"

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data" / SECTION_SLUG
SITE_ROOT = ROOT
SECTION_OUT = ROOT / SECTION_SLUG

H = html.escape


def md_inline(text: str) -> str:
    """Tiny inline markdown → HTML. Handles **bold** and *italics*. Sufficient for source content."""
    if not text:
        return ""
    s = H(text)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", s)
    return s


def md_paragraphs(text: str) -> str:
    """Split body text on blank lines, wrap each in <p>."""
    if not text:
        return ""
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    return "\n".join(f"<p>{md_inline(p)}</p>" for p in paragraphs)


def fmt_date(iso: str) -> str:
    """2026-04-07 → 07-Apr-2026."""
    if not iso:
        return ""
    from datetime import datetime
    return datetime.strptime(iso, "%Y-%m-%d").strftime("%d-%b-%Y")


# ============================================================================
# Shared chrome (matches v0.8.4)
# ============================================================================


def topnav() -> str:
    """Top mega-menu nav. Keep in sync with index.html."""
    return f"""
<nav class="topnav"><div class="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center gap-4">
<a href="/" class="flex items-center gap-3 shrink-0">
  <img src="/assets/fynd-logo.png" alt="Fynd" class="w-7 h-7 rounded-md" />
  <div class="hidden sm:flex items-center gap-2">
    <span class="font-semibold text-sm" style="color: var(--ink);">Fynd</span>
    <span class="text-xs" style="color: var(--border);">×</span>
    <span class="mono text-xs tracking-widest" style="color: var(--ink); font-weight: 500;">RRVL · JPL</span>
  </div>
</a>
<div class="hidden md:flex items-center gap-1">
  <a href="/" class="nav-link">Home</a>
  <!-- TODO: paste full Tracks + More mega-menu from tools/build_impetus.py topnav() -->
  <a href="/numbers" class="nav-link">Numbers</a>
</div>
<div class="hidden lg:flex items-center shrink-0">
  <span class="nav-version"><span class="nav-version-dot"></span>{VERSION}</span>
</div>
</div></nav>
"""


def footer(owner_name: str, last_verified: str) -> str:
    return f"""
<footer class="py-16"><div class="max-w-7xl mx-auto px-6">
<div class="grid md:grid-cols-12 gap-8 mb-12">
  <div class="md:col-span-6">
    <a href="/" class="flex items-center gap-3 mb-4">
      <img src="/assets/fynd-logo.png" alt="Fynd" class="w-7 h-7 rounded-md" />
      <div class="flex items-center gap-2">
        <span class="font-semibold text-sm" style="color: var(--ink);">Fynd</span>
        <span class="text-xs" style="color: var(--border);">×</span>
        <span class="mono text-xs tracking-widest" style="color: var(--ink); font-weight: 500;">RRVL · JPL</span>
      </div>
    </a>
    <p class="text-sm max-w-md" style="color: var(--ink-muted);">{H(SECTION_TITLE)} · part of the Fynd × Reliance Retail register.</p>
  </div>
  <div class="md:col-span-3">
    <div class="section-label mb-3">Other tracks</div>
    <ul class="space-y-1 text-sm" style="color: var(--ink);">
      <!-- TODO: paste sibling track list from impetus/index.html footer -->
    </ul>
  </div>
  <div class="md:col-span-3">
    <div class="section-label mb-3">Owner</div>
    <span class="text-sm" style="color: var(--ink);">{H(owner_name)}</span>
    <div class="text-sm mt-1" style="color: var(--ink-muted);">Last verified {H(last_verified)}</div>
  </div>
</div>
<div class="pt-8 border-t flex flex-wrap items-center justify-between gap-4 mono text-xs" style="border-color: var(--border); color: var(--ink-muted);">
  <div>© 2026 RRVL · Jio Platforms Limited · Fynd · Strict internal circulation</div>
  <div>{VERSION}</div>
</div>
</div></footer>
"""


def page(title: str, body: str, owner_name: str = "TBD", last_verified: str = "TBD") -> str:
    """Wrap body in full HTML document. Loads style.css + Tailwind CDN."""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{H(title)}</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<script src="/auth.js"></script>
<script src="https://cdn.tailwindcss.com"></script>
<link rel="icon" type="image/png" href="/assets/fynd-logo.png">
<link rel="stylesheet" href="/style.css">
</head>
<body>
{topnav()}
{body}
{footer(owner_name, last_verified)}
</body>
</html>
"""


# ============================================================================
# Per-page rendering · IMPLEMENT for the section's data shape
# ============================================================================


def render_page(data: dict) -> str:
    """Render one sub-page from one YAML.

    Build the body using the §3 page template from the spec.
    Return the inner-body HTML (page() will wrap chrome).

    See tools/build_impetus.py for a full implementation across ~20 fields.
    """
    slug = data["slug"]
    title = data["title"]
    tagline = data.get("tagline", "")
    status = data.get("status_label", data.get("status", "live"))

    # Hero
    hero = f"""
<section class="pt-16 pb-12 border-b" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
<div class="crumb mb-6"><a href="/">Home</a><span class="sep">/</span><a href="/{SECTION_SLUG}">{H(SECTION_TITLE)}</a><span class="sep">/</span><span style="color: var(--ink);">{H(title)}</span></div>
<div class="section-label mb-3">{H(SECTION_LABEL)} · {H(slug.upper())} · {H(status.upper())}</div>
<h1 class="display text-5xl md:text-7xl mb-6" style="color: var(--ink);">{H(title)}.</h1>
<p class="text-lg max-w-3xl mb-4" style="color: var(--ink-muted);">{md_inline(tagline)}</p>
</div></section>
"""

    # TODO: render §01..§0N from data[...] fields
    # See tools/build_impetus.py:
    #   - render_audience(data)
    #   - render_what_it_does(data)
    #   - render_scale(data)
    #   - render_what_improved(data)
    #   - render_updates(data)
    #   - render_screenshots(data)
    #   - render_progress(data)
    sections = ""

    # ------------------------------------------------------------------------
    # COMMON EMBED PATTERNS (snippets — copy into your render_* helpers)
    # ------------------------------------------------------------------------
    #
    # Inline PDF embed (matches /impetus/category-intel/<report>/ pattern):
    #
    # <div class="card overflow-hidden" style="height: 80vh;">
    #   <iframe src="<PDF_URL>" style="width:100%;height:100%;border:0;"
    #     title="<title>"></iframe>
    # </div>
    # <div class="mt-4 flex items-center gap-3">
    #   <a href="<PDF_URL>" download class="btn-secondary text-xs"
    #      style="padding:8px 16px;">Download PDF (<size>)</a>
    #   <a href="<PDF_URL>" target="_blank" rel="noopener"
    #      class="text-xs accent">Open in new tab →</a>
    # </div>
    #
    # Photo lightbox (anchor wraps the thumb, opens full-size in new tab):
    #
    # <a href="<full-size>" target="_blank">
    #   <img src="<full-size>" alt="<caption>" class="photo-thumb" loading="lazy">
    # </a>
    #
    # Where .photo-thumb is in your <style> block:
    #   width: 100%; aspect-ratio: 4/3; object-fit: cover;
    #   border-radius: 8px; border: 1px solid var(--border);

    return hero + sections


def render_index(all_data: list[dict]) -> str:
    """Render the section index page from all sub-page data.

    Typically a hero with section-level stats + a card grid linking to each sub-page.
    See impetus/index.html for the canonical pattern.
    """
    cards = []
    for d in all_data:
        cards.append(f"""
<a href="/{SECTION_SLUG}/{d['slug']}" class="card platform-card p-5 block">
  <div class="cat">{H(d.get('category', ''))}</div>
  <h3 class="font-semibold text-lg mb-2" style="color: var(--ink);">{H(d['title'])}</h3>
  <p class="text-sm mb-3" style="color: var(--ink-muted);">{md_inline(d.get('tagline', ''))}</p>
  <span class="pill pill-{d.get('status', 'live')}">{H(d.get('status_label', d.get('status', 'Live')))}</span>
</a>
""")

    return f"""
<section class="pt-16 pb-12 border-b" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
<div class="crumb mb-6"><a href="/">Home</a><span class="sep">/</span><span style="color: var(--ink);">{H(SECTION_TITLE)}</span></div>
<div class="section-label mb-3">{H(SECTION_LABEL)} · LIVE</div>
<h1 class="display text-5xl md:text-7xl mb-6" style="color: var(--ink);">{H(SECTION_TITLE)}.</h1>
<!-- TODO: hero subhead (apex-readable, run through website-tone-of-voice) -->
<!-- TODO: stat strip · 4-8 tiles · canonical numbers from data -->
</div></section>

<section class="py-16 border-b" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
{''.join(cards)}
</div>
</div></section>
"""


# ============================================================================
# Main
# ============================================================================


def load_all() -> list[dict]:
    out = []
    for f in sorted(DATA_DIR.glob("*.yaml")):
        with f.open() as fh:
            out.append(yaml.safe_load(fh))
    return out


def write_page(slug: str, html_str: str) -> None:
    out_dir = SECTION_OUT / slug
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "index.html").write_text(html_str, encoding="utf-8")
    print(f"wrote {out_dir.relative_to(ROOT)}/index.html")


def main(argv: list[str]) -> None:
    only = argv[1] if len(argv) > 1 else None
    all_data = load_all()

    for d in all_data:
        if only and d["slug"] != only:
            continue
        html_str = page(
            title=f"{d['title']} · {SECTION_TITLE}",
            body=render_page(d),
            owner_name=d.get("dri", {}).get("name", "TBD"),
        )
        write_page(d["slug"], html_str)

    if not only:
        index_html = page(
            title=SECTION_TITLE,
            body=render_index(all_data),
        )
        SECTION_OUT.mkdir(parents=True, exist_ok=True)
        (SECTION_OUT / "index.html").write_text(index_html, encoding="utf-8")
        print(f"wrote {SECTION_OUT.relative_to(ROOT)}/index.html")


if __name__ == "__main__":
    main(sys.argv)
