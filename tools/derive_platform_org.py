"""Print platform-specific org stats derived from organisation/data.json.

Use to hydrate the §People section on any platform page (e.g. /jcp, /granary,
/impetus). Output is paste-ready: total · dedicated/shared split · engineering
% · location mix · billing mix · 13-track bar list.

Usage:
  python tools/derive_platform_org.py jcp
  python tools/derive_platform_org.py "Granary"

The argument matches data.json `pivot[].project` (case-insensitive).

Per CLAUDE.md → Org stats · canonical-source rule → Platform page hydration.
Don't restate org-wide totals (1,056 / 707 / 46% / 66%) on a platform page —
those belong only on /organisation. This script prints platform-only stats.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "organisation" / "data.json"


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("project", help="project name as in data.pivot[].project (case-insensitive)")
    args = p.parse_args()

    d = json.loads(DATA.read_text())
    target = args.project.lower()
    pivot = next((x for x in d["pivot"] if x.get("project", "").lower() == target), None)
    if pivot is None:
        names = sorted({x.get("project") for x in d["pivot"] if x.get("project")})
        print(f"unknown project: {args.project!r}\navailable: {', '.join(names)}", file=sys.stderr)
        return 1

    proj = pivot["project"]
    rows = [r for r in d["rows"] if r.get("project") == proj]
    proj_route = pivot.get("projectRoute") or ""

    def pct(n: int) -> int:
        return round(100 * n / len(rows)) if rows else 0

    eng = sum(1 for r in rows if r.get("department") == "Engineering")
    PB_DEPTS = {
        "Engineering", "Product", "Design", "Data Annotator",
        "Quality Assurance", "Research", "Design Research",
        "Data Analysis", "Data Science", "Fashion Design",
    }
    pb = sum(1 for r in rows if (r.get("department") or "") in PB_DEPTS)

    locations = Counter((r.get("location") or "—") for r in rows)
    billing = Counter((r.get("billing") or "—") for r in rows)

    dedicated = sum(
        t["count"] for t in pivot["tracks"]
        if not t.get("trackRoute") or (t["trackRoute"] or "").startswith(proj_route)
    )
    shared = pivot["total"] - dedicated

    print(f"=== {proj} · derived from organisation/data.json ===\n")
    print(f"Total            · {pivot['total']}")
    print(f"Tracks           · {len(pivot['tracks'])}  ({sum(1 for t in pivot['tracks'] if not t.get('trackRoute') or (t['trackRoute'] or '').startswith(proj_route))} dedicated · {sum(1 for t in pivot['tracks'] if t.get('trackRoute') and not (t['trackRoute'] or '').startswith(proj_route))} shared)")
    print(f"Dedicated split  · {dedicated} dedicated · {shared} shared with adjacent platforms")
    print(f"Engineering      · {eng} ({pct(eng)}%)")
    print(f"Product builders · {pb} ({pct(pb)}%)  [Eng+Product+Design+QA+Research+Data*+Fashion]")
    print()
    print("Locations:")
    for k, v in locations.most_common():
        print(f"  {k:<14} {v:>4}  ({pct(v)}%)")
    print()
    print("Billing:")
    for k, v in billing.most_common():
        print(f"  {k:<14} {v:>4}  ({pct(v)}%)")
    print()
    print("Tracks (largest → smallest):")
    max_count = max((t["count"] for t in pivot["tracks"]), default=1)
    for t in pivot["tracks"]:
        kind = "dedicated" if not t.get("trackRoute") or (t["trackRoute"] or "").startswith(proj_route) else "shared   "
        bar_pct = round(100 * t["count"] / max_count, 1)
        print(f"  [{kind}] {t['track']:<24} {t['count']:>4}  {bar_pct:>5}%  → {t.get('trackRoute') or '—'}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
