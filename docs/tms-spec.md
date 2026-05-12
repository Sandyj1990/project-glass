---
status: draft · v0.1
owner: Kushan Shah (CTPO · Supply Chain · Fynd)
route: /tms
shape: single-page (≤6 logical sections, hand-authored, no renderer)
mode: new section
source folder: docs/tms-notes-compilation/
narrative anchor: docs/2026-04-30-farooq-mda-update-letter.md — TMS slots under "AI-Native Platforms" alongside the agentic-commerce / agentic-auto cluster, framed as the quick-commerce OS that powers Reliance's 10–30 minute delivery promise on JioMart and the in-house furniture fleet at RBL (West Elm + Pottery Barn).
---

# Spec · /tms · Fynd Transport Management System

## §0 · Status

| Stage | Status |
|---|---|
| 0 raw | ✓ — `docs/tms-notes-compilation/` (2 PDFs + 40-slide sales deck) |
| 1 spec | this file |
| 2 data | inline in single-page HTML (no YAML — single-page section) |
| 3 assets | extract 4–6 PNGs from deck + 1 cover from JioMart PDF |
| 4 build | hand-author `tms/index.html` from SwapEasy template |
| 5 nav | home + mega-menu (AI-Native column) + IP catalog + sibling backlinks |
| 6 verify | local server + chrome-devtools MCP screenshot + website-page-reviewer |

---

## §1 · Why this page exists

**Audience.** RIL Apex leadership (MM Sir level) reading the cover letter dated 2026-04-30. The letter calls out *"AI-Native Platforms"* as one of the four Fynd × Reliance pillars, listing today: Boltic, PixelBin, Ratl, Kaily. TMS is the fifth — the quick-commerce / logistics OS that runs underneath JioMart's 10–30 minute promise and RBL's furniture fleet. Until now there has been no register entry for it.

**Gap to close.** Apex sees the JioMart delivery experience but has no single page that answers: *what is the platform · who runs on it · what does it do today · what is the AI-native part · who at Fynd owns it*. The TMS sales deck and two case-study PDFs answer all five — they just need to be condensed to apex grain.

**Narrative anchor.** The 2026-04-30 cover letter from Farooq Adam to MM Sir, under *AI-Native Platforms*. TMS earns the slot because (a) JioMart is the marquee Reliance deployment of the platform, (b) the platform is genuinely AI-native at the routing, slot-allocation and order-capture layers, and (c) the deck's framing is *"Quick Commerce OS"* — distinct enough from agentic auto (Boltic/PixelBin/Ratl) and agentic commerce (Kaily) to earn its own suffix in the mega-menu.

---

## §2 · Source inventory

| File | Type | Pages / slides | Key facts derivable |
|---|---|---|---|
| `Fynd TMS Sales Deck - Final.pptx` | 40-slide product deck | 40 | Modules (Control Tower, Rider App, Live Tracking, Precision Zones, AI Route Optimization, Slot-Based Delivery, Quick Commerce OS), customer stories (JioMart, West Elm + Pottery Barn, Sleep Company, Netmeds), upcoming features, implementation roadmap, pricing |
| `Fast delivery at scale—JioMart … 1000+ locations with Fynd.pdf` | Customer story · JioMart | 1 page | JioMart 1000+ locations · 95% on-time · 100% uptime since launch · 3× order capacity · 60% reduction in manual coordination · 40% faster dispatch |
| `Shipping simplified—West Elm cuts operational pain points by 80% with Fynd TMS.pdf` | Customer story · West Elm (RBL) | 1 page | West Elm India (RBL) · Delhi NCR + Mumbai + Hyderabad + Ahmedabad · 90% on-time · 80% fewer clicks · 80% drop in operational pain points · 40% faster dispatch · 85% automation of shipment tasks · DRI Divyendu Behera (RBL SCM), Ravi Patere (RBL Furniture Pan-India) |

**Reliance entities named:**
- **JioMart** (RRVL) — quick commerce, 1000+ locations
- **RBL · West Elm** — furniture, 4 cities (Delhi NCR, Mumbai, Hyderabad, Ahmedabad)
- **RBL · Pottery Barn** — paired with West Elm in deck slide 28
- **Netmeds** (Reliance Health) — medicine quick-delivery in deck slide 27 (supporting proof point only — no telemetry shared)

**Fynd people named (deck slide 3):**
- **Salman Saudagar** — COO, Jio Platforms (Fynd-side Reliance lead)
- **Kushan Shah** — CTPO, Supply Chain & Engineering Productivity (TMS owner)
- **Jigar Dafda** — CTPO, Commerce / AI / Emerging Platforms

