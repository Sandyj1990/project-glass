# /organisation · workflow + file inventory

The complete reference for how the `/organisation` section was built, what files participate, and how to extend it. Read this end-to-end before changing anything in `organisation/`, `tools/build_org_data.py`, or `tools/build_roster_delta_pdf.py`.

**Last updated:** 2026-05-03 · after round-3 follow-up (organogram billed-only filter + KPI strip removal · spec §9.13).

**Sister docs:**
- `docs/organisation-spec.md` — page-authoring spec (§1-9 Decisions). The structural why.
- `.ai/codebase-map.md > Organisation · canonical source` — the at-a-glance file map. The structural what.
- `CLAUDE.md > Org stats · canonical-source rule` — the never-do list. The forensic why.

---

## 1 · The audience problem this section solves

Audience: RIL Apex leadership (MM Sir level). They need to answer four questions in 30 seconds of scanning the page:

1. **Who runs Fynd?** — surfaced via §01 Leadership masthead on `/organisation` (Founders / CTPO / COO / CBO / CISO rows).
2. **How is the org structured?** — surfaced via the 4-tier model on `/organisation` (RR Platforms / External Commercialization / Shared Foundation / Adjacent).
3. **How does the org map to the platforms that ship?** — every project card links to its platform page; every track row links where mapped.
4. **How does the work pay for itself?** — the External Commercialization tier is given its own visual treatment (inverted full-width block) on Overview + a standalone deep-dive at `/organisation/external`.

Drill-down from Overview lands on `/organisation/directory` (1,056-row filterable table) or `/organisation/organogram` (1,048-node interactive reporting tree).

---

## 2 · The 4 routes

The section is **one URL prefix with four tabs**, joined by a `subnav-link` pill bar at the top of each page (vanilla HTML; no router):

```
┌──────────────────────────────────────────────────────────────────────────┐
│  Overview · Organogram · People Directory · External Commercialization   │
└──────────────────────────────────────────────────────────────────────────┘
   /organisation       /organisation/        /organisation/      /organisation/
                       organogram            directory           external
```

| Route | Purpose | Key sections | Hydrates from |
|---|---|---|---|
| `/organisation` | Editorial summary · 30s scan | Hero · §01 Masthead · §02 RR Platforms · §03 External (teaser) · §04 Foundation · §05 Adjacent | `data.{tiers, pivot, leaders, meta.totals}` |
| `/organisation/organogram` | Interactive reporting tree | Hero · search · 3 expand controls · breadcrumb · collapsible tree | `data.tree.{nodes, rootNames, children}` |
| `/organisation/directory` | Filterable people table | Hero · 4 filter pills · sortable 7-column table · pager | `data.{rows, facets}` |
| `/organisation/external` | Self-sustaining narrative + sub-tracks | Inverted hero block · sub-track table · lead block · 8 platform-page cards | `data.pivot[tier=external]` + `data.leaders.projectLeads["External Commercialization"]` |

All four pages do the same thing on boot: `fetch("/organisation/data.json")` → render. They share zero code (each is its own self-contained HTML + inline `<script>`), but they share the same source of truth.

**Subnav rule:** every time we add a new tab, the subnav block has to be hand-updated in **all 4 existing pages + the new one**. Subnav is page-local HTML, NOT driven by `tools/site_chrome.py`.

---

## 3 · Source files (gitignored)

Two source files. Neither is in this repo. Both are local-only and sensitive.

### 3.1 `docs/org-notes-compilation/Team List Billed v2.xlsx`
- **Sheet:** `Trupti -Updated Employee Master`
- **1,056 non-blank rows** · 1,049 unique Employee Numbers (7 ALP consultants share the placeholder id `Consultant`)
- **Authoritative for:** project assignment, billing entity, tier rollups, headcount totals, who's on the directory. The "billed roster".
- Columns: `Employee Number, Display Name, Department, Job Title, Reporting Manager, Billing Entity, Project, Track, Dedicated/ Platform, _, _, Average Rating 25-26, Average Rating 24-25` (last 2 columns dropped by the build script as sensitive).

