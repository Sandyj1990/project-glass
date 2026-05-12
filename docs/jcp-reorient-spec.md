# JCP Overview · Reorient Spec

**Status:** v0.7 · 2026-05-01 · **shipped** (4 commits + 4 feedback rounds, see §11)
**Owner:** Kushan Shah
**Routes:** `/jcp/` (existing — reorient) + `/jcp/release-notes/` (NEW subpage)
**Source content:** `docs/accenture-2026-04-16-compilation/` · `docs/jcp-notes-compilation/JCP Raw Release notes 2025-26.pdf`
**Supersedes:** `docs/jcp-update-spec.md` (v0.4 · committed `a47729e`)
**Inherits from:** `docs/website-orientation-spec.md` · register copy via `website-tone-of-voice` skill · canonical section ordering via `website-section-authoring` skill §4

---

## 1. Why this page exists

**Audience.** RIL Apex (MM Sir level) reviewing the register at `reliance-retail-fynd.vercel.app/jcp/`.

**Gap to close.** The current `/jcp/` page (v0.4, shipped 30-Apr-2026) duplicates surface-level material that lives better on its own pages, and ends with a closer ("Why this stack wins") that re-states stats already in the hero. Two specific symptoms:
- **Snapshot duplication.** B2C Snapshot (4 brand cards) and B2B Snapshot (4 cards) compress thin per-channel copy that the `/jcp/channels/` gallery already covers in full and at depth.
- **No durable evidence of what JCP shipped this year.** The page tells the reader JCP is at scale (700K orders/day, 79 channels, 200M+ customers) but never shows *what was built underneath that number in FY25-26*. There is a 45-page release-notes PDF in the repo that nobody can see.

**Why this belongs in the apex register.** The deeper question Apex asks of any platform is "what got shipped in the last year that justifies the headcount." The hero answers scale; the new Release Notes section answers shipped capability. Together they form the scale × throughput case for JCP without a separate slide deck.

**User asks (verbatim, 2026-05-01):**
1. Add latest Accenture deck context — already in (hero stats + Ecosystem cards + Cataloging callout all cite slides 19/35)
2. Remove "B2C Snapshot" section
3. Remove "B2B Snapshot" section
4. Keep "Why JCP scales the way it does." (Ecosystem · 9 cards · slide 35)
5. Remove the source line ("Source · Accenture · Updated Retail Platforms+Agents · Apr-16-2026 · slide 35")
6. Make AI Cataloging description consistent with `/jcp/cataloging/`
7. Remove "AJIO × JCP migration · Apex deadline met"
8. Remove "Ecosystem & differentiation" closer
9. Add "JCP Platform Release Notes" section sourced from `JCP Raw Release notes 2025-26.pdf`, organised as a changelog

---

## 2. Source inventory

| Source | Type | Path | Key facts |
|---|---|---|---|
| Accenture deck slide 31 | pptx slide | `docs/accenture-2026-04-16-compilation/slide_31/` | Channel coverage chart (79 channels, vertical breakdown) — already used in hero |
| Accenture deck slide 35 | pptx slide | `docs/accenture-2026-04-16-compilation/slide_35/` | "Ecosystem" — 9 capability cards + scale stats (700K/day, 50K/min peak, 200M+ customers, 30K+ stores) — already used |
| Accenture deck slide 19 | pptx slide | `docs/accenture-2026-04-16-compilation/slide_19/` | AI cataloging headline (15 days → 5 hours) — already cited in CTA card; full deep-dive lives at `/jcp/cataloging/` |
| Vertex Search internal note | PDF/internal | (already in page · 18-Dec-2025) | 90M+ production searches across 5 channels · +7.4–10.7% revenue uplift vs Algolia — keep as-is |
| **JCP Release Notes** | PDF · 45pp · 11.6 MB | `docs/jcp-notes-compilation/JCP Raw Release notes 2025-26.pdf` | FY25-26 shipped capability across ~19 sub-systems · ~150 line items · screenshots of admin UIs |
| `/jcp/cataloging/` page | live HTML | `jcp/cataloging/index.html` | Authoritative copy for the `/jcp/` AI Cataloging callout — see §3.6 below |

**Aggregate KPIs already on /jcp/ (kept):**
- 700K+ orders/day · 50K+ orders/min peak · 200M+ customers FY26 · 30K+ stores
- 79 channels (68 live · 5 in-progress · 6 planned) · 105 B2C · 7 B2B · 10 verticals
- Vertex Search · 5 channels live · 90M+ production searches · +7.4–10.7% revenue uplift

