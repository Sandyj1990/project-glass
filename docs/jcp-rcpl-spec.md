---
status: draft
owner: Kushan Shah
route: /jcp/rcpl
mode: new section (sub-page under /jcp)
shape: single-page (≤6 sub-pages — hand-authored, no renderer)
source folder: docs/rcpl-notes-compilation/
narrative anchor: 2026-04-30 Farooq letter to MM Sir — RCPL is named under "Fynd – Retail Projects · Special Projects" alongside ALP and RetailVista
sibling pages: /jcp · /jcp/channels · /jcp/cataloging · /jcp/7eleven · /jcp/release-notes
---

# §0 · What's changing and why

New JCP sub-tab: `/jcp/rcpl/`. The current JCP register has no surface for RCPL even though Fynd has full ownership of RCPL's end-to-end digital platform — Pre-Sales, Van Sales, Primary DMS, CTS, Pricing & Promotions, SFA — across five PODs in production. This page closes that gap with one document: status today, what shipped in March-April, what's deploying 28-Apr, and the AI-native FMCG OS plan for the next six months.

Triggered by the 2026-04-30 Farooq letter brief and the 2026-05-01 APEX Board Note. Source corpus is in `docs/rcpl-notes-compilation/` (Monthly Status Report, APEX Board Note, DMS Knowledge Base, 7 SOPs).

# §1 · Why this page exists

**Audience.** RIL Apex leadership (MM Sir level). Reading window: 60-90 seconds before scrolling for evidence.

**Gap to close.** The 2026-04-30 letter to MM Sir lists the Fynd – Retail Projects portfolio. RCPL is a ₹20,000 Cr FY26 run-rate business and one of Fynd's largest single-platform mandates, but it does not yet have a register surface. JCP itself names RCPL in its "B2B businesses" line on `/jcp/` and in `/jcp/channels` — but that's an entry in a list, not a status.

**Narrative anchor.** RCPL has scaled to ₹20,000 Cr in run-rate revenue in under three years. Fynd now owns the end-to-end DMS — inherited with structural debt, stabilising and scaling at the same time — and is architecting a dedicated AI-native FMCG OS as the long-term home for the business. The page reports both tracks honestly.

# §2 · Source inventory

| File | What it gives the page |
|---|---|
| `RCPL_APEX_Board_Note_Detailed.docx` (1-May-2026) | North star; AI-native DMS plan; 4-layer architecture (AI Sales Agent, NextGen SFA, NextGen DMS, eB2B); §06 vision content; ask of the board |
| `RCPL Digital Platform - Monthly Status Report .pdf` (24-Apr-2026, v1.0, Leena B / Ashish C) | §01 status strip; §02 5-POD table; §04 release notes; §05 in-flight 28-Apr cycle; §07 Phase 2 roadmap |
| `RCPL_DMS_Knowledge_Base.pdf` | §03 architecture (6 platform surfaces, URLs, stakeholder roles) |
| `SOP for Saarthi.pdf` | Saarthi description (assisted ordering for ASM/ASE) |
| `SOP – How to Use RCPL CSO App.pdf` | CSO App description (FOS field-facing tool, secondary orders) |
| `SOP for RCPL Primary DMS Onboarding and admin data.pdf` | Primary DMS T-4 → T0 timeline + 5-step distributor ordering flow |
| `SOP – Primary Ordering by Distributor.docx` | Distributor portal capabilities |
| `SIGNATURE RETAILER ONBOARDING SOP 1 (1).pdf` | Signature retailer program (premium onboarding, penny drop) |
| `BN-73 Pre-sales last mile delivery & settlement.docx` | Pre-Sell delivery requirements |
| `CTS - SOP Permanent Forward Flow.docx` | CTS 12-stage workflow |
| `Pricing User Manual.docx` | Pricing hierarchy (Retailer / Distributor / Anchor + Schemes + Virtual groupings) |
| `Article Creation SOP.docx` | Article creation pipeline (CMS → DMS) |

All files local to `docs/rcpl-notes-compilation/` (Stage 0 done).

# §3 · Page structure

Follows the canonical §3 ordering. Single-page, hand-authored.

| § | Title | Lens |
|---|---|---|
| Hero | `JCP · RCPL · Live` + H1 + 3-line subhead + 4 stat tiles + 3 ownership cards | The fact: ₹20,000 Cr business, Fynd-owned platform |
| 01 | **Status · 24-Apr-2026 cycle** | 3-strip: Delivered / In flight / Phase 2 roadmap |
| 02 | **What's live · 5 delivery PODs** | POD table — initiative · business impact · BU |
| 03 | **Architecture · Six platform surfaces** | 6 surface cards — Admin Portal · Distributor Platform · CSO App · Saarthi · CMS · CTS |
| 04 | **Recent shipments · Mar-Apr 2026** | 3-column release notes — Release 1 (CTU verification) · Release 2 (BPO + dashboards) · Release 3 (CTS + field ops) + headline tiles |
| 05 | **In flight · 28-Apr-2026 deployment** | 15-item table grouped by module |
| 06 | **Vision · AI-native FMCG OS** | 4-layer card stack — AI Sales Agent · NextGen SFA · NextGen DMS · eB2B for retailers |
| 07 | **Phase 2 roadmap · decisions needed** | 4-item table — what's queued, what action is needed, who decides |
| 08 | **Sources** | Card list of the 12 source artefacts in compilation folder |

§07 is a kept exception — Phase 2 is not "in flight"; it is *waiting on Reliance decisions*. Apex is the audience; this is the page where they see what to unblock.

