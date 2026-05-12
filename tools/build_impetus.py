"""Generate Impetus sub-platform pages from data/impetus/<slug>.yaml.

Per docs/impetus-restructure-spec.md:
  - Reads data/impetus/<slug>.yaml (one file per platform)
  - Emits impetus/<slug>/index.html using the §3 page template
  - Matches the v0.8.3 mega-menu chrome of the rest of the site

Run:
    .venv/bin/python tools/build_impetus.py            # all
    .venv/bin/python tools/build_impetus.py intelliloom  # one
"""

from __future__ import annotations

import html
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from site_chrome import topnav, footer, subnav_html  # noqa: E402

DATA_DIR = ROOT / "data" / "impetus"
SITE_ROOT = ROOT
VERSION = "v0.8.4"

H = html.escape


def md_inline(text: str) -> str:
    """Tiny inline markdown → HTML. Handles **bold** only (sufficient for the source content)."""
    if not text:
        return ""
    return re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", H(text))


# ============================================================================
# Shared chrome (matches v0.8.3)
# ============================================================================


def page_shell(title: str, body: str) -> str:
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
<style>{LOCAL_STYLES}</style>
</head>
<body>
{topnav()}
{body}
{footer()}
</body>
</html>
"""


LOCAL_STYLES = """
.audience-pills { display: flex; flex-wrap: wrap; gap: 6px; }
.stat-chip {
  display: inline-flex; align-items: center;
  font-family: 'JetBrains Mono', monospace; font-size: 12px; font-weight: 500;
  padding: 6px 12px; border-radius: 999px;
  background: #EEF2FF; color: #3730A3; border: 1px solid #C7D2FE;
}
.improved-callout {
  background: #ECFDF5; border-left: 4px solid #16A34A;
  padding: 18px 22px; border-radius: 8px;
  color: var(--ink); font-size: 15px; line-height: 1.55;
}
.improved-callout p { margin: 0 0 12px; }
.improved-callout p:last-child { margin: 0; }
.improved-callout .impact { background: white; padding: 14px 18px; border-radius: 6px; border: 1px solid #BBF7D0; margin-top: 14px; font-size: 14px; }
.improved-callout .impact-label { display: block; font-family: 'JetBrains Mono', monospace; font-size: 10px; text-transform: uppercase; letter-spacing: 0.05em; color: #047857; margin-bottom: 6px; }
.timeline-entry { display: flex; gap: 18px; align-items: flex-start; margin-bottom: 18px; }
.timeline-date {
  flex: 0 0 90px;
  font-family: 'JetBrains Mono', monospace; font-size: 11px; font-weight: 500;
  text-transform: uppercase; letter-spacing: 0.04em;
  background: var(--ink); color: white;
  padding: 6px 10px; border-radius: 4px; text-align: center;
}
.timeline-body { flex: 1; }
.timeline-body h3 { font-weight: 600; margin-bottom: 8px; color: var(--ink); }
.timeline-body ul { list-style: none; padding: 0; }
.timeline-body li { position: relative; padding-left: 16px; margin-bottom: 8px; font-size: 14px; line-height: 1.5; color: var(--ink); }
.timeline-body li::before { content: "·"; position: absolute; left: 4px; color: var(--accent); font-weight: 700; }
.scs-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 8px; }

/* §06 Progress · autonomy bar + workflow rows */
.autonomy-bar { display: grid; grid-template-columns: repeat(6, 1fr); gap: 4px; max-width: 540px; margin: 14px 0 18px; }
.autonomy-cell { padding: 10px 8px; border-radius: 6px; text-align: center; font-family: 'JetBrains Mono', monospace; font-size: 11px; line-height: 1.2; color: white; opacity: 0.32; transition: opacity 0.15s; }
.autonomy-cell.current { opacity: 1; box-shadow: 0 0 0 2px var(--ink); }
.autonomy-cell .lvl { font-weight: 700; font-size: 14px; display: block; }
.autonomy-cell .tag { font-size: 9px; letter-spacing: 0.04em; text-transform: uppercase; opacity: 0.85; }
.alvl-0 { background: #BFD0E5; color: #1E3A5F; }
.alvl-1 { background: #8FAACD; }
.alvl-2 { background: #5E83B5; }
.alvl-3 { background: #2E5D9D; }
.alvl-4 { background: #16407C; }
.alvl-5 { background: #0A2454; }

.lvl-pill { display: inline-flex; align-items: center; gap: 4px; padding: 3px 8px; border-radius: 4px; font-family: 'JetBrains Mono', monospace; font-size: 10.5px; font-weight: 600; letter-spacing: 0.04em; color: white; }
.lvl-pill .arrow { color: var(--ink-muted); font-weight: 400; padding: 0 4px; }

.workflow-row { display: grid; grid-template-columns: 240px 1fr; gap: 16px; padding: 14px 0; border-top: 1px solid var(--border); align-items: start; }
.workflow-row:first-child { border-top: none; }
.workflow-row .wf-head { font-size: 13px; }
.workflow-row .wf-name { font-weight: 600; color: var(--ink); margin-bottom: 6px; font-size: 14px; }
.workflow-row .wf-tag { font-family: 'JetBrains Mono', monospace; font-size: 10px; color: var(--ink-muted); margin-bottom: 6px; }
.workflow-row .wf-pills { display: flex; gap: 4px; align-items: center; margin-bottom: 6px; }
.workflow-row .wf-link { font-size: 11px; color: var(--accent); text-decoration: underline; }
.workflow-row .wf-plan { font-size: 13px; color: var(--ink); line-height: 1.5; padding-top: 2px; }

.quarter-card { padding: 16px 18px; border: 1px solid var(--border); border-radius: 10px; background: var(--bg); }
.quarter-card .qc-eyebrow { font-family: 'JetBrains Mono', monospace; font-size: 10px; letter-spacing: 0.06em; text-transform: uppercase; color: var(--accent); margin-bottom: 8px; }
.quarter-card .qc-title { font-weight: 700; font-size: 16px; color: var(--ink); margin-bottom: 6px; }
.quarter-card .qc-body { font-size: 13px; color: var(--ink); line-height: 1.5; }

/* Sub-sections (Cortex AI features etc.) + sidebar callouts */
.subsection { padding: 24px 0; border-top: 1px solid var(--border); }
.subsection:first-child { border-top: none; padding-top: 0; }
.subsection-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 28px; align-items: start; }
@media (max-width: 768px) { .subsection-grid { grid-template-columns: 1fr; } }
.subsection h3 { font-weight: 700; font-size: 22px; color: var(--ink); margin-bottom: 4px; letter-spacing: -0.01em; }
.subsection .ss-tag { font-family: 'JetBrains Mono', monospace; font-size: 10px; letter-spacing: 0.06em; text-transform: uppercase; color: var(--accent); margin-bottom: 12px; }
.subsection .ss-body { font-size: 15px; color: var(--ink); line-height: 1.6; }
.subsection .ss-body p { margin: 0 0 12px; }
.subsection .ss-body p:last-child { margin: 0; }
.subsection .ss-img { border: 1px solid var(--border); border-radius: 8px; overflow: hidden; }
.subsection .ss-img img { width: 100%; height: auto; display: block; }
.subsection .ss-img figcaption { padding: 8px 12px; font-family: 'JetBrains Mono', monospace; font-size: 10px; color: var(--ink-muted); border-top: 1px solid var(--border); background: var(--bg-soft); }

.sidebar-callout { background: var(--bg-soft); border-left: 3px solid var(--accent); padding: 14px 18px; border-radius: 0 8px 8px 0; margin-top: 16px; max-width: 720px; }
.sidebar-callout .sc-tag { font-family: 'JetBrains Mono', monospace; font-size: 10px; letter-spacing: 0.05em; text-transform: uppercase; color: var(--accent); margin-bottom: 6px; }
.sidebar-callout .sc-title { font-weight: 600; font-size: 14px; color: var(--ink); margin-bottom: 4px; }
.sidebar-callout .sc-body { font-size: 13px; color: var(--ink); line-height: 1.55; }
"""


# ============================================================================
# Page renderers
# ============================================================================


def render_audience(audience: list[str]) -> str:
    if not audience:
        return ""
    pills = "".join(f'<span class="pill">{H(a)}</span>' for a in audience)
    return f'<div class="audience-pills mb-4">{pills}</div>'


def render_scale(label: str, items: list[str], caption: str = "") -> str:
    if not items:
        return ""
    chips = "".join(f'<span class="stat-chip">{md_inline(c)}</span>' for c in items)
    cap = (
        f'<p class="text-sm mt-4 max-w-3xl" style="color: var(--ink-muted);">{md_inline(caption)}</p>'
        if caption else ""
    )
    return f"""
<section class="py-12 border-b" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
  <div class="section-label mb-4">03 · {H(label or 'Scale')}</div>
  <div class="scs-grid">{chips}</div>
  {cap}
</div></section>
"""


def render_what_improved(wi: dict | None) -> str:
    if not wi:
        return ""
    body = wi.get("body", "")
    impact = wi.get("expected_metric_impact", "")
    if not body and not impact:
        return ""
    body_html = "".join(f"<p>{md_inline(p)}</p>" for p in body.strip().split("\n\n") if p.strip())
    impact_html = ""
    if impact:
        impact_html = (
            '<div class="impact">'
            '<span class="impact-label">Expected metric impact</span>'
            f'{md_inline(impact)}'
            '</div>'
        )
    return f"""
<section class="py-12 border-b" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
  <div class="section-label mb-4">04 · What improved</div>
  <div class="improved-callout max-w-4xl">
    {body_html}
    {impact_html}
  </div>
</div></section>
"""


def render_updates_shipped(entries: list[dict]) -> str:
    if not entries:
        return ""
    rows = []
    for e in entries:
        bullets = "".join(f"<li>{md_inline(b)}</li>" for b in e.get("bullets", []))
        rows.append(f"""
<div class="timeline-entry">
  <div class="timeline-date">{H(e.get('date', ''))}</div>
  <div class="timeline-body">
    <h3>{md_inline(e.get('heading', ''))}</h3>
    <ul>{bullets}</ul>
  </div>
</div>
""")
    return f"""
<section class="py-12 border-b" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
  <div class="section-label mb-6">05 · Updates shipped (latest first)</div>
  <div class="max-w-4xl">{''.join(rows)}</div>
</div></section>
"""


def render_screenshots(shots: list[dict]) -> str:
    if not shots:
        return ""
    tiles = []
    for s in shots:
        tiles.append(f"""
<div class="card overflow-hidden">
  <img src="{H(s['src'])}" alt="{H(s.get('caption', ''))}" style="width:100%;display:block;border-bottom:1px solid var(--border);" />
  <div class="p-3">
    <div class="cap-num">{md_inline(s.get('caption', ''))}</div>
  </div>
</div>
""")
    return f"""
<section class="py-12 border-b" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
  <div class="section-label mb-4">07 · Screenshots</div>
  <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-5">{''.join(tiles)}</div>
</div></section>
"""


def render_subsections(subs: dict | None) -> str:
    """Optional sub-sectioned block (e.g. Cortex's Command Center / AI Agents / Control Tower / Store Intelligence)."""
    if not subs or not subs.get("items"):
        return ""
    label = subs.get("label", "Features")
    section_num = subs.get("section_num", "03")
    items_html = []
    for it in subs["items"]:
        body_paras = "".join(f"<p>{md_inline(p)}</p>" for p in it.get("body", "").strip().split("\n\n") if p.strip())
        img_block = ""
        if it.get("image"):
            cap = it.get("caption", "")
            cap_html = f'<figcaption>{md_inline(cap)}</figcaption>' if cap else ""
            img_block = f'<figure class="ss-img"><img src="{H(it["image"])}" alt="{H(it.get("heading", ""))}" />{cap_html}</figure>'
        tag = it.get("tag", "")
        tag_html = f'<div class="ss-tag">{H(tag)}</div>' if tag else ""
        text_col = f'{tag_html}<h3>{md_inline(it.get("heading", ""))}</h3><div class="ss-body">{body_paras}</div>'
        if img_block:
            items_html.append(f'<div class="subsection"><div class="subsection-grid"><div>{text_col}</div><div>{img_block}</div></div></div>')
        else:
            items_html.append(f'<div class="subsection"><div>{text_col}</div></div>')
    return f"""
<section class="py-12 border-b" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
  <div class="section-label mb-6">{H(section_num)} · {md_inline(label)}</div>
  <div>{''.join(items_html)}</div>
</div></section>
"""


LEVEL_NAMES = ["Manual", "Assisted", "Augmented", "Intelligent", "Agentic", "Autonomous"]


def render_progress(progress: dict | None) -> str:
    """§06 Progress · path to L3/L4 (per spec §9)."""
    if not progress:
        return ""
    current = progress.get("current_level")
    summary = progress.get("current_summary", "")
    workflows = progress.get("workflows", [])
    quarter = progress.get("this_quarter", [])

    if current is None and not workflows and not quarter:
        return ""

    # Sub-section A · autonomy bar
    bar_html = ""
    if current is not None:
        cells = []
        for i in range(6):
            cls = f"autonomy-cell alvl-{i}" + (" current" if i == current else "")
            cells.append(f'<div class="{cls}"><span class="lvl">L{i}</span><span class="tag">{LEVEL_NAMES[i]}</span></div>')
        bar_html = f"""
<div class="mb-8">
  <h3 class="font-semibold text-base mb-1" style="color: var(--ink);">Where this platform sits today</h3>
  <div class="autonomy-bar">{''.join(cells)}</div>
  {f'<p class="text-sm max-w-3xl" style="color: var(--ink); line-height: 1.55;">{md_inline(summary)}</p>' if summary else ''}
</div>
"""

    # Sub-section B · workflow rows
    wf_html = ""
    if workflows:
        rows = []
        for w in workflows:
            name = w.get("name", "")
            number = w.get("number", "")
            cur = w.get("current")
            tgt = w.get("target")
            plan = w.get("plan", "")
            anchor = number.replace(".", "-") if number else name.lower().replace(" ", "-")
            cur_pill = f'<span class="lvl-pill alvl-{cur}">L{cur} · {LEVEL_NAMES[cur]}</span>' if cur is not None else ""
            tgt_pill = f'<span class="lvl-pill alvl-{tgt}">L{tgt} · {LEVEL_NAMES[tgt]}</span>' if tgt is not None else ""
            arrow = '<span class="arrow">→</span>' if cur is not None and tgt is not None else ''
            rows.append(f"""
<div class="workflow-row">
  <div class="wf-head">
    <div class="wf-name">{H(name)}</div>
    {f'<div class="wf-tag">§ {H(number)}</div>' if number else ''}
    <div class="wf-pills">{cur_pill}{arrow}{tgt_pill}</div>
    <a href="/impetus/autonomy/#matrix-{H(anchor)}" class="wf-link">See in matrix →</a>
  </div>
  <div class="wf-plan">{md_inline(plan)}</div>
</div>
""")
        wf_html = f"""
<div class="mb-8 max-w-5xl">
  <h3 class="font-semibold text-base mb-3" style="color: var(--ink);">Workflows this platform enables</h3>
  {''.join(rows)}
</div>
"""

    # Sub-section C · this quarter cards
    qt_html = ""
    if quarter:
        cards = []
        for c in quarter:
            cards.append(f"""
<div class="quarter-card">
  <div class="qc-eyebrow">{H(c.get('eyebrow', ''))}</div>
  <div class="qc-title">{md_inline(c.get('title', ''))}</div>
  <div class="qc-body">{md_inline(c.get('body', ''))}</div>
</div>
""")
        qt_html = f"""
<div class="max-w-5xl">
  <h3 class="font-semibold text-base mb-3" style="color: var(--ink);">What we'll prove this quarter</h3>
  <div class="grid grid-cols-1 md:grid-cols-3 gap-3">{''.join(cards)}</div>
</div>
"""

    return f"""
<section class="py-12 border-b" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
  <div class="section-label mb-4">06 · Progress · path to L3 / L4</div>
  <p class="text-sm mb-8 max-w-3xl" style="color: var(--ink-muted); line-height: 1.55;">Per the <a href="/impetus/autonomy/" class="accent" style="text-decoration:underline;">Autonomy framework</a>: where this platform sits today, the workflows it enables, and what moves in the next 90 days.</p>
  {bar_html}{wf_html}{qt_html}
</div></section>
"""


def render_output_gallery(gallery: dict | None) -> str:
    """Optional 'Output gallery' CTA block (per spec §6.2 — for AI Photoshoot)."""
    if not gallery or not gallery.get("links"):
        return ""
    cards = []
    for ln in gallery["links"]:
        thumb = f'<img src="{H(ln["thumb"])}" alt="{H(ln.get("title", ""))}" style="width:100%;height:160px;object-fit:cover;display:block;border-radius:8px 8px 0 0;border-bottom:1px solid var(--border);" />' if ln.get("thumb") else ""
        cards.append(f"""
<a href="{H(ln['href'])}" class="card card-hover block" style="overflow:hidden;">
  {thumb}
  <div class="p-4">
    <div class="cap-num mb-1">{H(ln.get('eyebrow', ''))}</div>
    <div class="font-semibold mb-1" style="color: var(--ink);">{md_inline(ln.get('title', ''))}</div>
    <div class="text-sm" style="color: var(--ink-muted);">{md_inline(ln.get('subtitle', ''))}</div>
  </div>
</a>
""")
    label = gallery.get("label", "Output Gallery")
    intro = gallery.get("intro", "")
    intro_html = f'<p class="text-base max-w-3xl mb-6" style="color: var(--ink); line-height: 1.6;">{md_inline(intro)}</p>' if intro else ""
    return f"""
<section class="py-12 border-b" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
  <div class="section-label mb-4">{H(gallery.get('section_num', '08'))} · {md_inline(label)}</div>
  {intro_html}
  <div class="grid grid-cols-1 md:grid-cols-3 gap-4 max-w-5xl">{''.join(cards)}</div>
</div></section>
"""


def render_sources(sources: list[dict]) -> str:
    if not sources:
        return ""
    rows = []
    for s in sources:
        label = H(s.get("label", ""))
        href = s.get("href", "")
        if href:
            rows.append(f'<li>· <a href="{H(href)}" class="accent" style="text-decoration:underline;">{label}</a></li>')
        else:
            rows.append(f'<li>· <span style="color:var(--ink-muted);">{label}</span></li>')
    return f"""
<section class="py-10 border-b" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
  <div class="section-label mb-3">Sources</div>
  <ul class="text-sm space-y-1">{''.join(rows)}</ul>
</div></section>
"""


# ============================================================================
# Main page assembly
# ============================================================================


def build_page(data: dict) -> str:
    slug = data["slug"]
    title = data["title"]
    sub_title = data.get("sub_title", "")
    tagline = data.get("tagline", "")
    status = data.get("status", "live")
    status_label = data.get("status_label", "Live")
    status_class = "pill-live" if status == "live" else "pill-build"

    hero = f"""
<section class="pt-16 pb-10 border-b" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
  <div class="crumb mb-6"><a href="/">Home</a><span class="sep">/</span><a href="/impetus">Impetus</a><span class="sep">/</span><span style="color: var(--ink);">{H(title)}</span></div>
  <div class="section-label mb-3">IMPETUS · {H(slug.upper().replace("-", " "))} · {H(status_label.upper())}</div>
  <h1 class="display text-5xl md:text-7xl mb-4" style="color: var(--ink);">{H(title)}.</h1>
  {f'<p class="text-xl mb-6" style="color: var(--ink-muted);">{H(sub_title)}</p>' if sub_title else ''}
  {f'<p class="text-lg max-w-3xl mb-6" style="color: var(--ink);"><strong>{md_inline(tagline)}</strong></p>' if tagline else ''}
  {render_audience(data.get('audience', []))}
  <div class="flex items-center gap-2">
    <span class="pill {status_class}">{H(status_label)}</span>
  </div>
</div></section>
"""

    what_it_does = data.get("what_it_does", "")
    what_block = ""
    sidebar = data.get("what_it_does_sidebar")
    sidebar_html = ""
    if sidebar and sidebar.get("body"):
        tag_html = f'<div class="sc-tag">{H(sidebar["tag"])}</div>' if sidebar.get("tag") else ""
        title_html = f'<div class="sc-title">{md_inline(sidebar["title"])}</div>' if sidebar.get("title") else ""
        body_html = f'<div class="sc-body">{md_inline(sidebar["body"])}</div>'
        sidebar_html = f'<div class="sidebar-callout">{tag_html}{title_html}{body_html}</div>'
    if what_it_does:
        paras = "".join(f'<p class="text-base mb-4" style="color: var(--ink); line-height: 1.6;">{md_inline(p)}</p>'
                        for p in what_it_does.strip().split("\n\n") if p.strip())
        what_block = f"""
<section class="py-12 border-b" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
  <div class="section-label mb-4">02 · What it does for you</div>
  <div class="max-w-3xl">{paras}</div>
  {sidebar_html}
</div></section>
"""

    # §03 is either chip-strip scale OR sub-sectioned features (per spec §10.1).
    subsections = data.get("subsections")
    if subsections:
        section_03 = render_subsections({**subsections, "section_num": subsections.get("section_num", "03")})
    else:
        section_03 = render_scale(data.get("scale_label", "Scale"), data.get("scale", []), data.get("scale_caption", ""))

    body = (
        hero
        + what_block
        + section_03
        + render_what_improved(data.get("what_improved"))
        + render_updates_shipped(data.get("updates_shipped", []))
        + render_progress(data.get("progress"))
        + render_screenshots(data.get("screenshots", []))
        + render_output_gallery(data.get("output_gallery"))
        + render_sources(data.get("sources", []))
    )

    return page_shell(f"{title} · Impetus", body)


def main() -> None:
    only = sys.argv[1] if len(sys.argv) > 1 else None
    yaml_files = sorted(DATA_DIR.glob("*.yaml"))
    if only:
        yaml_files = [f for f in yaml_files if f.stem == only]
        if not yaml_files:
            print(f"No YAML found for slug: {only}")
            sys.exit(1)

    for yp in yaml_files:
        data = yaml.safe_load(yp.read_text())
        slug = data["slug"]
        out = SITE_ROOT / "impetus" / slug / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(build_page(data))
        print(f"  wrote {out.relative_to(ROOT)}  ({len(out.read_text()):,} bytes)")


if __name__ == "__main__":
    main()
