## SwapEasy · Spec

**Status:** v0.1.1 · 2026-05-01 · audit pass applied (8 findings resolved · inline source attributions removed)
**Owner:** Ashish Chandorkar (Fynd · CPO, JCP) · RIL counterpart · Varun Dhanuka
**Route:** `/swapeasy/` (new)
**Source content:** `docs/swapeasy-notes-compilation/`
**Narrative anchor:** `docs/swapeasy-notes-compilation/SwapEasy_APEX_Board_Note.docx` (Ashish Chandorkar → Reliance APEX Board · May 2026) — answers the explicit ask: *"endorsement of SwapEasy as a horizontal platform commitment across formats — not a Reliance Digital-only initiative."*
**Inherits from:** `docs/website-orientation-spec.md` · §3 page template · register copy via `website-tone-of-voice` skill · canonical section ordering via `website-section-authoring` skill §4.

---

## 1. Why this page exists

**Audience.** RIL Apex leadership (MM Sir level) reviewing the register at `reliance-retail-fynd.vercel.app`. Copy must be apex-readable: factual, scannable, no marketing voice, no Fynd self-praise, names where they matter, claims that survive challenge.

**Gap to close.** The register has no entry for SwapEasy today. The Tracks mega-menu lists 14 platforms / projects / AI-native products; SwapEasy is a deployed JCP product running across 625 RD stores and 854 MJS stores, generating ₹3.75 Cr/month of incremental SAP-traceable revenue, and is currently invisible in the register. The May-2026 APEX Board Note is the moment SwapEasy is being formally pitched as a horizontal platform commitment — the register needs to carry the page before that conversation lands.

**Why this belongs in the apex register.** SwapEasy is the only deployed re-commerce surface in the register. It is the Reliance answer to a $6B → $11B organised second-hand electronics market (CAGR ~17%). It demonstrates the JCP pattern of building a horizontal platform that sits underneath multiple Reliance retail formats — the same shape JCP itself takes for forward commerce, applied to re-commerce. And it carries a measurable adoption gap (network attach rate 1.6% vs proven 10.5% on Apple 16+) that is exactly the kind of execution problem the Apex board can unblock.

---

## 2. Source inventory

| Source | Type | Path | Key facts |
|---|---|---|---|
| APEX Board Note · May 2026 | docx | `docs/swapeasy-notes-compilation/SwapEasy_APEX_Board_Note.docx` | Single canonical narrative · all live metrics, 60-day workstreams, 6-month roadmap, vision, asks |
| In-store flow · landing | png · 1320×2868 | `docs/swapeasy-notes-compilation/IMG_1562.png` | Customer surface · "Exchange karo. Extra Savings paao." promo · "Bonus up to ₹8000 Exchange" · Mobile category card · store address auto-bound (My Jio Store, Bony Plaza Shop) |
| In-store flow · brand select | png · 1320×2868 | `docs/swapeasy-notes-compilation/IMG_1563.png` | Step 1/2 of "Exchange Your Mobile" · 8 brands visible (Vivo, Tecno, Samsung, Realme, POCO, OPPO, Nothing, Nokia) · search-for-models field |
| In-store flow · quote | png · 1320×2868 | `docs/swapeasy-notes-compilation/IMG_1564.png` | Quote screen · Apple iPhone 17 Pro Max (12 GB / 512 GB) → "Get up to ₹1,05,500" · CTAs: Get Exact Value · Select your Device · Check for another mobile |
| Admin console · login | png · 3574×2074 | `docs/swapeasy-notes-compilation/Screenshot 2026-05-01 at 4.10.47 PM.png` | SwapEasy operator login · `+91` mobile-OTP · Terms & Privacy links |
| Admin console · Exchanges | png · 3598×2086 | `docs/swapeasy-notes-compilation/Screenshot 2026-05-01 at 4.11.40 PM.png` | List of Exchange Orders · 10-status pipeline (All / Confirmed / Cancelled / Handover / Pickup Awaited / Pickup Completed / Not Picked Up / In Transit / Out For Delivery / RVP Delivered) · sales channels include Reliance Digital + Digital Mobile Stores · Bump Up On / Off filters |
| Admin console · Transactions | png · 3600×2088 | `docs/swapeasy-notes-compilation/Screenshot 2026-05-01 at 4.12.22 PM.png` | List Of Transactions · Liquidation Partner / Bump-Up sub-tabs · per-LP closing-balance ledger · Manually Debit-Credit · Bulk Upload / Bulk Bump-up Upload · all rows CONFIRMED |