§08 Sources block kept (deviation from default-no rule): this page synthesises 3 distinct named artefacts (Board Note, Monthly Status, DMS KB) plus 9 SOPs the reader may want to navigate to. Multi-artefact synthesis qualifies under the skill's exemption.

# §4 · Data model

No YAML — this is a single-page section, hand-authored. Source citations sit inline as `cap-num` eyebrows above the content they support (e.g., *"Source · Monthly Status Report · 24-Apr-2026 · p. 2"*).

# §5 · Asset pipeline

No images required for v1. The Monthly Status PDF's screenshots are bullet-text + UI screenshots embedded — would need `pdfimages -j` extraction per skill §6. Defer until v2 when actual product UI screenshots are useful (Apex doesn't need release-note screenshots).

# §6 · Navigation wiring

This is a JCP sub-page, so the only required edit is the JCP subnav row, which appears in **5 files**:

- `jcp/index.html` (line 77)
- `jcp/channels/index.html`
- `jcp/cataloging/index.html`
- `jcp/7eleven/index.html` (line 77)
- `jcp/release-notes/index.html`

Add `<a href="/jcp/rcpl" class="subnav-link">RCPL</a>` to each row. Position: between `7-Eleven` and `Release Notes` (chronological by ship-order).

Top-nav mega-menu: **no edit needed** — RCPL is reached via JCP, not as a top-level track. JCP already appears in the Platforms column.

Home page card: **no edit needed** — JCP card already mentions RCPL in the B2B body copy.

# §7 · Build / verify

```bash
python3 -m http.server 8000
# open http://localhost:8000/jcp/rcpl
```

Auth bypass: `sessionStorage.setItem('fyndrrl_auth_v1','1')` in DevTools console.

Visual checks via Chrome DevTools MCP — full-page screenshot, console scrub.

# §8 · Phased delivery

P1 (this commit): Spec → page → subnav wiring → local verify → page-reviewer audit. ~2-3 hours.

P2 (later, if asked): Add product UI screenshots from the Monthly Status PDF (pdfimages extraction). Add architecture diagram if RIL counterpart provides one. Embed the Board Note PDF or the Monthly Status PDF as a downloadable artefact at the top of §08 Sources.

# §9 · Decisions

- **D1 · Page lives under `/jcp/rcpl/` (sub-tab) not as a top-level `/rcpl` route.** Why: the user brief explicitly says "tab under JCP page similar to existing tabs"; RCPL transacts on JCP rails (DMS is the FMCG vertical of JCP). How to apply: subnav wiring only; no top-nav mega-menu edit.
- **D2 · Keep §08 Sources block.** Deviation from default-no. Why: 3 distinct strategic artefacts (Board Note + Monthly Status + DMS KB) plus 9 SOPs — reader may need to disambiguate which fact came from where, and the 7 SOPs are themselves reference artefacts the reader can navigate to.
- **D3 · Vision section (§06) marked vision/proposal, not Live.** Why: the AI Sales Agent / NextGen SFA / NextGen DMS / eB2B are *six-month plan asks of the APEX board*, not built features. How to apply: section eyebrow says `Proposal · 6-month plan`; no `Live` pills inside; sub-points carry no dates because Board Note doesn't bind them to dates.
- **D4 · Footer matches sibling JCP pages** (carries the `Owner · Salman Saudagar (COO, Fynd) · v0.8.4` line for visual consistency with `/jcp/`, `/jcp/7eleven`, `/jcp/cataloging`). Why: a register-wide author/version sweep is a separate task; introducing inconsistency on a single new page is more confusing than carrying the deprecated line one more time. How to apply: when the register-wide sweep happens, this page comes along with the rest.
- **D5 · Module body uses RCPL acronyms verbatim** (CSO, ASE/ASM, BPO, CTS, SAP, CCO, GRN, FOS, SFA, DMS, FMCG, Saarthi, Samruddhi, HPC). Why: these are the names RCPL operators use; an Apex reader scanning for whether the platform actually covers their world wants to see the words. How to apply: introduce the term inline on first use (e.g., "CSO · channel sales officer"), then use the short form. Don't translate to generic English.
- **D6 · Numbers used on the page (verbatim from source).** ₹20,000 Cr (FY26 run-rate); 5 PODs; ₹5,000 Cr+ order coverage UAT; 1.86 L assets; 40+ items deployed Mar-Apr; 15 items in 28-Apr cycle; ~35,000 physical CSO visits eliminated; 1 critical security fix; 9 data-correction scripts (20-Apr-2026); 60-70% of L1 tickets to be resolved by Multi-Segment + Beat Mgmt; 20-30% DBs are anchors; ~₹50 Cr asset-loss avoidance; ~₹1 Cr FTE optimisation; ₹1,200 Cr/month pricing coverage; ₹500 Cr/month Auto DO orders; ₹1,000 Cr/month non-bev primary; ~₹4,000 Cr Pre-Sales Beverage; ~₹1,000 Cr Van Sales Beverage. All sourced to Monthly Status Report and Board Note.

# §10 · Out of scope

- Per-SOP deep-dive pages (one per workflow). Defer — the user can browse the SOPs directly from §08 Sources if needed.
- Live screenshots / video tours of the platform UIs.
- A separate `/rcpl` top-level route (D1).
- Embedded PDF viewers for the Board Note or Monthly Status.
- Detailed Phase 2 timeline commitments — those belong on the next Monthly Status, not on this register surface.
- Marketing/competitive framing vs HUL/P&G or commercial DMS products.