### 3.2 `~/Documents/work/engineering-os/docs/onboarding/keka_roster_full.csv`
- **1,095 rows** · 1 per Employee Number, no duplicates
- **Authoritative for:** the reporting tree (`Reporting To` chain) and per-person metadata (CXO, Date Joined, Location). The "keka HRIS export".
- Columns: `Employee Number, Display Name, Email, Location, Department, Job Title, Reporting To, Date Joined, Time Type, Employment Status, Exit Date, Replacement Status, PROJECT, CXO's, Business Unit, Business Line, Role Type, Region`.
- **Important:** this file is the source of truth for **who reports to whom**. Both founders are in here (Farooq Adam + SMG = Sreeraman Mohan Girija); both are self-reporting roots.

### 3.3 `~/Documents/work/engineering-os/backend/data/keka/employees.csv`
- **~1,105 rows** · maps `employee_id → photo_path`
- **Authoritative for:** which employee has a CDN photo URL. Used purely as a join key.
- Columns: `employee_id, name, email, photo_path` (4 columns).
- Photo binaries are mirrored to `gs://impetus-socialpilot/rrl-portfolio/assets/keka-photos/` and served from `https://socialassets.impetusz0.de/rrl-portfolio/assets/keka-photos/<id>.<ext>`.

### 3.4 The 9 `data.rows` not in keka

When the build joins billed (1,056 rows) on Employee Number to the full keka roster, **9 rows have no keka match**. These are billed contractors using a different employee-id namespace (the 8 ALP "Consultant"-id consultants + Gaurav Sharma). They still appear in `data.rows` and on the directory; they just have no `cxo`/`location`/`dateJoined`/`reportingTo` enrichment, and they don't appear in the organogram tree.

---

## 4 · Build pipeline

Single build, single output. Run from repo root:

```bash
python3 tools/build_org_data.py
```

```
                    docs/org-notes-compilation/                         organisation/
                    Team List Billed v2.xlsx                            mappings.json
                                                                        (xlsx → display + tier
                                                                         + placeholderNames)
                                  │                                              │
                                  │                                              │
                                  ▼                                              ▼
                          ┌───────────────────────────────────────────────────────────┐
                          │              tools/build_org_data.py                       │
                          │                                                            │
                          │  1. load_mappings()      → projects + tracks + tiers      │
                          │                            + placeholders                  │
                          │  2. load_leadership()    → founders + cSuite + leads      │
                          │  3. load_keka_photo_map() → emp_id → CDN URL              │
                          │  4. load_full_roster()   → 1,095 keka rows                │
                          │  5. main loop            → 1,056 billed rows enriched     │
                          │  6. pivot construction   → per-project + per-tier         │
                          │  7. build_tree()         → drop placeholders + non-billed │
                          │                            reparent up the chain          │
                          │  8. write data.json + print summary + unmapped report     │
                          └───────────────────────────────────────────────────────────┘
                                  │                                              ▲
                                  │                                              │
                                  ▼                                       organisation/
                          organisation/data.json (committed)              leadership.json
                                  │                                       (founders + C-suite
                                  │ fetched on load by all 4 pages         + 14 project leads)
                                  ▼
                  ┌──────────────┬─────────────────┬──────────────┬─────────────────────┐
                  │ /organisation │ /organogram     │ /directory   │ /external           │
                  └──────────────┴─────────────────┴──────────────┴─────────────────────┘
```

Plus the two keka csvs come from a sibling repo (`engineering-os`), not this one.

---

## 5 · Files in `organisation/`

### 5.1 `organisation/mappings.json`
Hand-edited config. Single source of truth for:
- **Tier model** — declared in `tiers` (label + order per key) and per-project `tier` field.
- **xlsx → display normalisation** — projects + tracks have `displayName` + `route` + (track-only) `chips`. The build script lower-cases + trims track keys for case-insensitive matching against xlsx values that drift in capitalisation.
- **Placeholder names** — `placeholderNames` array lists keka rows that are open-hire seats / dummies. These are excluded from the organogram tree (their reports reparent up).

