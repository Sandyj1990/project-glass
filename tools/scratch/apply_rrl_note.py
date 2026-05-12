"""One-shot · apply changes from docs/jcp-notes-compilation/RRL Website
Screenshots/RRL Website Modifications.pdf to:
  - tools/scratch/rbl_synthetic.json  (storefront edits + 4 net-new entries)
  - tools/scratch/non_rbl_channels.json (drop CoverStory's old skip entry)

Run after the PDF_CHANNELS edits in build_jcp_channels_md.py.
Idempotent.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
RBL = ROOT / "tools" / "scratch" / "rbl_synthetic.json"
NON_RBL = ROOT / "tools" / "scratch" / "non_rbl_channels.json"

URL_FIXES = {
    "diesel":       "dieselindia.com",
    "lenscrafters": "lenscrafters.in",
    "coach":        "coach.in",
}

# 4 net-new storefronts.
NEW_STOREFRONTS = [
    {
        "src": "https://socialassets.impetusz0.de/rrl-portfolio/images/jcp-channels/coverstory.png",
        "slug": "coverstory", "brand": "CoverStory",
        "domain": "coverstory.co.in", "vertical": "F&L",
        "loadTime": "—", "accessibility": None,
    },
    {
        "src": "https://socialassets.impetusz0.de/rrl-portfolio/images/jcp-channels/la-martina.png",
        "slug": "la-martina", "brand": "La Martina",
        "domain": "lamartina.com", "vertical": "F&L",
        "loadTime": "—", "accessibility": None,
    },
    {
        "src": "https://socialassets.impetusz0.de/rrl-portfolio/images/jcp-channels/molton-brown.png",
        "slug": "molton-brown", "brand": "Molton Brown",
        "domain": "moltonbrown.com", "vertical": "Beauty",
        "loadTime": "—", "accessibility": None,
    },
    {
        "src": "https://socialassets.impetusz0.de/rrl-portfolio/images/jcp-channels/facegym.png",
        "slug": "facegym", "brand": "Facegym",
        "domain": "facegym.com", "vertical": "Beauty",
        "loadTime": "—", "accessibility": None,
    },
]


def patch_rbl():
    rows = json.loads(RBL.read_text())
    by_slug = {r["slug"]: r for r in rows}

    # Drop Mard
    if "mard" in by_slug:
        del by_slug["mard"]
        print("  removed: mard")

    # URL fixes
    for slug, new_domain in URL_FIXES.items():
        if slug in by_slug:
            old = by_slug[slug].get("domain")
            by_slug[slug]["domain"] = new_domain
            print(f"  url-fix: {slug:18s} {old:25s} → {new_domain}")

    # Append net-new storefronts
    for s in NEW_STOREFRONTS:
        if s["slug"] not in by_slug:
            by_slug[s["slug"]] = s
            print(f"  new:     {s['slug']:18s} ({s['domain']})")
        else:
            print(f"  skip:    {s['slug']:18s} (already present)")

    RBL.write_text(json.dumps(list(by_slug.values()), indent=2))
    print(f"\n  rbl_synthetic.json now has {len(by_slug)} entries")


def patch_non_rbl():
    """Drop the old CoverStory skip entry — it's now an RBL-style storefront."""
    rows = json.loads(NON_RBL.read_text())
    new_rows = [r for r in rows if r.get("slug") != "coverstory"]
    if len(new_rows) != len(rows):
        NON_RBL.write_text(json.dumps(new_rows, indent=2))
        print(f"  removed coverstory from non_rbl_channels.json ({len(rows)} → {len(new_rows)})")
    else:
        print(f"  coverstory not in non_rbl_channels.json (idempotent)")


def main():
    patch_rbl()
    print()
    patch_non_rbl()


if __name__ == "__main__":
    main()