---

## §3 · Page structure

Single page at `/tms`. Hand-authored from the SwapEasy template (which cleanly demonstrates the canonical §0–§06 ordering). No sub-pages.

| § | Title pattern | Content |
|---|---|---|
| 0 | Hero | Eyebrow: *"AI-Native · Quick-commerce OS · Live across JioMart + RBL · West Elm · Pottery Barn"*. H1: *"Fynd TMS."* Subhead: 3 sentences naming JioMart 1000+ locations, RBL 4-city furniture fleet, and the AI route-optimization core. Status pills: Live · Building · Roadmap. Stat tiles: 4 — JioMart locations live, JioMart on-time rate, RBL pain-point drop, JioMart system uptime. |
| 01 | Status · Apr-2026 | 3-column Live / Building / Roadmap strip. Live: JioMart + RBL deployments and operating numbers. Building: upcoming features from deck slide 30 (Live Costing, AI Conversational Analytics, Offline rider mode, Invoicing & Reconciliation). Roadmap: international rollout (deck pricing covers India, SEA, MENA), Quick Commerce OS adjacencies (WMS, OMS, dark store). |
| 02 | What's live for Reliance today | Module table (5 rows): Control Tower · Rider App · Customer Live Tracking · Precision Delivery Zones · AI Route Optimization. Each row: status pill + Reliance entity it runs for + anchor outcome. |
| 03 | Architecture · 4 layers | Layered card diagram: ① Order ingestion (OMS / ERP / POS / email-AI) → ② Routing brain (precision polygons + AI route opt + slot allocation) → ③ Execution surface (Control Tower for dispatch + Rider App for fleet + Live Tracking for customer) → ④ Reliance integrations (SAP POS, JioMart sales channels, RBL store ops). |
| 04 | Deep dive · two Reliance deployments | Two side-by-side cards. **JioMart card**: hero number 1000+ locations · 95% on-time · 100% uptime · 3× order capacity · 40% faster dispatch · 60% less manual coordination · 95% routine tasks automated · 50% fewer support inquiries. **RBL · West Elm + Pottery Barn card**: 4 cities (Delhi NCR, Mumbai, Hyderabad, Ahmedabad) · 90% on-time · 80% fewer clicks · 80% pain-point drop · 40% faster dispatch · 85% shipment automation · named DRIs Divyendu Behera + Ravi Patere. Each card carries a `Source · Fynd customer story · 2026` eyebrow per the honesty rule. |
| 05 | In flight · upcoming features | Six in-flight workstreams from deck slide 30: AI Conversational Analytics · AI-Driven Order Integration (email → TMS) · Live Costing & Serviceability · Offline rider support · Invoicing & Reconciliation · Map-pinned task UI. Each card: name + 1-line description + Building pill. |
| 06 | (skipped) Vision / Roadmap | **Override** — single-page section with the honesty contract sitting in §02 module table itself. The deck's "TMS of the Future" cards are absorbed into §05 In flight. (Recorded as D2 below.) |

**No §07 Research, no §08 Sources block** — the page itself is the artefact, eyebrow citations cover provenance per the tone-of-voice rule on default-no Sources blocks.

---

## §4 · Data model

Single-page section. No YAML; copy lives directly in `tms/index.html`.

**Stat-tile schema (mental model only):**
- `label` (cap-num style)
- `value` (display-2)
- `context` (small grey, optional, ≤8 words)

**Module-row schema (§02 table):**
- `module` — display name
- `status` — Live | Building | Roadmap
- `live_for` — which Reliance entity / scope
- `anchor_outcome` — single number that proves it works

---

## §5 · Asset pipeline

Six images from the deck (40 slides) + one cover from the JioMart PDF. All resized to ≤1600px wide, JPEG q80, written into `assets/tms/`.

**To extract from `Fynd TMS Sales Deck - Final.pptx`:**

1. `cover.jpg` — slide 1 (deck title slide) OR slide 9 (modules overview). Pick whichever reads cleaner at thumbnail.
2. `01-control-tower.jpg` — slide 10 (Control Tower mockup)
3. `02-rider-app.jpg` — slide 11 (Rider App mockup)
4. `03-live-tracking.jpg` — slide 12 (Customer Live Tracking)
5. `04-precision-zones.jpg` — slide 19 (Precision Delivery Zones polygon mock) OR JioMart PDF page 1 polygon screenshot — pick whichever is sharper
6. `05-ai-route.jpg` — slide 20 (AI Route Optimization)

