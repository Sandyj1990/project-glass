# Fynd Horizon · Page Spec

| | |
|---|---|
| **Status** | v0.1 · authoring in progress |
| **Owner (Fynd)** | Salman Saudagar (COO) |
| **DRI (Fynd-side, Horizon)** | Yash Singh |
| **RIL counterpart** | Reliance Trends · RCP cluster · Mumbai cluster |
| **Route** | `/fynd-horizon` |
| **Source content** | `docs/fynd-horizon-notes-compilation/` (D02 deck · 18 slides · 2026-04-27) + `docs/2026-04-30-farooq-mda-update-letter.md` (Farooq → MM Sir) + `docs/accenture-2026-04-16-compilation/` slide 29 (Accenture pitch) |
| **Narrative anchor** | Farooq's 2026-04-30 MDA letter names "Recent Innovations · Fynd Horizon and Autri" as one of the dedicated pillars Apex needs to see. Today's `/fynd-horizon/` is a stub — this spec elevates it to a v0.1 register entry. |

---

## §0 · What's changing and why

This is a **new section** going from a placeholder hub to its first content drop. The trigger is two-fold:

1. The 2026-04-30 letter to MM Sir explicitly lists Fynd Horizon as a Recent Innovations pillar. The placeholder currently reads *"Page in progress · Hub page coming soon"* — that lands flat in front of Apex.
2. The D02 deck (Apr 27, 2026) is the first internally-aligned, slide-grade artefact for Horizon. It maps the strategic shift, the in-store hardware kit, the user journey, the AI-native layer, the fit-selection paths, and a benchmark vs Uniqlo/Shein/Zara. Plus a "Mathematics Behind Measurements" CEO brief that explains the depth-sensing math at a level Apex can follow.

Live status to the customer: **RCP store · 31-Mar-2026** · **Mumbai cluster · 27-Apr-2026**. So the page is not vapourware — it ships with a live deployment and a published benchmark.

---

## §1 · Why this page exists

**Audience.** RIL Apex leadership (MM Sir level) reading the 2026-04-30 update letter. Secondary: anyone in RIL corporate strategy or Trends ops trying to understand what "Fynd Horizon" actually is and why it merits its own line in the cover letter.

**Gap to close.** The cover letter names Horizon but the linked register page is empty. Apex clicking through gets nothing — a credibility hit for the whole register.

**Narrative anchor.** *"Ultra Fast Retail. Made-to-Order in 24 Hours."* (D02 cover). Horizon decouples retail from inventory: scan → try-on → buy → manufacture → deliver, in the same store, in the same day, with zero stock risk. The strategic frame is: Trends today displays ~2,000 SKUs per store and customers walk out when their size/colour isn't on the floor. Horizon turns the same 2,000 sq ft into 50,000+ SKUs by replacing physical inventory with a measure-perfect virtual try-on tied to a 24-hour MTO factory in Tirupur.

---

## §2 · Source inventory

| File | What's in it | Use for |
|---|---|---|
| `docs/fynd-horizon-notes-compilation/Fynd_Horizon_D02.pptx` (18 slides · 27-Apr-2026) | D02 master deck. Slides 1-2 cover/exec; 3-4 strategic shift + business case; 5-11 user journey (steps 0-5); 12 in-store hardware kit; 13 VTO experience; 14 AI-native layer; 15 fit selection (standard vs measure-perfect); 16 benchmark table; 17 sector divider; 18 vision. | All copy + benchmark table verbatim |
| `docs/fynd-horizon-notes-compilation/Mathematics_Behind_Measurements_Final.pdf` (2 pp · CEO Brief · May 2026) | Three-pillar math explanation: 17-keypoint pose estimation, depth-sensing pixel→world conversion, Ramanujan ellipse approximation for circumferences. ±1 cm accuracy claim. | §07 Research artefact (embed or download) |
| `docs/fynd-horizon-notes-compilation/IMG_2416.jpeg` | Photo of an actual Fynd Horizon LED wall installation at a Trends store · LED wall renders the Infinite Aisle catalog grid + a model in store · "Fynd Horizon" branded sign on the right. Real installation, not a render. | Hero / §02 evidence shot |
| `docs/fynd-horizon-notes-compilation/image (117).png` | Screenshot of Infinite Studio admin dashboard · "Weekly Performance Report · Apr 24 → May 1, 2026" · 178 try-ons / 17 today / 58% completion / 103 looks / 25% engagement / ₹1358 est profit · 14-day activity trend · key highlights (registered users / VTO looks / videos / measurements taken) · peak hours · size distribution · recent sessions. | §05 evidence shot for AI-native layer (the operator surface that proves the metering claim) |
| `docs/2026-04-30-farooq-mda-update-letter.md` | Cover letter to MM Sir naming Fynd Horizon under "Recent Innovations". | Eyebrow / framing |
| `docs/accenture-2026-04-16-compilation/INDEX.md` §12 (slide 29 · 6 images) | Accenture-deck pitch for Apparel Infinite Studio: ">98% accuracy via Intel RealSense", "Gemini Cloud Rendering · Physics-accurate fabric rendering under 2s", "Infinite Aisle · 2k → 50k+ SKUs". | Cross-reference for the same numbers · enables sources card with two independent citations |

