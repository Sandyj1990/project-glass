"""Generate a PDF report of the roster delta for HR tally.

Diffs the billed sheet (docs/org-notes-compilation/Team List Billed v2.xlsx)
against the keka HRIS export (engineering-os/docs/onboarding/keka_roster_full.csv).
Categorises keka-only rows into placeholders (open hires + dummies) vs real
people, surfaces billed-only rows, and lists duplicate Employee Numbers.

Run from repo root:
    python3 tools/build_roster_delta_pdf.py

Output: docs/roster-delta-<today>.pdf  (gitignored — PDFs aren't committed)

PDF structure (3 pages, A4):
  · Header + sources + summary table (counts, intersection, both deltas).
  · Section 1: keka-only real people, grouped by department. Each row:
    Emp ID · Name · Job Title · Time Type · Reports to · Joined.
  · Section 2: placeholder seats (the 7 entries in
    organisation/mappings.json > placeholderNames) with reporting chains.
  · Section 3: billed-only rows (people on the billing sheet but missing
    from keka — likely HRIS-export gaps or contractor-id namespacing).
  · Section 4: duplicate Employee Number groups in billed (today: the 8
    ALP consultants sharing the placeholder id 'Consultant').

When to re-run:
  · After every Team List Billed v2.xlsx refresh (HR will want to tally).
  · After every keka_roster_full.csv refresh.
  · After any change to placeholderNames in organisation/mappings.json.

Re-run is safe — output filename embeds today's date, so multiple runs
don't overwrite each other; you can keep a history.

Dependencies: reportlab (pip install reportlab) + openpyxl (already
required by build_org_data.py).

For the full /organisation lifecycle context, read:
    docs/organisation-workflow.md
"""
import csv, openpyxl, warnings
from collections import defaultdict, Counter
from datetime import date
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether,
)

warnings.filterwarnings("ignore")
ROOT = Path(__file__).resolve().parent.parent
XLSX = ROOT / "docs/org-notes-compilation/Team List Billed v2.xlsx"
KEKA = Path("/Users/kushanshah/Documents/work/engineering-os/docs/onboarding/keka_roster_full.csv")
OUT = ROOT / f"docs/roster-delta-{date.today().isoformat()}.pdf"

PLACEHOLDER_NAMES = {
    "Jigar - Robotics", "Jigar - Commerce Channel DoE", "Jigar Extension Lead",
    "Jigar Fynd Automation Commerce Lead", "Jigar- JCP Projects",
    "CBO India+Global", "Fynd Dummy",
}

# ---------- Load data ----------
wb = openpyxl.load_workbook(str(XLSX), data_only=True, read_only=True)
s = wb["Trupti -Updated Employee Master"]
all_rows = list(s.iter_rows(values_only=True))
hdr = all_rows[0]
EMP, NAME, DEPT, TITLE, PROJ = (
    hdr.index("Employee Number"), hdr.index("Display Name"),
    hdr.index("Department"), hdr.index("Job Title"), hdr.index("Project"),
)
billed_raw = []
for r in all_rows[1:]:
    if r[EMP] is None and not r[NAME]: continue
    eid = r[EMP]
    if isinstance(eid, float) and eid.is_integer(): eid = str(int(eid))
    elif eid is not None: eid = str(eid).strip()
    billed_raw.append({"id": eid, "name": r[NAME], "dept": r[DEPT], "title": r[TITLE], "project": r[PROJ]})
billed_dup = Counter(b["id"] for b in billed_raw)
billed_unique_ids = set(billed_dup) - {None}
billed_by = {}
for b in billed_raw:
    if b["id"] is not None and b["id"] not in billed_by:
        billed_by[b["id"]] = b

keka_raw = list(csv.DictReader(open(KEKA)))
keka_by = {(r.get("Employee Number") or "").strip(): r for r in keka_raw}
keka_unique_ids = set(keka_by) - {""}

only_keka_ids = sorted(keka_unique_ids - billed_unique_ids)
only_billed_ids = sorted(billed_unique_ids - keka_unique_ids)

