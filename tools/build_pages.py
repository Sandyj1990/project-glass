"""Generate static HTML pages for the Impetus design portfolio surfaces.

Reads:
  - images/index.json       (linesheet brands + images)
  - data/photoshoots.json   (4 shoots)
  - data/videos.json        (29 videos)
  - reports under ~/Documents/work/trend-engine/reports/*-india/output/*.pdf

Writes:
  - impetus/brands/<slug>/index.html         (7 brand pages)
  - impetus/photoshoots/index.html
  - impetus/photoshoots/<slug>/index.html    (4 photoshoot pages, 3 layouts)
  - pixelbin/videos/index.html
  - pixelbin/videos/<slug>/index.html        (29 video embeds)
  - impetus/category-intel/index.html
  - impetus/category-intel/<slug>/index.html (4 PDF embed pages)
  - impetus/explore/index.html
  - impetus/about/index.html

Run:  .venv/bin/python tools/build_pages.py
"""

from __future__ import annotations

import html
import json
import re
import shutil
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE_ROOT = ROOT
IMAGES_INDEX = ROOT / "images" / "index.json"
PHOTOSHOOTS_INDEX = ROOT / "data" / "photoshoots.json"
VIDEOS_INDEX = ROOT / "data" / "videos.json"
TREND_ENGINE_REPORTS = Path.home() / "Documents/work/trend-engine/reports"

VERSION = "v0.7"

# CDN base for assets (images + PDFs). Files live under <CDN_BASE>/images/...
# and <CDN_BASE>/pdfs/.... Set to empty string for local-dev-only mode.
CDN_BASE = "https://socialassets.impetusz0.de/rrl-portfolio"


def cdn_image(path: str) -> str:
    """Return the public URL for an image under images/."""
    if CDN_BASE:
        return f"{CDN_BASE}/images/{path}"
    return f"/images/{path}"


def cdn_pdf(path: str) -> str:
    """Return the public URL for a report PDF (relative to the pdfs/ root)."""
    if CDN_BASE:
        return f"{CDN_BASE}/pdfs/{path}"
    return f"/impetus/category-intel/_pdfs/{path}"

# Brand display names
LINESHEET_BRAND_NAMES = {
    "ajio": "AJIO",
    "john-players-jeans": "John Players Jeans",
    "kg-frendz": "KG Frendz",
    "lee-cooper-kids": "Lee Cooper Kids",
    "rio": "Rio",
    "superdry": "Superdry",
    "_unsorted": "Cross-brand · Rio / Fig / DNMX",
}

PHOTOSHOOT_BRAND_NAMES = {
    "asos": "ASOS",
    "trends": "Reliance Trends",
    "buda-jeans": "Buda Jeans",
}

VIDEO_BRAND_NAMES = {
    "reliance-jewels": "Reliance Jewels",
    "metro-wholesale": "Metro Wholesale",
    "swadesh": "Swadesh",
    "satya-paul": "Satya Paul",
    "nmacc": "NMACC",
    "reliance-digital": "Reliance Digital",
    "jiomart": "JioMart",
    "dnmx": "DNMX",
    "superdry": "Superdry",
}

PLATFORM_LABELS = {
    "youtube-long": "YouTube",
    "youtube-shorts": "YouTube Shorts",
    "instagram-reel": "Instagram Reel",
    "instagram-post": "Instagram",
}

REPORT_DEFS = [
    {
        "slug": "mens-polos-aw26-india",
        "title": "Men's Polos · AW26 · India",
        "season": "AW26",
        "gender": "mens",
        "category": "Polos",
        "pdfs": [{"label": "Category report", "filename": "mens-polos-aw26-category-report.pdf"}],
    },
    {
        "slug": "mens-shirts-ss27-india",
        "title": "Men's Shirts · SS27 · India",
        "season": "SS27",
        "gender": "mens",
        "category": "Shirts",
        "pdfs": [{"label": "Category report", "filename": "mens-shirts-ss27-category-report.pdf"}],
    },
    {
        "slug": "mens-tshirts-ss27-india",
        "title": "Men's T-Shirts · SS27 · India",
        "season": "SS27",
        "gender": "mens",
        "category": "T-Shirts",
        "pdfs": [{"label": "Category report", "filename": "mens-tshirts-ss27-category-report.pdf"}],
    },
    {
        "slug": "midi-dress-ss27-india",
        "title": "Midi Dress · SS27 · India",
        "season": "SS27",
        "gender": "womens",
        "category": "Dresses",
        "pdfs": [
            {"label": "Category report", "filename": "midi-dress-ss27-category-report.pdf"},
            {"label": "Trend report", "filename": "midi-dress-ss27-trend-report.pdf"},
        ],
    },
]


# ============================================================================
# HTML builders — shared chrome
# ============================================================================

H = html.escape

NAV_LINKS = [
    ("/", "Home", False),
    ("/jcp", "JCP", False),
    ("/impetus", "Impetus", True),
    ("/autonomous", "Autonomous", False),
    ("/granary", "Granary", False),
    ("/samarth", "Samarth", False),
    ("/alp", "ALP", False),
    ("/rcpl", "RCPL", False),
    ("/retail-vista", "Vista", False),
    ("/retail-jarvis", "Jarvis", False),
    ("/forge", "Forge", False),
    ("/organisation", "Org", False),
    ("/culture", "Culture", False),
    ("/catalog", "Catalog", False),
]

PORTFOLIO_SURFACES = [
    ("/impetus/brands", "Brands"),
    ("/impetus/photoshoots", "Photoshoots"),
    ("/impetus/category-intel", "Category Intel"),
]

# PixelBin tab strip (Overview · GlamAR · Videos). Used for the Videos page
# which is built here but lives under /pixelbin since the AI motion is a
# PixelBin sub-product.
PIXELBIN_SURFACES = [
    ("/pixelbin",        "Overview"),
    ("/pixelbin/glamar", "GlamAR"),
    ("/pixelbin/videos", "Videos"),
]


def topnav() -> str:
    items = "".join(
        f'<a href="{H(href)}" class="nav-link{ " active" if active else ""}">{H(label)}</a>'
        for href, label, active in NAV_LINKS
    )
    return f"""
<nav class="topnav"><div class="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
<a href="/" class="flex items-center gap-3">
  <div class="w-7 h-7 rounded-md flex items-center justify-center text-white" style="background: var(--ink);">
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none"><path d="M9 11l3 3 8-8M3 12l3 3 8-8" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"/></svg>
  </div>
  <div class="flex items-center gap-2">
    <span class="font-semibold text-sm" style="color: var(--ink);">Fynd</span>
    <span class="text-xs" style="color: var(--border);">×</span>
    <span class="mono text-xs tracking-widest" style="color: var(--ink); font-weight: 500;">RRVL · JPL</span>
  </div>
</a>
<div class="hidden md:flex items-center gap-0.5" style="font-size: 12px;">{items}</div>
<div class="mono text-xs hidden lg:block" style="color: var(--ink-muted);">{VERSION}</div>
</div></nav>
"""


def subnav(active_path: str) -> str:
    surfaces = PIXELBIN_SURFACES if active_path.startswith("/pixelbin") else PORTFOLIO_SURFACES
    items = []
    for href, label in surfaces:
        cls = "subnav-link active" if active_path == href else "subnav-link"
        items.append(f'<a href="{H(href)}" class="{cls}">{H(label)}</a>')
    return f'<div class="flex flex-wrap gap-2 mb-8">{"".join(items)}</div>'


def crumbs(*parts: tuple[str, str | None]) -> str:
    """parts is a sequence of (label, href_or_None). Last item is current page."""
    bits = []
    for i, (label, href) in enumerate(parts):
        if href and i < len(parts) - 1:
            bits.append(f'<a href="{H(href)}">{H(label)}</a>')
        else:
            bits.append(f'<span style="color: var(--ink);">{H(label)}</span>')
        if i < len(parts) - 1:
            bits.append('<span class="sep">/</span>')
    return f'<div class="crumb mb-6">{" ".join(bits)}</div>'


def footer(last_verified: str = "") -> str:
    return """
<footer class="py-10" style="background: var(--ink); color: white;"><div class="max-w-7xl mx-auto px-6 text-sm" style="opacity: 0.7;">
  <div>© 2026 RRVL · Jio Platforms Limited · Fynd · Strict internal circulation only</div>
</div></footer>
"""


