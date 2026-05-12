"""Generate /agents/ index + /agents/<slug>/ detail pages.

Per docs/agents-spec.md v0.4.

Run:
    .venv/bin/python tools/build_agents.py            # all (index + every yaml)
    .venv/bin/python tools/build_agents.py cortex-planning   # one detail page
    .venv/bin/python tools/build_agents.py --index           # just the index
"""

from __future__ import annotations

import html
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from site_chrome import topnav, footer  # noqa: E402

DATA_DIR = ROOT / "data" / "agents"
OUT_DIR = ROOT / "agents"
VERSION = "v0.9.0-agents"

H = html.escape


def md_inline(text: str) -> str:
    if not text:
        return ""
    return re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", H(text))


# ============================================================================
# Local styles · scoped to /agents/ pages
# ============================================================================

LOCAL_STYLES = """
.agent-stat { padding: 14px 16px; border: 1px solid var(--border); border-radius: 10px; background: var(--bg); }
.agent-stat .a-label { font-family: 'JetBrains Mono', monospace; font-size: 10px; letter-spacing: 0.06em; text-transform: uppercase; color: var(--ink-muted); margin-bottom: 6px; }
.agent-stat .a-value { font-weight: 700; font-size: 22px; color: var(--ink); line-height: 1.1; letter-spacing: -0.01em; }
.agent-stat .a-context { font-size: 11px; color: var(--ink-muted); margin-top: 4px; line-height: 1.4; }

.pill { display: inline-flex; align-items: center; padding: 3px 10px; border-radius: 999px; font-family: 'JetBrains Mono', monospace; font-size: 10.5px; font-weight: 600; letter-spacing: 0.04em; }
.pill-live    { background: #DCFCE7; color: #166534; border: 1px solid #BBF7D0; }
.pill-build   { background: #FEF3C7; color: #92400E; border: 1px solid #FDE68A; }
.pill-scoping { background: #E0E7FF; color: #3730A3; border: 1px solid #C7D2FE; }
.pill-track   { background: #F1F5F9; color: #1E293B; border: 1px solid #CBD5E1; text-transform: uppercase; }
.pill-l       { background: #0A2454; color: white; }
.pill-platform a { color: #1E293B; text-decoration: none; }
.pill-platform { background: #FAFAF9; color: #1E293B; border: 1px solid #E5E7EB; padding: 4px 11px; }
.pill-platform a:hover { color: var(--accent); }

.agent-card { display: block; padding: 18px 20px; border: 1px solid var(--border); border-radius: 12px; background: var(--bg); transition: border-color 0.15s, box-shadow 0.15s; text-decoration: none; color: var(--ink); height: 100%; }
.agent-card:hover { border-color: var(--accent); box-shadow: 0 4px 14px rgba(0,0,0,0.06); }
.agent-card .ac-pills { display: flex; gap: 4px; flex-wrap: wrap; margin-bottom: 10px; }
.agent-card .ac-name { font-weight: 700; font-size: 17px; color: var(--ink); margin-bottom: 6px; letter-spacing: -0.01em; }
.agent-card .ac-sub { font-size: 13px; color: var(--ink-muted); line-height: 1.45; margin-bottom: 12px; }
.agent-card .ac-stat { font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--ink); padding-top: 10px; border-top: 1px solid var(--border); }
.agent-card .ac-stat strong { color: var(--accent); font-weight: 700; }
.agent-card .ac-platform { font-size: 11px; color: var(--ink-muted); margin-top: 6px; }

.band-header { padding: 10px 0; border-bottom: 1px solid var(--border); margin-bottom: 18px; display: flex; align-items: baseline; gap: 14px; }
.band-header .b-label { font-family: 'JetBrains Mono', monospace; font-size: 11px; letter-spacing: 0.08em; text-transform: uppercase; color: var(--accent); }
.band-header .b-framing { font-size: 13px; color: var(--ink-muted); }

.workflow-step { display: grid; grid-template-columns: 56px 1fr; gap: 16px; padding: 14px 0; border-top: 1px solid var(--border); align-items: start; }
.workflow-step:first-child { border-top: none; }
.workflow-step .ws-num { font-family: 'JetBrains Mono', monospace; font-size: 13px; font-weight: 700; color: white; background: var(--accent); padding: 4px 0; text-align: center; border-radius: 6px; height: 28px; }
.workflow-step .ws-title { font-weight: 600; font-size: 15px; color: var(--ink); margin-bottom: 4px; }
.workflow-step .ws-detail { font-size: 13.5px; color: var(--ink); line-height: 1.55; }

.data-table { width: 100%; border-collapse: collapse; font-size: 13px; }
.data-table th, .data-table td { padding: 10px 12px; text-align: left; border-bottom: 1px solid var(--border); vertical-align: top; }
.data-table th { font-family: 'JetBrains Mono', monospace; font-size: 10.5px; text-transform: uppercase; letter-spacing: 0.05em; color: var(--ink-muted); font-weight: 600; background: var(--bg-soft); }
.data-table td .ent { font-size: 12.5px; color: var(--ink-muted); }

.tech-chip { display: inline-block; padding: 4px 10px; border-radius: 6px; background: #F1F5F9; color: #1E293B; font-family: 'JetBrains Mono', monospace; font-size: 11px; margin: 2px 4px 2px 0; border: 1px solid #E2E8F0; }
.note-pending { padding: 12px 16px; background: #FEF9C3; border-left: 3px solid #CA8A04; border-radius: 0 6px 6px 0; font-size: 13px; color: #713F12; line-height: 1.5; margin-top: 10px; }

.pattern-chip { display: flex; flex-direction: column; padding: 12px 14px; border: 1px solid var(--border); border-radius: 8px; background: var(--bg); }
.pattern-chip .pc-name { font-weight: 600; font-size: 13px; color: var(--ink); margin-bottom: 4px; }
.pattern-chip .pc-usage { font-size: 12px; color: var(--ink-muted); line-height: 1.45; }

.linked-platform-card { display: block; padding: 14px 16px; border: 1px solid var(--border); border-radius: 10px; background: var(--bg); text-decoration: none; color: var(--ink); transition: border-color 0.15s; }
.linked-platform-card:hover { border-color: var(--accent); }
.linked-platform-card .lp-name { font-weight: 700; font-size: 14px; color: var(--ink); margin-bottom: 4px; }
.linked-platform-card .lp-role { font-size: 12px; color: var(--ink-muted); line-height: 1.45; }
.linked-platform-card .lp-arrow { color: var(--accent); font-size: 12px; margin-top: 6px; font-family: 'JetBrains Mono', monospace; }

.workflow-ascii { background: #0F172A; color: #E2E8F0; padding: 18px 20px; border-radius: 8px; font-family: 'JetBrains Mono', monospace; font-size: 11.5px; line-height: 1.5; overflow-x: auto; white-space: pre; }

.in-flight-row { padding: 12px 0; border-top: 1px solid var(--border); }
.in-flight-row:first-child { border-top: none; }
.in-flight-row .ifr-date { display: inline-block; font-family: 'JetBrains Mono', monospace; font-size: 11px; font-weight: 600; background: var(--ink); color: white; padding: 3px 8px; border-radius: 4px; margin-right: 10px; }
.in-flight-row .ifr-milestone { font-size: 13.5px; color: var(--ink); line-height: 1.5; }

.diagram-wrap { padding: 18px 12px; border: 1px solid var(--border); border-radius: 10px; background: #FAFAFA; margin-bottom: 8px; overflow: hidden; }
.diagram-wrap svg { display: block; margin: 0 auto; max-width: 100%; height: auto; font-family: 'Inter', system-ui, sans-serif; }
.diagram-caption { font-size: 11px; color: var(--ink-muted); font-family: 'JetBrains Mono', monospace; margin-bottom: 18px; }

@media (max-width: 768px) {
  .diagram-wrap, .diagram-caption { display: none; }
}
"""


