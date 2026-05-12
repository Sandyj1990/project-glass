# Impetus restructure · Spec

**Status:** v0.3 · 2026-04-30 · **substantive sections shipped**
**Owner:** Kushan Shah
**Source content:**
- **A.** `docs/Impetus notes compilation/Impetus Release Notes.pdf` · Q1 2026 Release Compendium · 18 product tracks · 105 pages with UI screenshots · per-platform content
- **B.** `docs/Impetus notes compilation/Operationalizing_Autonomous_Commerce_for_Retail.pdf` · Farooq Adam · the L0–L5 Autonomy Ladder + workflow-by-workflow matrix · framework for the "path to L3/L4 this quarter" claim in the cover letter
- **C.** `docs/Impetus notes compilation/Operationalizing_Autonomous_Commerce_Diagrams.pdf` · the matrix as a 2-page diagram; the colored cells = "target autonomy state in the next 90 days"
- **D.** `docs/Impetus notes compilation/Updated Retail Platforms+Agents_ Accenture - Apr 16, 2026.pptx` · 69-slide Apr 16 deck · deeper Impetus content: Command Center, AI Agents (Trend-to-Design, Agentic Control Tower, Store Intelligence), case studies (Superdry SDX, Cataloging, Photoshoots), Generative Media, MES, Jarvis

**Inherits from:** `docs/website-orientation-spec.md` · §3 page template

---

## 0. Implementation status (added 2026-04-30)

Tracked against the section numbering below. ✓ shipped · ⚠ partial · ✗ pending.

### Done ✓

| § | Deliverable | Where it landed |
|---|---|---|
| §2 | Canonical 15-platform inventory locked | `data/impetus/<slug>.yaml` × 15 |
| §3 | Homogenous page template, all 7 sections | `tools/build_impetus.py` + 15 generated pages |
| §3.1 | Eyebrow as `IMPETUS · <SLUG IN CAPS> · LIVE` | renderer in `build_impetus.py` |
| §3.2 | Empty sections drop heading | `render_what_improved` early-return |
| §4 | Asset extraction · 122 screenshots | `assets/impetus/<slug>/` + GCS mirror at `gs://impetus-socialpilot/rrl-portfolio/assets/impetus/` |
| §5 | New `/impetus/index.html` rebuilt with FY26 stat strip + secondary platform-breadth strip + 15-card grid + value-chain band + portfolio-output framing + sources | `impetus/index.html` |
| §6.1 | UCP routed to `/ucp/`, not `/impetus/` | (UCP page itself still pending — see Phase 5) |
| §6.2 | AI Photoshoot ↔ photoshoots/videos cross-linking | `output_gallery` block on platform page + "Powered by" backlink on /photoshoots/ and /videos/ |
| §6.3 | Cortex vs Analytics split (separate pages) | `/impetus/cortex/` + `/impetus/analytics/` |
| §6.4 | GMetri uses `/impetus/gmetri/` slug | data file at `data/impetus/gmetri.yaml` |
| §6.5 | Index uses 15 platforms (not 14, not 18) | confirmed |
| §7 Phase 1 | Scaffold · 14 stub directories + index placeholder grid | shipped early |
| §7 Phase 2 | Content extraction · all 14 platforms verbatim from PDF | shipped (~2,400 lines of YAML) |
| §7 Phase 3 | Generator + 15 generated pages | `tools/build_impetus.py` |
| §7 Phase 4 | `/impetus/index.html` rebuild | shipped |
| §7 Phase 6 | Autonomy framework + Accenture content | shipped (`/autonomous/` + Cortex restructure) |
| §8 | `/autonomous/` · all 8 sections including the 15-platform mapping table at §06 | `impetus/autonomy/index.html` (sections renumbered: §06 mapping, §07 capability matrix, §08 measure-progress) |
| §8.2 | Diagram rendering via PDF → JPG (option b) | `assets/autonomous/matrix-1.jpg`, `matrix-2.jpg` (144dpi, q72) |
| §8.3 | Per-platform → autonomy cross-links | `render_progress` emits `#matrix-<n-n>` anchors; capability rows have matching `id=` |
| §9 | §06 Progress section on every platform | `progress` YAML block + `render_progress` |
| §10 | Accenture pptx mappings (s4 · s11 · s12-s16 · s17-s18 · s19 · s20 · s21-s22 · s23 · s24) | extracted to `assets/impetus/_accenture/`, embedded into Cortex / GMetri / IntelliVerse / Companion App / AI Photoshoot / PLM / index lede |
| §10.1 | Cortex page revised structure · 4 sub-sections (Command Center · AI Agents · Agentic Control Tower · Store Intelligence) | `subsections` block in `cortex.yaml` |
| App. C | Old "Sub-IPs · 16 modules" grid removed; backup at `docs/impetus-index-backup-2026-04-30.html` | done |

### Partial ⚠

| § | Deliverable | Status |
|---|---|---|
| §5 | Per-card DRI line on the 15-platform grid | Org-wide pointer to `/organisation` only. Awaiting per-platform DRI list. |
| §8.1 §06 | DRI column in 15-platform mapping table | Column rendered with "TBD" placeholder. Awaiting DRI list. |
| App. B | Slug ↔ data folder | Spec said `data/ips/<id>/` (folder); shipped as `data/impetus/<slug>.yaml` (single file). Functional difference is zero, naming differs from spec. |

### Pending ✗