Pipeline:
```bash
# 1. Convert deck to PDF (soffice missing locally; ask user OR install LibreOffice OR use cloud)
# Workaround: use python-pptx to extract slide images directly
.venv/bin/python tools/scratch/extract_tms_slides.py
# (writes assets/tms/raw/<slide>.png — then resize via PIL to <descriptor>.jpg q80)
```

**No GCS mirror.** ≤7 images, well under the 20-file / 100MB threshold. Local `assets/tms/` only.

---

## §6 · Navigation wiring

Six entry points per `references/nav-wire-checklist.md`. **Lazy strategy** for v0.1 (home + mega-menu + IP catalog + the new page itself); footer "Other tracks" sweep deferred to v0.2 unless the user requests strict.

| Edit | Path | Status |
|---|---|---|
| Home page card | `index.html` | **Required.** Add TMS card under AI-Native cluster. |
| Top-nav · Tracks · AI-Native column | every page with topnav (~25 files) | **Strict required** for the link to appear in mega-menu — append between Kaily and Recent Innovations divider with `<span class="mono-suffix">QC OS</span>`. |
| Top-nav · More | n/a | Not a meta-page; skip. |
| IP Catalog (`/catalog`) | `catalog/index.html` | **Required.** Add TMS entry. |
| Footer "Other tracks" | every track page | **Deferred** to v0.2. Note in commit. |
| Sibling indexes | n/a | No sibling currently mentions TMS. |

**Mega-menu sweep:** `grep -rl 'mega-link">Kaily' --include='*.html'` to find every page that needs the AI-Native column updated.

---

## §7 · Build / verify

Single-page section, no renderer. Hand-author `tms/index.html` from `swapeasy/index.html` as template (closest shape: hero + status + modules + how-it-works + deep-dive + in-flight, no §06 vision).

```bash
# Local verify
python3 -m http.server 8000
# open http://localhost:8000/tms
# bypass auth: sessionStorage.setItem('fyndrrl_auth_v1', '1'); location.reload();
```

Walk the §9 verify checklist from `website-section-authoring`. After v0.1 lands, run `website-page-reviewer` skill against `/tms` for an independent audit.

---

## §8 · Phased delivery

| Phase | Hours | Deliverable |
|---|---|---|
| P1 | 1.0 | Spec written, signed off |
| P2 | 0.5 | Slide images extracted to `assets/tms/` |
| P3 | 1.5 | `tms/index.html` hand-authored from SwapEasy template |
| P4 | 0.5 | Nav wire (home + ~25-file mega-menu sweep + IP catalog) |
| P5 | 0.5 | Local verify + Chrome DevTools screenshot pass |
| P6 | 0.5 | website-page-reviewer audit + ship resolutions |

Total: ~4.5 hours.

---

## §9 · Decisions