**Aggregate KPIs derivable from source:**
- Network: 625 RD stores live (~90% of RD network) · 854 MJS stores active
- Volume: 4,189 exchanges in Oct '25 (up from ~1,000 in launch month)
- Revenue: ₹3.75 Cr incremental, Oct '25 (RD ₹3.48 Cr · MJS ₹0.27 Cr · BISMI ₹0.87 L) — all SAP-traceable
- Avg exchange value: ~₹14,000 per transaction
- Apple 16+ Oct '25 attach rate: 10.5% on transacting stores · top stores (Seawoods, 8D RCP) 15–20% · network avg 1.6%
- LP ecosystem: 41 partners onboarded · ~₹85 L wallet balance under management · 15 actively rotating capital
- Adoption proof: ₹410 avg sale per transacting store vs ₹329 non-transacting (+25%)
- Pendency: 333 units pending pickup state-wise · 26 of 41 LPs stuck
- Market context: Indian organised second-hand electronics ~$6B → ~$11B by FY26 · CAGR ~17% · smartphones 90% of supply · refurb margin 8–10% vs ~5% on new

---

## 3. Page structure

Single-page section. Hand-authored HTML rendered from one YAML. Mirrors the canonical §0 → §08 ordering with two documented overrides (see §9 D2 and D4).

### §0 · Hero
- Crumb: `Home / SwapEasy`
- Section label: `SPECIAL PROJECT · SWAPEASY · LIVE`
- H1: **SwapEasy.**
- Subhead: *"Reliance's in-store re-commerce platform. 625 RD stores live · 4,189 exchanges in Oct '25 · ₹3.75 Cr incremental revenue. Built on JCP. Owned and run by Reliance."* (29 words, opens with the lead frame, closes with the standard ownership line)
- Status pills:
  - `Live · 625 RD + 854 MJS stores · ₹3.75 Cr Oct '25`
  - `Building · network attach 1.6% → 5%+ · LP rebalance · live dashboards`
  - `Roadmap · laptops · tablets · TVs · home & living · omnichannel`
- `cap-num`: *"Live · Sep–Oct 2025 reporting period"*
- Stat tiles (4):
  - **Network coverage** · `625 RD + 854 MJS` · *90%+ of RD network*
  - **Oct '25 exchanges** · `4,189` · *up from ~1,000 at launch*
  - **Avg exchange value** · `~₹14,000` · *stable across cohorts*
  - **Liquidation partners** · `41 onboarded` · *15 actively rotating · ~₹85 L wallet*

### §01 · Status · Sep–Oct '25
- Component: 3-column Live / Building / Roadmap strip
- Source row: APEX Board Note §2 (Where we are today) + §3 (Next 60 days) + §4 (Next 6 months)
- Live column: deployed footprint (RD + MJS counts); revenue (₹3.75 Cr SAP-traceable); LP ecosystem (41 partners, ₹85 L wallet); proof point (Apple 16+ 10.5%)
- Building column: network adoption push (1.6% → 5%+ attach); LP rebalance (26 of 41 stuck); brand bump-up replication (Samsung, OnePlus, Xiaomi); live dashboards (replacing weekly emails); pilot category seed (50 stores)
- Roadmap column: Phase 1 categories (laptops, tablets, smartwatches, TVs); Phase 2 (home & living, kitchenware, online omnichannel); platform investments (multi-LP bidding, auto reconciliation, ML fraud, programmable bump-up)
- One-line readout below the strip: *"Stores that adopt SwapEasy sell more. Oct '25 data: ₹410 avg sale per transacting store vs ₹329 non-transacting (+25%). The constraint is adoption discipline, not platform capability."* (verbatim from board note §2 read-out)

