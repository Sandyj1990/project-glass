"""Emit jcp/channels/index.html — visual gallery of every JCP channel.

Reads the same three sources as build_jcp_channels_md.py:
  - PDF channel directory (encoded in build_jcp_channels_md.py),
  - tools/scratch/rbl_synthetic.json   (storefront screenshots),
  - tools/scratch/non_rbl_play.json    (mobile apps).

Layout mirrors impetus/videos/index.html:
  - Topnav + crumb + hero + sub-nav matching v0.8.4 chrome
  - Filter chip strip (All / Storefront / Mobile App / In-Store · B2B / Cluster)
  - Three card sections: Storefronts (31) · Mobile apps (13) · Other surfaces (34)
  - Lightbox for click-to-zoom on screenshots
"""
from __future__ import annotations

import html
import json
import sys
from pathlib import Path

from build_jcp_channels_md import PDF_CHANNELS, SKIP_REASONS  # type: ignore

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from site_chrome import topnav, footer, subnav_html  # noqa: E402

SCRATCH = ROOT / "tools" / "scratch"
OUT = ROOT / "jcp" / "channels" / "index.html"
H = html.escape

# Public CDN that mirrors the local images/ tree.
CDN_BASE = "https://socialassets.impetusz0.de/rrl-portfolio"


def cdn(path: str) -> str:
    return f"{CDN_BASE}/images/{path}"


LOCAL_STYLES = """
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

.status-pill {
  display: inline-block; font-family: 'JetBrains Mono', monospace; font-size: 9.5px;
  text-transform: uppercase; letter-spacing: 0.04em;
  padding: 2px 7px; border-radius: 3px;
}
.status-live { background: #ECFDF5; color: #047857; border: 1px solid #BBF7D0; }
.status-progress { background: #FFFBEB; color: #B45309; border: 1px solid #FDE68A; }
.status-planned { background: #F3F4F6; color: #4B5563; border: 1px solid #D1D5DB; }

/* Storefront card · 16:9 desktop screenshot */
.shot-card {
  background: white; border: 1px solid var(--border); border-radius: 8px;
  overflow: hidden; transition: all 0.15s;
}
.shot-card:hover { border-color: var(--ink); transform: translateY(-2px); }
.shot-thumb {
  position: relative; aspect-ratio: 16/9; background: var(--bg-soft);
  border-bottom: 1px solid var(--border); cursor: zoom-in;
  overflow: hidden;
}
.shot-thumb img { width: 100%; height: 100%; object-fit: cover; object-position: top center; display: block; }
.shot-thumb .meta-badge {
  position: absolute; top: 6px; right: 6px;
  font-family: 'JetBrains Mono', monospace; font-size: 9.5px;
  background: rgba(0,0,0,0.6); color: white; padding: 2px 6px; border-radius: 3px;
}

/* App card · phone-shaped 9:16 screenshot with icon overlay */
.app-card {
  background: white; border: 1px solid var(--border); border-radius: 8px;
  overflow: hidden; transition: all 0.15s;
}
.app-card:hover { border-color: var(--ink); transform: translateY(-2px); }
.app-thumb {
  position: relative; aspect-ratio: 9/16; background: var(--bg-soft);
  border-bottom: 1px solid var(--border); cursor: zoom-in;
  overflow: hidden;
}
.app-thumb img { width: 100%; height: 100%; object-fit: cover; object-position: center top; display: block; }
.app-thumb .icon-overlay {
  position: absolute; top: 8px; left: 8px;
  width: 40px; height: 40px; border-radius: 8px;
  border: 2px solid white; box-shadow: 0 2px 6px rgba(0,0,0,0.15);
  background: white;
}
.app-thumb .icon-overlay img { width: 100%; height: 100%; object-fit: cover; }

/* Skipped card · text-only minimal */
.skip-card {
  background: var(--bg-soft); border: 1px dashed var(--border);
  border-radius: 8px; padding: 14px 16px;
}
.skip-card .reason {
  font-size: 12px; color: var(--ink-muted); line-height: 1.4; margin-top: 6px;
}

/* Lightbox */
.lightbox {
  position: fixed; inset: 0; background: rgba(0,0,0,0.92); z-index: 100;
  display: none; align-items: center; justify-content: center; padding: 4vh 4vw;
}
.lightbox.open { display: flex; }
.lightbox img { max-width: 100%; max-height: 100%; object-fit: contain; }
.lightbox .close {
  position: absolute; top: 18px; right: 22px; color: white; font-size: 32px;
  line-height: 1; cursor: pointer; opacity: 0.7;
}
.lightbox .close:hover { opacity: 1; }
.lightbox .meta {
  position: absolute; bottom: 14px; left: 22px; color: white; opacity: 0.85;
  font-family: 'JetBrains Mono', monospace; font-size: 11px; letter-spacing: 0.04em;
}
"""