# ============================================================================
# Page shell
# ============================================================================

LIGHTBOX_HTML = """
<div id="lightbox" role="dialog" aria-modal="true" aria-label="Screenshot preview" style="display:none; position:fixed; inset:0; z-index:1000; background:rgba(10,10,10,0.92); align-items:center; justify-content:center; padding:32px; cursor:zoom-out;">
  <button type="button" id="lightbox-close" aria-label="Close preview" style="position:absolute; top:20px; right:24px; background:transparent; border:0; color:#fff; font-size:32px; line-height:1; cursor:pointer; padding:8px 12px;">&times;</button>
  <img id="lightbox-img" src="" alt="" style="max-width:100%; max-height:100%; object-fit:contain; box-shadow:0 20px 60px rgba(0,0,0,0.5); cursor:auto;" />
</div>
<script>
(function(){
  var box = document.getElementById('lightbox');
  var img = document.getElementById('lightbox-img');
  var closeBtn = document.getElementById('lightbox-close');
  function open(src, alt){ img.src = src; img.alt = alt || ''; box.style.display = 'flex'; document.body.style.overflow = 'hidden'; }
  function close(){ box.style.display = 'none'; img.removeAttribute('src'); document.body.style.overflow = ''; }
  document.querySelectorAll('a.js-lightbox').forEach(function(a){
    a.addEventListener('click', function(e){
      if(e.metaKey || e.ctrlKey || e.shiftKey || e.button === 1) return;
      e.preventDefault();
      var inner = a.querySelector('img');
      open(a.getAttribute('href'), inner ? inner.getAttribute('alt') : '');
    });
  });
  box.addEventListener('click', function(e){ if(e.target === box || e.target === img) close(); });
  closeBtn.addEventListener('click', close);
  document.addEventListener('keydown', function(e){ if(e.key === 'Escape' && box.style.display === 'flex') close(); });
})();
</script>
"""


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
<link rel="stylesheet" href="/present.css">
<script src="/present.js" defer></script>
<style>{LOCAL_STYLES}</style>
</head>
<body>
{topnav()}
{body}
{footer()}
{LIGHTBOX_HTML}
</body>
</html>
"""


# ============================================================================
# Reusable building blocks
# ============================================================================

STATUS_LABELS = {"live": "Live", "build": "Building", "scoping": "Scoping"}
STATUS_PILL_CLASS = {"live": "pill-live", "build": "pill-build", "scoping": "pill-scoping"}

PATTERN_DEFS = [
    ("Tool Calling", "Agent invokes external tools/functions to read state and write back to systems."),
    ("Standard Tool Interfaces (MCP)", "Common contract for tool discovery, schemas, auth — agent and tool teams decoupled."),
    ("Context Engineering", "Choosing, structuring, and compressing what the agent sees per turn."),
    ("Agent Memory", "Short-term · episodic · semantic · procedural memory across runs."),
    ("Context Graphs", "Entities and relationships for multi-hop reasoning over retail decisions."),
    ("Wide Research", "Generate many candidate hypotheses, score broadly, then converge."),
    ("Deep / Hierarchical", "Planner → specialist sub-agents → integrator."),
    ("Multi-Agent Orchestration", "Peer agents propose · critique · enforce · arbitrate."),
    ("Observability", "Inputs · context · tool calls · outputs · errors captured as traces."),
    ("Evals", "Golden tests · simulations · replay · adversarial · policy compliance."),
]


def render_status_pill(status: str) -> str:
    klass = STATUS_PILL_CLASS.get(status, "pill-build")
    label = STATUS_LABELS.get(status, status.capitalize())
    return f'<span class="pill {klass}">{H(label)}</span>'


def render_stats(stats: list[dict]) -> str:
    if not stats:
        return ""
    cells = []
    for s in stats:
        cells.append(
            f'<div class="agent-stat">'
            f'<div class="a-label">{H(s.get("label", ""))}</div>'
            f'<div class="a-value">{H(str(s.get("value", "")))}</div>'
            + (f'<div class="a-context">{H(s.get("context", ""))}</div>' if s.get("context") else "")
            + "</div>"
        )
    return f'<div class="grid grid-cols-2 md:grid-cols-4 gap-3 mb-2">{"".join(cells)}</div>'


def render_inline_svg(svg: str | None, caption: str = "") -> str:
    """Render a hand-authored inline SVG (D20 · matches JCP / dark-factory convention).
    The svg string is embedded as-is — author is responsible for valid SVG markup."""
    if not svg:
        return ""
    cap = f'<div class="diagram-caption">{H(caption)}</div>' if caption else ""
    return f'<div class="diagram-wrap">{svg.strip()}</div>{cap}'


def render_workflow(data: dict) -> str:
    if not data.get("workflow_steps"):
        return ""
    img_html = ""
    # Inline SVG diagram (D20) — prepended above any image / step strip
    diagram_html = render_inline_svg(data.get("workflow_svg"), data.get("workflow_diagram_caption", ""))
    kind = data.get("workflow_image_kind")
    img = data.get("workflow_image")
    caption = data.get("workflow_image_caption", "")
    ascii_block = data.get("workflow_ascii")
    if kind == "ascii" and ascii_block:
        img_html = f'<pre class="workflow-ascii mb-3">{H(ascii_block)}</pre>'
        if caption:
            img_html += f'<div class="text-xs mb-5" style="color: var(--ink-muted); font-family: \'JetBrains Mono\', monospace;">{H(caption)}</div>'
    elif img:
        img_html = (
            f'<a href="{H(img)}" class="js-lightbox" target="_blank" rel="noopener" title="Open full-size">'
            f'<img src="{H(img)}" alt="{H(caption)}" '
            f'style="width:100%; max-height:380px; object-fit:contain; background:#fff; '
            f'border:1px solid var(--border); border-radius:8px; cursor:zoom-in; margin-bottom:8px;" />'
            f"</a>"
        )
        if caption:
            img_html += f'<div class="text-xs mb-5" style="color: var(--ink-muted); font-family: \'JetBrains Mono\', monospace;">{H(caption)}</div>'
    rows = []
    for step in data["workflow_steps"]:
        rows.append(
            '<div class="workflow-step">'
            f'<div class="ws-num">{H(step.get("num", ""))}</div>'
            f'<div><div class="ws-title">{H(step.get("title", ""))}</div>'
            f'<div class="ws-detail">{md_inline(step.get("detail", ""))}</div></div>'
            "</div>"
        )
    return diagram_html + img_html + '<div>' + "".join(rows) + "</div>"


def render_data_section(data: dict) -> str:
    d = data.get("data") or {}
    if not d:
        return ""
    rows = []
    for src in d.get("sources", []):
        rows.append(
            "<tr>"
            f'<td><strong>{H(src.get("name", ""))}</strong></td>'
            f'<td>{H(src.get("classification", ""))}</td>'
            f'<td><span class="ent">{H(src.get("entities", ""))}</span></td>'
            "</tr>"
        )
    table = (
        '<table class="data-table mb-4">'
        "<thead><tr><th>Data source</th><th>Classification</th><th>Key entities</th></tr></thead>"
        f'<tbody>{"".join(rows)}</tbody></table>'
    )
    cadence = ""
    if d.get("refresh_cadence"):
        cadence = f'<p class="text-sm mb-3" style="color: var(--ink);"><strong>Refresh cadence:</strong> {md_inline(d["refresh_cadence"])}</p>'
    kpis = ""
    if d.get("kpis_moved"):
        kpi_chips = "".join(f'<span class="tech-chip">{H(k)}</span>' for k in d["kpis_moved"])
        kpis = f'<p class="text-sm mb-1" style="color: var(--ink);"><strong>KPIs moved:</strong></p><div>{kpi_chips}</div>'
    return table + cadence + kpis


def render_architecture(data: dict) -> str:
    a = data.get("architecture") or {}
    if not a:
        return ""
    parts = []
    # Inline SVG architecture diagram (D20) — top of section
    diagram_html = render_inline_svg(data.get("architecture_svg"), data.get("architecture_diagram_caption", ""))
    if diagram_html:
        parts.append(diagram_html)
    if a.get("topology"):
        parts.append(f'<p class="text-sm mb-3" style="color: var(--ink);"><strong>Topology.</strong> {md_inline(a["topology"])}</p>')
    for key, label in [("models", "Models"), ("tools", "Tools"), ("memory", "Memory layers")]:
        items = a.get(key) or []
        if items:
            chips = "".join(f'<span class="tech-chip">{H(str(x))}</span>' for x in items)
            parts.append(f'<p class="text-sm mb-2" style="color: var(--ink);"><strong>{label}.</strong></p><div class="mb-3">{chips}</div>')
    if a.get("runtime"):
        parts.append(f'<p class="text-sm mb-3" style="color: var(--ink);"><strong>Runtime.</strong> {md_inline(a["runtime"])}</p>')
    if a.get("note_pending"):
        parts.append(f'<div class="note-pending">{md_inline(a["note_pending"])}</div>')
    return "".join(parts)


def render_patterns(data: dict) -> str:
    patterns = data.get("patterns") or []
    if not patterns:
        return ""
    cells = []
    for p in patterns:
        cells.append(
            '<div class="pattern-chip">'
            f'<div class="pc-name">{H(p.get("name", ""))}</div>'
            f'<div class="pc-usage">{md_inline(p.get("usage", ""))}</div>'
            "</div>"
        )
    return f'<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3">{"".join(cells)}</div>'


def render_evals(data: dict) -> str:
    e = data.get("evals") or {}
    if not e:
        return ""
    parts = []
    if e.get("approach"):
        parts.append(f'<p class="text-sm mb-3" style="color: var(--ink);">{md_inline(e["approach"])}</p>')
    if e.get("gates"):
        items = "".join(f'<li>{md_inline(g)}</li>' for g in e["gates"])
        parts.append(f'<p class="text-sm mb-1" style="color: var(--ink);"><strong>Gates and thresholds.</strong></p><ul class="list-disc pl-5 text-sm" style="color: var(--ink);">{items}</ul>')
    return "".join(parts)


def render_status_section(data: dict) -> str:
    parts = []
    parts.append('<div class="grid grid-cols-1 md:grid-cols-3 gap-6">')
    # Live today
    parts.append(
        '<div><div class="text-xs mb-2" style="color: var(--ink-muted); font-family: \'JetBrains Mono\', monospace; text-transform: uppercase; letter-spacing: 0.06em;">Live for RIL today</div>'
        f'<div class="text-sm" style="color: var(--ink); line-height: 1.55;">{md_inline(data.get("live_today", "—"))}</div></div>'
    )
    # In flight
    if_html = '<div><div class="text-xs mb-2" style="color: var(--ink-muted); font-family: \'JetBrains Mono\', monospace; text-transform: uppercase; letter-spacing: 0.06em;">In flight</div>'
    in_flight = data.get("in_flight") or []
    if not in_flight:
        if_html += '<div class="text-sm" style="color: var(--ink-muted);">—</div>'
    else:
        for row in in_flight:
            if_html += (
                '<div class="in-flight-row">'
                f'<span class="ifr-date">{H(str(row.get("date", "")))}</span>'
                f'<span class="ifr-milestone">{md_inline(row.get("milestone", ""))}</span>'
                "</div>"
            )
    if_html += "</div>"
    parts.append(if_html)
    # Roadmap
    rm_html = '<div><div class="text-xs mb-2" style="color: var(--ink-muted); font-family: \'JetBrains Mono\', monospace; text-transform: uppercase; letter-spacing: 0.06em;">Roadmap</div>'
    roadmap = data.get("roadmap") or []
    if not roadmap:
        rm_html += '<div class="text-sm" style="color: var(--ink-muted);">—</div>'
    else:
        items = "".join(f'<li>{md_inline(r)}</li>' for r in roadmap)
        rm_html += f'<ul class="list-disc pl-5 text-sm" style="color: var(--ink); line-height: 1.5;">{items}</ul>'
    rm_html += "</div>"
    parts.append(rm_html)
    parts.append("</div>")
    return "".join(parts)


def render_linked_platforms(data: dict) -> str:
    platforms = data.get("linked_platforms") or []
    if not platforms:
        return ""
    cells = []
    for p in platforms:
        cells.append(
            f'<a href="{H(p.get("route", "#"))}" class="linked-platform-card">'
            f'<div class="lp-name">{H(p.get("name", ""))}</div>'
            f'<div class="lp-role">{H(p.get("role", ""))}</div>'
            f'<div class="lp-arrow">View platform →</div>'
            "</a>"
        )
    return f'<div class="grid grid-cols-1 md:grid-cols-3 gap-3">{"".join(cells)}</div>'


def render_sources_section(data: dict) -> str:
    sources = data.get("source_citations") or []
    if not sources:
        return ""
    items = "".join(f'<li class="text-sm mb-2" style="color: var(--ink);">{md_inline(s)}</li>' for s in sources)
    return f'<ul class="list-disc pl-5">{items}</ul>'


# ============================================================================
# Detail page
# ============================================================================


def render_detail(slug: str, data: dict) -> str:
    name = data.get("name", slug)
    sub = data.get("sub_title", "")
    track = data.get("track", "").upper()
    autonomy = data.get("autonomy_level", "")
    status = data.get("status", "build")
    primary = data.get("primary_platform") or {}

    pills_row = f'{render_status_pill(status)} '
    pills_row += f'<span class="pill pill-track">{H(track)}</span> '
    if autonomy:
        pills_row += f'<span class="pill pill-l">{H(autonomy)}</span> '
    if primary.get("name"):
        pills_row += (
            f'<span class="pill pill-platform">Powered by &nbsp;'
            f'<a href="{H(primary.get("route", "#"))}">→ {H(primary["name"])}</a></span>'
        )

    section = lambda num, label, body, extra_class="": (
        f'<section class="py-10 border-t" style="border-color: var(--border);">'
        f'<div class="container mx-auto px-6 max-w-6xl">'
        f'<div class="text-xs mb-3" style="color: var(--accent); font-family: \'JetBrains Mono\', monospace; text-transform: uppercase; letter-spacing: 0.06em;">{H(num)} · {H(label)}</div>'
        f'<div class="{extra_class}">{body}</div>'
        f"</div></section>"
    )

    # Hero
    hero = f"""
