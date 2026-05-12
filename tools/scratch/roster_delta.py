"""Diff billed roster (Team List Billed v2.xlsx) vs full keka export
(keka_roster_full.csv). Surface (a) the count breakdown, (b) duplicates within
each, and (c) the symmetric delta by Employee Number.
"""
import csv, openpyxl, warnings
from collections import defaultdict, Counter
warnings.filterwarnings("ignore")

XLSX = "docs/org-notes-compilation/Team List Billed v2.xlsx"
KEKA = "/Users/kushanshah/Documents/work/engineering-os/docs/onboarding/keka_roster_full.csv"

# ---- Load billed (allow duplicates so we can count them) ----
wb = openpyxl.load_workbook(XLSX, data_only=True, read_only=True)
s = wb["Trupti -Updated Employee Master"]
all_rows = list(s.iter_rows(values_only=True))
hdr = all_rows[0]
EMP = hdr.index("Employee Number")
NAME = hdr.index("Display Name")
DEPT = hdr.index("Department")
TITLE = hdr.index("Job Title")
PROJ = hdr.index("Project")

billed_raw = []  # all rows
for r in all_rows[1:]:
    if r[EMP] is None and not r[NAME]: continue  # truly blank row
    eid = r[EMP]
    if isinstance(eid, float) and eid.is_integer(): eid = str(int(eid))
    elif eid is not None: eid = str(eid).strip()
    billed_raw.append({
        "id": eid,
        "name": r[NAME],
        "dept": r[DEPT],
        "title": r[TITLE],
        "project": r[PROJ],
    })

billed_dup = Counter(b["id"] for b in billed_raw)
billed_unique_ids = set(billed_dup) - {None}

# ---- Load keka ----
keka_raw = list(csv.DictReader(open(KEKA)))
keka_dup = Counter((r.get("Employee Number") or "").strip() for r in keka_raw)
keka_unique_ids = set(keka_dup) - {""}

print(f"=== ROW COUNTS ===")
print(f"billed (Team List Billed v2.xlsx)")
print(f"  total non-blank rows:           {len(billed_raw):>5}")
print(f"  unique Employee Numbers:        {len(billed_unique_ids):>5}")
print(f"  rows with NULL Employee Number: {sum(1 for b in billed_raw if b['id'] is None):>5}")
print(f"  duplicate Employee Numbers:     {sum(c-1 for c in billed_dup.values() if c > 1):>5}")
dup_billed = [(eid, c) for eid, c in billed_dup.items() if c > 1 and eid is not None]
if dup_billed:
    print("    duplicates:")
    for eid, c in dup_billed:
        names = [b["name"] for b in billed_raw if b["id"] == eid]
        print(f"      {eid!r:8s}  x{c}  · {names}")
print()
print(f"keka (keka_roster_full.csv)")
print(f"  total rows:                     {len(keka_raw):>5}")
print(f"  unique Employee Numbers:        {len(keka_unique_ids):>5}")
dup_keka = [(eid, c) for eid, c in keka_dup.items() if c > 1 and eid]
if dup_keka:
    print("  duplicates in keka:")
    for eid, c in dup_keka[:10]:
        print(f"      {eid!r:8s}  x{c}")
print()

print(f"=== DELTA (by Employee Number) ===")
print(f"intersection: {len(billed_unique_ids & keka_unique_ids):>5}")
print(f"only in keka: {len(keka_unique_ids - billed_unique_ids):>5}")
print(f"only in billed: {len(billed_unique_ids - keka_unique_ids):>5}")
print()

only_keka_ids = sorted(keka_unique_ids - billed_unique_ids)
only_billed_ids = sorted(billed_unique_ids - keka_unique_ids)

# Index keka by id
keka_by = {(r.get("Employee Number") or "").strip(): r for r in keka_raw}

print(f"=== IN KEKA · NOT IN BILLED · {len(only_keka_ids)} unique ids ===")
print("(people on the keka HRIS roster who aren't on the billing sheet)")
by_dept = defaultdict(list)
for eid in only_keka_ids:
    k = keka_by[eid]
    by_dept[(k.get("Department") or "—")].append(k)
for dept in sorted(by_dept):
    print(f"\n  · {dept} ({len(by_dept[dept])})")
    for k in sorted(by_dept[dept], key=lambda x: x.get("Display Name") or ""):
        title = k.get("Job Title") or "—"
        time_type = k.get("Time Type") or "—"
        print(f"    {k.get('Employee Number'):8s}  {k.get('Display Name'):32s}  {title[:42]:42s}  type: {time_type}")

print()
print(f"=== IN BILLED · NOT IN KEKA · {len(only_billed_ids)} unique ids ===")
billed_by = {}
for b in billed_raw:
    if b["id"] is not None and b["id"] not in billed_by:
        billed_by[b["id"]] = b
by_dept2 = defaultdict(list)
for eid in only_billed_ids:
    b = billed_by.get(eid)
    if b:
        by_dept2[(b.get("dept") or "—")].append(b)
for dept in sorted(by_dept2):
    print(f"\n  · {dept} ({len(by_dept2[dept])})")
    for b in sorted(by_dept2[dept], key=lambda x: x.get("name") or ""):
        title = b.get("title") or "—"
        proj = b.get("project") or "—"
        print(f"    {b['id']:8s}  {b.get('name') or '':32s}  {title[:42]:42s}  proj: {proj}")