def page_shell(title: str, body: str, extra_styles: str = "", extra_scripts: str = "") -> str:
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{H(title)}</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<script src="/auth.js"></script>
<script src="https://cdn.tailwindcss.com"></script>
<link rel="stylesheet" href="/style.css">
<style>{COMMON_STYLES}{extra_styles}</style>
</head>
<body>
{topnav()}
{body}
{footer()}
{extra_scripts}
</body>
</html>
"""


COMMON_STYLES = """
.subnav-link {
  font-family: 'JetBrains Mono', monospace; font-size: 11px;
  text-transform: uppercase; letter-spacing: 0.04em; color: var(--ink-muted);
  padding: 8px 14px; border-radius: 999px; border: 1px solid var(--border);
  transition: all 0.15s;
}
.subnav-link:hover { border-color: var(--ink); color: var(--ink); }
.subnav-link.active { background: var(--ink); color: white; border-color: var(--ink); }
.filter-chip {
  display: inline-flex; align-items: center; gap: 6px;
  font-family: 'JetBrains Mono', monospace; font-size: 11px;
  text-transform: uppercase; letter-spacing: 0.04em; color: var(--ink-muted);
  padding: 6px 12px; border-radius: 999px; border: 1px solid var(--border);
  background: white; cursor: pointer; user-select: none; transition: all 0.15s;
}
.filter-chip:hover { border-color: var(--ink); color: var(--ink); }
.filter-chip.active { background: var(--ink); color: white; border-color: var(--ink); }
.filter-chip .count { color: inherit; opacity: 0.55; }
.cat-pill {
  display: inline-block; font-family: 'JetBrains Mono', monospace; font-size: 10px;
  text-transform: uppercase; letter-spacing: 0.04em; color: var(--ink-muted);
  padding: 3px 8px; border-radius: 4px; background: var(--bg-soft);
  border: 1px solid var(--border-soft);
}
.lightbox {
  position: fixed; inset: 0; background: rgba(0,0,0,0.92); z-index: 100;
  display: none; align-items: center; justify-content: center; padding: 4vh 4vw;
}
.lightbox.open { display: flex; }
.lightbox img, .lightbox video { max-width: 100%; max-height: 100%; object-fit: contain; }
.lightbox .close {
  position: absolute; top: 18px; right: 22px; color: white; font-size: 32px;
  line-height: 1; cursor: pointer; opacity: 0.7;
}
.lightbox .close:hover { opacity: 1; }
.lightbox .meta {
  position: absolute; bottom: 14px; left: 22px; color: white; opacity: 0.75;
  font-family: 'JetBrains Mono', monospace; font-size: 11px; letter-spacing: 0.04em;
}
/* Video lightbox: iframe sized to its aspect ratio, fits viewport. */
.video-lightbox-frame {
  background: black; border-radius: 8px; overflow: hidden;
  box-shadow: 0 8px 40px rgba(0,0,0,0.4);
}
.video-lightbox-frame.long {
  aspect-ratio: 16/9; width: min(90vw, 1280px); max-height: 86vh;
}
.video-lightbox-frame.shorts {
  aspect-ratio: 9/16; height: min(86vh, 760px); max-width: 90vw;
}
.video-lightbox-frame iframe { width: 100%; height: 100%; border: 0; display: block; }
.image-tile {
  position: relative; background: var(--bg-soft);
  border: 1px solid var(--border); border-radius: 8px; overflow: hidden; cursor: zoom-in;
}
.image-tile img { width: 100%; height: auto; display: block; transition: transform 0.3s; }
.image-tile:hover img { transform: scale(1.02); }
/* When a tile needs uniform sizing (regular grid, not masonry), opt into
   fit-cover. Image fills its container, anchored to top so faces/heads/
   garment necklines stay visible instead of being cropped. */
.image-tile.fit-cover img {
  height: 100%; object-fit: cover; object-position: center top;
}
.image-tile .badge {
  position: absolute; top: 6px; right: 6px;
  font-family: 'JetBrains Mono', monospace; font-size: 10px;
  background: rgba(0,0,0,0.6); color: white; padding: 2px 6px; border-radius: 3px;
  opacity: 0; transition: opacity 0.2s;
}
.image-tile:hover .badge { opacity: 1; }

/* Masonry layout — true Pinterest-style. Lets each tile keep its natural
   aspect ratio so we never crop a design. Columns rebalance on resize. */