**Image extracts** (`tools/scratch/horizon_extract/` · 78 PNG/JPG from the pptx · sized for inspection only). The two non-decorative ones we'll re-publish:

- `slide_07_img_05.png` (1.6 MB · 14-product Trends Infinite Aisle catalog grid screenshot · §03 user journey, Step 1 Browse evidence)
- `slide_12_img_07.png` (700 KB · LED-wall + iPad render of in-store hardware setup · §04 hardware kit illustration)

---

## §3 · Page structure

Single-page section (no sub-routes). Hand-authored — well under the 6-section / renderer threshold. Convention: canonical §0-§08 ordering from website-section-authoring §4. Two override calls (recorded as Decisions D2 and D3 in §9).

### §0 · Hero

- Crumb: Home / Fynd Horizon
- Section-label: `Recent Innovations · Made-to-Order in 24 Hours`
- H1: `Fynd Horizon.`
- Subhead (1 sentence): `Ultra Fast Retail. The same Trends store, 25× the SKUs, made-to-measure in 24 hours — with zero inventory risk.`
- Status pills: `Live · RCP cluster · 31-Mar-2026` · `Live · Mumbai cluster · 27-Apr-2026` · `Building · Tirupur MTO factory · cycle live since 25-Mar-2026`
- Stat tiles row (4):
  - SKUs available · `50,000+` · all from JCP unified catalog
  - vs Trends today · `~2,000` · per-store displayed today
  - Body-measurement accuracy · `98.3%` · vs Bodygram, n=200
  - Order → doorstep · `30 min / 24-48 hr` · standard / made-to-order
- Hero image strip: full-width photo (`IMG_2416.jpeg`) of the actual installation — proves "live" beyond a screenshot.

### §01 · Status (27-Apr-2026)

3-column Live / Building / Roadmap strip. Lifted from the deck's status framing.

