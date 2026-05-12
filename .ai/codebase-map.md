# Codebase map · Fynd × Reliance Retail register

A static site that reports the state of every Fynd-built platform deployed across Reliance Retail. Audience: **RIL Apex leadership (MM Sir level)**. Hosted on Vercel; all static HTML; Tailwind via CDN.

Production URL: https://reliance-retail-fynd.vercel.app  
Local dev: `python3 -m http.server 8765`  
Auth bypass for local verify: `sessionStorage.setItem('fyndrrl_auth_v1', '1')` in DevTools console

---

## Top-level layout

```
.
├── index.html                  Home · platform-cards grid + filter chips · the entry point
├── style.css                   CSS variables + utility classes used across all pages
├── auth.js                     Confidential-overlay gate (SHA-256 password)
├── vercel.json                 cleanUrls: true · trailingSlash: false
├── CLAUDE.md                   Project memory for AI assistants (root-level)
│
├── .ai/                        AI-assistant artefacts (this map + future)
├── .claude/                    Skills + per-project Claude Code config
│
├── <route>/index.html × 28     One folder per top-level route
│   ├── impetus/                F&L AI platform (15 sub-platforms under /impetus/<slug>/)
│   ├── jcp/                    Jio Commerce Platform (with /channels/, /release-notes/, etc.)
│   ├── granary/                Grocery AI
│   ├── ucp/                    Unified Commerce Platform + Marketing OS
│   ├── alp/, retail-vista/, retail-jarvis/, samarth/, forge/, hirefirst/, swapeasy/
│   │                           Special projects
│   ├── boltic/, pixelbin/, ratl/, kaily/, fynd-konnect/, tms/, kio/
│   │                           AI-Native engineering platforms
│   ├── fynd-horizon/, autri/, dark-factory/
│   │                           Recent Innovations
│   ├── agents/                 Agent catalog (6 ship-ready agents under /agents/<slug>/)
│   ├── ai-native/              How Fynd builds (engineering culture)
│   ├── autonomous/             Autonomy framework (L0-L5)
│   ├── frameworks/             Farooq's working papers
│   ├── organisation/           4-tab section · subnav: Overview · Organogram · People Directory · External Commercialization
│   │   ├── index.html          §01 Leadership masthead · §02-05 tier sections (RR Platforms · External · Foundation · Adjacent)
│   │   ├── organogram/         Interactive collapsible tree · billed-only (~1,048 nodes · 2 founder roots) · keka used only for reporting lines · vanilla JS
│   │   ├── directory/          Filterable 1,056-row people directory · 4 filters · pager · URL-state sync
│   │   ├── external/           External Commercialization deep-dive (310 ppl · self-sustaining engine framing)
│   │   ├── data.json           BUILD ARTEFACT · all org-stats live here (committed) · see "Organisation · canonical source"
│   │   ├── mappings.json       Single source of truth · xlsx → display normalisation + tier + placeholder list
│   │   └── leadership.json     Authoritative founders / C-suite / project leads (hand-edited)
│   ├── culture/, fynd-academy/
│
├── assets/<route>/             Web-ready images for each route (mirrored to CDN for many)
├── images/                     Per-route image indexes (most binaries served from CDN, see .gitignore)
├── data/<route>/<slug>.yaml    Structured per-page data for renderers (e.g., data/impetus/, data/jcp/)
├── data/agents-x-platforms.yaml  CANONICAL source for agent ↔ platform deployment mapping. ALL "platform X uses agent Y" claims derive from here. Sweep via tools/inject_path_to_l4.py
├── linesheets/                 Source linesheets (large binaries, ignored)
│
├── docs/                       Spec docs · source-material compilations · audit history
│   ├── <route>-spec.md         Authoring spec per route (governs page structure, decisions)
│   ├── <route>-notes-compilation/   Raw source material per route (most ignored from git, see .gitignore)
│   ├── audits/                 docs/audits/<route>-audit-<date>{-vN}.json · audit history
│   └── 2026-04-30-farooq-mda-update-letter.md   The Apex cover letter that frames Recent Innovations
│
└── tools/                      Renderers + scratch
    ├── build_<route>.py        Per-route renderer (impetus, jcp, agents, etc.)
    ├── build_pages.py          Generic page builder
    ├── inject_subnavs.py       Sub-nav chip injector (TARGETS list hand-maintained)
    ├── site_chrome.py          CANONICAL source for topnav + footer + per-track subnavs · ALL nav edits go here
    ├── inject_chrome.py        Sweep tool · syncs nav + footer across all pages from site_chrome.py
    ├── inject_meta_robots.py   Sweep tool · injects <meta name="robots"> noindex into every page (SEO defence)
    ├── inject_path_to_l4.py    Sweep tool · syncs §03 Path to L4 sections + agent "Deployed in" blocks from data/agents-x-platforms.yaml
    ├── build_org_data.py       Builds organisation/data.json from 2 sources · billed xlsx (1,056) + keka full roster (1,095) · emits tiers, leaders, tree
    ├── build_roster_delta_pdf.py  Generates docs/roster-delta-<date>.pdf · 3-page A4 HR-tally artefact · diffs billed sheet vs keka HRIS
    └── scratch/                One-off helpers + screenshots (mostly ignored, see .gitignore)
```