# Categorise the keka-only rows
keka_real = []
keka_placeholders = []
for eid in only_keka_ids:
    k = keka_by[eid]
    n = (k.get("Display Name") or "").strip()
    bucket = keka_placeholders if n in PLACEHOLDER_NAMES else keka_real
    bucket.append(k)

# ---------- PDF setup ----------
doc = SimpleDocTemplate(
    str(OUT), pagesize=A4,
    leftMargin=14*mm, rightMargin=14*mm, topMargin=14*mm, bottomMargin=14*mm,
    title="Roster delta · billed v2.xlsx vs keka_roster_full.csv",
    author="Fynd × Reliance Retail register",
)

styles = getSampleStyleSheet()
H1 = ParagraphStyle("H1", parent=styles["Heading1"], fontName="Helvetica-Bold",
                    fontSize=18, leading=22, spaceAfter=4, textColor=colors.HexColor("#0A0A0A"))
H2 = ParagraphStyle("H2", parent=styles["Heading2"], fontName="Helvetica-Bold",
                    fontSize=12, leading=16, spaceBefore=12, spaceAfter=4, textColor=colors.HexColor("#0A0A0A"))
H3 = ParagraphStyle("H3", parent=styles["Heading3"], fontName="Helvetica-Bold",
                    fontSize=10, leading=14, spaceBefore=8, spaceAfter=2, textColor=colors.HexColor("#0A0A0A"))
PMono = ParagraphStyle("PMono", parent=styles["BodyText"], fontName="Courier",
                       fontSize=8, leading=10, textColor=colors.HexColor("#666666"))
P = ParagraphStyle("P", parent=styles["BodyText"], fontName="Helvetica",
                   fontSize=9, leading=12, textColor=colors.HexColor("#333333"))
PSmall = ParagraphStyle("PSmall", parent=P, fontSize=8, leading=10)

flow = []

# ---------- Title page header ----------
flow.append(Paragraph("Roster delta · billed sheet vs keka HRIS", H1))
flow.append(Paragraph(
    f"Generated {date.today().strftime('%d-%b-%Y')} · for HR tally · strict internal circulation only",
    PMono))
flow.append(Spacer(1, 6))
flow.append(Paragraph(
    "<b>Sources:</b><br/>"
    "&nbsp;· billed: <font face='Courier'>docs/org-notes-compilation/Team List Billed v2.xlsx</font> · sheet <font face='Courier'>Trupti -Updated Employee Master</font><br/>"
    "&nbsp;· keka:  <font face='Courier'>engineering-os/docs/onboarding/keka_roster_full.csv</font>",
    P))

# ---------- Summary table ----------
flow.append(Paragraph("Summary", H2))
summary_data = [
    ["Metric", "Count", "Notes"],
    ["billed · total non-blank rows", f"{len(billed_raw):,}", "what data.json reports"],
    ["billed · unique Employee Numbers", f"{len(billed_unique_ids):,}", "after dedup"],
    ["billed · duplicate rows", f"{sum(c-1 for c in billed_dup.values() if c > 1):,}",
     "all share placeholder id 'Consultant'"],
    ["keka · total rows", f"{len(keka_raw):,}", "1 per Employee Number, no dups"],
    ["keka · placeholder seats", f"{len(keka_placeholders):,}", "open hires + dummies (excluded from organogram)"],
    ["keka · real people", f"{len(keka_raw) - len(keka_placeholders):,}", ""],
    ["intersection (same id)", f"{len(billed_unique_ids & keka_unique_ids):,}", "fully reconciled"],
    [Paragraph("<b>only in keka · NOT in billed</b>", P), f"{len(only_keka_ids):,}",
     f"of which {len(keka_placeholders)} placeholders + {len(keka_real)} real people"],
    [Paragraph("<b>only in billed · NOT in keka</b>", P), f"{len(only_billed_ids):,}",
     "may be HRIS-export gaps or contractor-id namespacing"],
]
tbl = Table(summary_data, colWidths=[68*mm, 22*mm, 90*mm], repeatRows=1)
tbl.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0A0A0A")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 9),
    ("LEADING", (0, 0), (-1, -1), 11),
    ("ALIGN", (1, 0), (1, -1), "RIGHT"),
    ("FONTNAME", (1, 1), (1, -1), "Courier"),
    ("LINEBELOW", (0, 0), (-1, -1), 0.4, colors.HexColor("#DDDDDD")),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F8F8F8")]),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("LEFTPADDING", (0, 0), (-1, -1), 6),
    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ("TOPPADDING", (0, 0), (-1, -1), 5),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
]))
flow.append(tbl)