### §02 · What's live for Reliance today
- Component: Module table (4 rows · status pill · DRI · anchor outcome)
- Rows:
  | Module | Status | Live for | Anchor outcome |
  |---|---|---|---|
  | Mobile exchange (customer) | Live | RD + MJS in-store counters | 4,189 exchanges Oct '25 |
  | POS-applied exchange credit | Live | All transacting stores | ₹3.75 Cr SAP-traceable revenue Oct '25 |
  | LP orchestration & wallet | Live | 41 partners across zones | ~₹85 L wallet under management |
  | Brand-funded bump-up | Live · Apple 16+ pilot | Transacting RD stores | 10.5% attach (top stores 15–20%) |
- Source citation eyebrow under the table: *"Source · APEX Board Note · §2 Where we are today · May 2026 · Ashish Chandorkar"*

### §03 · How it works · 5 steps from counter to cash *(section ordering override · see §9 D2)*
- Component: 5-step flow with the 3 mobile screenshots inline (steps 1–3) and a 2-card admin block for steps 4–5
- Steps:
  1. **Counter sign-in.** Customer enters in-store; SwapEasy auto-binds the My Jio Store address. Promo banner offers up to ₹8,000 bonus on the day's bump-up SKU. *(IMG_1562)*
  2. **Pick brand and model.** 8 OEMs visible by default (Vivo, Tecno, Samsung, Realme, POCO, OPPO, Nothing, Nokia); search for any other model. *(IMG_1563)*
  3. **Get a quote.** Standardised diagnostic on the device returns a fair-market quote — example shown: Apple iPhone 17 Pro Max (12 GB / 512 GB) → ₹1,05,500. Customer chooses *Get Exact Value* (full diagnostic) or proceeds with the quoted ceiling. *(IMG_1564)*
  4. **POS credit applied.** Approved exchange value is applied as credit at the SAP point-of-sale terminal; new device walks out with the customer the same visit. SAP captures the uplift as incremental revenue.
  5. **LP routing & reconciliation.** Old device is routed to the highest-bidding liquidation partner active in that zone, with a 3-day pickup SLA, full ledger entry, and audit trail (operator surface in §04).
- One-liner closer: *"One spine — diagnostic → quote → POS → LP — reused for every category the platform expands into (§06 roadmap)."*

### §04 · Deep dive · operator console
- Component: Two stacked screenshot cards (Exchanges, Transactions) with a 3-line caption per shot
- Screenshot 1 · **Exchanges queue.** *"List of Exchange Orders · 10-status pipeline from Confirmed through RVP Delivered. Sales channels include Reliance Digital and Digital Mobile Stores. Bump Up On / Off filters scope to brand-funded campaigns."*
- Screenshot 2 · **Transactions ledger.** *"Per-LP closing balance reconciled on every confirmed exchange. Bulk upload + bulk bump-up upload for catalogue refresh. Manually Debit-Credit Amount for ad-hoc adjustments. Order status closes the loop back to the Exchanges queue."*
- Side caption (cap-num): *"Source · operator screenshots · 01-May-2026"*

### §05 · In flight · next 60 days
- Component: 5-card grid · one per workstream · each card carries the named outcome from board note §3
- Cards (verbatim):
  1. **Network-wide adoption.** Activate the 386 RD + ~800 MJS stores that have not yet transacted. SAP-MIS daily flow into store dashboards. Field engagement by store. *Outcome by Day 60: network attach rate from ~1.6% → 5%+.*
  2. **LP ecosystem health.** Rebalance device flow to under-utilised LPs (26 of 41 stuck). Enforce 3-day pickup SLA. Clear state-wise pickup pendency (currently 333 units). *Outcome by Day 60: 100% of LPs actively rotating capital.*
  3. **Brand bump-up programs.** Replicate the Apple 16+ playbook with Samsung, OnePlus, Xiaomi for festive / Q4. Brand-funded top-ups directly on platform. *Outcome by Day 60: 3 brand programs live · double-digit attach on focus SKUs.*
  4. **Live dashboards.** Replace manual weekly emails with real-time format-, store-, and brand-level dashboards for leadership. *Outcome by Day 60: single source of truth, dashboards live.*
  5. **New-electronics expansion · kick-off.** Begin diagnostic & grading framework for laptops, tablets, smartwatches and TVs. Identify pilot stores and first LP cohort. *Outcome by Day 60: pilot category live in 50 stores.*
