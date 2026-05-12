# Website orientation · Spec

**Status:** v0.1 · 2026-04-30
**Owner:** Kushan Shah
**Driver:** Farooq's letter to MM Sir (`docs/2026-04-30-farooq-mda-update-letter.md`)

---

## 1. Why this restructure

The site currently reads as a collection of track pages. The cover letter to MM Sir lays out an explicit two-bucket frame and names every platform that needs visibility. We restructure so:

1. **Every platform mentioned in the letter has a discoverable home.** No reader of the letter should look at the site and not find a section that maps to each bullet.
2. **It reads like a website, not a 12-page memo.** Same chrome, same card primitives, same density on every page. No track is one-of-a-kind.
3. **The site itself is positioned as the "real-time transparency system"** the letter ends on — not just a deck.

This spec covers IA, the page template every IP/platform page must conform to, the content audit (have vs. need), the visual upgrade, and a phased migration plan.

---

## 2. Information architecture · matches the letter word for word

The letter's structure is the IA. Two top buckets, one meta surface.

### Bucket A · Impetus (the F&L AI platform)

The letter pulls Impetus out of the "Retail Projects" group and gives it its own section: *"details of all sub-platforms deployed, adoption across the value chain of F&L with dedicated people involved."* So Impetus gets a dedicated parent + per-sub-IP children.

```
/impetus/                       Impetus track overview (existing)
/impetus/cortex/                Cortex Planning Agent          (HAVE inline · NEED page)
/impetus/trend-to-design/       Trend-to-Design Agent          (HAVE data · NEED page)
/impetus/ask-impetus/           Ask Impetus AI Business Analyst (HAVE data · NEED page)
/impetus/scan-and-go/           Scan & Go                      (HAVE data · NEED page)
/impetus/companion-app/         Trends Companion App           (HAVE data · NEED page)
/impetus/horizon/               Fynd Horizon                   (HAVE data · NEED page; ALSO under "Recent Innovations")
/impetus/digital-twin/          Digital Twin                   (HAVE data · NEED page)
/impetus/garment-designer/      Garment Designer (3D)          (HAVE data · NEED page)
/impetus/print-designer/        Print Designer                 (HAVE data · NEED page)
/impetus/pulsepoint/            PulsePoint                     (HAVE data · NEED page)
/impetus/jiia/                  JIIA                           (HAVE data · NEED page)

(existing portfolio surfaces — already homogenous)
/impetus/brands/                Brands PLP
/impetus/photoshoots/           AI Photoshoots
/impetus/videos/                AI Videos
/impetus/category-intel/        Category Intel
```