---

## Page conventions

**Every page** carries:
- `<nav class="topnav">` mega-menu block (Tracks + More) — duplicated across all pages
- Crumb (`<div class="crumb">…</div>`) right under the nav
- `<div class="section-label">` opening every numbered section, contiguous `01 · NN`
- H1 (`<h1 class="display">`) once
- Footer: single copyright line `© YYYY RRVL · Jio Platforms Limited · Fynd · Strict internal circulation only`
- Imports: `/auth.js`, Tailwind CDN (`cdn.tailwindcss.com`), `/style.css`, Inter + JetBrains Mono fonts

**Every page does NOT carry:**
- A `Source · …` or `Author · …` attribution line — page-itself-as-artefact rule (provenance lives in spec + git)
- A `§Sources` block — always-remove rule (commit `e867725`)
- An `Owner · {name} · v{version}` footer line — deprecated chrome
- A hero `Author / Date / Version` block

**Section ordering** (canonical default · `website-section-authoring` SKILL.md §3):
- §0 Hero · §01 Status · §02 What's live · §03 Architecture · §04 Deep dive · §05 In flight · §06 Vision/Roadmap · §07 Research · §08 Sources (~~Sources block now removed register-wide~~)
- Overrides documented in each spec's §9 Decisions

---

## Nav + footer · canonical source

The mega-menu and footer HTML are duplicated across ~70 pages but should never be edited directly. The system has a single source of truth and a sweep tool:

- **`tools/site_chrome.py`** — canonical Python module with the menu data dicts (`PLATFORMS`, `SPECIAL_PROJECTS`, `AI_NATIVE`, `RECENT_INNOVATIONS`, `MORE_MENU`) and the `topnav()` / `footer()` renderers. Edit here.
- **`tools/inject_chrome.py`** — idempotent sweep tool. Reads `site_chrome.py` and rewrites the `<nav class="topnav">…</nav>` and `<footer …>…</footer>` blocks on every register page. Run after editing `site_chrome.py`.

```bash
python tools/inject_chrome.py --dry     # preview changes
python tools/inject_chrome.py           # write changes
python tools/inject_chrome.py --check   # verify drift; exits non-zero if any page diverges (CI / pre-commit)
python tools/inject_chrome.py --only path/to/index.html
```

**Drift mechanism:** if you edit a page's `<nav>` HTML directly without updating `site_chrome.py`, your edit gets silently reverted the next time anyone runs `inject_chrome.py`. That's how items disappear from the menu. Always edit the canonical, then sync.

**Excluded from the sweep:**
- `tools/` (`EXCLUDE_DIRS = {".venv", "node_modules", ".git", ".vercel", "tools"}`)
- Files not named `index.html` — e.g., `docs/impetus-index-backup-2026-04-30.html` is a frozen historical snapshot, intentionally untouched.

---

## Path to L4 · canonical source

The agent ↔ platform deployment mapping has the same canonical-source pattern as nav + footer. Every page that asserts *"agent X is deployed in platform Y"* (the §03 Path to L4 section on a platform page, or the "Deployed in" block on an agent page) is derived from a single YAML registry, not hand-edited.

- **`data/agents-x-platforms.yaml`** — single source of truth. Each agent slug lists its deployments + per-deployment "unlocks" string. Per-platform current rungs (L0–L5) also locked here. Edit this when an agent lands on a new platform OR an existing deployment changes state.
- **`tools/inject_path_to_l4.py`** — idempotent sweep tool. Reads the YAML and rewrites the content between `<!-- PATH-TO-L4-START -->` … `<!-- PATH-TO-L4-END -->` markers on each platform page AND the `<!-- DEPLOYED-IN-START -->` … `<!-- DEPLOYED-IN-END -->` markers on each agent page.