<section class="pt-10 pb-8" style="background: linear-gradient(180deg, var(--bg-soft) 0%, var(--bg) 100%);">
  <div class="container mx-auto px-6 max-w-6xl">
    <nav class="text-xs mb-4" style="color: var(--ink-muted); font-family: 'JetBrains Mono', monospace;">
      <a href="/" style="color: var(--ink-muted);">Home</a> /
      <a href="/agents" style="color: var(--ink-muted);">AI Agents</a> /
      <span style="color: var(--ink);">{H(name)}</span>
    </nav>
    <div class="text-xs mb-3" style="color: var(--accent); font-family: 'JetBrains Mono', monospace; letter-spacing: 0.08em; text-transform: uppercase;">AI Agents · {H(slug.upper())} · {H(STATUS_LABELS.get(status, status.upper()))}</div>
    <h1 class="display-1 text-4xl md:text-5xl mb-3" style="color: var(--ink); letter-spacing: -0.02em; font-weight: 800;">{H(name)}.</h1>
    <p class="text-lg max-w-3xl mb-5" style="color: var(--ink-muted); line-height: 1.5;">{md_inline(sub)}</p>
    <div class="mb-6" style="display: flex; flex-wrap: wrap; gap: 6px;">{pills_row}</div>
    {render_stats(data.get("stats", []))}
  </div>