- **D1 · Reliance anchor** — JioMart-led (quick-commerce hero). Hero leads with JioMart 1000+ locations + 10–30 min promise. RBL West Elm/Pottery Barn (4 cities, furniture) and Netmeds (Reliance Health, supporting only) fill out the deployment story. Why: JioMart is the marquee Reliance entity Apex recognises immediately and the case-study numbers are the most quotable. *How to apply:* every hero stat tile and the §04 deep-dive lead are JioMart numbers; RBL is co-equal in §02 module table and §04 second card.
- **D2 · Honesty pills · Live · case-study eyebrow → upgraded to Live (canonical)** — User chose to mark JioMart 1000+ locations / 95% on-time / 100% uptime and RBL 90% on-time / 80% pain-drop as Live-today numbers, citing the published Fynd customer stories as canonical sources. *How to apply:* status pills read `Live` not `Live · case study`. Each customer-story card still carries an eyebrow `Source · Fynd customer story · 2026` so the apex reader can trace the number, but the pill itself is unqualified Live.
- **D3 · Mega-menu suffix · "quick-commerce OS"** — TMS sits in the AI-Native column with `<span class="mono-suffix">QC OS</span>` instead of `agentic auto` or `agentic commerce`. Why: the deck's own framing (slide 16–25) is "Quick Commerce OS"; it's distinct from the Boltic/PixelBin/Ratl automation cluster and from Kaily's commerce surface. *How to apply:* every nav update uses `QC OS` exactly; do not introduce a competing suffix.
- **D4 · Section ordering override · skip §06 Vision** — Single-page section earns a leaner shape. The honesty contract sits in §02 module table + §04 deep-dive cards; the deck's "TMS of the Future" content is absorbed into §05 In flight. Why: register-wide guidance for small pages says drop §06 when the §02 table carries the contract. *How to apply:* page ends at §05 In flight + footer.
- **D5 · No §08 Sources block** — Per tone-of-voice default-no rule. Provenance lives inline (eyebrow citations on §04 cards) and in this spec file. *How to apply:* do not append a Sources card list at the bottom.
- **D6 · No author / version line in hero or footer** — Per register-wide rule. Crumb + section-label + H1 + subhead is enough orientation. Footer is the single copyright line. *How to apply:* copy footer block verbatim from `swapeasy/index.html`.
- **D7 · Lazy nav-wire** — Footer "Other tracks" lists on ~12 sibling track pages are NOT updated in v0.1. Backlinks lag. Will sweep in a follow-up commit if Apex review surfaces the omission. *How to apply:* commit message must say "lazy nav: home + mega-menu + IP catalog only".
- **D8 · Section ordering override · merge §03 Architecture into §02** — User feedback round 1 collapsed the standalone §03 Architecture section into §02 What's live. The 4-layer architecture frame remains as a compact strip at the top of §02, then the 5 live module cards each carry a `Layer NN` eyebrow that maps them to the architecture. The 5 modules previously sat as a screenshot strip inside §04 Deep dive; that strip moved into §02. Why: removed double-counting (modules were named once in the §02 table and once in the §04 strip; layers were described once in §03 and again in §02 by implication). Apex reads "what's live" as a single coherent block instead of three. *How to apply:* page-structure now hero · §01 Status · §02 What's live (4 layers + 5 modules + QC OS) · §03 Deep dive · §04 In flight. Section-label run is contiguous 01-02-03-04. Reference: feedback round 1 commit on 2026-05-01.
- **D9 · Netmeds elevated to third deployment card** — Round 2 feedback: Netmeds was buried in two body bullets, missing from the hero, the status pill, and §03 deep-dive. Now surfaced in five places: page title, hero eyebrow, hero subhead, hero status pill, and a dedicated third deployment card in §03. Why: Netmeds is one of three Live Reliance deployments per the deck source (slide 27); under-surfacing it understated the platform's Reliance footprint. *How to apply:* §03 deep-dive grid is now `lg:grid-cols-3` (was `lg:grid-cols-2`); title changed from "two Reliance deployments" → "three Reliance deployments". Netmeds card is qualitative-only (no fabricated operating numbers — the deck source is qualitative). Card carries an explicit "Honesty note" stating the telemetry pull is in flight. Reference: feedback round 2 commit on 2026-05-01.
- **D10 · Section ordering override · drop §01 Status entirely** — Round 3 feedback: §01 "What's running. What's being built. What's next." was a TOC of the rest of the page. Every bullet in its three columns was already present downstream — Live column = §02 module cards + hero stat tiles; Building column = §03 In flight cards (5 of 6 verbatim); Roadmap column = hero status pill + §02 bonus QC OS card. Apex reads §01 as filler. Dropped entirely; the useful synthesizing line ("Fynd TMS is the transport spine for three Reliance delivery models...") moved into §02 as the intro paragraph. Hero now does §01's job — 4 stat tiles + 3 Live/Building/Roadmap pills + subhead naming all three Reliance entities. *How to apply:* sections renumbered §02→§01, §03→§02, §04→§03. Section-label run is now contiguous 01-02-03. Internal cross-references (`see §04` → `see §03`, `§01 Roadmap` → `hero status pill above`) updated. Page reduced from 5 sections to 4. Reference: feedback round 3 commit on 2026-05-01.

---

## §10 · Out of scope

- Pricing tables (deck slides 37–39: India ₹ / SEA $ / MENA $) — these are commercial collateral for prospects, not register material for Apex.
- The Sleep Company case study (deck slide 26) — non-Reliance customer; pulls focus from JioMart + RBL.
- Implementation roadmap (deck slide 31) — supplier-side process, not register-relevant for the Apex reader.
- Security & Compliance grid (deck slide 34) — generic boilerplate; if Apex requests later, port the live `/hirefirst` Governance pattern instead.
- Pricing / cost-recovery tiles in the hero — banned construction per tone-of-voice §3.
- "ROI payback" tiles — banned per tone-of-voice §3.
- Quick Commerce OS sister modules (WMS, OMS, dark-store display, deck slides 17–25) — listed as Roadmap adjacencies in §01 only; not separately deep-dived. The page is about TMS, not the broader QC OS suite.

---

**Built by Fynd. Owned and run by Reliance.**
