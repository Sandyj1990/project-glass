import csv
path = "/Users/kushanshah/Documents/work/engineering-os/docs/onboarding/keka_roster_full.csv"
rows = list(csv.DictReader(open(path)))

CXO_COL = "CXO's"
names_to_check = ["Farooq Adam", "Sreeraman", "Jigar Dafda", "Kushan Shah", "Pratik Patel", "Fahim Sakri", "Salman Saudagar", "Ragini Varma", "Ronak Modi"]

by_name = {}
for r in rows:
    n = (r.get("Display Name") or "").strip()
    if n:
        by_name.setdefault(n, r)

for name in names_to_check:
    matches = [n for n in by_name if name.lower() in n.lower()]
    if matches:
        for m in matches[:3]:
            r = by_name[m]
            title = r.get("Job Title", "")
            rt = r.get("Reporting To", "")
            cxo = r.get(CXO_COL, "")
            print(f"{m:30s}  Title: {title:40s}  Reports to: {rt:25s}  CXO: {cxo}")
    else:
        print(f"{name}  NOT FOUND")
print()
print("People with Founder/Chief in title:")
for r in rows:
    t = (r.get("Job Title") or "")
    if any(k in t for k in ("Founder", "Chief")):
        print(f"  {r.get('Display Name'):30s}  {t:40s}  Reports to: {r.get('Reporting To'):25s}  CXO: {r.get(CXO_COL)}")
