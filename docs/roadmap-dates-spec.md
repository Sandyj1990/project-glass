---
spec: roadmap-dates
purpose: Map roadmap line items currently shown on register pages to dates evidenced in their `*-notes-compilation/` source files. Updates the pages with explicit dates without disrupting current copy.
status: draft · awaiting sign-off · DO NOT IMPLEMENT YET
as-of: 03-May-2026
owner: <fill>
---

# Roadmap Dates · Spec

## 0 · Why

Several register pages carry a "Roadmap" pill or section listing line items (e.g., *Phase 1 · within electronics*, *Production rollout*, *Plant-wide rollout*) without a date. The dates exist in the source compilation files (board notes, status reports, project-plan XLSX, concept notes) but did not survive the page authoring step. This spec catalogues every item, attaches the source-evidenced date, flags where no source date exists, and proposes a single consistent visual treatment so we can update all pages in one sweep without breaking the existing copy register.

**Non-goals.** New roadmap items. New copy. Re-prioritising. Anything that changes the *meaning* of what a page already says — only adding the date that should already have been there.

---

## 1 · Date format & visual treatment

Tone-of-voice rule: dates in user-facing copy are `DD-MMM-YYYY` (e.g., `10-Apr-2026`). Where a source uses a window (e.g., "Months 1–4 from May 2026"), render as `May–Aug 2026`. Where a source uses a quarter, render as `Q2 FY27` or `Apr–Jun 2026` (whichever the source uses verbatim).

Three placement patterns are already in use across the register; this spec adopts them as-is rather than introducing new ones:

| Pattern | Example currently on register | Use when |
|---|---|---|
| **A · Pill suffix** | `<span class="pill pill-phase2">Roadmap · 6 months</span>` (swapeasy) | Section pill — single window covering the whole roadmap |
| **B · cap-num row** | `<div class="cap-num mb-3">Phase 1 · live · 28 - Apr - 2026</div>` (granary) | Per-phase heading inside a roadmap card |
| **C · Inline bullet suffix** | `Phase 1 · within electronics · laptops · tablets …` → append ` · May–Aug 2026` | Roadmap bullet list where each item has its own window |

**Rule.** Add the date with a ` · ` separator. Never restructure the bullet. Never replace existing copy.

---

## 2 · Source coverage matrix

Pages grouped by date-evidence strength. Only pages with both (a) a current roadmap section AND (b) a notes-compilation source are listed. Pages with no source-evidenced date are flagged as **GAP** at the end.

### 2.1 · swapeasy — STRONG
**Source.** `docs/swapeasy-notes-compilation/SwapEasy_APEX_Board_Note.docx` (dated May 2026)
**Anchor date.** Document date is `May 2026` → "Months 1–4" = May–Aug 2026; "Months 4–6+" = Aug–Nov 2026; "Day 60" = 30-Jun-2026 (relative to 01-May-2026).

| Page item (current) | Proposed date suffix | Source citation | Conf. |
|---|---|---|---|
| `Phase 1 · within electronics · laptops · tablets · smartwatches · TVs & large appliances` | ` · May–Aug 2026` | Board Note §4 "Phase 1 — Beyond Mobiles, Within Electronics (Months 1–4)" | High |
| `Phase 2 · beyond electronics · home & living · kitchenware · online + omnichannel exchange` | ` · Aug–Nov 2026` | Board Note §4 "Phase 2 — Beyond Electronics (Months 4–6+)" | High |
| `Multi-Liquidation Partner bidding engine` | ` · in flight · target by Aug 2026` | Board Note §4 "Platform & Capability Investments (Parallel)" — runs alongside Phase 1 | Med |
| `Auto reconciliation + Liquidation Partner ledger` | ` · in flight · target by Aug 2026` | Same | Med |
| Section pill `Roadmap · 6 months` | No change (already dated implicitly via "6 months" + page anchor `Live · Feb 2026 reporting period`) | — | — |
| §01 "Building · next 60 days" bullets (Network adoption push, LP rebalance, …) | ` · by 30-Jun-2026` | Board Note §3 "Next 60 Days" + Table "Outcome by Day 60" | High |

### 2.2 · jcp/rcpl — STRONG
**Source.** `docs/rcpl-notes-compilation/RCPL Digital Platform - Monthly Status Report .pdf` + `RCPL_APEX_Board_Note_Detailed.docx` (dated 1 May 2026)
**Anchor date.** "Next 60 days" relative to `01-May-2026` → ends `30-Jun-2026`. Apex Note "Next 6 Months" = May–Oct 2026.

