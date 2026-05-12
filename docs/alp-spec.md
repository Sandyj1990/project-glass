# ALP page · Restructure spec

**Status:** v0.1 · 2026-05-01 · **drafting**
**Owner:** Kushan Shah
**Route:** `/alp/` (already live at v0.8.4; this spec restructures it)
**Source content:** `docs/alp-notes-compilation/`
**Narrative anchor:** ALP = Asset Lifecycle Platform. Internal new-store-opening (NSO) system for Reliance Retail. MVP went live for the GJ cluster in Apr-2026; Phase 2 (AI feasibility scoring + integrations with Board / Sirion / R-Dash / SAP / Retail Vista) is in build. Page must report what is *actually* shipped vs what is on the Phase 2 roadmap, with no individual names asserted.

**Inherits from:** `docs/website-orientation-spec.md` · §3 page template · `website-tone-of-voice.md` for register.

**Built using:** `.claude/skills/website-section-authoring` (workflow) + `.claude/skills/website-tone-of-voice` (copy register).

---

## 0. Implementation status

| Stage | Deliverable | Where it lands |
|---|---|---|
| 0 raw | Source compilation folder | `docs/alp-notes-compilation/` (PRD PDF, project plan xlsx, screenshots PDF) |
| 1 spec | This file | `docs/alp-spec.md` |
| 2 data | Single page · no YAML; copy authored inline | `alp/index.html` |
| 3 assets | 5 product screenshots from Screenshots PDF | `assets/alp/` |
| 4 build | Hand-authored HTML (single-page section) | `alp/index.html` |
| 5 nav | Already wired in mega-menu (`Special Projects` column); no new nav edits | — |
| 6 verify | Local server walk + Chrome DevTools screenshot + console clean | — |

---

## 1. Why this page exists

**Audience.** RIL Apex leadership reviewing the register. Same frame as `/jcp`, `/granary`, `/hirefirst`.

**Gap to close.** Current `/alp` v0.8.4 carries three problems that fail the *factual* and *no Fynd self-praise* rules of the tone-of-voice:

1. **Title error.** Page reads "Asset Lifecycle Planning". Source PRD and project plan use **Asset Lifecycle Platform**. (User-confirmed: ALP = Platform.)
2. **Invented "Sub-IPs".** The seven cards in the existing §Sub-IPs (Site selection AI, Lease intelligence, Rent benchmarking, Footfall prediction, Productivity scorecard, Closure / relocation, Cross-format visibility) do **not** appear in the PRD, project plan, or screenshots. They were authored as a narrative scaffold but tagged as live/build with proof points lifted from `/retail-vista` ("10.5 Cr buildings indexed", "22 data categories"). Per `website-tone-of-voice` §1.1: *"If you cannot point at the source, do not write the line."*
3. **Unsourced people.** Hero asserts Karan Muley (Lead), Nishant Amin (Co-conceptualisation), Shubham Srivastava, Saurav (RIL counterpart). None appear in either source document. The project plan only names Irin Mathew (Other Key Members). User decision: **strip all individual names from page**.

**Two truth-states to honour:**

1. **Phase 1 MVP (live for GJ cluster pilot, Apr-2026)** — what the project plan marks **Done**: SAML SSO, RBAC, AOP/catchment ingestion, Lead Management Dashboard, Lead Creation form + Lead ID, Lead Journey workflow with 7 tabs and 11 statuses, manual approval flow across Approvals/Legal/Construction/Payments tabs, email alerts, prototype UAT.
2. **Phase 2 (in build / planned)** — AI Business Feasibility scoring (blocked on Retail Vista), advanced SLA matrix, integrations with Board / Sirion / R-Dash / SAP / FR Portal / Retail Vista, mobile lead creation (offline mode), advanced forms (Term Sheet, LDD, Site Evaluation Report, Rent Intelligence Dashboard, License Tracking, Maintenance), AI summary on lead details.

Per user decision, the seven existing "Sub-IP" cards are kept as **roadmap intent**, all marked `Roadmap` — none claim Live/Build status.