Schema:
```json
{
  "tiers": {
    "<tier-key>": { "label": "<display>", "order": 1 }
  },
  "kinds": { "Platform": "Shared", "Dedicated": "Dedicated" },
  "projects": {
    "<xlsx Project value>": {
      "displayName": "...",
      "route": "/path",
      "tier": "rr-platforms" | "external" | "foundation" | "adjacent"
    }
  },
  "tracks": {
    "<xlsx Track value>": {
      "displayName": "...",
      "route": "/path",
      "chips": [{ "label": "...", "route": "/path" }]
    }
  },
  "placeholderNames": ["Jigar - Robotics", "CBO India+Global", "Fynd Dummy", ...]
}
```

**When to edit:**
- xlsx adds a new Project or Track value → add a corresponding entry. Build script's unmapped report will tell you which.
- Platform page added or renamed → update `route`.
- Tier model changes → update `tier` per project + `tiers` block.
- Keka adds/removes placeholder seats → update `placeholderNames`.

### 5.2 `organisation/leadership.json`
Hand-edited config. Single source of truth for:
- Founders (2 entries · Farooq + SMG)
- C-suite (6 entries · CTPO × 2, COO, CBO × 2, CISO) — derived from "Reporting To = founder" filter on the keka full roster (round 3)
- Project leads (14 entries · one per xlsx Project) — derived from senior-title scan, hand-confirmed where possible

Schema:
```json
{
  "founders":     [{ "name", "title", "since", "scope", "displayName"? }],
  "cSuite":       [{ "name", "title", "_role": "CTPO|COO|CBO|CISO|...", "scope", "directReports"? }],
  "projectLeads": {
    "<project displayName>": { "name", "title", "scope", "_uncertain"? }
  }
}
```

**Why hand-edited:** the manager-column derivation is too noisy (Engineering Managers with the most reports surface as "leads" but aren't always the project lead by responsibility). This file is the place to record what's true; the build reads it on every run.

**`_uncertain: true`** on an entry means the round-3 derivation produced this name but the role isn't confirmed. 7 such entries remain after round 3 (Granary, UCP, ALP, RCPL, HireFirst, Central Support, JioGames, Neolync) — to be hand-confirmed in round 4+.

**`displayName`** on a founder entry overrides what's shown in the masthead/organogram (e.g., SMG's billed-roster name is the literal "SMG"; `displayName: "Sreeraman Mohan Girija"` makes the public render readable).

### 5.3 `organisation/data.json`
Build artefact. ~22 K lines, ~600 KB, committed (small enough). **Never hand-edit.** Regenerated by `tools/build_org_data.py` on every run.

Top-level shape:
```json
{
  "meta": {
    "source": "...path to xlsx + sheet...",
    "generated": "build via tools/build_org_data.py",
    "totals": {
      "rows",                 // 1,056 — billed roster size
      "onRRL",                // 707 — billing entity = RRL
      "engineering",          // 488 — Department = Engineering only
      "engineeringPct",       // 46
      "productBuilders",      // 699 — broad: Eng + Product + Design + Data + QA + Research
      "productBuildersPct",   // 66 — what /organisation hero + homepage §09 quote
      "photoHits", "photoMisses"
    }
  },
  "facets":  { "project", "track", "department", "billing", "kind" },
  "tiers":   [{ "key", "label", "order", "total" }, ...],
  "leaders": <copy of leadership.json>,
  "tree":    {
    "nodes": [{ "id", "name", "title", "dept", "location", "photo",
                "reportingTo", "cxo", "project", "dateJoined",
                "directReports" }, ...],
    "rootNames": ["Farooq Adam", "SMG"],
    "children": { "<parent name>": ["<child name>", ...] },
    "droppedPlaceholder": [...],
    "droppedNonBilled": [...]
  },
  "pivot":   [{ "project", "projectRoute", "tier", "total",
                "tracks": [...], "topTracks": [...top 5...], "moreTracks": N }, ...],
  "rows":    [{ "id", "name", "department", "title", "manager", "billing",
                "project", "projectRoute", "tier", "track", "trackRoute",
                "trackChips", "kind", "photo",
                "cxo", "location", "dateJoined", "reportingTo" }, × 1056]
}
```