</section>
"""

    # § 01 Job
    job = data.get("job") or {}
    job_html = (
        '<div class="grid grid-cols-1 md:grid-cols-3 gap-6">'
        f'<div><div class="text-xs mb-2" style="color: var(--ink-muted); font-family: \'JetBrains Mono\', monospace; text-transform: uppercase; letter-spacing: 0.06em;">The pain</div>'
        f'<div class="text-sm" style="color: var(--ink); line-height: 1.55;">{md_inline(job.get("pain", ""))}</div></div>'
        f'<div><div class="text-xs mb-2" style="color: var(--ink-muted); font-family: \'JetBrains Mono\', monospace; text-transform: uppercase; letter-spacing: 0.06em;">What the agent does</div>'
        f'<div class="text-sm" style="color: var(--ink); line-height: 1.55;">{md_inline(job.get("what_it_does", ""))}</div></div>'
        f'<div><div class="text-xs mb-2" style="color: var(--ink-muted); font-family: \'JetBrains Mono\', monospace; text-transform: uppercase; letter-spacing: 0.06em;">What humans still do</div>'
        f'<div class="text-sm" style="color: var(--ink); line-height: 1.55;">{md_inline(job.get("human_role", ""))}</div></div>'
        "</div>"
    )

    # Empty DEPLOYED-IN marker pair · populated by tools/inject_path_to_l4.py
    # on the next sweep. New agent pages need the markers present at first
    # build; the injector replaces only what's between them.
    deployed_in_stub = (
        "<!-- DEPLOYED-IN-START · auto-generated by tools/inject_path_to_l4.py · do not edit -->\n"
        "<!-- (sweep pending — run: python tools/inject_path_to_l4.py) -->\n"
        "<!-- DEPLOYED-IN-END -->"
    )

    body = (
        hero
        + deployed_in_stub
        + section("01", "The job to be done", job_html)
        + section("02", "How it works · the closed loop", render_workflow(data))
        + section("03", "Underlying data", render_data_section(data))
        + section("04", "Design patterns used", render_patterns(data))
        + section("05", "Evals · what gates each output", render_evals(data))
        + section("06", "Linked platforms", render_linked_platforms(data))
    )
    # §Architecture and §Status dropped per user feedback 2026-05-02.
    # Architecture detail too internal for Apex; status lives on the linked platform page.
    # § Sources block deliberately not rendered — see agents-spec D18 + tone-of-voice §3.
    # Provenance lives in YAML's source_citations: as developer-facing metadata only.

    return page_shell(f"{name} · AI Agents · Reliance Retail × Fynd", body)


# ============================================================================
# Index page
# ============================================================================


def render_index(catalog: dict, agents: dict[str, dict]) -> str:
    hero = catalog.get("hero", {})
    track_labels = catalog.get("track_labels", {})
    order = catalog.get("order", {})

    hero_html = f"""