| § | Deliverable | Notes |
|---|---|---|
| §7 Phase 5 | `/ucp/` page | UCP source = PDF pp. 78-86 + `docs/UCP Notes compilation/` (local). Recipe in App. A.4. ~3-4 hours. |
| §7 Phase 5 | `/jcp/scan-and-go/` page | Source = PDF p. 92 (1 page only). ~1 hour. |
| §8.3 | Optional `% of workflows at L3+` hero stat on `/impetus/index.html` | Spec says "can include" — not built. Index strip currently shows `5 of 15 platforms at L3+` (computed manually). |

### Out of scope per §11 (deferred to v2)

Cross-platform comparison views · live JIRA/Git refresh · inline charts on platform pages · IntelliVerse 4-sub-IP children as separate routes · interactive autonomy matrix (clickable cells).

### Commit log

`93db35b` · `ff40ab6` · `2a6c101` · `cc03a52` · `252e429` · `8dd7b75` · `1816eac` — 7 commits on branch `fynd-create-portfolio`.

---

## 1. Why this spec

The cover letter to MM Sir says: *"Impetus: Details of all sub-platforms deployed, adoption across the value chain of F&L with dedicated people involved."*

Today, `/impetus/index.html` answers that with a long card grid that mixes Fynd-Create design IPs (Trend-to-Design, AI PIM, Yousta PLM, etc.) with platform IPs. The compendium PDF is the canonical, leadership-blessed inventory — 18 tracks, all with a strict, homogenous structure. The user's curated list condenses these to 15 named platforms.

This spec turns the PDF into a 15-platform website surface under `/impetus/`, with a homogenous page template every sub-platform must follow, asset extraction from the PDF, and a migration path for what's already on the existing `/impetus/index.html`.

---

## 2. The canonical 15-platform inventory

Locked from the user's curated list. PDF page ranges in brackets — these are the source of every word, number, and screenshot.

| # | Platform | URL | PDF p. | data/ips/ |
|---|---|---|---|---|
| 1 | **Command Center / Cortex** · Revenue, margin, inventory, vendor & AOP dashboards with AI-explained insights | `/impetus/cortex/` | 5–11 | `cortex` ✓ |
| 2 | **Fabric Platform / IntelliLoom** · Unified fabric ordering & inventory management | `/impetus/intelliloom/` | 12–13 | NEW |
| 3 | **Impetus PLM** · End-to-end product lifecycle: Design → Tech Pack → Sourcing → Production | `/impetus/plm/` | 14–20 | NEW |
| 4 | **NextWave / FTF** · Fashion Trends Forecasting — celebrity, regional & marketplace trend signals | `/impetus/nextwave/` | 21–24 | NEW |
| 5 | **Costing Engine** · Automated material-level costing with vendor pricing & approval workflows | `/impetus/costing-engine/` | 25–28 | NEW |
| 6 | **Master-Hub / CMT** · Single source of truth for vendor, material & product data | `/impetus/master-hub/` | 29–30 | NEW |
| 7 | **IntelliVerse** · Procuro · IntelliMake · IntelliQC · IntelliPack (PO to shipping) | `/impetus/intelliverse/` | 31–49 | NEW |
| 8 | **UVP (Unified Vendor Platform)** · Vendor co-creation platform used by Shein | `/impetus/uvp/` | 50–56 | NEW |
| 9 | **Recollect** · Reconciliation engine for invoice ↔ PO ↔ GRN matching | `/impetus/recollect/` | 57–64 | NEW |
| 10 | **GMetri (Digital Twin)** · 3D store visualisation & shelf/planogram compliance auditing | `/impetus/gmetri/` | 65–70 | `digital-twin` ✓ (alias) |
| 11 | **PulsePoint** · Store-ops task management, surveys & KPI dashboards | `/impetus/pulsepoint/` | 71–77 | `pulsepoint` ✓ |
| 12 | **Store Companion App** · In-store shopping companion for product discovery & assistance | `/impetus/companion-app/` | 87–91 | `companion-app` ✓ |
| 13 | **AI Photoshoot** · AI-powered product photography & video generation | `/impetus/ai-photoshoot/` | 93–96 | `ai-photoshoot` ✓ |
| 14 | **Impetus Command Center** · Analytics & real-time dashboards for all business functions | `/impetus/analytics/` | 58 (SuperSet section) | NEW |
| 15 | **InstaDesk** · Unified helpdesk for support tickets & SLA tracking | `/impetus/instadesk/` | 101–103 | NEW |

### 2.1 Sub-platforms in the PDF that aren't in the user's 15

| PDF track | Reason it's not in user's 15 | Action |
|---|---|---|
| **UCP (Unified Customer Profile)** · pp. 78–86 | The letter routes UCP to its own "UCP & Marketing OS" bucket under Fynd-Retail Projects, not under Impetus. | Build at `/ucp/` per `website-orientation-spec.md`, NOT under `/impetus/`. |
| **Scan N Go / Kiosk** · p. 92 | Bundled into JCP's customer-facing surface in the org chart. | Build at `/jcp/scan-and-go/` (sibling to `/jcp/cataloging/`), NOT under `/impetus/`. |
| **Ask Impetus** · pp. 97–100 | Cross-cutting AI assistant. Lives in the IP catalog but not as its own Impetus sub-platform. | Cross-link from `/impetus/cortex/` and `/impetus/analytics/`; no standalone page in v1. |

### 2.2 Existing pages this spec REPLACES

Today's `/impetus/index.html` has a "Sub-IPs · 16 modules under Impetus" card grid that lists IPs from the *Fynd Create design portfolio* (Trend-to-Design, Print Designer, Garment Designer, Fynd Create, AI PIM, Yousta PLM, TMS Apparel, etc.). These overlap partially with the user's canonical 15 but aren't the same list.