- Source eyebrow: *"Source · APEX Board Note · §3 Next 60 days · May 2026"*

### §06 · 6-month roadmap + vision
- Component: Two-column block. Left = roadmap table (Phase 1 / Phase 2 / Parallel platform investments). Right = vision prose (3 paragraphs).
- **Phase 1 · Beyond Mobiles, Within Electronics (Months 1–4).** Three rows: Laptops & tablets · Smartwatches & wearables · TVs & large appliances. Each carries the board-note one-liner (e.g., *"Laptops & tablets: highest near-term revenue lever after mobiles. Component-level diagnostics (battery health, screen, keyboard, ports). Refurbisher LPs onboarded with category capability."*).
- **Phase 2 · Beyond Electronics (Months 4–6+).** Three rows: Home & living · Kitchenware & small appliances · Online + omnichannel exchange. Verbatim from board note §4 Phase 2.
- **Parallel platform investments.** Four bullets: multi-LP bidding engine · auto reconciliation + LP ledger · ML fraud + tampering detection · brand-funded bump-up engine (programmable per SKU, region, season).
- **Vision (right column).** Three short paragraphs from board note §5:
  - *"SwapEasy's destination is not a feature, nor a category vertical. It is the re-commerce operating system that sits underneath every Reliance retail format — wherever a customer has something old to trade, and wherever a partner has the appetite to buy it back."*
  - *"At scale: any customer, in any Reliance store or app, across any category, can scan, get a fair quote, see brand-funded top-ups, and walk out with a new product — with the old item routed to the highest-bidding partner in their zone, fully reconciled and audited."*
  - *"Strategic value to the group: ~5% format-revenue uplift at maturity · 8–10% margin on resale vs ~5% on new · richer first-party data on upgrade cycles, brand affinity and price sensitivity · a defensible moat as India's organised re-commerce category formalises · a B2B platform asset JCP can extend to non-Reliance retailers in time."*

### §07 · Research / Evidence
- **Skipped** for v0.1. No standalone research artefact exists — the board note is a single document and is already cited inline. (See §9 D3.)

### §08 · Sources
- **Skipped** for v0.1 per the `website-tone-of-voice` default-no-Sources rule. The page cites a single canonical source (the May-2026 APEX Board Note) and surfaces it inline at the end of §02 and §05. The screenshots carry their own source eyebrow at §04. No second artefact to disambiguate. (See §9 D4.)

### Footer
Standard footer block: *"Built by Fynd. Owned and run by Reliance."* + the copyright line. **No Owner / version line on the page itself** (per `website-section-authoring` skill §4 author-metadata rule). Nav version pill in the top-right stays.

---

## 4. Data model

Single YAML at `data/swapeasy/swapeasy.yaml`. Hand-author renders directly from this file — no per-section renderer needed for v0.1.