# ---------- Section · in keka, not billed (real people) ----------
flow.append(Paragraph(
    f"In keka · NOT in billed · real people · {len(keka_real)} rows",
    H2))
flow.append(Paragraph(
    "These people appear on the keka HRIS roster but are not on the billing sheet. "
    "Most are contractors paid through a separate P&amp;L, plus a few full-time staff "
    "in InfoSec / Program / Technical Support / Engineering.",
    P))

by_dept_real: dict[str, list] = defaultdict(list)
for k in keka_real:
    by_dept_real[(k.get("Department") or "—")].append(k)

for dept in sorted(by_dept_real):
    rows_for_dept = sorted(by_dept_real[dept], key=lambda x: x.get("Display Name") or "")
    flow.append(Paragraph(f"{dept} · {len(rows_for_dept)}", H3))
    rows = [["Emp ID", "Name", "Job Title", "Time Type", "Reports to", "Joined"]]
    for k in rows_for_dept:
        rows.append([
            k.get("Employee Number", "") or "",
            k.get("Display Name", "") or "",
            (k.get("Job Title") or "")[:46],
            k.get("Time Type", "") or "",
            (k.get("Reporting To") or "")[:24],
            k.get("Date Joined", "") or "",
        ])
    t = Table(rows, colWidths=[16*mm, 42*mm, 56*mm, 20*mm, 30*mm, 18*mm], repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0A0A0A")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 7.5),
        ("LEADING", (0, 0), (-1, -1), 10),
        ("FONTNAME", (0, 1), (0, -1), "Courier"),
        ("FONTNAME", (5, 1), (5, -1), "Courier"),
        ("LINEBELOW", (0, 0), (-1, -1), 0.3, colors.HexColor("#EEEEEE")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#FAFAFA")]),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    flow.append(t)

# ---------- Section · placeholders ----------
flow.append(PageBreak())
flow.append(Paragraph(
    f"In keka · NOT in billed · placeholder seats · {len(keka_placeholders)} rows",
    H2))
flow.append(Paragraph(
    "Open hires and dummy entries used as org-chart placeholder seats. "
    "These are excluded from the public organogram (build script filter at "
    "<font face='Courier'>organisation/mappings.json &gt; placeholderNames</font>).",
    P))
rows = [["Emp ID", "Name", "Job Title", "Reports to", "CXO"]]
# Use Paragraphs so long names wrap rather than overflowing into the next column.
cell = ParagraphStyle("cell", parent=P, fontSize=8, leading=10)
for k in sorted(keka_placeholders, key=lambda x: x.get("Display Name") or ""):
    rows.append([
        Paragraph(k.get("Employee Number", "") or "", PMono),
        Paragraph(k.get("Display Name", "") or "", cell),
        Paragraph((k.get("Job Title") or ""), cell),
        Paragraph((k.get("Reporting To") or ""), cell),
        Paragraph((k.get("CXO's") or ""), cell),
    ])
t = Table(rows, colWidths=[14*mm, 50*mm, 42*mm, 46*mm, 30*mm], repeatRows=1)
t.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0A0A0A")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 8),
    ("LEADING", (0, 0), (-1, -1), 11),
    ("FONTNAME", (0, 1), (0, -1), "Courier"),
    ("LINEBELOW", (0, 0), (-1, -1), 0.3, colors.HexColor("#EEEEEE")),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#FAFAFA")]),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("LEFTPADDING", (0, 0), (-1, -1), 4),
    ("RIGHTPADDING", (0, 0), (-1, -1), 4),
    ("TOPPADDING", (0, 0), (-1, -1), 3),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
]))
flow.append(t)