| Page item (current) | Proposed date suffix | Source citation | Conf. |
|---|---|---|---|
| Hero pill `Phase 2 · 4 domains queued` | ` · scoped for May–Oct 2026` | APEX Board Note "Next 6 Months · The AI-Native DMS Platform for RCPL" | High |
| `Pre-Sales` POD 1 row (status: In flight) | Add row caption ` · go-live week of 05-May-2026` | Monthly Status §Escalations: "Pre-sales was originally going live on 10th April … pre-sales deployment is confirmed for next week" (report week 28-Apr-2026) | High |
| Apr-28 deployment items (40+ shipped, 5 workflow areas) | Already covered by hero "5 delivery PODs" — add cap-num `Deployed · 28-Apr-2026` above table 02 | Monthly Status §Deployment Update | High |
| `Van Sales + Multi-Role UAM` (decision needed) | ` · timeline pending business sign-off · scope May–Oct 2026` | Monthly Status §Phase 2 Roadmap "Timeline not yet confirmed" | High |
| `Non-Beverage SFA (Multi-Segment Mapping + Beat Mgmt)` | ` · awaiting initiation · scope May–Oct 2026` | Same | High |
| `Anchor Order Fulfilment` | ` · scope undefined · target H2 FY27` | Same — flagged as "significant coverage gap" | Med |
| Phase 2 Roadmap section header | Add cap-num `Roadmap · May–Oct 2026 (next 6 months)` | APEX Board Note framing | High |

### 2.3 · fynd-horizon — STRONG (mostly already dated)
**Source.** `docs/fynd-horizon-notes-compilation/Fynd_Horizon_D02.pptx` (PPTX text mentions Q2 2026)

| Page item (current) | Proposed date suffix | Source citation | Conf. |
|---|---|---|---|
| `15-Jul-2026 · public launch · Nexus Seawoods` | No change — already dated | Page already aligned | High |
| `Pre-cut pipeline at scale · target factory yield +18% by Q2 2026` | No change — already dated | PPTX confirms "Q2 2026" | High |
| `Expansion beyond Mumbai cluster · sequencing TBD with Trends ops` | Leave as TBD — no source date | — | GAP |
| `On-call rotation · 5-minute page-out on any photoreal drift > 0.5%` | Leave as is — operational, not roadmap | — | n/a |
| `L3 autonomy targets · per the autonomy framework that anchors the 30-Apr-2026 letter to MM Sir` | No change — already dated | Already cites letter date | High |

### 2.4 · forge — STRONG (single-date all items)
**Source.** `docs/forge-notes-compilation/Neolync_Fynd_Forge_Production_Readiness_v2.xlsx` (Version 2.0 · 07-Apr-2026)
**Observation.** Every checklist row has Target Date `10th APRIL 2026` (= `10-Apr-2026`). Page already covers this via §04 "Pilot · NeoLync Tirupati · Phase 1" → `Go-live validation runs against a 15-category checklist (v2.0 · 07-Apr-2026)`.

| Page item (current) | Proposed date suffix | Source citation | Conf. |
|---|---|---|---|
| `Roadmap · plant-wide rollout · Industry 5.0 agentic stack` (hero pill) | ` · post Phase 1 (Apr 2026)` | XLSX Legend: "Phase 1 = Planning & Traceability (current go-live phase)" | Med |
| §04 "Phase 1 · Planning & Traceability" | Add `Target · 10-Apr-2026` cap-num under heading | XLSX Target Date column | High |
| Phase 2 / Phase 3 (if listed on page — not in current grep) | n/a | XLSX Legend has no Phase 2 dates | GAP |

### 2.5 · alp — PARTIAL
**Source.** `docs/alp-notes-compilation/ALP project plan for phase 1.xlsx` (two sheets: Phase 1 + Phase 2)
**Observation.** Sheet 1 (Phase 1) has Status column populated (Done / In Progress / Out of scope) but no Start/End Date columns. Sheet 2 (Phase 2) has explicit `Start Date` and `End Date` columns — both **empty** for every row.