```bash
python tools/inject_path_to_l4.py --dry     # preview
python tools/inject_path_to_l4.py           # write
python tools/inject_path_to_l4.py --check   # CI / pre-commit gate · exits non-zero on drift
python tools/inject_path_to_l4.py --only impetus jcp   # restrict to specific slugs
```

**Drift mechanism:** hand-edits to either side (the §03 Path to L4 section OR the "Deployed in" block) get **silently reverted** by the next sweep. Always edit the YAML and re-run.

**5 platforms in scope:** Impetus · JCP · UCP · Granary · RetailVista. The other 17 platforms have **no** §03 Path to L4 section — their absence is itself the signal of where the agent program hasn't yet landed (per `docs/path-to-l4-spec.md` §7).

**6 agents in the registry** (the canonical 6 from `/agents/`): Cortex Planning · Trend-to-Design · Category Intelligence · AI Cataloging · Marketing · Retail Vista.

---

## Organisation · canonical source

Every org-wide number on the site (total headcount, on-RRL count, engineering %, per-project headcount, leadership names, organogram nodes) derives from one build that joins two sources. This is the same canonical-source pattern as nav + path-to-l4 — never hardcode an org-stat into a page; always derive from `organisation/data.json`.

> **Full lifecycle reference:** `docs/organisation-workflow.md` — sources, build script function-by-function, page-by-page render contract, verification protocol, common-edit recipes (~13 sections, ~480 lines). Read this before any non-trivial change.

### The 4 routes

`/organisation` is a section, not a single page. 4 tabs joined by a `subnav-link` pill bar at the top of each:

| Route | What it shows | Hydrates from |
|---|---|---|
| `/organisation` | Hero stats · §01 Leadership masthead · §02 RR Platforms tier · §03 External (inverted teaser) · §04 Foundation · §05 Adjacent | `data.{tiers, pivot, leaders, meta.totals}` |
| `/organisation/organogram` | Collapsible reporting tree · search · breadcrumb · 4 controls (default 3 levels / all / none / focus) | `data.tree.{nodes, rootNames, children}` |
| `/organisation/directory` | Filterable 1,056-row table · 4 filter pills · pager · sort · URL-state sync | `data.{rows, facets}` |
| `/organisation/external` | Self-sustaining narrative + sub-track table + 8 platform-page cards | `data.pivot[tier=external]` |

All 4 fetch the same `/organisation/data.json` on load. Pivot deep-link works: `/organisation/directory?project=Granary` pre-applies the filter.

### Sources + build pipeline

```
docs/org-notes-compilation/Team List Billed v2.xlsx   ──┐    (gitignored · 1,056 rows · billed roster · authoritative for tier rollups + project assignment)
                                                         │
~/Documents/work/engineering-os/docs/onboarding/         ├──►   tools/build_org_data.py   ──►   organisation/data.json   (committed)
keka_roster_full.csv                                     │       reads:                            shape:
(local-only · 1,095 rows · authoritative for             │        · billed xlsx                     · meta { source, totals { rows, onRRL, eng, engPct, photoHits } }
reporting tree + Reporting To + CXO + Date Joined)       │        · keka full roster                · facets { project, track, department, billing, kind }
                                                         │        · keka photo csv                  · tiers [ { key, label, order, total } ]
~/Documents/work/engineering-os/backend/data/keka/      ─┤        · organisation/mappings.json      · leaders { founders, cSuite, projectLeads }
employees.csv                                            │          (display + route + tier +       · pivot [ { project, projectRoute, tier, total, tracks, topTracks, moreTracks } ]
(local-only · 1,105 rows · employee_id → photo URL       │           placeholderNames)              · tree { nodes [...], rootNames, children { name → [child names] } }
on the impetusz0.de CDN)                                 │        · organisation/leadership.json    · rows [ { id, name, dept, title, manager, project, tier, track, kind, photo, cxo, location, dateJoined, ... } × 1056 ]
                                                         │
                                                         └─►   stdout summary: row counts · tier rollups · enrichment hit rate · unmapped report
```

### Files