## 2. Source inventory

| File | Type | Key facts derivable |
|---|---|---|
| `ALP - PRD.pdf` (1.5MB, 27 pp) | Product Requirements Document | Login (SAML), team structure (RE / BT / EPC), dashboard cards by role, 11-status taxonomy, Lead ID format `LD-FY27-0000`, ageing rules, Progress Timeline (7 stages), Activity Log triggers, Overview / Site Visit Assessment / Validation tab specs, Approval cards (Site / Business levels — Apex at top), Legal / Construction / Finance tab spec, RBAC, audit trail, AI summary scope-out for MVP |
| `ALP project plan for phase 1.xlsx` | Phase 1 plan (9 initiatives) + Phase 2 plan (7 initiatives) | Initiative-level status (Done / In Progress / Out of scope); Risk register; Phase 2 scope (AI feasibility, integrations, mobile, advanced forms); Other Key Members: **Irin Mathew** (only named individual) |
| `ALP Screenshots.pdf` (1.2MB, 3 pp) | Product UI screenshots | Lead Management Dashboard (RE, GJ cluster — 5 leads, ALP-2026-0001 to ALP-2026-0072); Leads Tracker (all-format pivot); Lead Details (TEST lead, Overview tab, Progress Timeline 7 stages, Site/Approvals/Legal/Construction tabs, Add Forms sidebar with 6 forms marked Coming Soon, AI Summary marked Coming Soon, Activity Log) |

**Aggregate facts to surface:**

- 9 Phase 1 initiatives (1 Done block, 7 individual Done items, 2 In Progress: AOP-data ingestion + Feedback/Testing). 1 Out of scope for MVP: AI feasibility scoring (Phase 2).
- Lead ID convention: `LD-FY27-0000` (PRD says `LD`, screenshots show `ALP-2026-NNNN` — flag inconsistency, prefer screenshot evidence)
- 11 statuses: Draft, New, Under BT validation, Under Negotiations, Under BT approvals, Under Apex approval, Confirmed Properties, RFC offered, RFC under fit-outs, Operational, Rejected
- 7 Lead Detail tabs: Overview, Site Visit Assessment, Validations, Approvals, Legal, Fit-Out (Construction), Payments
- 7-stage Progress Timeline: Site Details → Validations → Approvals → Legal → Fit-Out → Operational → Rent Declaration
- Approval ladder ends at **Apex** (after RRVL CFO Office, RRVL CLT)
- 100+ formats supported; Phase 1 starts with grocery-related formats only
- 4 manual-update tabs in MVP (Approvals, Legal, Construction, Payments) → Phase 2 integrations: Board (Approvals), Sirion (Legal), R-Dash (Construction), FR Portal/SAP (Finance), Retail Vista (Catchments)
- AOP funnel cards: 5 cards differ between RE view (Balance to Acquire / Under Apex Approval / Under BT approvals / Under Negotiations / Under BT Validations) and BT view (AOP / Operational / RFC Under Fit-outs / RFC Offered / Confirmed Properties)

## 3. Page structure (post-restructure as Add / Keep / Remove diff)

The current page is 9 sections (hero · 4-PRD table · pain-vs-fix · 7 Sub-IPs · Deep cards · Connections · Roadmap · footer). Most of it goes; the remaining shape:

| § | Section | Action | Notes |
|---|---|---|---|
| 0 | Hero | **Keep + correct** | Title `ALP.` stays. Subhead corrected: "Asset Lifecycle Platform" (not Planning). Eyebrow re-tagged `Track 05 · Reliance Retail · NSO platform · MVP live`. Status pills: stage / phase 1 done / phase 2 building / pilot scope. Strip all individual-name tiles. Keep the "How Fynd transforms real estate" prose but rewrite to source: replace Vista/RIL-data/agentic-engine claim with the actual MVP-shipped scope. |
| 01 | What ALP is for Reliance | **Add** | 3-card Problem / Solution / Impact strip. Sourced from PRD framing of the new-store opening process. |
| 02 | Phase 1 · what's live in MVP | **Add** (replaces the "4 PRDs locked" table) | Table of 9 Phase 1 initiatives with status pills, mapped to actual project-plan rows. |
| 03 | Lead lifecycle | **Add** (replaces "Single record per site" pain/fix block) | The 7-tab structure of the Lead Details page, the 11 statuses, and the 7-stage Progress Timeline. Embed `03-overview-tab.jpg` screenshot. |
| 04 | Inside the platform · screenshots | **Add** (replaces "Sub-IPs" card grid + "Deep cards" table) | Lightboxed screenshots of: Dashboard, Leads Tracker, Site Assessment, Approvals tab. 4 cards. |
| 05 | Access model · who sees what | **Add** | RBAC summary: RE (state-scoped) / BT (format-category + region scoped) / Leadership (cross-state). Source: PRD pp. 2-7. |
| 06 | Phase 2 · roadmap intent | **Restructure** (this absorbs the user-approved "keep sub-IPs as Roadmap" decision) | Two groups:<br>**A. Phase 2 plan (project-plan-sourced):** AI Feasibility Scoring · Integrations (Board/Sirion/R-Dash/SAP/Retail Vista) · Mobile lead creation · Advanced forms · Advanced SLA matrix.<br>**B. Roadmap intent (longer-horizon, marked `Roadmap`):** Site selection AI · Lease intelligence · Rent benchmarking · Footfall prediction · Productivity scorecard · Closure/relocation framework · Cross-format visibility. |
| 07 | Connections | **Restructure** | Drop the 3-card "What ALP plugs into" block; the Phase 2 Integrations row in §06 already names every connected system. Replace with 1-line Vista relationship if needed. **Decision · drop the section** (§06 carries the load). |
| Footer | Footer | **Keep + clean** | Drop `Owner · Salman Saudagar (COO, Fynd) · v0.8.4`. Keep only the copyright line per `website-section-authoring` §4 (no author/version metadata on page). |

**Section-numbering note.** After restructure, on-page eyebrow numbers run `01 → 02 → 03 → 04 → 05 → 06`. The §08 Sources block was authored in v0.9.0 and dropped in v0.9.1 per audit decision D8 — inline source eyebrows in §02 and §05 carry the citation chain.

## 4. Data model

Single-page section. No YAML. All copy authored directly in `alp/index.html`. Data structures (status taxonomies, initiative table, RBAC matrix) inlined as `<table>` and `<div>` blocks.

## 5. Asset pipeline

5 screenshots extracted from `ALP Screenshots.pdf` via `pdfimages -j -all`, then trimmed to white background and resized to max 1600px wide JPEG q82. Output:

| Source img | Target | What it shows |
|---|---|---|
| `img-000.png` | `assets/alp/01-dashboard.jpg` | Lead Management Dashboard · RE team view · GJ cluster · 5 leads |
| `img-002.png` | `assets/alp/02-leads-tracker.jpg` | All-format Leads Tracker pivot · Beauty/Electronics/Fashion etc. |
| `img-003.png` | `assets/alp/03-overview-tab.jpg` | Lead Details · Overview tab · 7-stage Progress Timeline · Add Forms sidebar |
| `img-004.png` | `assets/alp/04-approvals-tab.jpg` | Lead Details · Approvals tab · Site Approvals cards |
| `img-006.png` | `assets/alp/05-site-assessment.jpg` | Lead Details · Site Visit Assessment tab · BT view (RE locked) |

Local-only (5 files, ~500KB total — well under the 20-file / 100MB GCS-mirror threshold). All paths in HTML use `/assets/alp/<file>`. Lightbox snippet wired per `website-section-authoring` §6.

## 6. Navigation wiring

`/alp` is already wired into:
- Top-nav mega-menu · Tracks · Special Projects column (every page · ~25 files)
- Home page card grid
- IP Catalog

No new nav edits needed.

## 7. Build / verify

Hand-author `alp/index.html` (single-page section per skill §7 cutoff: ≤6 logical card-groups). Local verify:

