"""Patch tools/scratch/non_rbl_play.json with the Accenture-deck overrides
per docs/jcp-update-spec.md §3.2 + §9.3.

Idempotent. Re-running has no effect once applied.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
PLAY = ROOT / "tools" / "scratch" / "non_rbl_play.json"

# 5 already-OK slugs · just add primary_shot_override
OVERRIDES = {
    "jiomart":          "accenture-s33-img03.png",
    "tira":             "accenture-s33-img04.png",
    "ajio":             "accenture-s33-img06.png",
    "metro-kirana":     "accenture-s34-img04.png",
    "reliance-digital": "accenture-s34-img03.png",
}

# 3 currently-skipped slugs · flip to OK + add fields
UN_SKIPS = {
    "trends": {
        "name": "Reliance Trends",
        "model": "B2C",
        "vertical": "F&L",
        "cluster": "SNG",
        "format": "In-Store, Website",
        "status": "ok",
        "remarks": "Companion App in 2 stores; Kiosk planned",
        "primary_shot_override": "accenture-s33-img01.png",
        "badge": "in-store companion · staff app",
        "has_icon": False,
        "play_url": "",
        "play_package_id": "",
    },
    "rcpl": {
        "name": "RCPL",
        "model": "B2B",
        "vertical": "Grocery",
        "cluster": "JMP",
        "format": "Website",
        "status": "ok",
        "remarks": "Reliance Consumer Brands portal",
        "primary_shot_override": "accenture-s34-img01.png",
        "badge": "B2B · brand portal",
        "has_icon": False,
        "play_url": "",
        "play_package_id": "",
    },
    "jiomart-digital": {
        "name": "Jiomart Digital ASP / B2B / StoreSell / COFO",
        "model": "B2B",
        "vertical": "Electronics",
        "cluster": "JMD",
        "format": "Website",
        "status": "ok",
        "remarks": "Website live for BPL · Kelvinator · MyLyf · Wyzr",
        "primary_shot_override": "accenture-s34-img06.png",
        "badge": "B2B · electronics ASP",
        "has_icon": False,
        "play_url": "",
        "play_package_id": "",
    },
}


def main() -> int:
    rows = json.loads(PLAY.read_text())
    by_slug = {r["slug"]: r for r in rows}

    for slug, override in OVERRIDES.items():
        if slug not in by_slug:
            print(f"  WARN: {slug} not in non_rbl_play.json")
            continue
        by_slug[slug]["primary_shot_override"] = override
        print(f"  override     {slug:20s} ← {override}")

    for slug, fields in UN_SKIPS.items():
        if slug not in by_slug:
            print(f"  WARN: {slug} not in non_rbl_play.json")
            continue
        by_slug[slug].update(fields)
        # Drop `skip` / `skip_reason` / `reason` / `candidates` if present
        for k in ("skip", "skip_reason", "reason", "candidates"):
            by_slug[slug].pop(k, None)
        print(f"  un-skip + override  {slug:20s} ← {fields['primary_shot_override']}")

    PLAY.write_text(json.dumps(list(by_slug.values()), indent=2))
    n_ok = sum(1 for r in by_slug.values() if r.get("status") == "ok")
    n_skipped = sum(1 for r in by_slug.values() if r.get("status") == "skipped")
    print(f"\nFinal: ok={n_ok}, skipped={n_skipped}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