<section class="pt-10 pb-8" style="background: linear-gradient(180deg, var(--bg-soft) 0%, var(--bg) 100%);">
  <div class="container mx-auto px-6 max-w-6xl">
    <nav class="text-xs mb-4" style="color: var(--ink-muted); font-family: 'JetBrains Mono', monospace;">
      <a href="/" style="color: var(--ink-muted);">Home</a> /
      <span style="color: var(--ink);">AI Agents</span>
    </nav>
    <div class="text-xs mb-3" style="color: var(--accent); font-family: 'JetBrains Mono', monospace; letter-spacing: 0.08em; text-transform: uppercase;">AI Agents · Catalog · Live</div>
    <h1 class="display-1 text-4xl md:text-5xl mb-3" style="color: var(--ink); letter-spacing: -0.02em; font-weight: 800;">AI Agents.</h1>
    <p class="text-lg max-w-3xl mb-2" style="color: var(--ink-muted); line-height: 1.5;">{H(hero.get("subhead", "").strip())}</p>
  </div>
</section>
"""

    # § 02 · The agents · grouped by track band
    bands_html = []
    for track_key in ["plan", "buy", "sell"]:
        slugs = order.get(track_key, [])
        if not slugs:
            continue
        meta = track_labels.get(track_key, {})
        cards = []
        for s in slugs:
            ag = agents.get(s)
            if not ag:
                # Stub card for not-yet-extracted agents
                cards.append(
                    f'<div class="agent-card" style="opacity:0.45; cursor: default;">'
                    f'<div class="ac-pills"><span class="pill pill-build">Pending</span></div>'
                    f'<div class="ac-name">{H(s.replace("-", " ").title())}</div>'
                    f'<div class="ac-sub">YAML extraction pending · P2 phase.</div>'
                    "</div>"
                )
                continue
            anchor_stat = ""
            stats_list = ag.get("stats") or []
            if stats_list:
                first = stats_list[0]
                anchor_stat = f'<strong>{H(str(first.get("value", "")))}</strong> · {H(first.get("label", ""))}'
            primary = ag.get("primary_platform") or {}
            cards.append(
                f'<a href="/agents/{H(s)}/" class="agent-card">'
                f'<div class="ac-pills">{render_status_pill(ag.get("status", "build"))}'
                + (f'<span class="pill pill-l">{H(ag.get("autonomy_level", ""))}</span>' if ag.get("autonomy_level") else "")
                + "</div>"
                f'<div class="ac-name">{H(ag.get("name", s))}</div>'
                f'<div class="ac-sub">{md_inline(ag.get("sub_title", ""))}</div>'
                + (f'<div class="ac-stat">{anchor_stat}</div>' if anchor_stat else "")
                + "</a>"
            )
        bands_html.append(
            f'<div class="mb-10">'
            f'<div class="band-header">'
            f'<span class="b-label">{H(meta.get("label", track_key.upper()))} · {len(slugs)}</span>'
            f'<span class="b-framing">{H(meta.get("framing", ""))}</span>'
            "</div>"
            f'<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">{"".join(cards)}</div>'
            "</div>"
        )
    bands_section = (
        '<section class="py-10 border-t" style="border-color: var(--border);">'
        '<div class="container mx-auto px-6 max-w-6xl">'
        '<div class="text-xs mb-3" style="color: var(--accent); font-family: \'JetBrains Mono\', monospace; text-transform: uppercase; letter-spacing: 0.06em;">02 · The agents · by value-chain track</div>'
        + "".join(bands_html)
        + "</div></section>"
    )

    # § 03 · Autonomy matrix (reuse from /autonomous/)
    matrix_section = f"""