**Drift mechanism:** the homepage `§09 ORGANISATION` once quoted `1,100+ people · 68 % product builders` for months while `/organisation` quoted the live `1,056 / 46 %`. Apex saw two different totals on the same site. Don't hardcode org-stats anywhere; always derive from `data.json`. Per-rule: **CLAUDE.md > Org stats · canonical-source rule**.

**Platform-page hydration · the protocol.** Twenty-two platform pages (`/jcp`, `/impetus`, `/granary`, `/ucp`, `/retail-vista`, `/boltic`, …) carry a §People-equivalent section that quotes platform-specific headcount. The two rules:

1. **No org-wide totals on a platform page.** Quotes like `1,056 people · 707 on RRL · 46% engineering · 66% product builders` belong on `/organisation` only. Platform pages link to `/organisation` for org-wide context.
2. **Quote only platform-scoped stats** derived from `data.json` filtered to the project — never read numbers off a deck or memory.

The helper script does the derivation:
```bash
python tools/derive_platform_org.py jcp        # case-insensitive
python tools/derive_platform_org.py granary
```
Output sections: total · track count + dedicated-vs-shared split · engineering % · product builders % · location mix · billing mix · per-track bar list with route classification (dedicated = `trackRoute` matches platform route prefix or is null; shared = trackRoute points at an adjacent platform).

Re-sync trigger: after any rebuild of `data.json` (i.e., after `tools/build_org_data.py` runs against a new xlsx), re-run the helper for each platform page that has a §People section and reconcile drift in track counts, names, percentages.

Reference implementation: `/jcp` §04 People — 2-column layout (tracks bar chart on left, named accountability on right), quotes only JCP-specific numbers, no org-wide echoes.

### 5.4 `organisation/index.html` (Overview)
~370 LOC vanilla HTML + CSS + JS. Renders:
- Hero (crumb · subnav pills · §0 stat tiles hydrating from `data.meta.totals`)
- §01 Leadership stewardship — text-only matrix masthead. Renders Founders + C-suite grouped by `_role`.
- §02 RR Platforms — 3-column card grid; each card shows project name (link if `projectRoute`), headcount, share-of-tier bar, lead from `leaders.projectLeads`, top-5 tracks (rest collapse into "+N more"), drill-down link to `/organisation/directory?project=<name>`.
- §03 External Commercialization — full-width inverted block (ink bg, white text) with self-sustaining narrative + 3-stat strip + CTA to `/organisation/external`.
- §04 Shared Foundation — 2-column card grid (Infrastructure + Central Support).
- §05 Adjacent JPL builds — inline footnote-row (Neolync · JioGames).

**Bar widths use share-of-tier**, not share-of-total — that way visual scale is meaningful within each block.

### 5.5 `organisation/directory/index.html` (People Directory)
The 1,056-row filterable table. 4 filter pills (Project · Track · Department · Dedicated/Shared) + free-text search + sortable columns + 50/page pagination + URL-state sync (`?project=Granary&track=Cortex` etc.).

Round-2 extracted this from the Overview page (it was the 02 section before). The pivot deep-link works: clicking a project card on Overview opens this page pre-filtered.

### 5.6 `organisation/external/index.html` (External Commercialization)
Standalone deep-dive. Hero with own H1 ("External Commercialization."), inverted hero block with the self-sustaining narrative, §01 sub-track table (Commerce 285 · Extensions 14 · Fynd Create 11), §02 lead block (Ragini Varma · CBO India), §03 platform-page card grid (8 cards: Boltic · PixelBin · Ratl · Kaily · Konnect · Horizon · TMS · Kio).

Narrative framing per round 2: *"The same IP shipped to RR is commercialized externally to paying customers. Revenue from this org pays for the platform investment that ships to Reliance Retail. Self-sustaining means the org pays for itself; not that it operates separately."*

### 5.7 `organisation/organogram/index.html`
Interactive collapsible tree. Renders `data.tree`. ~270 LOC vanilla JS, no D3 / no library.

