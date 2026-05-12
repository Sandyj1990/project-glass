# /organisation rebuild · spec

**Status:** Built and shipped 2026-05-02 · `/organisation` v0.10.1 · feedback round applied.
**Author:** Kushan Shah
**Date opened:** 2026-05-02
**Last updated:** 2026-05-03 · v2 xlsx ingest + RR Counterpart column dropped + homepage org-totals reconciled — see §8.
**Source materials (gitignored):**
- `docs/org-notes-compilation/Team List Billed v2.xlsx` — sheet `Trupti -Updated Employee Master` *(authoritative since 2026-05-03; v1 retained on disk as a backup)*
- `docs/org-notes-compilation/Fynd - Unlocking Growth.pdf` — slides 17–23 (used by `/culture` rebuild, not this spec)
- `/Users/kushanshah/Documents/work/engineering-os/backend/data/keka/employees.csv` + `photos/` — photo mapping by Employee ID
- Live website nav (`index.html` mega-menu) — canonical Platform list

**Out of scope for this spec:**
- `/culture` page (separate effort, sourced from PDF slides 17–23)
- AI Native Ways of Working tab content body (placeholder only — instructions to follow)

---

## 1 · Page shape (current · 2026-05-03)

The Organisation register is split across **two routes**, joined by an `/impetus`-style subnav (`subnav-link` pills) at the top of each page. Both pages share the same nav, footer, and `data.json` source.

| Route | Tab label | Body |
|---|---|---|
| `/organisation` | Overview (active) | Hero (crumb, H1, lead, 4-stat strip) + § 01 Project × Track pivot. |
| `/organisation/directory` | People Directory | Hero (crumb, H1, lead) + filter bar + filterable directory table + pager. |

**Pivot → directory deep-link.** Clicking any project header row on the Overview pivot navigates to `/organisation/directory?project=<name>`. The directory's `readState()` parses the query string on load and pre-applies the project filter — same mechanism as the original same-page filter, just across a route boundary.

**AI-Native** content (originally Tab 2 in the 2026-05-02 rebuild) now lives at `/ai-native/`. The Overview page carries a one-line redirect script that bounces `/organisation/#ai-native` to `/ai-native/` for any stale links.

**Sections preserved across the split:**
- Hero stat strip — Total, Engineering %, 10+ years tenure, Founder-led — hydrates on the Overview page from `data.meta.totals`.
- The Project × Track pivot table (§ 2.3 below) stays on Overview.
- Filterable directory (§ 2.2 below) moves verbatim to `/organisation/directory`, including the same column set, filter set, sort, search, pager, and URL-state sync.

**Sections retired** since the 2026-05-02 spec was written:
- The two anchor-driven tabs (`#structure`, `#ai-native`) and the AI-Native placeholder body — AI-Native moved to its own page.
- The "Leadership" block above the tables — not present in the live page.
- The "Where the work happens" footer card — not present.

> Historical note: the 2026-05-02 rebuild shipped as one HTML file with two anchor-driven tabs. AI-Native was extracted to `/ai-native/` shortly after. People Directory was extracted to `/organisation/directory` on 2026-05-03 to mirror the `/impetus` subnav pattern (one route per logical view) and keep the Overview page a fast-loading summary.

---

## 2 · Tab 1 · Org Structure

### 2.1 Platforms list (canonical, user-facing)

Source = website nav (Tracks mega-menu + More). **Mappings live in `organisation/mappings.json`** — a committed JSON config the build script reads on every run. To rename a Project/Track display name, point a value at a different platform page, or add a sub-chip (like Pulsepoint on the Sell Track row), edit that file and re-run `python3 tools/build_org_data.py`. No Python edits required.

**JSON shape:**

```json
{
  "projects": {
    "<xlsx Project value>": { "displayName": "...", "route": "/path" }
  },
  "tracks": {
    "<xlsx Track value>": {
      "displayName": "...",
      "route": "/path",
      "chips": [{ "label": "Pulsepoint", "route": "/impetus/pulsepoint/" }]
    }
  }
}
```

`displayName`, `route`, and `chips` are all optional. Missing `displayName` → use the raw xlsx value. Missing `route` → render as plain text. `chips` render as small linked pills after the track name (used when one xlsx Track bundles multiple platforms, e.g., the "Sell Track: Store Tech Adoption" row carries Pulsepoint as a chip in addition to its primary Companion App link). The build script lower-cases + trims track keys for case-insensitive matching against xlsx values that drift in capitalisation.

**Current mappings** are in `organisation/mappings.json`. Snapshot below for reference; the JSON is the source of truth.

**Projects** (8 of 13 link to a platform page; the other 5 normalise display name only):

| xlsx Project | displayName | route |
|---|---|---|
| JCP | JCP | /jcp |
| Impetus | Impetus | /impetus |
| Granary | Granary | /granary |
| Unified customer Profile | UCP & Marketing OS | /ucp |
| ALP | ALP | /alp |
| RCPL | RCPL | /jcp/rcpl |
| HireFirst | HireFirst | /hirefirst |
| Samarth Plus | Samarth | /samarth |
| External Monitization | External Monetization | *(plain text)* |
| Central Support / Monobrands / JioGames / Neolync | *(unchanged)* | *(plain text)* |

**Tracks** (linked cells, plus the Pulsepoint chip on the Sell Track row):

| xlsx Track | displayName | route |
|---|---|---|
| AI Photoshoot | AI Photoshoot | /impetus/photoshoots/ |
| InstaDesk | InstaDesk | /impetus/instadesk/ |
| AI Design | AI Design | /impetus/brands/ |
| AI Catalog | AI Catalog | /jcp/cataloging/ |
| Impetus Command Center / Ask Impetus | Impetus Command Center · Ask Impetus | /impetus/analytics/ |
| Plan: Cortex | Plan: Cortex | /impetus/cortex/ |
| Impetus PLM | Impetus PLM | /impetus/plm/ |
| Retail Jarvis | Retail Jarvis | /retail-jarvis/ |
| Make: Intellimake / IntelliQC / IntelliPack | Make: IntelliVerse (Intellimake / QC / Pack) | /impetus/intelliverse/ |
| Sell Track: Store Tech Adoption (NPS, Companion App, Pulsepoint, Scan & Go etc) | Sell: Store Tech Adoption | /impetus/companion-app/ + Pulsepoint chip → /impetus/pulsepoint/ |
| Retail Vista | Retail Vista | /retail-vista/ |
| Pixelbin / PixelBin | PixelBin | /pixelbin |
| Boltic / Ratl / Kaily / Konnect / GlamAR / Horizon | (mapped) | /boltic, /ratl, /kaily, /fynd-konnect, /pixelbin/glamar, /fynd-horizon |
| Move - TMS / WMS | TMS / WMS | /tms |
| RCPL · Unified customer Profile · ALP | (mapped) | /jcp/rcpl, /ucp, /alp |
| Storefronts / Core Platform / Commerce | (unchanged) | /jcp |
| Forge MES | Forge MES | /forge |