<section class="py-10 border-t" style="border-color: var(--border);">
  <div class="container mx-auto px-6 max-w-6xl">
    <div class="text-xs mb-3" style="color: var(--accent); font-family: 'JetBrains Mono', monospace; text-transform: uppercase; letter-spacing: 0.06em;">03 · The autonomy matrix · where each agent sits</div>
    <p class="text-sm mb-4" style="color: var(--ink); line-height: 1.55; max-width: 720px;">{hero.get("workflows_at_l4", 5)} of {hero.get("total_workflows", 21)} workflows reach L4 in the 90-day plan. The remaining 16 sit at L2-L3 deliberately — strategy stays human, brand stays human-curated, compliance stays human-accountable.</p>
    <a href="/assets/autonomous/matrix-1.jpg" class="js-lightbox" target="_blank" rel="noopener" title="Open full-size">
      <img src="/assets/autonomous/matrix-1.jpg" alt="Autonomy matrix · 21 retail workflows × L0-L5" style="width:100%; max-width:1100px; border:1px solid var(--border); border-radius:8px; cursor:zoom-in;" />
    </a>
    <div class="text-xs mt-2" style="color: var(--ink-muted); font-family: 'JetBrains Mono', monospace;">Canonical home: <a href="/autonomous" style="color: var(--accent);">/autonomous</a></div>
  </div>
