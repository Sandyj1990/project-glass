"""Derive the leadership stack + per-project + per-track leads from data.json.

Approach:
- Founders: Farooq Adam + Sreeraman Thiagarajan (known seed names).
- C-level: anyone whose Reporting Manager is a founder.
- Project lead: the manager that the most rows in that project report to,
  filtered to "senior" titles (Director, Head, VP, CXO, Founder).
- Track lead: same approach within each Project x Track slice.
"""
import json
from collections import Counter, defaultdict

with open("organisation/data.json") as f:
    d = json.load(f)
rows = d["rows"]
total = len(rows)

FOUNDER_NAMES = {"Farooq Adam", "Sreeraman Thiagarajan"}

SENIOR_TITLE_KEYWORDS = (
    "Founder", "Co-founder", "Chief", "President", "VP", "Vice President",
    "Head ", "Head,", "Head of", "Director", "CTO", "CPO", "CTPO",
    "CBO", "CFO", "COO", "CXO", "EVP", "SVP",
)
def is_senior(title):
    if not title: return False
    t = title.strip()
    return any(k.lower() in t.lower() for k in SENIOR_TITLE_KEYWORDS)

# Build name -> title map (most-frequent title if multiple rows)
name_to_titles = defaultdict(Counter)
for r in rows:
    if r.get("name") and r.get("title"):
        name_to_titles[r["name"]][r["title"]] += 1
def title_for(name):
    c = name_to_titles.get(name)
    return c.most_common(1)[0][0] if c else None

print("=" * 70)
print(f"FOUNDERS · seeded · also confirmed in roster")
for n in FOUNDER_NAMES:
    print(f"  {n} · {title_for(n) or '(not in roster)'}")

print()
print("=" * 70)
print("C-LEVEL · people whose manager is a founder")
clevel = sorted({r["name"] for r in rows
                 if r.get("manager") in FOUNDER_NAMES and r.get("name")})
for n in clevel:
    t = title_for(n)
    flag = " [SENIOR]" if is_senior(t or "") else ""
    print(f"  {n:35s}  {t}{flag}")

print()
print("=" * 70)
print("PROJECT LEADS · most-reported-to senior manager per project")
print(f"{'Project':28s} {'Lead':30s} {'Title':40s} {'Reports':>4s}")
print("-" * 110)

projects = sorted({r.get("project") for r in rows if r.get("project")},
                  key=lambda p: -sum(1 for r in rows if r.get("project") == p))
for p in projects:
    proj_rows = [r for r in rows if r.get("project") == p]
    mgr_count = Counter(r.get("manager") for r in proj_rows if r.get("manager"))
    # Filter to senior managers
    senior_mgrs = [(m, c) for m, c in mgr_count.most_common() if is_senior(title_for(m) or "")]
    if senior_mgrs:
        lead, count = senior_mgrs[0]
    else:
        lead, count = (mgr_count.most_common(1)[0] if mgr_count else (None, 0))
    print(f"{p:28s} {lead or '-':30s} {(title_for(lead) or '-'):40s} {count:>4d}")

print()
print("=" * 70)
print("TRACK LEADS · most-reported-to senior manager per (project, track)")
print(f"{'Project':22s} {'Track':40s} {'Lead':28s} {'Reports':>4s}")
print("-" * 110)

# Group rows by (project, track), pick lead per group.
groups = defaultdict(list)
for r in rows:
    p = r.get("project") or "-"
    t = r.get("track") or "-"
    groups[(p, t)].append(r)

for (p, t), grp in sorted(groups.items(), key=lambda kv: (kv[0][0], -len(kv[1]))):
    if len(grp) < 3:
        continue  # skip tiny groups
    mgr_count = Counter(r.get("manager") for r in grp if r.get("manager"))
    senior_mgrs = [(m, c) for m, c in mgr_count.most_common() if is_senior(title_for(m) or "")]
    if senior_mgrs:
        lead, count = senior_mgrs[0]
    else:
        lead, count = (mgr_count.most_common(1)[0] if mgr_count else (None, 0))
    print(f"{p[:22]:22s} {t[:40]:40s} {(lead or '-')[:28]:28s} {count:>4d}")