| File | Role | Edit cadence |
|---|---|---|
| `organisation/mappings.json` | xlsx-value → display-name + route + tier; 14 projects + 49 tracks + 7 placeholder names | When xlsx adds a new Project/Track value, or a platform page is added/renamed, or the tier model changes |
| `organisation/leadership.json` | Founders / C-suite / 14 project leads — names + titles + scopes | Hand-edited only · authoritative · build script reads on every run |
| `organisation/data.json` | Build artefact (~22 K lines, ~600 KB) — committed for the live site to fetch | Re-generated · NEVER hand-edit |
| `tools/build_org_data.py` | The build itself · ~270 LOC · loads xlsx + 2 keka csvs + mappings + leadership · emits everything above | When schema changes (new fields, new derivations) |
| `tools/build_roster_delta_pdf.py` | HR delta report generator · 3-page A4 PDF for tally | When the report format needs adjusting |

```bash
python3 tools/build_org_data.py            # rebuild data.json
python3 tools/build_roster_delta_pdf.py    # generate docs/roster-delta-<today>.pdf for HR
```

### Tier model

The 14 xlsx Projects collapse into 4 tiers (declared in `mappings.json > projects[*].tier`):

| Tier | Projects | People | Visual treatment |
|---|---|---:|---|
| `rr-platforms` | JCP · Impetus · Granary · UCP & Marketing OS · ALP · RCPL · Samarth · HireFirst · Monobrands | 619 | 3-col card grid · ink section header |
| `external` | External Monetization (display: External Commercialization) | 310 | Inverted full-width block · self-sustaining narrative · own deep-dive page |
| `foundation` | Infrastructure · Central Support | 117 | 2-col card grid |
| `adjacent` | JioGames · Neolync | 10 | Inline footnote-row, no cards |

### Tree filter · billed-only

The organogram displays **only billed-roster members**. The keka roster is consulted for reporting lines (`Reporting To` chain) and per-node metadata (CXO, Date Joined, Location), but a node is rendered only if its Display Name appears in the billed sheet.

Two filter passes inside `build_tree()`, both using the same chain-resolution mechanism:

1. **Placeholders** — `mappings.json > placeholderNames` is the single source of truth for org-chart placeholder seats (open hires + dummies). Today it carries 7 entries: `Jigar - Robotics`, `Jigar - Commerce Channel DoE`, `Jigar Extension Lead`, `Jigar Fynd Automation Commerce Lead`, `Jigar- JCP Projects`, `CBO India+Global`, `Fynd Dummy`.
2. **Non-billed** — every keka name not present in `data.rows[].name`. Today this drops ~40 contractors who appear on the keka HRIS but aren't on the billing sheet.

Both work the same way: when a row is dropped, anyone reporting to it is reparented to the first visible ancestor up the chain. If the chain dies inside the dropped set (no visible ancestor reachable), the descendant becomes a root.

Build-time counts (today): 1,095 keka rows → drop 7 placeholders → drop ~40 non-billed → **~1,048 billed nodes** in the tree.

### Drift mechanism + unmapped report

`build_org_data.py` prints an end-of-build report:
- `tiers:  rr-platforms=619 · external=310 · foundation=117 · adjacent=10` — must add to the `data.meta.totals.rows`.
- `leaders: 2 founders, 6 c-suite, 14 project leads` — sanity-check from leadership.json.
- `tree: 1088 nodes, 2 root(s) ['Farooq Adam', 'SMG']` — confirms placeholder filter + roots.
- `unmapped: none` — OR a list of xlsx Project/Track values that have no entry in `mappings.json`. **Resolve by adding the entry** before committing.

### Spec lifecycle

`docs/organisation-spec.md` carries the full history of the 4 build rounds (§9 Round 2 scope locked → §9.10 Round 2 shipped → §9.11 Round 3 shipped → §9.12 Round 3 follow-up). Read §9 before touching the structure of any tab; it explains *why* each section exists.

### What NEVER to do

- Hardcode any org-wide number in a page (homepage, /organisation, anywhere). All numbers derive from `data.json`. After every rebuild, sweep for stale quotes (CLAUDE.md *Org stats · canonical-source rule*).
- Hand-edit `organisation/data.json`. It's a build artefact. Edit `mappings.json` / `leadership.json` and re-run the build.
- Add a 5th tab without updating the subnav block in **all 4 existing pages** + the new one. Subnav is page-local HTML (not driven by `site_chrome.py`).
- Drop a person from the directory without first adding them to `placeholderNames` if they're a dummy/open hire — otherwise their reports get orphaned.