</section>
"""

    # § 04 · 10 building blocks
    pattern_cells = [
        f'<div class="pattern-chip"><div class="pc-name">{H(name)}</div><div class="pc-usage">{H(desc)}</div></div>'
        for name, desc in PATTERN_DEFS
    ]
    blocks_section = (
        '<section class="py-10 border-t" id="building-blocks" style="border-color: var(--border);">'
        '<div class="container mx-auto px-6 max-w-6xl">'
        '<div class="text-xs mb-3" style="color: var(--accent); font-family: \'JetBrains Mono\', monospace; text-transform: uppercase; letter-spacing: 0.06em;">04 · The 10 building blocks · how every agent is constructed</div>'
        '<p class="text-sm mb-5" style="color: var(--ink); line-height: 1.55; max-width: 720px;">Every agent on this catalog is built from some combination of these primitives.</p>'
        f'<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3">{"".join(pattern_cells)}</div>'
        "</div></section>"
    )

    # § Sources block deliberately not rendered — see agents-spec D18 + tone-of-voice §3.
    body = hero_html + bands_section + matrix_section + blocks_section
    return page_shell("AI Agents · Catalog · Reliance Retail × Fynd", body)


# ============================================================================
# Main
# ============================================================================


def load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def load_all_agents() -> dict[str, dict]:
    out = {}
    for f in sorted(DATA_DIR.glob("*.yaml")):
        if f.name.startswith("_"):
            continue
        out[f.stem] = load_yaml(f)
    return out


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    rel = path.relative_to(ROOT)
    print(f"  wrote {rel} ({len(content):,} bytes)")


def build_index() -> None:
    catalog = load_yaml(DATA_DIR / "_catalog.yaml")
    agents = load_all_agents()
    write(OUT_DIR / "index.html", render_index(catalog, agents))


def build_detail(slug: str) -> None:
    path = DATA_DIR / f"{slug}.yaml"
    if not path.exists():
        print(f"  ! no yaml at {path.relative_to(ROOT)}")
        return
    data = load_yaml(path)
    write(OUT_DIR / slug / "index.html", render_detail(slug, data))


def main() -> None:
    args = sys.argv[1:]
    if not args or args[0] in ("--all", "all"):
        print("Building /agents/ index + every detail page…")
        build_index()
        for slug in load_all_agents():
            build_detail(slug)
    elif args[0] in ("--index", "index"):
        print("Building /agents/ index only…")
        build_index()
    else:
        for slug in args:
            print(f"Building /agents/{slug}/…")
            build_detail(slug)
    print("Done.")


if __name__ == "__main__":
    main()