.masonry {
  column-gap: 12px;
  /* Column counts mirror Tailwind responsive grid: 2 cols mobile → 6 cols desktop. */
  column-count: 2;
}
@media (min-width: 768px) { .masonry { column-count: 4; } }
@media (min-width: 1024px) { .masonry { column-count: 6; } }
.masonry > .image-tile {
  break-inside: avoid;
  margin-bottom: 12px;
  display: block;
  width: 100%;
}
.video-thumb {
  position: relative; aspect-ratio: 16/9; background: var(--bg-soft);
  border-radius: 8px 8px 0 0; overflow: hidden; border-bottom: 1px solid var(--border);
}
.video-thumb img { width: 100%; height: 100%; object-fit: cover; display: block; }
.video-thumb .play-overlay {
  position: absolute; inset: 0; display: flex; align-items: center; justify-content: center;
  background: linear-gradient(180deg, transparent 60%, rgba(0,0,0,0.4));
  color: white; font-size: 40px; opacity: 0.85;
}
.video-thumb.shorts { aspect-ratio: 9/16; }
.video-thumb.placeholder {
  display: flex; align-items: center; justify-content: center;
  color: var(--ink-soft); font-family: 'JetBrains Mono', monospace; font-size: 11px;
  text-transform: uppercase; letter-spacing: 0.04em;
}
.placeholder-tile {
  background: linear-gradient(135deg, var(--accent-soft), var(--bg-soft));
  display: flex; align-items: center; justify-content: center;
  color: var(--accent); font-family: 'JetBrains Mono', monospace;
  font-size: 13px; font-weight: 500; text-align: center; padding: 12px;
}
.gender-bar { display: flex; height: 4px; border-radius: 2px; overflow: hidden; background: var(--border-soft); }
.gender-bar > span { display: block; height: 100%; }
.g-womens { background: #EC4899; }
.g-mens { background: #3B82F6; }
.g-kids, .g-kids-boys, .g-kids-girls { background: #F59E0B; }
.g-_unknown { background: var(--border); }
"""


# ============================================================================
# Helpers
# ============================================================================


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)
    rel = path.relative_to(ROOT)
    print(f"  wrote {rel}  ({len(content):,} bytes)")


def fmt_num(n: int | float) -> str:
    if n is None:
        return "—"
    if n >= 1000:
        s = f"{n/1000:.1f}".rstrip("0").rstrip(".")
        return s + "k"
    return str(n)


def slug_to_label(s: str) -> str:
    return s.replace("-", " ").replace("_", " ").title()


def gender_legend(mix: dict[str, int]) -> str:
    order = [("womens", "Womens"), ("mens", "Mens"), ("kids", "Kids"),
             ("kids-boys", "Kids · Boys"), ("kids-girls", "Kids · Girls")]
    total = sum(mix.values()) or 1
    parts = []
    for key, label in order:
        if mix.get(key):
            pct = round(mix[key] / total * 100)
            parts.append(f"{label} {pct}%")
    return " · ".join(parts) or "—"


def gender_bar(mix: dict[str, int]) -> str:
    order = ["womens", "mens", "kids", "kids-boys", "kids-girls", "_unknown"]
    total = sum(mix.values()) or 1
    spans = []
    for k in order:
        if mix.get(k):
            spans.append(f'<span class="g-{k}" style="width:{mix[k]/total*100}%"></span>')
    return f'<div class="gender-bar">{"".join(spans)}</div>'


def lightbox_html() -> str:
    return """
<div id="lightbox" class="lightbox" onclick="if(event.target===this)closeLightbox()">
  <span class="close" onclick="closeLightbox()">×</span>
  <img id="lb-img" alt="" />
  <div id="lb-meta" class="meta"></div>
</div>
<script>
function openLightbox(src, meta) {
  document.getElementById('lb-img').src = src;
  document.getElementById('lb-meta').textContent = meta || '';
  document.getElementById('lightbox').classList.add('open');
}
function closeLightbox() { document.getElementById('lightbox').classList.remove('open'); }
document.addEventListener('keydown', e => { if (e.key === 'Escape') closeLightbox(); });
</script>
"""


# ============================================================================
# BRANDS — single PLP filterable by gender × category × brand
# ============================================================================


def build_brands_plp(idx: dict) -> None:
    """Single PLP at /impetus/brands/ replacing both the old card-index and
    the old /impetus/explore/. Filters: gender, category, brand."""
    print("Building brands PLP…")
    write(SITE_ROOT / "impetus" / "brands" / "index.html", build_brands_plp_page(idx))


def build_brands_plp_page(idx: dict) -> str:
    # Build a flat array of unique image records (deduped by sha256).
    # Filter to product designs only — exclude moodboards / trend research /
    # color palettes / overview slides / cover pages (any image without a
    # category_slug AND without a theme_slug is non-product chrome).
    # Lee Cooper Kids' "Range plan" images have theme but no category — they
    # ARE products, so we keep them via the OR condition.
    total_in_idx = 0
    seen = set()
    flat: list[dict] = []
    for brand, b in idx["brands"].items():
        for arr in b["linesheets"].values():
            for r in arr:
                total_in_idx += 1
                if r["sha256"] in seen:
                    continue
                seen.add(r["sha256"])
                if not (r.get("category_slug") or r.get("theme_slug")):
                    continue  # non-product slide (moodboard/cover/etc)
                flat.append({
                    "path": r["path"],
                    "brand": r["brand"],
                    "linesheet": r["linesheet_slug"],
                    "gender": r.get("gender") or "_unknown",
                    "category": r.get("category_slug") or "_unknown",
                    "slide": r["slide_number"],
                    "seq": r["seq_in_slide"],
                    "title": (r.get("slide_title") or "")[:80],
                    "w": r.get("width"),
                    "h": r.get("height"),
                })
    flat.sort(key=lambda r: (r["brand"], r["linesheet"], r["slide"], r["seq"]))

    brand_counts = Counter(r["brand"] for r in flat)
    gender_counts = Counter(r["gender"] for r in flat)
    cat_counts = Counter(r["category"] for r in flat)

    def chips(name: str, counts: Counter, label_map=None) -> str:
        items = [
            f'<button class="filter-chip active" data-{name}="all">All <span class="count">· {sum(counts.values())}</span></button>'
        ]
        for k, n in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])):
            label = (label_map or {}).get(k, k)
            items.append(
                f'<button class="filter-chip" data-{name}="{H(k)}">{H(label)} <span class="count">· {n}</span></button>'
            )
        return "".join(items)

    brand_chips = chips("brand", brand_counts, LINESHEET_BRAND_NAMES)
    gender_chips = chips("gender", gender_counts)
    cat_chips = chips("category", cat_counts)

    # Pre-resolve full image URLs so the inline JS doesn't have to know about CDN.
    js_records = []
    for r in flat:
        js_records.append({
            "u": cdn_image(r["path"]),
            "b": r["brand"],
            "g": r["gender"],
            "c": r["category"],
            "s": r["slide"],
        })

    body = f"""
<section class="pt-16 pb-8 border-b" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
  {crumbs(("Home", "/"), ("Impetus", "/impetus"), ("Brands", None))}
  <div class="section-label mb-3">Impetus · Design Portfolio · single PLP</div>
  <h1 class="display text-5xl md:text-7xl mb-6" style="color: var(--ink);">Brands.</h1>
  <p class="text-lg max-w-3xl mb-8" style="color: var(--ink-muted);">
    Every AI-generated product design produced by the Trend-to-Design Agent for Reliance brands. Filter by gender, category, brand. {len(flat)} designs shown (deduped by sha256; moodboards · color palettes · trend research · overview slides excluded).
  </p>
  {subnav("/impetus/brands")}
</div></section>

<section class="py-8 border-b" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
  <div class="cap-num mb-2">Gender</div>
  <div class="flex flex-wrap gap-2 mb-5" id="gender-chips">{gender_chips}</div>
  <div class="cap-num mb-2">Category</div>
  <div class="flex flex-wrap gap-2 mb-5" id="category-chips">{cat_chips}</div>
  <div class="cap-num mb-2">Brand</div>
  <div class="flex flex-wrap gap-2" id="brand-chips">{brand_chips}</div>
</div></section>

<section class="py-8 border-b" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
  <div class="flex items-baseline justify-between mb-4">
    <div class="cap-num"><span id="result-count">{len(flat)}</span> designs · <button onclick="clearAll()" class="underline">clear filters</button></div>
  </div>
  <div id="grid" class="masonry"></div>
  <p id="empty-state" class="hidden text-center py-12" style="color: var(--ink-muted);">No designs match these filters.</p>
  <div id="paginator" class="hidden text-center py-6">
    <button onclick="loadMore()" class="btn-secondary text-xs" style="padding:8px 16px;">Load more</button>
    <p class="cap-num mt-2"><span id="shown-count">0</span> of <span id="total-count">0</span></p>
  </div>
</div></section>

{lightbox_html()}

<script>
const ALL = {json.dumps(js_records)};
const PAGE_SIZE = 120;
const filters = {{ gender: 'all', category: 'all', brand: 'all' }};
let visible = ALL;
let shown = 0;

function applyFilters() {{
  visible = ALL.filter(r =>
    (filters.gender === 'all' || r.g === filters.gender) &&
    (filters.category === 'all' || r.c === filters.category) &&
    (filters.brand === 'all' || r.b === filters.brand)
  );
  document.getElementById('result-count').textContent = visible.length;
  document.getElementById('empty-state').classList.toggle('hidden', visible.length > 0);
  shown = 0;
  document.getElementById('grid').innerHTML = '';
  renderNext();
}}

function renderNext() {{
  const slice = visible.slice(shown, shown + PAGE_SIZE);
  const html = slice.map(r => {{
    const meta = `${{r.b}} · slide ${{r.s}} · ${{r.c}}`;
    return `<div class="image-tile" onclick='openLightbox(${{JSON.stringify(r.u)}}, ${{JSON.stringify(meta)}})'>` +
           `<img src="${{r.u}}" loading="lazy" alt="${{meta}}" ` +
           `onerror="this.parentElement.style.opacity=0.25;this.style.display='none'" />` +
           `<span class="badge">${{r.b}}</span></div>`;
  }}).join('');
  document.getElementById('grid').insertAdjacentHTML('beforeend', html);
  shown += slice.length;
  const pag = document.getElementById('paginator');
  if (shown < visible.length) {{
    pag.classList.remove('hidden');
    document.getElementById('shown-count').textContent = shown;
    document.getElementById('total-count').textContent = visible.length;
  }} else {{
    pag.classList.add('hidden');
  }}
}}

function loadMore() {{ renderNext(); }}

function bindChipGroup(containerId, key) {{
  const buttons = document.querySelectorAll('#' + containerId + ' .filter-chip');
  buttons.forEach(b => b.addEventListener('click', () => {{
    buttons.forEach(x => x.classList.remove('active'));
    b.classList.add('active');
    filters[key] = b.dataset[key];
    applyFilters();
  }}));
}}

function clearAll() {{
  for (const k in filters) filters[k] = 'all';
  document.querySelectorAll('.filter-chip').forEach(b => {{
    const isAll = Object.values(b.dataset).includes('all');
    b.classList.toggle('active', isAll);
  }});
  applyFilters();
}}

bindChipGroup('gender-chips', 'gender');
bindChipGroup('category-chips', 'category');
bindChipGroup('brand-chips', 'brand');

// Auto-load more on scroll near bottom.
window.addEventListener('scroll', () => {{
  if (shown >= visible.length) return;
  if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 800) renderNext();
}});

applyFilters();
</script>
"""
    return page_shell("Brands · Impetus Design Portfolio", body)


# ============================================================================
# PHOTOSHOOTS — index + detail
# ============================================================================


def build_photoshoots(data: dict) -> None:
    print("Building photoshoots…")
    write(SITE_ROOT / "impetus" / "photoshoots" / "index.html", build_photoshoots_index(data))
    for shoot in data["shoots"]:
        write(
            SITE_ROOT / "impetus" / "photoshoots" / shoot["slug"] / "index.html",
            build_photoshoot_detail(shoot),
        )


def photoshoot_hero(shoot: dict) -> str | None:
    """Pick a hero image from the shoot."""
    if shoot.get("type") == "marketplace-listing":
        for sku in shoot.get("skus", []):
            if sku.get("image"):
                return cdn_image(sku["image"]["path"])
    elif shoot.get("type") == "showcase":
        for ex in shoot.get("examples", []):
            if ex.get("output"):
                return cdn_image(ex["output"]["path"])
    elif shoot.get("type") == "campaign":
        if shoot.get("images"):
            return cdn_image(shoot["images"][0]["path"])
    return None


def build_photoshoots_index(data: dict) -> str:
    cards = []
    for shoot in data["shoots"]:
        slug = shoot["slug"]
        title = shoot["title"]
        brand = shoot.get("brand") or "—"
        brand_label = PHOTOSHOOT_BRAND_NAMES.get(brand, brand)
        marketplace = shoot.get("marketplace", "")
        type_label = (shoot.get("type") or "").replace("-", " ").title()
        # Item count varies per type
        if shoot.get("type") == "marketplace-listing":
            item_count = f'{len(shoot.get("skus", []))} SKUs'
        elif shoot.get("type") == "showcase":
            item_count = f'{len(shoot.get("examples", []))} examples'
        else:
            item_count = f'{len(shoot.get("images", []))} images'

        hero = photoshoot_hero(shoot)
        hero_html = (
            f'<a href="/impetus/photoshoots/{H(slug)}" class="hero" style="display:block;aspect-ratio:4/5;background:var(--bg-soft);overflow:hidden;border-radius:12px 12px 0 0;border-bottom:1px solid var(--border)">'
            f'<img src="{H(hero)}" loading="lazy" style="width:100%;height:100%;object-fit:cover;object-position:center top;display:block" /></a>'
            if hero
            else f'<a href="/impetus/photoshoots/{H(slug)}" class="hero placeholder-tile" style="aspect-ratio:4/3;border-radius:12px 12px 0 0">No preview</a>'
        )

        cards.append(f"""
<article class="card overflow-hidden">
  {hero_html}
  <div class="p-5">
    <div class="flex items-center gap-2 mb-2">
      <span class="pill pill-live">Live</span>
      <span class="pill">{H(type_label)}</span>
    </div>
    <h3 class="font-semibold text-lg mb-2" style="color: var(--ink);">{H(title)}</h3>
    <div class="cap-num mb-3">Brand · {H(brand_label)}{(' · ' + marketplace.upper()) if marketplace else ''}</div>
    <div class="cap-num mb-4">{H(item_count)}</div>
    <a href="/impetus/photoshoots/{H(slug)}" class="btn-secondary text-xs" style="padding: 8px 16px;">Open →</a>
  </div>
</article>
""")

    body = f"""
<section class="pt-16 pb-12 border-b" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
  {crumbs(("Home", "/"), ("Impetus", "/impetus"), ("Photoshoots", None))}
  <div class="section-label mb-3">Impetus · Design Portfolio · AI Photoshoots · all live</div>
  <h1 class="display text-5xl md:text-7xl mb-6" style="color: var(--ink);">Photoshoots.</h1>
  <p class="text-lg max-w-3xl mb-8" style="color: var(--ink-muted);">
    A curated representative sample of the AI-generated on-model photoshoot work delivered to Reliance brands. Three structural shapes: marketplace listings, showcases, brand campaigns.
  </p>
  {subnav("/impetus/photoshoots")}

  <div class="cap-num mb-3">{data["totals"]["shoots"]} shoots · {data["totals"].get("imagesCollected", "—")} images · representative sample</div>
</div></section>

<section class="py-16 border-b" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
  <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-5">
    {''.join(cards)}
  </div>
</div></section>
"""
    return page_shell("Photoshoots · Impetus Design Portfolio", body)


def build_photoshoot_detail(shoot: dict) -> str:
    type_ = shoot.get("type")
    if type_ == "marketplace-listing":
        return build_photoshoot_marketplace(shoot)
    if type_ == "showcase":
        return build_photoshoot_showcase(shoot)
    return build_photoshoot_campaign(shoot)


def build_photoshoot_marketplace(shoot: dict) -> str:
    slug = shoot["slug"]
    title = shoot["title"]
    brand = PHOTOSHOOT_BRAND_NAMES.get(shoot.get("brand"), shoot.get("brand", ""))
    marketplace = (shoot.get("marketplace") or "").upper()
    stats = shoot.get("stats", {})
    team = shoot.get("team", [])
    skus = shoot.get("skus", [])

    sku_tiles = []
    for sku in skus:
        img_block = ""
        if sku.get("image"):
            src = cdn_image(sku["image"]["path"])
            img_block = (
                f'<div class="image-tile fit-cover" style="aspect-ratio:4/5;cursor:zoom-in" '
                f'onclick=\'openLightbox({json.dumps(src)}, "{H(sku["sku"])} · {H(sku.get("color", ""))}")\'>'
                f'<img src="{H(src)}" loading="lazy" /></div>'
            )
        else:
            img_block = (
                f'<div class="placeholder-tile" style="aspect-ratio:3/4;border-radius:8px;border:1px solid var(--border)">'
                f'Live SKU · view on {marketplace}</div>'
            )
        sku_tiles.append(f"""
<div class="card overflow-hidden">
  {img_block}
  <div class="p-3">
    <div class="cap-num mb-1">{H(sku.get("color", ""))}</div>
    <div class="font-mono text-xs mb-2" style="color: var(--ink-muted);">{H(sku["sku"])}</div>
    <a href="{H(sku["url"])}" target="_blank" rel="noopener" class="text-xs font-medium accent">View on {marketplace} →</a>
  </div>
</div>
""")

    team_html = " · ".join(f"{H(t['name'])} ({H(t.get('role', ''))})" for t in team)

    body = f"""
<section class="pt-16 pb-12 border-b" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
  {crumbs(("Home", "/"), ("Impetus", "/impetus"), ("Photoshoots", "/impetus/photoshoots"), (title, None))}
  <div class="section-label mb-3">Photoshoot · Marketplace listing · Live</div>
  <div class="flex items-center gap-2 mb-4">
    <span class="pill pill-live">Live</span>
    <span class="pill">Marketplace listing</span>
    <span class="pill">{H(brand)}</span>
    <span class="pill">{H(marketplace)}</span>
  </div>
  <h1 class="display text-4xl md:text-6xl mb-6" style="color: var(--ink);">{H(title)}.</h1>
  <p class="text-lg max-w-3xl mb-8" style="color: var(--ink-muted);">{H(shoot.get("summary", ""))}</p>

  <div class="grid grid-cols-2 md:grid-cols-4 gap-3 max-w-4xl mb-6">
    <div class="card p-4"><div class="cap-num mb-1">SKUs live</div><div class="display-2 text-3xl">{stats.get("skusLive", "—")}</div></div>
    <div class="card p-4"><div class="cap-num mb-1">In pipeline</div><div class="display-2 text-3xl">{stats.get("skusInPipeline", "—")}+</div></div>
    <div class="card p-4"><div class="cap-num mb-1">Processing</div><div class="display-2 text-3xl">{stats.get("processingDays", "—")}d</div></div>
    <div class="card p-4"><div class="cap-num mb-1">Time to live</div><div class="display-2 text-3xl">{stats.get("timeToLiveDays", "—")}d</div></div>
  </div>

  <div class="card p-5 max-w-4xl" style="background: var(--accent-soft); border-color: #DDD6FE;">
    <div class="cap-num mb-2" style="color: var(--accent);">Achievement</div>
    <div class="font-medium" style="color: var(--ink);">Consistent plus-size model face across all SKUs · zero manual retouching · fully automated pipeline.</div>
  </div>

  {f'<div class="mt-6 cap-num">Team · {team_html}</div>' if team else ''}
</div></section>

<section class="py-16 border-b" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
  <div class="section-label mb-3">SKUs · {len(skus)} live on {marketplace}</div>
  <h2 class="display-2 text-3xl mb-8" style="color: var(--ink);">Live products.</h2>
  <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4">
    {''.join(sku_tiles)}
  </div>
</div></section>

{lightbox_html()}
"""
    return page_shell(f"{title} · Photoshoots", body)


def build_photoshoot_showcase(shoot: dict) -> str:
    title = shoot["title"]
    brand = PHOTOSHOOT_BRAND_NAMES.get(shoot.get("brand"), shoot.get("brand", ""))
    marketplace = (shoot.get("marketplace") or "").upper()
    stats = shoot.get("stats", {})
    pilot = shoot.get("pilot", {})
    dataset = shoot.get("dataset", {})
    examples = shoot.get("examples", [])
    use_cases = shoot.get("useCases", [])

    use_case_chips = "".join(
        f'<span class="pill">{H(uc)}</span>' for uc in use_cases
    )

    example_rows = []
    for ex in examples:
        style_code = ex.get("styleCode") or ""
        cat = ex.get("category", "")
        note = ex.get("note", "")
        in_block = ""
        if ex.get("input"):
            inp = ex["input"]
            src = cdn_image(inp["path"])
            kind = inp.get("kind", "input")
            in_block = (
                f'<div class="card overflow-hidden">'
                f'<div class="image-tile" style="aspect-ratio: auto; cursor:zoom-in" '
                f'onclick=\'openLightbox({json.dumps(src)}, "INPUT · {H(kind)} · {H(style_code)}")\'>'
                f'<img src="{H(src)}" loading="lazy" style="aspect-ratio:auto;height:auto" /></div>'
                f'<div class="p-3"><div class="cap-num">Input · {H(kind)}</div></div></div>'
            )
        else:
            in_block = (
                '<div class="card placeholder-tile" style="aspect-ratio:1/1">No input shared</div>'
            )

        out = ex.get("output", {})
        out_src = cdn_image(out["path"])
        out_kind = out.get("kind", "output")
        out_block = (
            f'<div class="card overflow-hidden">'
            f'<div class="image-tile fit-cover" style="aspect-ratio:1/1; cursor:zoom-in" '
            f'onclick=\'openLightbox({json.dumps(out_src)}, "OUTPUT · {H(out_kind)} · {H(style_code)}")\'>'
            f'<img src="{H(out_src)}" loading="lazy" /></div>'
            f'<div class="p-3"><div class="cap-num">Output · {H(out_kind)}</div></div></div>'
        )

        example_rows.append(f"""
<div class="mb-10">
  <div class="cap-num mb-2">{H(style_code) if style_code else "Standalone"} · {H(cat)}{' · ' + H(note) if note else ''}</div>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
    {in_block}
    {out_block}
  </div>
</div>
""")

    body = f"""
<section class="pt-16 pb-12 border-b" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
  {crumbs(("Home", "/"), ("Impetus", "/impetus"), ("Photoshoots", "/impetus/photoshoots"), (title, None))}
  <div class="section-label mb-3">Photoshoot · Showcase · Live</div>
  <div class="flex items-center gap-2 mb-4">
    <span class="pill pill-live">Live</span>
    <span class="pill">Showcase</span>
    <span class="pill">{H(brand)}</span>
    <span class="pill">{H(marketplace)}</span>
    <span class="pill">{H(dataset.get("season", ""))}</span>
  </div>
  <h1 class="display text-4xl md:text-6xl mb-6" style="color: var(--ink);">{H(title)}.</h1>
  <p class="text-lg max-w-3xl mb-8" style="color: var(--ink-muted);">{H(shoot.get("summary", ""))}</p>

  <div class="cap-num mb-3">Use cases</div>
  <div class="flex flex-wrap gap-2 mb-8">{use_case_chips}</div>

  <div class="grid grid-cols-2 md:grid-cols-4 gap-3 max-w-4xl">
    <div class="card p-4"><div class="cap-num mb-1">Styles processed</div><div class="display-2 text-3xl">{fmt_num(dataset.get("stylesAnalysed"))}</div></div>
    <div class="card p-4"><div class="cap-num mb-1">Images processed</div><div class="display-2 text-3xl">{fmt_num(dataset.get("imagesAnalysed"))}</div></div>
    <div class="card p-4"><div class="cap-num mb-1">Style acceptance</div><div class="display-2 text-3xl accent">{round((stats.get("styleAcceptanceRate") or 0)*100)}%</div></div>
    <div class="card p-4"><div class="cap-num mb-1">Pilot rendered</div><div class="display-2 text-3xl">{pilot.get("stylesGenerated", "—")}</div></div>
  </div>
</div></section>

<section class="py-16 border-b" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
  <div class="section-label mb-3">Input ↔ Output examples · {len(examples)}</div>
  <h2 class="display-2 text-3xl mb-8" style="color: var(--ink);">From PLM image to live render.</h2>
  {''.join(example_rows)}
</div></section>

{lightbox_html()}
"""
    return page_shell(f"{title} · Photoshoots", body)


def build_photoshoot_campaign(shoot: dict) -> str:
    title = shoot["title"]
    brand = PHOTOSHOOT_BRAND_NAMES.get(shoot.get("brand"), shoot.get("brand", ""))
    marketplace = (shoot.get("marketplace") or "").upper()
    collection = shoot.get("collection", "")
    gender = shoot.get("gender", "")
    images = shoot.get("images", [])

    tiles = []
    for img in images:
        src = cdn_image(img["path"])
        meta = f'{img.get("graphic", "")} · {img.get("colorway", "")}'
        if img.get("licensed"):
            meta += f' · Licensed: {img["licensed"]}'
        tiles.append(f"""
<div class="card overflow-hidden">
  <div class="image-tile fit-cover" style="aspect-ratio: 4/5; cursor:zoom-in"
       onclick='openLightbox({json.dumps(src)}, {json.dumps(meta)})'>
    <img src="{H(src)}" loading="lazy" />
  </div>
  <div class="p-4">
    <div class="cap-num mb-1">{H(img.get("colorway", ""))}{' · LICENSED ' + H(img["licensed"]).upper() if img.get("licensed") else ''}</div>
    <h4 class="font-medium text-sm" style="color: var(--ink);">{H(img.get("graphic", ""))}</h4>
  </div>
</div>
""")

    body = f"""
<section class="pt-16 pb-12 border-b" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
  {crumbs(("Home", "/"), ("Impetus", "/impetus"), ("Photoshoots", "/impetus/photoshoots"), (title, None))}
  <div class="section-label mb-3">Photoshoot · Campaign · Live</div>
  <div class="flex items-center gap-2 mb-4">
    <span class="pill pill-live">Live</span>
    <span class="pill">Campaign</span>
    <span class="pill">{H(brand)}</span>
    <span class="pill">{H(marketplace)}</span>
    {f'<span class="pill">{H(collection)}</span>' if collection else ''}
    {f'<span class="pill">{H(gender)}</span>' if gender else ''}
  </div>
  <h1 class="display text-4xl md:text-6xl mb-6" style="color: var(--ink);">{H(title)}.</h1>
  <p class="text-lg max-w-3xl mb-8" style="color: var(--ink-muted);">{H(shoot.get("summary", ""))}</p>
</div></section>

<section class="py-16 border-b" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
  <div class="section-label mb-3">{len(images)} renders</div>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-5xl">
    {''.join(tiles)}
  </div>
</div></section>

{lightbox_html()}
"""
    return page_shell(f"{title} · Photoshoots", body)


# ============================================================================
# VIDEOS
# ============================================================================


def build_videos(data: dict) -> None:
    print("Building videos…")
    write(SITE_ROOT / "pixelbin" / "videos" / "index.html", build_videos_index(data))
    # No per-video detail pages: the listing plays inline (click thumbnail
    # to swap in an autoplay iframe). Old detail folders are cleaned up by
    # the explicit rm step in main().


def build_videos_index(data: dict) -> str:
    videos = sorted(data["videos"], key=lambda v: (v["brand"], v["title"]))
    by_brand = Counter(v["brand"] for v in videos)

    # Split by orientation. Long-form YouTube = landscape; everything else
    # (YouTube Shorts, Instagram Reels, Instagram posts) = vertical.
    landscape = [v for v in videos if v["platform"] == "youtube-long"]
    vertical = [v for v in videos if v["platform"] != "youtube-long"]

    brand_chips = '<button class="filter-chip active" data-brand="all">All <span class="count">· ' + str(len(videos)) + '</span></button>'
    for brand, n in sorted(by_brand.items()):
        label = VIDEO_BRAND_NAMES.get(brand, brand)
        brand_chips += f'<button class="filter-chip" data-brand="{H(brand)}">{H(label)} <span class="count">· {n}</span></button>'

    def card(v: dict) -> str:
        thumb = v.get("thumbUrl") or ""
        is_shorts = v["platform"] != "youtube-long"
        cls = "video-thumb shorts" if is_shorts else "video-thumb"
        if thumb:
            # YouTube returns 404 on maxresdefault for some uploads
            # (e.g. Metro Catering Video). Fall back to hqdefault, which is
            # always available. onerror=null prevents looping if both fail.
            fallback = (
                f"https://i.ytimg.com/vi/{v['videoId']}/hqdefault.jpg"
                if v["platform"].startswith("youtube")
                else ""
            )
            on_err = (
                f"onerror=\"this.onerror=null;this.src='{fallback}'\""
                if fallback else ""
            )
            thumb_html = (
                f'<div class="{cls}" onclick="playVideo(this)">'
                f'<img src="{H(thumb)}" {on_err} loading="lazy" alt="" />'
                f'<div class="play-overlay">▶</div></div>'
            )
        else:
            blabel = VIDEO_BRAND_NAMES.get(v["brand"], v["brand"])
            thumb_html = (
                f'<div class="{cls} placeholder-tile" onclick="playVideo(this)" '
                f'style="cursor:pointer">{H(blabel.upper())}'
                f'<div class="play-overlay" style="background:none">▶</div></div>'
            )
        plat_label = PLATFORM_LABELS.get(v["platform"], v["platform"])
        brand_label = VIDEO_BRAND_NAMES.get(v["brand"], v["brand"])
        # Build the embed URL with playback params. YouTube auto-selects
        # quality based on iframe size + network, but vq=hd1080 nudges it
        # toward HD when available. modestbranding=1 + iv_load_policy=3 hide
        # YouTube logo + on-video annotations for a cleaner look.
        embed = v["embedUrl"]
        sep = "&" if "?" in embed else "?"
        if v["platform"].startswith("youtube"):
            embed_play = f"{embed}{sep}autoplay=1&rel=0&vq=hd1080&modestbranding=1&iv_load_policy=3&playsinline=1"
        else:
            embed_play = f"{embed}{sep}autoplay=1"
        return f"""
<article class="card overflow-hidden video-card"
  data-brand="{H(v['brand'])}" data-platform="{H(v['platform'])}"
  data-embed="{H(embed_play)}" data-shorts="{'1' if is_shorts else '0'}">
  {thumb_html}
  <div class="p-4">
    <div class="flex items-center gap-2 mb-2">
      <span class="pill">{H(plat_label)}</span>
      <a href="{H(v['url'])}" target="_blank" rel="noopener" class="text-xs accent ml-auto" title="Open on {H(plat_label)}">↗</a>
    </div>
    <h3 class="font-medium text-sm mb-2" style="color: var(--ink);">{H(v['title'])}</h3>
    <div class="cap-num">{H(brand_label)}</div>
  </div>
</article>
"""

    landscape_cards = "".join(card(v) for v in landscape)
    vertical_cards = "".join(card(v) for v in vertical)

    body = f"""
<section class="pt-16 pb-12 border-b" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
  {crumbs(("Home", "/"), ("PixelBin", "/pixelbin"), ("Videos", None))}
  <div class="section-label mb-3">PixelBin · AI Videos · all live</div>
  <h1 class="display text-5xl md:text-7xl mb-6" style="color: var(--ink);">Videos.</h1>
  <p class="text-lg max-w-3xl mb-8" style="color: var(--ink-muted);">
    AI-generated motion delivered for Reliance brands — brand films, ads, reels, product videos. Hosted on YouTube and Instagram, embedded here.
  </p>
  {subnav("/pixelbin/videos")}

  <div class="cap-num mb-3">{len(videos)} videos · {len(by_brand)} brands · {len(landscape)} long-form · {len(vertical)} vertical</div>
</div></section>

<section class="py-10 border-b" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
  <div class="cap-num mb-3">Filter by brand</div>
  <div class="flex flex-wrap gap-2" id="brand-filters">{brand_chips}</div>
</div></section>

<section class="py-12 border-b" id="section-landscape" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
  <div class="section-label mb-3">Long-form · landscape · {len(landscape)}</div>
  <h2 class="display-2 text-2xl md:text-3xl mb-6" style="color: var(--ink);">Long-form films + ads.</h2>
  <div id="grid-landscape" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
    {landscape_cards}
  </div>
  <p class="hidden text-center py-8 cap-num" id="empty-landscape" style="color: var(--ink-muted);">No long-form videos for this filter.</p>
</div></section>

<section class="py-12 border-b" id="section-vertical" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
  <div class="section-label mb-3">Vertical · shorts + reels · {len(vertical)}</div>
  <h2 class="display-2 text-2xl md:text-3xl mb-6" style="color: var(--ink);">Shorts + reels.</h2>
  <div id="grid-vertical" class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-5 gap-5">
    {vertical_cards}
  </div>
  <p class="hidden text-center py-8 cap-num" id="empty-vertical" style="color: var(--ink-muted);">No vertical videos for this filter.</p>
</div></section>

<div id="video-lightbox" class="lightbox" onclick="if(event.target===this)closeVideoLightbox()">
  <span class="close" onclick="closeVideoLightbox()">×</span>
  <div id="video-lightbox-frame" class="video-lightbox-frame long"></div>
</div>

<script>
// YouTube serves a tiny 120x90 placeholder with HTTP 200 (not 404) when
// maxresdefault.jpg doesn't exist for an upload. Detect that by checking
// naturalWidth after load and swap to hqdefault, which is always available.
document.addEventListener('DOMContentLoaded', () => {{
  document.querySelectorAll('.video-card').forEach(card => {{
    const platform = card.dataset.platform || '';
    if (!platform.startsWith('youtube')) return;
    const m = (card.dataset.embed || '').match(/\/embed\/([^?]+)/);
    if (!m) return;
    const fallback = 'https://i.ytimg.com/vi/' + m[1] + '/hqdefault.jpg';
    const img = card.querySelector('img');
    if (!img) return;
    function check() {{
      if (img.naturalWidth > 0 && img.naturalWidth < 200 && img.src !== fallback) {{
        img.src = fallback;
      }}
    }}
    if (img.complete) check(); else img.addEventListener('load', check, {{ once: true }});
  }});
}});

// Click-to-play: open an autoplaying iframe in a centered overlay.
function playVideo(thumbEl) {{
  const card = thumbEl.closest('.video-card');
  const embed = card.dataset.embed;
  const shorts = card.dataset.shorts === '1';
  const frame = document.getElementById('video-lightbox-frame');
  frame.className = 'video-lightbox-frame ' + (shorts ? 'shorts' : 'long');
  frame.innerHTML = `<iframe src="${{embed}}"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
    allowfullscreen></iframe>`;
  document.getElementById('video-lightbox').classList.add('open');
  document.body.style.overflow = 'hidden';
}}
function closeVideoLightbox() {{
  // Empty the iframe container so the video stops playing immediately.
  document.getElementById('video-lightbox-frame').innerHTML = '';
  document.getElementById('video-lightbox').classList.remove('open');
  document.body.style.overflow = '';
}}
document.addEventListener('keydown', e => {{ if (e.key === 'Escape') closeVideoLightbox(); }});
(function() {{
  let curBrand = 'all';
  function applyToSection(gridId, emptyId, sectionId) {{
    const grid = document.getElementById(gridId);
    let visible = 0;
    grid.querySelectorAll('.video-card').forEach(card => {{
      const ok = (curBrand === 'all' || card.dataset.brand === curBrand);
      card.style.display = ok ? '' : 'none';
      if (ok) visible++;
    }});
    document.getElementById(emptyId).classList.toggle('hidden', visible > 0);
    // Hide whole section if grid is empty AND a brand filter is active.
    document.getElementById(sectionId).style.display = (visible === 0 && curBrand === 'all') ? '' : '';
  }}
  function apply() {{
    applyToSection('grid-landscape', 'empty-landscape', 'section-landscape');
    applyToSection('grid-vertical',  'empty-vertical',  'section-vertical');
  }}
  document.querySelectorAll('#brand-filters .filter-chip').forEach(b => b.addEventListener('click', () => {{
    document.querySelectorAll('#brand-filters .filter-chip').forEach(x => x.classList.remove('active'));
    b.classList.add('active'); curBrand = b.dataset.brand; apply();
  }}));
}})();
</script>
"""
    return page_shell("Videos · Impetus Design Portfolio", body)


# build_video_detail removed — videos play inline on the listing now.


# ============================================================================
# CATEGORY INTEL
# ============================================================================


def build_category_intel() -> None:
    print("Building category-intel…")
    # Copy PDFs to public location.
    pdf_root = SITE_ROOT / "impetus" / "category-intel" / "_pdfs"
    pdf_root.mkdir(parents=True, exist_ok=True)
    for r in REPORT_DEFS:
        src_dir = TREND_ENGINE_REPORTS / r["slug"] / "output"
        for pdf in r["pdfs"]:
            src = src_dir / pdf["filename"]
            if src.exists():
                dst = pdf_root / r["slug"] / pdf["filename"]
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
                pdf["bytes"] = src.stat().st_size
                pdf["servedAt"] = cdn_pdf(f"{r['slug']}/{pdf['filename']}")
                print(f"  cached {pdf['filename']} ({pdf['bytes']//1024} KB) → {pdf['servedAt']}")
            else:
                pdf["servedAt"] = None
                pdf["bytes"] = 0
                print(f"  MISSING: {src}")

    write(SITE_ROOT / "impetus" / "category-intel" / "index.html", build_category_intel_index())
    for r in REPORT_DEFS:
        write(
            SITE_ROOT / "impetus" / "category-intel" / r["slug"] / "index.html",
            build_category_intel_detail(r),
        )


def build_category_intel_index() -> str:
    cards = []
    for r in REPORT_DEFS:
        total_bytes = sum((p.get("bytes") or 0) for p in r["pdfs"])
        size_mb = total_bytes / 1024 / 1024
        cards.append(f"""
<article class="card overflow-hidden card-hover">
  <div class="p-6">
    <div class="flex items-center gap-2 mb-3">
      <span class="pill pill-live">Live</span>
      <span class="pill">{H(r["season"])}</span>
      <span class="pill">{H(r["gender"])}</span>
      <span class="pill">India</span>
    </div>
    <h3 class="font-semibold text-xl mb-2" style="color: var(--ink);">{H(r["title"])}</h3>
    <div class="cap-num mb-2">Category · {H(r["category"])}</div>
    <div class="cap-num mb-4">{len(r["pdfs"])} PDF{'' if len(r["pdfs"]) == 1 else 's'} · {size_mb:.1f} MB total</div>
    <a href="/impetus/category-intel/{H(r["slug"])}" class="btn-secondary text-xs" style="padding: 8px 16px;">Open PDF →</a>
  </div>
</article>
""")

    body = f"""
<section class="pt-16 pb-12 border-b" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
  {crumbs(("Home", "/"), ("Impetus", "/impetus"), ("Category Intel", None))}
  <div class="section-label mb-3">Impetus · Design Portfolio · Category Intelligence · India only</div>
  <h1 class="display text-5xl md:text-7xl mb-6" style="color: var(--ink);">Category Intel.</h1>
  <p class="text-lg max-w-3xl mb-8" style="color: var(--ink-muted);">
    Published trend reports for the India market — runway-to-retail signals, fabric direction, color palettes, capsule concepts. PDFs sourced from the trend-engine.
  </p>
  {subnav("/impetus/category-intel")}

  <div class="cap-num mb-3">{len(REPORT_DEFS)} reports · India market</div>
</div></section>

<section class="py-16 border-b" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
  <div class="grid md:grid-cols-2 gap-5">
    {''.join(cards)}
  </div>
</div></section>
"""
    return page_shell("Category Intel · Impetus Design Portfolio", body)


def build_category_intel_detail(r: dict) -> str:
    pdfs = r["pdfs"]
    available = [p for p in pdfs if p.get("servedAt")]

    if not available:
        embed = '<div class="card p-12 text-center" style="color: var(--ink-muted);">PDF not yet available.</div>'
    elif len(available) == 1:
        p = available[0]
        embed = f"""
<div class="card overflow-hidden" style="height: 80vh;">
  <iframe src="{H(p['servedAt'])}" style="width:100%;height:100%;border:0;"></iframe>
</div>
<div class="mt-4 flex items-center gap-3">
  <a href="{H(p['servedAt'])}" download class="btn-secondary text-xs" style="padding:8px 16px;">Download PDF</a>
  <a href="{H(p['servedAt'])}" target="_blank" rel="noopener" class="text-xs accent">Open in new tab →</a>
</div>
"""
    else:
        # Tabs
        tabs = ""
        panels = ""
        for i, p in enumerate(available):
            active_tab = "active" if i == 0 else ""
            active_panel = "" if i == 0 else "hidden"
            tabs += f'<button class="subnav-link {active_tab}" data-tab="{i}" onclick="showTab({i})">{H(p["label"])}</button>'
            panels += f"""
<div class="tab-panel {active_panel}" data-panel="{i}">
  <div class="card overflow-hidden" style="height: 80vh;">
    <iframe src="{H(p['servedAt'])}" style="width:100%;height:100%;border:0;"></iframe>
  </div>
  <div class="mt-4 flex items-center gap-3">
    <a href="{H(p['servedAt'])}" download class="btn-secondary text-xs" style="padding:8px 16px;">Download PDF</a>
    <a href="{H(p['servedAt'])}" target="_blank" rel="noopener" class="text-xs accent">Open in new tab →</a>
  </div>
</div>
"""
        embed = f"""
<div class="flex flex-wrap gap-2 mb-6" id="report-tabs">{tabs}</div>
{panels}
<script>
function showTab(i) {{
  document.querySelectorAll('#report-tabs .subnav-link').forEach((b, j) => b.classList.toggle('active', j === i));
  document.querySelectorAll('.tab-panel').forEach((p, j) => p.classList.toggle('hidden', j !== i));
}}
</script>
"""

    body = f"""
<section class="pt-16 pb-8 border-b" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
  {crumbs(("Home", "/"), ("Impetus", "/impetus"), ("Category Intel", "/impetus/category-intel"), (r["title"], None))}
  <div class="section-label mb-3">Report · {H(r["season"])} · India</div>
  <div class="flex items-center gap-2 mb-4">
    <span class="pill pill-live">Live</span>
    <span class="pill">{H(r["season"])}</span>
    <span class="pill">{H(r["gender"])}</span>
    <span class="pill">India</span>
    <span class="pill">{H(r["category"])}</span>
  </div>
  <h1 class="display-2 text-3xl md:text-5xl mb-4" style="color: var(--ink);">{H(r["title"])}.</h1>
</div></section>

<section class="py-8 border-b" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
  {embed}
</div></section>
"""
    return page_shell(f"{r['title']} · Category Intel", body)


# ============================================================================
# EXPLORE — REMOVED (merged into BRANDS PLP above)
# ============================================================================


def _unused_build_explore(idx: dict) -> None:
    print("Building explore…")
    write(SITE_ROOT / "impetus" / "explore" / "index.html", build_explore_page(idx))


def build_explore_page(idx: dict) -> str:
    # Build a flat array of unique image records (deduped by sha256).
    seen = set()
    flat: list[dict] = []
    for brand, b in idx["brands"].items():
        for arr in b["linesheets"].values():
            for r in arr:
                if r["sha256"] in seen:
                    continue
                seen.add(r["sha256"])
                flat.append({
                    "path": r["path"],
                    "brand": r["brand"],
                    "linesheet": r["linesheet_slug"],
                    "gender": r.get("gender") or "_unknown",
                    "category": r.get("category_slug") or "_unknown",
                    "slide": r["slide_number"],
                    "seq": r["seq_in_slide"],
                    "title": r.get("slide_title", "")[:80],
                    "w": r.get("width"),
                    "h": r.get("height"),
                })
    # Sort
    flat.sort(key=lambda r: (r["brand"], r["linesheet"], r["slide"], r["seq"]))

    # Compute filter facets
    brand_counts = Counter(r["brand"] for r in flat)
    gender_counts = Counter(r["gender"] for r in flat)
    cat_counts = Counter(r["category"] for r in flat)

    def chips(name: str, counts: Counter, label_map=None) -> str:
        items = [f'<button class="filter-chip active" data-{name}="all">All <span class="count">· {sum(counts.values())}</span></button>']
        for k, n in sorted(counts.items()):
            label = (label_map or {}).get(k, k)
            items.append(f'<button class="filter-chip" data-{name}="{H(k)}">{H(label)} <span class="count">· {n}</span></button>')
        return "".join(items)

    brand_chips_html = chips("brand", brand_counts, LINESHEET_BRAND_NAMES)
    gender_chips_html = chips("gender", gender_counts)
    cat_chips_html = chips("category", cat_counts)

    body = f"""
<section class="pt-16 pb-8 border-b" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
  {crumbs(("Home", "/"), ("Impetus", "/impetus"), ("Explore", None))}
  <div class="section-label mb-3">Impetus · Design Portfolio · PLP-style explorer</div>
  <h1 class="display text-5xl md:text-7xl mb-6" style="color: var(--ink);">Explore.</h1>
  <p class="text-lg max-w-3xl mb-8" style="color: var(--ink-muted);">
    Filter the entire deduped design catalog by gender × category × brand. {len(flat)} unique designs.
  </p>
  {subnav("/impetus/explore")}
</div></section>

<section class="py-8 border-b" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
  <div class="cap-num mb-2">Gender</div>
  <div class="flex flex-wrap gap-2 mb-5" id="gender-chips">{gender_chips_html}</div>
  <div class="cap-num mb-2">Category</div>
  <div class="flex flex-wrap gap-2 mb-5" id="category-chips">{cat_chips_html}</div>
  <div class="cap-num mb-2">Brand</div>
  <div class="flex flex-wrap gap-2" id="brand-chips">{brand_chips_html}</div>
</div></section>

<section class="py-8 border-b" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
  <div class="flex items-baseline justify-between mb-4">
    <div class="cap-num"><span id="result-count">{len(flat)}</span> designs · 5 filters available · <button onclick="clearAll()" class="underline">clear</button></div>
  </div>
  <div id="grid" class="masonry"></div>
  <p id="empty-state" class="hidden text-center py-12" style="color: var(--ink-muted);">No designs match these filters.</p>
</div></section>

{lightbox_html()}

<script>
const ALL = {json.dumps(flat)};
const filters = {{ gender: 'all', category: 'all', brand: 'all' }};
function applyFilters() {{
  const grid = document.getElementById('grid');
  const visible = ALL.filter(r =>
    (filters.gender === 'all' || r.gender === filters.gender) &&
    (filters.category === 'all' || r.category === filters.category) &&
    (filters.brand === 'all' || r.brand === filters.brand)
  );
  document.getElementById('result-count').textContent = visible.length;
  document.getElementById('empty-state').classList.toggle('hidden', visible.length > 0);
  // Render up to 200 at once; lazy-load the rest via simple pagination on scroll.
  const html = visible.slice(0, 400).map(r => {{
    const meta = `${{r.brand}} · slide ${{r.slide}} · ${{r.category}}`;
    const src = '/images/' + r.path;
    return `<div class="image-tile" onclick='openLightbox("${{src}}", "${{meta}}")'>` +
           `<img src="${{src}}" loading="lazy" alt="${{meta}}" ` +
           `onerror="this.parentElement.style.opacity=0.3;this.style.display='none'" />` +
           `<span class="badge">${{r.brand}}</span></div>`;
  }}).join('');
  grid.innerHTML = html;
  if (visible.length > 400) {{
    grid.insertAdjacentHTML('afterend', `<p class="text-center cap-num py-6">Showing first 400 of ${{visible.length}}. Refine filters to see more.</p>`);
  }}
}}
function bindChipGroup(containerId, key) {{
  const buttons = document.querySelectorAll('#' + containerId + ' .filter-chip');
  buttons.forEach(b => b.addEventListener('click', () => {{
    buttons.forEach(x => x.classList.remove('active'));
    b.classList.add('active');
    filters[key] = b.dataset[key];
    applyFilters();
  }}));
}}
function clearAll() {{
  for (const k in filters) filters[k] = 'all';
  document.querySelectorAll('.filter-chip').forEach(b => {{
    b.classList.toggle('active', b.dataset[Object.keys(b.dataset)[0]] === 'all');
  }});
  applyFilters();
}}
bindChipGroup('gender-chips', 'gender');
bindChipGroup('category-chips', 'category');
bindChipGroup('brand-chips', 'brand');
applyFilters();
</script>
"""
    return page_shell("Explore · Impetus Design Portfolio", body)


# ============================================================================
# Cross-link from existing /impetus/index.html
# ============================================================================

DESIGN_PORTFOLIO_BLOCK = """
<!-- DESIGN_PORTFOLIO_LINK -->
<section class="py-16 border-b" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
<div class="section-label mb-3">Design portfolio · live · explore the work</div>
<h2 class="display-2 text-3xl md:text-4xl mb-8" style="color: var(--ink);">What Trend-to-Design has shipped.</h2>
<p class="text-lg max-w-3xl mb-8" style="color: var(--ink-muted);">Every linesheet, photoshoot, video, and category-intel report produced by the Impetus Trend-to-Design pipeline. Filter the design library by brand, gender, category — or open the AI photoshoots, videos, or India trend reports.</p>
<div class="grid md:grid-cols-2 lg:grid-cols-4 gap-4">
<a href="/impetus/brands" class="card card-hover p-5 block"><div class="cap-num mb-2">01 · BRANDS</div><h3 class="font-semibold mb-1">PLP · all designs</h3><p class="text-sm" style="color: var(--ink-muted);">876 unique · gender × category × brand</p></a>
<a href="/impetus/photoshoots" class="card card-hover p-5 block"><div class="cap-num mb-2">02 · PHOTOSHOOTS</div><h3 class="font-semibold mb-1">AI on-model shoots</h3><p class="text-sm" style="color: var(--ink-muted);">4 shoots · representative sample</p></a>
<a href="/pixelbin/videos" class="card card-hover p-5 block"><div class="cap-num mb-2">03 · VIDEOS</div><h3 class="font-semibold mb-1">AI-generated motion</h3><p class="text-sm" style="color: var(--ink-muted);">29 videos · 9 brands · now under PixelBin</p></a>
<a href="/impetus/category-intel" class="card card-hover p-5 block"><div class="cap-num mb-2">04 · CATEGORY INTEL</div><h3 class="font-semibold mb-1">Trend reports · India</h3><p class="text-sm" style="color: var(--ink-muted);">4 reports · SS27 · AW26</p></a>
</div>
</div></section>
"""


def link_from_impetus_index() -> None:
    print("Linking from existing /impetus/index.html…")
    path = SITE_ROOT / "impetus" / "index.html"
    text = path.read_text()
    if "DESIGN_PORTFOLIO_LINK" in text:
        # Replace existing block (idempotent re-runs).
        text = re.sub(
            r"<!-- DESIGN_PORTFOLIO_LINK -->.*?</section>",
            DESIGN_PORTFOLIO_BLOCK.strip(),
            text,
            count=1,
            flags=re.DOTALL,
        )
    else:
        # Insert before the footer.
        marker = "<footer"
        if marker not in text:
            print("  ! couldn't find <footer> in impetus/index.html, skipping")
            return
        text = text.replace(marker, DESIGN_PORTFOLIO_BLOCK + "\n" + marker, 1)
    path.write_text(text)
    print(f"  updated {path.relative_to(ROOT)}")


# ============================================================================
# Main
# ============================================================================


def main() -> None:
    images_idx = json.loads(IMAGES_INDEX.read_text())
    photoshoots = json.loads(PHOTOSHOOTS_INDEX.read_text())
    videos = json.loads(VIDEOS_INDEX.read_text())

    # Sweep stale per-video detail folders (videos now play inline).
    videos_root = SITE_ROOT / "pixelbin" / "videos"
    if videos_root.exists():
        for child in videos_root.iterdir():
            if child.is_dir():
                shutil.rmtree(child)

    build_brands_plp(images_idx)
    build_photoshoots(photoshoots)
    build_videos(videos)
    build_category_intel()
    link_from_impetus_index()
    print("\nDone.")


if __name__ == "__main__":
    main()