| Page item (current) | Proposed date suffix | Source citation | Conf. |
|---|---|---|---|
| `Live for the GJ-cluster pilot · Apr-2026` | No change — already dated | Page-internal | High |
| `Phase 2 plan: AI Business Feasibility scoring + 6 platform integrations …` | Leave undated — Sheet 2 has no dates | — | **GAP** |
| `4 manual-update tabs ready for Phase 2 integration with Board / Sirion / R-Dash / SAP` | Leave undated — same gap | — | **GAP** |

**Action.** Flag this gap to the ALP owner; ask for Phase 2 Start/End dates before the page is updated. Until then, leave Phase 2 copy as-is.

### 2.6 · samarth — STRONG
**Source.** `docs/samarth-plus-notes-compilation/MODULE_WORK_BREAKDOWN.pdf`
**Observation.** Six dated phases, Oct 2025 → Apr 2026. Page already says `Live · Apr 2026` and `Prod cutover · Apr 2026`.

| Page item (current) | Proposed date suffix | Source citation | Conf. |
|---|---|---|---|
| `Live · Apr 2026` | No change — already dated | Phase 6 (Apr 2026 · Prod limited pilot) | High |
| `Building · In flight` bullets (Bulk-upload, BU-master role mapping, Career Tree, Activated-certification) | ` · in Phase 6 prod stabilisation · post-Apr 2026` | PDF Phase 6 detail; "bulk-upload tooling built specifically for the prod data lift" appears in Phase 5 (Mar 2026) | High |
| `Roadmap · 6–12 mo` pill | No change — pill already gives a window | Page-internal | High |
| `Smart Proctoring Agent / Action Learning Projects / LMS+IJP / Workforce Intelligence` | Leave undated — source has no dates for these | — | **GAP** (forward-looking AI agents not on the dated phase plan) |

### 2.7 · retail-jarvis — STRONG (anchor) · PARTIAL (rollout)
**Source.** `docs/retail-jarvis-notes-compilation/2026-04-30-farooq-mda-update-letter.md`

| Page item (current) | Proposed date suffix | Source citation | Conf. |
|---|---|---|---|
| `01 - May - 2026` status anchor | No change — already dated | Page-internal | High |
| `11-page cornerstone working note shipped 26 - Nov - 2025 (working-note rev 16 - Dec - 2025)` | No change — already dated | Page-internal | High |
| `Production rollout · Multi-store · non-biometric by design` | ` · this quarter (target Jul 2026)` | MDA letter "the path for each to reach L3/L4 autonomy this quarter" — Q ending Jun 2026 from a 30-Apr-2026 anchor | Low (interpretive) |
| `Product to be re-housed under Impetus as Impetus Jarvis per Farooq` | No change — not a roadmap item | — | n/a |

**Action.** "this quarter" reading is interpretive. Confirm with Farooq before adding the date suffix.

### 2.8 · dark-factory — GAP (date placeholders in source)
**Source.** `docs/mtm-notes-compilation/Mobile_Tailor_Concept_Note_Formatted.md`
**Observation.** Phase Gate Plan exists with Alpha / Beta / Gamma stages but each says `<<DATE NEEDED>>`. Source explicitly flags the gap.

| Page item (current) | Proposed date suffix | Source citation | Conf. |
|---|---|---|---|
| `Phase 1 · Alpha · Pending sign-off` | Leave undated until concept note is updated | Source: `<<DATE NEEDED>>` | **GAP** |
| `Phase 2 · Beta · Roadmap` | Same | Same | **GAP** |
| `Phase 3 · Gamma · Roadmap` | Same | Same | **GAP** |
| `Roadmap · Beta & Gamma · AJIO-permanent` (hero pill) | Leave as-is | Same | **GAP** |
| `Live at RCP since 31-Mar-2026, Mumbai cluster since 27-Apr-2026` | No change — already dated | Page-internal | High |

**Action.** Date this section only after the MTM concept note's `<<DATE NEEDED>>` placeholders are filled in by the product owner. Do not invent dates.

### 2.9 · Marketing Agent (no register page yet) — REFERENCE
**Source.** `docs/agent-catalog-notes-compilation/Autonomous_Marketing_Platform_Multi_Agent_Framework.docx` (dated 06-Feb-2026)
**Observation.** Explicit 30-60-90 day roadmap. Document not yet bound to a register page (agent-catalog → /agents directory route to confirm). Recording dates here for when it is wired in:

| Source item | Resolved date |
|---|---|
| Days 1–30 · MVP (brand-aware content gen, intent-driven audiences, assisted campaign setup) | 06-Feb-2026 → 08-Mar-2026 |
| Days 31–60 · intelligence + orchestration | 09-Mar-2026 → 07-Apr-2026 |
| Days 61–90 · full autonomous decisioning | 08-Apr-2026 → 07-May-2026 |

### 2.10 · retail-vista — WEAK
**Source.** `docs/retailvista-notes-compilation/RetailVista_Status_Update.pdf`
**Observation.** Page is already heavily dated (`01 - May - 2026` anchor; Steering / Data Partners named). The Status Update PDF treats roadmap items at capability level only — no per-item dates.

| Page item (current) | Proposed date suffix | Source citation | Conf. |
|---|---|---|---|
| `Roadmap · 1000-city scale · Pricing · Customer Listening · SCM · Land Parcel · TAM` | Leave as-is | — | **GAP** |
| `01 · Scale / 05 · Customer Digital Twin / 06 · Network reference` (Roadmap pills) | Leave as-is | — | **GAP** |

---

## 3 · Pages with no source-date coverage

These pages have a roadmap section but the corresponding `*-notes-compilation/` folder has no dated roadmap source. Leave undated unless a new source is provided.

- **ucp** — `Roadmap · AI-Native UCP · full agentic chat` and `Next horizon · L4` items. No dated source in `ai-native-notes-compilation/` or elsewhere.
- **kio** — `Roadmap · Beauty + Grocery vertical pilots`. PPTX has no dated roadmap.
- **autri** — `Roadmap · grocery-estate rollout`. No source date doc.
- **fynd-konnect** — `Next horizon · Roadmap`. PDFs are platform pitch decks, no roadmap dating.
- **tms** — `From the platform roadmap (deck slide 30 · "TMS of the Future")`. Deck slide reference is the only anchor; not date-bound.
- **hirefirst** — Module roadmap pills (Prompt-to-JD, Similar Job Detection, Auto Stage Configure). No source compilation folder.
- **granary** — Already dated (`Phase 1 · live · 28 - Apr - 2026`); "Roadmap · STP · CDT · Consensus Forecasting" pill — leave as-is.
- **impetus/recollect** — Single-line roadmap mention, sub-page; out of scope for this sweep.

---

## 4 · Open items requiring product-owner input before page edits

| Page | Question | Owner |
|---|---|---|
| **alp** | What are the Start/End dates for the 7 Phase 2 initiatives? Sheet 2 of `ALP project plan for phase 1.xlsx` has the columns but they are empty. | ALP PM |
| **dark-factory / MTM** | Concept note has `<<DATE NEEDED>>` for Alpha / Beta / Gamma. Confirm or commit dates. | MTM PM |
| **retail-jarvis** | Confirm "Production rollout · this quarter" reading from the 30-Apr-2026 MDA letter — is target Jul 2026 correct, or should it be later? | Farooq |
| **retail-vista** | Three Roadmap pills (Scale / CDT / Network reference) have no date in source — provide windows or leave undated? | RV PM |
| **forge** | XLSX is single-date (10-Apr-2026 across all 220 rows). Is there a Phase 2 source with later dates, or is plant-wide rollout intentionally undated? | Forge PM |

---

## 5 · Implementation sequence (after sign-off)

1. **Sign-off.** This spec → green light from page owner per page.
2. **Resolve §4 open items.** Do not edit pages that depend on missing source dates.
3. **Per-page edits.** One commit per page, scoped to date suffixes only. Commit pattern: `<page> · roadmap · add source-evidenced dates`. No copy changes beyond the ` · DATE` suffix.
4. **Verify.** For each updated page: contiguous section labels (`grep -n 'section-label mb-3">[0-9]' …`), tone-of-voice date format `DD-MMM-YYYY`, no banned vocab introduced.
5. **Audit.** Run `website-page-reviewer` against each updated page; resolve HIGH + MEDIUM findings; write audit JSON to `docs/audits/`.
6. **Nav untouched.** No `tools/site_chrome.py` change; this is a content-only sweep.

---

## 6 · What this spec does NOT do

- Add new roadmap items not currently on the page.
- Change ordering, prioritisation, or framing of existing items.
- Touch the nav, footer, or `tools/site_chrome.py`.
- Create new pages.
- Add `§Sources` blocks, attribution lines, or owner footers (banned per CLAUDE.md).
- Invent dates where the source has none — the GAP rows above stay GAP until a source is provided.