Features:
- Default expanded to 3 levels (Founders → C-suite → Directors).
- Click any node to expand/collapse its subtree.
- Search box (debounced 120ms) jumps to a name and expands the path from root.
- Three expand controls: "Expand to 3 levels" / "Expand all" / "Collapse all".
- Breadcrumb bar shows the path from root for the focused node, each crumb clickable.
- Each node carries: avatar (32px circle, fallback initials) + name + title + dept + location + tenure + direct-report count badge.
- Founder rows render with ink-on-white inverted treatment.

**Cycle protection:** the keka roster has at least one circular Reporting To reference (Imran Khan ↔ Prashasy Ashok). All recursive walks (`renderNode`, `expandToDepth`, etc.) carry a per-path `seen` set so cycles can't spin the call stack.

**Billed-only filter:** post round-3 follow-up, the tree only renders nodes whose Display Name appears in the billed sheet. Keka is the source for reporting lines; billed is the source for who's visible. See §6 below for the build-side filter.

---

## 6 · `tools/build_org_data.py` — function-by-function

The whole build is one Python file (~310 LOC). Run from repo root: `python3 tools/build_org_data.py`.

### 6.1 `load_mappings()`
Reads `organisation/mappings.json`. Returns `(projects, tracks, kinds, tiers, placeholders)`.
- `tracks` keys are lowercased + trimmed for case-insensitive matching.
- `placeholders` is a `set[str]` for O(1) membership tests in the tree builder.

### 6.2 `load_leadership()`
Reads `organisation/leadership.json`. Returns the full dict (founders + cSuite + projectLeads). Falls back to an empty skeleton if the file is missing — the build still succeeds, the masthead just renders empty.

### 6.3 `load_keka_photo_map()`
Reads the 4-column `keka/employees.csv`. Returns `{employee_id: cdn_photo_url}` for use as a join key.

### 6.4 `load_full_roster()`
Reads `keka_roster_full.csv` (the 18-column HRIS export). Returns `(rows, by_emp_id)` where `by_emp_id` is the join lookup. Returns `([], {})` if the file is missing — the build still succeeds, just with no `tree` block and no per-row CXO/location/dateJoined enrichment.

### 6.5 `build_tree(full_rows, photo_map, placeholders, visible_names)`
The most subtle function. Filters the keka roster down to the visible (billed) population, walking through placeholder + non-billed chains so nobody is orphaned.

```
       full_rows (1,095)
            │
            ▼
   ┌──────────────────────┐
   │ Pre-pass:            │
   │ rt_by_name = {       │   build a name → reportingTo lookup
   │   "Farooq Adam":     │   from the full keka roster.
   │     "Farooq Adam",   │
   │   "Jigar Dafda":     │
   │     "Farooq Adam",   │
   │   ...                │
   │ }                    │
   └──────────────────────┘
            │
            ▼
   drop_set = placeholders ∪ (rt_by_name.keys() - visible_names)
            │
            ▼
   ┌──────────────────────┐
   │ resolve_visible(n)    │  for each dropped name, walk Reporting To
   │   walk up rt_by_name  │  chain until we hit a visible ancestor
   │   while in drop_set:  │  (or terminate at a cycle / missing entry).
   │     follow            │
   │   return ancestor     │
   └──────────────────────┘
            │
            ▼
   drop_resolves = { dropped_name: visible_ancestor_name, ... }
            │
            ▼
   ┌──────────────────────┐
   │ Main loop over full_rows:                    │
   │   if name in placeholders → skip + record    │
   │   if name not in visible  → skip + record    │
   │   else:                                       │
   │     rt = row.reportingTo                      │
   │     if rt in drop_set: rt = drop_resolves[rt] │
   │     emit node + add to children[rt]           │
   └──────────────────────┘
            │
            ▼
   Sort children by subtree size (biggest first).
   Compute directReports per node.
            │
            ▼
   return { nodes, rootNames, children,
            droppedPlaceholder, droppedNonBilled }
```