**Decision (Apr 30 review):** rebuild `/impetus/index.html` from scratch using **only the user's 15-platform list** as the canonical inventory. Keep the current page intact as a backup at **`docs/impetus-index-backup-2026-04-30.html`** so the user can manually reference / port any sub-IP descriptions over as the new pages are built. The four design-portfolio surfaces (`/impetus/brands/`, `/impetus/photoshoots/`, `/impetus/videos/`, `/impetus/category-intel/`) stay live throughout.

---

## 3. Homogenous page template (every sub-platform page)

Direct port of the PDF's per-section structure. Six fixed sections in fixed order. Same components everywhere — no track is one-of-a-kind.

```
┌──────────────────────────────────────────────────────────────────┐
│ TOP NAV (shared, mega-menu, v0.8.3)                              │
├──────────────────────────────────────────────────────────────────┤
│ HERO                                                              │
│   Breadcrumb · Home / Impetus / <Platform>                        │
│   Eyebrow · IMPETUS · SUB-PLATFORM · LIVE                         │
│   H1 · <Platform Name>.                                           │
│   Sub-line · 1-line tagline (from §2 column 2)                    │
│   Pills · audience pills + status pill                            │
│                                                                   │
│ § 01 · For                                                        │
│   "👤 For: <comma-separated audience list>"                       │
│   ↳ Pulled verbatim from PDF                                      │
│                                                                   │
│ § 02 · What It Does for You                                       │
│   2-3 paragraph narrative · plain English                         │
│   ↳ Pulled verbatim from PDF                                      │
│                                                                   │
│ § 03 · How Many People Use It (or "Scale" / "How Much Is Being    │
│   Managed" — header label varies per platform per the PDF)        │
│   Chip strip · 4-8 stat chips                                     │
│   ↳ Each chip from PDF                                            │
│                                                                   │
│ § 04 · What Improved                                              │
│   Light-green callout box                                         │
│   Checkmark bullet list                                           │
│   Bold "Expected metric impact:" line at the end if present       │
│                                                                   │
│ § 05 · Updates Shipped (Latest First)                             │
│   Vertical timeline · date pill + body                            │
│   Each entry: bold subheading + bullet list                       │
│                                                                   │
│ § 06 · Screenshots                                                │
│   Image grid · 1-3 screenshots from PDF                           │
│   Each with caption (verbatim from PDF page footer)               │
│                                                                   │
│ § 07 · Sources (footer)                                           │
│   "Q1 2026 Release Compendium · pp. <X>–<Y>" link to mirror PDF   │
│                                                                   │
│ FOOTER (shared)                                                   │
└──────────────────────────────────────────────────────────────────┘
```

### 3.1 Component-level rules

- **Eyebrow line** = `IMPETUS · <PLATFORM SLUG IN CAPS> · LIVE` (or `IN PILOT` for any not yet in production).
- **Audience pills** in the hero use the existing `.pill` class. Each audience role gets its own pill (`Buyers`, `Planners`, `FCoE`, etc.).
- **Stat chips in §03** use a new `.stat-chip` class — small rounded pill, `JetBrains Mono`, ~14px text. Light grey bg with hairline border. Mirrors the PDF's pale-blue chips.
- **§04 What Improved** uses a left-bordered callout. Light green bg (`#ECFDF5`), green left border (4px solid `#16A34A`). Each line starts with ✓.
- **§05 Updates Shipped** is a vertical timeline. Each entry has a date pill (small, dark blue bg matching PDF) + heading + bullet list. Latest first.
- **§06 Screenshots** lives in a 2- or 3-col grid. Each tile is a `.card` with the screenshot, hairline-bottom-bordered, then a small caption row inside.

### 3.2 Sections that may be empty

