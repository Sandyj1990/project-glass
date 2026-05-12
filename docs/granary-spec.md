# Granary page · Restructure spec

**Status:** v0.2 · 2026-05-01 · **shipped (page at v0.9.2)**
**Owner:** Kushan Shah
**Route:** `/granary/` (already live; this spec restructures it)
**Source content:** `docs/Granary project documents dump/` (user-supplied; canonical compilation folder by reference)
**Narrative anchor:** Granary is the live grocery planning + assortment platform on the Cortex stack. This restructure re-anchors the page around the 28-Apr-2026 status truth: 11-store pilot is live and validating, the Command Centre is the in-build next-gen surface (5 of 37 routes wired today, 27 still mock), and SAP integration + ODBC scale-up are the immediate gates to the 3K-4K-store rollout.
**Inherits from:** `docs/website-orientation-spec.md` · `docs/hirefirst-spec.md` (canonical update-mode template) · `website-tone-of-voice.md` for register.

**Built using:** `.claude/skills/website-section-authoring` (workflow) + `.claude/skills/website-tone-of-voice` (copy register).

---

## 0. Implementation status

| Stage | Deliverable | Where it lands |
|---|---|---|
| 0 raw | Source compilation folder | `docs/Granary project documents dump/` (user-supplied — keeping original name; the skill convention `docs/granary-compilation/` is reserved for any future net-new dumps) |
| 1 spec | This file | `docs/granary-spec.md` |
| 2 data | Single page · no YAML; copy authored inline (≤6-card hand-author rule from skill, although page has more sections — value of a renderer for this section is low because content is bespoke per-block) | `granary/index.html` |
| 3 assets | 6 Command Centre screenshots from `Screenshots.pdf` (pages 1, 11, 12, 14, 15, 5) — extracted, resized, web-named | `assets/granary/command-centre/` |
| 4 build | Hand-authored HTML, full-page rewrite of `granary/index.html` per §3 diff below | `granary/index.html` |
| 5 nav | Already wired in mega-menu (`Platforms` column); no nav edits unless home-page card numbers are stale | check `index.html`, `catalog/index.html` only |
| 6 verify | Local server walk + Chrome DevTools screenshot + console clean + every claim traceable to a source file in §2 | — |

---

## 1. What's changing and why

The current `/granary` page (v0.8.4, written 30-Apr) is **bullish** — it presents Phase 1 modules as "all completed", lists 12 sub-IPs as Live/Pilot/Build with no built-percent nuance, and frames the 13-module Granary vision as if it's mostly already shipped. The 28-Apr-2026 source material flips this:

**The 28-Apr Update brings five new threads not yet on the page:**
1. **11 pilot stores** in Mumbai (page says 10), now also serving **Smart Point** alongside Smart Bazaar
2. **SAP integration** dev complete across SAP/RDIP/Cortex; IRM raised for IP whitelisting; testing **expected this week** (page is silent on SAP)
3. **ODBC → Databricks views** in progress — the explicit gate to scaling beyond 11 to 3,000–4,000 stores
4. **DC Demand Forecasting POC** for NCR (100+ stores) for vendor ordering
5. **Top 250 SKU availability checklist** deployed; system auto-derives top SKUs and shares with store ops