**Platform pages with no representation in the xlsx** (people are billed under broader Projects/Tracks): Retail Vista, Retail Jarvis, Forge, SwapEasy, Autri, Dark Factory, Fynd Academy. These pages exist on the site but no xlsx row carries a matching Project or Track. Their teams are folded into JCP / Impetus / External Monitization rows.

### 2.2 Table 1 · Employee directory (filterable)

Source rows: `Trupti -Updated Employee Master` (1,056 employee rows). Every row renders as a card or table row.

**Columns:**
1. Photo (avatar circle, 40×40, fallback = initials on tinted bg)
2. Employee ID (mono, small)
3. Name (`Display Name`)
4. Department
5. Project (link to Platform page where mapped)
6. Track
7. Dedicated/Shared (`Dedicated/ Platform`, normalised via `mappings.json kinds`)
8. *(carried in `data.json` but not currently rendered)* Job Title, Reporting Manager, Billing Entity

> *Removed 2026-05-03:* the **RR Counterpart** column + its filter — the source column was dropped in `Team List Billed v2.xlsx`. To be re-derived later from project-level counterpart data already maintained across the register (see §8 changelog).

**Filters** (top of table, all clientside, AND-combined):
- Project (multiselect, sourced from Platforms list)
- Track (multiselect, sourced from unique values within current Project filter)
- Department (multiselect)
- Dedicated vs Shared
- Free-text search (name, ID, manager)

> *Removed 2026-05-03:* the RR Counterpart filter (column dropped in v2 xlsx). Billing Entity remains in the data but is not currently rendered as a filter.

**Behavior:**
- Default view: all 1,056 rows, paginated 50/page (or virtualized if perf is fine).
- URL state: filter selections serialize to query string so links are shareable (`/organisation?project=Impetus&track=AI+Design`).
- Sort: any column header click; default sort = Project, then Track, then Name.
- Empty state: "No one matches these filters."