def load_data():
    rbl_rows = json.loads((SCRATCH / "rbl_synthetic.json").read_text())
    play_rows = json.loads((SCRATCH / "non_rbl_play.json").read_text())
    rbl = {r["slug"]: r for r in rbl_rows}
    play = {r["slug"]: r for r in play_rows}
    return rbl, play


def status_class(status: str) -> str:
    s = status.lower()
    if "live" in s:
        return "status-live"
    if "progress" in s:
        return "status-progress"
    return "status-planned"


def render_storefront(num, name, slug, model, vertical, status, cluster, fmt, remarks, rbl_row):
    domain = rbl_row["domain"]
    href = f"https://{domain}" if not domain.startswith("http") else domain
    img = cdn(f"jcp-channels/{slug}.png")
    return f"""
<article class="shot-card channel-card"
  data-slug="{H(slug)}" data-cluster="{H(cluster)}" data-status="{H(status)}" data-surface="storefront" data-vertical="{H(vertical)}">
  <div class="shot-thumb" onclick="zoomImage('{H(img)}', '{H(name)} · {H(domain)}')">
    <img src="{H(img)}" alt="{H(name)} storefront" loading="lazy" />
    <span class="meta-badge">{H(rbl_row['loadTime'])} · a11y {rbl_row['accessibility']}</span>
  </div>
  <div class="p-4">
    <div class="flex items-center gap-2 mb-2 flex-wrap">
      <span class="status-pill {status_class(status)}">{H(status)}</span>
    </div>
    <h3 class="font-semibold text-sm mb-1" style="color: var(--ink);">{H(name)}</h3>
    <a href="{H(href)}" target="_blank" rel="noopener" class="text-xs mono accent" style="text-decoration: underline; word-break: break-all;">{H(domain)} ↗</a>
    <div class="text-xs mt-2" style="color: var(--ink-muted);">{H(vertical)}{(' · ' + H(remarks)) if remarks else ''}</div>
  </div>
</article>
"""


def render_app(num, name, slug, model, vertical, status, cluster, fmt, remarks, play_row):
    pkg = play_row.get("play_package_id", "")
    play_url = play_row.get("play_url", f"https://play.google.com/store/apps/details?id={pkg}")
    primary = play_row.get("primary_shot", 1)
    # `primary_shot_override` is a hand-curated path (e.g. "accenture-s33-img03.png")
    # under the slug folder. When set, takes precedence over the auto-numbered shot.
    override = play_row.get("primary_shot_override")
    icon = cdn(f"jcp-channels/{slug}/icon.png")
    shot = cdn(f"jcp-channels/{slug}/{override}") if override else cdn(f"jcp-channels/{slug}/shot-{primary}.png")
    # Optional small badge (e.g. "in-store companion · staff app" for Trends)
    badge = play_row.get("badge")
    badge_html = f'<span class="status-pill" style="background: #FEF3C7; color: #92400E; border: 1px solid #FDE68A;">{H(badge)}</span>' if badge else ""
    # Caption text in the lightbox
    caption_suffix = "Play Store" if not override else "Accenture · 16-Apr-2026"
    # Optional icon (Trends has no Play Store, hence no icon — render without overlay)
    icon_overlay = f'<div class="icon-overlay"><img src="{H(icon)}" alt="" loading="lazy" /></div>' if play_row.get("has_icon", True) else ""
    return f"""
<article class="app-card channel-card"
  data-slug="{H(slug)}" data-cluster="{H(cluster)}" data-status="{H(status)}" data-surface="mobile-app" data-vertical="{H(vertical)}">
  <div class="app-thumb" onclick="zoomImage('{H(shot)}', '{H(name)} · {H(caption_suffix)}')">
    <img src="{H(shot)}" alt="{H(name)} app" loading="lazy" />
    {icon_overlay}
  </div>
  <div class="p-4">
    <div class="flex items-center gap-2 mb-2 flex-wrap">
      <span class="status-pill {status_class(status)}">{H(status)}</span>
      {badge_html}
    </div>
    <h3 class="font-semibold text-sm mb-1" style="color: var(--ink);">{H(name)}</h3>
    <div class="text-xs" style="color: var(--ink-muted);">{H(vertical)}{(' · ' + H(remarks)) if remarks else ''}</div>
  </div>
</article>
"""