**The Command Centre Status Report adds the honesty thread:** of the 13-module Granary vision, **~15-20% is built today**. The Command Centre (Granary's new unified front-end, deployed in SIT) has 33 backend endpoints all live and DB-connected, but only **5 of 37 frontend routes** are wired to real data — Home/Dashboard, Category Overview, Range Review, Delist Detail, Requests. The other 27 routes are mock-data scaffolding for Forecasting, Pricing, Fresh, Supply Chain, Store Execution, Calendar, etc.

**Two truth-states to honour** (mirrors the hirefirst pattern):
1. **Live for RIL today** — the 5 real Command Centre routes + the underlying ML Forecasting on Databricks + Cortex assortment/MBQ engines that have been in production since 13-Nov-2025.
2. **Building / Roadmap** — Command Centre is in build (deployed in SIT, consolidating modules onto a single UI; 5/37 routes real, 27 in design/mock today), SAP integration is in test this week, ODBC is the scale-up gate, DC POC is running, and STP/CDT/Consensus Forecasting/MDQ-planogram are the next-horizon roadmap.

**Pill convention** (mirrors `/hirefirst`): `Live`, `Building`, `Roadmap`. Every borrowed claim from the Command Centre Status Report or the Apr-28 update carries a pill. The Command Centre itself is **Building** — the screenshots show real product UI but the surface as a whole is in build, with only 5 routes carrying live data today.

**Audience.** RIL Apex leadership reviewing the register. Same audience as `/impetus`, `/jcp`, `/hirefirst`. Undertells beat overtells — the page builds trust for the asks (SAP IRM whitelisting, ODBC connectivity) by matching what they'd hear from Mayank, Aushin, Shahid in the same week.

---

## 2. Source inventory

| File | Type | Key facts derivable |
|---|---|---|
| `Granary_Update_Apr28.md` | Leadership update memo (5 sections: Current State / Achievements / Command Centre / Roadmap / Positioning) | 11 pilot stores · 10 segments (Food + HPC) · Smart Bazaar + Smart Point · SAP dev complete + IRM · ODBC + Databricks · DC POC NCR 100+ · Top 250 checklist · STP/CDT/Consensus Forecasting roadmap |
| `Granary_Weekly_Update_Apr28.md` | Weekly status note (Executive Summary / Current Status / What's Coming Up / Governance) | Same threads, adds: "Command Centre exception-driven homepage live — surfacing overstock, zero-stock, and DOH issues with priority-ranked queues (P1/P2/P3)"; "MBQ now article-level precision per store" |
| `Granary Command Centre Current State.txt` | Backend/frontend status report (Backend API endpoints / Frontend routes / Full-vision-vs-current table / Roadmap with effort estimates) | 33 backend endpoints all working · 37 frontend routes (5 live: Login/Dashboard/Assortment/Delist Detail/+1) · 13-module vision with built-% per module (Command Center 30% / Store Intelligence 0% / Assortment 40% / Demand Forecasting 0% / Inventory 25% / Supplier 0% / Pricing 0% / Fresh 0% / Supply Chain 0% / Store Execution 0% / Calendar 0% / Capital Efficiency 10% / Admin 5%) · ~15-20% of vision built |
| `Addional Context.txt` | Tue-28-Apr meeting notes (assortment workflow + data pipeline) | Excel-based rules now automated · Top 250 SKU checklist · SAP UAT testing · ODBC → 3K-4K stores · MBQ article-level · DC vendor ordering · Fresh/dairy on database · CDT/SAP/planogramming next |
| `Screenshots.pdf` (24 pages, 7MB, screenshots of the Command Centre web app) | Real product UI | Live evidence: Home/Exceptions/DOH heatmap (p.1) · Range Review with Classification Matrix CX/CY/CZ + Margin-vs-Volume quadrants (p.11) · Category Overview Drinks with Sales Trend / Margin YoY / Region-wise / Overstocked-stores (p.12) · Baseline Forecast article list (p.14) · Home extended dashboard (p.15) · Delist workflow modal + multi-select (p.5, p.8-10). Pages 17-24 show an older/mockup Rules + Assortment-Projects UI — skip. p.3 is Jira-internal — skip. |
| `Granary Cortex - CLT Review v2.docx` | CLT review doc (26-Apr-2026) — not parsed in detail; reference for Cortex framing | Source citation for Cortex case study |
| `Cortex for Granary — Assortment Planning and Inventory Optimization System V3.pdf` | Functional architecture doc | Confirms Cortex = the planning sub-platform; Assortment + Inventory Optimization scope |
| `Granary Platform – One Pager Summary.docx` | High-level one-pager (26-Oct-2025) | Strategic anchor; predates current restructure but useful for cross-checking the Granary story arc |
| `Granary_Scope_of_Work.docx` | SOW (2-Mar-2026) | Module scope reference |
| Existing page evidence (kept from current `/granary/index.html`) | Cortex case study (17-Apr-2026 · Aushin Ganguli) | +3.8pp OSA · −19.5% inventory · −28% shelving events · 16-loc validation MAPE 41% |

**Aggregate facts to surface** (post-restructure):

- **Phase 1 today**: 11 pilot stores in Mumbai · 10 merchandise segments (Food + HPC) · Smart Bazaar + Smart Point teams validating
- **Modules running in production**: ML Forecasting on Databricks (12K SKUs × 4K stores · 48M rows · MAPE 41% from 55%+ baseline), Cortex Planning (Assortment Intelligence + MBQ Automation + Range Review), Top 250 SKU availability checklist
- **Verified outcomes** (from Apr-17 Cortex case study): +3.8pp on-shelf availability · −19.5% inventory value · −28% shelving events
- **Command Centre** (in build): 33 backend endpoints live + DB-connected · 37 frontend routes (5 wired to live data: Home, Category Overview, Range Review, Delist Detail, Requests) · exception-driven homepage live (Zero Sales / Negative Inventory / High DOH alerts) · DOH treemap heatmap · multi-select delist workflow with reason classification · daily prod deploys
- **In flight this week**: SAP API testing (IRM whitelisting closing), ODBC + Databricks pipeline finalization (gates 3K-4K-store scale-up), DC Demand Forecasting POC (NCR 100+ stores), business UAT closure (Smart Bazaar + Smart Point)
- **Roadmap** (named): Straight-Through Processing (80–90% routine assortment auto-processed) · Customer Decision Trees (shelf arrangement from shopper purchase patterns) · Consensus Forecasting (maker-checker workflows · seasonal auto-handling · statistical store clustering) · MBQ + planogramming integration for MDQ values · Fresh FNV shrinkage tracking
- **Vision honesty**: ~15-20% of full 13-module vision built today · roadmap durations from Status Report (Store Intelligence ~3 weeks, Demand Forecasting UI ~3 weeks, complete Assortment ~2 weeks, complete Inventory ~2 weeks, Pricing ~3 weeks, Fresh ~2 weeks, Supplier ~2 weeks, Supply Chain ~3 weeks, Store Execution ~2 weeks, Calendar/Capital Eff/Admin ~4 weeks)

---

## 3. Page structure (post-restructure)

The current page has 8 sections. Final shape (after v0.9.2 trims to 8 sections — see D7) has hero + 8 numbered sections.

```
CURRENT (v0.8.4)                                       POST-RESTRUCTURE (v0.9.2)
─────────────────────────────────────────────────      ─────────────────────────────────────────────────
§0  Hero (stats + team)                          →     §0  Hero (refreshed numbers + status pill + 3-format strip absorbed from prior §09)
§01 Architecture · 4 layers                      →     §01 Status (28-Apr-2026) (NEW · Live/Building/Roadmap 3-col strip)
§02 Phase-1 modules · all completed              →     §02 What's live in production (KEEP+RENAME)
§03 Sub-IPs · 12 modules under Granary           →     §03 Command Centre · in build · the unified front-end (NEW · 6 product screenshots)
§04 Deep cards · the four IPs that move the P&L  →     §04 Phase 1 implementation · Cortex deck (REPURPOSED · was Phase 1 results, but unsourced — see D5)
§05 Verified outcomes · case-study scope         →     §05 In flight · this week (NEW)
§06 Where Granary is live (3 formats)            →     §06 The 13-module vision · built vs full (NEW · honesty table)
§07 Recent Apex engagement Q1 2026               →     §07 Architecture · 4 layers (KEEP+RE-ANCHOR from current §01)
                                                       §08 Sources (NEW · standard pattern · includes research-subpage citation)

Cut from intermediate v0.9.1 (per D7):
  §08 Connected platforms       — RCPL DMS / Fynd Quick / WMS / AutRi / JIIA cards · those IPs live on their own tracks
  §09 Where Granary is live     — folded into hero as a 3-card format strip
  §10 Recent Apex engagement    — register-wide log, not Granary-specific
```

**Diff summary:**

| Action | Section | Notes |
|---|---|---|
| **Keep** | Hero | Refresh numbers (10→11 stores, add Smart Point, add status pill `Live · Phase 1 · 11 stores · SAP integration in test`) |
| **Keep** | Phase 1 results (3 numbers: +3.8pp OSA / −19.5% inventory / −28% shelving) | Move up; restate as "validated outcomes from the 11-store pilot · case study 17-Apr-2026" |
| **Keep** | Where Granary is live (3 formats: RCPL / Smart Bazaar / FreshPik) | Add Smart Point line to Smart Bazaar copy |
| **Keep** | Recent Apex engagement | Append 28-Apr Update + 30-Apr Command Centre Status Report entries |
| **Keep** | Architecture · 4 layers | Move down to §07 (was §01); update copy: Layer 04 = Command Centre (Building), Layer 03 = Cortex agents (Live), Layer 02 = 3D Twin (Roadmap), Layer 01 = Databricks (Live) |
| **Keep but split** | Sub-IPs · 12 modules + Deep cards | Split into §02 (live modules of Granary itself) and §08 (connected platforms — RCPL DMS, Fynd Quick, WMS, AutRi grocery, JIIA — the ones around Granary, not part of it) |
| **Add** | §01 Status today strip | Three columns: Live / Building / Roadmap. The page's spine. Tight summary; drives readers down to detail sections. |
| **Add** | §03 Command Centre · the in-build surface | Lead with what it is (unified front-end consolidating Granary modules · in SIT · daily prod deploys). 33 endpoints live, 5/37 routes wired to live data, 27 in design. Embed 4-5 screenshots tagged Live (real surfaces) or Building (in design). The honesty fulcrum. |
| **Add** | §05 In flight · this week | SAP integration (IRM in test) · ODBC + Databricks (scale-up gate) · DC POC NCR · UAT closure. Each with `Building` pill. The "what to expect to hear next week" beat. |
| **Add** | §06 The 13-module vision · built today vs full | The honesty table from the Status Report. Module · Built today · Status pill. Drops the page into RIL Apex's lap with the same picture they'd get from a candid status reviewer. |
| **Add** | §11 Sources | Apr-28 update + weekly update + Command Centre Status Report + Cortex case study + 17-Apr Cortex pdf. Standard sources block. |
| **Remove** | "Phase-1 modules · all completed 7-Nov-2025" framing as a top-line claim | Replaced by §02 (what's actually running in prod) + §06 (built-vs-vision honest table). The "all completed" claim doesn't survive contact with the 5/37-routes truth. |
| **Renumber** | All section labels (`§01` → `§01 Status today` etc.); update every `<div class="section-label">` heading + matching `<!-- §NN -->` HTML comments | Tax noted in skill §10 |

### §0 Hero — copy refinements

Keep current crumb + section label + author line + version bump. Update H1 unchanged. Refresh subhead and stats:

- H1: **Granary.** (unchanged)
- Subhead 1: keep current "Agentic planning and assortment platform purpose-built for grocery retail…" line; update format names line to mention **Smart Point** alongside Smart Bazaar where Apr-28 Update notes both teams are validating
- Subhead 2: keep "How Fynd transforms Reliance grocery" paragraph; this is the Fynd-built / Reliance-owned framing and remains accurate
- **Status pill**: Add `Live · Phase 1 · 11-store Mumbai pilot · SAP integration in test` immediately under the subhead (new — mirrors hirefirst's status reportage)
- **Stats grid 1** (4 tiles): keep `Forecast scale 48M`, `Stores impacted 3,500+`, refresh OSA `+3.8pp` and `−19.5% inventory` (unchanged numbers; case-study source unchanged)
- **Stats grid 2** (4 tiles): update `Stores in Phase 1 pilot · 11` (new tile) · `Merchandise segments · 10 (Food + HPC)` (new tile) · keep `Sponsors · Farooq · Kushan` · keep `RIL counterparts · Damodar Mall · Saurabh Sharma`
- Move team-roster tiles into §02 "What's live in production" so each module's DRI sits with the module rather than under hero (less crowded hero; better contextual attribution)

### §01 · Status today

Three-column strip. Each column is a tight summary that points down to the detailed section. No padding copy.

| Live | Building | Roadmap |
|---|---|---|
| ML Forecasting on Databricks · 12K SKUs × 4K stores · 48M-row daily refresh · MAPE 41% (from 55%+) | **Command Centre** · 5 of 37 routes wired to live data · 27 in design · daily prod deploys | Straight-Through Processing · 80-90% routine assortment auto-processed |
| Cortex Planning · Assortment Intelligence + MBQ Automation + Range Review · Phase 1 across 11 Mumbai stores · 10 segments (Food + HPC) | **SAP integration** · dev complete across SAP/RDIP/Cortex · IRM whitelisting in test this week | Customer Decision Trees · shelf arrangement from shopper purchase patterns |
| Top 250 SKU availability checklist · auto-derived · live with store ops | **ODBC + Databricks** · pipeline in finalization · gates 3K-4K-store scale-up | Consensus Forecasting · maker-checker · seasonal auto-handling · statistical store clustering |
| Rules Engine · operator-tunable · audit-grade | **DC Demand Forecasting POC** · NCR 100+ stores · vendor ordering | MBQ + planogramming integration · MDQ values |
| Verified outcomes (Apr-17 Cortex case study): +3.8pp OSA · −19.5% inventory · −28% shelving events | **UAT closure** · Smart Bazaar + Smart Point validating Cortex delist recommendations | Fresh FNV shrinkage tracking |

Each pill is colour-coded per existing `pill pill-live` / `pill pill-build` CSS. Add a third class `pill pill-roadmap` if not present (use grey/muted treatment).

### §02 · What's live in production

Module table — 4 columns (Module · Status · DRI · Anchor outcome) — restricted to the things actually running in prod:

| Module | Status | DRI | Anchor outcome |
|---|---|---|---|
| ML Forecasting Engine | `Live` on Databricks | Shahid Kazi | 12K SKUs × 4K stores · 48M rows · MAPE 41% (from 55%+ baseline) |
| Cortex Planning Workbench | `Live` · daily prod deploys | Mayank Jain · Advait Pandit · Aushin Ganguli | End-to-end Assortment + Inventory Planning · 11-store pilot |
| Assortment Intelligence | `Live` | Mayank Jain · Advait Pandit | Range Review · Classification matrix CX/CY/CZ · Margin-vs-Volume quadrants · multi-select delist with reason classification |
| MBQ Automation | `Live` | Aushin Ganguli | Article-level stock targets per store · replaced state-level manual approach |
| Top 250 SKU availability checklist | `Live` | Aushin Ganguli (deployment) | Auto-derived top SKUs · shared with store ops for shelf validation |
| Rules Engine | `Live` | Aushin Ganguli | Operator-tunable · audit-grade |

Note removed from current page: the line "Price & Promotion Intelligence · Live" — verify against Apr-28 sources before keeping. Status report doesn't list it as a built module; current page may be over-claiming. **Decision**: drop from §02 Live; if Granary product team wants it back, re-introduce under §05 In flight or §06 vision table with explicit pill.

### §03 · Command Centre · the in-build surface

The honesty fulcrum. Four-column intro block:

- **What it is** · The unified front-end being built to consolidate Granary's modules — assortment, forecasting, MBQ, dashboards — onto a single platform. Deployed in SIT today; daily prod deploys; exception-driven homepage; priority-ranked queues (P1/P2/P3).
- **What's wired** · 33 backend endpoints live and DB-connected. 5 of 37 frontend routes carry real data today: Home/Dashboard, Category Overview, Range Review, Delist Detail, Requests. Backed by 40 UAT tables; multi-tenant; SSH tunnel + Redis + RBAC.
- **What's in design** · Forecasting UI, Pricing, Fresh, Supply Chain, Store Execution, Calendar, Suppliers, Capital Efficiency, Admin pages — 27 routes scaffolded with mock data, awaiting build per the §06 vision table.
- **Who's building** · Mayank Jain · Advait Pandit · Aushin Ganguli · Shahid Kazi (Cortex) · Granary product team (Command Centre UI)

Below the intro, a 6-card screenshot grid. Each card: image + tight caption + Live/Building pill.

1. **Home · Exceptions + DOH heatmap** (`p-01`) · `Live` · Filter strip (Zone/Format/State/City/Store/Segment/Category/Period) · Exception cards (Zero Sales · Negative Inventory · High DOH · High Markdown) · DOH Distribution Heatmap with per-bucket inventory cost
2. **Range Review · Classification Matrix + Margin-vs-Volume** (`p-11`) · `Live` · CX/CY/CZ revenue bands · Core Stars / Niche Premium / Rationalize / Traffic Drivers quadrants with No-of-SKUs / %-Margin / %-Volume
3. **Category Overview · Drinks** (`p-12`) · `Live` · Sales Trend YoY · Gross Margin Performance · Region-wise Performance · Overstocked + Understocked stores
4. **Delist workflow · multi-select with reason classification** (`p-09`) · `Live` · 9 reason-codes (High inventory holding cost · Product discontinued · Quality/defect · Supplier reliability · End of seasonal lifecycle · Regulatory/compliance · Strategic portfolio optimization · Negative or low profit margin)
5. **Baseline Forecast · article list** (`p-14`) · `Building` · Article-week forecast view across the 11-store pilot — UI live in SIT, full forecasting screens in build
6. **Home · extended dashboard** (`p-15`) · `Live` · Total Sales / Markdown / Margin / Active SKUs / Availability / ROS / DOH metric tiles · Brand Performance top-50

### §04 · Phase 1 results

Three numbers (kept from current page §05). Restate as: *"Validated outcomes from the 11-store Mumbai pilot · 10 merchandise segments (Food + HPC) · Smart Bazaar + Smart Point validating against control. Source: Cortex Granary case study, 17-Apr-2026 (Aushin Ganguli)."*

- `+3.8pp` On-shelf availability (north star: 99%)
- `−19.5%` Inventory value (north star: 20% reduction)
- `−28%` Shelving events (operator workload reduction)

### §05 · In flight · this week

Status strip — 4-5 cards, each with `Building` pill, two-line copy:

- **SAP integration** · Dev complete across SAP, RDIP, and Cortex. IRM raised for IP whitelisting; testing expected to close this week. Will complete the end-to-end Assortment Listing/Delisting flow Cortex → SAP via RDIP.
- **ODBC + Databricks connectivity** · Pipeline in finalization. The explicit gate to scaling beyond 11 pilot stores to 3,000–4,000-store rollout with real-time data refresh.
- **DC Demand Forecasting POC** · NCR region · 100+ stores · vendor ordering use case. Fresh and dairy forecasting integrated and running on database.
- **UAT closure · Smart Bazaar + Smart Point** · Format and Category teams validating Cortex-generated delist recommendations against current manual decisions. Driving toward sign-off.
- **Top 300/1000 SKU availability** · Expanding Top-250 checklist with automated OOS reason classification, photo evidence, and auto-triggered replenishment.

### §06 · The 13-module vision · built today vs full

The Status-Report table, Apex-flavoured. Adds the honesty contract:

| Module | Built today | Status |
|---|---|---|
| 1. Command Centre | Dashboard + morning briefing · Exception cards · DOH heatmap | `Building` · ~30% |
| 2. Store Intelligence | — | `Roadmap` · ~3 weeks |
| 3. Assortment Planning | Range Review · Classification matrix · Margin-vs-Volume quadrants · Delist workflow | `Building` · ~40% |
| 4. Demand Forecasting (UI) | Baseline Forecast view (engine in production) | `Building` · UI ~0% · engine `Live` |
| 5. Inventory Management | DOH + risk APIs | `Building` · ~25% |
| 6. Supplier Management | — | `Roadmap` · ~2 weeks |
| 7. Pricing Intelligence | — | `Roadmap` · ~3 weeks |
| 8. Fresh Command | — | `Roadmap` · ~2 weeks |
| 9. Supply Chain Ops | — | `Roadmap` · ~3 weeks |
| 10. Store Execution | — | `Roadmap` · ~2 weeks |
| 11. Calendar | — | `Roadmap` · part of ~4-week bundle |
| 12. Capital Efficiency | Some inventory metrics | `Building` · ~10% |
| 13. Admin | Mock UI pages | `Building` · ~5% |

Closing line: *"~15-20% of full vision built today; foundation production-grade (multi-tenant backend, 40 UAT tables, daily prod deploys). Roadmap durations are engineering estimates from the 30-Apr Command Centre Status Report."*

### §07 · Architecture · 4 layers

Keep existing 4-layer block; tighten copy and tag each layer:

- Layer 04 · Experience → **Command Centre · operator surface** — `Building`
- Layer 03 · Agentic → **Cortex agents** — Assortment Intelligence · Forecasting · Rules Engine · Replenishment — `Live`
- Layer 02 · 3D Twin → Digital store mirror · planogram · capacity · expiry — `Roadmap`
- Layer 01 · Data / ML → **Databricks-native** · sales · inventory · supplier · loyalty · POS feeds · ML pipelines — `Live`

### §08 · Connected platforms

The IPs that surround Granary but aren't part of it (split out from current §03 Sub-IPs + §04 Deep cards). 4-5 cards:

- **RCPL FMCG DMS** · `Live` · 1.3 Cr outlet target by 2028 · Fynd-built DMS replacing legacy distributor stack · DRI Aushin Ganguli · Damodar Mall (RIL)
- **Fynd Quick · Q-Commerce OS** · `Live` · 700+ orders/min · 90% on-time · sub-30-min · powering JioMart Quick · DRI Pratik Patel · Jainish Jain
- **WMS** · `Live` · 99.7% pick accuracy · powers JioMart at 1M+ orders/day at peak · DRI Pratik Patel
- **AutRi · Onshelf grocery** · `Building` · FreshPik Powai pilot · 95%+ shelf compliance · Phase 2 with Fynd Nucleus · DRI Salman Saudagar (scope) · Saaket Chawali
- **JIIA · Agentic Shopping** · `Building` · Google Cloud Next '26 keynote · 40M+ image catalog · DRI Shyam Dixit

These are **adjacent**, not Granary modules. Keeping them together in their own section avoids the current page's ontological mix-up of Granary modules with surrounding platforms.

Drop from current 12-card sub-IP grid: "Vendor Onboarding (JCP)", "Smart Bazaar Companion / FreshPik / 7-Eleven", "Cheruvatur · Wadera · Jain deep models". Reason: Vendor Onboarding belongs on `/jcp`; Companion belongs on `/jcp` or its own page; Cheruvatur/Wadera/Jain deep models belong inside §02 ML Forecasting if at all (or §05 In flight if active research). Granary product team to decide before drafting.

### §09 · Where Granary is live (3 formats)

Keep current §06 verbatim but expand Smart Bazaar copy to mention **Smart Point** validation per Apr-28 Update.

### §10 · Recent Apex engagement

Keep current §07 entries (Project MAGA, FreshPik NextGen, RRFB inventory, Apex Review · Grocery). Append:

- **28-Apr-2026** · **Granary Phase-1 leadership update.** *Update from Mayank Jain · Aushin Ganguli to leadership: 11 pilot stores live · Smart Bazaar + Smart Point validating · SAP integration dev complete (IRM whitelisting in test) · ODBC pipeline finalisation gates 3K-4K-store scale-up · DC POC NCR 100+ stores · Top 250 checklist deployed.*
- **30-Apr-2026** · **Command Centre status review.** *33 backend endpoints live · 5/37 frontend routes wired to live data · 13-module vision ~15-20% built · roadmap with engineering estimates per module.*

### §11 · Sources

Standard sources block (mirrors `/hirefirst` §13 pattern):

- **Granary Phase-1 leadership update** · 28-Apr-2026 · `Granary_Update_Apr28.md`
- **Granary weekly update** · 28-Apr-2026 · `Granary_Weekly_Update_Apr28.md`
- **Command Centre status report** · 30-Apr-2026 · `Granary Command Centre Current State.txt`
- **Cortex Granary case study** · 17-Apr-2026 · Aushin Ganguli · `Granary Cortex _ Assortment & Forecasting.pdf` (link to Drive if available)
- **Cortex for Granary · Assortment + Inventory Optimization System V3** · 1-Feb-2026 · `Cortex for Granary — Assortment Planning and Inventory Optimization System V3.pdf`

---

## 4. Asset pipeline

**Source:** `docs/Granary project documents dump/Screenshots.pdf` (24 pages, 7MB, 1914×928 pts each)

**Extract & resize** (already prototyped at 60dpi for preview into `tools/scratch/granary-preview/`; final at 100dpi web-quality):

```bash
mkdir -p assets/granary/command-centre
pdftoppm -r 100 -jpeg -jpegopt quality=78 \
  -f 1 -l 1   "docs/Granary project documents dump/Screenshots.pdf" \
  assets/granary/command-centre/01-home-exceptions
pdftoppm -r 100 -jpeg -jpegopt quality=78 \
  -f 11 -l 11 "docs/Granary project documents dump/Screenshots.pdf" \
  assets/granary/command-centre/02-range-review-classification
pdftoppm -r 100 -jpeg -jpegopt quality=78 \
  -f 12 -l 12 "docs/Granary project documents dump/Screenshots.pdf" \
  assets/granary/command-centre/03-category-overview-drinks
pdftoppm -r 100 -jpeg -jpegopt quality=78 \
  -f 9  -l 9  "docs/Granary project documents dump/Screenshots.pdf" \
  assets/granary/command-centre/04-delist-reason-modal
pdftoppm -r 100 -jpeg -jpegopt quality=78 \
  -f 14 -l 14 "docs/Granary project documents dump/Screenshots.pdf" \
  assets/granary/command-centre/05-baseline-forecast
pdftoppm -r 100 -jpeg -jpegopt quality=78 \
  -f 15 -l 15 "docs/Granary project documents dump/Screenshots.pdf" \
  assets/granary/command-centre/06-home-extended-dashboard
# pdftoppm appends `-1.jpg` or `-01.jpg` depending on version; rename to descriptor.jpg
for f in assets/granary/command-centre/*-1.jpg assets/granary/command-centre/*-01.jpg; do
  [ -f "$f" ] && mv "$f" "${f%-*}.jpg"
done
# resize cap to 1600px wide
for f in assets/granary/command-centre/*.jpg; do
  sips -Z 1600 -s format jpeg -s formatOptions 80 "$f" --out "$f"
done
```

**No GCS mirror needed** — 6 images at ~150-250KB each = <2MB total · stays in git.

**No raw PDF hosting** — 7MB Screenshots.pdf is internal source material; not for public link. The Cortex case study PDF (~2.5MB) could be hosted under `assets/granary/granary-cortex-assortment-forecasting.pdf` if the user wants a downloadable Evidence link in §02 — defer until asked.

---

## 5. Navigation wiring

Granary already exists in the Tracks mega-menu (`Platforms` column → `Granary` with `Grocery AI` mono-suffix). No new route, no new entry.

**To check:**
- `index.html` (home page) · is there a Granary card with stats? Quick grep before drafting; refresh if stats are stale (10→11 stores etc.)
- `catalog/index.html` · ditto

No other nav file edits expected.

---

## 6. Build / verify

Single hand-edited file: `granary/index.html`. No renderer needed (content is bespoke per-section, low repetition; matches the hirefirst pattern).

```bash
python3 -m http.server 8000
# open http://localhost:8000/granary
# In DevTools console once: sessionStorage.setItem('fyndrrl_auth_v1','1'); location.reload();
```

Use Chrome DevTools MCP for the screenshot pass — `new_page → evaluate_script` (auth bypass) → `take_screenshot` (full page) → `list_console_messages` for errors.

**Verify checklist** (per skill §9):
- [ ] Hero status pill renders correctly
- [ ] All 6 Command Centre screenshots load (no broken-image icons)
- [ ] Section labels are a contiguous run §01 → §11 (`grep -n 'section-label mb-3">[0-9]' granary/index.html`)
- [ ] Mobile viewport renders at 375px (§01 strip + §06 vision table both responsive)
- [ ] Every URL/domain in copy is wrapped in `<a href target="_blank" rel="noopener">`
- [ ] Numbers traceable to source folder (11 stores → Apr-28 Update; 5/37 routes → Status Report; +3.8pp/-19.5%/-28% → Apr-17 Cortex case study)
- [ ] Names spelled correctly (Mayank Jain · Advait Pandit · Aushin Ganguli · Shahid Kazi · Damodar Mall · Saurabh Sharma · Karan Muley · Vincent Braganza)
- [ ] Dates in `DD-MMM-YYYY`
- [ ] No marketing voice; no "world-class", "industry-leading", etc.

---

## 7. Phased delivery

| Phase | Scope | Hours | Commit |
|---|---|---|---|
| P1 | Spec (this file) + asset extraction (6 screenshots into `assets/granary/command-centre/`) | 0.5 | 1 commit · `granary · spec + screenshot assets · Apr-28 update + Command Centre evidence` |
| P2 | Hand-edit `granary/index.html` per §3 diff; stages §0 hero + §01 strip + §02 live + §03 Command Centre + §04 results | 1.5 | 1 commit · `granary · v0.9.0 restructure · Apr-28 truth + Command Centre honesty pill (top half)` |
| P3 | Stages §05 in-flight + §06 vision table + §07 architecture + §08 connected + §09 formats + §10 Apex log + §11 sources; renumber sweep; section-label contiguity check | 1.5 | 1 commit · `granary · v0.9.0 restructure · vision table + connected platforms + sources (bottom half)` |
| P4 | Verify locally with Chrome DevTools MCP; spot-fix copy register against `website-tone-of-voice` checklist; update home-page card stats if needed | 0.5 | 1 commit · `granary · verify pass · home card refresh` |

Total: ~4 hours; 4 commits.

---

## 8. Decisions

Locked via AskUserQuestion (1-May-2026):

- **D1 · Update depth.** Full restructure of the Live/in-prod content per the latest material. The Command Centre is the in-build next-gen surface and lives under Building, not as its own Live section. (Mid-restructure path declined — full was the call.)
  - **Why:** the page was reading bullish vs the actual 28-Apr status; Apex-grade audience needs honest. **How to apply:** §03 introduces Command Centre as Building; §06 makes the gap explicit with the 13-module table.
- **D2 · Honesty register.** Hirefirst-style pills (`Live` · `Building` · `Roadmap`). Every borrowed claim gets a pill.
  - **Why:** RIL Apex compares notes; the Status Report's 5/37-routes line is in the room — we can't undertell our problems but also can't overclaim live state. **How to apply:** every module/feature mentioned carries a pill; never mix tiers in a sentence without tagging.
- **D3 · Screenshots.** Yes, embed 4-6 real Command Centre screenshots from `Screenshots.pdf`. Skip the Jira-internal screenshot (p.3) and the older lighter-header Rules/Assortment-Projects screens (p.17, p.18-24) which are mockup or legacy UI.
  - **Why:** the page needs visual evidence that real product exists, not just claims about a tool — countering any read that "everything is in build". **How to apply:** §03 carries 6 screenshots, each with Live/Building pill matching the Status Report's truth.
- **D4 · Price & Promotion Intelligence.** Drop from the page. The current §02 module table loses this row; the §03 sub-IP card it carried in the prior layout is gone.
  - **Why:** Status Report doesn't list it as built; 28-Apr update is silent; no citable source for the Live claim. Re-introduce only when Granary product team can name a deployment + source.
  - **How to apply:** strip the row from §02 and any pill mention elsewhere. Don't replace with a Building/Roadmap row either — silence is more honest than a placeholder.
- **D5 · Cortex case-study PDF · GCS hosting + inline viewing.** Upload `Granary Cortex _ Assortment & Forecasting.pdf` (~2.5MB) to `gs://impetus-socialpilot/rrl-portfolio/assets/granary/`. Reference at `https://socialassets.impetusz0.de/rrl-portfolio/assets/granary/granary-cortex-assortment-forecasting.pdf`. Embed inline-viewable on the page (likely a thumbnail + open-in-new-tab card under §04 Phase 1 results, with the PDF rendered in an `<embed>` or `<iframe>` for inline reading).
  - **Why:** the +3.8pp / −19.5% / −28% numbers are the page's headline outcomes — viewers should be able to read the source without leaving the page. GCS hosting is durable beyond Drive permission churn.
  - **How to apply:** add to Stage 3 asset pipeline (gsutil cp + curl 200-check); add an inline embed block in §04. Drive link still kept as a backup chip.
- **D6 · Sub-IP cuts.** Drop all three of "Vendor Onboarding (JCP)", "Smart Bazaar Companion / FreshPik / 7-Eleven", and "Cheruvatur · Wadera · Jain deep models" from the Granary page.
  - **Why:** none fit cleanly as Granary modules or Connected platforms. Vendor Onboarding lives on `/jcp`. Companion belongs on `/jcp` or its own page. Deep-learning research extensions are not load-bearing without their own surface.
  - **How to apply:** none are present in §02 or §08 of the new structure. If anyone asks where they went, redirect: Vendor Onboarding → `/jcp`, Companion → `/jcp` (or a future page), deep models → bring back as a §05 In flight line *only* if 16-loc validation produces citable results.
- **D7 · Trim from 11 sections to 8 (v0.9.1 → v0.9.2).** Cut §08 Connected platforms, §10 Recent Apex engagement; fold §09 Where Granary is live into the hero as a 3-card format strip. Renumber §11 Sources → §08.
  - **Why:** §08 Connected platforms duplicated content already covered on its own tracks (`/rcpl`, `/jcp`, `/autri`, `/jcp#jiia`) — the cards on /granary added no information beyond a link, and the user prefers the page stay focused on what *Granary* is rather than what surrounds it. §10 Recent Apex engagement is a register-wide log pattern; the page itself is the artefact Apex is reading, not a re-list of when it has been seen. §09 was a 3-card strip already short enough to live in the hero, where it complements the status-pill block — and removing it as a standalone section saves a scroll without losing the format-coverage signal.
  - **How to apply:** the 3-format cards moved into the hero below the second stat-tile row; ensure RCPL / Smart Bazaar + Smart Point / FreshPik retain the same copy. Cross-page consistency is unaffected because nothing on a sibling page links to `/granary#08`, `/granary#09`, or `/granary#10` anchors.
- **D8 · Merge §04 Command Centre into §02 (v0.9.3 → v0.9.4).** Folded the §04 Command Centre deep-dive (4-card intro + 6-screenshot grid) into §02 What is live as a sub-block below the module table. Deleted the 4-card intro entirely (its content duplicated info already on the module table, §03 Layer 04, and §05 vision table). Renumbered §05 In flight → §04, §06 Vision → §05, §07 Research → §06, §08 Sources → §07. **Canonical-ordering override** — the default convention (Status → What's live → Architecture → Deep dive → In flight → …) puts deep-dive at §04. We override here because the §02 module table and the §04 deep-dive cover the same beat ("what's live"); two adjacent sections about the same thing read as redundant on a page this size.
  - **Why:** user feedback — "Merge this section (What operators see) under Modules in Production. Don't have two sections about the same thing."
  - **How to apply:** §02 now has module table + screenshot grid in one section. The reviewer skill's canonical-ordering rubric should treat this as a *documented* override (this D8 entry is the documentation).
- **D9 · Drop "production" from user-facing copy (v0.9.3 → v0.9.4).** "Production", "prod deploys", "production-grade" are engineering shorthand that reads as opaque to Apex. Replaced across the page with `live`, `running today`, `daily updates`, `battle-tested`. Section labels: "What's live in production" → "What is live"; "13-module vision · built today vs full" already clean. Hero caption: "Phase 1 · in production" → "Phase 1 · live". §05 vision intro: "production-grade with daily prod deploys" → "live with daily updates".
  - **Why:** user feedback — "Production is a technical term." Mirrors the broader exec-readability rule already in `website-tone-of-voice.md` §7 jargon translation table; D9 codifies "production" as part of that rule.
  - **How to apply:** added to `website-tone-of-voice.md` §7 jargon table (production → live / running / daily updates / battle-tested) and to `website-page-reviewer` audit-framework §4 jargon failure pattern. Future pages should pre-empt the substitution; existing pages caught by the audit's jargon check.

---

## 9. Out of scope

- **Cortex case study PDF hosting** — defer; current page already links to Drive; only host locally if user asks.
- **Connected-platforms deep links** — keep `/rcpl`, `/jcp`, `/jcp#jiia` anchors as today; don't expand into deeper module pages from this page.
- **Sub-IP grid restoration** — current page lists 12 sub-IPs; restructure cuts to 6 live + 5 connected. If the cut "Cheruvatur · Wadera · Jain deep models" or "Smart Bazaar Companion" are load-bearing for some other audience, they belong on their own pages, not back on `/granary`.
- **Forecasting research paper page** (`/granary/research/transforming-retail-forecasting`) — no changes; sub-page is independently maintained.
- **Renderer for `/granary`** — single-page section, bespoke content per block; no Python build script. If the page grows past 12 sections or starts repeating structures, revisit.

---

## 10. Footer

**DRI (Fynd-side):** Salman Saudagar (COO, Fynd).
**RIL counterparts named on the page:** Damodar Mall · Saurabh Sharma.
**Spec author:** Kushan Shah · 1-May-2026.
