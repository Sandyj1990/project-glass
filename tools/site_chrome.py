"""Single source of truth for the site's topnav + footer + per-track subnavs.

Anything that ships nav HTML (page builders, in-place injection scripts)
imports from here. To add a new section, edit the dicts below and rerun
`tools/inject_chrome.py` — the script will rewrite every checked-in
index.html that already has a <nav class="topnav"> block.

Conventions:
  - `href` is the canonical URL (relative to /).
  - `suffix` is an optional grey monospace count/tag rendered next to the link.
  - "Stub" sections (UCP, Boltic, PixelBin, Ratl, Kaily, Fynd Horizon, Autri,
    Dark Factory) point at minimal "Page in progress" placeholders so links
    never 404 even before the real hub page lands.
"""
from __future__ import annotations

VERSION = "v0.8.4"


# ---------------------------------------------------------------------------
# Menu data — Tracks mega-menu, mirrors Farooq's 2026-04-30 letter:
#   Impetus · JCP · UCP · Granary · Special Projects · AI-Native · Recent
# ---------------------------------------------------------------------------

PLATFORMS = [
    {"href": "/impetus", "label": "Impetus",       "suffix": "F&L AI"},
    {"href": "/jcp",     "label": "JCP",           "suffix": "Enterprise Commerce"},
    {"href": "/rcpl",    "label": "RCPL",          "suffix": "FMCG B2B"},
    {"href": "/granary", "label": "Granary",       "suffix": "Grocery AI"},
    {"href": "/ucp",     "label": "UCP & Marketing OS", "suffix": ""},
]

SPECIAL_PROJECTS = [
    {"href": "/alp",           "label": "ALP",           "suffix": ""},
    {"href": "/retail-vista",  "label": "Retail Vista",  "suffix": ""},
    {"href": "/retail-jarvis", "label": "Retail Jarvis", "suffix": ""},
    {"href": "/samarth",       "label": "Samarth",       "suffix": ""},
    {"href": "/forge",         "label": "Forge MES",     "suffix": ""},
    {"href": "/hirefirst",     "label": "HireFirst",     "suffix": "HR Tech"},
    {"href": "/swapeasy",      "label": "SwapEasy",      "suffix": "re-commerce"},
]

AI_NATIVE = [
    {"href": "/agents",       "label": "AI Agents",    "suffix": "directory"},
    {"href": "/boltic",       "label": "Boltic",       "suffix": "automation OS"},
    {"href": "/pixelbin",     "label": "PixelBin",     "suffix": "visual AI"},
    {"href": "/ratl",         "label": "Ratl",         "suffix": "agentic QA"},
    {"href": "/kaily",        "label": "Kaily",        "suffix": "agentic commerce"},
    {"href": "/fynd-konnect", "label": "Fynd Konnect", "suffix": "integration backbone"},
    {"href": "/tms",          "label": "TMS",          "suffix": "quick-commerce OS"},
    {"href": "/kio",          "label": "Kio",          "suffix": "self-checkout"},
]

RECENT_INNOVATIONS = [
    {"href": "/fynd-horizon", "label": "Fynd Horizon", "suffix": ""},
    {"href": "/autri",        "label": "Autri",        "suffix": ""},
    {"href": "/dark-factory", "label": "Dark Factory", "suffix": "Mobile Neo Tailor"},
]

MORE_MENU = [
    {"href": "/autonomous",   "label": "Autonomy framework",   "suffix": "L0–L5"},
    {"href": "/ai-native",    "label": "AI-Native Engineering","suffix": "how Fynd builds"},
    {"href": "/frameworks",   "label": "Frameworks",           "suffix": ""},
    {"href": "/organisation", "label": "Organisation",         "suffix": ""},
    {"href": "/culture",      "label": "Culture",              "suffix": ""},
    {"href": "/fynd-academy", "label": "Fynd Academy",         "suffix": "talent"},
]


# Routes that snap the active state onto a specific top-level chip.
# All other paths default to "Tracks".
MORE_PATHS = {it["href"] for it in MORE_MENU} | {it["href"] + "/" for it in MORE_MENU}


# ---------------------------------------------------------------------------
# Renderers
# ---------------------------------------------------------------------------


def _link(item: dict) -> str:
    suffix_html = (
        f' <span class="mono-suffix">{item["suffix"]}</span>'
        if item.get("suffix") else ""
    )
    return f'<a href="{item["href"]}" class="mega-link">{item["label"]}{suffix_html}</a>'


def _column_links(items: list[dict]) -> str:
    return "\n          ".join(_link(it) for it in items)


def derive_active(path: str) -> str:
    """Return 'tracks' | 'more' for the top-level chip to highlight.

    `path` is the page's URL path (e.g. '/jcp/channels/' or '/organisation/').
    Trailing slashes are tolerated.
    """
    if not path:
        return "tracks"
    norm = path if path.startswith("/") else "/" + path
    # Match against More entries by prefix so /organisation/anything still matches.
    for href in (it["href"] for it in MORE_MENU):
        if norm == href or norm == href + "/" or norm.startswith(href + "/"):
            return "more"
    return "tracks"