**New aggregate KPIs derivable from Release Notes PDF:**
- 19 capability areas with FY25-26 releases (Payments, OMS, Search, Catalog, Pricing, Inventory, Coupons, Cart & Checkout, CMS/Theme, Logistics, Serviceability, Auth, Comms, Integrations, etc.)
- ~150 individual capability line items
- Notable scale lifts: Algolia → Vertex 100% migration (zero downtime) · Vue → React platform UI migration · UCP integration shipped · Kafka layer for hyperlocal scale

---

## 3. Page structure (target)

**Sequencing follows the canonical section ordering** in `website-section-authoring` skill §4 (the same ordering `/hirefirst/` and `/granary/` use): §0 Hero → §01 What X is for Reliance → §02 What's live → §03 Architecture (skip) → §04 Deep dive → §05 In flight (skip) → §06 Vision (skip) → §07 Research (skip) → §08 Sources.

Per **D5 (resolved)** the Release Notes content is too dense for inline; it ships as a dedicated subpage `/jcp/release-notes/`. On `/jcp/` it's represented by a CTA card paired with the AI Cataloging CTA — the same "deep-dive launcher" pattern.

### `/jcp/` page (reorient)

```
§0   Hero                                     (KEEP, strip all deck/slide refs)
§01  What JCP is for Reliance                 (= current Ecosystem · 9 cards) (KEEP, strip all deck/slide refs)
§02  What's live · two CTAs                   (NEW · 2-card grid — Release Notes + AI Cataloging deep-dive launchers)
§04  Deep dive · Search · Vertex production uplift   (= current Vertex Search section) (KEEP, strip the "Vertex Search · Proven Performance Uplift" source callout per D6)
Footer
```

Per **D6 (resolved)** there is no §08 Sources block on `/jcp/`. All provenance lives in git. (The `/jcp/release-notes/` subpage retains its own §08 because that page has a single source artefact worth naming.)

### `/jcp/release-notes/` page (NEW subpage)

```
§0   Hero                                     (Eyebrow + H1 "JCP · Release Notes" + subhead with grand total + 4 stat tiles)
§01  What's in this page                      (10 jump-link cards · area name · ~N items · maps to §02 below)
§02  What shipped this year                   (NEW · 10 accordion sections · ~150 verbatim line items · per D2/D3)
§08  Sources                                  (single notes line citing the JCP Release Notes PDF)
Footer
```

**Skipped canonical sections (documented per skill §4 override pattern):**
- **§03 Architecture** — JCP's architecture (microservices, Kafka layer, etc.) is described in capability terms inside §01 Ecosystem cards; a separate diagram doesn't add information at apex level. Defer until/unless we author an architecture-only deep-dive page.
- **§05 In flight** — JCP doesn't currently maintain a public "shipping next 1-4 weeks" list at apex grain. Release notes (§02) is the closest equivalent and looks backward. Add §05 in a future spec if a credible in-flight list emerges.
- **§06 Vision / Roadmap scorecard** — vision claims for JCP would be Reliance Retail strategy, not platform-team scope. Out of register.
- **§07 Research** — no research artefact for `/jcp/`. The deep-dive lives at `/jcp/cataloging/` instead.

REMOVED from current page: B2C Snapshot · B2B Snapshot · AJIO × JCP migration · "Ecosystem & differentiation" closer.

### §0 · Hero (KEEP — minor edit)
*(canonical §0)*
- All four FY26 stat tiles stay (700K · 50K · 200M+ · 30K+)
- All four channel-coverage tiles stay (79 · 105 · 7 · 10)
- Three people tiles stay (CPO · Eng leads · RIL counterparts)
- **Edit (D6):** the eyebrow `cap-num` above the stat strip currently says `FY 2025-26 · Accenture · 16-Apr-2026 · slide 35` → strip to `FY 2025-26`.
- **Edit (D6):** the `cap-num` above channel coverage currently says `Channel coverage · slide 31 + Channel Coverage PDF (Feb-2026)` → strip to `Channel coverage`.