### 6.6 `main()` orchestration
- Loads xlsx → strips sensitive columns → for each row: normalises Project + Track via mappings, resolves tier, joins to full roster for CXO/location/dateJoined/reportingTo, joins to photo map, appends to `rows`.
- Tracks `unmapped_projects`, `unmapped_tracks`, `untiered_projects` — printed at end as the "unmapped report".
- Computes pivot grouped by Project, sub-grouped by Track. Top 5 tracks per project go into `topTracks`; rest stay in `tracks`.
- Computes tier rollups (people per tier).
- Calls `build_tree()` with `visible_names = {r.name for r in rows}` (billed-only filter).
- Writes `organisation/data.json`.
- Prints summary: row counts · tier rollups · leader counts · tree counts · enrichment hit rate · unmapped report.

### 6.7 What main() prints

```
wrote /Users/kushanshah/Documents/work/reliance-retail-fynd/organisation/data.json
  rows: 1056   on RRL: 707   eng: 488 (46%)
  photo hits: 918 / 1056
  facets: 14 projects, 49 tracks
  tiers:  rr-platforms=619 · external=310 · foundation=117 · adjacent=10
  leaders: 2 founders, 6 c-suite, 14 project leads
  tree:    1048 nodes (billed-only) · 2 root(s) ['Farooq Adam', 'SMG']
           dropped: 7 placeholders + 40 non-billed (reparented up the chain)
  enrich:  1047/1056 rows joined to full roster (cxo + location)
  unmapped: none — every xlsx Project + Track has a mappings.json entry, every project has a tier
```

Sanity checks to do after every build:
- Tier rollup must equal `meta.totals.rows` (619 + 310 + 117 + 10 = 1,056).
- `tree.nodes` count should be approximately `data.rows` count minus the ~9 not-in-keka rows (1,056 - 9 + small adjustments for join behavior = ~1,048).
- `unmapped: none` — if any drift surfaces, fix `mappings.json` first, re-run.

---

## 7 · `tools/build_roster_delta_pdf.py` — HR tally artefact

Run from repo root: `python3 tools/build_roster_delta_pdf.py`. Output: `docs/roster-delta-<today>.pdf` (gitignored).

### 7.1 What it does
Diffs `Team List Billed v2.xlsx` against `keka_roster_full.csv` by Employee Number. Categorises:
- Keka-only rows → real people (~41) vs placeholders (7).
- Billed-only rows → ~2 (HRIS-export gaps or contractor-id namespacing).
- Duplicate Employee Numbers in billed → 8 ALP consultants share id `Consultant`.

### 7.2 PDF structure (3 pages, A4)
- Header + sources + summary table.
- Section 1: keka-only real people, grouped by department (Engineering 16 · Program 10 · Growth 7 · Finance 4 · InfoSec 2 · Research 1 · Tech Support 1). Each row: Emp ID · Name · Job Title · Time Type · Reports to · Joined.
- Section 2: 7 placeholder seats with their reporting chain visible.
- Section 3: 2 billed-only rows.
- Section 4: duplicate-id group (the 8 ALP consultants).

### 7.3 Tech
ReportLab. `reportlab.platypus` flowables — `Paragraph`, `Table`, `TableStyle`, `Spacer`, `PageBreak`. A4, 14mm margins, footer with page number + provenance line.

### 7.4 When to re-run
- After every xlsx refresh (HR will want to see the delta).
- After any `placeholderNames` change.
- Output filename embeds the date, so multiple runs don't overwrite each other.

---

## 8 · The 4 build rounds — what each one shipped

Captured in detail in `docs/organisation-spec.md > §9`. Brief:

| Round | Date | Trigger | What changed |
|---|---|---|---|
| **1** (45c9994) | 2026-05-03 | `Team List Billed v2.xlsx` arrived (replacing v1) | v2 ingest. RR Counterpart column dropped at source. Build script pinned to v2. Homepage `§09` reconciled to v2 totals (1,056 / 60% / no `1,100+`). Added CLAUDE.md *Org stats · canonical-source rule*. |
| **1.5** (10e9006) | 2026-05-03 | UX feedback — directory was disconnected from pivot | Split People Directory into its own subnav tab at `/organisation/directory`. Pivot click → directory deep-link. Subnav: Overview · People Directory. |
| **2** (~d9c23da) | 2026-05-03 | UX feedback — page reads like an Excel pivot, no leaders, External Monetization not framed correctly | Tier model. Leadership masthead. RR Platforms card grid. External Commercialization deep-dive page. Subnav: Overview · People Directory · External Commercialization. |
| **3** (1f01d7a) | 2026-05-03 | Richer keka HRIS export with Reporting To arrived | Organogram tab. Tree built from keka. Leadership.json backfilled from authoritative `CXO's` column. Subnav: Overview · Organogram · People Directory · External Commercialization. |
| **3 follow-up · placeholder filter** (f7449c9) | 2026-05-03 | 7 placeholder seats surfacing in organogram | `placeholderNames` config in mappings.json. `build_tree()` reparent logic. HR delta PDF generator. |
| **3 follow-up · billed-only tree** (this) | 2026-05-03 | Organogram should match billed roster exactly | `build_tree()` second filter pass: drop non-billed names; reparent up the chain. KPI strip removed from organogram page. |

---

## 9 · Verification protocol

After every build or page change, before commit:

1. **Build runs clean:** `python3 tools/build_org_data.py` — confirm `unmapped: none`, sane totals.
2. **Chrome canonical not drifted:** `python3 tools/inject_chrome.py --check` exits 0 (per CLAUDE.md *Nav + footer rule*).
3. **Local dev server:** `python3 -m http.server 8765` (background).
4. **Auth bypass + verify each tab in Chrome DevTools MCP:**
   - `new_page http://localhost:8765/organisation/`
   - `evaluate_script` with `sessionStorage.setItem('fyndrrl_auth_v1', '1'); location.reload();`
   - `wait_for ["RR Platforms"]`
   - `take_screenshot` + `list_console_messages` (only the standing Tailwind CDN warning is acceptable)
   - Repeat for `/organisation/organogram/`, `/organisation/directory/`, `/organisation/external/`.
5. **Cache busting:** if `data.json` changed, force `ignoreCache: true` on first navigate. Browser cache on `/organisation/data.json` is aggressive otherwise.
6. **Org-stat sweep:** if any number changed, `grep -rnE --include='*.html' "1,?0[0-9]{2}|\\b[6-9][0-9]\\s*%\\s*product" .` and reconcile any drift.
7. **Stop server:** `kill $(lsof -ti:8765)`.

---

## 10 · Git workflow

Per CLAUDE.md `Workflow` section:
- Always work on `fynd-create-portfolio`. Never branch off it. Never push to `master`.
- Commits use `<area> · <thing> · <descriptor>` lowercase dot-separated style. Example: `organisation · round 3 · organogram tab + leadership backfill from full keka roster`.
- Stage only files you touched. Don't bundle parallel-session changes (they're someone else's commit).

**Race-condition note:** when multiple Claude tabs are working in parallel on the same branch, commits diverge. If `git pull --rebase` chokes on `.claude/settings.json` (sandbox-blocked path), and you've verified content equivalence between local and remote sibling commits with `git diff <local-old-SHA> origin/<branch>` showing empty diff, **`git push --force-with-lease` is safe**. Otherwise: amend the commit to drop `.claude/settings.json`, then rebase normally.

---

## 11 · Where to look for X — quick reference