def render_skipped(num, name, slug, model, vertical, status, cluster, fmt, remarks):
    reason = SKIP_REASONS.get(slug, "no public consumer surface")
    return f"""
<article class="skip-card channel-card"
  data-slug="{H(slug)}" data-cluster="{H(cluster)}" data-status="{H(status)}" data-surface="other" data-vertical="{H(vertical)}">
  <div class="flex items-center gap-2 flex-wrap mb-1">
    <span class="status-pill {status_class(status)}">{H(status)}</span>
    <span class="text-xs mono" style="color: var(--ink-muted);">{H(fmt)}</span>
  </div>
  <h3 class="font-semibold text-sm" style="color: var(--ink);">{H(name)}</h3>
  <div class="text-xs mt-1" style="color: var(--ink-muted);">{H(vertical)}{(' · ' + H(remarks)) if remarks else ''}</div>
  <div class="reason">{H(reason)}</div>
</article>
"""


EXTRA_APPS = [
    # Web-wrapped Android apps that ship alongside an existing storefront card.
    # Don't bump the channel count (PDF_CHANNELS stays the canonical 78 ± Mard).
    {
        "slug": "superdry-app", "name": "Superdry India · App",
        "vertical": "F&L", "cluster": "FP", "status": "Live",
        "format": "Android", "remarks": "Web-wrapped storefront on Play Store",
        "play_url": "https://play.google.com/store/search?q=superdry+india&c=apps",
        "primary_shot_override": "shot-1.png",
        "badge": "web-wrapped app",
        "has_icon": False,
    },
    {
        "slug": "hamleys-app", "name": "Hamleys India · App",
        "vertical": "Toys & Kids", "cluster": "FP", "status": "Live",
        "format": "Android", "remarks": "Web-wrapped storefront on Play Store",
        "play_url": "https://play.google.com/store/search?q=hamleys+india&c=apps",
        "primary_shot_override": "shot-1.png",
        "badge": "web-wrapped app",
        "has_icon": False,
    },
    {
        "slug": "sephora-app", "name": "Sephora India · App",
        "vertical": "Beauty", "cluster": "FP", "status": "Live",
        "format": "Android", "remarks": "Consumer app on Play Store",
        "play_url": "https://play.google.com/store/search?q=sephora+india&c=apps",
        "primary_shot_override": "shot-1.png",
        "badge": "consumer app",
        "has_icon": False,
    },
]


def main():
    rbl, play = load_data()

    storefronts, apps, skipped = [], [], []
    for row in PDF_CHANNELS:
        num, name, slug, model, vertical, status, cluster, fmt, remarks = row
        if slug in rbl:
            storefronts.append(render_storefront(*row, rbl_row=rbl[slug]))
        elif slug in play and play[slug].get("status") == "ok":
            apps.append(render_app(*row, play_row=play[slug]))
        else:
            skipped.append(render_skipped(*row))

    # Render extra app cards (not in PDF_CHANNELS — additional surfaces of
    # existing brands; don't affect the channel count).
    for ea in EXTRA_APPS:
        apps.append(render_app(
            num=None, name=ea["name"], slug=ea["slug"], model="B2C",
            vertical=ea["vertical"], status=ea["status"], cluster=ea["cluster"],
            fmt=ea["format"], remarks=ea["remarks"],
            play_row=ea,
        ))

    page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Channels · JCP · Fynd × RRVL · JPL</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<script src="/auth.js"></script>
<script src="https://cdn.tailwindcss.com"></script>
<link rel="icon" type="image/png" href="/assets/fynd-logo.png">
<link rel="stylesheet" href="/style.css">
<style>{LOCAL_STYLES}</style>
</head>
<body>
{topnav(active="tracks")}

<section class="pt-16 pb-10 border-b" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
  <div class="crumb mb-6"><a href="/">Home</a> <span class="sep">/</span> <a href="/jcp">JCP</a> <span class="sep">/</span> <span style="color: var(--ink);">Channels</span></div>
  <div class="section-label mb-3">JCP · Channel Coverage · 79 channels</div>
  <h1 class="display text-5xl md:text-7xl mb-6" style="color: var(--ink);">Channels.</h1>
  <p class="text-lg max-w-3xl mb-8" style="color: var(--ink-muted);">
    Every storefront and mobile app the JioCommerce Platform powers across Reliance Retail — websites, in-store kiosks, marketplaces and OMS.
  </p>
  {subnav_html("jcp", "/jcp/channels")}
  <div class="grid grid-cols-2 md:grid-cols-4 gap-3 max-w-4xl">
    <div class="card p-4"><div class="cap-num mb-1">Total channels</div><div class="display-2 text-3xl" style="color: var(--ink);">78</div></div>
    <div class="card p-4"><div class="cap-num mb-1">Storefronts captured</div><div class="display-2 text-3xl accent">{len(storefronts)}</div></div>
    <div class="card p-4"><div class="cap-num mb-1">Mobile apps captured</div><div class="display-2 text-3xl accent">{len(apps)}</div></div>
    <div class="card p-4"><div class="cap-num mb-1">In-store / B2B / planned</div><div class="display-2 text-3xl" style="color: var(--ink-muted);">{len(skipped)}</div></div>
  </div>