If the PDF section is missing for a given platform, drop the heading entirely (don't render an empty section). But the order is fixed §01 → §06.

---

## 4. Asset extraction (one-time)

The PDF has UI screenshots starting around the IntelliVerse and UCP sections (p. 50+) and likely throughout. We extract them as PNGs and host on GCS so the site references stable URLs.

### 4.1 Process

```bash
# 1. Identify screenshot pages per platform (TBD by visual sweep)
# 2. Extract via pdfimages or pdftoppm at 200 DPI
pdftoppm -r 200 -png "docs/Impetus notes compilation/Impetus Release Notes.pdf" \
  /tmp/impetus-pages/page

# 3. Crop screenshot regions per platform → save as PNG
#    (manual or via Pillow; aim for ~1600px wide JPEGs at quality 85)

# 4. Upload to GCS at the same prefix the website-spec uses for portfolio assets
gsutil -m cp -r assets/impetus/ \
  gs://impetus-socialpilot/rrl-portfolio/assets/impetus/

# Resulting URLs:
#   https://socialassets.impetusz0.de/rrl-portfolio/assets/impetus/<platform>/<n>.png
```

### 4.2 Per-platform screenshot inventory

To be filled by sweep through PDF. From the pages I've already seen:

| Platform | Screenshot pages in PDF | Caption shown |
|---|---|---|
| Command Center / Cortex | TBD (sweep p. 5–11) | TBD |
| UCP (will go to `/ucp/`) | p. 80 | "UCP audience builder: Targeting users by behavior and purchase history" |
| IntelliVerse | TBD (sweep p. 31–49 — long section, likely several) | TBD |
| GMetri | TBD (sweep p. 65–70) | TBD |
| Companion App | TBD (sweep p. 87–91) | TBD |
| AI Photoshoot | TBD (sweep p. 93–96) | TBD |

A one-shot sweep of the PDF lists every screenshot. Captions are pulled verbatim from each page.

### 4.3 If a platform has no screenshot in the PDF

Drop §06 from that platform's page. Don't generate a placeholder. Add a comment in the page noting "No screenshots in source — add when available." Visible to maintainers, invisible to readers.

---

## 5. New `/impetus/index.html` structure

The current page is dense and mixes platform sub-IPs with design-portfolio output. New structure separates them clearly:

```
HERO
  Breadcrumb · Home / Impetus
  Eyebrow · TRACK 02 · F&L AI PLATFORM · LIVE
  H1 · "Impetus."
  Lede · "Reliance's AI-first platform for Fashion & Lifestyle retail. 
          15 sub-platforms in production, used by 2,000+ people across 
          the F&L value chain — Plan · Buy · Make · Sell."
  Stat strip · 8-card grid · canonical FY26 numbers (1 Apr 2025 → 31 Mar 2026)
    Row 1 · scale of work
      · Options designed · 1,06,892
      · Active vendors · 1,316
      · Shipments dispatched · 27,48,859
      · Peak packing in a day · 1,11,241 qty
    Row 2 · throughput + lifecycle
      · Total POs created · 11,06,954
      · Pieces delivered · 15,08,34,232
      · Vendor → store · 5 days avg (awb_delivered − awb_created)
      · Last refresh · <rolling · pulled from data source>

  Smaller secondary strip below the hero · platform breadth
    · 15 sub-platforms in production
    · 40+ updates shipped Q1 2026
    · 2,000+ users across F&L
    · 18 product tracks documented in Q1 release compendium

§ 01 · WHAT WE BUILT · 15 SUB-PLATFORMS
  H2 · "All 15 sub-platforms in production."
  Lede · "Every sub-platform lives by the same template: who it's for, 
          what it does, how many use it, what improved, what shipped, 
          screenshots. The numbers are pulled from the Q1 2026 Release 
          Compendium."
  
  4-column card grid (16 cards if we add an "All releases" tile).
  Each card:
    · Eyebrow with category line (Plan / Buy / Make / Sell / Operate)
    · H3 · Platform name
    · 2-line tagline
    · Stat row · 1 headline number
    · DRI line · "DRI · <name>"
    · Status pill
    · Card click → /impetus/<slug>/

§ 02 · ADOPTION · ACROSS THE F&L VALUE CHAIN
  H2 · "Embedded in every F&L stage · Plan · Buy · Make · Sell."
  4-column band (existing). Each column: stage label + comma-sep IP list.
  Slightly tightened copy from current page.

§ 03 · DESIGN PORTFOLIO OUTPUT · WHAT IMPETUS HAS SHIPPED
  H2 · "What Impetus has shipped."
  Sub-lede · "Distinct from the platform sub-IPs above. This is the 
              creative work product — designs, photoshoots, videos, 
              category-intel reports — produced ON TOP of the platforms 
              and visible to Reliance brand teams today."
  4-card row (existing) · Brands · Photoshoots · Videos · Category Intel
  Each card → /impetus/<surface>/

§ 04 · OPERATING CADENCE / NUMBERS / LAST APEX
  Existing strip. Trim to 3 cards:
    · Cornerstone · 13 Nov 2024 · 76 sl.
    · Last Apex · Feb 11 · MDA chain
    · Refresh cadence · Daily (Cortex live since 15 Apr)

§ 05 · TEAM (carried from existing)
  Existing org snapshot. Keep.

§ 06 · SOURCES
  Existing. Add link to Impetus Release Notes PDF on the CDN.

FOOTER (shared)
```

The big shift from today: **the design-portfolio surfaces (Brands · Photoshoots · Videos · Category Intel) are clearly labeled as OUTPUT of the platforms**, not as platforms themselves. And the 15 actual sub-platforms get a dedicated grid up top, sourced from the leadership-blessed PDF.

---

## 6. Discrepancies & resolutions

### 6.1 UCP placement

- **PDF says** UCP = "Unified Customer Profile" · marketing teams · audience builder for Meta/Google · 79 formats · 7,000 stores. Pages 78–86 in Impetus compendium.
- **User's letter** routes UCP to "UCP & Marketing OS" under Fynd-Retail Projects · NOT under Impetus.
- **Resolution:** Build UCP at `/ucp/` per `website-orientation-spec.md` §2.B2. Add a one-line cross-reference on `/impetus/index.html` ("UCP lives at /ucp/ — see Fynd-Retail Projects."). Don't double-list.

### 6.2 AI Photoshoot · platform AND its output gallery

- **AI Photoshoot is one of the 15 Impetus sub-platforms** (PDF pp. 93–96).
- **The 4 shoots we built yesterday** under `/impetus/photoshoots/` (AJIO × ASOS · SS26 PLM Pilot · Buda Jeans HP · Buda Jeans Valentine) are the **output of that platform** — not a separate surface.
- **Resolution: parent-child structure.**
  - `/impetus/ai-photoshoot/` = **platform page** (PDF content: pipeline, throughput, ~4,000 videos, 88% first-pass, 90% cost reduction, 15 days→5 hours, who uses it, what shipped). Lives in the §01 grid as one of 15.
  - `/impetus/photoshoots/` = **its output gallery** (4 representative shoots). Lives as a child surface.
  - On the platform page (§06 Screenshots slot), replace screenshots with an **"Output gallery →" CTA card** that links to `/impetus/photoshoots/` and shows 1-2 hero thumbnails.
  - On the gallery index page, add a **"Powered by · AI Photoshoot platform →" link** above the card grid pointing back to the platform page.
  - On `/impetus/index.html`, the §03 "Design portfolio output" row keeps `/impetus/photoshoots/` as a tile, but the tile copy explicitly says "Output of /impetus/ai-photoshoot/".
- **URL structure · LOCKED (Apr 30 review)** · Option (a) — flat URLs. Both `/impetus/photoshoots/` and `/impetus/videos/` stay at their current paths. Parent-child relationship is conveyed via copy and cross-links, not URL nesting. Zero churn on existing bookmarks.
- **`/impetus/videos/` · LOCKED · same parent** · the AI Photoshoot platform covers both photo and video output ("AI-powered product photography & video generation" per the user's #13). Both `/impetus/photoshoots/` and `/impetus/videos/` are framed as **output of `/impetus/ai-photoshoot/`** — cross-linked from the platform page's "Output gallery" section.

### 6.3 Impetus Command Center vs Cortex

- User lists both **#1 "Command Center / Cortex"** and **#14 "Impetus Command Center"** as separate platforms.
- **PDF** has Cortex (pp. 5–11) and SuperSet/Analytics (mentioned p. 58 in TOC) as separate concerns.
- **Resolution:** Treat Cortex as the AI-explained dashboard layer (`/impetus/cortex/`) and Impetus Command Center as the analytics/SuperSet layer (`/impetus/analytics/`). They're related but distinct. Add a section on each page noting the relationship.

### 6.4 GMetri vs digital-twin

- **PDF** uses "GMetri (Digital Twin)" — both names, parenthetical.
- **Existing** `data/ips/digital-twin/` folder.
- **Resolution:** URL = `/impetus/gmetri/` (matches user's list). data folder stays as `digital-twin` (alias). Page H1 = "GMetri.", sub-line "(Digital Twin)".

### 6.5 Numbers in the cover-letter list

User writes "**14** Impetus Command Center" — this is the 14th line, not "14 IPs". Not the same as the existing `/impetus/index.html` "14 IPs in production" stat. The new index uses 15 (matches user's list) or 18 (matches PDF) — pick **15** to align with the user's curation.

---

## 7. Migration plan

### Phase 1 · scaffold + asset prep (½ day)
- Create stub directories under `/impetus/` for the 13 NEW pages (cortex stays in data, the rest get folders).
- Add a 15-card grid placeholder to `/impetus/index.html` (linking to all 15 stubs with "Coming · sourcing now" copy).
- Sweep the PDF and produce the screenshot inventory (§4.2 table fully filled in).
- Extract screenshots from PDF, upload to GCS at `assets/impetus/<slug>/<n>.png`.

### Phase 2 · content extraction (1 day)
- For each of 15 platforms, extract from PDF into a YAML data file at `data/ips/<id>/release-notes.yaml`:
  - `for` (audience list)
  - `what_it_does` (paragraphs)
  - `scale` (chip list)
  - `what_improved` (bullet list with optional bold "Expected metric impact" line)
  - `updates_shipped` (timeline entries with dates, headings, bullets)
  - `screenshots` (paths + captions)
- Verbatim copy from the PDF — no rewriting in v1. Reading-the-PDF and reading-the-page should match word-for-word for an MDA reviewer.

### Phase 3 · template + page generation (1-2 days)
- Build a generator: read `data/ips/<id>/release-notes.yaml` → write `/impetus/<slug>/index.html` per the §3 template.
- Generate all 15 pages from the same template.
- Hand-verify each page against its source PDF section.

### Phase 4 · /impetus/index.html rebuild (½ day)
- Implement §5 structure.
- Replace the existing "Sub-IPs · 16 modules" grid with the 15-platform card grid linking to the new pages.
- Add §03 "Design portfolio output" framing for the existing 4 portfolio surfaces.

### Phase 5 · UCP/Scan&Go siblings (½ day · separate from Impetus)
- `/ucp/` per website-orientation-spec §2.B2 — content from PDF pp. 78–86.
- `/jcp/scan-and-go/` — content from PDF p. 92.
- Cross-reference both from `/impetus/index.html`.

### Phase 6 · autonomy framework + Accenture content (1-2 days)
- Build `/autonomous/` per §8.
- Extract diagram pages from Doc C, upload to GCS, embed.
- Update each platform page's §06 Progress per §9 (autonomy bar + workflow rows + this-quarter card).
- Pull Accenture pptx images for Cortex sub-sections (Command Center, AI Agents, Control Tower, Store Intelligence) per §10.
- Refresh `/impetus/index.html` lede with Doc D s20 framing.

**Total: ~5-6 days** for a leadership-blessed, content-verbatim, PDF + pptx-aligned `/impetus/` surface with the autonomy framework anchoring every Progress section.

---

## 8. NEW page · `/autonomous/` · Autonomy ladder + 90-day path

This is the page that operationalizes the cover-letter line *"path for each to reach L3/L4 autonomy this quarter."* It anchors every sub-platform's §06 Progress section. Without this, the L3/L4 claim has no shared definition.

**Source:** Doc B + C from the source list above. Render verbatim from Farooq's paper. The diagram PDF is the visual.

### 8.1 Page structure

```
HERO
  Breadcrumb · Home / Impetus / Autonomy
  Eyebrow · IMPETUS · AUTONOMY LADDER · 90-DAY PATH
  H1 · "From human-driven to autonomous."
  Lede · 1-paragraph framing from Doc B §1.1 Executive Summary
         ("Retail is an inventory risk business. 85-97% of every rupee…")
  Author byline · Farooq Adam · Apr 15, 2026
  Status pill · Framework · Live

§ 01 · The premise
  3 paragraphs, verbatim from Doc B §1.1
  Pull-quote callout · "AI has entered the conversation — but in most
  organisations it is still a surface-level addition. The bet itself
  has not changed."

§ 02 · The risk gates
  Verbatim from §1.2 Doc B
  4-card grid · Inventory holding risk (Plan) · Procurement risk (Buy)
  · Supply chain risk (Move) · Revenue risk (Sell)

§ 03 · The 6 levels of autonomy
  6-card vertical stack · L0 → L5 · each card:
    · Level number + name in display font
    · One-line definition (verbatim from Doc B §1.3)
    · "Who decides · Who executes · Who bears risk" tag row
    · Color band matching the diagram PDF's blue ramp
  Bottom callout · 3 transition lines from Doc B verbatim:
    "L1→L2 · tool upgrade — same people with better instruments"
    "L2→L3 · skill upgrade — same people doing the same jobs faster"
    "L3→L4 · identity shift — roles dissolve, the org becomes a
     fundamentally different entity"

§ 04 · Not every workflow should reach L5
  Verbatim from Doc B §1.3 closing paragraph
  3-card grid · Strategy/vision (L1-L2) · Brand/creative (L3) ·
  Compliance/ethics (L2-L3)

§ 05 · The 90-day target matrix · across the F&L value chain
  Big embedded diagram · the 1.4 [1/2] and [2/2] pages from Doc C
  rendered as inline SVG OR <img> from CDN-uploaded PDF page exports
  Caption strip · "The colours represent target autonomy state in the
  next 90 days. Source: Operationalizing Autonomous Commerce Diagrams,
  Apr 14, 2026."
  Below the diagram · short explainer text from Doc B §1.4

§ 06 · How each Impetus platform maps to the matrix
  Table · 15 platforms × workflow rows they enable
  Each row: platform name · workflows it powers · today's level (chip
  in current-state color) · target in 90 days (chip in target-state
  color) · DRI for the move
  This table is the executive summary of the entire transparency
  system the cover letter promises.

§ 07 · How we measure progress
  3-card row · Risk reduction (per Doc B §1.2)
  · Throughput uplift · Defect/anomaly rate
  Each card · 1 paragraph from Doc B
  Footer link · Download the full paper (PDF on CDN)

§ 08 · Sources
  Operationalizing Autonomous Commerce for Retail · Farooq Adam ·
  15 Apr 2026 (PDF link)
  Operationalizing Autonomous Commerce Diagrams · 14 Apr 2026 (PDF link)
```

### 8.2 Diagram rendering

Two options for the 90-day matrix:

- **(a) Inline SVG** · best fidelity, searchable text, accessible. Requires a one-time pass to convert Doc C's two diagram pages from PDF to SVG (e.g. via `pdf2svg`) then drop into the HTML. Heavy markup but a one-time cost.
- **(b) PNG export from PDF** · simpler. `pdftoppm -r 200` per page → upload to GCS → `<img>` tag. No accessibility for cell text but the image is shareable as-is.

**Recommendation:** start with (b) for v1, upgrade to (a) when the matrix becomes interactive.

### 8.3 Cross-linking

Every sub-platform page (per §3 template, §06 Progress) links into specific anchors of `/autonomous/#matrix-<workflow>` so the reader can see how that specific platform fits the broader picture.

The home page hero stat strip can include "% of workflows at L3+" pulled from this matrix once each platform is tagged.

---

## 9. Updated `§06 Progress` section · grounded in the L0–L5 ladder

Replace the §06 Progress section in the original page template (§3 above) with this enriched version. Every Impetus sub-platform page conforms.

```
§ 06 · Progress · path to L3 / L4

Sub-section A · "Where this platform sits today"
  Mini autonomy bar · 6 cells (L0…L5) · current cell highlighted
  1-line description · "Today: <verbatim summary of current capability
                       at the highest workflow this platform enables>"

Sub-section B · "Workflows this platform enables"
  Stacked bullet list · for each workflow the platform powers:
    · <Workflow name> (e.g. Demand Forecasting · 1.1)
    · Current level pill (L0–L5 with color)
    · 90-day target pill
    · 1-line plan to move from current → target
    · Cross-link · "See in matrix →" → /autonomous/#matrix-<workflow>

Sub-section C · "What we'll prove this quarter"
  3-card row · borrowed pattern from §07 Sources but framed forward
    · "Workflow we move next" · <e.g. OTB Budgeting L2 → L3>
    · "Risk reduction milestone" · <e.g. ₹X Cr inventory at risk → ₹Y>
    · "Identity shift indicator" · <e.g. role X dissolves into role Y>
```

This puts the cover letter's "path for each to reach L3/L4 autonomy this quarter" on every page, with a verifiable per-workflow plan — not a marketing claim.

---

## 10. Accenture pptx · content additions per platform

Doc D (Apr 16 Accenture deck, 69 slides) deepens specific platforms. Pull material into the relevant `/impetus/<slug>/` page's §02 What It Does and §03 How Many People Use It sections. Verbatim from the deck.

| Pptx slide | Material | Goes into |
|---|---|---|
| s4 | Six-cadence Retail Clock — explainer | `/impetus/cortex/` · §02 sidebar callout (Cortex IS the cadence layer) |
| s10 | Impetus Scale (930 mfrs · 39.2K options · 3.6 days · 88 stores fully digitised · 105M items) | **Superseded** by FY26 numbers (1 Apr 2025 → 31 Mar 2026): 1,06,892 options designed · 1,316 active vendors · 27,48,859 shipments · 1,11,241 peak qty/day · 11,06,954 POs · 15.08 Cr pieces delivered · 5 days vendor→store avg. Use the FY26 set on `/impetus/index.html` hero strip; mention the s10 figures only as historical comparison if useful. |
| s11 | Digital Twin · "Fabric · Garment · Store" 3-pillar framing | `/impetus/gmetri/` · §02 expansion |
| s12 | Impetus AI Agents · Trend-to-Design Agent | `/impetus/cortex/` · §03 sub-section "AI Agents" |
| s13–14 | Impetus Command Center [1/2] and [2/2] · the unified monitor-plan-act surface · "Scan to watch demo video" | `/impetus/cortex/` · §02 lead paragraph (this is the canonical pitch — replace any other Cortex copy) |
| s15 | Agentic Control Tower · "agent-driven control tower that detects, prioritizes, and resolves business exceptions" | `/impetus/cortex/` · §03 sub-section "Agentic Control Tower" — sibling to AI Agents |
| s16 | Store Intelligence · "AI-powered store intelligence that decodes demand, competition, and localized growth" | `/impetus/cortex/` · §03 sub-section "Store Intelligence" — third sibling |
| s17–18 | Superdry SDX case study · 120 designs in 5 days · 90% time reduction · live on AJIO product link | `/impetus/plm/` · §05 Updates Shipped (already in PLM scope per user's #3 mapping); also referenced in `/impetus/photoshoots/` Buda Jeans intro |
| s19 | AI Native Cataloging & Photoshoots · mannequin imagery framing | `/impetus/ai-photoshoot/` · §02 lead paragraph |
| s20 | "One integrated system across planning, execution, measurement and governance" | `/impetus/index.html` lede (replaces current copy) |
| s21–22 | Generative Media · Product Videos / Video Ads / Music Videos / Short Film + Social Media Reach | `/impetus/photoshoots/` and `/impetus/videos/` index strips — use as the "what we produce" framing |
| s23 | MES · Manufacturing Execution System · the challenges + the platform | `/impetus/intelliverse/` · §02 (IntelliVerse IS the MES per user's #7 mapping) |
| s24 | "App Feature Map · Optimizing Sales Force · Key Features for Peak Performance" | `/impetus/companion-app/` · §02 (this is Companion App's feature spec) |
| s25 | Jarvis · CCTV + wearable audio + store data | NOT Impetus · belongs to `/retail-jarvis/` (existing track). Add a "powered by Jarvis intel" callout to `/impetus/pulsepoint/` if PulsePoint consumes Jarvis signals. |

**Asset extraction from the pptx** · the deck has numerous diagrams + screenshots embedded as images. Run the same extraction approach as for the Release Notes PDF (see §4): unzip pptx, lift images from `ppt/media/`, name per slide, upload to GCS at `assets/impetus/<platform>/`. Captions reconstructed from each slide's title text.

### 10.1 Cortex page · revised structure

The Accenture deck has a LOT of material on Cortex/Command Center (s13–s16 cover 4 separate features). The Cortex page therefore gets a richer §03 with **sub-sections** instead of a flat chip strip:

```
§ 03 · How many people use it · features live today
  Sub-section · Command Center [1/2] + [2/2]
    Verbatim from Doc D s13–s14 · 4 quick stats from PDF p.5–11
  Sub-section · AI Agents · Trend-to-Design
    Verbatim from Doc D s12
  Sub-section · Agentic Control Tower
    Verbatim from Doc D s15
  Sub-section · Store Intelligence
    Verbatim from Doc D s16
```

Cortex effectively becomes the umbrella page for "the Impetus AI brain," with these 4 features as siblings under it.

---

## 11. Out of scope · v1

- Editing or rewriting any source content. We render verbatim from the four source docs (A · B · C · D in the source list). Anything we want to change goes to the source first.
- Cross-platform comparison views (e.g. "all Q1 launches in one timeline").
- Live data refresh from JIRA/Git for any of the 15 platforms — that's the `/transparency/` story per `website-orientation-spec.md` §6, separate effort.
- Inline charts on individual platform pages — chip-stat strips only in v1.
- Per-platform deep dives (sub-IP children of IntelliVerse, etc.) — IntelliVerse has 4 sub-modules (Procuro · IntelliMake · IntelliQC · IntelliPack); v1 lists them as section headers within a single `/impetus/intelliverse/` page, not as separate routes.
- Interactive autonomy matrix on `/autonomous/` — v1 ships as a static image of the diagram. Cell-level interactivity (filter by workflow, click a cell for the platform list) is a v2.

---

## Appendix A · per-platform content recipe

Filled in for the 4 platforms we've already inspected. Other 11 need a sweep.

### A.1 Cortex / Command Center (`/impetus/cortex/`)

- **For:** CEO / Business Head, F&L Leadership, Buyers, Sourcing Managers, Planning Teams
- **What it does:** "Open one screen and the whole business is there… 6 modules live: Portfolio Health, Margin Analysis, Store Intelligence, Inventory Health, Vendor Performance and AOP Tracking."
- **How many use it (chips):**
  - Revenue: ₹22.2 Cr/day | GM%: 39.9% | 4 zones, 10 states, 3,198 stores
  - Inventory: ₹1,442 Cr total | 6.9% aged >180 days | ₹85.1 Cr at risk
  - Vendor OTIF: 70.6% (vs 90% target) | Fill Rate: 87% (vs 95%)
  - 6 modules live | CEO + 8 leadership roles | Desktop, iPad, iOS
- **What improved (✓ list, 7 lines):** copy verbatim from PDF p. 5
- **Updates shipped:** "15 Apr 2026 · Command Center (Beta) LIVE, Public Launch" + bullets · "14 Apr 2026 · Buy Plan Status + UX Enhancements" + bullets · plus older entries through to start of Q1
- **Screenshots:** TBD — sweep pp. 5–11

### A.2 IntelliMAF / IntelliLoom (`/impetus/intelliloom/`)

- **For:** Buyers, Planners, FCoE (Fabric Centre of Excellence), Format Heads, Sourcing Managers, Mill Vendors
- **What it does:** "Buyers and planners raise fabric requests through structured forms instead of ad-hoc emails and WhatsApp messages…"
- **How much is being managed (chips):**
  - ₹420 crore+ in fabric orders on platform | ₹258 crore (~67%) assigned to suppliers
  - ₹127 crore in active buyer decisions | ₹34.6 crore in early-stage pipeline
  - ~3,650 metric tonnes of weft knit fabric | ~3.08 crore metres of woven/warp/denim fabric
  - 38 improvements shipped in March alone
- **What improved (callout):** copy verbatim from PDF p. 12 with the "Expected metric impact:" line
- **Updates shipped:** "2 Apr · March Improvements, 38 Updates in 11 Releases" · "19 Feb · Fabric Budget Controls + Supplier Assignment + Format Head Approval" · "5 Feb · Structured Fabric Requests, Replacing Emails and WhatsApp"
- **Screenshots:** TBD — sweep pp. 12–13

### A.3 Impetus PLM (`/impetus/plm/`)

- **For:** Fashion Designers, Technical Designers, Buyers, Product Managers, Sourcing Teams
- **What it does:** "Impetus PLM replaces Centric PLM for design, tech pack and product development…"
- **How many use it (chips):**
  - Rolled out: Yousta Mens Wear (14 Apr 2026) | All Centric styles migrated
  - Upcoming: Yousta All Segments & Azorte & Fashion Factory (20 Apr), Trends (23 Apr)
- **What improved (✓ list, 7 lines):** copy verbatim from PDF p. 14
- **Updates shipped:** "14 Apr 2026 · PLM Rolled Out for Yousta Mens Wear" + bullets · "Apr 2026 (Upcoming) · Phased Format Rollout" + bullets
- **Screenshots:** TBD — sweep pp. 14–20

### A.4 UCP — going to `/ucp/`, not `/impetus/`

(Per §6.1 above, this routes to Fynd-Retail Projects.)

- **For:** Marketing Teams (campaign targeting), Store Staff (NPS, customer satisfaction), Business Heads (insights), Customers (offers & savings)
- **What it does:** "Marketing teams build customer lists using RPOS (Retail POS) real-time transaction data (~2 lakh events per day from 16+ retail formats) and push them directly to Meta (Facebook/Instagram) and Google Ads, no manual spreadsheet exports…"
- **Scale (chips):**
  - 79 retail formats, ~7,000 stores | 7.2 million orders processed
  - 5 lakh daily NPS surveys | ~2 lakh daily purchase events
  - 16+ retail formats connected | 46 campaigns run this quarter
- **What improved (callout):** copy verbatim from PDF p. 79
- **Updates shipped:** "2 Apr · Customer Savings Display on JioMart (Fayda Meter)" · "1 Apr · Satisfaction Survey via SMS, Every Purchase Triggers Feedback" · "24 Mar · Any Platform Can Now Integrate + Shared Addresses + Privacy Controls" · "30 Jan 2026 · Real-Time Purchase Data + Rich Messaging + Social Media Campaign Support"
- **Screenshots:** UCP audience builder (PDF p. 80) — caption: "UCP audience builder: Targeting users by behavior and purchase history"

(Recipes for the remaining 11 to be filled by the same one-page-per-platform sweep through the PDF.)

---

## Appendix B · slug ↔ data folder mapping

| URL slug | data/ips/ folder | Notes |
|---|---|---|
| `cortex` | `cortex` | exists |
| `intelliloom` | NEW · `intelliloom` | aliases: IntelliMAF |
| `plm` | NEW · `impetus-plm` | replaces Centric PLM, name plain "PLM" in URL |
| `nextwave` | NEW · `nextwave` | aliases: FTF, Fashion Trends Forecasting |
| `costing-engine` | NEW · `costing-engine` | |
| `master-hub` | NEW · `master-hub` | aliases: CMT, Central Master Table |
| `intelliverse` | NEW · `intelliverse` | umbrella for Procuro, IntelliMake, IntelliQC, IntelliPack |
| `uvp` | NEW · `uvp` | Unified Vendor Platform |
| `recollect` | NEW · `recollect` | Reconciliation Engine |
| `gmetri` | `digital-twin` (alias to `gmetri`) | URL uses `gmetri` per user's list |
| `pulsepoint` | `pulsepoint` | exists |
| `companion-app` | `companion-app` | exists |
| `ai-photoshoot` | `ai-photoshoot` | exists; SEPARATE from `/impetus/photoshoots/` (output surface) |
| `analytics` | NEW · `impetus-analytics` | aliases: Impetus Command Center, SuperSet |
| `instadesk` | NEW · `instadesk` | |

---

## Appendix C · what gets removed from current `/impetus/index.html`

- The "Sub-IPs · 16 modules under Impetus" card grid (lines 1 of grep above and following 7 cards). Replaced by the 15-platform grid linking to the new pages.
- The 16 specific cards listed (Trend-to-Design, AI Cataloging, Print Designer, Garment Designer, Fynd Create, TMS Apparel, AI PIM, Yousta PLM, …). Most of these become content INSIDE the new platform pages or move to `/impetus/<surface>/` portfolio pages. None get deleted — just relocated.
- The "Plan · Buy · Make · Sell" pillar grid stays — it's the value-chain framing the cover letter calls out as "adoption across the value chain."
- The header track summary stays.