---

## Skills (canonical instructions)

Located under `.claude/skills/`. Read these before editing pages, not training memory.

| Skill | When to use | What it covers |
|---|---|---|
| `website-tone-of-voice.md` | Every user-facing string | 5 rules · banned vocab · stat-tile / hero-subhead / card-lede formulas · pre-publish checklist · Reliance entity casing (RIL/RRVL/RRL/RBL/RCPL/JPL/RCP/HSEF/JioMart/AJIO/Tira/Reliance Trends/…) |
| `website-section-authoring/` | Adding a new top-level route | Stages 0-6 lifecycle · folder conventions · YAML schema · asset pipeline · GCS mirror · nav-wire checklist |
| `website-page-reviewer/` | Auditing a page before sharing with Apex | 8-phase protocol · 6-dimension scoring (source / tone / honesty / structural / visual / cross-page) · audit JSON schema |

The authoring skill calls itself the workflow; the tone skill is the rule-set; the reviewer is adversarial.

---

## Data + asset conventions

**Structured data** at `data/<route>/<slug>.yaml`. One YAML per sub-page. Renderer reads this. Schema norms:
- Header always: `slug`, `title`, `status` (live/pilot/build), `date` (ISO), `source_folder`, `source_citation`
- Body fields vary per route
- Approximations carry `~`: `~50` (string-quoted: `"~50"`)
- Dates ISO in YAML (`2026-04-07`); rendered `DD-MMM-YYYY`
- Asset paths absolute (`/assets/<route>/<file>.jpg`) or full CDN URL

**Images:**
- Local · `assets/<route>/<file>.jpg` · max 1600px wide · JPEG q80-82
- CDN · `https://socialassets.impetusz0.de/rrl-portfolio/assets/<route>/<file>.jpg`
- GCS · `gs://impetus-socialpilot/rrl-portfolio/assets/<route>/`
- For ≥20 files / ≥100 MB / explicit user request: full mirror via `gsutil -m cp -r` + `sed`-rewrite paths
- For 1-5 files: small-file carve-out — `gsutil -m cp <files>` + `sed`-rewrite + delete local copy (CDN-only)

**Lightbox** (page convention for product / UI / admin screenshots):
- Wrap each `<img>` in `<a href="<asset>" class="js-lightbox">`
- Drop the lightbox CSS + markup + script before `</body>` once per page
- Strip the infrastructure if the page has zero `<img>` to bind (avoids dead code)

---

## Audit + spec lifecycle

```
0 raw           docs/<route>-notes-compilation/   Source material (mostly ignored from git)
1 spec          docs/<route>-spec.md              Page-authoring spec (§3 page-structure, §9 Decisions)
2 data          data/<route>/<slug>.yaml × N      Structured per-page data
3 assets        assets/<route>/<slug>/            Web-ready images / PDFs
4 build         tools/build_<route>.py            Renderer (or hand-author for ≤6 sub-pages)
5 nav           Sweep edits to mega-menu          See website-section-authoring §8
6 verify        Local server + DevTools MCP       Audit per website-page-reviewer
audit JSONs     docs/audits/<route>-audit-<date>-{,vN}.json   Scored audit history
```

---

## Branch + deploy convention

- Always work on branch **`fynd-create-portfolio`**. Never branch off it.
- Commits accumulate; periodic PRs merge chunks into `master`.
- Vercel deploys `master` to https://reliance-retail-fynd.vercel.app
- 27+ PRs merged to date; this is a long-lived feature branch by design.
- Never push directly to master. Never delete `fynd-create-portfolio`.

---

## Common gotchas

