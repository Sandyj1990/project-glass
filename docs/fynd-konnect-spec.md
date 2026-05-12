# Fynd Konnect · Spec

**Status:** v0.1 · 2026-05-01 · draft for sign-off
**Owner:** Kushan Shah
**Route:** `/fynd-konnect/` (new)
**Source content:** `docs/fynd-konnect-notes-compilation/`
**Narrative anchor:** `docs/2026-04-30-farooq-mda-update-letter.md` — answers MM Sir's ask for "all sub-platforms deployed, adoption across the value chain… platforms involved… UCP, Granary, AI-Native Platforms…". Konnect is the integration backbone the rest of the register quietly rides on — JCP, Sephora Engage, RBL/RRVL brand operations, marketplace expansion all touch it.
**Inherits from:** `docs/website-orientation-spec.md` · §3 page template · register copy via `website-tone-of-voice` skill

---

## 1. Why this page exists

**Audience.** RIL Apex leadership (MM Sir level) reviewing the register at `reliance-retail-fynd.vercel.app`. Copy must be apex-readable: factual, scannable, no marketing voice, no Fynd self-praise, names where they matter, claims that survive challenge.

**Gap to close.** The register has `/jcp` (JioMart channel surface) and `/rbl` / `/rcpl` (brand customers) but no page for the **integration backbone** that connects them — the SAP / TIBCO / Kafka layer that decides whether RBL's brand portfolio can scale safely on Fynd Commerce. Today an Apex reader hitting "where does Konnect live?" finds nothing. The Partnership Review PDF (May 2025–May 2026) is a 13-capability operational record that has no home on the site.

**Why this belongs in the apex register.** Three angles:

1. **Scale evidence.** `~800` live brands on JioMart through Fynd Omni · `3-4 lakh` shipments/month · `20+` RBL & RRVL brands on the SAP integration layer · `50+` marketplace channels across `9+` countries. These numbers belong somewhere readable.
2. **The integration honesty contract.** Konnect is what makes RBL's Furniture, Fashion, Beauty and 7-Eleven India onboardings reconcile in SAP without manual finance work. It's invisible when it works; the page makes it visible.
3. **International expansion thesis.** Most RBL brands have an active or planned international thesis. Konnect compresses that timeline because the marketplace-integration layer is already in place — Noon, Lazada, Shopee, TikTok Shop already wired.

---

## 2. Source inventory

| Source | Type | Path | Key facts |
|---|---|---|---|
| Fynd × RRL Platform Partnership Review | PDF · 20pp · 391KB | `docs/fynd-konnect-notes-compilation/Fynd RRL Platform Partnership Review copy copy.pdf` | The canonical 6-section document. Four pillars; 13 RBL capabilities organised into 6 themes (Foundation Architecture · Compliance & Finance · Brand Enablement · Loyalty & Programmes · Payments Modernisation · Performance & Ops); marketplace gateway across India / Middle East / SEA. |
| Emazing case study | PDF · ~1MB | `docs/fynd-konnect-notes-compilation/DOC-20260224-WA0000.pdf` | Fynd WMS at Emazing (3PL on JioMart) · 73% complaint reduction · 8.8% expired-product complaints prevented · 20% packing efficiency · 100% batch + expiry visibility · Quote from Mohd Suhel Ansari, COO Emazing Deals Limited. |
| Platform architecture diagram | PNG · 442KB | `docs/fynd-konnect-notes-compilation/Platform architecture.png` | The Konnect-as-hub diagram. Marketplaces (Amazon, Flipkart, Myntra, Nykaa, Meesho, IR, Shopee, TikTok Shop, Lazada) + Storefronts (Shopify, Magento, Woo) + Fynd Marketplaces (TIRA, Ajio) on the left; 3P ERP (SAP, JD), 3P WMS (Unicommerce, Increff, Browntape, Vinculum, EasyEcom, Logic, Manhattan, etc.), 3P POS (Petpooja, Ginesys, Ajira, Wondersoft), Store OS on the right. Centre: Fynd Commerce + Konnect with eight subsystems — Sales & Returns Posting · Shipping Updates · Analytics & Insights · Inventory Sync · Returns Management · Product Catalog · Pricing Updates · Order Processing. |

