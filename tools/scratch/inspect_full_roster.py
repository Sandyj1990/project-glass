import csv
from collections import Counter

path = "/Users/kushanshah/Documents/work/engineering-os/docs/onboarding/keka_roster_full.csv"
rows = list(csv.DictReader(open(path)))
print(f"rows: {len(rows)}")
print(f"keys: {list(rows[0].keys())}")
print()
cxo = Counter((r.get("CXO's") or "").strip() or "(blank)" for r in rows)
print("CXO's distribution (top 20):")
for k, v in cxo.most_common(20):
    print(f"  {v:5d}  {k!r}")
print()
print("Reporting To = blank/root (probable founders):")
for r in rows:
    rt = (r.get("Reporting To") or "").strip()
    if not rt:
        print(f"  emp={r.get('Employee Number'):6}  {r.get('Display Name'):35s}  {r.get('Job Title')}")
print()
# Department distribution
dep = Counter((r.get("Department") or "").strip() or "—" for r in rows)
print("Departments (top 15):")
for k, v in dep.most_common(15):
    print(f"  {v:5d}  {k!r}")
print()
# Status filter
status = Counter((r.get("Employment Status") or "—") for r in rows)
print("Employment Status:")
for k, v in status.most_common():
    print(f"  {v:5d}  {k!r}")