```yaml
slug: swapeasy
title: SwapEasy
status: live
date: 2026-05-01
source_folder: docs/swapeasy-notes-compilation/
source_citation: "APEX Board Note · May 2026 · Ashish Chandorkar (Fynd · CPO JCP) → Reliance APEX Board"
ril_counterpart: Varun Dhanuka

hero:
  section_label: "SPECIAL PROJECT · SWAPEASY · LIVE"
  h1: "SwapEasy."
  subhead: "Reliance's in-store re-commerce platform. 625 RD stores live · 4,189 exchanges in Oct '25 · ₹3.75 Cr incremental revenue. Built on JCP. Owned and run by Reliance."
  cap_num: "Live · Sep–Oct 2025 reporting period"
  pills:
    - {kind: live,  text: "Live · 625 RD + 854 MJS stores · ₹3.75 Cr Oct '25"}
    - {kind: build, text: "Building · network attach 1.6% → 5%+ · LP rebalance · live dashboards"}
    - {kind: phase2, text: "Roadmap · laptops · tablets · TVs · home & living · omnichannel"}
  stats:
    - {label: "Network coverage",     number: "625 RD + 854 MJS",  context: "90%+ of RD network"}
    - {label: "Oct '25 exchanges",    number: "4,189",              context: "up from ~1,000 at launch"}
    - {label: "Avg exchange value",   number: "~₹14,000",           context: "stable across cohorts"}
    - {label: "Liquidation partners", number: "41 onboarded",       context: "15 actively rotating · ~₹85 L wallet"}

status_strip:
  date_eyebrow: "Sep–Oct 2025"
  live: ["625 RD stores live (90%+ of network)", "854 MJS stores active", "₹3.75 Cr incremental revenue Oct '25 (SAP-traceable)", "41 LPs · ~₹85 L wallet · 15 rotating", "Apple 16+ Oct '25 attach 10.5% (top stores 15–20%)"]
  building: ["Activate 386 RD + ~800 MJS non-transacting stores", "Network attach 1.6% → 5%+", "LP rebalance · 26 of 41 stuck", "Brand bump-up · Samsung, OnePlus, Xiaomi", "Live format/store/brand dashboards", "Pilot 50 stores · new electronics"]
  roadmap: ["Phase 1: laptops, tablets, smartwatches, TVs", "Phase 2: home & living, kitchenware, online omnichannel", "Multi-LP bidding engine", "Auto reconciliation + LP ledger", "ML fraud + tampering detection", "Brand-funded bump-up engine (programmable)"]
  readout: "Stores that adopt SwapEasy sell more. Oct '25 data: ₹410 avg sale per transacting store vs ₹329 non-transacting (+25%). The constraint is adoption discipline, not platform capability."

modules:
  source: "Source · APEX Board Note · §2 Where we are today · May 2026"
  rows:
    - {module: "Mobile exchange (customer)",     status: live, scope: "RD + MJS in-store counters",     outcome: "4,189 exchanges Oct '25"}
    - {module: "POS-applied exchange credit",    status: live, scope: "All transacting stores",         outcome: "₹3.75 Cr SAP-traceable revenue Oct '25"}
    - {module: "LP orchestration & wallet",      status: live, scope: "41 partners across zones",       outcome: "~₹85 L wallet under management"}
    - {module: "Brand-funded bump-up",           status: live_pilot, scope: "Apple 16+ on transacting RD", outcome: "10.5% attach (top stores 15–20%)"}

how_it_works:
  closer: "One spine — diagnostic → quote → POS → LP — reused for every category the platform expands into (§06 roadmap)."
  steps:
    - {n: 1, h: "Counter sign-in",         body: "Customer enters in-store; SwapEasy auto-binds the My Jio Store address. Promo banner offers up to ₹8,000 bonus on the day's bump-up SKU.", asset: "/assets/swapeasy/01-counter-signin.jpg"}
    - {n: 2, h: "Pick brand and model",    body: "8 OEMs visible by default (Vivo, Tecno, Samsung, Realme, POCO, OPPO, Nothing, Nokia); search for any other model.",                       asset: "/assets/swapeasy/02-brand-select.jpg"}
    - {n: 3, h: "Get a quote",             body: "Standardised diagnostic returns a fair-market quote — example: Apple iPhone 17 Pro Max (12 GB / 512 GB) → ₹1,05,500. Get Exact Value runs the full diagnostic; otherwise the quoted ceiling stands.", asset: "/assets/swapeasy/03-quote.jpg"}
    - {n: 4, h: "POS credit applied",      body: "Approved exchange value is applied as credit at the SAP point-of-sale terminal; new device walks out the same visit. SAP captures the uplift as incremental revenue.",  asset: null}
    - {n: 5, h: "LP routing & reconcile",  body: "Old device is routed to the highest-bidding liquidation partner active in that zone, with a 3-day pickup SLA, full ledger entry, and audit trail (operator surface in §04).",                                           asset: null}

console:
  source: "Source · operator screenshots · 01-May-2026"
  shots:
    - {h: "Exchanges queue",     body: "List of Exchange Orders · 10-status pipeline from Confirmed through RVP Delivered. Sales channels include Reliance Digital and Digital Mobile Stores. Bump Up On / Off filters scope to brand-funded campaigns.",                       asset: "/assets/swapeasy/04-admin-exchanges.jpg"}
    - {h: "Transactions ledger", body: "Per-LP closing balance reconciled on every confirmed exchange. Bulk upload + bulk bump-up upload for catalogue refresh. Manually Debit-Credit Amount for ad-hoc adjustments. Order status closes the loop back to the Exchanges queue.", asset: "/assets/swapeasy/05-admin-transactions.jpg"}

in_flight:
  source: "Source · APEX Board Note · §3 Next 60 days · May 2026"
  cards:
    - {h: "Network-wide adoption",       body: "Activate the 386 RD + ~800 MJS stores that have not yet transacted. SAP-MIS daily flow into store dashboards. Field engagement by store.",        outcome: "Network attach rate from ~1.6% → 5%+."}
    - {h: "LP ecosystem health",         body: "Rebalance device flow to under-utilised LPs (26 of 41 stuck). Enforce 3-day pickup SLA. Clear state-wise pickup pendency (currently 333 units).", outcome: "100% of LPs actively rotating capital."}
    - {h: "Brand bump-up programs",      body: "Replicate the Apple 16+ playbook with Samsung, OnePlus, Xiaomi for festive / Q4. Brand-funded top-ups directly on platform.",                      outcome: "3 brand programs live · double-digit attach on focus SKUs."}
    - {h: "Live dashboards",             body: "Replace manual weekly emails with real-time format-, store-, and brand-level dashboards for leadership.",                                          outcome: "Single source of truth · dashboards live."}
    - {h: "New-electronics expansion",   body: "Begin diagnostic & grading framework for laptops, tablets, smartwatches and TVs. Identify pilot stores and first LP cohort.",                      outcome: "Pilot category live in 50 stores."}

roadmap:
  phase_1:
    title: "Phase 1 · Beyond Mobiles, Within Electronics (Months 1–4)"
    rows:
      - {h: "Laptops & tablets",         body: "Highest near-term revenue lever after mobiles. Component-level diagnostics (battery health, screen, keyboard, ports) and zone-specific grading. Refurbisher LPs onboarded with category capability."}
      - {h: "Smartwatches & wearables",  body: "Lower-ticket but high-volume. Bundle exchange offers with new device sales."}
      - {h: "TVs & large appliances",    body: "Reuse the Delivery-Partner doorstep QC flow already designed for online exchanges. Integrate with existing Reliance Digital home-delivery network."}
  phase_2:
    title: "Phase 2 · Beyond Electronics (Months 4–6+)"
    rows:
      - {h: "Home & living",             body: "Furniture, décor and kitchenware exchange. Buy-back partners differ (re-furnishers, charities, secondary marketplaces); the quote-grade-orchestrate spine holds."}
      - {h: "Kitchenware & small appliances", body: "High-attach categories at JioMart, Reliance Smart and Trends Home — opens a re-commerce flywheel across formats."}
      - {h: "Online + omnichannel exchange", body: "Doorstep diagnostics and re-quote logic to bring exchange to AJIO, JioMart and Reliance Digital online journeys. Completes the omnichannel loop."}
  platform_investments:
    title: "Platform & capability investments (parallel)"
    bullets:
      - "Multi-LP bidding engine — competitive quotes per device, per zone, in real time."
      - "Automated reconciliation, LP ledger and accounting (replacing manual settlement)."
      - "ML-based fraud and tampering detection at pickup and LP receipt."
      - "Brand-funded bump-up engine, programmable per SKU, region and season."

vision:
  paragraphs:
    - "SwapEasy's destination is not a feature, nor a category vertical. It is the re-commerce operating system that sits underneath every Reliance retail format — wherever a customer has something old to trade, and wherever a partner has the appetite to buy it back."
    - "At scale: any customer, in any Reliance store or app, across any category, can scan, get a fair quote, see brand-funded top-ups, and walk out with a new product — with the old item routed to the highest-bidding partner in their zone, fully reconciled and audited."
    - "Strategic value to the group: ~5% format-revenue uplift at maturity · 8–10% margin on resale vs ~5% on new · richer first-party data on upgrade cycles, brand affinity and price sensitivity · a defensible moat as India's organised re-commerce category formalises · a B2B platform asset JCP can extend to non-Reliance retailers in time."
```