# ---------- Section · in billed, not keka ----------
flow.append(Spacer(1, 14))
flow.append(Paragraph(
    f"In billed · NOT in keka · {len(only_billed_ids)} rows",
    H2))
flow.append(Paragraph(
    "These appear on the billing sheet but are missing from the keka HRIS roster. "
    "Likely HRIS-export gaps or contractors with a different employee-id namespace.",
    P))
rows = [["Emp ID", "Name", "Department", "Job Title", "Project"]]
for eid in only_billed_ids:
    b = billed_by.get(eid, {})
    rows.append([
        b.get("id", "") or "",
        b.get("name", "") or "",
        b.get("dept", "") or "",
        (b.get("title") or "")[:42],
        b.get("project", "") or "",
    ])
t = Table(rows, colWidths=[20*mm, 42*mm, 32*mm, 56*mm, 32*mm], repeatRows=1)
t.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0A0A0A")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 8),
    ("LEADING", (0, 0), (-1, -1), 11),
    ("FONTNAME", (0, 1), (0, -1), "Courier"),
    ("LINEBELOW", (0, 0), (-1, -1), 0.3, colors.HexColor("#EEEEEE")),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#FAFAFA")]),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("LEFTPADDING", (0, 0), (-1, -1), 4),
    ("RIGHTPADDING", (0, 0), (-1, -1), 4),
    ("TOPPADDING", (0, 0), (-1, -1), 3),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
]))
flow.append(t)

# ---------- Section · billed dups ----------
dup_billed = [(eid, c) for eid, c in billed_dup.items() if c > 1 and eid is not None]
if dup_billed:
    flow.append(Spacer(1, 14))
    flow.append(Paragraph(
        f"Billed sheet · duplicate Employee Numbers · {sum(c for _, c in dup_billed)} rows",
        H2))
    flow.append(Paragraph(
        "These billing-sheet rows share the same Employee Number — almost certainly "
        "a placeholder ID being reused for multiple consultants. Each shows up as one "
        "of the rows in the 'only in billed' list (above) because the dedup loses "
        "all but one.",
        P))
    for eid, c in dup_billed:
        names = [b["name"] for b in billed_raw if b["id"] == eid]
        flow.append(Paragraph(f"Employee Number = <font face='Courier'>{eid}</font> · used by {c} people:", H3))
        rows = [["Name", "Department", "Job Title", "Project"]]
        for n in sorted(names):
            row = next((b for b in billed_raw if b["id"] == eid and b["name"] == n), {})
            rows.append([n, row.get("dept", "") or "", (row.get("title") or "")[:48], row.get("project", "") or ""])
        t = Table(rows, colWidths=[44*mm, 30*mm, 60*mm, 36*mm], repeatRows=1)
        t.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0A0A0A")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 8),
            ("LEADING", (0, 0), (-1, -1), 11),
            ("LINEBELOW", (0, 0), (-1, -1), 0.3, colors.HexColor("#EEEEEE")),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#FAFAFA")]),
            ("LEFTPADDING", (0, 0), (-1, -1), 4),
            ("RIGHTPADDING", (0, 0), (-1, -1), 4),
            ("TOPPADDING", (0, 0), (-1, -1), 3),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ]))
        flow.append(t)

# ---------- Build ----------
def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Courier", 7)
    canvas.setFillColor(colors.HexColor("#888888"))
    canvas.drawString(14*mm, 8*mm, "Roster delta · billed v2.xlsx vs keka_roster_full.csv · strict internal circulation")
    canvas.drawRightString(A4[0] - 14*mm, 8*mm, f"page {doc.page}")
    canvas.restoreState()

doc.build(flow, onFirstPage=footer, onLaterPages=footer)
print(f"wrote {OUT}")
print(f"summary: {len(keka_real)} keka-only real · {len(keka_placeholders)} placeholders · {len(only_billed_ids)} billed-only · {len(dup_billed)} dup-id groups")
