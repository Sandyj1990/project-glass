---
section: kio
route: /kio
status: drafting v0.1
owner: Kushan Shah (Fynd)
audience: RIL Apex leadership (MM Sir level)
narrative anchor: |
  Farooq's 30-Apr-2026 MDA letter does NOT list Kio in the platform inventory. Home /
  index.html and /catalog already reference it (Pilot Malad, 168 units locked Fashion
  Factory, ~₹18 Cr FY26-27). The /kio page closes that gap: a single-page register
  entry for the Physical-AI checkout hardware track that anchors Fashion Factory
  rollout and the SnacAdda internal lab.
---

# /kio · spec · v0.1

Single-page section. Hand-authored `kio/index.html` (no renderer — content fits in 6 sections).

---

## §0 · Why this page exists

**Gap to close.** The home page register (line 312) and the IP catalog (lines 182-187) both name *Fynd Kio*, *SwiftScan*, *Fynd Swift Module*, and *SnacAdda* as Live IPs — but there is no `/kio` route to expand them. Apex review of those rows leads nowhere.

**Audience.** RIL Apex leadership (MM Sir level). Reads top-to-bottom in seconds. Wants: what is live, who runs it, what number proves it. Hardware claims must be specs-grade, not marketing-grade.

**Narrative anchor.** Physical AI bucket (home line 774): *"Edge Labs · Kio (production) · AutRi · Onshelf · Horizon (MDA Apr 14)."* /kio is the production entry in that bucket. The Annual Plan 2026-27 already books the hardware revenue line (~₹18 Cr).

---

## §1 · Source inventory