- **Live** — RCP store live to customers since 31-Mar-2026 · Mumbai cluster live 27-Apr-2026 · Tirupur partner factory MTO cycle running since 25-Mar-2026 · Infinite Studio admin live (178 try-ons in week of 24-Apr → 1-May)
- **Building** — store-by-store rollout across Mumbai cluster · demand-prediction agent (next-3-outfit forecast feeding tonight's pre-cut) · token-economics dashboard for AOV vs cost-per-session
- **Roadmap** — pre-cut pipeline at scale (target: factory yield +18% by Q2 2026) · expansion beyond Mumbai cluster · self-healing rendering on-call rotation hardened

### §02 · The strategic shift · current → future

The "before vs after" frame from D02 slides 3-4. Two-column comparison:

| Lens | Trends today | Horizon |
|---|---|---|
| Inventory | ~2,000 SKUs displayed per store · physical only | 50,000+ SKUs available · all virtual via JCP catalog |
| Inventory risk | Markdown risk on every garment · 45 days holding | Zero · only manufacture what is sold · 0 days holding |
| Returns rate | 8.5% online · sizing-driven | <2% target · deep-tech fit eliminates sizing returns |
| Fulfilment | Pull from shelf / 48 hr | 30 min (dark store) or 24-48 hr (MTO factory) |
| Revenue density | Limited by floor sq ft | 25× reach from same footprint |

Closing strap-line: *"Strategic Shift: Ultra Fast Retail powered by automated factories that turn orders into products in 24 hours."*

### §03 · User journey · 6 steps

End-to-end flow at any Horizon-enabled Trends store. Five customer steps + Step 0 (body scan). Card grid, 6 cards. Each card carries: step number, name, customer-experience line, deep-tech caption, and (for steps 1+2) an embedded screenshot.

| Step | Customer experience | Deep tech behind it |
|---|---|---|
| **0 · Body Scan** | 3-click profile (selfie + front-full + side-full) · captures shoulder/chest/waist/inseam + posture/volume | Intel RealSense depth + SMPL parametric model · >98% accuracy under clothing |
| **1 · Browse** | 50K+ styles from JCP catalog · filter by occasion/colour/trend/price · single tap to add to try-on queue | Catalog from Fynd UNO · live sync with brand inventory |
| **2 · Try** | See garment on your own body, not a model's · best-fit recommendation · mix & match outfits in seconds | Gemini Cloud Rendering · physics-accurate drape · <2 s render |
| **3 · Buy** | One-tap checkout · "Manufacturing Started" status · live track from "Order Placed" → "Cutting Fabric" | Unified OMS · factory API integration · real-time fabric availability check |
| **4 · Make** | Garment manufactured from scratch · 24-hour turnaround · precision-stitched to spec | Automated laser cutting · robotic sewing lines · AI-CV defect detection |
| **5 · Deliver** | 30 min (dark store) or 24-48 hr (factory) to doorstep · Perfect Fit Guarantee — remake free if it doesn't fit | Route optimisation · automated sorting · predictive logistics |

Footer strap: *"Catalog from Fynd UNO · Rendering QA by Ratl · Order routing through JCP."* — anchors the platform integration.

Embed `slide_07_img_05.png` (Infinite Aisle catalog grid) inside Step 1; embed `slide_12_img_07.png` (LED-wall render) as the section header visual.

### §04 · In-store hardware kit

Plug-and-play. ≤6 hours per store. Standardised SKUs · zero local config.

5-card grid:

| Component | Spec |
|---|---|
| LED Wall | 16 ft × 8 ft 4K · life-size mirror |
| iPad Pro 12.9″ | Catalog browse · checkout · staff control |
| Intel RealSense D555 | Dual depth cameras · 3D body scan |
| Edge Compute Box | Local inference fallback · 90 s warmup |
| 48 MP WebCam | Full-body picture |

### §05 · AI-native layer

The three "predicting the future, not reflecting the past" agents from D02 slide 14. Each card: title, what it does, three-bullet how-it-works, target metric.

| Agent | What it does | Target / threshold |
|---|---|---|
| **Demand prediction** | Predicts customer's next 3 outfits from scan + browse history. Surfaces top-12 looks before customer asks. Pre-cuts factory fabric tonight for tomorrow's predicted orders. | Factory yield **+18% by Q2 2026** |
| **Self-healing rendering** | Auto-reviews 100% of VTO renderings every night via Ratl QA agent. Flags photoreal drift > 0.5% to DRI within 1 hour. Catches Gemini cloud regressions before customer impact. | On-call rotation: pages within **5 min** of red flag |
| **Token economics** | Every try-on metered at **₹4.20 / session** today. Profit threshold: AOV must clear **₹780** to break even. Hard cap: 50 try-ons per customer per session. | Per-session profit-positive at every store |

Embed `image (117).png` (Infinite Studio admin dashboard) as evidence — proves the metering loop is real, not aspirational. Caption it as the operator surface.

### §06 · Two fit paths · speed or measure-perfect

D02 slide 15 verbatim. Re-framed from D01's "casual vs formal" to "speed vs measure-perfect" — a deliberate decision worth keeping in the page.

Two-card side-by-side:

**Standard Fit** · Ready to wear · 30 min
- Best-matched standard size from scan (S/M/L/XL)
- Fulfilled from local Trends dark store (Mumbai cluster: 3 stores)
- Inventory pre-positioned (no stockout > 99% time)
- Free returns within 7 days — max 2 per customer (MDA policy)

**Measure-Perfect Fit · Made to Order** · 24-48 hr
- Manufactured to exact body measurements from depth scan
- Tirupur partner factory · automated cut + sew + AI QC
- Pre-cut fabric tonight for tomorrow's predicted orders
- Remake-free guarantee if fit imperfect — owner: factory DRI

### §07 · Benchmarks · vs Uniqlo, Shein, Zara

D02 slide 16 verbatim. *Benchmarked against Uniqlo, Shein, Zara — not against ourselves. Targets are Ratl-verified.*

| Metric | Horizon target | Trends today | Uniqlo Tokyo | Shein on-demand | Zara |
|---|---|---|---|---|---|
| SKU reach / store | 50,000 | 2,000 | ~8,000 | 600,000 (online only) | ~10,000 |
| Returns rate | <2% | 8.5% (online) | ~6% | ~12% | ~10% |
| Order → doorstep (custom) | 24-48 hr | 7 days | n/a (no MTO) | 5-10 days | 14 days |
| Order → doorstep (standard) | 30 min | 48 hr | n/a | n/a | n/a |
| Inventory holding | 0 days (MTO) | 45 days | ~14 days | ~3 days | 14 days |

Benchmark source: Ratl.ai verified study, 18-Apr-2026. Sample: 200 customers across Mumbai + Bangalore + Tokyo. Owner: Pratiksha Kasbe. Data refreshed every 30 days.

### §08 · Research · Mathematics behind measurements

The 2-page CEO Brief PDF embedded inline. Three pillars: 17-keypoint pose estimation, depth-sensing pixel→real-world projection, Ramanujan's ellipse approximation for body circumferences. ±1 cm accuracy · <0.04% formula error · single phone camera + 100-year-old equation = tape-measure-grade body data.

Embed via `<iframe>` for direct read inline (Granary research-section precedent), with download link.

### §09 · Sources

Card list of every file cited.

---

## §4 · Data model

Single-page section · no YAML data layer. All copy lives directly in `fynd-horizon/index.html`. Asset references are absolute paths under `/assets/fynd-horizon/`.

---

## §5 · Asset pipeline

Five web-ready assets to publish, all under `assets/fynd-horizon/`:

| Source | Web target | Process |
|---|---|---|
| `docs/fynd-horizon-notes-compilation/IMG_2416.jpeg` (4032×3024 · 1.8 MB) | `assets/fynd-horizon/01-installation.jpg` | sips · max 1600 px wide · q80 |
| `tools/scratch/horizon_extract/slide_07_img_05.png` (1.6 MB) | `assets/fynd-horizon/02-infinite-aisle.jpg` | sips · max 1600 px wide · q85 PNG→JPG |
| `tools/scratch/horizon_extract/slide_12_img_07.png` (700 KB) | `assets/fynd-horizon/03-hardware-kit.jpg` | sips · max 1200 px wide · q85 PNG→JPG |
| `docs/fynd-horizon-notes-compilation/image (117).png` (640 KB · 3024×1964) | `assets/fynd-horizon/04-infinite-studio-admin.jpg` | sips · max 1600 px wide · q85 PNG→JPG |
| `docs/fynd-horizon-notes-compilation/Mathematics_Behind_Measurements_Final.pdf` (420 KB · 2 pp) | `assets/fynd-horizon/horizon-math-ceo-brief.pdf` | copy as-is (well under 30 MB) |

No GCS mirror needed — five files totalling well under 5 MB. Commit directly.

No PPTX hosting — the 3.5 MB D02 deck stays in `docs/fynd-horizon-notes-compilation/` and is not exposed as a web download (internal-only deck; the page itself is the polished surface).

---

## §6 · Navigation wiring

Already done — `/fynd-horizon` is in the Tracks mega-menu under "Recent Innovations" on every page (the placeholder shipped with nav wiring). Verify only:

- [x] Tracks · Recent Innovations · Fynd Horizon link present and points at `/fynd-horizon`
- [ ] Home page card (`/index.html`) — verify card exists for Fynd Horizon
- [ ] IP Catalog (`/catalog`) — verify entry exists
- [ ] No footer "Other tracks" sweep needed for v0.1 (lazy strategy per skill §8)

---

## §7 · Build / verify

Hand-authored. No renderer. Edit `fynd-horizon/index.html` directly.

Local verify:

```bash
python3 -m http.server 8000
# DevTools console: sessionStorage.setItem('fyndrrl_auth_v1', '1'); location.reload();
# Open http://localhost:8000/fynd-horizon
```

Walk through:
- [ ] Hero loads with installation photo
- [ ] All status pills render
- [ ] All four stat tiles render
- [ ] Strategic-shift table renders
- [ ] User-journey 6-card grid renders + screenshots load
- [ ] Hardware-kit 5-card grid renders
- [ ] AI-native 3-card grid renders + admin dashboard screenshot loads
- [ ] Fit-paths 2-card grid renders
- [ ] Benchmark table renders
- [ ] Math PDF embed loads + download link works
- [ ] Sources cards render

---

## §8 · Phased delivery

| Phase | Scope | Hours |
|---|---|---|
| **P1 · v0.1 ship** (this spec) | Full §0-§09 hand-authored. Five assets published locally. Math PDF embedded. | ~3 |
| **P2 · feedback round 1** | Apex / Salman / Yash / Farooq comments applied. Likely: tighten copy, swap any imagery. | ~1 |
| **P3 · live admin metric refresh** | Replace static "178 try-ons" with a current screenshot taken close to publish date. Optional. | ~0.5 |

---

## §9 · Decisions

| ID | Decision | Why | How to apply |
|---|---|---|---|
| **D1** | Status pill on hero is `Live · RCP cluster · 31-Mar-2026` + `Live · Mumbai cluster · 27-Apr-2026` (no Building/Roadmap pills in hero). | The fact this is *live to customers* is the headline. Building/Roadmap belongs in §01 status strip, not the hero. | Hero pills = live deployments only |
| **D2** | Section ordering override · use §02 "strategic shift" instead of canonical §02 "What's live · module table". | The page's strategic frame *is* the comparison (Trends today vs Horizon). Modules per se are secondary; the user-journey cards in §03 carry that load. | Replace canonical §02 module table with the before/after comparison table from D02 slides 3-4 |
| **D3** | Section ordering override · use §07 "Benchmarks vs Uniqlo/Shein/Zara" instead of canonical §06 "Vision / Roadmap scorecard". | The honesty contract here is *external* benchmark, not internal vision-vs-built. Slide 16 is already the honesty fulcrum — Ratl-verified, named owner, named dashboard. | §07 uses the slide 16 table verbatim with footnote citing Ratl + Pratiksha Kasbe + dashboard URL |
| **D4** | Hero stat tile uses `98.3%` (vs Bodygram, n=200) for accuracy. Math PDF says ±1 cm / <0.04%. | The two numbers measure different things — 98.3% is accuracy of the *predicted body shape* vs ground-truth Bodygram; ±1 cm is geometric accuracy *given* a good keypoint+depth read. Hero uses the customer-facing accuracy claim; PDF carries the math. | Hero pill = 98.3% · §08 PDF section explains the math at depth |
| **D5** | Embed Infinite Studio admin screenshot in §05 (AI-native layer) rather than §02 evidence. | The dashboard proves the *metering* claim (token economics) — that's a §05 narrative beat. §02 already carries the strategic-shift table. | `04-infinite-studio-admin.jpg` lives in §05 with caption tying it to the token-economics row |
| **D6** | Page does NOT carry author/version metadata in hero or footer. | Per skill §4 honesty rule — provenance lives in git, not on the page. | Hero stops at H1+subhead+pills+stats. Footer = copyright line only |
| **D7** | DRI named in spec footer only. Not surfaced on the page itself. | Same reason as D6. The page itself is the artefact; DRI lives in the spec for review traceability. | Page footer = copyright line; spec header = Yash Singh (DRI) / Salman Saudagar (Owner) |

---

## §10 · Out of scope

- D02 slide 17 sector divider (Infrastructure / Software / Retail) — internal positioning, not page-worthy.
- D02 slide 18 vision card — implicit in the existing Vision tone of the page; doesn't need a standalone card.
- Sub-routes under `/fynd-horizon/<x>/` — single-page section. If the math PDF or a dedicated case study needs to be its own route later, that's a separate spec.
- Master pptx hosted as a download — internal deck, not for the register.
- Per-store Mumbai cluster store list — wait until names are confirmed; placeholder copy says "Mumbai cluster · 3 stores" matching slide 15.
- A CTA button to schedule an in-store demo — not in source material; would be a marketing-tone violation.

---

**End of spec.** v0.1 · 2026-05-01 · ready to author.
