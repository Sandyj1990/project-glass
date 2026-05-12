"""Emit docs/jcp-channels-spec.md from:
  - the canonical 78-row JCP channel directory (encoded below, sourced from
    docs/jcp-notes-compilation/Channel_Coverage_JCP.pdf · Feb 21, 2026),
  - tools/scratch/rbl_synthetic.json   (31 RBL storefront screenshots),
  - tools/scratch/non_rbl_play.json    (13 Play Store apps + skip metadata).

Each channel row resolves to one of three surface types:
  - storefront  -> RBL synthetic monitor screenshot, links to live site
  - mobile-app  -> Play Store icon + first phone screenshot, links to store
  - skipped     -> no public consumer surface (B2B, in-store/OMS only,
                   non-commerce site, planned, etc.) — listed for completeness
                   with a short reason.

The output is structured so a small builder can later turn it into HTML.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRATCH = ROOT / "tools" / "scratch"
OUT = ROOT / "docs" / "jcp-channels-spec.md"

# Public CDN that mirrors the local images/ tree.
# Files are uploaded with `gsutil -m -q rsync -r -x '.*\.json$' images/jcp-channels/
#   gs://impetus-socialpilot/rrl-portfolio/images/jcp-channels/`.
CDN_BASE = "https://socialassets.impetusz0.de/rrl-portfolio"


def cdn(path: str) -> str:
    return f"{CDN_BASE}/images/{path}"


# Canonical channel directory from the JCP Channel Coverage PDF (Feb 21, 2026).
# (num, name, slug, model, vertical, status, cluster, format, remarks)
PDF_CHANNELS = [
    (1,  "Metro Kirana",         "metro-kirana",        "B2B", "Grocery",                       "Live",         "JMP",              "Website",            ""),
    (2,  "Ajio DMS",              "ajio-dms",            "B2B", "F&L",                           "Live",         "JMP",              "Website",            ""),
    (3,  "RCPL",                  "rcpl",                "B2B", "Grocery",                       "Live",         "JMP",              "Website",            ""),
    (4,  "Farmer",                "farmer",              "B2B", "Agriculture",                   "To Be Planned","JMP",              "Website",            ""),
    (5,  "Jiomart Digital ASP, B2B, StoreSell, COFO", "jiomart-digital", "B2B", "Electronics", "Live", "JMD", "Website", "Website live for BPL, Kelvinator, MyLyf, Wyzr"),
    (6,  "Reliance Digital",      "reliance-digital",    "B2C", "Electronics",                   "Live",         "JMD",              "Website",            ""),
    (7,  "PBG Websites",          "pbg-websites",        "B2C", "Electronics",                   "Live",         "JMD",              "Website",            ""),
    (8,  "Tira",                  "tira",                "B2C", "Beauty",                        "Live",         "Tira",             "Website",            ""),
    (9,  "Jiomart",               "jiomart",             "B2C", "Grocery, Electronics, F&L",     "Live",         "Jiomart-RHOS",     "Website",            "30% rollout"),
    (10, "Ajio",                  "ajio",                "B2C", "F&L",                           "In-Progress",  "Ajio",             "Website",            ""),
    (11, "Netmeds",               "netmeds",             "B2C", "Pharma",                        "Live",         "Netmeds",          "Website",            ""),
    (12, "Swadesh",               "swadesh",             "B2C", "Furniture",                     "Live",         "Swadesh",          "Website",            "India website live, International in-progress"),
    (13, "Urban Ladder",          "urban-ladder",        "B2C", "Furniture",                     "Live",         "Swadesh",          "Website",            "Phase 1 live, Phase 2 in-progress"),
    (14, "Reliance Jewels",       "reliance-jewels",     "B2C", "Jewellery",                     "Live",         "SNG",              "Website",            ""),
    (15, "Jiogames",              "jiogames",            "B2C", "Digital Top-Up",                "Live",         "SNG",              "Website",            ""),
    (16, "7-Eleven",              "7eleven",             "B2C", "Fresh Food",                    "Live",         "SNG",              "Marketplace",        "Integration with Zomato & Swiggy"),
    (17, "Freshpik",              "freshpik",            "B2C", "Grocery",                       "Live",         "SNG",              "Website",            ""),
    (18, "Milkbasket",            "milkbasket",          "B2C", "Grocery",                       "Live",         "Jiomart Headless", "Website",            "Live on JCP only for cataloguing"),
    (19, "Amante",                "amante",              "B2C", "F&L",                           "To Be Planned","SNG",              "Website, Marketplace",""),
    (20, "Zivame",                "zivame",              "B2C", "F&L",                           "To Be Planned","SNG",              "Website, Marketplace",""),
    (21, "Clovia",                "clovia",              "B2C", "F&L",                           "To Be Planned","SNG",              "Website, Marketplace",""),
    (22, "Trends",                "trends",              "B2C", "F&L",                           "Live",         "SNG",              "In-Store, Website",  "Non-Commerce Website. Live with Companion App in 2 stores. Kiosk deployment planned."),
    (23, "Yousta",                "yousta",              "B2C", "F&L",                           "Live",         "SNG",              "In-Store",           "Website in-progress"),
    (24, "Azorte",                "azorte",              "B2C", "F&L",                           "Live",         "SNG",              "In-Store",           "Website in-progress"),
    (25, "Fashion Factory",       "fashion-factory",     "B2C", "F&L",                           "Live",         "SNG",              "In-Store",           "Live with Kiosk"),
    (26, "Centro",                "centro",              "B2C", "F&L",                           "Live",         "SNG",              "Website",            ""),
    (27, "Trends Footwear",       "trends-footwear",     "B2C", "F&L",                           "Live",         "SNG",              "Website",            ""),
    (28, "Performax",             "performax",           "B2C", "F&L",                           "Live",         "SNG",              "Website",            "Non-Commerce Website"),
    (29, "PRET",                  "pret",                "B2C", "Fresh Food",                    "Live",         "FP",               "Website",            "Non-Commerce Website"),
    (30, "SuperDry",              "superdry",            "B2C", "F&L",                           "Live",         "FP",               "Website, In-Store",  ""),
    (31, "Sunglasshut India",     "sunglasshut",         "B2C", "F&L",                           "Live",         "FP",               "Website, In-Store",  ""),
    (32, "Armani Exchange",       "armani-exchange",     "B2C", "F&L",                           "Live",         "FP",               "Website, In-Store",  ""),
    (33, "Muji",                  "muji",                "B2C", "F&L, Beauty, Home Decor, Electronics", "Live",  "FP",               "Website",            ""),
    (34, "AFEW by Rahul Mishra",  "afew-rahul-mishra",   "B2C", "F&L",                           "Live",         "FP",               "Website",            ""),
    (35, "Gulabo",                "gulabo",              "B2C", "F&L",                           "Live",         "FP",               "Website",            ""),
    (36, "AKOK",                  "akok",                "B2C", "F&L",                           "Live",         "FP",               "Website",            ""),
    (37, "Vision Express",        "vision-express",      "B2C", "F&L",                           "Live",         "FP",               "Website",            "Non-Commerce Website. Commerce Website development in-progress"),
    (38, "Steve Madden",          "steve-madden",        "B2C", "F&L",                           "Live",         "FP",               "Website, In-Store",  ""),
    (39, "Pottery Barn Kids",     "pottery-barn-kids",   "B2C", "Furniture",                     "Live",         "FP",               "Website",            ""),
    (40, "Charles Tyrwhitt",      "charles-tyrwhitt",    "B2C", "F&L",                           "Live",         "FP",               "Website, In-Store",  ""),
    # (41, "Mard", ...) — REMOVED per RRL-Website-Modifications note: brand has shut its website down.
    (42, "Sephora",               "sephora",             "B2C", "Beauty",                        "Live",         "FP",               "Website",            ""),
    (43, "Pottery Barn",          "pottery-barn",        "B2C", "Furniture",                     "Live",         "FP",               "Website",            ""),
    (44, "Ed-A-Mamma",            "ed-a-mamma",          "B2C", "F&L",                           "Live",         "FP",               "Website",            ""),
    (45, "Brooks Brothers",       "brooks-brothers",     "B2C", "F&L",                           "Live",         "FP",               "Website, In-Store",  ""),
    (46, "Diesel",                "diesel",              "B2C", "F&L",                           "Live",         "FP",               "Website, In-Store",  ""),
    (47, "West Elm",              "westelm",             "B2C", "Furniture",                     "Live",         "FP",               "Website",            ""),
    (48, "Mothercare",            "mothercare",          "B2C", "F&L, Beauty",                   "Live",         "FP",               "Website, In-Store",  ""),
    (49, "Gas Jeans",             "gas-jeans",           "B2C", "F&L",                           "Live",         "FP",               "Website, In-Store",  ""),
    (50, "Tiffany",               "tiffany",             "B2C", "F&L",                           "Live",         "FP",               "Website",            ""),
    (51, "Bally",                 "bally",               "B2C", "F&L",                           "Live",         "FP",               "Website",            ""),
    (52, "Hamleys",               "hamleys",             "B2C", "F&L",                           "Live",         "FP",               "Website",            ""),
    (53, "Tumi",                  "tumi",                "B2C", "F&L",                           "Live",         "FP",               "Website",            ""),
    (54, "Ritu Kumar",            "ritu-kumar",          "B2C", "F&L",                           "Live",         "FP",               "Website",            ""),
    (55, "Satya Paul",            "satya-paul",          "B2C", "F&L",                           "Live",         "FP",               "Website, In-Store",  ""),
    (56, "Hunkemoller",           "hunkemoller",         "B2C", "F&L",                           "Live",         "FP",               "Website, In-Store",  ""),
    (57, "Centro Shoes",          "centro-shoes",        "B2C", "F&L",                           "Live",         "FP",               "Website",            ""),
    (58, "CoverStory",            "coverstory",          "B2C", "F&L",                           "Live",         "FP",               "Website",            ""),
    (59, "ADIDAS Kids",           "adidas-kids",         "B2C", "F&L",                           "Live",         "FP",               "In-Store, OMS",      ""),
    (60, "Kate Spade",            "kate-spade",          "B2C", "F&L",                           "Live",         "FP",               "In-Store, OMS",      "Website development planned"),
    (61, "VERSACE",               "versace",             "B2C", "F&L",                           "Live",         "FP",               "In-Store, OMS",      ""),
    (62, "Tory Burch",            "tory-burch",          "B2C", "F&L",                           "Live",         "FP",               "In-Store, OMS",      "Website development planned"),
    (63, "Scotch & Soda",         "scotch-soda",         "B2C", "F&L",                           "Live",         "FP",               "In-Store, OMS",      ""),
    (64, "Paul Smith",            "paul-smith",          "B2C", "F&L",                           "Live",         "FP",               "In-Store, OMS",      ""),
    (65, "Paul & Shark",          "paul-shark",          "B2C", "F&L",                           "Live",         "FP",               "In-Store, OMS",      ""),
    (66, "Michael Kors",          "michael-kors",        "B2C", "F&L",                           "Live",         "FP",               "In-Store, OMS",      ""),
    (67, "La Martina",            "la-martina",          "B2C", "F&L",                           "In-Progress",  "FP",               "Website, In-Store",  "International site live; India website going live next week (2026-05)"),
    (68, "Emporio Armani",        "emporio-armani",      "B2C", "F&L",                           "Live",         "FP",               "In-Store, OMS",      ""),
    (69, "EA7 Emporio Armani",    "ea7-emporio-armani",  "B2C", "F&L",                           "Live",         "FP",               "In-Store, OMS",      ""),
    (70, "Dune London",           "dune-london",         "B2C", "F&L",                           "Live",         "FP",               "In-Store, OMS",      ""),
    (71, "BOSS",                  "boss",                "B2C", "F&L",                           "Live",         "FP",               "In-Store, OMS",      ""),
    (72, "Catwalk",               "catwalk",             "B2C", "F&L",                           "Live",         "FP",               "Website",            "Non-Commerce Website"),
    (73, "Avantra",               "avantra",             "B2C", "F&L",                           "Live",         "FP",               "Website",            "Non-Commerce Website"),
    (74, "LensCrafters",          "lenscrafters",        "B2C", "F&L",                           "Live",         "FP",               "Website",            ""),
    (75, "Coach",                 "coach",               "B2C", "F&L",                           "Live",         "FP",               "Website",            ""),
    (76, "GAP",                   "gap",                 "B2C", "F&L",                           "In-Progress",  "FP",               "Website, In-Store",  ""),
    (77, "Kiko Milano",           "kiko-milano",         "B2C", "F&L",                           "Planned",      "FP",               "Website",            ""),
    (78, "AJSK",                  "ajsk",                "B2C", "F&L",                           "In-Progress",  "FP",               "Website",            "Non-Commerce Website"),
    # ── 2026-05-01 RRL Website Modifications note · 2 net-new channels (CoverStory + La Martina already existed at #58 + #67) ──
    (79, "Molton Brown",          "molton-brown",        "B2C", "Beauty",                        "Planned",      "FP",               "Website",            "D2C site planned; international live"),
    (80, "Facegym",               "facegym",             "B2C", "Beauty",                        "In-Progress",  "FP",               "Website",            "Non-commerce site in progress; international live"),
]

# Channels with no public consumer surface — surfaced via Companion App / StoreOS
# or non-commerce/planned. Reasons mirror the per-slug skip_reason in
# tools/scratch/non_rbl_channels.json.
SKIP_REASONS = {
    "ajio-dms":          "B2B distribution platform · no consumer surface",
    "rcpl":              "B2B Reliance Consumer Products distribution · no consumer app",
    "farmer":            "Channel in planning stage · no live surface",
    "jiomart-digital":   "B2B platform · storefront sites for BPL · Kelvinator · MyLyf · Wyzr",
    "pbg-websites":      "Premium Business Group website portfolio · no single consumer app",
    "amante":            "JCP onboarding planned",
    "zivame":            "JCP onboarding planned",
    "clovia":            "JCP onboarding planned",
    "trends":            "In-Store + non-commerce site · powered via Companion App + StoreOS",
    "yousta":            "In-Store today · website in-progress",
    "azorte":            "In-Store today · website in-progress",
    "fashion-factory":   "In-Store + Kiosk · no consumer app",
    "performax":         "Non-commerce site · no consumer app",
    "pret":              "Non-commerce site · no consumer app",
    "trends-footwear":   "Web-only sub-brand of Trends · no standalone app",
    "swadesh":           "Website-only craft commerce channel · no consumer app",
    "centro-shoes":      "Web-only · no consumer app",
    "adidas-kids":       "In-Store / OMS only · powered via Companion App + StoreOS",
    "kate-spade":        "In-Store / OMS only · website development planned",
    "versace":           "In-Store / OMS only · powered via Companion App + StoreOS",
    "tory-burch":        "In-Store / OMS only · website development planned",
    "scotch-soda":       "In-Store / OMS only · powered via Companion App + StoreOS",
    "paul-smith":        "In-Store / OMS only · powered via Companion App + StoreOS",
    "paul-shark":        "In-Store / OMS only · powered via Companion App + StoreOS",
    "michael-kors":      "In-Store / OMS only · powered via Companion App + StoreOS",
    # "la-martina" — removed; now a storefront (international site live; India coming next week)
    "emporio-armani":    "In-Store / OMS only · powered via Companion App + StoreOS",
    "ea7-emporio-armani":"In-Store / OMS only · powered via Companion App + StoreOS",
    "dune-london":       "In-Store / OMS only · powered via Companion App + StoreOS",
    "boss":              "In-Store / OMS only · powered via Companion App + StoreOS",
    "catwalk":           "Non-commerce site · no consumer app",
    "avantra":           "Non-commerce site · no consumer app",
    "kiko-milano":       "Channel onboarding planned",
    "ajsk":              "Non-commerce site under construction",
}


def load_rbl():
    rows = json.loads((SCRATCH / "rbl_synthetic.json").read_text())
    return {r["slug"]: r for r in rows}


def load_play():
    rows = json.loads((SCRATCH / "non_rbl_play.json").read_text())
    return {r["slug"]: r for r in rows}


def render(num, name, slug, model, vertical, status, cluster, fmt, remarks, rbl, play):
    lines = [f"### {num}. {name}", ""]
    lines.append(f"- **Slug:** `{slug}`")
    lines.append(f"- **Cluster:** {cluster} · **Vertical:** {vertical} · **Model:** {model}")
    lines.append(f"- **Status:** {status} · **Format:** {fmt}")
    if remarks:
        lines.append(f"- **Remarks:** {remarks}")

    r = rbl.get(slug)
    p = play.get(slug)

    if r:
        domain = r["domain"]
        url = f"https://{domain}" if not domain.startswith("http") else domain
        lines.append(f"- **Surface:** Storefront · [`{domain}`]({url})")
        lines.append(f"- **Image:** [`{cdn(f'jcp-channels/{slug}.png')}`]({cdn(f'jcp-channels/{slug}.png')}) (RBL synthetic monitor · load {r['loadTime']} · a11y {r['accessibility']})")
    elif p and p.get("status") == "ok":
        store_url = p.get("play_url", "")
        pkg = p.get("play_package_id", "")
        primary = p.get("primary_shot", 1)
        lines.append(f"- **Surface:** Mobile App · [Play Store · `{pkg}`]({store_url})")
        lines.append(f"- **Icon:** [`{cdn(f'jcp-channels/{slug}/icon.png')}`]({cdn(f'jcp-channels/{slug}/icon.png')})")
        lines.append(f"- **Screenshot:** [`{cdn(f'jcp-channels/{slug}/shot-{primary}.png')}`]({cdn(f'jcp-channels/{slug}/shot-{primary}.png')})")
    else:
        reason = SKIP_REASONS.get(slug, "no public consumer surface")
        lines.append(f"- **Surface:** — _({reason})_")

    lines.append("")
    return "\n".join(lines)


def main():
    rbl = load_rbl()
    play = load_play()

    # Group by cluster, preserving PDF order
    clusters: dict[str, list] = {}
    for row in PDF_CHANNELS:
        clusters.setdefault(row[6], []).append(row)

    out: list[str] = []
    out.append("# JCP Channel Coverage Gallery")
    out.append("")
    out.append("> Source of truth for `/jcp/channels/` — a visual gallery of the storefronts and mobile apps that the JioCommerce Platform powers.")
    out.append(">")
    out.append("> · Channel directory mirrors `docs/jcp-notes-compilation/Channel_Coverage_JCP.pdf` (Feb 21, 2026) — 78 channels across 10 clusters.")
    out.append("> · Storefront screenshots come from RBL OS Synthetic Monitor (`https://rbl-os.vercel.app/synthetic`, last sync 5 Apr 2026).")
    out.append("> · Mobile-app icons + first phone screenshot come from Google Play Store, scraped via `tools/build_jcp_channels.py`.")
    out.append("> · Channels with no public consumer surface (B2B, in-store/OMS only, non-commerce sites, planned) are listed for completeness with a one-line reason.")
    out.append("")

    # Top-level coverage table
    storefronts = sum(1 for row in PDF_CHANNELS if row[2] in rbl)
    apps = sum(1 for row in PDF_CHANNELS if row[2] in play and play[row[2]].get("status") == "ok" and row[2] not in rbl)
    skipped = len(PDF_CHANNELS) - storefronts - apps
    out.append("## Coverage")
    out.append("")
    out.append(f"- **78** channels in the JCP directory")
    out.append(f"- **{storefronts}** storefronts captured from RBL OS Synthetic Monitor")
    out.append(f"- **{apps}** mobile apps captured from Google Play Store")
    out.append(f"- **{skipped}** channels with no public consumer surface (in-store / B2B / planned / non-commerce)")
    out.append("")

    out.append("## Channels by cluster")
    out.append("")

    cluster_order = ["FP", "SNG", "JMP", "JMD", "Swadesh", "Tira", "Jiomart-RHOS", "Ajio", "Netmeds", "Jiomart Headless"]
    for cluster in cluster_order:
        rows = clusters.get(cluster, [])
        if not rows:
            continue
        out.append(f"## Cluster · {cluster} ({len(rows)})")
        out.append("")
        for row in rows:
            out.append(render(*row, rbl=rbl, play=play))

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(out))
    print(f"Wrote {OUT} ({len(OUT.read_text()):,} bytes, {len(PDF_CHANNELS)} channels)")


if __name__ == "__main__":
    main()
