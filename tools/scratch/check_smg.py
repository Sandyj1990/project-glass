import csv
rows = list(csv.DictReader(open("/Users/kushanshah/Documents/work/engineering-os/docs/onboarding/keka_roster_full.csv")))
print("Reports to SMG:")
for r in rows:
    rt = (r.get("Reporting To") or "").strip()
    if rt == "SMG":
        print(f"  {r.get('Display Name'):30s}  {r.get('Job Title')}")
print()
print("Anyone with Sreeraman-ish name:")
for r in rows:
    n = (r.get("Display Name") or "").strip()
    if "sreeraman" in n.lower() or "smg" in n.lower():
        print(f"  {n:30s}  Title={r.get('Job Title')}  RT={r.get('Reporting To')!r}")