def topnav(active: str = "tracks") -> str:
    """Render the global topnav. `active` ∈ {'tracks', 'more'}."""
    tracks_cls = "nav-link active" if active == "tracks" else "nav-link"
    more_cls = "nav-link active" if active == "more" else "nav-link"

    platforms_links = _column_links(PLATFORMS)
    special_links = _column_links(SPECIAL_PROJECTS)
    ai_native_links = _column_links(AI_NATIVE)
    recent_links = _column_links(RECENT_INNOVATIONS)
    more_links = "\n      ".join(_link(it) for it in MORE_MENU)

    chevron = (
        '<svg viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.6" '
        'stroke-linecap="round" stroke-linejoin="round"><polyline points="3 5 6 8 9 5"/></svg>'
    )

    return f"""
<nav class="topnav"><div class="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center gap-4">
<a href="/" class="flex items-center gap-3 shrink-0">
  <img src="https://socialassets.impetusz0.de/rrl-portfolio/assets/fynd-logo.png" alt="Fynd" class="w-7 h-7 rounded-md" />
  <div class="hidden sm:flex items-center gap-2">
    <span class="font-semibold text-sm" style="color: var(--ink);">Fynd</span>
    <span class="text-xs" style="color: var(--border);">×</span>
    <span class="mono text-xs tracking-widest" style="color: var(--ink); font-weight: 500;">RRVL · JPL</span>
  </div>
</a>
<div class="hidden md:flex items-center gap-1">
  <a href="/" class="nav-link">Home</a>
  <div class="nav-mega"><span class="{tracks_cls}" tabindex="0">Tracks {chevron}</span>
    <div class="nav-mega-panel" style="min-width: 720px;">
      <div class="grid grid-cols-3 gap-6">
        <div>
          <div class="mega-col-label">Platforms</div>
          {platforms_links}
        </div>
        <div>
          <div class="mega-col-label">Special Projects</div>
          {special_links}
        </div>
        <div>
          <div class="mega-col-label">AI-Native</div>
          {ai_native_links}
          <div class="mega-col-label" style="margin-top:18px;">Recent Innovations</div>
          {recent_links}
        </div>
      </div>
    </div>
  </div>
  <div class="nav-mega"><span class="{more_cls}" tabindex="0">More {chevron}</span>
    <div class="nav-mega-panel" style="min-width: 280px;">
      {more_links}
    </div>
  </div>
</div>
<div class="hidden lg:flex items-center shrink-0">
  <span class="nav-version"><span class="nav-version-dot"></span>{VERSION}</span>
</div>
</div></nav>
""".strip("\n")


def footer() -> str:
    """Single-line copyright footer.

    The deprecated `Owner · {name} · v{version}` line was dropped from this
    canonical in commit 8763048; the wrapper class is back to plain `text-sm`
    (no flex layout needed for one child). Do not re-add the Owner line — the
    rule is documented in CLAUDE.md and .ai/codebase-map.md.
    """
    return """
<footer class="py-10" style="background: var(--ink); color: white;"><div class="max-w-7xl mx-auto px-6 text-sm" style="opacity: 0.7;">
  <div>© 2026 RRVL · Jio Platforms Limited · Fynd · Strict internal circulation only</div>
</div></footer>
""".strip("\n")


# ---------------------------------------------------------------------------
# Per-track subnav strips. Each track's hub + sub-pages render this just
# below the breadcrumb so users can jump between sub-pages without leaving the
# track. The mega-menu only ever shows the hub link itself — never sub-pages —
# to avoid the duplication that broke the old menu.
# ---------------------------------------------------------------------------

SUBNAV = {
    "jcp": [
        {"href": "/jcp",                "label": "Overview"},
        {"href": "/jcp/channels",       "label": "Channels"},
        {"href": "/jcp/cataloging",     "label": "AI Cataloging"},
        {"href": "/jcp/7eleven",        "label": "7-Eleven"},
        {"href": "/jcp/release-notes",  "label": "Release Notes"},
    ],
    "impetus": [
        {"href": "/impetus",                "label": "Overview"},
        {"href": "/impetus/brands",         "label": "Brands"},
        {"href": "/impetus/category-intel", "label": "Category Intel"},
        # /impetus/photoshoots removed: directory has 4 case-study children
        # but no own index.html — local Python SimpleHTTP serves a directory
        # listing (200), Vercel 404s in production. Re-add once a parent
        # index page is authored. (See docs/audits/wiring-audit-2026-05-03.md C2.)
    ],
    "granary": [
        {"href": "/granary", "label": "Overview"},
        # /granary/research removed: page does not exist on disk; sub-nav
        # was 404ing in production. Re-add when granary/research/index.html
        # is authored. (See docs/audits/wiring-audit-2026-05-03.md C1.)
    ],
    "pixelbin": [
        {"href": "/pixelbin",        "label": "Overview"},
        {"href": "/pixelbin/glamar", "label": "GlamAR"},
        {"href": "/pixelbin/videos", "label": "Videos"},
    ],
}


def derive_track(path: str) -> str | None:
    """Return the SUBNAV key for the page's URL, or None for non-track pages."""
    if not path:
        return None
    norm = path if path.startswith("/") else "/" + path
    if norm.startswith("/jcp"):
        return "jcp"
    if norm.startswith("/impetus"):
        return "impetus"
    if norm.startswith("/granary"):
        return "granary"
    if norm.startswith("/pixelbin"):
        return "pixelbin"
    return None


def subnav_html(track: str, active_href: str = "") -> str:
    """Render the chip strip for a track. `active_href` highlights one chip."""
    items = SUBNAV.get(track, [])
    if not items:
        return ""
    norm_active = active_href.rstrip("/")
    chips = []
    for it in items:
        is_active = it["href"].rstrip("/") == norm_active
        cls = "subnav-link active" if is_active else "subnav-link"
        chips.append(f'<a href="{it["href"]}" class="{cls}">{it["label"]}</a>')
    return f'<div class="flex flex-wrap gap-2 mb-8">{"".join(chips)}</div>'
