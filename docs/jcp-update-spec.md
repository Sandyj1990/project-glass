# JCP page update · Accenture deck integration · Spec

**Status:** v0.4 · 2026-05-01 · §9 signed off (incl. Agentic Commerce destination + Sub-IPs rehome) · ready to implement
**Owner:** Kushan Shah
**Routes:**
- `/jcp/` — **major prune + Accenture-deck augment.** Cut 5 sections (105-row B2C roster, 7-row B2B roster, headcount snapshot, Sub-IPs, Deep cards). Move 3 sections out (UCP → /ucp, ZIP+JIIA cards → /kaily, GlamAR card → /pixelbin). Modify hero stats. Insert new Ecosystem section. Replace AI Cataloging block with a CTA card pointing at the deep-dive.
- `/jcp/channels/` — swap 8 Play Store screenshots for the cleaner Accenture-deck UI shots; un-skip 3 channels (Trends, RCPL, JioMart Digital) so they show as mobile-app cards.
- `/jcp/cataloging/` — refresh with slide-19 numbers (15 days → 5 hours · AI Photoshoot Studio · AI Generated Video).
- `/ucp/` — replace the "Page in progress" stub with the UCP section lifted from `/jcp/`. Extension deferred.
- `/kaily/` — replace the "Page in progress" stub with the ZIP (AJIO) + JIIA (JioMart) cards lifted from `/jcp/`. Plus the slide-37 ZIP image as hero.
- `/pixelbin/` — replace the "Page in progress" stub with the GlamAR card lifted from `/jcp/`, plus the slide-41 PixelBin umbrella content (PixelBin · Fynd Studios · Fynd Snap · GlamAR).
- `/catalog/` — append 19 sub-IP rows lifted from the Sub-IPs section being cut from `/jcp/`.
**Source content:** `docs/jcp-notes-compilation/Updated Retail Platforms+Agents_ Accenture - Apr 16, 2026-2.pptx` · slides 31-35 (JCP) + slide 19 (Cataloging) + slide 37 (ZIP) + slide 38 (GlamAR) + slide 41 (PixelBin)
**Source index:** `docs/accenture-2026-04-16-compilation/INDEX.md` — topic-organized navigation for the deck. Use that index for any verbatim copy + image CDN URLs (don't re-parse).
**Narrative anchor:** Farooq's 2026-04-30 letter — *"Jio Commerce Platform — implementation and impact across RRL, RBL, and RRVL."* The Accenture deck is the highest-fidelity public-facing source on JCP scale + ecosystem; the register should match it.
**Inherits from:** `docs/website-orientation-spec.md` · §3 page template · register copy via `website-tone-of-voice` skill

---

## 1. Why this page exists

**Audience.** RIL Apex leadership (MM Sir level) reviewing the register at `reliance-retail-fynd.vercel.app`. Copy must be apex-readable: factual, scannable, no marketing voice, no Fynd self-praise, names where they matter, claims that survive challenge.

**Gap to close.** Two specific gaps:

1. **Numbers drift.** `/jcp/` today claims *"350K+ peak orders / hour · 50K+ orders / min · 300M+ customers · 78 channels"*. The Apr-16-2026 Accenture deck (slide 35) reports the FY 2025-26 ecosystem numbers as **700K+ orders/day · 30K+ stores served · 200M+ customers · 50K+ orders/min**. Slide 32 reports the historic peaks as **300M+ customers served · 350K+ peak per hour order**. Slide 31 reports the channel split as **7 B2B businesses · 105 B2C businesses · 32K+ stores**. The register should pick one canonical set per stat tile and source-cite it.

2. **App screenshots are weak.** `/jcp/channels` uses Google Play Store screenshots for 12 mobile apps. Some of those are promo cards (JioMart, Milkbasket, 7-Eleven) rather than clean UI. The Accenture deck slides 33-34 supply purpose-built app screenshots for 8 of those apps — apex-quality renders, not marketing tiles. The register should switch to those.

**Why this belongs in the apex register.** The Accenture deck is the canonical externally-vetted JCP narrative. The register's `/jcp/` page is the most-clicked surface from the home register; mismatched numbers between it and the deck reads as carelessness at apex level. The `/jcp/channels/` gallery is the highest-signal visual asset on the site; cleaner shots compound credibility.

---

## 2. Source inventory

| Source | Type | Path | Key facts derivable |
|---|---|---|---|
| Accenture deck · slide 31 | Title slide · brand wall + scale | `docs/jcp-notes-compilation/Updated Retail Platforms+Agents_ Accenture - Apr 16, 2026-2.pptx` slide 31 | "Jio Commerce Platform: Scale" · 7 B2B Businesses · 105 B2C Businesses · 32K+ Stores · 1 brand-collage image of ~36 brands |
| Accenture deck · slide 32 | Enterprise commerce overview | same · slide 32 | Subtitle: *"Powering seamless shopping experiences across online and stores—faster, smarter, and at scale"* · 300M+ customers served · 350K+ Peak per Hour Order · framing: B2B / In-store / B2C platforms · brands referenced: Smart Greens, Fruits & Vegetables, Reliance Consumer Brands |
| Accenture deck · slide 33 | B2C Snapshot | same · slide 33 | Date range: Nov 2024 → Dec 2025 · 4 named B2C apps: JioMart Quick Commerce, In-Store Companion × AJIO (TRENDS), TIRA Beauty Platform, AJIO Fashion Marketplace · 4 phone-frame UI screenshots |
| Accenture deck · slide 34 | B2B Snapshot | same · slide 34 | 4 named B2B platforms: RCPL · Metro Kirana Platform · JioMart Digital B2B · JioMart Digital ASP · 4 phone-frame UI screenshots |
| Accenture deck · slide 35 | Ecosystem · scale of retail transformation · FY 2025-26 | same · slide 35 | 700K+ Orders/Day · 30K+ Total Stores Served · 200M+ Customers · 50K+ Orders/Min · 9 capability cards: Microservice-Based Platform · Accelerated Go-To-Market · Eliminating Redundancy · Cross-Tech Leverage (15+ retail extensions) · Optimized Resourcing · AI Documentation & Learning (Danswer) · Modular & Flexible Architecture · Centralized Governance · Seamless Scalability |
| Existing `/jcp/index.html` | Live register page | `jcp/index.html` | Current claims: 78 channels, 68 live, 350K+ peak/hr, 50K+/min, 300M customers, 105 B2C in roster, 7 B2B in roster |
| Existing `/jcp/channels/index.html` | Live channels gallery | `jcp/channels/index.html` | Generated by `tools/build_jcp_channels_page.py` from `tools/scratch/non_rbl_play.json` · 12 mobile apps with Play Store screenshots |

**Aggregate KPIs after this update:**
- **Daily**: 700K+ orders/day (slide 35) — *new*
- **Peak**: 350K+ peak orders / hour, 50K+ orders / min (slide 32) — *retained from existing*
- **Customers**: 300M+ served (slide 32) AND 200M+ FY 2025-26 (slide 35) — *both, distinguished by frame*
- **Channels**: 78 channels in register (existing PDF), 105 B2C + 7 B2B businesses (slide 31), 30K+ stores served (slide 35), 32K+ stores (slide 31)
- **Architecture**: 9 capability claims (slide 35) — *new*

---

## 3. Page structure

### 3.1 · `/jcp/` rewrite

The page has 13 existing sections. **5 cut, 2 moved out, 1 modified, 1 inserted, 5 retained.**

#### Inventory of existing sections

| # | Section | Verdict | Reason |
|---|---------|---------|--------|
| 0 | Hero stat strip | **MODIFY** | Change A · re-source to slides 31, 35 |
| 1 | B2C Snapshot — 4-card grid (JioMart / AJIO / Tira / Companion) | **RETAIN** | apex-relevant snapshot |
| 2 | B2B Snapshot — Reliance B2B · single platform | **RETAIN** | apex-relevant snapshot |
| 3 | Full B2C roster · 105 businesses (verified subset table) | **CUT** | duplicates `/jcp/channels/` |
| 4 | JCP team · headcount snapshot (~140) | **CUT** | not central to platform narrative |
| 5 | Full B2B roster · 7 businesses (table) | **CUT** | duplicates `/jcp/channels/` |
| 6 | Sub-IPs · 19 modules under JCP | **MOVE** | → `/catalog/` (lift the 19 module rows before deleting from /jcp/) |
| – | (NEW) Ecosystem · 9 capability cards | **INSERT** | Change B · slide 35 verbatim |
| 7 | Deep cards · "Outcome · evidence · reach · next" | **CUT** | not apex-valuable |
| 8 | UCP — Unified Customer Platform | **MOVE** | → `/ucp/` (replaces current stub); extension deferred |
| 9 | Agentic Commerce — three agents in production | **SPLIT** | ZIP (AJIO) + JIIA (JioMart) → `/kaily/` · GlamAR → `/pixelbin/` |
| 10 | Vertex Search — uplift over Algolia | **RETAIN** | search infra is JCP-specific |
| 11 | AI Cataloging — ~14 sec per brand | **REPLACE** | shrink to a CTA card *"AI Cataloging · ~14 sec/brand · see deep-dive →"* pointing at `/jcp/cataloging/`; the deep-dive page gets the slide-19 refresh |
| 12 | AJIO × JCP migration — Apex deadline met | **RETAIN** | named Apex commitment delivered |
| 13 | Ecosystem & differentiation (closing section) | **RETAIN** | apex-tier closer |

**Result:** /jcp/ goes from 13 sections → 8 sections (4 retained + 1 modified hero + 1 new ecosystem + 1 CTA card for cataloging + 1 closer). Roughly halves the page weight while raising signal.

### 3.2 · `/jcp/cataloging/` refresh

Slide 19 ("Impetus AI Native Cataloging & Photoshoots") is the canonical pitch. Update the existing deep-dive with:
- **Headline number:** *"Before 15 days · After 5 hours"* — full-width callout
- **Outcomes (4 cards):** Scalable & Fast · Face Consistency · AI generated models library (ethnicity, age, size, gender) · Better sales conversions with videos
- **Pipeline visual:** Mannequin Image → AI Photoshoot Studio Visual → AI Enriched Catalog → AI Generated Video
- Use slide-19 images from CDN: `https://socialassets.impetusz0.de/rrl-portfolio/assets/accenture-2026-04-16/slide_19/img_<NN>.png`
- Source line: *"Source · Accenture · Updated Retail Platforms+Agents · Apr-16-2026 · slide 19"*

### 3.3 · `/kaily/` — first content version (replaces stub)

Lift these two cards from /jcp/'s Agentic Commerce section before deletion:

- **ZIP · AJIO Commerce Agent** — Live on AJIO.com. 88% positive CX · 86% catalog covered · 2M+ discovery chats. *"An AI Agent That Shops With You, Not Just For You."* Slide-37 image as the hero (`assets/accenture-2026-04-16/slide_37/img_01.png` on CDN).
- **JIIA · JioMart Agentic Shopping Assistant** — Google Cloud Next '26 keynote · 29-Apr-2026. 40M+ images indexed. Gemini multimodal. Team named.

Page hero: *"Kaily · agentic commerce live on AJIO and JioMart."* (per Farooq's letter framing).

Page structure: hero → ZIP card (with slide-37 image) → JIIA card → source line. Section count: 1 hero + 2 cards + 1 source = ~3 sections. Single-page section per `website-section-authoring` skill (~6 sub-pages or fewer → hand-author).

### 3.4 · `/pixelbin/` — first content version (replaces stub)

Two layers of content:

**Layer 1 · slide 41 (PixelBin umbrella):** *"New age marketing and entertainment with AI."* Sub-products with scale stats:
- PixelBin · 5,000+ images
- Fynd Studios · 50+ AI Ads
- Fynd Snap · 25 K photoshoots
- GlamAR · 200+ AR/VR

**Layer 2 · GlamAR card lifted from /jcp/'s Agentic Commerce:**
- *AI-first 3D, AR, and VR commerce platform.* Live on Sephora · Vision Express · LensCrafters · WestElm.
- 40% return reduction · 106% revenue per visit · 90% engagement lift
- Saturdays: VTO converts at 32% vs 9% · Foxtale: AI Skin Analysis 1.6× higher conversion

Single-page section. ~3 sections (umbrella → GlamAR detail → source).

### 3.5 · `/catalog/` — append 19 sub-IP rows

Extract the 19 sub-IP module names + 1-line descriptions from `/jcp/index.html` *before* deleting that section. Append to `/catalog/index.html` as new rows under a "JCP sub-IPs" group (or merge into the existing IP table — verify the catalog's structure during P3).

#### Change A · Hero stat strip (existing §0) — re-source numbers to the Accenture deck

**Current** (`jcp/index.html` line 99-101):
```
Peak orders / hour · 350K+
Orders / min · peak · 50K+
Customers served · 300M+
```

**New** — keep the four-tile layout but re-label per slide 35 framing:
```
Tile 1 · Orders / day        700K+    (FY 2025-26 · slide 35)
Tile 2 · Orders / min · peak  50K+    (slide 35)
Tile 3 · Customers · FY26    200M+    (slide 35)
Tile 4 · Stores served       30K+     (slide 35)
```

Plus a second 4-tile row reused from existing:
```
Tile 5 · Total channels       78      (PDF)
Tile 6 · B2C businesses      105      (slide 31)
Tile 7 · B2B businesses        7      (slide 31)
Tile 8 · Verticals covered    10      (existing)
```

Source line below the strip: *"Source · Accenture · Updated Retail Platforms+Agents · Apr-16-2026 · slides 31, 32, 35"*.

#### Change B · New section `§ Ecosystem` — 9 capability cards from slide 35

Insert as a new section between the existing "Sub-IPs · 19 modules" and "Deep cards" sections.

- **Section label:** `Ecosystem · scale of retail transformation · FY 2025-26`
- **H2:** *"Why JCP scales the way it does."*
- **Component:** 3-column card grid (3 rows × 3 columns) from slide 35
- **Card content** (verbatim from slide 35):

| # | Title | Subtitle |
|---|-------|----------|
| 1 | Microservice-Based Platform | Modular, scalable, and interoperable services |
| 2 | Accelerated Go-To-Market | Pre-built features accelerate launches |
| 3 | Eliminating Redundancy | Streamlined workflows for faster cycles |
| 4 | Cross-Tech Leverage | 15+ retail extensions enhance efficiency |
| 5 | Optimized Resourcing | Unified tech stack lowers manpower needs |
| 6 | AI Documentation & Learning | Strengthening the ecosystem with Danswer |
| 7 | Modular & Flexible Architecture | Adaptable across diverse business verticals |
| 8 | Centralized Governance | Centralized compliance ensures alignment |
| 9 | Seamless Scalability | Easily scalable infrastructure solutions |

- **Source line:** *"Source · Accenture · Updated Retail Platforms+Agents · Apr-16-2026 · slide 35"*

#### ~~Change C · Brand wall~~ — _cut per §9.2 decision_

The slide-31 brand collage will not be used on `/jcp/`. The 105-row verified-subset table is the only roster surface.

### 3.2 · `/jcp/channels/` swap

Replace the Play Store first-screenshot for these 8 channels with the Accenture-deck UI shot (one per channel, full-bleed inside the existing app-card frame). Channels NOT listed below keep their existing Play Store shot.

| Slug | Source slide / image | Replaces |
|---|---|---|
| `jiomart` | slide 33 / img_03.png (JioMart Quick Commerce home) | `images/jcp-channels/jiomart/shot-2.png` (current pick) |
| `tira` | slide 33 / img_04.png (TIRA top-categories home) | `images/jcp-channels/tira/shot-5.png` |
| `ajio` | slide 33 / img_06.png (AJIO Wrogn home + ICICI promo) | `images/jcp-channels/ajio/shot-4.png` |
| `metro-kirana` | slide 34 / img_04.png (Metro Wholesale home + Stock Clock) | `images/jcp-channels/metro-kirana/shot-2.png` |
| `reliance-digital` | slide 34 / img_03.png (Reliance Digital Connect, Bangalore) | `images/jcp-channels/reliance-digital/shot-1.png` |
| `jiomart-digital` | slide 34 / img_06.png (JioMart Digital ASP, electronics) | currently skipped → un-skip and treat as a mobile-app card |
| `rcpl` | slide 34 / img_01.png (Reliance Consumer Brands "From Our Hands to Yours") | currently skipped → un-skip |
| `trends` | slide 33 / img_01.png (TRENDS Companion App: Sangam Complex Mumbai, Scan & Go, Tier rewards) | currently skipped → un-skip and add new "Companion app" card |

For `jiomart-digital`, `rcpl`, and `trends`: these were in the *skipped* group on `/jcp/channels/` (no Play Store hit / B2B / in-store). With the Accenture shots they become real mobile-app cards. The existing skip-reason note moves to a small footnote ("In-store companion app, available to store staff only" for trends).

The swap is purely an asset substitution — the page builder, filter chips, lightbox, etc. all unchanged.

---

## 4. Data model

This change has no new YAMLs. It reuses two existing data sources:

- `tools/scratch/non_rbl_play.json` — 4 entries (`jiomart`, `tira`, `ajio`, `metro-kirana`, `reliance-digital`) get `primary_shot` overrides flipped to point at a new image filename, OR a new field `primary_shot_override: "accenture-2026-04-16.png"` so the builder picks that path.

- `tools/scratch/non_rbl_channels.json` — 3 entries (`jiomart-digital`, `rcpl`, `trends`) flip from `skip: true` to `skip: false` and gain `primary_shot_override` pointing at the new asset.

For `/jcp/index.html` Change A and B, content is hand-edited inline (no YAML). Change C adds one image reference.

### Asset names

Use the slide + slot as the filename so traceability stays inline:

```
images/jcp-channels/<slug>/accenture-s33-img03.png
images/jcp-channels/<slug>/accenture-s34-img04.png
…
```

`tools/build_jcp_channels_page.py` learns one new line: when `primary_shot_override` is set, use it instead of `shot-<primary_shot>.png`.

---

## 5. Asset pipeline

Source already extracted to `tools/scratch/jcp_slide_images/slide_<n>/img_<NN>.png` by `tools/scratch/extract_jcp_slides.py` (committed under tools/scratch). Map and ship:

```bash
# Pass A · canonical naming
mkdir -p images/jcp-channels/{rcpl,jiomart-digital,trends}
# Move + rename per the table in §3.2
cp tools/scratch/jcp_slide_images/slide_33/img_01.png images/jcp-channels/trends/accenture-s33-img01.png
cp tools/scratch/jcp_slide_images/slide_33/img_03.png images/jcp-channels/jiomart/accenture-s33-img03.png
cp tools/scratch/jcp_slide_images/slide_33/img_04.png images/jcp-channels/tira/accenture-s33-img04.png
cp tools/scratch/jcp_slide_images/slide_33/img_06.png images/jcp-channels/ajio/accenture-s33-img06.png
cp tools/scratch/jcp_slide_images/slide_34/img_01.png images/jcp-channels/rcpl/accenture-s34-img01.png
cp tools/scratch/jcp_slide_images/slide_34/img_03.png images/jcp-channels/reliance-digital/accenture-s34-img03.png
cp tools/scratch/jcp_slide_images/slide_34/img_04.png images/jcp-channels/metro-kirana/accenture-s34-img04.png
cp tools/scratch/jcp_slide_images/slide_34/img_06.png images/jcp-channels/jiomart-digital/accenture-s34-img06.png

# Pass B · brand wall + capability section
mkdir -p assets/jcp/accenture-2026-04-16/
cp tools/scratch/jcp_slide_images/slide_31/img_01.png assets/jcp/accenture-2026-04-16/brand-wall.png
```

### CDN mirror

Per skill §6, mirror all new assets to GCS and rewrite paths:

```bash
gsutil -m -q rsync -r -x '.*\.json$' images/jcp-channels/ \
  gs://impetus-socialpilot/rrl-portfolio/images/jcp-channels/

gsutil -m cp -r assets/jcp/ \
  gs://impetus-socialpilot/rrl-portfolio/assets/jcp/
```

The page builder already uses CDN URLs, so no in-page sed needed for `/jcp/channels/`. For the brand-wall image on `/jcp/index.html`, link directly to the CDN URL.

### Image sizes

The PPTX images are PNG at varying sizes. No resize needed for slide 33-34 phone shots (they're already 945×2048 max — comfortable for 9:16 frame display). The brand-wall (slide 31, 2048×1067) is fine at full width.

---

## 6. Navigation wiring

**No nav changes.** `/jcp/` and `/jcp/channels/` are already linked from the global mega-menu (Tracks → Platforms → JCP) and the per-track subnav (Overview · Channels · AI Cataloging · RBL · RCPL).

The 3 newly un-skipped channel slugs (`trends`, `rcpl`, `jiomart-digital`) move from the *In-store · B2B · planned* section on `/jcp/channels/` into the *Mobile apps* section. Headline counts auto-update from data: storefronts 31 → 31, mobile apps 12 → 15, in-store/B2B/planned 35 → 32.

---

## 7. Build / verify

```bash
# 1. Extract slides (already done; re-run if PPTX updates)
.venv/bin/python tools/scratch/extract_jcp_slides.py

# 2. Copy + rename per §5 (paste the cp block)

# 3. Update tools/scratch/non_rbl_channels.json + non_rbl_play.json per §4
#    (un-skip 3 slugs · add primary_shot_override for 8 slugs)

# 4. Patch tools/build_jcp_channels_page.py to honour primary_shot_override

# 5. Rebuild the gallery
.venv/bin/python tools/build_jcp_channels_page.py

# 6. Hand-edit jcp/index.html for Changes A, B, C

# 7. Push to CDN
gsutil -m -q rsync -r -x '.*\.json$' images/jcp-channels/ \
  gs://impetus-socialpilot/rrl-portfolio/images/jcp-channels/
gsutil -m cp -r assets/jcp/ \
  gs://impetus-socialpilot/rrl-portfolio/assets/jcp/

# 8. Verify
python3 -m http.server 8765
# Open /jcp/ → confirm new stat tiles, ecosystem section, brand wall
# Open /jcp/channels/ → confirm 15 mobile-app cards, all using Accenture shots for the 8 listed
```

Walk the §9 verify checklist from `website-section-authoring`:
- [ ] `/jcp/` hero stats trace to slide 35 / 31
- [ ] `/jcp/` ecosystem section matches slide 35 verbatim
- [ ] Brand wall image loads from CDN
- [ ] `/jcp/channels/` shows 15 mobile-app cards (was 12)
- [ ] All 8 listed channels show the Accenture image, not the Play Store one
- [ ] Filter chips, lightbox, layout unchanged
- [ ] `/jcp/channels-spec.md` doc reference still points at the right counts

---

## 8. Phased delivery

| Phase | Scope | Time |
|---|---|---|
| **P1** | Copy + rename slide images to `images/jcp-channels/<slug>/accenture-…png` (8 phone shots) + push to GCS | ~20 min |
| **P2** | `tools/build_jcp_channels_page.py` patch for `primary_shot_override` + `tools/scratch/non_rbl_play.json` + `non_rbl_channels.json` updates (8 overrides + 3 un-skips + Trends staff-app badge) · rebuild + verify | ~45 min |
| **P3a** | `/jcp/index.html` rewrite — modify hero (Change A), insert Ecosystem section (Change B), delete 4 sections (B2C roster, B2B roster, headcount, Deep cards), replace AI Cataloging block with CTA card | ~45 min |
| **P3b** | Lift `§ UCP` block from `/jcp/` → `/ucp/index.html` (replace stub) | ~20 min |
| **P3c** | Lift `§ Agentic Commerce` ZIP + JIIA cards → `/kaily/index.html` (replace stub) + add slide-37 hero image | ~25 min |
| **P3d** | Lift GlamAR card + add slide-41 PixelBin umbrella content → `/pixelbin/index.html` (replace stub) | ~25 min |
| **P3e** | Lift 19 sub-IP rows from `/jcp/` → append to `/catalog/index.html` (read catalog structure first; merge into existing IP table) | ~30 min |
| **P3f** | Refresh `/jcp/cataloging/index.html` with slide-19 content (15 days → 5 hours · pipeline visual · slide-19 images) | ~30 min |
| **P4** | Local verify + CDN sanity sweep + commit | ~30 min |

Total v1: **~4.5 hr** (up from v0.3's ~2.5 hr because Agentic Commerce split, Cataloging refresh, and Sub-IPs rehome are now in scope).

---

## 9. Decisions

Locked 2026-05-01.

1. **Hero stat strip framing** → **Two strips, slide-35 first.** Top strip (FY 2025-26 · slide 35): 700K+ orders/day · 50K+/min peak · 200M+ customers · 30K+ stores. Second strip (slide 31 + register): 78 channels · 105 B2C businesses · 7 B2B businesses · 10 verticals. Both rows source-cited. *Drops the existing 350K+/hour and 300M+ customer tiles — both are slide-32 peaks; the FY 26 view in slide 35 supersedes.*
2. **Brand wall (slide 31 collage)** → **Don't use it.** Removed from scope.
3. **Trends Companion App** → **Add as a 13th mobile-app card on `/jcp/channels/`** with a small "in-store companion · staff app" badge.
4. **Field name** → `primary_shot_override` (string · relative path under the slug folder). Page builder picks this if present, else falls back to `shot-<primary_shot>.png`.
5. **Stores number** → **30K+ everywhere** (slide 35 · FY 2025-26).
6. **105-row B2C roster + 7-row B2B roster** → **Both deleted from `/jcp/`** (no replacement card). The data lives on `/jcp/channels/`. The existing subnav chip "Channels" is the discovery path.
7. **Sub-IP merge into gallery cards** → **Skip.** Only ~17 of 105 channels carry sub-IP data; not worth the schema churn for sparse coverage.
8. **§ JCP team headcount (~140)** → **Cut.** Moves to `/organisation` if it surfaces anywhere.
9. **§ Sub-IPs · 19 modules + § Deep cards** → **Cut.** Not apex-valuable.
10. **§ UCP** → **Move to `/ucp/`** (replace the current "Page in progress" stub with the lifted UCP narrative). Extension of UCP page deferred.
11. **§ Agentic Commerce** → **Split.** ZIP (AJIO) + JIIA (JioMart) → `/kaily/` (Farooq's letter names Kaily as the agentic commerce platform live on JioMart and AJIO). GlamAR → `/pixelbin/` (PixelBin umbrella per slide 41 covers GlamAR). Both replace existing stubs.
12. **AI Cataloging on /jcp/** → **Replace the inline section with a CTA card** pointing readers at `/jcp/cataloging/`. The deep-dive page itself gets the slide-19 refresh (15 days → 5 hours · pipeline visual · slide-19 images on CDN).
13. **Sub-IPs (19 modules)** → **Move to `/catalog/`** (the IP Catalog page). Lift the 19 module names + descriptions from `/jcp/index.html` before deleting that section, append to `/catalog/index.html`.

---

## 10. Out of scope (v1)

- **Slide 32 hero diagram** (img_18, the JCP categories diagram) — promising as a `/jcp/` overview visual but needs design polish first.
- **Other Accenture slides** (1-30, 36, 39-49, 50-69) covered by `docs/accenture-2026-04-16-compilation/INDEX.md` but not in this spec — see INDEX for the future-page mapping.
- **Re-checking the 105 vs 78 channels discrepancy.** Spec acknowledges both as cited claims; reconciliation deferred.
- **Updating `docs/jcp-channels-spec.md`** to reflect the 3 un-skipped slugs — defer until Implementation P2 is committed.
- **Hand-cropping or re-sizing the slide images** — ship as-is, full PNG.
- **Extending `/ucp/`, `/kaily/`, `/pixelbin/` beyond the lifted-and-light content.** The v0.1 of each is whatever fits in this spec; deeper extension is a separate spec per page.
- **Re-classifying the 19 sub-IPs** within /catalog/ — append as a flat group; deeper categorisation (which sub-IP belongs to which Fynd umbrella platform) is a follow-up.
- **Auto-redirect for deep links to /jcp/#ucp, /jcp/#agentic-commerce, etc.** — anyone with a stale deep link hits a missing anchor. Accept the link rot; the subnav + global menu provide the new entry points.

---

**End of spec.** Awaiting sign-off on §9 decisions before implementation.