</div></section>

<section class="py-8 border-b" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
  <div class="cap-num mb-3">Filter by surface</div>
  <div class="flex flex-wrap gap-2" id="surface-filters">
    <button class="filter-chip active" data-filter="surface" data-value="all">All <span class="count">· 78</span></button>
    <button class="filter-chip" data-filter="surface" data-value="mobile-app">Mobile apps <span class="count">· {len(apps)}</span></button>
    <button class="filter-chip" data-filter="surface" data-value="storefront">Storefronts <span class="count">· {len(storefronts)}</span></button>
    <button class="filter-chip" data-filter="surface" data-value="other">In-store · B2B · planned <span class="count">· {len(skipped)}</span></button>
  </div>
</div></section>

<section class="py-12 border-b" id="section-apps" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
  <div class="section-label mb-3">Mobile apps · {len(apps)}</div>
  <h2 class="display-2 text-2xl md:text-3xl mb-2" style="color: var(--ink);">Consumer apps we power.</h2>
  <p class="text-sm max-w-3xl mb-8" style="color: var(--ink-muted);">First phone screenshot from each app's Google Play Store listing. Click any tile to zoom; click ↗ to open the listing.</p>
  <div id="grid-apps" class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-5">
    {''.join(apps)}
  </div>
</div></section>

<section class="py-12 border-b" id="section-storefronts" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
  <div class="section-label mb-3">Storefronts · {len(storefronts)}</div>
  <h2 class="display-2 text-2xl md:text-3xl mb-8" style="color: var(--ink);">Live websites we power.</h2>
  <div id="grid-storefronts" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
    {''.join(storefronts)}
  </div>
</div></section>

<section class="py-12 border-b" id="section-other" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
  <div class="section-label mb-3">In-store · B2B · planned · {len(skipped)}</div>
  <h2 class="display-2 text-2xl md:text-3xl mb-2" style="color: var(--ink);">No public consumer surface.</h2>
  <p class="text-sm max-w-3xl mb-8" style="color: var(--ink-muted);">Channels powered by JCP that don't have a separate consumer storefront or app — surfaced via the Companion App, StoreOS, kiosks, partner apps, B2B portals or sites under construction.</p>
  <div id="grid-other" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3">
    {''.join(skipped)}
  </div>
</div></section>

<div id="lightbox" class="lightbox" onclick="closeLightbox(event)">
  <span class="close" onclick="closeLightbox(event)">×</span>
  <img id="lightbox-img" src="" alt="" />
  <div id="lightbox-meta" class="meta"></div>
</div>

{footer()}

<script>
const surfaceFilters = document.querySelectorAll('#surface-filters .filter-chip');
const cards = document.querySelectorAll('.channel-card');
const sectionAnchors = {{
  'storefront': document.getElementById('section-storefronts'),
  'mobile-app': document.getElementById('section-apps'),
  'other':      document.getElementById('section-other'),
}};
let activeSurface = 'all';

function applyFilters() {{
  cards.forEach(c => {{
    const ms = activeSurface === 'all' || c.dataset.surface === activeSurface;
    c.style.display = ms ? '' : 'none';
  }});
  // Hide entire sections if they have zero visible cards.
  Object.entries(sectionAnchors).forEach(([surface, el]) => {{
    if (!el) return;
    const anyVisible = el.querySelectorAll('.channel-card:not([style*="display: none"])').length > 0;
    el.style.display = anyVisible ? '' : 'none';
  }});
}}

surfaceFilters.forEach(b => b.addEventListener('click', () => {{
  surfaceFilters.forEach(x => x.classList.remove('active'));
  b.classList.add('active');
  activeSurface = b.dataset.value;
  applyFilters();
}}));

function zoomImage(src, meta) {{
  const lb = document.getElementById('lightbox');
  document.getElementById('lightbox-img').src = src;
  document.getElementById('lightbox-meta').textContent = meta || '';
  lb.classList.add('open');
}}
function closeLightbox(e) {{
  if (e && e.target.tagName === 'IMG') return;
  document.getElementById('lightbox').classList.remove('open');
}}
document.addEventListener('keydown', (e) => {{ if (e.key === 'Escape') closeLightbox(); }});
</script>
</body>
</html>
"""

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(page)
    print(f"Wrote {OUT} ({len(page):,} bytes)")
    print(f"  storefronts={len(storefronts)} apps={len(apps)} other={len(skipped)}")


if __name__ == "__main__":
    main()
