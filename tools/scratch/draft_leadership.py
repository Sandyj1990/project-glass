"""Draft a leadership.json from data.json + senior-title scan.

Strategy:
- Founders: seeded (Farooq, Sreeraman) — Sreeraman not in roster, Farooq is.
- C-suite: scan rows for senior titles (Chief, Director, Head, VP, etc.),
  rank by team size (count of direct reports + indirect via project/track).
- Project leads: per project, pick the senior-title manager with most reports.
"""
import json
from collections import Counter, defaultdict

with open("organisation/data.json") as f:
    d = json.load(f)
rows = d["rows"]

SENIOR_KEYWORDS = (
    "Founder", "Co-founder", "Chief", "President", "VP", "Vice President",
    "Head ", "Head,", "Head of", "Director", "CTO", "CPO", "CTPO",
    "CBO", "CFO", "COO", "CXO", "EVP", "SVP",
)
def is_senior(title):
    if not title: return False
    return any(k.lower() in title.lower() for k in SENIOR_KEYWORDS)

name_to_title = {}
name_to_dept = {}
for r in rows:
    if r.get("name") and r.get("title"):
        name_to_title.setdefault(r["name"], r["title"])
        name_to_dept.setdefault(r["name"], r.get("department"))

# Direct reports per manager
direct_reports = Counter()
for r in rows:
    if r.get("manager"):
        direct_reports[r["manager"]] += 1

# Senior people, ranked by direct reports
senior_people = []
for name, title in name_to_title.items():
    if is_senior(title):
        senior_people.append({
            "name": name,
            "title": title,
            "department": name_to_dept.get(name),
            "directReports": direct_reports.get(name, 0),
        })
senior_people.sort(key=lambda x: -x["directReports"])

# Project leads
project_lead = {}
for proj in {r["project"] for r in rows if r.get("project")}:
    proj_rows = [r for r in rows if r.get("project") == proj]
    mgrs = Counter(r["manager"] for r in proj_rows if r.get("manager"))
    seniors = [(m, c) for m, c in mgrs.most_common()
               if is_senior(name_to_title.get(m, ""))]
    if seniors:
        m, c = seniors[0]
        project_lead[proj] = {
            "name": m,
            "title": name_to_title.get(m, "?"),
            "directReports": c,
        }
    elif mgrs:
        m, c = mgrs.most_common(1)[0]
        project_lead[proj] = {
            "name": m,
            "title": name_to_title.get(m, "?"),
            "directReports": c,
            "_uncertain": True,
        }

# Output JSON
out = {
    "_comment": "Authoritative leadership stack for /organisation. Edit by hand. Build script (tools/build_org_data.py) reads this and emits it under data.leaders. Names + scopes here override anything derivable from the roster manager column.",
    "_uncertain_note": "Entries with _uncertain=true were derived from data.json but the role/title is ambiguous. Edit the name/title/scope fields and remove _uncertain when confirmed.",
    "founders": [
        {
            "name": "Farooq Adam",
            "title": "Co-founder",
            "since": "2013-05-01",
            "scope": "Sets product direction across the Fynd platform stack",
        },
        {
            "name": "Sreeraman Thiagarajan",
            "title": "Co-founder",
            "since": "2013-05-01",
            "scope": "Drives commercial and partnership strategy",
            "_uncertain": True,
            "_note": "Not in v2 roster — billed differently. Confirm scope.",
        },
    ],
    "cSuite": [
        {
            "name": p["name"],
            "title": p["title"],
            "department": p["department"],
            "directReports": p["directReports"],
            "_uncertain": True,
        }
        for p in senior_people[:8]
    ],
    "projectLeads": project_lead,
}

print(json.dumps(out, indent=2, ensure_ascii=False))