---

## 5. Asset pipeline

Source `docs/swapeasy-notes-compilation/` → published `assets/swapeasy/`. 6 PNGs total · all under 1 MB raw · no GCS mirror needed (well below the 20-file / 100MB threshold).

### Pass A · mobile screenshots (3 portrait shots, 1320×2868 PNG)

```bash
mkdir -p assets/swapeasy
sips -Z 1200 -s format jpeg -s formatOptions 85 \
  "docs/swapeasy-notes-compilation/IMG_1562.png" --out "assets/swapeasy/01-counter-signin.jpg"
sips -Z 1200 -s format jpeg -s formatOptions 85 \
  "docs/swapeasy-notes-compilation/IMG_1563.png" --out "assets/swapeasy/02-brand-select.jpg"
sips -Z 1200 -s format jpeg -s formatOptions 85 \
  "docs/swapeasy-notes-compilation/IMG_1564.png" --out "assets/swapeasy/03-quote.jpg"
```

Note: portrait shots get a tighter ceiling (1200px wide) because they will render in a phone-frame card on the page; 1600 is overkill for a tall narrow asset.

### Pass B · admin screenshots (3 landscape shots, ~3600×2086 PNG)

The login screen is mostly whitespace with a centred card — it doesn't earn a section on the page, but include in the source folder for completeness. Only ship the two operational shots:

```bash
sips -Z 1600 -s format jpeg -s formatOptions 80 \
  "docs/swapeasy-notes-compilation/Screenshot 2026-05-01 at 4.11.40 PM.png" --out "assets/swapeasy/04-admin-exchanges.jpg"
sips -Z 1600 -s format jpeg -s formatOptions 80 \
  "docs/swapeasy-notes-compilation/Screenshot 2026-05-01 at 4.12.22 PM.png" --out "assets/swapeasy/05-admin-transactions.jpg"
```

### Pass C · documents

Board note `.docx` is 14 KB · stays in source folder · not hosted as a download (internal-only operator material; the page itself is the polished surface). No PDF conversion needed for v0.1.

---

## 6. Navigation wiring

Lazy strategy for v0.1 (per skill §8): edit home + Tracks mega-menu only. Footer "Other tracks" lists across the existing pages can lag a release. Strict sweep deferred to v0.2.

| File | Edit |
|---|---|
| `index.html` (home) | Add SwapEasy card under the "Special Projects" group on the home grid |
| Tracks mega-menu (in `granary/index.html` + ~24 other pages) | Add `<a href="/swapeasy" class="mega-link">SwapEasy <span class="mono-suffix">re-commerce OS</span></a>` to the **Special Projects** column, after `HireFirst`. Use `grep -rl 'mega-link">HireFirst' --include='*.html'` to find every page; lazy strategy edits home + new page only |
| `catalog/index.html` (IP Catalog) | Add SwapEasy entry · Special Project category · 1-line description |

---

## 7. Build / verify

No renderer for v0.1 (single page, well under 6-card threshold). Hand-author `swapeasy/index.html` directly from the YAML.

```bash
# Generate web-ready assets
mkdir -p assets/swapeasy
# (run the sips commands from §5)

# Local verify
python3 -m http.server 8000
# open http://localhost:8000/swapeasy
# Bypass auth gate in DevTools console:
#   sessionStorage.setItem('fyndrrl_auth_v1', '1'); location.reload();
```