### §01 · What JCP is for Reliance — "Why JCP scales the way it does." (KEEP — strip all source refs)
*(canonical §01 · current Ecosystem · 9 cards)*
- All 9 cards verbatim
- **Edit (D6):** Drop the trailing `<p class="text-xs">Source · Accenture · Updated Retail Platforms+Agents · Apr-16-2026 · slide 35</p>` line.
- **Edit (D6):** Strip the section eyebrow → from `Ecosystem · scale of retail transformation · FY 2025-26` (the current line — note: there's no slide-35 ref in this eyebrow today, just `FY 2025-26` which stays). Subhead currently reads "Nine capability claims from the Accenture deck (16-Apr-2026 · slide 35) — verbatim. The properties that let one stack carry 700K+ orders a day across 79 channels." Strip to: "The properties that let one stack carry 700K+ orders a day across 79 channels."

### §02 · What's live · two CTAs (NEW · replaces inline Cataloging callout)
*(canonical §02 · two-card grid · CTAs out to deep-dive subpages)*

Two `card-hover` deep-dive launchers in a `grid md:grid-cols-2 gap-4` block. Each card:

**Card A · Release Notes**
- Eyebrow: `What's live · FY 2025-26`
- H3: `What shipped on JCP this year.`
- Body: Roughly 150 capability releases across 10 sub-systems — payments, OMS, search, catalog, pricing, inventory, coupons, cart, logistics, identity. Sourced from internal JCP product release notes.
- Mono line: `~150 items · 10 areas · FY 2025-26`
- CTA: `Open Release Notes →` → `/jcp/release-notes/`

**Card B · AI Cataloging** *(rewrite per §3.4 below)*
- Eyebrow: `Deep dive · Tira × Akind · live`
- H3: `From days of manual work to ~14 seconds per SKU.`
- Body: Same Web Grounding pipeline measured at Netmeds (~5 days → ~2 minutes per 1,000 SKUs) and Reliance Digital (35-40% faster · 75% first-pass auto-fill), now live in production for the Akind brand inside Tira with Google. **Accuracy 89% · 332/382 attributes filled · ~14 sec per SKU.**
- CTA: `Open AI Cataloging deep-dive →` → `/jcp/cataloging/`

### §04 · Deep dive · Search · Vertex production uplift (KEEP — strip source callout per D6)
*(canonical §04 · current Vertex Search section · stays as the only inline deep dive on /jcp/)*

- All numbers in the table stay (Tira/Netmeds metrics, channel-live count, ROI band)
- **Edit (D6):** the subhead currently ends with: `Lead: Vidit Kumar Gupta. Source: "Vertex Search · Proven Performance Uplift" · 18 - Dec - 2025 · Internal.` → strip the `Source: "Vertex Search…"` portion. Lead name stays (per tone-of-voice §1.5 names where they matter).
- No changes — section already passes the apex bar (numbers up front, source named, lead named).

### §3.4 · AI Cataloging copy rewrite (used inside §02 Card B above)
- **Current copy** (jcp/index.html:182-184):
  > "From manual enrichment to ~14 seconds per brand. Latest Accenture deck (16-Apr-2026 · slide 19) reports **15 days → 5 hours** for full AI Photoshoot + cataloguing pipeline. Deep-dive page covers the architecture, model library, and per-brand outcomes."
- **Issue:** the `~14 seconds` headline is the Tira × Akind production result (`/jcp/cataloging/` §02), but the body line then anchors on Accenture's `15 days → 5 hours` figure. Two different units, two different references — confusing.
- **Rewrite shown in §02 Card B above.** All numbers in the rewrite (~14 sec, 89% accuracy, 332/382 attributes, Netmeds 5d→2m, Reliance Digital 35-40%) appear verbatim on `jcp/cataloging/index.html` (§01 + §02). The Accenture `15 days → 5 hours` framing moves *out* of the /jcp/ summary card and stays only on `/jcp/cataloging/` where it has full context.

### `/jcp/release-notes/` subpage detail (NEW)

**Hero (§0)**
- Crumb: `Home / JCP / Release Notes`
- Subnav chips (same set as other JCP subpages — see §6)
- Section label: `JCP · Release Notes · FY 2025-26`
- H1: `Release Notes.`
- Subhead: `What shipped on JCP across FY25-26 — ~150 capability releases across 10 sub-systems. Source: internal JCP product release notes.`
- 4 stat tiles:
  - `Items shipped` · `~150` · `FY25-26`
  - `Capability areas` · `10` · `Search · Catalog · Pricing · Inventory · Coupons · Cart · OMS · Logistics · Payments · Platform`
  - `Channels touched` · `79` · `every JCP-served brand`
  - `Source` · `Internal` · `JCP product release notes`

**§01 · What's in this page (10 jump-link cards)**
- 3-column card grid · each card: cap-num index `01`–`10` · area name · 1-line lede · `~N items` mono line · `<a href="#area-NN">Jump →</a>`
- Anchors map 1:1 to §02 accordion sections below

**§02 · What shipped this year (10 accordion sections · per D2/D3)**

Visual: native `<details>` + `<summary>` (CSS-only · no JS · matches the rest of the register). Each accordion:

```html
<details class="card p-0" id="area-NN">
  <summary class="p-6 cursor-pointer flex items-center justify-between">
    <div>
      <div class="cap-num mb-1">NN</div>
      <h3 class="font-semibold text-lg">{Area name}</h3>
    </div>
    <span class="cap-num">~N items · click to expand</span>
  </summary>
  <div class="px-6 pb-6">
    <ul class="findings-list">
      <li>{verbatim line item from PDF}</li>
      ... ~10-25 items per area ...
    </ul>
  </div>
</details>
```

Default-collapsed. The grand total (~150) and the per-area count are visible without expanding.

**Grouping** — 19 raw PDF sub-systems compressed to **10 capability areas** (mapping unchanged from prior draft):

| # | Capability area | Sub-systems folded in (from PDF) | Sample bullets (illustrative — full list extracted at build time) |
|---|---|---|---|
| 01 | **Search & Discovery** | Common Extensions / Search · Vertex extensions · ViSenze · Osmos | Algolia → Vertex 100% migration · zero downtime · Vertex Phoenix integration · ViSenze image search · Osmos catalog sync · Vertex collection support · A/B testing framework |
| 02 | **Catalog** | Catalog · Catalog Import-Export · Bulk Extension · FDK Store | Secondary Categories · Variants Logic Revamp · Boolean & Multi-Value Attributes · Brand Slug · Template Hierarchy · App-Product Webhooks v2 · Wishlist Server · Coupon-based Collections |
| 03 | **Pricing** | Pricing | Discount v2 · Maker-Checker · Discount-Level Threshold · Document Encryption · Price & Inventory Split · Early Access Pricing · Tax Precision · Price Override · Seller Identifier Search |
| 04 | **Inventory** | Inventory | Bulk Quantity Update · Inventory Aging · Price Zone-Based Visibility · Sellable Quantity logic |
| 05 | **Coupons & Promotions** | Coupon & Promotion Capabilities | Nth-order coupons · frequency limits · group-level limits · incompatibility checks · MRP/ESP application · level-based cohort · multi-slot · geo-based offers |
| 06 | **Cart & Checkout** | Cart & Checkout | Cart function · Fraud Engine · Subscription Engine · Cart-level GWP · Stackability · Fraud control |
| 07 | **OMS & Order Lifecycle** | OMS · Integrations (Ajio Herald, Return Promise, Fraud) | Cancellation fees · Replacement/Exchange · Real-time order ringer · Quick commerce · Rectron reconciliation · Multi-Promise for Tira · Ajio Herald Order Orchestrator · Return Promise Engine |
| 08 | **Logistics & Serviceability** | Logistics · Serviceability (Fulfilment, Routing, Promise, Coverage, Quick Commerce, Misc) | Hyperlocal carriers (Grab, Shadowfax, Shipsy) · DTDC · Shipyaari · Blitz · Sequel · Clickpost · Kafka layer for scale · Multi-mode fulfillment · Polygon serviceability · Dynamic Promise per mode · International serviceability · Quick commerce for JioMart |
| 09 | **Payments** | Payments · Qwikcilver | CVV-less · BNPL · EDC mapping · COD payouts · payment routing · Ajio Wallets · UPI QR · multi-MOP · Qwikcilver StoreOS binding |
| 10 | **Platform · Identity · Theme · Comms** | Platform Authentication · Theme/SEO/CMS · Communications · Haptik · Seller Central VMS · Shipsy WMS/TMS | Mobile Number Update · Truecaller login · Email Verification · UCP Integration · JWT · PII Encryption · Page Mapper · CMS Maker-Checker · Global Sections · Personalization · Page Archival · Multi-Scheduler · Vue → React platform UI migration · JioCX integration · Pointblank SMS · Haptik dual React/Vue |

**Per D3 (Exhaustive · ~150 verbatim items):** every line item from the 45-page PDF goes into the appropriate accordion verbatim (single-line compressed). Item-extraction happens during build (one-time author pass; not a renderer that re-parses the PDF on every build).

**§08 · Sources line**
- One-line cap-num: `Source · "JCP Raw Release Notes 2025-26" · internal · maintained by JCP product + engineering · 45-page PDF on file at docs/jcp-notes-compilation/`

Source: `docs/jcp-notes-compilation/JCP Raw Release notes 2025-26.pdf` (45 pages · ~150 line items · screenshots of admin UIs).

**Section eyebrow:** `Release Notes · FY 2025-26 · platform changelog`
**H2:** What shipped on JCP this year.
**Subhead:** A catalogue of capabilities released across the platform in FY25-26 — grouped by sub-system. Source: internal release notes maintained by JCP product + engineering.

**Grouping strategy** — the 19 raw sub-systems in the PDF compress to **10 capability areas** for the apex register. Each area gets a card; each card has a short headline and 3-6 bullet items pulled verbatim from the PDF (compressed to single-line).

| # | Capability area | Sub-systems folded in (from PDF) | Sample bullets |
|---|---|---|---|
| 01 | **Search & Discovery** | Common Extensions / Search · Vertex extensions · ViSenze · Osmos | Algolia → Vertex 100% migration · zero downtime · Vertex Phoenix integration · ViSenze image search · Osmos catalog sync · Vertex collection support · A/B testing framework |
| 02 | **Catalog** | Catalog · Catalog Import-Export · Bulk Extension · FDK Store | Secondary Categories · Variants Logic Revamp · Boolean & Multi-Value Attributes · Brand Slug · Template Hierarchy · App-Product Webhooks v2 · Wishlist Server · Coupon-based Collections |
| 03 | **Pricing** | Pricing | Discount v2 · Maker-Checker · Discount-Level Threshold · Document Encryption · Price & Inventory Split · Early Access Pricing · Tax Precision · Price Override · Seller Identifier Search |
| 04 | **Inventory** | Inventory | Bulk Quantity Update · Inventory Aging · Price Zone-Based Visibility · Sellable Quantity logic |
| 05 | **Coupons & Promotions** | Coupon & Promotion Capabilities | Nth-order coupons · frequency limits · group-level limits · incompatibility checks · MRP/ESP application · level-based cohort · multi-slot · geo-based offers |
| 06 | **Cart & Checkout** | Cart & Checkout | Cart function · Fraud Engine · Subscription Engine · Cart-level GWP · Stackability · Fraud control |
| 07 | **OMS & Order Lifecycle** | OMS · Integrations (Ajio Herald, Return Promise, Fraud) | Cancellation fees · Replacement/Exchange · Real-time order ringer · Quick commerce · Rectron reconciliation · Multi-Promise for Tira · Ajio Herald Order Orchestrator · Return Promise Engine |
| 08 | **Logistics & Serviceability** | Logistics · Serviceability (Fulfilment, Routing, Promise, Coverage, Quick Commerce, Misc) | Hyperlocal carriers (Grab, Shadowfax, Shipsy) · DTDC · Shipyaari · Blitz · Sequel · Clickpost · Kafka layer for scale · Multi-mode fulfillment · Polygon serviceability · Dynamic Promise per mode · International serviceability via Clickpost · Quick commerce for JioMart |
| 09 | **Payments** | Payments · Qwikcilver | CVV-less · BNPL · EDC mapping · COD payouts · payment routing · Ajio Wallets · UPI QR · multi-MOP · Qwikcilver StoreOS binding |
| 10 | **Platform · Identity · Theme · Comms** | Platform Authentication · Theme/SEO/CMS · Communications · Haptik · Seller Central VMS · Shipsy WMS/TMS | Mobile Number Update · Truecaller login · Email Verification · UCP Integration · JWT · PII Encryption · Page Mapper · CMS Maker-Checker · Global Sections · Personalization · Page Archival · Multi-Scheduler · Vue → React platform UI migration · JioCX integration · Pointblank SMS · Haptik dual React/Vue |

**Visual component (proposed default · open for D2 below):**
- 10 cards in a `grid md:grid-cols-2 lg:grid-cols-3` (matches Ecosystem cards above for visual rhythm)
- Each card: cap-num index (`01` … `10`) · h3 area name · 1-line lede · `<ul>` of 3-6 bullets · bottom mono line `~N items shipped`
- **No per-item dates** (PDF doesn't carry them — see §9 D4)
- **No "Source" footer line** (per ask #5; the section eyebrow says `· platform changelog` and the body subhead names the source — that's enough for apex)

### §08 · Sources — RESOLVED · NO SOURCES BLOCK on /jcp/
Per D6 there is no §08 on `/jcp/`. All provenance lives in git. The `/jcp/release-notes/` subpage retains its own §08 (single line citing the JCP Release Notes PDF).

### Footer
Standard footer — no change. Per `website-tone-of-voice` §1, the footer is the single copyright line; no Owner / version line.

---

## 4. Data model

Two pages, one of them new. Both hand-authored — no renderer, no YAML.

| File | Why hand-author |
|---|---|
| `jcp/index.html` | Edit-in-place — already authored, this is a structural reorient |
| `jcp/release-notes/index.html` | Single page · 10 fixed accordion sections · skill rule §1 says ≤6 sub-pages → hand-author. One page = trivially within that. The PDF is a one-time source extraction; nothing re-parses it on rebuild. |

If the release-notes content ever needs to be machine-driven (e.g., per-area sub-pages, or a renderer that ingests CSV from JCP product), promote to `data/jcp/release-notes.yaml` + `tools/build_jcp_release_notes.py` at that point.

---

## 5. Asset pipeline

No new images. The 45-page release-notes PDF includes admin-UI screenshots — those are operator-facing and stay out of the published page. The PDF itself remains in `docs/jcp-notes-compilation/` as the source of truth (not linked from the published page; it's confidential operator material).

If a future iteration wants visual evidence on `/jcp/release-notes/`, extract 4-6 marquee screenshots only (e.g., Vertex Search admin, Discount v2 builder, Promise Configuration) and host them via the standard CDN flow (skill §6). Not in v1 scope.

---

## 6. Navigation wiring

A new subpage means **the JCP subnav grows by one chip**. That's the only nav change — no top-nav, IP Catalog, or footer-list edit needed (the parent /jcp/ entry already covers discovery).

### Edit · `tools/site_chrome.py` SUBNAV["jcp"]
Insert `Release Notes` chip. Position it last among JCP-internal pages (before RBL/RCPL which are separate tracks):

```python
"jcp": [
    {"href": "/jcp",                "label": "Overview"},
    {"href": "/jcp/channels",       "label": "Channels"},
    {"href": "/jcp/cataloging",     "label": "AI Cataloging"},
    {"href": "/jcp/7eleven",        "label": "7-Eleven"},
    {"href": "/jcp/release-notes",  "label": "Release Notes"},   # NEW
    {"href": "/rbl",                "label": "RBL"},
    {"href": "/rcpl",               "label": "RCPL"},
],
```

### Then re-inject across all JCP-subnav pages:
```bash
.venv/bin/python tools/inject_subnavs.py
```

This propagates the new chip to /jcp/, /jcp/channels/, /jcp/cataloging/, /jcp/7eleven/, /rbl/, /rcpl/ and the new /jcp/release-notes/.

### Things NOT changing
- Top-nav Tracks mega-menu — `/jcp/` parent entry already there
- IP Catalog — `/jcp/` parent entry already there
- Footer "Other tracks" lists — list parent tracks only, not subpages
- Home page card — links to `/jcp/`, not subpages

---

## 7. Build / verify

All hand-edit. No new scripts.

```bash
# 1. Edit jcp/index.html
#    - remove §B2C, §B2B, §AJIO migration, §closer
#    - edit hero eyebrow (drop "Accenture · 16-Apr-2026 · slide 35")
#    - drop trailing source <p> in Ecosystem
#    - replace inline AI Cataloging callout with new §02 two-card grid
#    - add §08 sources notes line
#    - renumber section labels per canonical (00 → 01 → 02 → 04 → 08)

# 2. Create jcp/release-notes/index.html
#    - hand-author from spec §3
#    - 10 <details>/<summary> accordions
#    - extract verbatim line items from JCP Release Notes PDF (one-time)

# 3. Update tools/site_chrome.py SUBNAV["jcp"] (add Release Notes chip)
.venv/bin/python tools/inject_subnavs.py

# 4. Local verify
python3 -m http.server 8765
# Walk:
# - http://localhost:8765/jcp/                — confirm 4 surviving sections + canonical numbering
# - http://localhost:8765/jcp/release-notes/  — confirm hero + 10 accordions + sources
# - http://localhost:8765/jcp/cataloging/     — confirm subnav chip update propagated
# - http://localhost:8765/jcp/channels/       — same
# - http://localhost:8765/jcp/7eleven/        — same

# 5. /audit pass via website-page-reviewer skill on both /jcp/ and /jcp/release-notes/
```

Sweep after the section deletes — per skill §10 "Renumber tax":
```bash
grep -n 'section-label mb-3">[0-9]' jcp/index.html
# numbers should be a contiguous canonical run (00 → 01 → 02 → 04 → 08)
```

---

## 8. Phased delivery

| Phase | Scope | Time |
|---|---|---|
| **P0** | Sign-off on §9 decisions | (this convo) |
| **P1** | Edit `jcp/index.html` — section removals · hero/ecosystem eyebrow cleanup · §02 two-card grid · §08 sources | ~30 min |
| **P2** | Extract ~150 verbatim line items from `JCP Raw Release notes 2025-26.pdf` into a working list grouped by the 10 capability areas | ~60 min |
| **P3** | Hand-author `jcp/release-notes/index.html` — hero · §01 jump-cards · §02 ten accordions populated from P2 list · §08 sources | ~90 min |
| **P4** | `tools/site_chrome.py` SUBNAV edit + `inject_subnavs.py` re-run | ~10 min |
| **P5** | Local verify + `/audit` skill pass on both pages + fix findings | ~45 min |
| **P6** | Commit (one logical change per commit per skill §13) + push | ~10 min |

Total: **~4-4.5 hr** (after sign-off).

---

## 9. Decisions

**D1 · Section order — RESOLVED by skill canonical ordering**
The `website-section-authoring` skill §4 puts "What's live" at §02. With Release Notes promoted to a subpage (D5), §02 on `/jcp/` becomes the two-card "deep-dive launcher" grid (Release Notes + AI Cataloging). Vertex Search becomes §04. Documented in §3 above.

**D2 · Visual treatment for the Release Notes — RESOLVED**
Accordion (`<details>` / `<summary>`) per capability area. CSS-only · no JS · default-collapsed · per-area item count visible without expanding.

**D3 · Granularity of bullet items — RESOLVED**
Exhaustive · all ~150 line items verbatim from the PDF · grouped into the 10 capability areas. Item extraction is a one-time author pass during P2 (no PDF re-parsing on rebuild).

**D4 · Date stamping — RESOLVED by source**
Single `FY 2025-26` stamp at section level. The source PDF carries no per-item dates so anything finer would be invented. If JCP product later supplies a dated CSV, promote to YAML + renderer + per-area quarterly grouping.

**D5 · Inline vs subpage — RESOLVED**
Promote to dedicated `/jcp/release-notes/` subpage. `/jcp/` carries a CTA card in §02 alongside the AI Cataloging CTA. Confirmed by user note "release notes are too dense and need a separate page".

**D6 · Source attribution on /jcp/ — RESOLVED**
Strip ALL deck/slide references everywhere on `/jcp/`. No §08 Sources block on `/jcp/` (provenance lives in git). Pulls: hero eyebrows · Ecosystem subhead Accenture mention · Ecosystem trailing `<p>Source…</p>` · Vertex Search "Source: 'Vertex Search · Proven Performance Uplift'" callout. The `/jcp/release-notes/` subpage keeps its own §08 sources line because the PDF is the single source for the entire page.

**D7 · Treatment of removed B2C / B2B content — RESOLVED**
Hard-delete from `jcp/index.html`. Trust git history. The `/jcp/channels/` gallery already covers per-brand depth.

---

## 10. Out of scope (v1)

- Per-item dates on Release Notes (PDF doesn't carry them — D4)
- Marquee screenshots on `/jcp/release-notes/` (4-6 admin-UI captures could be CDN-hosted; defer to v2 once content lands)
- Editing `/jcp/cataloging/`, `/jcp/channels/`, `/jcp/7eleven/` content — unaffected by this reorient (only the subnav chip propagates)
- AJIO × JCP migration content — fully removed; if it needs to live somewhere, that's a separate spec
- `data/jcp/release-notes.yaml` + renderer — premature; promote when JCP product supplies a machine-readable feed

---

## 11. Implementation log (what actually shipped)

The v0.5 spec went through **4 feedback rounds** during implementation. This log captures the as-built state, deviations from the original plan, and the scripts/commands that proved useful.

### 11.1 Final `/jcp/` page structure (v0.7, shipped)

```
§0   Hero            stats + 3 people tiles (Product · Eng · RIL counterpart)
§01  Where deployed  B2C/B2B 2-card grid → /jcp/channels/                    (NEW vs v0.5)
§02  Architecture    Fynd-for-Retail diagram from Fynd Commerce 2025 deck    (NEW vs v0.5)
§03  Platform properties  9 Ecosystem cards (was §01 in v0.5; demoted + retitled)
§04  What's live     2-card CTA grid → Release Notes + AI Cataloging deep-dives
§05  Vertex Search   3-col stats (was 4; ROI payback tile dropped in round 4)
Footer                no Sources block, per D6
```

### 11.2 Subpage shipped: `/jcp/release-notes/`

- Hero + 4 stat tiles (~150 items · 10 areas · 79 channels · Internal source)
- §01 ten jump-link cards
- §02 ten `<details>` accordions (CSS-only · default-collapsed) with verbatim line items + 1 marquee admin-UI screenshot per area (Inventory + Cart get text-only)
- No §08 Sources block (removed in round 3)

### 11.3 Cross-page changes that landed alongside

- `/jcp/channels/` — Mobile-app section moved before Storefronts; broken `↗` arrow on app cards removed; storefront URLs surfaced as prominent underlined hyperlinks; "Captured from RBL OS Synthetic Monitor" sub-header removed.
- `/jcp/7eleven/` — §02 restructured from 6-card grid + dump-of-screenshots-at-bottom to 6 vertically-stacked cards (2.1–2.6) each with its inline screenshots; SOURCES block removed.

### 11.4 Scripts / commands that proved useful

**PDF screenshot extraction — the right way:**
```bash
# WRONG (round 2 attempt): renders entire PDF page including bullet text — illegible
pdftoppm -r 150 -jpeg -f $page -l $page input.pdf out

# RIGHT (round 3 fix): extracts embedded UI images directly, no surrounding text
pdfimages -j -f 1 -l 45 input.pdf /tmp/img
# Then convert PPM → JPEG via PIL
```

**Image trim + resize via PIL:**
```python
from PIL import Image, ImageChops
im = Image.open(p).convert('RGB')
bg = Image.new('RGB', im.size, (255,255,255))
bbox = ImageChops.difference(im, bg).getbbox()
im.crop(bbox).save(p, 'JPEG', quality=85, optimize=True)
```

**Architecture diagram crop (remove slide title from top + logo from right):**
```python
w, h = im.size
im.crop((0, int(h*0.11), int(w*0.96), h))  # crop top 11% + right 4%
```

**CDN cache invalidation — query strings DON'T work:**
```bash
# CDN at socialassets.impetusz0.de IGNORES query strings — re-uploading
# the same filename leaves the cached version live (max-age=3600).
# Must use a versioned filename (-v2, -v3) to force a fresh fetch.

cp 09-payments.jpg 09-payments-v2.jpg
gsutil -h "Cache-Control:public,max-age=3600" -m cp *-v2.jpg \
  gs://impetus-socialpilot/rrl-portfolio/assets/jcp/release-notes/

# Then sed-rewrite HTML to point to -v2:
sed -i.bak 's|/release-notes/01-search\.jpg|/release-notes/01-search-v2.jpg|g' \
  jcp/release-notes/index.html
```

**Subnav chip propagation:**
```bash
# Edit tools/site_chrome.py SUBNAV["jcp"] to add the new chip
# Then re-inject across all JCP-subnav pages:
.venv/bin/python tools/inject_subnavs.py
# But: tools/inject_subnavs.py TARGETS list is hand-maintained. New
# subpages must be added there OR the inject is silent. /jcp/channels/
# is built by build_jcp_channels_page.py and does NOT go through the
# injector — needs a separate rebuild.
.venv/bin/python tools/build_jcp_channels_page.py
```

### 11.5 Lessons (now reflected in skill updates)

| Lesson | Where captured |
|---|---|
| `pdfimages -j` beats `pdftoppm` for embedded UI screenshots | `website-section-authoring` §6 Asset pipeline |
| CDN ignores `?v=` query strings; use filename suffix to invalidate | `website-section-authoring` §6 GCS mirror + §10 Common issues |
| Default to no §08 Sources block on register pages | `website-tone-of-voice` §5 |
| Don't add named "Lead: …" to a deep-dive section unless the lead's name is the headline (rare) | `website-tone-of-voice` §6 |
| One target per card — no decorative `↗` arrow that just links to the same place as the card body | `website-tone-of-voice` §5 |
| Unsourced "X-month ROI payback" tiles are register banned | `website-tone-of-voice` §3 |
| Screenshots that include surrounding text from the source PDF are illegible at apex grain — extract the UI element only | `website-section-authoring` §6 |

### 11.6 Commits shipped

| Commit | Scope |
|---|---|
| `c1cfd72` | spec · jcp-reorient v0.5 |
| `a2ab70c` | /jcp/ · v0.5 reorient (canonical sequencing, §02 CTA grid) |
| `9b17a15` | /jcp/release-notes/ · new subpage |
| `de03078` | site_chrome · Release Notes subnav chip propagation |
| `7ddb8cd` | /jcp/ · v0.6 architecture-led structure (round 1 · §01 Where + §02 Architecture + §03 Platform properties) |
| `755eb5c` | /jcp/ + release-notes · feedback round 2 (people block, channel list, mobile-before-desktop, accordion alignment, first screenshot pass) |
| `832da27` | /jcp/ + sub-pages · feedback round 3 (architecture crop, sources removal, screenshot re-crop via pdfimages) |
| `444e8e6` | /jcp/ + channels · feedback round 4 (Vertex tile + lead removal, channel card hyperlinks) |

---

**End of spec.** Shipped 2026-05-01. Future iterations should start a new spec rather than amending this one.
