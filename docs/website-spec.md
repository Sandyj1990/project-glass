# Fynd Create — Design Portfolio & Category Intelligence

**Status:** v0.1 spec, 2026-04-29
**Owner:** Kushan Shah
**Inherits visual system from:** [reliance-retail-fynd.vercel.app](https://reliance-retail-fynd.vercel.app)

---

## 1. Purpose

A single internal site that consolidates the design output of Fynd Create (the trend-to-design IP within Impetus) into five discoverable surfaces:

1. **Brand portfolios** — every linesheet image, organized by brand × gender × category, browsable and filterable.
2. **Photoshoots** — AI-generated on-model imagery delivered to Reliance brands. Curated representative sample of the broader pipeline; every entry shown is **live / delivered work** (not WIP). Three structural shapes: marketplace listings (live SKUs on AJIO), showcases (input → output proof of delivered renders), and brand campaigns.
3. **Videos** — AI-generated motion (brand films, ads, reels, product videos) curated from the Fynd Studio Portfolio sheet. Hosted externally on YouTube / Instagram and embedded in-page; we don't re-host the bytes.
4. **Category Intelligence** — published PDF reports per gender × category × season, **India market only** (sourced from `~/Documents/work/trend-engine/reports/*-india/output/*.pdf`).
5. **(removed)** — `/explore` collapsed into `/brands` (§5.2). The Brands surface IS the single PLP filterable by gender × category × brand.

The audience is internal: design leads, planners, RRVL apex reviewers, and Fynd leadership reviewing what Fynd Create has produced for Reliance brands. Same reading persona as the source register — MDA / executive.

---

## 2. Visual System (inherited)

**Strict inheritance from reliance-retail-fynd.vercel.app.** Same library of primitives, same restraint. No new design language.

### Typography
- **Family:** `Inter, system-ui, sans-serif` only.
- **H1:** 72 px / 72 lh / 700 / -2.88 px tracking.
- **H2:** 48 px / 700.
- **H3:** 18 px / 600.
- **Body:** 16 px / 24 lh / 400.
- **Eyebrow / section marker:** small-caps, 12 px, weight 500, letter-spaced, paired with `§` glyph.
- **Tabular data:** Inter, weight 500, slightly tighter line-height; numerics tabular-nums.

### Color
| Role | Token | Hex |
|---|---|---|
| Page background | `bg` | `#ffffff` |
| Foreground text | `fg` | `#0a0a0a` |
| Muted text | `muted` | `#6b7280` (gray-500) |
| Hairline borders | `border` | `#e5e5e5` (neutral-200) |
| Section tint, success | `accent.green` | `#047857` text on `#ecfdf5` bg |
| Section tint, warning | `accent.amber` | `#b45309` text on `#fffbeb` bg |
| Brand accent | `accent.purple` | `#6b5bd6` |
| Inverted surface | `inverted` | `#0a0a0a` bg, `#ffffff` text |

No gradients. No shadows beyond a 1 px hairline. Status badges (LIVE / DRAFT / PILOT) use the tinted bg + colored text pattern from the reference.

### Layout
- **Container:** `max-width: 1200 px`, centered, `px-6` gutters on mobile.
- **Section rhythm:** `pt-24 pb-20 border-b` — generous vertical, single hairline divider.
- **Section header:** `§ NN · LABEL` (small caps eyebrow) + an H2.
- **Cards:** flat, hairline border, no shadow. Hover state = border darkens to fg, no lift.
- **Tables:** dense, no zebra striping, top + bottom hairline, column heads in muted small caps.

### Components reused
- Top nav: brand mark (`Fynd Create`) + anchor links + small confidentiality marker on the right.
- Numbered track cards (`01 · BRAND`, `02 · BRAND` …).
- Status pills (`LIVE`, `DRAFT`, `READY`, `IN REVIEW`).
- Footer: Owner · Last verified date · Version, on inverted dark surface.
- "How to read" rules section copied from the source as the documentation pattern for the report library.

---

## 3. Information Architecture

```
/                            Home — register cover + jump-points to all 5 surfaces
/brands                      Single PLP — every AI-generated linesheet image,
                             filterable by gender × category × brand. 876 unique
                             designs (deduped by sha256). NO per-brand detail
                             pages — the brand chip filter is the drilldown.

/photoshoots                 Photoshoot index (one card per AI-generated lookbook set)
/photoshoots/<slug>          Photoshoot detail (3 layouts: marketplace-listing,
                             showcase, campaign)

/videos                      Video index (one card per AI-generated video)
/videos/<slug>               Video detail (embedded YouTube/Instagram iframe)

/category-intel              Category Intelligence index (4 India-market PDFs in v1)
/category-intel/<slug>       Embedded PDF viewer for one report

```

**No deeper than 3 levels.** Image detail is a modal/lightbox over the current page, not a separate route — keeps deep linking simple while preserving filter state.

---

## 4. Navigation

Top nav, sticky, hairline border-bottom, exactly the reference site's pattern:

```
Fynd Create · Portfolio   Brands   Photoshoots   Videos   Category Intel   Confidential · v0.1 · Apr 29
```

- No mega-menu. No hamburger on desktop — every primary surface is one click.
- Mobile: collapsed to a single drawer; brand mark stays.
- Breadcrumbs on every detail page (e.g. `Home › Impetus › Photoshoots › <title>`). The Brands PLP doesn't have child pages, so its breadcrumb stops at "Brands".

---

## 5. Page Specs

### 5.1 Home (`/`)

Mirrors the reference register's cover page.

**Section §00 · Cover**
- H1: "The Fynd Create design library."
- Lede paragraph: ~40 words explaining what's collected here, where it came from, and that it's continuously updated as new linesheets land.
- Counter strip (5 stat blocks, Inter 700 / large numerals):
  - `876` unique designs
  - `7` brands
  - `4` photoshoots · `14` images (sample — more delivered)
  - `<N>` videos · `<runtime>` total runtime
  - `4` India-market intelligence reports

**Section §01 · Brands**
- Numbered card grid (3 cols desktop, 1 col mobile), one card per brand.
- Card shows: brand name (H3), image count, gender mix bar (e.g., `womens 50% · mens 50%`), top 3 categories, latest linesheet date, `Open →` link.
- Cards in alphabetical order by brand slug.

**Section §02 · Photoshoots**
- Numbered card grid, one card per AI-generated photoshoot set.
- Card shows: photoshoot title (H3), brand chip (if tied), shot count, hero image thumbnail, generated date, `Open →`.

**Section §03 · Videos**
- Numbered card grid, one card per AI-generated video.
- Card shows: video title (H3), brand chip, duration, aspect-ratio chip (16:9 / 9:16 / 1:1), poster frame, `Watch →`.

**Section §04 · Category Intelligence**
- Same card grid pattern.
- Card per report: title, season, market (always India in v1), status, `Open PDF →`.

**Section §05 · Explore**
- Single CTA card: "Browse the full library by brand, gender, category." → `/brands` (the PLP).

**Section §06 · How this is built**
- "How to read" rules block inherited verbatim. Adapted rules:
  1. One brand = one card.
  2. Every image traces back to a linesheet + slide number.
  3. Categories normalized to a controlled vocabulary; aliases mapped in `tools/gdrive_download/pptx_extract.py` (`CATEGORY_ALIASES`).
  4. Gender comes from deck-level evidence; mid-deck shifts are honored (e.g., Ajio).
  5. Reports are evidence-tagged (RUNWAY · RETAIL · SEARCH · SOCIAL · TRADE · FORECAST).
  6. Last verified date on every page, sourced from `index.json.generatedAt`.

**Footer (inverted)**
- Owner · Last verified · Version · Strict internal circulation.

### 5.2 Brands (`/brands`) — single PLP

The Brands surface is a **single PLP** filterable by gender × category × brand. Replaces the old per-brand index + per-brand-detail + separate /explore (all merged here).

- Hero: H1 "Brands.", lede explaining what's in the catalog (876 unique designs deduped by sha256 from 1,128 total) + sub-nav.
- Three filter-chip rows: **Gender** · **Category** · **Brand**. Each chip shows count. "All" chip resets that dimension. Filters AND together.
- Result strip: `<count> designs · clear filters`.
- Image grid: 6-col desktop (4 tablet, 2 mobile). Square crops, lazy-loaded from CDN.
- Click any tile → lightbox with full-resolution image + brand · slide · category metadata.
- Pagination: first 120 designs render immediately, infinite-scroll loads the rest in batches of 120 as the user nears the bottom (plus a "Load more" button for explicit control).
- Dedup is **always on** in v1 (one tile per unique sha256).
- No per-brand detail pages; no separate /explore. The brand chip filter is the brand drilldown.

### 5.5 Photoshoots index (`/photoshoots`)

- Numbered card grid (3 cols desktop, 1 col mobile), one card per shoot.
- Eyebrow strip above the grid: `A SELECTION FROM THE FYND CREATE AI PHOTOSHOOT PIPELINE · ALL LIVE` — surfaces that this is a representative sample, not the full inventory (driven by `data/photoshoots.json.note`).
- Card shows: shoot title (H3), brand chip (separate registry — `asos`, `trends`, `buda-jeans`, …), marketplace chip (`AJIO`), type chip (`marketplace listing` / `showcase` / `campaign`), shot count, hero thumbnail, `Open →`.
- Filter chips at top: brand chips + type chips. Optional gender filter when at least one brand is selected.
- Status pills follow the source register's pattern (`LIVE` only — none of the entries are WIP).
- v1 brand registry (separate from `/brands` and `/videos`):
  `asos (1)` · `trends (1)` · `buda-jeans (2)`. Marketplace = `ajio` for all.

### 5.6 Photoshoot detail (`/photoshoots/<slug>`)

The page renders **one of three layouts** based on the entry's `type`. No type → fall back to the campaign layout.

#### Type: `marketplace-listing` (e.g. AJIO × ASOS)
- Hero strip: title, brand + marketplace chips, "6 SKUs live · 65+ in pipeline · 1-day processing · 2-day go-live".
- Achievement callout: "Consistent plus-size model face across all SKUs. Zero manual retouching."
- Team credits row: ML team, QC.
- SKU grid: one tile per SKU. Tile shows the model image (when collected) and color name. Click → outbound link to the marketplace product page.
- Per-tile state: ✓ image collected, ⚠ image pending (link-only).

#### Type: `showcase` (e.g. SS26 PLM)
- Hero strip: title, brand + marketplace chips, season badge, summary.
- Use-cases row: 3 chips (Buying feedback · Demand signal testing · Cataloguing).
- Stats panel (Inter 700, large numerals): styles processed · images processed · style acceptance rate · styles rendered.
- Examples grid: input ↔ output pairs side-by-side. Each row = one styleCode, with input on the left (sketch / tech-pack / flat-lay) and output on the right (studio / lifestyle render). Standalone outputs (no paired input) get a single full-width tile.

#### Type: `campaign` (e.g. Buda Jeans × Harry Potter / × Valentine's Day)
- Hero strip: title, brand + marketplace chips, collection name + gender chip, summary.
- Image grid: 2-col desktop, full aspect ratios preserved. Each tile labels the graphic, colorway, and any licensing note (e.g. "Licensed: Disney").
- Click → lightbox with prev/next.

**All three layouts share:**
- Footer: "Selection from broader delivered set" + last-verified date.
- No cross-link to `/brands/<slug>` — photoshoot brands (asos / trends / buda-jeans) don't appear in `/brands` (which holds linesheet brands).

### 5.7 Videos index (`/videos`)

- Card grid, one card per video. Source: `data/videos.json` (29 videos across 9 brands in v1, generated by `tools/build_videos_index.py` from `docs/Fynd Studio - Portfolio.xlsx`).
- Card: title, brand chip, platform chip (`YouTube` · `YouTube Shorts` · `Instagram Reel`), thumbnail (YouTube auto, Instagram fallback to brand-color placeholder until posters are added).
- Filter chips at top: brand chips (9), platform chips (3). No gender filter (videos aren't gender-tagged in v1).
- Default sort: by brand → title.
- v1 brand registry (separate from `/brands` linesheet brands):
  `reliance-jewels (5)` · `metro-wholesale (7)` · `swadesh (5)` · `satya-paul (4)` · `nmacc (4)` · `reliance-digital (1)` · `jiomart (1)` · `dnmx (1)` · `superdry (1)`

### 5.8 Video detail (`/videos/<slug>`)

- Embedded player, sized to the platform's native aspect:
  - YouTube long-form: `<iframe src="https://www.youtube.com/embed/<id>">` at 1200 × 675 (16:9).
  - YouTube Shorts: same `embed/<id>` URL at 405 × 720 (9:16).
  - Instagram Reel: `<iframe src="https://www.instagram.com/reel/<shortcode>/embed/">` at 405 × 720.
- Header strip: title (H2), brand chip, platform chip, `Open on <platform> →`.
- No file size / codec / download — these are external embeds, not files we own.
- Cross-link: "More from this brand" → filtered `/videos?brand=<slug>` if more than one video for that brand.
- No `/videos/<slug>/<variant>` sub-routes — each platform URL is its own video record.

### 5.8.1 Inclusion / exclusion rules (encoded in `tools/build_videos_index.py`)

- **Source:** all rows of `docs/Fynd Studio - Portfolio.xlsx`.
- **Excluded by title substring** (15 rows in v1):
  - Fynd-self / ambiguous: `What Makes us Humans`, `Raju Video SOF`, `SOF Fynd ...`, `Fynd AI OS`, `AI Home Tour`, `AI Video Magic Mirror`, `Hacktimus`
  - Non-Reliance brands: `Nasher Miles ...`, `The Sleep Company`, `Neck Pillow by The Sleep`
- **Brand assignment:** title-keyword regex table (see `BRAND_RULES` in the script). Rows that don't match any keyword are reported as warnings (not silently dropped).
- Re-run with `.venv/bin/python tools/build_videos_index.py`.

### 5.9 Category Intelligence index (`/category-intel`)

- Card grid, one card per **India-market** report folder under `~/Documents/work/trend-engine/reports/*-india`. ANZ and other-market reports are excluded in v1.
- Each card: title (from folder name + report metadata), season badge, gender badge, page count, file size, `Open PDF →`.
- Filter chips at top: `Mens · Womens · SS · AW`. (No market filter — India only.)
- v1 source set (4 reports, all under `*-india/output/`):
  - `mens-polos-aw26-india/output/mens-polos-aw26-category-report.pdf`
  - `mens-shirts-ss27-india/output/mens-shirts-ss27-category-report.pdf`
  - `mens-tshirts-ss27-india/output/mens-tshirts-ss27-category-report.pdf`
  - `midi-dress-ss27-india/output/midi-dress-ss27-category-report.pdf`
  - `midi-dress-ss27-india/output/midi-dress-ss27-trend-report.pdf` (second PDF on the same card; "Category report" / "Trend report" tab toggle)

### 5.10 Report detail (`/category-intel/<slug>`)

- **Embedded PDF viewer** (browser-native `<iframe>` / `<object>` to the bucket-hosted PDF, with a download button as fallback).
- Header strip above the viewer: title, season + gender badges, page count, file size, `Download PDF`, `Open in new tab`.
- For reports with multiple PDFs (currently only `midi-dress-ss27-india`), tab toggle between them — same page, no extra route.
- No markdown rendering, no TOC, no inline charts. The PDF is the source of truth for layout and content; the website is just a wrapper that surfaces it. This keeps the website out of the report's editorial design path.
- Cross-link out to the relevant brand category in `/brands` (e.g., "Mens T-Shirts SS27 India" → `/brands` filtered to mens × t-shirt).

### 5.11 (removed)

`/explore` was merged into `/brands` — see §5.2. There is no separate Explore surface in v1.

### 5.12 (removed)

`/about` was removed in v0.7. Methodology lives in this spec; readers don't need a public-facing About page in v1.

---

## 6. Tech Stack

- **Framework:** **Plain static HTML + vanilla CSS**, matching the existing reliance-retail-fynd repo (`index.html` + `style.css` + per-track folders, deployed on Vercel with `cleanUrls: true`). No Next.js, no build system in v1. CSS variables already defined in `style.css` (`--ink`, `--bg`, `--accent #6B5BD6`, etc.) — design tokens are inherited directly.
- **Optional escape hatch:** if a surface (likely `/brands` PLP) becomes painful to maintain as generated HTML, introduce **Astro** as a static site generator. Astro outputs the same plain HTML the rest of the repo serves; no other moves needed.
- **Typography:** Inter + JetBrains Mono via Google Fonts `<link>` (already loaded in the existing pages).
- **Image hosting:** **new dedicated GCS bucket** (provisional name `fynd-create-portfolio`, region `asia-south1` Mumbai for proximity to Indian reviewers). Public-read bucket; Vercel serves the rest of the page over HTTPS, images linked directly. To provision: `gcloud storage buckets create gs://fynd-create-portfolio --location=asia-south1 --uniform-bucket-level-access` then grant `allUsers:objectViewer`.
- **PDF hosting:** same GCS bucket; embedded in-page via `<iframe>` / `<object>` with download fallback. No PDF.js or custom viewer in v1.
- **Video hosting:** **none — videos are external.** Embedded via the platforms' own iframes:
  - YouTube: `https://www.youtube.com/embed/<id>` (long-form and Shorts both work).
  - Instagram Reels: `https://www.instagram.com/reel/<shortcode>/embed/`.
  - No `ffmpeg`, no posters to generate from MP4, no GCS video bytes.
- **Video thumbnails:** YouTube's auto-generated `https://i.ytimg.com/vi/<id>/{maxresdefault,hqdefault}.jpg` cached into `images/video-thumbs/` at build time. Instagram reels (2 in v1: NMACC Wicked, Metro 72Hr) get a **brand-color flat tile placeholder** rendered at build time — no manual screenshots, no oEmbed dance.
- **Search/filter:** all client-side (the indexes are small — combined ~1.5 MB JSON gzipped). No need for a search service in v1.
- **Analytics:** none in v1; add Plausible if needed.
- **Auth:** **Vercel Password Protection** (Pro plan feature). Single shared password set in Project → Settings → Deployment Protection. Easier to share with external reviewers (RRVL apex, partners) than per-user SSO. Apply to both production and preview deployments.

---

## 7. Decisions Resolved · Open Items

### Resolved (2026-04-30 review)

| # | Decision | Outcome |
|---|---|---|
| 1 | GCS bucket | New bucket `gs://fynd-create-portfolio` in `asia-south1` (Mumbai) |
| 2 | Auth posture | Vercel Password Protection (single shared password, both prod + preview) |
| 3 | Lee Cooper / cross-brand triage | Accept the gap for v1 — Lee Cooper `category=null`, cross-brand `brand=_unsorted` |
| 4 | Linesheet PDF preview | No — images only. Source `.pptx` stays local. |
| 5 | Image dedup | **Dedup by default**, with a "Show duplicates" toggle. Default view = 876 unique. |
| 6 | Video categories | Skip for v1. `category=null` on every record. Brand + platform filters only. |
| 7 | Instagram reel posters | Brand-color flat-tile placeholder rendered at build time. No screenshots, no oEmbed. |

### Still open

(none blocking v1)

### Resolved late (post 2026-04-30 photoshoot batches)

| # | Decision | Outcome |
|---|---|---|
| 8 | Photoshoots source / pipeline | Manual hand-curation into `data/photoshoots.json` + drop images into `images/photoshoots/<slug>/`. No scripted ingestion in v1 — entries are too varied (marketplace listings vs showcases vs campaigns). |
| 9 | Photoshoot tagging vocab | Separate brand registry from designs and videos. Brands in v1: `asos`, `trends`, `buda-jeans`. All `marketplace: ajio`. |
| 10 | Photoshoot stills in PLP | **Segregated to `/photoshoots`**. Designs PLP (`/brands`) holds linesheet designs only; photoshoots are their own surface. |
| 11 | Photoshoot framing | Catalog is a curated representative sample of broader delivery. Eyebrow on `/photoshoots` + `note` field surface this. All entries `status: live`. |

### Operational notes (not decisions)

- Videos: when a new Reliance-umbrella brand appears in the source sheet, `tools/build_videos_index.py` will report it as "unmapped" and skip the row. Add a new pattern to `BRAND_RULES` and re-run.
- Photoshoots: when a new shoot lands, append to `data/photoshoots.json` (no script). Drop images into `images/photoshoots/<slug>/` (gitignored). Update `totals.shoots` and `totals.imagesCollected`.

---

## 8. Phased Build Plan

### Phase 1 — Static portfolio (1 week)
- Provision GCS bucket: `gcloud storage buckets create gs://fynd-create-portfolio --location=asia-south1 --uniform-bucket-level-access` + grant `allUsers:objectViewer`.
- Sync extracted images to bucket: `gsutil -m rsync -r images/ gs://fynd-create-portfolio/images/`.
- Add Brands surface to the existing static HTML repo (no Next.js): `brands/index.html`, `brands/<slug>/index.html`, `brands/<slug>/<linesheet>/index.html`.
- Reuse `style.css` design tokens already defined in the repo. Add only what's new (image grid, lightbox, masonry).
- Deploy to Vercel preview.

### Phase 2 — Brands PLP filters (folded into Phase 1)
- The Brands surface (§5.2) IS the PLP. Gender × category × brand chips, lightbox, infinite-scroll.
- No separate /explore.

### Phase 3 — Category Intelligence (2-3 days)
- Sync the 4 India-market PDFs to the GCS bucket (done — at `<CDN>/pdfs/<slug>/`).
- `/category-intel` index card grid + `/category-intel/<slug>` PDF embed.
- Tab toggle for the midi-dress 2-PDF case.
- Cross-links into `/brands` (filtered).

### Phase 3.5 — Videos (1-2 days)
- `data/videos.json` is already generated by `tools/build_videos_index.py` (29 videos in v1).
- Build `/videos/index.html` (card grid with brand + platform filter chips) and `/videos/<slug>/index.html` (embedded YouTube/Instagram iframe).
- Cache YouTube thumbs into `images/video-thumbs/` at build time.
- Render brand-color flat-tile placeholders for the 2 Instagram reels.

### Phase 3.6 — Photoshoots (1-2 days)
- `data/photoshoots.json` is hand-curated; 4 entries · 14 images in v1.
- Build `/photoshoots/index.html` (card grid + sample-set framing eyebrow).
- Build `/photoshoots/<slug>/index.html` with three layouts dispatched on `type`: `marketplace-listing`, `showcase`, `campaign`.
- Sync images to GCS bucket alongside the linesheet images.

### Phase 4 — Polish + auth (1-2 days)
- Enable Vercel Password Protection (Project → Settings → Deployment Protection → Password) for production + previews. Set the shared password.
- Final design pass against the reference site for parity.
- Last-verified dates wired from data sources.

### Phase 5 (optional) — Tagging tool
- Tiny browser tool to triage Lee Cooper + cross-brand `_unsorted/` images.
- Writes to `overrides.json`. Re-run build to apply.

---

## 9. Out of Scope (v1)

- Editing tools — view-only.
- Image upload / new-linesheet ingestion via UI — still a Python pipeline rerun.
- Comments / annotations.
- Multi-tenant or per-user views.
- Analytics dashboards on top of the design library (count of variants, time series, etc.) — could be Phase 6.
- Full-text search across reports (filter chips suffice for 4 PDFs; revisit at 30+).
- ANZ and other non-India market reports (currently 3 reports excluded: `mens-activewear-aw27-anz`, `womens-activewear-aw27-anz`, `womens-smart-casual-aw27-anz`).
- In-page rendering of report content from `content.md` / `data.ts` / `generate.tsx` — site only links to / embeds the published PDF.

---

## Appendix A — Vocabulary Reference

**Three independent brand registries** (no cross-mapping in v1):

- **Linesheet brands** (`/brands`): `ajio`, `john-players-jeans`, `kg-frendz`, `lee-cooper-kids`, `rio`, `superdry`, plus the cross-brand bucket `_unsorted` (split target: `rio` / `fig` / `dnmx`).
- **Photoshoot brands** (`/photoshoots`): `asos`, `trends`, `buda-jeans`. All `marketplace: ajio`.
- **Video brands** (`/videos`): `reliance-jewels`, `metro-wholesale`, `swadesh`, `satya-paul`, `nmacc`, `reliance-digital`, `jiomart`, `dnmx`, `superdry`.

**Genders:** `womens`, `mens`, `kids`, `kids-boys` (extend with `kids-girls`, `unisex` as needed).

**Design categories (canonical, post-alias):** `t-shirt`, `sweatshirt`, `shirt`, `printed-shirt`, `stripe-shirt`, `aop-polo`, `aop-shirt`, `polo`, `shacket`, `leggings`, `dress`, `shirt-dress`, `oversized-shirt-dress`, `jumpsuit`, `skirt`, `pencil-skirt`, `top`, `peplum-top`, `peplum-blouse`, `cowl-dress`, `lounge-set`, `henley-tee`, `co-ord-set`. Defined by `CATEGORY_ALIASES` in `tools/gdrive_download/pptx_extract.py`.

**Themes (designs):** `sun-drenched-escape`, `urban-playground`, `coastal-rhythm`, `retro-reboot`, `aop`, `embellished`, `licensed`. Free-text; not enumerated.

**Photoshoot types:** `marketplace-listing` · `showcase` · `campaign`.

**Photoshoot image kinds:** `model` · `studio` · `lifestyle` · `flat-lay` · `tech-pack` · `design-sketch`.

**Video platforms:** `youtube-long` · `youtube-shorts` · `instagram-reel` · `instagram-post`.

**Report seasons:** `ss27`, `aw26`, `aw27`, etc. **Markets:** `india` (only one in v1; ANZ excluded). Slug pattern: `<gender>-<category>-<season>-<market>`.

---

## Appendix B — Reference Patterns to Copy Verbatim

From [reliance-retail-fynd.vercel.app](https://reliance-retail-fynd.vercel.app):

- The `§ NN · LABEL` eyebrow + H2 section header.
- The `01 · CATEGORY  STATUS` card pattern (where CATEGORY = "Platform" / "Vertical", STATUS = "LIVE" / "BUILDING" / "PILOT"). For us: `01 · BRAND  READY`, `02 · BRAND  DRAFT`, etc.
- Dense table format with muted small-caps column heads.
- "How to read" rule grid, inverted dark footer.
- Confidentiality marker in the top nav (`Confidential · v0.1 · Apr 29`).
- "Sources" footer on every detail page, listing the underlying data sources with links.

---

## Appendix C — Data Contracts

### `images/index.json` (designs)

Produced by `tools/gdrive_download/build_index.py`. Site consumes:

- `brands.<brand>.linesheets.<slug>[]` — flat list of image records.
- `byGender` / `byCategory` / `byGenderCategory` / `byGenderCategoryBrand` — pivot maps of `{key: [paths]}`.
- Per-image fields: `path`, `mime_type`, `bytes`, `width`, `height`, `sha256`, `gender`, `category`, `category_slug`, `theme`, `theme_slug`, `slide_number`, `slide_title`, `seq_in_slide`, `linesheet`, `source_file`.

Rebuild:
```
.venv/bin/python -m gdrive_download.build_index \
  --pptx-dir linesheets --output images
```

### `data/videos.json` (videos)

Produced by `tools/build_videos_index.py`. Site consumes:

- `videos[]` — flat list of video records.
- `totals.byBrand` / `totals.byPlatform` — for the home counter and filter chips.
- Per-video fields: `slug`, `title`, `brand`, `platform` (`youtube-long` | `youtube-shorts` | `instagram-reel` | `instagram-post`), `videoId`, `url`, `embedUrl`, `thumbUrl`, `category`, `sourceRow`.

Rebuild:
```
.venv/bin/python tools/build_videos_index.py
```

### `data/photoshoots.json` (photoshoots)

Hand-curated; no script in v1. Site consumes:

- `note` — top-of-page eyebrow framing ("representative sample · all live").
- `totals.shoots` / `totals.imagesCollected` — home counter.
- `shoots[]` — flat list of shoot records.

Per-shoot fields:
- Always: `slug`, `title`, `type` (`marketplace-listing` | `showcase` | `campaign`), `status: "live"`, `brand`, `marketplace`, `publishedAt`, `summary`.
- `marketplace-listing` adds: `model`, `stats` (skusLive, skusInPipeline, processingDays, timeToLiveDays, manualRetouching), `team[]`, `skus[]` (each has `sku`, `color`, `url`, optional `image`), `narrative`.
- `showcase` adds: `useCases[]`, `dataset` (season, stylesAnalysed, imagesAnalysed), `stats` (acceptance rates), `pilot` (stylesGenerated, imageTypes), `examples[]` (each has `styleCode`, `category`, optional `input`, `output`).
- `campaign` adds: `collection`, `gender`, `images[]` (each has `path`, `graphic`, `colorway`, optional `licensed`).

Image record fields: `path` (relative to GCS root), `width`, `height`, `bytes`, `kind` (`model` | `studio` | `lifestyle` | `flat-lay` | `tech-pack` | `design-sketch`).

Update workflow: edit JSON by hand, drop new images into `images/photoshoots/<slug>/`, bump `totals`.
