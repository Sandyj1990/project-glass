#!/usr/bin/env python3
"""Generate /docs/index.html · power-user back-office.

Hidden from public nav. Surfaces every file under data/ (not just binary assets):
- All cross-cutting sources (data/sources/, data/research/, data/audits/) at the top
- Per-IP drawer shows narrative · metrics · team · releases · links · slack-extracts · binary assets
- In-page Supabase upload to add new binaries without touching the repo
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools" / "build_data"))

from spec import IPS  # type: ignore

DATA_DIR = ROOT / "data"
DOCS_DIR = ROOT / "docs"
DOCS_DIR.mkdir(exist_ok=True)

GH_OWNER = "salmansaudagar-ai"
GH_REPO = "reliance-retail-fynd"
ASSET_BUCKETS = ["decks", "docs", "images", "videos"]
META_FILES = ["meta.json", "narrative.md", "metrics.yaml", "team.yaml", "releases.yaml", "links.yaml"]


def gh_blob(rel_path):
    return f"https://github.com/{GH_OWNER}/{GH_REPO}/blob/master/{rel_path}"


def file_size_kb(path):
    return path.stat().st_size // 1024


def list_dir_files(path):
    """Return [(name, gh_url, size_kb)] for every file in a folder."""
    out = []
    if not path.exists():
        return out
    for f in sorted(path.iterdir()):
        if f.is_file():
            rel = f.relative_to(ROOT)
            out.append({"name": f.name, "url": gh_blob(rel), "size_kb": file_size_kb(f)})
    return out


def collect_ip(ip):
    """Per-IP inventory · all data files (meta + narrative + metrics + team + releases + links + slack + assets)."""
    slug = ip["slug"]
    folder = DATA_DIR / "ips" / slug
    inv = {
        "slug": slug,
        "name": ip["name"],
        "tagline": ip.get("tagline", ""),
        "status": ip.get("status", "Build"),
        "track": ip.get("track", ""),
        "track_role": ip.get("track_role", ""),
        "web_anchor": ip.get("web_anchor", ""),
        "dri": ip.get("team", {}).get("dri", []),
        "meta_files": [],
        "slack_extracts": [],
        "assets": {b: [] for b in ASSET_BUCKETS},
    }

    # Meta files
    for fname in META_FILES:
        p = folder / fname
        if p.exists():
            inv["meta_files"].append({
                "name": fname,
                "url": gh_blob(p.relative_to(ROOT)),
                "size_kb": file_size_kb(p),
            })

    # Slack extracts
    inv["slack_extracts"] = list_dir_files(folder / "slack-extracts")

    # Asset buckets
    for b in ASSET_BUCKETS:
        inv["assets"][b] = list_dir_files(folder / "assets" / b)

    inv["repo_count"] = (
        len(inv["meta_files"])
        + len(inv["slack_extracts"])
        + sum(len(inv["assets"][b]) for b in ASSET_BUCKETS)
    )
    return inv


CHEVRON = '<svg viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><polyline points="3 5 6 8 9 5"/></svg>'

NAV_HTML = f'''<nav class="topnav"><div class="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center gap-4">
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
  <div class="nav-mega"><span class="nav-link" tabindex="0">Tracks {CHEVRON}</span>
    <div class="nav-mega-panel">
      <div class="grid grid-cols-3 gap-4">
        <div>
          <div class="mega-col-label">Platform</div>
          <a href="/jcp" class="mega-link">JCP <span class="mono-suffix">68 live</span></a>
          <a href="/impetus" class="mega-link">Impetus <span class="mono-suffix">F&amp;L AI</span></a>
          <a href="/granary" class="mega-link">Granary <span class="mono-suffix">Grocery AI</span></a>
        </div>
        <div>
          <div class="mega-col-label">Vertical</div>
          <a href="/samarth" class="mega-link">Samarth</a>
          <a href="/rcpl" class="mega-link">RCPL</a>
          <a href="/retail-vista" class="mega-link">Retail Vista</a>
          <a href="/retail-jarvis" class="mega-link">Retail Jarvis</a>
          <a href="/alp" class="mega-link">ALP</a>
          <a href="/forge" class="mega-link">Forge MES</a>
          <a href="/hirefirst" class="mega-link">HireFirst <span class="mono-suffix">HR Tech</span></a>
        </div>
        <div>
          <div class="mega-col-label">Capability</div>
          <a href="/autonomous" class="mega-link">Autonomous <span class="mono-suffix">11 sub</span></a>
          <a href="/pixelbin/videos" class="mega-link">Studio · Videos</a>
          <a href="/impetus/photoshoots" class="mega-link">AI Photoshoots</a>
          <a href="/impetus/brands" class="mega-link">Brand designs</a>
          <a href="/impetus/category-intel" class="mega-link">Category intel</a>
        </div>
      </div>
    </div>
  </div>
  <a href="/numbers" class="nav-link">Numbers</a>
  <a href="/docs" class="nav-link active">Docs</a>
  <div class="nav-mega"><span class="nav-link" tabindex="0">More {CHEVRON}</span>
    <div class="nav-mega-panel" style="min-width: 280px;">
      <a href="/organisation" class="mega-link">Organisation <span class="mono-suffix">~430 on RR</span></a>
      <a href="/culture" class="mega-link">Culture</a>
      <a href="/catalog" class="mega-link">IP Catalog <span class="mono-suffix">all IPs</span></a>
    </div>
  </div>
</div>
<div class="hidden lg:flex items-center gap-2 shrink-0">
  <span class="back-office-pill">back-office</span>
  <span class="nav-version"><span class="nav-version-dot"></span>v0.8.4</span>
</div>
</div></nav>'''


def render_root_section(label, folder_name):
    """Render a root-level data folder section · sources / research / audits."""
    folder = DATA_DIR / folder_name
    files = list_dir_files(folder)
    if not files:
        return ""
    rows = "".join(
        f'<a href="{f["url"]}" target="_blank" class="root-file" title="{f["size_kb"]} KB">'
        f'<span class="root-file-name">{f["name"]}</span>'
        f'<span class="root-file-size">{f["size_kb"]} KB</span>'
        f'</a>'
        for f in files
    )
    gh_folder_url = f"https://github.com/{GH_OWNER}/{GH_REPO}/tree/master/data/{folder_name}"
    return f'''
<div class="root-bucket">
  <div class="root-bucket-head">
    <div>
      <div class="cap-num" style="color: var(--ink);">{label}</div>
      <div class="text-xs" style="color: var(--ink-muted);">data/{folder_name}/ · {len(files)} files</div>
    </div>
    <a href="{gh_folder_url}" target="_blank" class="text-xs" style="color: var(--ink-muted);">view on GitHub →</a>
  </div>
  <div class="root-files">{rows}</div>
</div>
'''


def render():
    inventory = [collect_ip(ip) for ip in IPS]
    inventory_json = json.dumps(inventory)

    total_files = sum(ip["repo_count"] for ip in inventory)
    status_count = {"Live": 0, "Pilot": 0, "Build": 0}
    for ip in inventory:
        status_count[ip["status"]] = status_count.get(ip["status"], 0) + 1

    sources_html = render_root_section("Sources · cross-cutting reference material", "sources")
    research_html = render_root_section("Research · reviews + persona passes + evolution log", "research")
    audits_html = render_root_section("Audits · MDA-perspective punch-lists", "audits")

    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Docs · back-office · all data sources · Reliance Retail × Fynd</title>
<link rel="icon" type="image/png" href="/assets/fynd-logo.png">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<script src="/auth.js"></script>
<script src="https://cdn.tailwindcss.com"></script>
<link rel="stylesheet" href="/style.css">
<style>
  .back-office-pill {{ font-family: 'JetBrains Mono', monospace; font-size: 10px; letter-spacing: 0.06em; text-transform: uppercase; padding: 4px 8px; border-radius: 999px; background: #FEF2F2; color: #B91C1C; border: 1px solid #FECACA; }}

  .sb-banner {{ background: white; border: 1px solid var(--border); border-radius: 14px; padding: 16px 20px; }}
  .sb-banner.unset {{ border-color: var(--amber); background: #FFFBEB; }}
  .sb-banner.set {{ border-color: var(--green); }}
  .sb-fields {{ display: grid; grid-template-columns: 1fr 1fr 180px auto; gap: 8px; }}
  .sb-fields input {{ padding: 8px 12px; border: 1px solid var(--border); border-radius: 8px; font-size: 13px; font-family: 'JetBrains Mono', monospace; }}
  .sb-fields input:focus {{ outline: none; border-color: var(--accent); }}
  .sb-btn {{ padding: 8px 16px; background: var(--ink); color: white; font-size: 13px; font-weight: 600; border-radius: 8px; cursor: pointer; border: 0; transition: opacity .15s; }}
  .sb-btn:hover {{ opacity: 0.85; }}
  .sb-btn-secondary {{ background: white; color: var(--ink); border: 1px solid var(--border); }}

  .stats-row {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 10px; }}
  .stat-tile {{ background: var(--bg-soft); border: 1px solid var(--border); border-radius: 10px; padding: 12px 14px; }}
  .stat-tile .num {{ font-size: 22px; font-weight: 800; letter-spacing: -0.02em; }}
  .stat-tile .lbl {{ font-family: 'JetBrains Mono', monospace; font-size: 10px; letter-spacing: 0.06em; text-transform: uppercase; color: var(--ink-muted); margin-top: 2px; }}

  /* Cross-cutting buckets */
  .root-bucket {{ background: white; border: 1px solid var(--border); border-radius: 12px; padding: 14px 16px; margin-bottom: 10px; }}
  .root-bucket-head {{ display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 10px; }}
  .root-files {{ display: flex; flex-wrap: wrap; gap: 6px; }}
  .root-file {{ display: inline-flex; align-items: center; gap: 8px; padding: 6px 10px; border-radius: 8px; background: var(--bg-soft); border: 1px solid var(--border-soft); font-size: 12px; transition: all .12s; }}
  .root-file:hover {{ border-color: var(--accent); color: var(--accent); }}
  .root-file-name {{ font-family: 'JetBrains Mono', monospace; }}
  .root-file-size {{ font-family: 'JetBrains Mono', monospace; font-size: 10px; color: var(--ink-muted); }}
  .root-file:hover .root-file-size {{ color: var(--accent); }}

  .filter-bar {{ display: flex; flex-wrap: wrap; gap: 6px; align-items: center; }}
  .filter-bar input {{ flex: 1; min-width: 240px; padding: 9px 14px; border: 1px solid var(--border); border-radius: 999px; font-size: 13px; }}
  .filter-bar input:focus {{ outline: none; border-color: var(--accent); }}
  .filter-chip {{ font-family: 'JetBrains Mono', monospace; font-size: 11px; text-transform: uppercase; letter-spacing: 0.04em; padding: 6px 12px; border-radius: 999px; border: 1px solid var(--border); background: white; cursor: pointer; user-select: none; transition: all 0.15s; }}
  .filter-chip:hover {{ border-color: var(--ink); }}
  .filter-chip.active {{ background: var(--ink); color: white; border-color: var(--ink); }}

  .ip-table {{ width: 100%; border-collapse: collapse; }}
  .ip-table th {{ font-family: 'JetBrains Mono', monospace; font-size: 10px; letter-spacing: 0.06em; text-transform: uppercase; color: var(--ink-muted); text-align: left; padding: 12px 14px; border-bottom: 1px solid var(--ink); background: var(--bg-soft); }}
  .ip-row td {{ padding: 12px 14px; border-bottom: 1px solid var(--border); vertical-align: middle; }}
  .ip-row {{ cursor: pointer; transition: background .12s; }}
  .ip-row:hover {{ background: var(--bg-soft); }}
  .ip-row.expanded {{ background: rgba(107,91,214,0.04); }}
  .ip-name {{ font-weight: 600; color: var(--ink); }}
  .ip-meta {{ font-family: 'JetBrains Mono', monospace; font-size: 10px; color: var(--ink-muted); margin-top: 2px; }}
  .file-count-pill {{ display: inline-flex; align-items: center; gap: 5px; font-family: 'JetBrains Mono', monospace; font-size: 10px; padding: 3px 8px; border-radius: 6px; background: var(--bg-soft); color: var(--ink-muted); border: 1px solid var(--border-soft); margin-right: 4px; }}
  .file-count-pill.has-files {{ background: rgba(107,91,214,0.08); color: var(--accent); border-color: rgba(107,91,214,0.18); }}
  .file-count-pill strong {{ color: var(--ink); }}
  .file-count-pill.has-files strong {{ color: var(--accent); }}

  .ip-drawer-row td {{ padding: 0 !important; border-bottom: 1px solid var(--border); background: var(--bg-soft); }}
  .ip-drawer {{ padding: 24px 28px; }}
  .drawer-grid {{ display: grid; grid-template-columns: 1fr 320px; gap: 24px; }}
  .bucket-section {{ margin-bottom: 16px; }}
  .bucket-head {{ display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px; }}
  .bucket-name {{ font-family: 'JetBrains Mono', monospace; font-size: 11px; letter-spacing: 0.06em; text-transform: uppercase; color: var(--ink); font-weight: 600; }}
  .bucket-count {{ font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--ink-muted); }}
  .file-list {{ background: white; border: 1px solid var(--border); border-radius: 8px; overflow: hidden; }}
  .file-row {{ display: grid; grid-template-columns: 1fr auto auto auto; gap: 12px; padding: 8px 14px; border-bottom: 1px solid var(--border-soft); align-items: center; font-size: 12px; }}
  .file-row:last-child {{ border-bottom: 0; }}
  .file-row .file-name {{ font-family: 'JetBrains Mono', monospace; color: var(--ink); overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }}
  .file-row .file-source {{ font-family: 'JetBrains Mono', monospace; font-size: 9px; padding: 2px 6px; border-radius: 4px; }}
  .file-source.repo {{ background: var(--accent-soft); color: var(--accent); }}
  .file-source.cloud {{ background: #ECFDF5; color: #047857; }}
  .file-source.meta {{ background: #FEF3C7; color: #92400E; }}
  .file-source.slack {{ background: #DBEAFE; color: #1E40AF; }}
  .file-row .file-size {{ font-family: 'JetBrains Mono', monospace; color: var(--ink-muted); }}
  .file-row a {{ color: var(--ink-muted); transition: color .12s; }}
  .file-row a:hover {{ color: var(--accent); }}
  .file-row button {{ background: transparent; border: 0; color: var(--ink-muted); cursor: pointer; transition: color .12s; padding: 0; }}
  .file-row button:hover {{ color: var(--red); }}
  .empty-list {{ padding: 12px 14px; font-size: 12px; color: var(--ink-muted); font-style: italic; }}

  .drop-zone {{ border: 2px dashed var(--border); border-radius: 12px; padding: 28px 20px; text-align: center; background: white; transition: border-color .15s, background .15s; }}
  .drop-zone.over {{ border-color: var(--accent); background: rgba(107,91,214,0.04); }}
  .drop-zone p {{ margin-bottom: 8px; }}
  .drop-zone-cap {{ font-family: 'JetBrains Mono', monospace; font-size: 10px; color: var(--ink-muted); letter-spacing: 0.06em; text-transform: uppercase; margin-bottom: 12px; }}
  .drop-zone .pick-btn {{ display: inline-block; padding: 8px 16px; background: var(--ink); color: white; border-radius: 8px; font-size: 13px; font-weight: 600; cursor: pointer; }}
  .bucket-picker {{ display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 12px; }}
  .bucket-picker label {{ display: inline-flex; align-items: center; gap: 6px; font-size: 12px; font-family: 'JetBrains Mono', monospace; padding: 4px 10px; border: 1px solid var(--border); border-radius: 999px; cursor: pointer; }}
  .bucket-picker input {{ accent-color: var(--accent); }}
  .upload-status {{ margin-top: 12px; font-size: 12px; min-height: 18px; }}
  .upload-status.ok {{ color: var(--green); }}
  .upload-status.err {{ color: var(--red); }}

  .recent-strip {{ background: white; border: 1px solid var(--border); border-radius: 12px; padding: 12px 16px; margin-bottom: 16px; }}
  .recent-strip .recent-list {{ display: flex; flex-wrap: wrap; gap: 6px; }}
  .recent-pill {{ font-family: 'JetBrains Mono', monospace; font-size: 11px; padding: 3px 10px; border-radius: 999px; background: var(--bg-soft); color: var(--ink-muted); }}

  kbd {{ font-family: 'JetBrains Mono', monospace; font-size: 10px; padding: 2px 6px; background: var(--bg-soft); border: 1px solid var(--border); border-bottom: 2px solid var(--border); border-radius: 4px; color: var(--ink); }}

  details summary {{ cursor: pointer; list-style: none; }}
  details summary::-webkit-details-marker {{ display: none; }}
</style>
</head>
<body>

{NAV_HTML}

<section class="pt-10 pb-6 border-b" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6 text-left">
<div class="crumb mb-4"><a href="/">Home</a> <span class="sep">/</span> <span style="color: var(--ink);">Docs · back-office</span></div>
<div class="flex flex-wrap items-baseline justify-between gap-3 mb-3">
  <h1 class="display text-3xl md:text-4xl" style="color: var(--ink);">Docs.</h1>
  <div class="text-xs" style="color: var(--ink-muted);">Hidden from public nav. <kbd>/</kbd> search · <kbd>Esc</kbd> close · click any IP row.</div>
</div>
<p class="text-sm max-w-3xl" style="color: var(--ink-muted);">Every byte of data that powers this register · cross-cutting sources at the top, then per-IP files (meta, narrative, metrics, team, releases, links, slack threads, decks, images, videos). Drag-drop uploads land in Supabase Storage and show up alongside repo files.</p>
</div></section>

<!-- Supabase configuration -->
<section class="py-4 border-b" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
<div id="sb-banner" class="sb-banner unset">
  <div class="flex items-baseline justify-between mb-3">
    <div>
      <div class="cap-num" style="color: var(--ink);">Supabase Storage · upload target</div>
      <div class="text-xs" id="sb-status" style="color: var(--amber);">Not configured</div>
    </div>
    <button id="sb-toggle" class="sb-btn sb-btn-secondary" style="font-size: 11px; padding: 4px 10px;">collapse</button>
  </div>
  <div id="sb-form" class="sb-fields">
    <input id="sb-url" type="text" placeholder="https://xxxxx.supabase.co" />
    <input id="sb-key" type="password" placeholder="anon/public key" />
    <input id="sb-bucket" type="text" placeholder="bucket-name" value="fyndrrl" />
    <button id="sb-save" class="sb-btn">save</button>
  </div>
  <div class="text-xs mt-3" style="color: var(--ink-muted);">Stored locally in your browser only. Bucket should be created in Supabase with public read · the auth gate covers access control. Path · <span class="mono">ips/&lt;slug&gt;/&lt;bucket&gt;/&lt;filename&gt;</span></div>
</div>
</div></section>

<!-- Stats -->
<section class="py-6 border-b" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
<div class="stats-row">
  <div class="stat-tile"><div class="num">{len(IPS)}</div><div class="lbl">IPs</div></div>
  <div class="stat-tile"><div class="num" style="color: var(--green);">{status_count.get("Live", 0)}</div><div class="lbl">Live</div></div>
  <div class="stat-tile"><div class="num" style="color: var(--amber);">{status_count.get("Pilot", 0)}</div><div class="lbl">Pilot</div></div>
  <div class="stat-tile"><div class="num" style="color: var(--ink-muted);">{status_count.get("Build", 0)}</div><div class="lbl">Build</div></div>
  <div class="stat-tile"><div class="num accent">{total_files}</div><div class="lbl">Repo files (data/)</div></div>
  <div class="stat-tile"><div class="num accent" id="cloud-count">--</div><div class="lbl">In Supabase</div></div>
</div>
</div></section>

<!-- Cross-cutting data buckets -->
<section class="py-6 border-b" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
<details open>
<summary>
  <div class="flex items-center gap-2 mb-4">
    <span class="cap-num" style="color: var(--ink);">Cross-cutting data</span>
    <span class="text-xs" style="color: var(--ink-muted);">(click to collapse)</span>
  </div>
</summary>
{sources_html}
{research_html}
{audits_html}
</details>
</div></section>

<!-- Recent uploads -->
<section class="py-3 border-b" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
<div id="recent-strip" class="recent-strip" style="display: none;">
  <div class="cap-num mb-2">Recent uploads · this session</div>
  <div id="recent-list" class="recent-list"></div>
</div>
</div></section>

<!-- Filters -->
<section class="py-4 border-b sticky top-0 z-30" style="border-color: var(--border); background: rgba(255,255,255,0.95); backdrop-filter: blur(8px);"><div class="max-w-7xl mx-auto px-6">
<div class="filter-bar">
  <input id="ip-search" type="search" placeholder="Search · IP name, slug, tagline · press / to focus" />
  <span class="filter-chip active" data-filter="status" data-value="all">All</span>
  <span class="filter-chip" data-filter="status" data-value="live">Live</span>
  <span class="filter-chip" data-filter="status" data-value="pilot">Pilot</span>
  <span class="filter-chip" data-filter="status" data-value="build">Build</span>
  <span class="filter-chip active" data-filter="files" data-value="all">All files</span>
  <span class="filter-chip" data-filter="files" data-value="yes">With files</span>
  <span class="filter-chip" data-filter="files" data-value="no">Empty</span>
</div>
</div></section>

<!-- IP table -->
<section class="py-4"><div class="max-w-7xl mx-auto px-6">
<table class="ip-table">
  <thead>
    <tr>
      <th style="width: 40%;">IP</th>
      <th>Status</th>
      <th>DRI</th>
      <th>Files (repo + cloud)</th>
      <th></th>
    </tr>
  </thead>
  <tbody id="ip-tbody"></tbody>
</table>
</div></section>

<footer class="py-10 mt-10" style="background: var(--ink); color: rgba(255,255,255,0.7);">
<div class="max-w-7xl mx-auto px-6 text-sm">
<div class="mb-2">/docs · back-office · {len(IPS)} IPs · {total_files} repo files (meta + slack + assets) · live Supabase inventory</div>
<div class="mono text-xs">regenerate with <span style="color:white;">python3 tools/build_data/build_docs.py</span></div>
</div>
</footer>

<script>
const INVENTORY = {inventory_json};
const ASSET_BUCKETS = {ASSET_BUCKETS!r};
const ALL_BUCKET_NAMES = [...ASSET_BUCKETS, "slack_extracts"];

// ---- Supabase config ----
const SB_URL_KEY = "fyndrrl_sb_url_v1";
const SB_KEY_KEY = "fyndrrl_sb_key_v1";
const SB_BUCKET_KEY = "fyndrrl_sb_bucket_v1";

function getSb() {{
  return {{
    url: localStorage.getItem(SB_URL_KEY) || "",
    key: localStorage.getItem(SB_KEY_KEY) || "",
    bucket: localStorage.getItem(SB_BUCKET_KEY) || "fyndrrl",
  }};
}}

function isConfigured() {{ const c = getSb(); return c.url && c.key && c.bucket; }}

function updateBanner() {{
  const banner = document.getElementById("sb-banner");
  const status = document.getElementById("sb-status");
  const c = getSb();
  document.getElementById("sb-url").value = c.url;
  document.getElementById("sb-key").value = c.key;
  document.getElementById("sb-bucket").value = c.bucket;
  if (isConfigured()) {{
    banner.classList.remove("unset");
    banner.classList.add("set");
    status.style.color = "var(--green)";
    status.textContent = "Configured · " + c.url + " · bucket " + c.bucket + " · ready";
  }} else {{
    banner.classList.add("unset");
    banner.classList.remove("set");
    status.style.color = "var(--amber)";
    status.textContent = "Not configured · paste your project URL, anon key, and bucket below.";
  }}
}}

document.getElementById("sb-save").addEventListener("click", () => {{
  localStorage.setItem(SB_URL_KEY, document.getElementById("sb-url").value.trim().replace(/\\/$/, ""));
  localStorage.setItem(SB_KEY_KEY, document.getElementById("sb-key").value.trim());
  localStorage.setItem(SB_BUCKET_KEY, document.getElementById("sb-bucket").value.trim());
  updateBanner();
  refreshAllSupabaseLists();
}});

document.getElementById("sb-toggle").addEventListener("click", (e) => {{
  const form = document.getElementById("sb-form");
  const btn = e.target;
  if (form.style.display === "none") {{ form.style.display = "grid"; btn.textContent = "collapse"; }}
  else {{ form.style.display = "none"; btn.textContent = "expand"; }}
}});

updateBanner();

// ---- Supabase Storage REST ----
async function sbList(prefix) {{
  const c = getSb();
  if (!isConfigured()) return [];
  const r = await fetch(`${{c.url}}/storage/v1/object/list/${{c.bucket}}`, {{
    method: "POST",
    headers: {{ "Authorization": `Bearer ${{c.key}}`, "apikey": c.key, "Content-Type": "application/json" }},
    body: JSON.stringify({{ prefix, limit: 200, sortBy: {{ column: "created_at", order: "desc" }} }}),
  }});
  if (!r.ok) {{ console.warn("sb list failed", r.status); return []; }}
  return r.json();
}}

async function sbUpload(path, file) {{
  const c = getSb();
  const r = await fetch(`${{c.url}}/storage/v1/object/${{c.bucket}}/${{path}}`, {{
    method: "POST",
    headers: {{ "Authorization": `Bearer ${{c.key}}`, "apikey": c.key, "x-upsert": "true" }},
    body: file,
  }});
  if (!r.ok) throw new Error(`upload failed ${{r.status}}: ${{await r.text()}}`);
  return r.json();
}}

async function sbDelete(path) {{
  const c = getSb();
  const r = await fetch(`${{c.url}}/storage/v1/object/${{c.bucket}}/${{path}}`, {{
    method: "DELETE",
    headers: {{ "Authorization": `Bearer ${{c.key}}`, "apikey": c.key }},
  }});
  if (!r.ok) throw new Error(`delete failed ${{r.status}}`);
  return r.json();
}}

function sbPublicUrl(path) {{
  const c = getSb();
  return `${{c.url}}/storage/v1/object/public/${{c.bucket}}/${{path}}`;
}}

const cloudFiles = {{}};

async function refreshSupabaseFor(slug) {{
  if (!isConfigured()) return;
  const subs = await sbList(`ips/${{slug}}/`);
  const grouped = {{}};
  for (const b of ALL_BUCKET_NAMES) grouped[b] = [];
  for (const sub of subs) {{
    if (sub.id === null) {{
      const files = await sbList(`ips/${{slug}}/${{sub.name}}/`);
      for (const f of files) {{
        if (f.id === null) continue;
        const bucket = sub.name;
        const path = `ips/${{slug}}/${{bucket}}/${{f.name}}`;
        if (!grouped[bucket]) grouped[bucket] = [];
        grouped[bucket].push({{
          name: f.name,
          size_kb: Math.round((f.metadata?.size || 0) / 1024),
          url: sbPublicUrl(path),
          path,
        }});
      }}
    }}
  }}
  cloudFiles[slug] = grouped;
  return grouped;
}}

async function refreshAllSupabaseLists() {{
  if (!isConfigured()) return;
  let totalCloud = 0;
  for (const ip of INVENTORY) {{
    await refreshSupabaseFor(ip.slug);
    if (cloudFiles[ip.slug]) totalCloud += Object.values(cloudFiles[ip.slug]).reduce((s, arr) => s + arr.length, 0);
  }}
  document.getElementById("cloud-count").textContent = totalCloud;
  renderTable();
}}

// ---- Render ----
let statusFilter = "all";
let filesFilter = "all";
let q = "";
let expandedSlug = null;

function fileCounts(ip) {{
  const repo = {{}};
  let repoTotal = ip.meta_files.length + ip.slack_extracts.length;
  for (const b of ASSET_BUCKETS) {{
    repo[b] = ip.assets[b].length;
    repoTotal += repo[b];
  }}
  repo["meta"] = ip.meta_files.length;
  repo["slack_extracts"] = ip.slack_extracts.length;
  const cloud = {{}};
  let cloudTotal = 0;
  if (cloudFiles[ip.slug]) {{
    for (const b of ALL_BUCKET_NAMES) {{
      cloud[b] = (cloudFiles[ip.slug][b] || []).length;
      cloudTotal += cloud[b];
    }}
  }} else {{
    for (const b of ALL_BUCKET_NAMES) cloud[b] = 0;
  }}
  return {{ repo, cloud, repoTotal, cloudTotal, total: repoTotal + cloudTotal }};
}}

function renderTable() {{
  const tbody = document.getElementById("ip-tbody");
  tbody.innerHTML = "";
  for (const ip of INVENTORY) {{
    const counts = fileCounts(ip);
    const matchesStatus = statusFilter === "all" || ip.status.toLowerCase() === statusFilter;
    const matchesFiles = filesFilter === "all" || (filesFilter === "yes" && counts.total > 0) || (filesFilter === "no" && counts.total === 0);
    const matchesQ = !q || ip.name.toLowerCase().includes(q) || ip.slug.includes(q) || ip.tagline.toLowerCase().includes(q);
    if (!(matchesStatus && matchesFiles && matchesQ)) continue;

    const pillClass = ip.status === "Live" ? "pill-live" : (ip.status === "Pilot" ? "pill-pilot" : "pill-build");
    const dri = ip.dri && ip.dri.length ? ip.dri[0] : "—";

    let pillsHtml = "";
    // meta + slack first as separate badges
    const mr = counts.repo.meta || 0;
    pillsHtml += `<span class="file-count-pill ${{mr>0?'has-files':''}}" title="${{mr}} canonical metadata files">meta <strong>${{mr}}</strong></span>`;
    const sr = counts.repo.slack_extracts || 0;
    const sc = counts.cloud.slack_extracts || 0;
    pillsHtml += `<span class="file-count-pill ${{(sr+sc)>0?'has-files':''}}" title="${{sr}} repo · ${{sc}} cloud">slack <strong>${{sr}}+${{sc}}</strong></span>`;
    for (const b of ASSET_BUCKETS) {{
      const r = counts.repo[b] || 0;
      const cc = counts.cloud[b] || 0;
      const cls = (r + cc) > 0 ? "file-count-pill has-files" : "file-count-pill";
      pillsHtml += `<span class="${{cls}}" title="${{r}} repo · ${{cc}} cloud">${{b}} <strong>${{r}}+${{cc}}</strong></span>`;
    }}

    const row = document.createElement("tr");
    row.className = "ip-row" + (expandedSlug === ip.slug ? " expanded" : "");
    row.dataset.slug = ip.slug;
    row.innerHTML = `
      <td>
        <div class="ip-name">${{ip.name}}</div>
        <div class="ip-meta">${{ip.slug}} · ${{ip.tagline}}</div>
      </td>
      <td><span class="pill ${{pillClass}}">${{ip.status}}</span></td>
      <td class="text-xs" style="color: var(--ink-muted);">${{dri}}</td>
      <td>${{pillsHtml}}</td>
      <td class="text-right">
        <a href="${{ip.web_anchor}}" class="text-xs" style="color: var(--ink-muted);" onclick="event.stopPropagation()" target="_blank">view page →</a>
      </td>
    `;
    row.addEventListener("click", () => toggleDrawer(ip.slug));
    tbody.appendChild(row);

    if (expandedSlug === ip.slug) {{
      const drawerRow = document.createElement("tr");
      drawerRow.className = "ip-drawer-row";
      drawerRow.innerHTML = `<td colspan="5"><div class="ip-drawer" id="drawer-${{ip.slug}}"></div></td>`;
      tbody.appendChild(drawerRow);
      renderDrawer(ip);
    }}
  }}
}}

function toggleDrawer(slug) {{
  expandedSlug = expandedSlug === slug ? null : slug;
  if (expandedSlug && isConfigured() && !cloudFiles[expandedSlug]) {{
    refreshSupabaseFor(expandedSlug).then(renderTable);
  }}
  renderTable();
}}

function fileRowHtml(file, sourceClass) {{
  return `<div class="file-row" ${{file.path?`data-path="${{file.path}}"`:''}}>
    <div class="file-name">${{file.name}}</div>
    <span class="file-source ${{sourceClass}}">${{sourceClass}}</span>
    <span class="file-size">${{file.size_kb}} KB</span>
    <div>${{file.url ? `<a href="${{file.url}}" target="_blank" style="margin-right:10px;">view ↗</a>` : ''}}${{sourceClass==="cloud"?`<button onclick="deleteFile('${{file.slug}}','${{file.path}}','${{file.name}}')">×</button>`:''}}</div>
  </div>`;
}}

function renderDrawer(ip) {{
  const root = document.getElementById(`drawer-${{ip.slug}}`);
  let bucketsHtml = "";

  // 1. Canonical metadata bucket (repo only · these come from spec.py + build.py)
  const metaFiles = ip.meta_files;
  let metaList = metaFiles.length === 0 ? `<div class="empty-list">no metadata yet</div>` : metaFiles.map(f => fileRowHtml({{...f}}, "meta")).join("");
  bucketsHtml += `<div class="bucket-section">
    <div class="bucket-head"><span class="bucket-name">canonical metadata</span><span class="bucket-count">${{metaFiles.length}} in repo</span></div>
    <div class="file-list">${{metaList}}</div>
  </div>`;

  // 2. Slack extracts (repo + cloud)
  const slackRepo = ip.slack_extracts;
  const slackCloud = (cloudFiles[ip.slug] && cloudFiles[ip.slug].slack_extracts) || [];
  let slackList = "";
  if (slackRepo.length === 0 && slackCloud.length === 0) {{
    slackList = `<div class="empty-list">no Slack extracts</div>`;
  }} else {{
    for (const f of slackRepo) slackList += fileRowHtml(f, "slack");
    for (const f of slackCloud) slackList += fileRowHtml({{...f, slug: ip.slug}}, "cloud");
  }}
  bucketsHtml += `<div class="bucket-section">
    <div class="bucket-head"><span class="bucket-name">slack extracts</span><span class="bucket-count">${{slackRepo.length}} repo · ${{slackCloud.length}} cloud</span></div>
    <div class="file-list">${{slackList}}</div>
  </div>`;

  // 3. Asset buckets (repo + cloud)
  for (const b of ASSET_BUCKETS) {{
    const repoFiles = ip.assets[b] || [];
    const cloudList = (cloudFiles[ip.slug] && cloudFiles[ip.slug][b]) || [];
    let listHtml = "";
    if (repoFiles.length === 0 && cloudList.length === 0) {{
      listHtml = `<div class="empty-list">no files yet</div>`;
    }} else {{
      for (const f of repoFiles) listHtml += fileRowHtml(f, "repo");
      for (const f of cloudList) listHtml += fileRowHtml({{...f, slug: ip.slug}}, "cloud");
    }}
    bucketsHtml += `<div class="bucket-section">
      <div class="bucket-head"><span class="bucket-name">${{b}}</span><span class="bucket-count">${{repoFiles.length}} repo · ${{cloudList.length}} cloud</span></div>
      <div class="file-list">${{listHtml}}</div>
    </div>`;
  }}

  const radios = ASSET_BUCKETS.map((b, i) =>
    `<label><input type="radio" name="bucket-${{ip.slug}}" value="${{b}}" ${{i === 0 ? "checked" : ""}} /> ${{b}}</label>`
  ).join("");

  root.innerHTML = `
    <div class="drawer-grid">
      <div>${{bucketsHtml}}</div>
      <div>
        <div class="cap-num mb-2">Upload to ${{ip.name}}</div>
        <div class="bucket-picker">${{radios}}</div>
        <div class="drop-zone" id="drop-${{ip.slug}}">
          <p class="drop-zone-cap">drag &amp; drop · or</p>
          <p><label class="pick-btn"><input type="file" multiple style="display:none" id="file-${{ip.slug}}" /> pick files</label></p>
          <p class="text-xs mt-3" style="color: var(--ink-muted);">Files upload to Supabase at<br/><span class="mono">ips/${{ip.slug}}/&lt;bucket&gt;/&lt;filename&gt;</span></p>
        </div>
        <div id="status-${{ip.slug}}" class="upload-status"></div>
        ${{!isConfigured() ? '<div class="text-xs mt-2" style="color: var(--amber);">Configure Supabase above to enable uploads.</div>' : ''}}
      </div>
    </div>
  `;
  bindUpload(ip.slug);
}}

function bindUpload(slug) {{
  const dz = document.getElementById(`drop-${{slug}}`);
  const fi = document.getElementById(`file-${{slug}}`);
  const status = document.getElementById(`status-${{slug}}`);
  function handleFiles(files) {{
    if (!isConfigured()) {{
      status.textContent = "Supabase not configured · paste credentials above.";
      status.className = "upload-status err"; return;
    }}
    const bucket = document.querySelector(`input[name="bucket-${{slug}}"]:checked`).value;
    runUpload(slug, bucket, Array.from(files), status);
  }}
  fi.addEventListener("change", e => handleFiles(e.target.files));
  ["dragenter","dragover"].forEach(ev => dz.addEventListener(ev, e => {{ e.preventDefault(); dz.classList.add("over"); }}));
  ["dragleave","drop"].forEach(ev => dz.addEventListener(ev, e => {{ e.preventDefault(); dz.classList.remove("over"); }}));
  dz.addEventListener("drop", e => handleFiles(e.dataTransfer.files));
}}

async function runUpload(slug, bucket, files, statusEl) {{
  let ok = 0, errs = [];
  for (const f of files) {{
    statusEl.textContent = `Uploading ${{f.name}}...`;
    statusEl.className = "upload-status";
    try {{
      const path = `ips/${{slug}}/${{bucket}}/${{f.name}}`;
      await sbUpload(path, f);
      ok += 1;
      addRecent(slug, bucket, f.name);
    }} catch (e) {{
      console.error(e);
      errs.push(f.name + ": " + e.message);
    }}
  }}
  if (ok > 0 && errs.length === 0) {{
    statusEl.textContent = `✓ Uploaded ${{ok}} file${{ok > 1 ? 's' : ''}} to ${{bucket}}`;
    statusEl.className = "upload-status ok";
  }} else if (errs.length > 0) {{
    statusEl.textContent = `Failed: ${{errs.join(' · ')}}`;
    statusEl.className = "upload-status err";
  }}
  await refreshSupabaseFor(slug);
  renderTable();
}}

async function deleteFile(slug, path, name) {{
  if (!confirm(`Delete ${{name}} from Supabase?`)) return;
  try {{
    await sbDelete(path);
    await refreshSupabaseFor(slug);
    renderTable();
  }} catch (e) {{ alert("Delete failed: " + e.message); }}
}}
window.deleteFile = deleteFile;

function addRecent(slug, bucket, name) {{
  const strip = document.getElementById("recent-strip");
  const list = document.getElementById("recent-list");
  strip.style.display = "block";
  const pill = document.createElement("span");
  pill.className = "recent-pill";
  pill.innerHTML = `<strong>${{slug}}</strong> · ${{bucket}} · ${{name}}`;
  list.prepend(pill);
  while (list.children.length > 10) list.removeChild(list.lastChild);
}}

document.querySelectorAll(".filter-chip").forEach(chip => {{
  chip.addEventListener("click", () => {{
    const dim = chip.dataset.filter;
    const val = chip.dataset.value;
    document.querySelectorAll(`.filter-chip[data-filter="${{dim}}"]`).forEach(c => c.classList.remove("active"));
    chip.classList.add("active");
    if (dim === "status") statusFilter = val;
    if (dim === "files") filesFilter = val;
    renderTable();
  }});
}});

document.getElementById("ip-search").addEventListener("input", e => {{
  q = e.target.value.toLowerCase();
  renderTable();
}});

document.addEventListener("keydown", e => {{
  if (e.key === "/" && !["INPUT","TEXTAREA"].includes(e.target.tagName)) {{
    e.preventDefault();
    document.getElementById("ip-search").focus();
  }} else if (e.key === "Escape" && expandedSlug) {{
    expandedSlug = null; renderTable();
  }}
}});

renderTable();
if (isConfigured()) refreshAllSupabaseLists();
</script>

</body>
</html>
'''


def main():
    out = DOCS_DIR / "index.html"
    out.write_text(render())
    print(f"✓ Wrote {out.relative_to(ROOT)}")
    repo_files = sum(
        len(collect_ip(ip)["meta_files"])
        + len(collect_ip(ip)["slack_extracts"])
        + sum(len(collect_ip(ip)["assets"][b]) for b in ASSET_BUCKETS)
        for ip in IPS
    )
    print(f"  {len(IPS)} IPs · {repo_files} repo files surfaced (meta + slack + assets)")
    print(f"  + cross-cutting · sources, research, audits at top of page")


if __name__ == "__main__":
    main()
