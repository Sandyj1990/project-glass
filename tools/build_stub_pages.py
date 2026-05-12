"""Generate uniform 'Page in progress' stubs for sections named in the
2026-04-30 letter that don't have a hub page yet. Re-runnable: rewrites
each stub with the latest chrome on every invocation.

Once a section gets a real hub page, REMOVE its slug from STUBS so this
script no longer overwrites it.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from site_chrome import topnav, footer  # noqa: E402

# Each row: (slug, title, eyebrow, blurb, kind)
# kind="first-build"  → "Hub page coming soon · named in 2026-04-30 letter"
# kind="rebuild"      → "Page being rewritten · prior content archived"
#
# Slugs that have been built out (ucp, kaily, pixelbin) are intentionally absent.
# Add a slug back here only if the page needs to revert to a stub.
STUBS = [
    ("boltic",       "Boltic",                     "AI-Native · Agentic automation", "Workflow agents that run AI-first business operations.",         "first-build"),
    ("ratl",         "Ratl",                       "AI-Native · Agentic automation", "AI agent framework used by RBL OS Synthetic Monitor and others.", "first-build"),
    ("fynd-horizon", "Fynd Horizon",               "Recent Innovations",             "Strategy + foresight platform for the Reliance retail estate.",   "first-build"),
    ("autri",        "Autri",                      "Recent Innovations",             "AI-native operations co-pilot.",                                  "first-build"),
    ("dark-factory", "Dark Factory · Made-to-Measure", "Recent Innovations",         "Lights-out manufacturing pilot for Made-to-Measure apparel.",      "first-build"),
    # 2026-05-01 · /rbl/ and /rcpl/ stripped pending re-author. Routes preserved.
    ("rbl",          "RBL · Reliance Brands",      "JCP · customer rollout",         "Reliance Brands portfolio on JCP — premium and luxury fashion houses.", "rebuild"),
    ("rcpl",         "RCPL · Reliance Consumer Products", "JCP · customer rollout",  "Reliance's FMCG arm — owned grocery + personal care brands distributed on JCP.", "rebuild"),
]


def render(slug: str, title: str, eyebrow: str, blurb: str, kind: str = "first-build") -> str:
    if kind == "rebuild":
        card_label = "Being rewritten"
        card_h2 = "Hub page is being rewritten."
        card_body = (
            "Prior content was a placeholder draft from v0.6 (29-Apr-2026); it has been "
            "removed pending a fresh author pass. The route stays live in navigation so "
            "external references don't break."
        )
    else:
        card_label = "Page in progress"
        card_h2 = "Hub page coming soon."
        card_body = (
            "This section is named in the 2026-04-30 letter to MM Sir but its hub page is "
            "still being authored. The link is wired through the global navigation so it "
            "stays discoverable from day one."
        )
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{title} · Fynd × RRVL · JPL</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<script src="/auth.js"></script>
<script src="https://cdn.tailwindcss.com"></script>
<link rel="icon" type="image/png" href="/assets/fynd-logo.png">
<link rel="stylesheet" href="/style.css">
</head>
<body>
{topnav(active="tracks")}

<section class="pt-20 pb-32"><div class="max-w-7xl mx-auto px-6">
  <div class="crumb mb-6"><a href="/">Home</a> <span class="sep">/</span> <span style="color: var(--ink);">{title}</span></div>
  <div class="section-label mb-3">{eyebrow} · placeholder</div>
  <h1 class="display text-5xl md:text-7xl mb-6" style="color: var(--ink);">{title}.</h1>
  <p class="text-lg max-w-3xl mb-10" style="color: var(--ink-muted);">{blurb}</p>

  <div class="card p-8 max-w-2xl">
    <div class="cap-num mb-3">{card_label}</div>
    <h2 class="font-semibold text-xl mb-3" style="color: var(--ink);">{card_h2}</h2>
    <p class="text-base mb-4" style="color: var(--ink);">
      {card_body}
    </p>
    <p class="text-sm" style="color: var(--ink-muted);"><strong>Owner:</strong> TBD · <strong>ETA:</strong> TBD</p>
  </div>
</div></section>

{footer()}
</body>
</html>
"""


def main() -> int:
    for row in STUBS:
        slug, title, eyebrow, blurb, kind = row
        out = ROOT / slug / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render(slug, title, eyebrow, blurb, kind))
        print(f"  wrote /{slug}/  ({kind:12s}  {len(out.read_text()):,} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