Walk the §9 verify checklist from the parent skill (covers asset 200s, mobile viewport, internal links, copy verify, etc.).

---

## 8. Phased delivery

| Phase | Scope | Time |
|---|---|---|
| **P1** | Spec sign-off (this file) | ~1.5 hr · done |
| **P2** | Asset pipeline · 5 web-ready JPGs | ~20 min |
| **P3** | Hand-author `/swapeasy/index.html` from spec + YAML | ~3 hr |
| **P4** | Nav wiring · home card + mega-menu Special Projects column + IP Catalog | ~30 min |
| **P5** | Local verify · screenshot · copy verify against tone-of-voice | ~30 min |
| **P6** | Commit · single logical commit per stage (data, assets, page, nav) | ~15 min |

Total v0.1: **~6 hr.**

---

## 9. Decisions

1. **D1 · Track placement → Special Projects.** Sits next to ALP / Retail Vista / Samarth / HireFirst, not next to Impetus / JCP / Granary / UCP. Rationale: matches the current scope (single-product, single-DRI on each side) rather than the horizontal-platform claim (which is what the board note is *asking* the Apex board to *endorse* — until that endorsement lands, the page reads more honestly as a focused initiative). Revisit on v0.2 if the Apex board grants the horizontal-platform mandate.
2. **D2 · §03 Architecture → How it works · 5-step in-store flow.** SwapEasy's apex-defensible story is the customer counter journey, not a layered abstraction stack. The 5-step flow uses the 3 mobile screenshots as inline evidence; a layered architecture diagram would either be wholly hand-drawn (no source) or read as filler. Override is documented here per the canonical-section-ordering rule.
3. **D3 · §07 Research skipped.** No standalone research artefact exists. The board note is a single document and cited inline at end of §02, §05, and §06.
4. **D4 · §08 Sources skipped.** Per `website-tone-of-voice` default-no-Sources-block rule: only one source artefact (board note + same-engagement screenshots), already cited inline. No second deck/memo/release-notes to disambiguate.
5. **D5 · Mobile screenshots · include all 3.** Strongest visual evidence of the live in-store flow; the storefront framing (My Jio Store address auto-binding) is itself part of the story (SwapEasy isn't a generic web exchange — it's an in-store SAP-integrated surface).
6. **D6 · Page shape · single page.** Under the 6-card / 6-sub-page threshold; hand-author HTML from one YAML; no renderer overhead. Matches `/granary/`, `/hirefirst/`, `/kaily/` shape.
7. **D7 · DRI line in spec only.** Spec footer carries `Owner · Ashish Chandorkar (Fynd · CPO JCP) · RIL counterpart · Varun Dhanuka`. The page itself drops the Owner / version line per §4 author-metadata rule; provenance lives in git + this spec.
8. **D8 · Login screenshot not shipped.** The 3rd admin screenshot (login screen) doesn't earn a section on the page — it's mostly whitespace with a centred card. Stays in the source folder for completeness. Only Exchanges + Transactions ship as §04 deep-dive shots.

---

## 10. Out of scope (v0.1)

- **Sub-page deep-dive on the admin console.** Defer; the two §04 shots carry enough operator evidence for v0.1.
- **B2B SwapEasy-as-a-service positioning.** Mentioned as one bullet in §06 vision; full external-retailer pitch deferred to a future page (would need a separate source).
- **The 333-unit pickup-pendency state-wise breakdown.** Mentioned as a metric in §05 LP card; no need for a state-by-state table on the public-facing register.
- **Multi-LP bidding engine deep-dive.** Listed as a parallel investment in §06; reads as a roadmap line until shipped.
- **Strict footer "Other tracks" sweep across all ~25 sibling pages.** Lazy strategy for v0.1; sweep deferred to v0.2.
- **Sub-page for `/swapeasy/research`** or any embedded paper. None exists today.
- **Live API / data feed of exchange volume.** Page is static HTML; numbers freeze at the May-2026 board-note snapshot. Refresh cadence is a manual edit per board update.

---

**End of spec.** Awaiting sign-off before implementation.