**Aggregate KPIs derivable from source:**
- `~800` live omni-seller brands on JioMart via Fynd Omni
- `3-4 lakh` shipments / month on JioMart 3P, sustained growth
- `7` major aggregator platforms normalised into one integration contract (Unicommerce, Vinculum, Increff, Browntape (Ginesys), EasyEcom, OMSGuru, Petpooja POS)
- `20+` RBL & RRVL brands on the SAP/TIBCO posting layer
- `13` major capability deliveries to RBL between May 2025 and May 2026
- `2` dedicated Kafka clusters processing inventory events (Fynd cluster + SNG JCP cluster) — `100+` stores per brand
- `10+` distinct payment methods covered across all brands (Flipkart prepaid · Myntra PPMP · COD with DP own-account · Qwikcilver · JioPay · JioOnePay · multi-PG · BharatPay QR · price-adjustment MOPs)
- `50+` marketplace channels across `3` regions, `9+` countries
- `73%` reduction in customer complaints at Emazing post-Fynd-WMS

---

## 3. Page structure

Single-page section. Konnect is one product family with four pillars — splitting into sub-pages would fragment the integration story. Hand-authored `index.html`, no renderer (this is below the 6-card cutoff for a Stage 4 build script).

Section order follows the canonical default with one override (D2 below): no separate `§03 Architecture` card-grid because the Platform architecture diagram earns its own visual moment in `§02`.

### §0 · Hero
- Crumb: `Home / Fynd Konnect`
- Section label: `AI-Native · Fynd Konnect · Integration backbone for the Reliance ecosystem`
- H1: **Fynd Konnect.**
- Subhead: *"The integration backbone connecting JioMart, RBL and RRVL brand operations, Sephora India loyalty, and 50+ marketplaces. ~800 live brands · 3-4 lakh shipments/month · 13 RBL capability deliveries in 12 months."*
- Status pills: `Live · ~800 brands on JioMart` · `Live · 20+ RBL & RRVL brands on SAP layer` · `Live · 50+ channels across 9+ countries`
- Stat tiles (4): brands · shipments/month · RBL capabilities · marketplaces

### §01 · Status (01 - May - 2026)
3-column Live / Building / Roadmap strip — the canonical opening.
- Live: Four pillars in production
- Building: Self-Ship for 1P JioMart sellers (UrbanLadder), JioMart Quick (UrbanPiper, Rista POS connectors), Split Payment posting
- Roadmap: Continuous marketplace + aggregator pipeline

### §02 · Platform architecture (one diagram)
The Platform architecture PNG · captioned. Header: *"What Konnect connects."* Subhead names the eight subsystems that flow through Konnect (Sales & Returns Posting · Shipping Updates · Analytics & Insights · Inventory Sync · Returns Management · Product Catalog · Pricing Updates · Order Processing).

### §03 · The four pillars
Four-card row · each card opens to a deeper section below.
- Pillar 1 · JioMart 3P Seller Platform (Fynd Omni) → §04
- Pillar 2 · RBL & RRVL Brand Operations (SAP/TIBCO) → §05
- Pillar 3 · Sephora India Omnichannel Loyalty (Fynd Engage) → §06
- Pillar 4 · Global Marketplace Reach (Fynd Konnect) → §07

### §04 · Pillar 1 · JioMart 3P Seller Platform (Fynd Omni)
- Scale table: Live brands, Monthly shipments, Aggregators integrated, Core JioMart systems
- "How the integration works" 5-bullet block · Inventory · Catalogue · Orders · Shipment status · Onboarding
- Aggregator ecosystem table · 7 platforms (Unicommerce, Vinculum, Increff, Browntape (Ginesys) · EasyEcom · OMSGuru · Petpooja POS) with coverage one-liner each
- Roadmap: Self-Ship for 1P JioMart sellers (UrbanLadder); Hyperlocal/Quick (Petpooja live, UrbanPiper + Rista next); Partner expansion
- **Live evidence card · Emazing** (the inline case study). 4 numbers + 1-line quote from COO. Sub-card with `Live` pill.