**Adoption** (the letter's "across the value chain of F&L") is a section on every Impetus IP page, not a separate page.

### Bucket B · Fynd – Retail Projects

The letter's six sub-bullets become six sub-buckets:

```
B1 · Jio Commerce Platform · "implementation and impact across RRL, RBL, and RRVL"
/jcp/                           JCP overview (existing)
/jcp/cataloging/                AI Cataloging (existing)
/jcp/rrl-rbl-rrvl/              NEW · explicit RRL × RBL × RRVL impact breakdown
                                (today this is buried inside /jcp/index.html sections)

B2 · UCP & Marketing OS
/ucp/                           NEW · UCP currently lives as a section inside /jcp/.
                                Promote to its own surface.
/marketing-os/                  NEW · separate page; today there's no dedicated home.

B3 · Granary
/granary/                       Granary (existing)
/granary/research/<paper>/      Research papers (existing pattern)
/granary/cortex/                NEW · planning brain page
/granary/forecasting/           NEW · ML Forecasting Engine page

B4 · Special Projects · "ALP, Retail Vista, others"
/alp/                           ALP (existing)
/retail-vista/                  Retail Vista (existing)
/forge/                         Forge MES (existing) · classify here as "other"
/hirefirst/                     HireFirst (existing) · same
/retail-jarvis/                 Retail Jarvis (existing) · same

B5 · AI-Native Platforms
/ai-native/                     NEW · landing page that explains the bucket
/ai-native/agentic-automation/  NEW · landing for the trio
/boltic/                        NEW · Boltic
/pixelbin/                      NEW · PixelBin
/ratl/                          NEW · Ratl AI
/ai-native/agentic-commerce/    NEW · landing
/kaily/                         NEW · Kaily · "live in JioMart and AJIO"

B6 · Recent Innovations
/innovations/                   NEW · landing
/innovations/fynd-horizon/      Fynd Horizon
/innovations/autri/             NEW · Autri
/innovations/dark-factory/      NEW · Dark Factory · Made to Measure
```

### Meta surface · Real-time transparency system (the site itself)

The letter ends naming this site as an "L3 Autonomous system that will replace our current ways of human-driven program management." We surface that explicitly.

```
/                               Home — explicitly framed as the transparency
                                system, not a track index. Hero says what
                                this site IS, not just what's on it.
/transparency/                  NEW · "How this works" — the JIRA / Git /
                                systems-of-record ingestion, refresh cadence,
                                L3 autonomy claim, owner.
/numbers/                       Existing
/organisation/                  Existing
/culture/                       Existing
/catalog/                       Existing IP catalog
```

### Top-nav redesign

The current Tracks mega-menu has 3 columns (Platform · Vertical · Capability). Replace with the letter's columns:

```
Tracks
├── Impetus
│   ├── Cortex · Trend-to-Design · Ask Impetus · Scan & Go ·
│   │   Companion App · Horizon · Digital Twin · Garment Designer ·
│   │   Print Designer · PulsePoint · JIIA
│   └── Brands · Photoshoots · Videos · Category Intel
├── JCP / UCP / Marketing OS
│   ├── JCP overview · RRL × RBL × RRVL impact
│   ├── UCP · Marketing OS
│   └── AI Cataloging
├── Granary
│   ├── Granary overview · Cortex · Forecasting · Research
├── Special Projects
│   └── ALP · Retail Vista · Forge MES · HireFirst · Retail Jarvis
├── AI-Native Platforms
│   ├── Agentic Automation · Boltic · PixelBin · Ratl
│   └── Agentic Commerce · Kaily
└── Recent Innovations
    └── Fynd Horizon · Autri · Dark Factory
```

(More items than today's nav, but the letter's shape demands them. Mega-panel widens to 4 columns.)

---

## 3. Homogenous page template (every IP/platform page)

This is the strict template. Every page in Buckets A, B, and "Recent Innovations" follows it. Same section order, same heading levels, same components. The site stops feeling like 20 different documents.

```
┌─────────────────────────────────────────────────────────────────┐
│ TOP NAV (shared across the site)                                │
├─────────────────────────────────────────────────────────────────┤
│ HERO                                                             │
│   Breadcrumb · IP-CATEGORY-LABEL · STATUS PILL                   │
│   H1: <Platform Name>.                                           │
│   1-2 sentence lede                                              │
│   Pills row · DRI · partner · live-since                         │
│ ─── §01 · Headline metrics                                       │
│   4-stat strip (Inter 700, large numerals)                       │
│ ─── §02 · What it does                                           │
│   2-3 paragraphs · plain English · what problem it solves        │
│ ─── §03 · Sub-IPs / modules (if applicable)                      │
│   Card grid · status pill on each · DRI line                     │
│ ─── §04 · Adoption · "across the value chain"                    │
│   Table or chip cloud: brands × verticals × volume               │
│   Names of platforms / surfaces it shows up in                   │
│ ─── §05 · People · dedicated team                                │
│   Compact org grid · DRI · ML lead · QC · RIL counterpart        │
│ ─── §06 · Progress · path to L3 / L4                             │
│   Today's autonomy level · what's automated · what's still       │
│   human · the next quarter's milestone toward L3/L4              │
│ ─── §07 · Sources                                                │
│   Slack thread / deck / sheet / Drive folder links               │
│ ─── §08 · Related (optional)                                     │
│   Cross-link to sibling IPs in the same bucket                   │
│ FOOTER (shared)                                                  │
└─────────────────────────────────────────────────────────────────┘
```

Component-level rules:

- **Status pill** is one of: `LIVE`, `PILOT`, `BUILDING`, `WORKSHOP`, `RESEARCH`. No other words.
- **Hero pill row** uses the existing `.pill` class. Brand pills use the existing tokens.
- **Headline metrics strip** is always 4 cards in a `grid-cols-2 md:grid-cols-4`. Even if you only have 2 numbers, you fill the other 2 with secondary metrics. Never 1, 3, or 5.
- **Sub-IP cards** match the cards on `/jcp/index.html`: `card card-hover p-6` with status pill, H3, DRI line.
- **Adoption** uses the same `grid-table` pattern from `/granary/index.html` line 116 ("ML Forecasting Engine" row).
- **People grid** uses the org card pattern from `/organisation/index.html`. One DRI per pod, photo optional.
- **Progress · L3/L4** is its own section (this is what the letter is selling). Mini-table with columns: `Step · Today · Target this quarter · Owner`.
- **Sources** is the same `Sources:` footer pattern used on the home register page.

If a section has no content, drop it (don't render an empty heading). But the order is fixed: §01–§08, in that order.

---

## 4. Content audit · have vs need

**Already have, just needs to be re-skinned to the template:**

| Page | What's there | What to add |
|---|---|---|
| `/impetus/index.html` | Track overview | §06 Progress to L3/L4 · §07 Sources |
| `/jcp/index.html` | Long, dense | Split: pull UCP into `/ucp/` · pull RRL/RBL/RRVL impact into `/jcp/rrl-rbl-rrvl/` |
| `/granary/index.html` | Most-templated already | §06 Progress to L3/L4 explicit |
| `/alp/`, `/retail-vista/`, `/forge/`, `/hirefirst/`, `/retail-jarvis/` | Track pages | Re-classify in nav as "Special Projects" |
| `/jcp/cataloging/` | Already homogenous | (none — keep as reference template) |
| `/granary/research/transforming-retail-forecasting/` | Already homogenous | (none — keep as reference template) |

**Have data in `data/ips/<id>/` but no page yet (10 Impetus sub-IPs):**

`cortex` · `trend-to-design` · `ask-impetus` · `scan-and-go` · `companion-app` · `digital-twin` · `garment-designer` · `print-designer` · `pulsepoint` · `jiia`

The data files give us the §02-§07 content for each. The template makes the page nearly mechanical — write a generator that reads `data/ips/<id>/{meta,narrative,metrics,releases,team,links}.{json,md,yaml}` and emits the templated page. **Strong recommendation: extend `tools/build_data/build.py` (already exists from v0.8.x) to support this template.** That gets us 10 pages cheaply.

**Have data, need a page (Fynd Retail Projects):**

`fynd-horizon` (under /innovations/) · `autri` (under /innovations/) · `boltic` · `pixelbin` · `ratl-ai` · `ucp` (extract from /jcp/)

**No content yet:**

`marketing-os` — needs source copy
`kaily` — needs source copy. The letter says "Live in JioMart & AJIO" so there's evidence; hunt it down.
`dark-factory` / Made to Measure — needs source copy
`/jcp/rrl-rbl-rrvl/` — needs to be carved out from the existing JCP narrative
`/transparency/` — needs writing (own work; we built the system, we describe how)

---

## 5. Make it look like a website, not an academic note

The current pages skew dense — long tables, lots of paragraph text, sparse imagery. The letter is talking to MM Sir; he should see a **product** (the transparency system), not a dossier. Specific changes:

- **Hero on every page gets a 4-stat strip** (already in template). Numbers first, prose second.
- **Replace long paragraphs with cards** wherever possible. Three short cards beat one long block.
- **Add screenshots + short video clips** to product pages (Cortex, Horizon, Autri, Boltic, PixelBin, Ratl, Kaily). Use the existing `data/ips/<id>/assets/images/` and `assets/decks/` folders that v0.8.x already supports.
- **Status pills everywhere.** Every IP card. Every roadmap row. Every sub-IP. The eye should be able to scan-only and learn what's live.
- **Inline charts** for metrics that have a time series (MAPE trend on Granary forecasting, throughput trend on Cataloging). Tiny SVG sparklines · no chart libraries.
- **Drop the term "register"** in user-facing copy. Replace with "platform" or just no label. The letter calls it a system; we should too.
- **Reduce the table count.** Most current tables can become 3 cards or a stat strip. Tables only when comparing 4+ rows on 4+ columns of similar data.

---

## 6. Reframe the home page

Today's `/` reads like a TOC of tracks. Per the letter, it IS the transparency system. New structure:

```
HERO
  H1: "Reliance × Fynd · Live program register."
  Lede: "Real-time transparency over every platform Fynd is delivering
         inside Reliance Retail. Sourced from JIRA, Git, and the live
         systems of record — refreshed on each platform's own cadence,
         not a quarterly deck."
  4-stat hero: # IPs live · # in pilot · # people on RR · last refresh
  Single CTA pill: "How this works →" → /transparency/

§01 · Impetus · F&L AI Platform (single-card row · big visual)
§02 · JCP · UCP & Marketing OS (single-card row)
§03 · Granary (single-card row)
§04 · Special Projects (compact 5-card grid)
§05 · AI-Native Platforms (compact 5-card grid · split into Automation + Commerce)
§06 · Recent Innovations (compact 3-card grid)
§07 · How this works (block linking to /transparency/)

FOOTER (same as today)
```

Each §-card carries: section name · 1-line description · 2-stat mini-strip · "Open →".

The order matches the letter exactly: Impetus first, then the six Retail Projects sub-buckets, then the meta system. No surprises for a reader who's just read the cover letter.

---

## 7. Migration plan

### Phase 1 · IA scaffold (1-2 days)
- Update top-nav mega-menu in every existing page (the integration team's flow).
- Add empty stub pages for the missing IPs (`/boltic/`, `/pixelbin/`, `/ratl/`, `/kaily/`, `/innovations/fynd-horizon/`, `/innovations/autri/`, `/innovations/dark-factory/`, `/ucp/`, `/marketing-os/`, `/transparency/`, `/jcp/rrl-rbl-rrvl/`). Stub = breadcrumb + "Coming soon · sourcing now" — so links don't 404.

### Phase 2 · template generator (2-3 days)
- Extend `tools/build_data/build.py` to emit pages from the §3 template using `data/ips/<id>/`.
- Generate the 10 Impetus sub-IP pages first (we have data for all).
- Then the AI-Native trio (boltic / pixelbin / ratl-ai · we have data).
- Then Horizon and Autri (we have data).

### Phase 3 · existing page conformance (3-5 days)
- Re-skin `/impetus/`, `/jcp/`, `/granary/`, `/alp/`, `/retail-vista/`, `/forge/`, `/hirefirst/`, `/retail-jarvis/` to the §3 template.
- Carve out `/ucp/` and `/jcp/rrl-rbl-rrvl/` from the existing `/jcp/index.html`.
- Carve out `/granary/cortex/` and `/granary/forecasting/` from `/granary/index.html`.

### Phase 4 · home + transparency (1-2 days)
- Rewrite `/` per §6.
- Write `/transparency/` page · explain the JIRA/Git ingestion, refresh cadence, the L3 autonomy claim, owners, and the audit log.

### Phase 5 · content fill (open-ended)
- Source copy for `/marketing-os/`, `/kaily/`, `/innovations/dark-factory/`.
- Add screenshots / short clips to the product pages.

---

## 8. Out of scope · v1

- Chart libraries · use inline SVG sparklines only.
- Full-text search · the catalog page already covers IP discovery.
- Automated chrome consistency tests · the integration team's manual sweep is fine.
- Per-user dashboards inside the site · the letter says "AI adoption by individuals" but that's a future surface, not a v1 page.
- Live JIRA / Git ingestion · v1 says it CAN ingest; the actual real-time pull is Phase 5+.

---

## Appendix · letter element → site location

A check that every word in the cover letter has a place to live.

| Letter element | Site home |
|---|---|
| Impetus · sub-platforms · adoption across F&L · dedicated people | `/impetus/` + 10 sub-IP pages, each with §04 Adoption + §05 People |
| Jio Commerce Platform · RRL/RBL/RRVL impact | `/jcp/` + new `/jcp/rrl-rbl-rrvl/` |
| UCP & Marketing OS | New `/ucp/` + `/marketing-os/` |
| Granary | `/granary/` + sub-pages for Cortex, Forecasting, Research |
| Special Projects · ALP, Retail Vista, others | `/alp/`, `/retail-vista/`, `/forge/`, `/hirefirst/`, `/retail-jarvis/` (rebucketed in nav) |
| Agentic Automation · Boltic, PixelBin, Ratl | `/boltic/`, `/pixelbin/`, `/ratl/` |
| Agentic Commerce · Kaily (JioMart, AJIO) | `/kaily/` |
| Fynd Horizon | `/innovations/fynd-horizon/` |
| Autri | `/innovations/autri/` |
| Dark Factory · Made to Measure | `/innovations/dark-factory/` |
| Real-time transparency system | `/transparency/` + framed on `/` |
| Roadmap · progress programs · AI adoption · L3/L4 path | §06 Progress on every page |
| Sourced from JIRA / Git / SoR | `/transparency/` explains; data refresh cadence on every page footer |

If anything in the letter doesn't show up in this table, the site is incomplete by definition. Currently 11 of 13 rows have at least a stub; the 2 gaps (Marketing OS · Kaily) need source copy before they can be built.