| Source | Path | Key facts derivable |
|---|---|---|
| Fynd Kio.pptx (16 slides) | `docs/kio-notes-compilation/Fynd Kio.pptx` (29 MB · gitignored after extraction) | Kio Series positioning · 3X faster checkout · 4 model variants (Wall · Standing · Tabletop · Bin) · 2 hardware platforms FKAP1/FKAP2 · peripherals · RFID accessories · SnacAdda case study · 3 verticals (Fashion · Beauty · Grocery) |
| Extracted slides | `docs/kio-notes-compilation/extracted/slides.md` + `slides.json` | Verbatim slide text + image manifest (24 slide images extracted) |
| Home page register | `index.html:312` | Pilot Malad · 168 units locked Fashion Factory · ~₹18 Cr FY26-27 · 3× faster than POS |
| IP Catalog | `catalog/index.html:182-187` | Fynd Kio · SwiftScan (21.5/27" · <15 sec checkout) · Fynd Swift Module (OTA) · SnacAdda DRIs |
| MDA letter | `docs/2026-04-30-farooq-mda-update-letter.md` | Kio NOT named in the platform list. Implicit under Physical AI / Recent Innovations. **Treat as gap evidence — page documents what the letter omits.** |
| Accenture deck | `docs/accenture-2026-04-16-compilation/INDEX.md` | Kio NOT in the 23-topic index. Same gap. |

---

## §2 · Page-structure (canonical ordering)

Single-page section. No sub-pages. Follows the canonical 0→08 ordering with overrides documented in §9 Decisions.

| § | Title | Content |
|---|---|---|
| **0** | Hero | Crumb + section-label + H1 *Kio.* + 2-line subhead + 3 status pills (Live · Building · Roadmap) + 4 stat tiles (Pilot stores · Locked units · Hardware line · Verticals) |
| **01** | Status (01-May-2026) | 3-col Live / Building / Roadmap strip — what's running today across Malad + SnacAdda · what's in flight (Fashion Factory rollout · Swift Module OTA hardening) · what's on the roadmap (additional verticals · RFID-bin upgrade) |
| **02** | What is live | Module table — Kio Series hardware · Swift Module (OTA) · SnacAdda lab · with status / DRI / anchor outcome |
| **03** | Hardware architecture · 4 layers | Edge compute (FKAP1/FKAP2 SoC) · Display (21.5″ FHD) · Peripherals (scanner · printer · LEDs · RFID) · Software stack (Android/Linux + StoreOS + FSM) |
| **04** | Deep dive · Model variants + peripherals | Visual cards for the 4 model variants (Wall · Standing · Tabletop · Bin) and the RFID accessories (Hard Tag Remover · Pin Collector · Bin 40-100L). Slide 8 + slide 7 imagery. |
| **05** | In flight · this quarter | Threads in active execution — Fashion Factory 168-unit shipment · Swift Module OTA hardening · vertical pilots beyond Fashion |
| **06** | SnacAdda · internal lab case study | Slide-14 verbatim: WeWork Andheri · 50+ items/min · FSM diagnostics · OTA updates. Slide-15/16 product-shot evidence. |
| **07** | Specifications | Two specs tables verbatim from slides 10 + 12 (FKAP1/FKAP2 SoC + display/power) |
| ~~08~~ | Sources | Skipped — single source artefact (Fynd Kio.pptx) cited inline in eyebrows. Apex-page Sources block default-no rule. |

---

## §3 · Data model

Single page · single YAML at `data/kio/kio.yaml`. Schema:

```yaml
slug: kio
title: Kio
status: live
date: 2026-05-01
source_folder: docs/kio-notes-compilation/
source_citation: "Fynd Kio.pptx · 16 slides · extracted 01-May-2026"

hero:
  eyebrow: "Track · Physical AI · Self-checkout hardware"
  h1: "Kio."
  subhead: |
    Self-checkout kiosk hardware for retail. Pilot live at Malad; 168 units locked
    for Reliance Retail Fashion Factory rollout (~₹18 Cr FY26-27 hardware line).
    3× faster than manned POS. Built on Fynd Swift Module for OTA fleet management.

stats:
  - label: "Pilot stores"
    value: "Malad"
    context: "live · production hardware"
  - label: "Locked units"
    value: "168"
    context: "Fashion Factory · FY26-27"
  - label: "Hardware line"
    value: "~₹18 Cr"
    context: "FY26-27 · Reliance Retail"
  - label: "Verticals"
    value: "3"
    context: "Fashion · Beauty · Grocery"

modules:
  - name: "Kio Series hardware"
    status: live
    dri: "Salman Saudagar · Naveen"
    outcome: "FKAP1 + FKAP2 platforms · 4 model variants · 21.5″ FHD touch · 3× faster checkout vs manned POS"
  - name: "Fynd Swift Module"
    status: live
    dri: "Robotics team"
    outcome: "OTA fleet management · firmware push · diagnostics · running across deployed fleet"
  - name: "SnacAdda · internal lab"
    status: live
    dri: "Bharat K · Aarav · Lalit · Smit · Adnan"
    outcome: "WeWork Andheri · 50+ items/min · FSM diagnostics validated"

variants:
  - "Wall Mounted Kiosk"
  - "Standing Kiosk"
  - "Table Top Kiosk"
  - "Bin Kiosk"

# specs tables: copied verbatim from slides 10 + 12
```

---

## §4 · Asset pipeline

**Extraction.** Already done — `tools/scratch/extract_kio.py` ran 01-May-2026, output to `docs/kio-notes-compilation/extracted/images/` (24 images extracted across 16 slides).

**Web-ready selection.** Pick ~6-8 images that earn their place:
- `cover.jpg` — slide-3 product hero (1034 KB · `slide_03_324a91aaf9.png`)
- `01-three-step.jpg` — slide-4 3-step checkout flow (composite or single best frame)
- `02-verticals.jpg` — slide-5 vertical applications
- `03-peripherals.jpg` — slide-6 peripherals layout
- `04-rfid-accessories.jpg` — slide-7 RFID bin accessories
- `05-variants.jpg` — slide-8 4 model variants
- `06-modular.jpg` — slide-9 modular construction
- `07-snacadda.jpg` — slide-15 or slide-16 SnacAdda product shot

**Sizing.** `sips -Z 1600 -s format jpeg -s formatOptions 80` → write to `assets/kio/`.

**GCS mirror decision.** ~7 images at ~200 KB each = ~1.4 MB total. Below the 20-file / 100MB threshold. **Keep local under `assets/kio/`** — no CDN mirror required for v0.1. Re-evaluate at v0.2 if image count grows.

---

## §5 · Navigation wiring

Six sites to touch:

1. **Home `index.html`:323** — wrap "Fynd Kio" line in `<a href="/kio">…</a>` (currently plain text)
2. **Home `index.html`:712** — Fashion Factory card "Companion + 168 Fynd Kio units" — wrap "Fynd Kio" link
3. **Home `index.html`:774** — Physical AI bucket card mentions "Kio (production)" — link
4. **Catalog `catalog/index.html`:182** — wrap "Fynd Kio (Self-Checkout Kiosk)" with link
5. **Top-nav mega-menu** — add `<a href="/kio">Kio <span class="mono-suffix">Physical AI</span></a>` under **Recent Innovations** column (sits next to Autri, Fynd Horizon, Dark Factory). Lazy strategy: home + new section only for v0.1; full ~25-file mega-menu sweep deferred.
6. **Footer "Other tracks" lists** — defer (lazy strategy)

---

## §6 · Build / verify

Hand-authored `kio/index.html`. No renderer. Use `granary/index.html` topnav + footer + style conventions verbatim.

```bash
mkdir -p kio assets/kio
# write kio/index.html
python3 -m http.server 8000
# DevTools: sessionStorage.setItem('fyndrrl_auth_v1','1'); location.reload();
# open http://localhost:8000/kio
```

Verify per §9 of website-section-authoring.

---

## §7 · Phased delivery

| Phase | Hours | Deliverables |
|---|---|---|
| P1 (this commit) | 2 | spec · YAML · extract images · `kio/index.html` v0.1 · home + catalog link wiring · mega-menu Recent Innovations link |
| P2 | 1 | website-page-reviewer audit pass · fix findings |
| P3 (later) | 1 | Full mega-menu sweep across ~25 sibling pages once Kio nav is settled |

---

## §8 · Decisions

**D1 · Live status.** Hero carries Live pill. Pilot Malad is live; 168 Fashion Factory units are *Locked* (= contract booked, shipping in flight). Use the same phrasing the home register already uses; do not soften to Pilot-only.
- **Why:** user confirmed via AskUserQuestion 01-May-2026; matches home + catalog claims.
- **How to apply:** Live pill in hero. *Locked units* tile uses neutral language; the Fashion Factory shipment shows up under §05 In flight as Building.

**D2 · Page scope.** Consolidated — Kio kiosk hardware + Fynd Swift Module (OTA software) + SnacAdda internal lab on the same page.
- **Why:** user confirmed; matches what the source pptx itself bundles. SwiftScan remains a separate catalog row pointing to the same `/kio` page.
- **How to apply:** Three modules in §02. SnacAdda gets its own §06 case study section.

**D3 · No Reliance counterpart named.** Page entity is *Reliance Retail · Fashion Factory*. No individual Reliance leader named.
- **Why:** user confirmed counterpart not yet known; do not invent one.
- **How to apply:** Stat tiles + body copy use *Fashion Factory* and *Reliance Retail* as entities. DRI footer line carries Fynd-side owners only (Salman Saudagar · Naveen).

**D4 · Section ordering override.** Skip §08 Sources block. Single source (the pptx) cited inline in eyebrows.
- **Why:** Apex-page Sources default-no rule (website-tone-of-voice §3); the page is the artefact, the spec records provenance.
- **How to apply:** No §08 section. Inline `cap-num` source eyebrows where claims need backing.

**D5 · Hardware-spec section is honest specs-grade, not marketing.** §07 carries the FKAP1/FKAP2 SoC table and display/power table verbatim from slides 10 + 12. No reinterpretation.
- **Why:** Apex reads hardware specs as truth; any softening reads as evasion.
- **How to apply:** Verbatim table copy from `slides.md`. No editorialising of clock speeds, NPU TOPS, RAM, OS versions.

---

## §9 · Out of scope

- SwiftScan as a separate page (catalog row continues to point at `/kio`).
- Granular Annual-Plan 2026-27 financial breakdown (the ~₹18 Cr line is the only number cited).
- Vertical-specific pilot details for Beauty + Grocery (page lists them; deep-dive deferred until pilots exist).
- Full ~25-file mega-menu sweep — deferred to P3.
- 27" SwiftScan variant tile-by-tile coverage (mentioned in spec table as derivable from catalog row but not surfaced as a hero tile in v0.1).

---

**End of spec · v0.1 · 01-May-2026.**