### §05 · Pillar 2 · RBL & RRVL Brand Operations · 13 capability deliveries
The page's deepest section.
- Brand portfolio table (Fashion · Furniture · Beauty · RRVL formats · Reliance Retail Formats)
- Twelve months at a glance — the 13-capability index (#, Capability, Theme)
- Then six theme groups, each rendered as a card cluster:
  - **Foundation Architecture** (3 deliveries): 01 SAP WM Migration · 06 RRA Kafka Pipelines · 09 RBL Furniture parity
  - **Compliance & Finance** (3 deliveries): 02 B2B E-Invoice (IRN) · 04 Multi-MOP Coverage · 05 Delivery Partner Own-Account Posting
  - **Brand Enablement** (3 deliveries): 03 Product Exchange · 08 TIRA & Nexus Marketplace · 13 EAN vs. Article Code
  - **Loyalty & Programmes** (1 delivery): 10 Sephora Beauty Pass loyalty in SAP posting
  - **Payments Modernisation** (2 deliveries): 11 JioOnePay / JioPay Multi-PG · 12 Split Payment Readiness
  - **Performance & Operational Excellence** (1 delivery): 07 Skip Unchanged Inventory

Each capability card carries: number badge, title, scope bullets, business outcome line, and a `Live` pill.

### §06 · Pillar 3 · Sephora India Omnichannel Loyalty (Fynd Engage)
- Lead paragraph: True omnichannel loyalty (one identity, one balance, one tier) — not three siloed stacks
- Capability bullets: unified member identity, earn flows, redeem flows, boutique product handling, mixed-cart logic, returns/reversals
- Strategic outcome line

### §07 · Pillar 4 · Global Marketplace Reach
- Why it matters paragraph: International expansion as a configuration exercise, not an engineering project
- Three sub-tables: India (30+ marketplaces) · Middle East (5) · Southeast Asia (5)
- "Taking an RBL brand into a new market" — 4-step playbook

### §08 · Sources
Card list of the 3 source files cited, with paths and date stamps. Standard last section.

### Footer
Standard footer block. No Author/Date/Owner page metadata (per spec convention).

---

## 4. Data model

Single YAML — `data/fynd-konnect/index.yaml` — captures the structured facts. The hand-authored `index.html` reads from it conceptually but doesn't render programmatically (single-page section).

Schema:

```yaml
slug: fynd-konnect
title: Fynd Konnect
status: live
date: 2026-05-01
source_folder: docs/fynd-konnect-notes-compilation/
source_citation: "Fynd × RRL Platform Partnership Review · May 2026 · v1.0"

hero:
  brands_live: "~800"
  shipments_per_month: "3-4 lakh"
  rbl_capabilities_delivered: "13"
  marketplaces: "50+"

pillars:
  - name: "JioMart 3P Seller Platform"
    fynd_name: "Fynd Omni"
    scope: "..."
    outcome: "..."
  # ...4 pillars

rbl_capabilities:
  - num: "01"
    title: "SAP WM Migration — MDN to Delivery-Based Model (DBM)"
    theme: "Foundation Architecture"
    scope:
      - "Previously, stock movement was posted in SAP on the basis of sales via POSDTA — architecturally misaligned with how SAP actually accounts for stock."
      # ...
    outcome: "The DBM became the prerequisite for safe brand onboarding…"
  # ...13 entries

aggregators:
  - { name: "Unicommerce", coverage: "India's largest e-commerce enablement SaaS" }
  # ...7 entries

marketplaces_india:    [{ name, business_models }, ...]
marketplaces_me:       [{ name, coverage }, ...]
marketplaces_sea:      [{ name, coverage }, ...]

emazing:
  metrics:
    complaint_reduction: "73%"
    expired_complaints_prevented: "8.8%"
    packing_efficiency: "20%"
    batch_visibility: "100%"
  quote: "Fynd WMS gave us the control we needed over batch, expiry, and accuracy. For FMCG there's no room for error and now we have a system that ensures there isn't any."
  attribution: "Mohd Suhel Ansari, COO, Emazing Deals Limited"
```

---

## 5. Asset pipeline

Source `docs/fynd-konnect-notes-compilation/` → published `assets/fynd-konnect/`.

### Pass A · diagram
- `Platform architecture.png` (442KB) → resize to max-width 1600px, jpeg q85 → `assets/fynd-konnect/01-platform-architecture.jpg`
- Crop trailing whitespace if any.

### Pass B · Emazing PDF screenshots
- The Emazing case study PDF has 3 useful diagram screenshots (packing-station illustration, batch-tracking flow, packing manual-verification illustration) and 1 metrics tile.
- Use `pdfimages -j` (per skill §6 — pdftoppm would render the surrounding text as noise).
- Pick the cleanest 1-2 images for the inline evidence card.
- Output: `assets/fynd-konnect/02-emazing-warehouse.jpg`, `assets/fynd-konnect/03-emazing-metrics.jpg`

### Pass C · source PDFs
- Copy as-is (both <2MB):
  - `assets/fynd-konnect/Fynd-RRL-Platform-Partnership-Review.pdf`
  - `assets/fynd-konnect/Emazing-WMS-case-study.pdf`

### GCS mirror
Total payload <5MB · ~5 files. **Skip GCS** — local hosting is sufficient.

---

## 6. Navigation wiring

Six-file checklist:
- [x] **Home page card** (`index.html`) — add a Fynd Konnect card or link mention
- [x] **Top-nav Tracks mega-menu · AI-Native column** — add Konnect entry (per D1 below)
- [ ] **More mega-menu** — N/A (not a meta-page)
- [ ] **IP Catalog** (`/catalog`) — add entry (lazy: defer to release sweep)
- [x] **`tools/site_chrome.py`** — add to `AI_NATIVE` list, run `tools/inject_chrome.py` to propagate across all `index.html` files
- [ ] **Sibling section indexes** — `/jcp` mentions Konnect; sweep for backlink update (lazy)

**Strategy:** Strict for site_chrome.py + injector (one shot, all pages updated). Lazy for IP Catalog and sibling backlinks (acceptable for v0.1 of a section nobody links to yet).

---

## 7. Build / verify

Single hand-authored `index.html`, no build script.

```bash
# Verify
python3 -m http.server 8000
# open http://localhost:8000/fynd-konnect
# DevTools console: sessionStorage.setItem('fyndrrl_auth_v1', '1'); location.reload();
```

Walk the §9 verify checklist from the website-section-authoring skill. Then run `website-page-reviewer` skill for the audit pass.

---

## 8. Phased delivery

| Phase | Scope | Time |
|---|---|---|
| **P1** | Spec + data YAML | ~30 min |
| **P2** | Asset pipeline (architecture diagram + Emazing extracts) | ~20 min |
| **P3** | Hand-author `/fynd-konnect/index.html` | ~75 min |
| **P4** | Nav wiring (site_chrome + injector + home card) | ~15 min |
| **P5** | Verify + audit + polish | ~30 min |

Total v0.1: **~2.5 hr.**

---

## 9. Decisions

1. **D1 · Nav placement.** Konnect lives in the **AI-Native** column of the Tracks mega-menu, alongside Boltic / PixelBin / Ratl / Kaily. *Why:* user-locked decision (2026-05-01). Konnect is integration infrastructure, not strictly AI-native, but the user is treating Fynd's platform infrastructure as part of the AI-native register. *How to apply:* `tools/site_chrome.py` `AI_NATIVE` list gets Konnect appended with suffix `"integration backbone"`.

2. **D2 · Architecture is one diagram, not a 4-card layered grid.** The canonical default §03 is a 4-card layered architecture. Konnect's source ships an authored architecture diagram (Platform architecture.png) that is more legible than any card-grid we'd derive from it. *Why:* the diagram already shows the marketplaces / storefronts / 3P-system network around the Konnect hub — a re-derivation loses fidelity. *How to apply:* §02 renders the diagram as a single bordered visual; §03 becomes "The four pillars" navigation summary instead.

3. **D3 · Emazing as inline evidence card under Pillar 1.** The Emazing case study sits as a card with 4 metrics + 1 quote inside §04 (Pillar 1 · JioMart). *Why:* user-locked decision (2026-05-01). Keeps the page single-scroll; avoids splitting into a sub-page when the case is one page of evidence. *How to apply:* card has `Live` pill, 4-metric grid, attributed quote, link to source PDF.

4. **D4 · Author / Owner page metadata stripped.** Per the website-section-authoring §4 convention. No Author / Date / Version line in hero. Standard footer copyright only. *Why:* page-level convention; provenance lives in git + this spec file.

5. **D5 · Brand portfolio names stay verbatim from source.** TUMI, GAP, WestElm, Pottery Barn, PB Kids, Sephora, Hamleys, Superdry, Ritu Kumar, Performax, Reliance Trends, YOUSTA, TIRA, Freshpik, Swadesh, 7-Eleven India, Nexus malls, Ajio. *Why:* Apex audience knows these brands; substituting or paraphrasing creates ambiguity. *How to apply:* render exactly as in source PDF Section 2.2 / 4.1.

---

## 10. Out of scope (v0.1)

- **Sub-page per pillar.** Each pillar could be its own page (Pillar 2 alone has 13 capabilities and would justify it). Defer: the page-as-one-document is the better Apex artefact for v0.1; sub-page split waits for Apex feedback.
- **Per-capability deep-dive screenshots.** Some RBL capabilities (e.g., the SAP DBM flow) would benefit from a flow diagram. The source doesn't include one and we won't fabricate. Defer to a v0.2 if Fynd authors deliver flow diagrams.
- **IP Catalog entry update.** Lazy nav strategy — sweep next time we touch `/catalog`.
- **`/jcp` backlink mentioning Konnect.** JCP page exists and references Konnect implicitly; explicit cross-link added in next JCP touch, not this one.
- **Live SAP / Kafka dashboards.** No telemetry surfacing to public site (security).
- **DRI / team names per capability.** The source PDF intentionally omits per-capability owners; we don't add them.

---

**End of spec.** Awaiting sign-off before implementation.