- **`/tmp/` is sandbox-blocked.** Use `$TMPDIR` or write to `tools/scratch/` directly.
- **Bash CWD persists between calls.** Use absolute paths or reset with `cd /Users/.../reliance-retail-fynd && …`.
- **Auth.js gate blocks local verify.** Bypass via DevTools: `sessionStorage.setItem('fyndrrl_auth_v1','1'); location.reload()`.
- **Mega-menu drift.** New nav entry = ~70 files to edit. Use `grep -l 'mega-link">…' --include='*.html' -r .` to find them; sweep via Python script.
- **CDN ignores query strings.** Re-uploading `<file>.jpg` with `?v=2` doesn't bust the cache (max-age=3600). Use a versioned filename instead.
- **YAML headcount as int.** `headcount: ~50` parses `~` as null — use `headcount: "~50"` (string).
- **`cleanUrls: true`** doesn't strip `/index.html`. Write internal links as `/<route>` not `/<route>/index.html`.
- **Vercel does serve `/docs/`** despite the prefix sounding internal — links to `/docs/<file>.md` from page copy resolve.
- **EMF files** (Microsoft enhanced metafile) don't render in browsers. Convert to PNG via `soffice` (LibreOffice) or rebuild native.
- **PPTX > 50 MB** rejected by GitHub. Ignore the source `.pptx` (`.gitignore` handles common paths) and mirror to CDN.
- **Tailwind CDN warning** in console is the only acceptable noise (`cdn.tailwindcss.com should not be used in production`).
- **Reporting cycles in keka data.** The HRIS has at least one circular reference (Imran Khan ↔ Prashasy Ashok report to each other). The organogram JS handles this with a per-path `seen` set; if you write your own tree walker, do the same or you'll blow the call stack.
- **Browser cache on `/organisation/data.json`** is aggressive after a rebuild. When verifying locally via Chrome DevTools MCP, navigate with `ignoreCache: true` or hard-reload — otherwise you'll see stale numbers.
- **Force-push hazard on `fynd-create-portfolio`.** Multiple Claude tabs can race and produce sibling commits with identical content but different SHAs. If `git pull --rebase` chokes on `.claude/settings.json` (sandbox-blocked), `git push --force-with-lease` is safe **only when** `git diff <local-old-SHA> origin/<branch>` is empty (content equivalence verified).

---

## Quick reference — where to look for X

| Looking for | Path |
|---|---|
| Site-wide CSS variables (`--ink`, `--accent`, etc.) | `style.css:1-14` |
| Visual register (tokens, components, sweep deltas) | `docs/design.md` |
| Agent ↔ platform deployment registry | `data/agents-x-platforms.yaml` (sweep · `tools/inject_path_to_l4.py`) |
| Path to L4 spec (5 in-scope platforms · pattern · markers) | `docs/path-to-l4-spec.md` |
| Mega-menu HTML block | Any page · search `<nav class="topnav">` |
| Home-page platform-cards data array | `index.html` · search `const items = [` |
| Tone-of-voice rules | `.claude/skills/website-tone-of-voice.md` |
| Per-route spec | `docs/<route>-spec.md` |
| Per-route audit history | `docs/audits/<route>-audit-*.json` |
| The Apex framing letter | `docs/2026-04-30-farooq-mda-update-letter.md` |
| Build skeleton template | `.claude/skills/website-section-authoring/references/build-script-skeleton.py` |
| YAML data template | `.claude/skills/website-section-authoring/references/data-yaml-template.yaml` |
| Nav-wire checklist | `.claude/skills/website-section-authoring/references/nav-wire-checklist.md` |
| Audit framework rubric | `.claude/skills/website-page-reviewer/references/audit-framework.md` |
| Source-audit protocol | `.claude/skills/website-page-reviewer/references/source-audit-protocol.md` |
| Visual-audit checklist | `.claude/skills/website-page-reviewer/references/visual-audit-checklist.md` |
| **Organisation · full lifecycle workflow doc** | `docs/organisation-workflow.md` (read this before editing anything in `organisation/` or its tools) |
| **Organisation · all 4 pages + data + spec** | `organisation/{,organogram,directory,external}/index.html` · `organisation/data.json` · `docs/organisation-spec.md` |
| Org-stat canonical source (the single source of truth) | `organisation/data.json` (built from xlsx + 2 keka csvs by `tools/build_org_data.py`) |
| Org tier model (rr-platforms / external / foundation / adjacent) | `organisation/mappings.json > tiers` + per-project `tier` field |
| Org placeholder filter (open hires + dummies excluded from organogram) | `organisation/mappings.json > placeholderNames` (resolves through chain via `build_tree()`) |
| Founders + C-suite + project leads | `organisation/leadership.json` (hand-edited authoritative file) |
| HR roster delta (billed sheet vs keka HRIS) | `python3 tools/build_roster_delta_pdf.py` → `docs/roster-delta-<today>.pdf` (gitignored) |
| Org-stat sweep recipe | `CLAUDE.md > Org stats · canonical-source rule` |