| Looking for | Path |
|---|---|
| All 4 organisation pages | `organisation/{,organogram,directory,external}/index.html` |
| The build script | `tools/build_org_data.py` |
| The HR delta PDF generator | `tools/build_roster_delta_pdf.py` |
| The data artefact (don't hand-edit) | `organisation/data.json` |
| xlsx → display + tier + placeholders | `organisation/mappings.json` |
| Founders + C-suite + project leads | `organisation/leadership.json` |
| Page-authoring spec + decision log | `docs/organisation-spec.md` (especially §9) |
| Source xlsx (gitignored) | `docs/org-notes-compilation/Team List Billed v2.xlsx` |
| Keka full HRIS roster | `~/Documents/work/engineering-os/docs/onboarding/keka_roster_full.csv` |
| Keka photo map | `~/Documents/work/engineering-os/backend/data/keka/employees.csv` |
| Photo CDN base | `https://socialassets.impetusz0.de/rrl-portfolio/assets/keka-photos/` |
| Org-stats canonical-source rule | `CLAUDE.md > Org stats · canonical-source rule` |
| Codebase map (this section in brief) | `.ai/codebase-map.md > Organisation · canonical source` |

---

## 12 · Common edits — recipes

### Refresh the billed roster (new xlsx arrives)
1. Drop new file at `docs/org-notes-compilation/Team List Billed v2.xlsx` (overwrite).
2. `python3 tools/build_org_data.py` — read the unmapped report. Add any new Project/Track entries to `mappings.json`. Re-run until `unmapped: none`.
3. Verify locally per §9.
4. `python3 tools/build_roster_delta_pdf.py` and share with HR.
5. Commit `mappings.json` (if changed) + `organisation/data.json`.

### Refresh the keka roster (new HRIS export)
1. Drop new file at `~/Documents/work/engineering-os/docs/onboarding/keka_roster_full.csv` (overwrite).
2. Check for new placeholder names: `python3 -c "import csv; [print(r['Display Name']) for r in csv.DictReader(open('...keka_roster_full.csv')) if 'Dummy' in (r.get('Display Name') or '') or '+' in (r.get('Display Name') or '') or ' - ' in (r.get('Display Name') or '')]"`. Add any new ones to `mappings.json > placeholderNames`.
3. `python3 tools/build_org_data.py`.
4. Verify the organogram in Chrome. Check `tree:` count for sanity.
5. Commit `data.json` (+ `mappings.json` if placeholderNames changed).

### Confirm an `_uncertain: true` project lead
1. Open `organisation/leadership.json`. Find the entry. Edit `name` / `title` / `scope` to the confirmed values.
2. Remove the `_uncertain` and `_note` keys.
3. `python3 tools/build_org_data.py`.
4. Verify on `/organisation` that the project card shows the new lead without "pending confirmation" badge.

### Add a new top-level tab to `/organisation`
1. Update the `subnav-link` block in **all 4 existing pages**:
   - `organisation/index.html`
   - `organisation/organogram/index.html`
   - `organisation/directory/index.html`
   - `organisation/external/index.html`
2. Create the new page at `organisation/<slug>/index.html` with the same `subnav-link` block, `<slug>` marked active.
3. Page must fetch `/organisation/data.json` directly (or a sub-slice). Don't introduce a new build artefact.
4. Add the route to the table in §2 of this doc + spec §9.x.

### Reframe the External Commercialization narrative
1. Edit copy in `organisation/external/index.html` (hero block + section §01 lead) and the §03 teaser block in `organisation/index.html`.
2. Per CLAUDE.md tone-of-voice: no marketing voice, no `we`/`our`, no exclamations.
3. No build re-run needed (copy is HTML-baked).

### Drop a person from the organogram (open hire / dummy)
1. Open `organisation/mappings.json`. Add their exact Display Name to `placeholderNames`.
2. `python3 tools/build_org_data.py`.
3. Verify the build summary shows `dropped: N+1 placeholders + ...`.
4. Verify on `/organisation/organogram` that they're gone and their reports reparented up.

### Generate the HR delta report
```bash
python3 tools/build_roster_delta_pdf.py
# → docs/roster-delta-<today>.pdf  (gitignored)
```
Open in any PDF viewer. Share via your channel of choice; this file is not committed.

---

## 13 · Future work (not yet shipped)

Per `docs/organisation-spec.md > §9.8` and §9.10-§9.13:
- **Spot-fix `_uncertain` leadership entries** — Granary, UCP & Marketing OS, ALP, RCPL, HireFirst, Central Support, JioGames, Neolync project leads still need hand-confirmation.
- **Leader photos on project cards** — Overview cards currently show text-only leader names. Could load photos from the keka CDN.
- **External revenue / customer surfaces** — `/organisation/external` deep-dive doesn't yet show ARR/MRR or top external accounts. Pending data from BD.
- **Re-derive RR Counterpart from project data** — column was dropped in v2 xlsx and removed from the directory in round 1. Future work: derive each row's RIL counterpart from project-level data already maintained on platform pages (the `/jcp` page already names Abhijit Khasnis; `/granary` names Advait Pandit + Ved Antani; etc.).