```bash
python3 -m http.server 8000
# http://localhost:8000/alp
# Bypass auth: sessionStorage.setItem('fyndrrl_auth_v1', '1'); location.reload();
```

Walk:
- Title reads "Asset Lifecycle Platform"
- All 5 screenshots load + lightbox opens on click + ESC closes
- All 9 initiatives in §02 carry a status pill
- All 7+5 Phase 2 / roadmap-intent items in §06 carry pills (Build vs Roadmap)
- No author/version line in footer
- No individual names in body copy (Irin Mathew may appear in §08 sources caption only if explicitly attributed in plan)

## 8. Phased delivery

Single phase (P1) — full restructure + screenshot wiring. Estimate: 2 hr.

## 9. Decisions

- **D1 · Title correction.** "Asset Lifecycle Planning" → **Asset Lifecycle Platform**. Source: PRD title page + user confirmation in task brief.
- **D2 · No individual names on page.** Strip Karan Muley / Nishant Amin / Shubham Srivastava / Saurav from hero. Per `website-tone-of-voice` §1.1, no claim without source. Project plan names Irin Mathew (PM) — keep optional in §08 Sources caption only if cleanly attributable.
  - **Why:** Source material does not corroborate any of the existing names. Apex-level honesty contract.
  - **How to apply:** Hero stat tiles drop the four "Lead / Co-conceptualisation / Adjacent ops / RIL counterpart" cards. Footer drops `Owner · Salman Saudagar`. No DRI lines anywhere on page.
- **D3 · Status framing = "MVP live · Phase 2 building".**
  - **Why:** Project plan shows 7 of 9 Phase 1 initiatives Done; screenshots show GJ-cluster pilot data with 5 live leads. AI Feasibility (initiative #7) explicitly marked Out of scope for MVP → Phase 2.
  - **How to apply:** Hero status pill is `MVP live · Apr-2026`. Phase 2 initiatives carry `Build` pills. Longer-horizon items carry `Roadmap` pills.
- **D4 · Keep existing 7 "Sub-IP" cards as roadmap intent.**
  - **Why:** User decision — preserve narrative continuity for readers familiar with prior version.
  - **How to apply:** All 7 items collapse into §06B "Roadmap intent" with `Roadmap` pills. Drop all proof-point lines that were lifted from `/retail-vista` ("10.5 Cr buildings indexed", "22 data categories"). Strip per-card DRI lines.
- **D5 · Lead ID format inconsistency.** PRD says `LD-FY27-0000`. Screenshots show `ALP-2026-NNNN`. Use the screenshot format on page (visual evidence > spec doc when they conflict; PRD predates screenshots).
- **D6 · Drop §07 "Connections" card grid.** §06 Phase 2 integrations row already names every connected system (Board / Sirion / R-Dash / SAP / Retail Vista). Renumber on-page eyebrows to a contiguous run.
- **D7 · Section ordering override.** Default §03 = Architecture; here §03 = Lead lifecycle. Documented because ALP's load-bearing structure is the lead-state-machine, not a layered-platform diagram. (Per `website-section-authoring` §4 canonical ordering rules.)
- **D8 · Drop §08 Sources block (v0.9.1).** Audit M1 flagged the Sources block as borderline against tone-of-voice §3 default-no rule. Although the page combines 3 distinct artefacts (carve-out applies), the inline eyebrows in §02 ("Source · ALP project plan for phase 1.xlsx") and §05 ("Source · PRD §Context about teams") already establish provenance. Block dropped to honour the default-no preference. Section labels now run §01 → §06.

## 10. Out of scope

- AI Feasibility Engine deep-dive (initiative is Phase 2; no PRD content yet beyond "blocked on Retail Vista").
- Email-alert content + escalation matrix specifics (Done per plan but no source detail).
- AOP funnel-card numerical thresholds.
- Lead Tracker pivot-table calculation logic (E = A+B+C+D etc.).
- Audit trail backend schema.
- Mobile UX flow (Phase 2).

---