**Data delivery:**
- Build step: `tools/build_org_data.py` reads the xlsx + keka csv, produces `organisation/data.json` with rows + a `photos` map (employeeId → CDN URL). Page hydrates from JSON at load.
- JSON is a build artefact, generated locally, committed (it's small — ~1,056 rows × small fields).

### 2.3 Table 2 · Project × Track pivot

Reproduces the pivot from `Trupti -Updated Employee Master` (the Pivot Table 1 sheet doesn't have cached values; we'll regenerate from the master sheet rows).

**Layout:** rows = Project, sub-rows = Track, cell = headcount, with row totals and grand total.

```
Project                         Track                                                  People
─────────────────────────────────────────────────────────────────────────────────────────────
Impetus                                                                                  239
                                Sell Track: Store Tech Adoption (NPS, Companion App…)    41
                                AI Design                                                 20
                                …
JCP                                                                                      355
                                Core Platform                                            174
                                Konnect                                                   35
                                …
External Monitization                                                                    315
                                Commerce                                                 266
                                …
─────────────────────────────────────────────────────────────────────────────────────────────
Total                                                                                  1,056
```

- Same filter set as Table 1 applies (so a user can filter to Department=Engineering and see the Project×Track count of just engineers).
- Each Project header row clickable → scrolls to Table 1 with that Project filter applied.
- Mini-bar in the People column for visual scan (largest = full width).

### 2.4 Photo CDN

- **GCS bucket:** `gs://impetus-socialpilot/rrl-portfolio/assets/keka-photos/`
- **Public CDN:** `https://socialassets.impetusz0.de/rrl-portfolio/assets/keka-photos/`
- **Filename:** `<employee_id>.<ext>` — extension preserved verbatim from keka source (`.jpg` / `.jpeg` / `.png`). The build step derives the URL by reading the `photo_path` field in `keka/employees.csv` and taking `basename(photo_path)`.
- **Upload mechanism (one-shot):** there is no dedicated upload script — `gsutil rsync` was used directly from the keka source dir. Re-run when keka adds new photos:
  ```bash
  gsutil -m -q rsync -r \
    /Users/kushanshah/Documents/work/engineering-os/backend/data/keka/photos \
    gs://impetus-socialpilot/rrl-portfolio/assets/keka-photos
  ```
- **Coverage as built:** 932 files in keka source → 932 uploaded → 918 / 1,056 (87%) of xlsx rows hit a photo. Misses fall back to a tinted-circle avatar with the employee's initials.
- **.gitignore:** the photo binaries are NOT mirrored into the repo. Only `organisation/data.json` (which embeds the per-employee CDN URL inline) is committed.

### 2.5 Leadership block (preserved)

Same content as today's `/organisation` § 01, no rewrites. Sits above the tables on the Org Structure tab.

---

## 3 · AI Native Ways of Working *(extracted)*

Originally Tab 2 of the 2026-05-02 rebuild. Now lives at `/ai-native/` as its own register page. Out of scope for this spec.

---

## 4 · Build pipeline (as shipped)

```
                   gsutil rsync (one-shot)
keka/photos/  ─────────────────────────────►  gs://impetus-socialpilot/rrl-portfolio/assets/keka-photos/
                                                          │
                                                          ▼
                                            https://socialassets.impetusz0.de/...
                                                          │
                                                          │ derived URL per employee
                                                          ▼
keka/employees.csv  ──┐
                      ├──►  tools/build_org_data.py  ──►  organisation/data.json (committed)
xlsx (gitignored)  ───┘                                          │
                                                                  ▼
                                                          organisation/index.html (fetch on load)
```

| Step | Command / file | When to re-run |
|---|---|---|
| 1. Upload photos | `gsutil -m -q rsync -r <keka>/photos gs://impetus-socialpilot/rrl-portfolio/assets/keka-photos` | New keka photos arrive |
| 2. Build data | `python3 tools/build_org_data.py` | xlsx changes; new mappings added |
| 3. Reload page | `/organisation` fetches `data.json` clientside | Automatic on page load |

**What `tools/build_org_data.py` does** (~200 LOC):
1. Opens `Trupti -Updated Employee Master` sheet via openpyxl.
2. Drops the three sensitive columns (`Average Rating 25-26`, `Average Rating 24-25`, `Current TCTC`).
3. Reads `keka/employees.csv` to build `employeeId → CDN URL`.
4. For each row, normalises Project + Track and resolves their routes from the two hardcoded mapping dicts.
5. Computes the pivot (Project → Tracks → counts) sorted by total desc.
6. Writes `organisation/data.json` (~500 KB) with `meta.totals`, `facets` (for filter chips), `pivot`, and `rows`.
7. Prints a one-line summary: row count, RRL count, eng %, photo hit rate.

**What `organisation/index.html` does** (~430 LOC, vanilla JS, no framework):
- Fetches `data.json` once on boot.
- Hydrates hero stats, pivot table, filter dropdowns, directory table.
- Handles tab switching, multiselect filters, free-text search, column-header sort, pagination (50/page), and URL-state sync.
- Photo `<img>` tags carry an inline `onerror` handler that swaps to an initials avatar on 404.

All inputs except `keka/employees.csv` and the two committed artefacts (`data.json`, `index.html`) are gitignored.

---

## 5 · Resolved decisions (2026-05-02)

1. **Unmapped Projects** → Show all 13 xlsx Projects as their own filter rows. The 4 unmapped (External Monitization, Central Support, Monobrands, JioGames) render as plain text in both Table 1's Project column and Table 2's pivot. No "Other" bucket.
2. **Link priority** → **Track column** is the navigable cell when the Track maps to a known platform page (Boltic, PixelBin, Ratl, Kaily, Fynd Konnect, TMS, GlamAR, Horizon, etc.). **Project column** renders as plain text for unmapped Projects, or as a link only for the 6 mapped Projects (Impetus, JCP, Granary, UCP, ALP, Samarth Plus, HireFirst, RCPL). The xlsx truth is preserved — we don't override the Project link based on Track.
3. **Sensitive columns** → Excluded entirely. Build script strips `Average Rating 25-26`, `Average Rating 24-25`, and any TCTC column before writing `data.json`. Page never reads them.
4. **Hero stats** → Recomputed live from the xlsx. Total = 1,056. On Reliance = 702 (Billing Entity = RRL). Engineering % = computed (Engineering dept / total). Founder-led = static "13 yrs". The current home-page number (~430 on RR) is a separate, narrower count and is not used here.
5. **AI Native tab** → Placeholder rendered now (heading + "Content coming · instructions pending" note). Final content arrives in a follow-up message.
6. **Reliance Counterpart column** → Visible column on Table 1 **and** a multiselect filter. Blank values render as em-dash. *(Removed 2026-05-03 — see §8 changelog. Future plan: re-derive from project-level counterpart data already maintained across the register.)*

> Resolved with user 2026-05-02.

---

## 6 · Acceptance checklist

- [x] `/organisation` loads with the Overview + People Directory subnav (default = Overview); People Directory is its own route at `/organisation/directory` *(updated 2026-05-03)*
- [x] Table 1 renders 1,056 rows, all filters work, photos load from CDN (918 / 1,056 hits, 138 fall back to initials)
- [x] Table 2 pivot totals match xlsx *(v2 · 2026-05-03)* — JCP 274, Infrastructure 65, External Monetization 310, Impetus 244, Central Support 52, Granary 27, Monobrands 26, UCP 22, RCPL 13, ALP 9, JioGames 5, Neolync 5, HireFirst 2, Samarth 2 = **1,056**
- [x] Mobile: tables stack via CSS `@media (max-width: 900px)` rule
- [x] No xlsx, pdf, or photos committed (gitignored: `docs/org-notes-compilation/`, `docs/*.pdf`)
- [x] All copy on the page passes the MDA bar (no em-dashes, no "leverage", DD - MMM - YYYY dates)
- [x] *(2026-05-03)* `/organisation/directory?project=<name>` deep-link pre-applies the project filter on load (verified: `?project=Granary` → 27 of 27)

---

## 7 · How to update later

- **xlsx refreshed** → drop new file at `docs/org-notes-compilation/Team List Billed.xlsx`, run `python3 tools/build_org_data.py`, commit `organisation/data.json`.
- **New keka photos** → run the `gsutil rsync` in § 2.4, then re-run the build script (URLs will pick up automatically since they're derived per-employee from the csv).
- **Rename a Project or Track display name** → edit `organisation/mappings.json`, set `displayName`, re-run the build.
- **New platform page added** → edit `organisation/mappings.json`, add the `route` (and optional `displayName`) under either `projects` or `tracks`. Re-run the build.
- **Track bundles multiple platforms** → use `chips` in `organisation/mappings.json` (see Sell Track example). Each chip renders as a small pill after the track name.
- **Add a third subnav tab** (e.g., Tenure / Leadership) → create `organisation/<tab>/index.html`, add the `subnav-link` pill to both existing pages' subnav blocks, and have the new page fetch `/organisation/data.json` directly. The subnav is page-local HTML (not driven by `tools/site_chrome.py`), so each route owns its own copy of the three pills.

---

## 8 · Changelog

**2026-05-03 · split People Directory into its own subnav tab**

- Created `/organisation/directory` — own hero (`People Directory.`), full filter bar, table, and pager. JS is the directory half of the original page (filters, sort, search, pagination, URL-state sync); reads `/organisation/data.json` from the absolute path.
- Trimmed `/organisation/index.html` — added the two-pill subnav at the top of the hero, kept hero stats + § 01 Project × Track pivot, dropped the directory section, the filter UI, and ~280 lines of unused CSS / JS. Pivot row click now navigates to `/organisation/directory?project=<name>` instead of scrolling to an inline anchor.
- Pattern mirrors `/impetus` (Overview · Brands · Photoshoots · Category Intel) — one logical view per route, joined by a `subnav-link` pill bar at the top of the page hero.
- Why: the Overview view (hero + pivot) and the People Directory view (filters + 1,056-row table) serve different reader intents. Splitting keeps Overview lightweight and gives the directory a shareable URL with filter params (`?project=Granary` etc.).
- Touched files: `organisation/index.html`, `organisation/directory/index.html` (new). `data.json` and `mappings.json` unchanged. `tools/build_org_data.py` unchanged. Commit `10e9006`.

**2026-05-03 · v2 xlsx ingest + RR Counterpart column dropped + homepage org-totals reconciled**

Drop-in replacement of the source xlsx. Same sheet name, same row count (1,056), same column ordering for the first 9 fields. The notable change: the `Reliance Counterpart` column was removed in v2 (replaced by two empty unnamed spacer cells) and `engineering` totals shifted ±5 rows due to a fresh roster cut.

Pivot drift v1 → v2:

| Project | v1 | v2 |
|---|---:|---:|
| JCP | 355 | 274 |
| **Infrastructure** *(new project)* | — | 65 |
| External Monetization | 315 | 310 |
| Impetus | 239 | 244 |
| Central Support | 37 | 52 |
| Granary | 27 | 27 |
| Monobrands | 26 | 26 |
| UCP & Marketing OS | 22 | 22 |
| RCPL | 13 | 13 |
| ALP | 10 | 9 |
| Neolync | 4 | 5 |
| JioGames | 5 | 5 |
| Samarth | 1 | 2 |
| HireFirst | 2 | 2 |
| **Total** | **1,056** | **1,056** |

The new "Infrastructure" project carved 65 people out of JCP's previous 355 (-81), with a few smaller shuffles. On RRL count moved 702 → 707. Engineering % stayed at 46%.

Changes shipped:

- `tools/build_org_data.py` pinned to `Team List Billed v2.xlsx`. Removed all counterpart resolution logic (no more `proj_meta.counterpart` / `track_meta.counterpart` / xlsx fallback). `data.meta.source` updated to point at v2.
- `organisation/data.json` regenerated. `counterpart` field gone from every row; `facets.counterpart` gone from the facets block. Hero stats live-derived as before.
- `organisation/mappings.json` cleaned — every `counterpart` field stripped from project + track entries (8 + 1 = 9 fields removed). The `_shape` block + `_comment` updated to reflect counterpart removal.
- `organisation/directory/index.html` — dropped the RR Counterpart column header, the per-row counterpart cell, the counterpart filter dropdown, and the `counterpart` Set in `STATE.filters`. Grid template went 8 → 7 columns. Hero lead reworded ("by project, track, department, or billing kind").
- `index.html` (homepage `§09`) — reconciled to v2 totals: `1,100+ people` → `1,056` (twice), `68 % product builders` → `60 %` (twice), `1,091 in 2025` → `1,056 in 2026`. The `~ 200 in 2014` historical anchor kept as-is.
- `CLAUDE.md` — added the *Org stats · canonical-source rule* section and a never-do entry. The site now has one source of truth for all org-wide numbers (`organisation/data.json`); other pages must be reconciled manually after each rebuild.

**Future work — re-derive RR Counterpart from project data.** Per user direction (2026-05-03), the Counterpart column is removed from the page entirely for now. Later: re-derive each row's RIL counterpart from the project + track context already maintained across the register (e.g., the `/jcp` page already names Abhijit Khasnis, `/granary` names Advait Pandit + Ved Antani, etc.). The mapping logic should live in a new `tools/derive_counterparts.py` step that reads project/track pages and writes a counterpart-per-employee map back into `data.json`. Re-add the column + filter to the directory page once that derivation is in.

---

## 9 · Round 2 · scope locked, in flight (opened 2026-05-03)

After v2 ingest landed, user feedback flagged five problems with the Overview page:

1. **Goal mismatch** — page must answer four questions in 30s scan: who runs Fynd, how the org is structured, how the org maps to platforms that ship, how it pays for itself. Current page answers none.
2. **Excel-pivot aesthetic** — flat 14-row Project × Track table with no leader names, no narrative, no hierarchy. People Directory feels disconnected.
3. **No leader visibility** — directory is filterable but doesn't surface "who leads at each level". Each project/track needs a named owner.
4. **Disconnected from platform pages** — many pivot rows are plain text; should link to /impetus, /jcp, etc.
5. **External Monetization framing** — must be re-framed as a self-sustaining commercialization arm (Fynd IP → external customers; the engine that funds the RR investment), not a budget-bucket.

### 9.1 Page model · 3 tabs (4 once organogram lands in round 3)

| Route | Tab label | Body |
|---|---|---|
| `/organisation` | Overview *(rewrite)* | Hero · Leadership masthead · 4 tier sections (RR Platforms · External Commercialization teaser · Shared Foundation · Adjacent) |
| `/organisation/directory` | People Directory *(unchanged)* | Filterable 1,056-row table |
| `/organisation/external` | External Commercialization *(new)* | Self-sustaining narrative deep-dive · sub-product cards (Boltic / PixelBin / Ratl / Kaily / Konnect / Horizon …) with leader + headcount + link to platform page |
| `/organisation/organogram` | Organogram *(round 3 · deferred)* | Interactive collapsible tree — founders → C-suite → directors → teams. Each node carries avatar + title + direct-report count. Search to jump to name. **Deferred until a richer keka HRIS export with `manager_id` lands** — current `keka/employees.csv` only has `id, name, email, photo_path`. |

### 9.2 Tier model · how the 14 xlsx Projects group

The flat 14-project list collapses into 4 tiers, each with its own visual treatment:

| Tier | Projects | People | Visual treatment |
|---|---|---:|---|
| **RR Platforms** | JCP · Impetus · Granary · UCP & Marketing OS · ALP · RCPL · Samarth · HireFirst · Monobrands | ~617 | 3-col card grid · ink section header · accent micro-divider |
| **External Commercialization** *(self-sustaining)* | External Monetization (display: "External Commercialization") | 310 | Full-width inverted block (ink bg, white text) · narrative inline · teaser link to `/organisation/external` |
| **Shared Foundation** | Infrastructure · Central Support | 117 | 2-col card grid · lighter section header · smaller cards |
| **Adjacent JPL builds** | JioGames · Neolync | 10 | Inline footnote-row · no cards |

Tier assignment lives in `organisation/mappings.json` as a new `tier` field per project. Build script emits `tier` per row and `tier` per pivot entry to `data.json`.

### 9.3 Leadership masthead · §01 of Overview

Editorial text-only matrix — **no avatars**, **no boxes**, **no org-chart lines**. Reads as a masthead / table-of-contents, not "About Us":

```
FOUNDERS
Farooq Adam              Sreeraman Thiagarajan
Co-founder · since '13   Co-founder · since '13

CTPO
Name Surname             Name Surname             Name Surname
Scope line               Scope line               Scope line

CBO
Name Surname             Name Surname
Scope line               Scope line
```

Names + roles + scopes live in a new `organisation/leadership.json` overlay (user-authored canonical list, since manager-column derivation is too noisy — Sreeraman not in roster, founders' direct-report layer empty). Schema:

```json
{
  "founders":     [{ "name", "title", "since", "scope" }],
  "cSuite":       [{ "name", "title", "scope", "_role": "CTPO|CBO|COO|…" }],
  "projectLeads": { "<project>": { "name", "title", "scope" } }
}
```

### 9.4 Project card composition

Each card surfaces what the pivot hides:

```
┌─────────────────────────────────┐
│ JCP            [274]            │  ← name (link if mapped) · headcount mono
│ ████████████░░░░                │  ← bar = share of TIER (not share of total)
│ Lead: Arunoday Ray · CTPO        │  ← from leadership.json
│                                 │
│ Storefronts        102 →        │  ← top 5 tracks by headcount, link if mapped
│ Core Platform      174 →        │
│ Konnect             35 →        │
│ PixelBin            18 →        │
│ Boltic              17 →        │
│ +5 more                         │  ← rest collapse into expandable "+N more"
│                                 │
│ → 274 people · directory        │  ← mono link to /directory?project=JCP
└─────────────────────────────────┘
```

Build script emits `topTracks` (top-5 by count) per pivot entry; the rest stay in the `tracks` array for the "+N more" expansion.

### 9.5 External Commercialization deep-dive · `/organisation/external`

Standalone subroute. Hero (own H1 = "External Commercialization."). Body:
- **Narrative block** — self-sustaining engine framing. The same IP shipped to RR is commercialized externally to paying customers. Funds the rest of the work.
- **Sub-product card grid** — Boltic · PixelBin · Ratl · Kaily · Fynd Konnect · Fynd Horizon · etc. Each card pulls from the tracks under "External Monetization" in `data.json`, plus carries leader (from `leadership.json`) and link to the platform page.
- **Customer / revenue surfaces** *(deferred to round 3 unless data is on-hand)* — external customer count, ARR / MRR, top external accounts.

### 9.6 Build script changes (`tools/build_org_data.py`)

- Load `organisation/leadership.json` and emit `data.leaders = { founders, cSuite, projectLeads }`.
- Read `tier` from `mappings.json`, emit `tier` on each row and on each pivot entry.
- Compute `topTracks` (top 5 by count) per pivot entry; full `tracks` array stays for drill-down.
- Print an **unmapped report** at end of build: every Project / Track that has no `displayName` or `route` in `mappings.json`. Surfaces drift after each xlsx refresh.

### 9.7 Mappings updates (`organisation/mappings.json`)

- Add `tier` per project (rr-platforms / external / foundation / adjacent).
- Rename External Monetization display → **"External Commercialization"**.
- Add routes for previously-unmapped tracks where a platform page exists (Infrastructure-* groups, Central Support tracks, Monobrand tracks).
- Add display names for any Infrastructure sub-tracks that surfaced in v2.

### 9.8 What's NOT in round 2 (deferred to round 3+)

- **Organogram tab** — needs richer keka export with `manager_id` (current 4-col csv = `id, name, email, photo_path` only carries identity + photos, no reporting structure). When available: collapsible tree, default 3 levels deep, each node with avatar + title + direct-report count, search to jump to name. ~400 LOC vanilla JS.
- **Leader photos on project cards** — text-only leader names in round 2 (cleaner, faster, reads better at scan distance). Photos are an option once round-2 shape is validated by Apex.
- **CLAUDE.md changes** — no new conventions; reusing existing tier + card patterns. Cross-page nav rules and org-stats-canonical-source rules from previous rounds still apply.
- **External revenue / customer surfaces** — pending data availability from BD team.

### 9.9 Acceptance for round 2

- [ ] `/organisation` Overview answers all four scan questions in ≤ 30s without scrolling past the hero
- [ ] Every project name on Overview is linked to its platform page where one exists; mappings.json `unmapped report` is empty
- [ ] Every project card shows a named lead from `leadership.json`
- [ ] External Commercialization tier is visually distinct from RR Platforms (inverted block on Overview · standalone deep-dive at `/organisation/external`)
- [ ] All 1,056 people remain reachable via `/organisation/directory` (unchanged)
- [ ] Subnav consistent across all 3 tabs (Overview · People Directory · External Commercialization)
- [ ] Org-stat sweep (per CLAUDE.md *Org stats · canonical source* rule) shows no drift from `data.json`
- [ ] `python3 tools/inject_chrome.py --check` exits 0 on all 70+ register pages

> **Status when this section was committed:** scope locked, no code written.

### 9.10 Round 2 build · shipped 2026-05-03

Built per the §9 scope. Touched files:

- `organisation/mappings.json` — added `tier` per project (rr-platforms / external / foundation / adjacent), added new top-level `tiers` block with display labels + ordering, renamed `External Monitization` xlsx key to v2's correctly-spelled `External Monetization` with display name "External Commercialization", added Infrastructure project entry, filled missing track routes for everything that maps to a platform page (16 new track entries: Ajio, JioMart, Longtail Channels, Platform Support, TMS, Store Tech variants, Store Automation, Make: IntelliVerse variant, Granary CPP + Collection Center, Extensions & Developer Ecosystem → /boltic, Orion → /hirefirst, Samarth Plus → /samarth, Cortex display normalization, Infrastructure sub-tracks (QA / DevOps / Reliability / Security)).
- `tools/build_org_data.py` — loads `organisation/leadership.json` (returns empty skeleton if absent). Emits `tier` per row + per pivot entry. Computes `topTracks` (top-5 by count) per pivot with `moreTracks` rest count. Emits `tiers` rollup (label + total per tier) and `leaders` block. Prints unmapped report at end of build (any unmapped Project / Track / project-without-tier surfaces; current build clean).
- `organisation/leadership.json` (new) — best-effort draft from data.json + senior-title scan. 2 founders (Farooq seeded + Sreeraman seeded with `_uncertain`), 8 C-suite (top by direct reports — Ragini Varma, Ronak Modi, Amboj Goyal, Arunoday Ray, Khaarthigha Subramanian, Abhimanyu Mallik, Rahul Mandowara, Nagabhushan C R; all `_uncertain`), 14 project leads (best-of-derivation per project; some `_uncertain`). User edits this file by hand to fix names / titles / scopes — build script reads on every run.
- `organisation/index.html` (Overview) — full rewrite per §9.4 / §9.5. Hero unchanged. New sections: §01 Leadership masthead (text-only matrix, founders + leadership rows with `_uncertain` tags), §02 RR Platforms (3-col project card grid, leads, top-5 tracks, +N more, drill-down link), §03 External Commercialization (inverted full-width block with stats + CTA to deep-dive), §04 Shared Foundation (2-col grid: Infrastructure + Central Support), §05 Adjacent (inline footnote-row: Neolync · JioGames). Bar widths share-of-tier (not share-of-total). All copy passes the register voice.
- `organisation/external/index.html` (new) — own hero, inverted hero block with self-sustaining narrative, §01 sub-track table (3 rows, ranked: Commerce 285 · Extensions 14 · Fynd Create 11), §02 Lead block (Ragini Varma derived as External lead), §03 Platform pages grid (8 cards: Boltic · PixelBin · Ratl · Kaily · Konnect · Horizon · TMS · Kio).
- `organisation/directory/index.html` — subnav extended to 3 tabs.

Build output (post round 2):
```
rows: 1056   on RRL: 707   eng: 488 (46%)
photo hits: 918 / 1056
facets: 14 projects, 49 tracks
tiers:  rr-platforms=619 · external=310 · foundation=117 · adjacent=10
leaders: 2 founders, 8 c-suite, 14 project leads
unmapped: none
```

Verification (chrome-devtools MCP, port 8765):
- `/organisation` — masthead renders (founders + leadership rows), all 9 RR Platform cards present with tier-share bars, External block shows 310/285/3, Foundation cards show Infrastructure (65) + Central Support (52), Adjacent inline shows Neolync 5 · JioGames 5. Hero stats hydrate (1,056 / 46%).
- `/organisation/external` — hero stats 310/285/3/44%, sub-track table ranks Commerce 285 (91.9%) → Extensions 14 → Fynd Create 11, Lead block surfaces Ragini Varma, 8 platform cards link to deep-dives.
- `/organisation/directory` — subnav now 3 tabs. Filter/table/pager unchanged from round 1.5.
- `python3 tools/inject_chrome.py --check` → 71 unchanged (new external page picked up canonical chrome).
- Console: only the standing Tailwind CDN warning.

**Round 3 still deferred.** Organogram tab (richer keka export with `manager_id` arrived at `/Users/kushanshah/Documents/work/engineering-os/docs/onboarding/keka_roster_full.csv` — to be wired in round 3). Leader photos on cards. External revenue surfaces. Spot-fix all `_uncertain: true` entries in `leadership.json`.

### 9.11 Round 3 build · shipped 2026-05-03

Built per the §9 organogram + leadership backfill scope. Trigger: user dropped the richer keka HRIS export at `/Users/kushanshah/Documents/work/engineering-os/docs/onboarding/keka_roster_full.csv` — 1,095 rows with `Reporting To` (parent edge), `CXO's` (authoritative C-suite), `Date Joined`, `Location`, `Department`, `Job Title`, `PROJECT`. This closed every gap that round 2's masthead and project-lead derivation hit.

Touched files:

- `tools/build_org_data.py` — added `load_full_roster()` (reads keka_roster_full.csv) and `build_tree()` (walks the roster, builds parent → children adjacency map, identifies self-reporting nodes as roots, computes direct-report counts per node, sorts children by subtree size). Each row in `data.rows` is now enriched with `cxo`, `location`, `dateJoined`, `reportingTo` from the full roster (matched by Employee Number; 1,047 of 1,056 billed rows joined). `data.json` gets a new `tree` block: `{ nodes, rootNames, children }`.
- `organisation/leadership.json` — backfilled from authoritative data. Founders now both confirmed in roster (Farooq Adam + SMG = Sreeraman Mohan Girija; both self-report). C-suite derived from `Reporting To = founder` filter on the full roster: 6 entries with explicit `_role` (CTPO · CTPO · COO · CBO · CBO · CISO). 14 project leads written; most `_uncertain` flags removed where titles are unambiguous (JCP, Impetus, Samarth, Monobrands, External, Infrastructure all confirmed). Comment block updated to record the source.
- `organisation/organogram/index.html` (new) — the fourth subnav tab. Hero with 4 live stats (people in tree, root count, depth, manager count). Search box (debounced 120ms) jumps to a name and expands the path. Three expand controls (3 levels / all / none). Breadcrumb bar shows the path from root for the focused node, each crumb clickable. Tree nodes carry avatar (24px) + name + title + dept + location + date-joined + direct-report count badge. Click any node to expand/collapse. Cycle-safe — every recursive walk carries a `seen` set so the Imran ↔ Prashasy reporting cycle in the source data can't blow the call stack.
- All 4 organisation pages — subnav extended to 4 tabs: `Overview · Organogram · People Directory · External Commercialization`.
- `organisation/index.html` — JS unchanged but now consumes the richer `data.leaders` cleanly. The masthead renders Founders / CTPO / COO / CBO / CISO sub-rows automatically because the `_role` field grouping was already in the round-2 code. Project lead names + titles now show authoritative values from `leadership.json`.

Build output (post round 3):
```
rows: 1056   on RRL: 707   eng: 488 (46%)
photo hits: 918 / 1056
facets: 14 projects, 49 tracks
tiers:  rr-platforms=619 · external=310 · foundation=117 · adjacent=10
leaders: 2 founders, 6 c-suite, 14 project leads
tree:    1095 nodes, 2 root(s) ['Farooq Adam', 'SMG']
enrich:  1047/1056 rows joined to full roster (cxo + location)
unmapped: none
```

Verification (chrome-devtools MCP, port 8765):
- `/organisation/organogram` — Hero stats render: 1,095 people · 2 roots · depth 7 · 212 managers. Default-expanded to 3 levels (Founders → C-suite → Directors). Tree shows Farooq (root, ink-bg) → Jigar Dafda (CTPO, 26 reports) → Pratik Patel · Fahim Sakri · etc., each with avatar + title + dept + location + tenure. Cycle (Imran ↔ Prashasy) handled cleanly — no stack overflow.
- `/organisation` — masthead now reads as designed: FOUNDERS (Farooq + SMG) · CTPO (Jigar + Kushan) · COO (Salman) · CBO (Ragini + Ronak) · CISO (Vijay). Project lead block reads authoritative names (JCP → Jigar Dafda · CTPO; Impetus → Khaarthigha · Head of Delivery; External → Ragini Varma · CBO).
- `/organisation/directory` + `/organisation/external` — subnav extended to 4 tabs without disturbing existing rendering.
- `python3 tools/inject_chrome.py --check` → 72 unchanged (new organogram page picked up canonical chrome).
- Console: only the standing Tailwind CDN warning.

**Known data-quality items** (surface but not fix in round 3):
- 1 cycle in source data (Imran Khan ↔ Prashasy Ashok report to each other). Cycle is rendered cleanly (each appears under the other on first encounter, descendant chain truncates). Source-of-truth fix belongs in HRIS, not this build.
- 5 nodes (out of 1,095) unreachable from either root. They're part of small disconnected sub-trees (likely consultants whose Reporting To name doesn't normalize to a roster entry). Source-of-truth fix belongs in HRIS.
- 9 rows in the billed xlsx (1,056) not present in the full roster (1,047 enriched). Likely contractors or shared-service folks with different employee-id namespacing. Their cards still render with billed-roster fields; just no `cxo` / `location` / `dateJoined` enrichment.
- 7 `_uncertain: true` entries still in `leadership.json` (Granary, UCP & Marketing OS, ALP, RCPL, HireFirst, Central Support, JioGames, Neolync project leads). These need a hand-confirmation pass.

**Still deferred to round 4+:** Leader photos on project cards on Overview. External revenue / customer surfaces. Spot-fix the `_uncertain` leadership entries.

### 9.12 Round 3 follow-up · placeholder filter + HR delta report

**Trigger:** the round 3 organogram surfaced 7 keka rows that were org-chart placeholder seats (open hires + dummies) — `Jigar - Robotics`, `Jigar - Commerce Channel DoE`, `Jigar Extension Lead`, `Jigar Fynd Automation Commerce Lead`, `Jigar- JCP Projects`, `CBO India+Global`, `Fynd Dummy`. These should not appear in the public organogram.

**Placeholder filter** (in `tools/build_org_data.py` + `organisation/mappings.json`):
- New `placeholderNames` array in `mappings.json` — single source of truth for which keka names to drop. Edit this list when keka adds or removes placeholder seats.
- `build_tree()` pre-pass resolves each placeholder to its first non-placeholder ancestor (placeholders chain — e.g., `Jigar - Robotics` → `Jigar Extension Lead` → `Jigar Fynd Automation Commerce Lead` → `Jigar Dafda`). When a placeholder is dropped, anyone reporting to it is reparented to that ancestor; nobody becomes orphaned.
- Tree count went 1,095 → **1,088 nodes**. 7 placeholders dropped, 7 reparented reports preserved.

**HR delta report** (`tools/build_roster_delta_pdf.py`, output `docs/roster-delta-<date>.pdf` · gitignored):
- 3-page A4 PDF. Run `python3 tools/build_roster_delta_pdf.py` after each xlsx or keka refresh; share with HR for tally.
- Sections: Summary → keka-only real people grouped by department (Engineering 16 · Program 10 · Growth 7 · Finance 4 · InfoSec 2 · Research 1 · Tech Support 1) → placeholder seats (7) → billed-only (2: Gaurav Sharma · Vikas Tiwari) → duplicate Employee Numbers (the 8 ALP consultants sharing the placeholder id `Consultant`).
- Headline numbers: billed has 1,056 non-blank rows / 1,049 unique IDs (7 share id `Consultant`); keka has 1,095 rows / **1,088 real people** + 7 placeholders; intersection 1,047; 48 keka-only (7 placeholders + 41 real); 2 billed-only.

The PDF generator uses `reportlab` (already installed). Output filename embeds today's date so multiple runs don't overwrite each other.

### 9.13 Round 3 follow-up · organogram billed-only filter + KPI strip removal

**Trigger:** the round-3 organogram displayed all 1,088 keka real people (after placeholder filter), but several of those weren't on the billing sheet (~40 contractors). User direction: organogram should only show billed-roster members; keka should serve as the reporting-line metadata source only.

**Build-script change** (`tools/build_org_data.py`):
- `build_tree()` now takes a `visible_names` set (built from `data.rows[].name`).
- Two filter passes, identical chain-resolution mechanism:
  1. Placeholders (existing) — `mappings.json > placeholderNames`.
  2. Non-billed (new) — every keka name not in `visible_names`.
- A row is rendered only if its name passes both filters. When a row is dropped, anyone reporting to it is reparented to the first visible ancestor up the keka reporting chain. If the chain dies in the dropped set, the descendant becomes a root.
- Tree return value now also carries `droppedPlaceholder` + `droppedNonBilled` arrays for visibility.
- Build summary prints both drop counts: `dropped: 7 placeholders + 40 non-billed (reparented up the chain)`.

**Page change** (`organisation/organogram/index.html`):
- Removed the 4-tile KPI stat strip (people / roots / depth / managers) per direction. Hero is title + one-line subhead only.
- Subhead reworded: "Reporting tree across the billed roster. Click any node to expand its team. Search to jump to a name." (was: "Complete reporting tree from the keka roster…")
- Removed the now-unused `computeDepth()` helper and `setStat` calls in the `render()` function. Stat-strip CSS dropped.

**Build output after this change:**
```
tree:    1048 nodes (billed-only) · 2 root(s) ['Farooq Adam', 'SMG']
         dropped: 7 placeholders + 40 non-billed (reparented up the chain)
```

Both founders are billed (Farooq under "Farooq Adam", Sreeraman under "SMG"), so the tree renders with 2 roots as expected.

**Verified locally** via Chrome DevTools MCP — page loads cleanly, tree expands to 3 levels by default (Founders → C-suite → Directors), no console errors beyond the standing Tailwind CDN warning, search + collapse + breadcrumb all work as before.

### 9.14 Round 3 follow-up · Product Builders metric + page-copy clean-up

**Trigger:** /organisation hero showed "Engineering 46%" while the homepage showed the broader "60% product builders". Numbers didn't reconcile, and "Engineering 46%" undersold the org by excluding everyone in Product / Design / QA / Data / Research who is also a builder.

**Build-script change** (`tools/build_org_data.py`):
- New `meta.totals.productBuilders` and `meta.totals.productBuildersPct` fields. Definition (set in code): Engineering + Product + Design + Data Analysis + Data Science + Data Annotator + Quality Assurance + Research + Design Research + Fashion Design.
- Engineering count + percentage retained for backwards compat (other pages may still reference it).

**Page changes:**
- `organisation/index.html` hero tile: was "Engineering 46%" → now "Product Builders 66%". Caption: "Engineering · Product · Design · Data · QA · Research".
- `index.html` §09 ORGANISATION reconciled: prose line + tile both updated 60% → 66% with the same definition.
- `CLAUDE.md > Org stats · canonical-source rule` table updated: new row for Product Builders %, current value 66, full definition spelled out.

**File-path leak removed from page copy** (separate user feedback in same turn):
- `organisation/index.html` §01 lead — dropped "Edit `organisation/leadership.json` to update names, titles, and scopes." (implementation detail, leaks file path to Apex).
- `organisation/index.html` project-card lead-pending placeholder copy — was "pending — add to leadership.json" → now "pending confirmation".
- `organisation/external/index.html` §02 lead — dropped "Edit `organisation/leadership.json` to update names + scopes."
- `organisation/external/index.html` lead-pending fallback — was "Leadership pending — add to organisation/leadership.json under projectLeads…" → now "Leadership pending confirmation."

**Build output after this run:**
```
rows: 1056   on RRL: 707   eng: 488 (46%)   product builders: 699 (66%)
```

**Verified locally** via Chrome DevTools MCP — Overview hero now reads `1,056 / Product Builders 66 % / 10 / 13 yrs`. Masthead intro reads cleanly without the file-path reference. Lead-pending copy is implementation-free.

### 9.15 Round 3 follow-up · masthead trim + External co-leads

**Trigger:** the masthead carried CBO and CISO rows that didn't belong on the founders/C-suite stewardship view — CBO is the External Commercialization function (better surfaced there); CISO is an infrastructure role (not at the same hierarchy level). Per direction: move CBOs to External, drop CISO entirely.

**Changes:**
- `organisation/leadership.json` cSuite trimmed from 6 entries → 3 (CTPO × 2 + COO). Ragini Varma (CBO India), Ronak Modi (CBO Global), Vijay Hatewar (CISO) all removed.
- `organisation/leadership.json` projectLeads["External Commercialization"] changed from a single object → an array of 3 co-leads:
  1. SMG · Co-founder · Drives commercial and partnership strategy across the external book
  2. Ragini Varma · CBO India · India commercial
  3. Ronak Modi · CBO Global · Global commercial
- `organisation/external/index.html` `renderLeadBlock()` now handles either single object (legacy) or array (new). Renders an auto-fit grid (`minmax(260px, 1fr)`) so 3 cards lay out side-by-side on desktop and stack on narrow viewports. Inline grid style — no Tailwind JIT dependency.
- `organisation/index.html` masthead intro line removed ("Founders, then the C-suite layer that owns the platform stack.") — heading "Who runs Fynd." carries the meaning alone.

**Result:**
- Masthead reads cleanly: FOUNDERS (Farooq + SMG) · CTPO (Jigar + Kushan) · COO (Salman). Three rows, focused.
- External page §02 Leadership now shows the 3-card commercial leadership block. SMG appears in BOTH masthead (as Founder) and External (as commercial driver) — that's correct semantically; he plays both roles.

Build output unchanged on totals; only `data.leaders.cSuite` length dropped from 6 → 3 and `data.leaders.projectLeads["External Commercialization"]` is now an array.

**Verified locally** via Chrome DevTools MCP — both pages render correctly, console clean.

### 9.16 Round 3 follow-up · Apex feedback batch · de-invert + expand + tighten

Five targeted edits per Apex feedback:

1. **Expand RR → Reliance Retail in user copy.**
   - `organisation/index.html` §02 heading: "RR Platforms." → "Reliance Retail Platforms."
   - `organisation/index.html` §03 narrative: 2 occurrences of "RR" → "Reliance Retail".
   - `organisation/external/index.html` hero narrative: 1 occurrence of "RR" → "Reliance Retail".

2. **Drop project counts from tier-meta lines.**
   - `renderTier()` and `renderAdjacent()` now print just `${tier.total} people` (no `· N projects`).
   - `renderExternal()` no longer renders any tier-meta line — the "1 project · N sub-tracks" was redundant since the inverted block stated "310 PEOPLE" prominently.
   - Markup for `data-tier-meta="external"` removed entirely from the §03 header.

3. **De-invert the External Commercialization block.** Was ink-bg/white-text (felt out of register). Now: white card surface · 1px border · ink heading + body · ink-pill CTA. Same visual language as the rest of the page.

4. **Make "+N more" expandable inline.**
   - `projectCardHtml()` now renders ALL tracks: top-5 visible, rest in a hidden block under the toggle.
   - `wireMoreToggles()` (one delegated click handler on body) flips the toggle between "+N more · click to expand" and "− collapse", showing/hiding the rest of the tracks inline. No need to leave the page for the full list.

5. **Strip the masthead intro line** ("Founders, then the C-suite layer that owns the platform stack.") — heading "Who runs Fynd." stands alone now. *Already shipped in §9.15 build but completed here.*

Verified locally · all four pieces visible in browser · `+N more · click to expand` toggle confirmed working · External card renders in white with ink CTA · console clean.

### 9.17 Round 3 follow-up · Apex feedback batch 2

Eight items per Apex feedback. All shipped:

1. **Lead column dropped from project cards.** `projectCardHtml()` no longer renders the leadership.json-driven lead block. Cards are: name + count + share-of-tier bar + visible tracks + "+N more" toggle + drill-down. Lead names still surface in §01 Masthead and on the External page.
2. **Longtail Channels → Emerging Businesses.** mappings.json track displayName updated.
3. **Retail Vista promoted to its own card.** New `splitTracksAsProjects` config in mappings.json. `build_org_data.py` re-assigns matching rows from the parent project (UCP & Marketing OS) to the new virtual project (Retail Vista) so the directory drill-down works. UCP & Marketing OS tile dropped from 22 → 13 people; Retail Vista now 9.
4. **ALP → Asset Lifecycle Platform.** mappings.json project + track displayName updated.
5. **External Commercialization page · added customer logo grids + Fynd.com link.** Slides 9 + 10 of `Fynd Annual Board Update 2025-2.pptx` extracted as PNGs (via python-pptx) to `assets/organisation/external-customers-{india,global}.png`. New §04 India Customers and §05 Global Customers sections render the grids. New §06 Learn More section carries an "Open fynd.com →" CTA pointing at https://www.fynd.com.
6. **External narrative paragraph removed** from §03 hero block on Overview. The headline + stats stand alone.
7. **Section reorder.** §03 Shared Foundation now precedes §04 External Commercialization. The section labels are contiguous 01 → 05 across Overview.
8. **Foundation cards expand pattern.** Foundation cards use the same `projectCardHtml` as RR Platforms — the "+N more · click to expand" toggle applies automatically when a card has more than 5 tracks. Today both Infrastructure (4 tracks) and Central Support (1 track) fit within the visible 5, so the toggle doesn't render — but the mechanism is shared.

Build output:
```
rows: 1056   on RRL: 707   eng: 488 (46%)   product builders: 699 (66%)
facets: 15 projects, 49 tracks    ← +1 (Retail Vista split)
tiers:  rr-platforms=619 · external=310 · foundation=117 · adjacent=10
```

**Verified locally** · Overview reads §01 → §05 cleanly, all 5 changes visible in Chrome DevTools MCP. External page now has 6 sections (Sub-tracks · Leadership · Platform pages · India customers · Global customers · Learn more · fynd.com link). Console clean.

### 9.18 Round 3 follow-up · organogram default state

Per direction: don't auto-expand multiple levels. Page loads with Farooq + 1 level open; everything else (including SMG's subtree) only opens when clicked.

**Change** (`organisation/organogram/index.html`):
- `boot()` no longer calls `expandToDepth(3)`. Instead: `EXPANDED.clear()` then `EXPANDED.add("Farooq Adam")`. Renders.
- Result: Farooq is the only expanded node on first load; his 8 direct reports are visible (Jigar · Kushan · Salman · Ragini · Ronak · Nagabhushan · Neel · Nanditha). SMG appears as a collapsed root underneath. Click any ▸ to expand.

The three expand controls (Expand to 3 levels · Expand all · Collapse all) still work for power users who want to see deeper layers in one shot.

Verified locally · default state matches the requested behavior · console clean.
