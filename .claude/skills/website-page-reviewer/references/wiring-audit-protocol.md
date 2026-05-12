# Wiring Audit Protocol

Register-wide sweep that validates internal route resolution, anchor integrity, asset paths, mega-menu coverage, sub-nav targets, and canonical-chrome consistency. Distinct from the per-page audit. Run when you need to confirm the site wires together cleanly — typically before a deploy, after a mega-menu sweep, or after a multi-page restructure.

**Why this is its own protocol.** Most checks here are not a "page property" — they only make sense across the whole register (every `href="/foo"` resolves to a real `index.html`, every `SUB_NAVS` entry has a target, no orphan top-level pages). A few checks (in-page anchor integrity, route refs from a single page) can run scoped, but the value is in running them across all 70+ register pages at once.

**First run produced** `docs/audits/wiring-audit-2026-05-03.md` — that file is the worked example of the output format below.

---

## Inputs

1. **Repo root** — typically `.` (the audit walks the tree)
2. **Live preview** — `http://localhost:8765/` (Python SimpleHTTP) for HTTP-status spot-checks. Optional but strongly recommended; a route that 200s on Python SimpleHTTP and 404s on Vercel is a known trap (see Phase 5).
3. **Optional scope filter** — restrict to a sub-tree (e.g., `jcp/*`, `agents/*`) when sweeping after a localized restructure. Default is the whole register.

---

## Output

Markdown report at `docs/audits/wiring-audit-<YYYY-MM-DD>.md`. Same severity model as the per-page audit (Critical / High / Medium / Low) but findings are register-scoped, not page-scoped.

```
1. SUMMARY
   - HTML pages scanned (count, with what was excluded)
   - Internal absolute href values (unique count)
   - Internal HTML routes (after stripping asset paths · unique count)
   - Anchor links (#fragment · unique count)
   - Internal asset references (count)
   - External (https://) links (count)
   - HTTP-only insecure (count · should be 0)
   - mailto / tel (count)
   - Net result · 1-line verdict

2. FINDINGS BY SEVERITY
   - Critical · navigation / canonical chrome that 404s for users
   - High · in-body broken (cards, buttons, inline anchors)
   - Medium · Receipts / footnotes
   - Low · in JS / comments / archived files (containment OK)

3. MEGA-MENU AUDIT
   - Count of top-level entries in tools/site_chrome.py (MENU_*)
   - Count of sub-nav entries (SUB_NAVS["..."])
   - Per-area resolution table: every entry resolves Y/N
   - Orphan top-level pages (exist on disk, not in mega-menu)
   - Sub-pages NOT in mega-menu but reachable from parent (deliberate, listed)

4. ANCHOR / TOC AUDIT
   - Pages with anchor links (count of N)
   - Total unique fragment values
   - Orphan anchors (link with no matching id on same page · should be 0)
   - Cross-page anchors (each validated against target file)

5. REDIRECTED ROUTES AUDIT
   - For each known-deprecated path: live HTML route refs vs legitimate asset path refs
   - Containment check on backup files (e.g., docs/impetus-index-backup-*.html)

6. RECEIPTS DEEP-CHECK (when applicable)
   - Per platform page that has a Receipts section: count of Receipts asset links + resolution rate
   - Aggregate: X/Y Receipts links resolve

7. LIVE PREVIEW HTTP CHECKS
   - Spot-check matrix: route → HTTP status (with notes for Vercel-vs-local divergence)

8. CHROME CONSISTENCY
   - inject_chrome.py --check result
   - inject_present.py --check result
   - inject_path_to_l4.py --check result

9. EXTERNAL LINKS (sanity)
   - Unique count, https-only count
   - Spot-check high-traffic destinations
   - No obviously stale subdomains

10. RECOMMENDATIONS
    - Ordered by impact (critical first)
    - Each: what's broken, where (file:line where applicable), suggested fix
```

---

## Workflow

```
Phase 1: INVENTORY
├── Walk the tree, listing every <href="..."> internal absolute link
├── Bucket into: HTML routes / anchor fragments / asset paths
├── Walk for every <id="..."> on every page (anchor-target side)
├── List external https:// links (sanity scope)
├── Note exclusions: tools/scratch/* extracts, docs/*-backup-*.html
└── Snapshot counts to seed the SUMMARY block

Phase 2: ROUTE RESOLUTION
├── For every internal HTML route href, check:
│   - Does <route>/index.html exist on disk?
│   - If route ends with a slug (no trailing slash), does <slug>.html exist?
├── Distinguish HTML routes from asset paths (legitimate /assets/<slug>/ that isn't a page)
├── Classify each unresolved route by severity:
│   - Critical · referenced from canonical chrome (mega-menu, sub-nav, footer)
│   - High · referenced from in-body card / button / inline anchor
│   - Low · referenced only from comments / JS strings / archived backup files
└── Build the FINDINGS BY SEVERITY block

Phase 3: ANCHOR INTEGRITY
├── For each href="#fragment" on each page:
│   - Does an id="fragment" exist on the SAME page?
│   - Orphan anchor → Medium finding (anchor jumps to nowhere)
├── For each href="/foo#fragment" cross-page anchor:
│   - Does foo/index.html have id="fragment"?
│   - Cross-page orphan → Medium finding
└── Build the ANCHOR / TOC AUDIT block

Phase 4: MEGA-MENU + SUB-NAV COVERAGE
├── Read tools/site_chrome.py: extract MENU_* and SUB_NAVS dicts
├── For each entry: does the target route resolve to a real index.html?
│   - SUB_NAVS["foo"] entry where foo/sub/ has children but no foo/sub/index.html → Critical
│     (Python SimpleHTTP serves a directory listing, Vercel 404s — see Phase 5)
├── List orphan top-level pages: directories with index.html that are NOT in any MENU_*
│   - Often deliberate (deep sub-pages, asset decks); list and confirm with author
├── Build the MEGA-MENU AUDIT block

Phase 5: VERCEL-VS-LOCAL DIVERGENCE TRAP
├── For each route that resolves on Python SimpleHTTP, also check:
│   - Does the resolution depend on directory-listing fallback?
│     (i.e., the directory exists with children but no index.html — local 200 via listing,
│      Vercel 404 because no auto-listing in production)
├── Spot-check the 5-8 most-likely-affected routes via HTTP HEAD
├── Any route in this trap → Critical finding (silent regression on deploy)
└── Note these explicitly in the LIVE PREVIEW HTTP CHECKS block

Phase 6: ASSET RESOLUTION
├── For every /assets/, /docs/, /images/, /data/ reference:
│   - Does the file exist on disk?
├── For each platform page with a Receipts section:
│   - Run a deep-check on Receipts links (PDFs, JPGs, internal page links)
│   - Report per-page resolution rate
├── Aggregate: X/Y unique asset references resolve · 0 missing OR list missing
└── Build the RECEIPTS DEEP-CHECK + asset count in SUMMARY

Phase 7: REDIRECTED ROUTES HYGIENE
├── For each known-deprecated HTML route (maintained list, e.g., /jcp/rcpl/ post-promotion):
│   - Count live HTML route refs (should be 0)
│   - Distinguish from legitimate asset path refs (e.g., /assets/jcp/rcpl/*.jpg may still
│     be the real on-disk location — this is OK if files resolve)
├── Containment check on backup files (docs/*-backup-*.html):
│   - Confirm 0 live pages reference the backup
│   - Recommend archiving (move to docs/_archive/ or rename with leading underscore)
└── Build the REDIRECTED ROUTES AUDIT block

Phase 8: CANONICAL CHROME CONSISTENCY
├── Run all three injection-tool --check commands:
│   - python3 tools/inject_chrome.py --check    (topnav + footer)
│   - python3 tools/inject_present.py --check   (present.* wiring + slide structure)
│   - python3 tools/inject_path_to_l4.py --check (agent ↔ platform registry)
├── Each must exit 0 with "0 patched, N unchanged"
├── Any drift → Critical finding (canonical source has been bypassed)
└── Build the CHROME CONSISTENCY block

Phase 9: EXTERNAL LINKS SANITY
├── Count unique external URLs
├── Confirm 0 plain HTTP (insecure)
├── Spot-check high-traffic destinations are on current canonical domains
│   (linkedin.com, github.com, fynd.com, ril.com, etc.)
├── No obviously stale subdomains
└── Build the EXTERNAL LINKS block

Phase 10: SYNTHESIS
├── Compile recommendations ordered by impact
├── Each: what's broken, where, suggested fix, effort estimate
├── Write the markdown report to docs/audits/wiring-audit-<YYYY-MM-DD>.md
└── Surface the count of findings by severity in the chat summary
```

---

## Severity classification (wiring-specific)

| Severity | Definition | Examples |
|---|---|---|
| **CRITICAL** | A route in canonical chrome (mega-menu, sub-nav, footer) 404s for the user · OR a chrome-injection tool reports drift · OR a route works on local SimpleHTTP and 404s on Vercel | `SUB_NAVS["granary"]` includes `/granary/research` but the directory doesn't exist · `inject_chrome.py --check` reports patched != 0 · `/impetus/photoshoots` is a directory with children but no `index.html` (Vercel 404 trap) |
| **HIGH** | An in-body card / button / inline anchor route doesn't resolve | A `<a href="/old-section">` from `/jcp/index.html` body that 404s |
| **MEDIUM** | An `href="#fragment"` anchor has no matching `id` on the same page · OR a cross-page anchor target is missing | TOC link `<a href="#section-04">` with no `id="section-04"` on page · `/jcp#autri` referenced from a live page where the anchor doesn't exist on `/jcp/` |
| **LOW** | Stale references contained in comments / JS strings / archived backup files | `/old-route` referenced only from `docs/impetus-index-backup-2026-04-30.html` (no live page links to the backup) |

---

## Common failure patterns

### 1 · The Python-SimpleHTTP-vs-Vercel directory-listing trap

The most-bitten footgun. Local preview (`python3 -m http.server 8765`) shows a directory listing for any directory missing `index.html`, returning HTTP 200. Vercel 404s the same path because production doesn't auto-list. Audits that run only against the local server miss this entire class of bug.

**Always check** — for every directory in `SUB_NAVS` whose route ends with a slug (e.g., `/foo/bar`), does `foo/bar/index.html` exist? If the directory has children but no own `index.html`, that's a **Critical** Vercel regression waiting to ship.

### 2 · `tools/site_chrome.py` is the canonical source for nav, NOT page HTML

Per `CLAUDE.md`, every nav / footer change goes through `tools/site_chrome.py` and is swept by `tools/inject_chrome.py`. Direct page-HTML edits get reverted on the next sweep. The wiring audit treats the rendered page chrome as a *check* against the canonical source — drift between them means someone bypassed the canonical and their edit will silently disappear.

### 3 · Asset paths that encode deprecated routes

When a route is renamed or promoted (e.g., `/jcp/rcpl/` → `/rcpl/`), the on-disk asset path may still encode the old structure (`assets/jcp/rcpl/*.jpg`). This is *not* a wiring failure — the assets resolve fine — but it's a **Low**-severity housekeeping note, because:
- Future readers wonder why RCPL assets live under `jcp/`
- A future cleanup may delete `assets/jcp/rcpl/` thinking it's orphaned

Recommend `git mv assets/<old>/<new> assets/<new>/` and update the `<img>` srcs as a low-priority follow-up.

### 4 · Backup files as anchor-orphan sources

Pages named like `docs/<route>-backup-<YYYY-MM-DD>.html` are explicit historical snapshots. They reference routes and anchors that may no longer exist. The audit should:
- Confirm 0 live pages link to the backup
- Treat dangling references *inside* the backup as **Low** severity
- Recommend moving to `docs/_archive/` or prefixing with `_` so future audits skip them cleanly

### 5 · Orphan top-level pages

Directories with `index.html` that are NOT in any `MENU_*` list. Sometimes deliberate (deep case studies under a sub-page, asset decks), sometimes a missed nav wire. Always **list explicitly** with the audit's read on which is which — let the reader confirm.

---

## When to run

- **Before any deploy** that touches `tools/site_chrome.py`, mega-menu structure, or any `index.html` at a route boundary
- **After any multi-page restructure** (e.g., a JCP-parity wave that touches 30 pages)
- **After any rename or promotion** (route moved up, sub-nav reorganized, page promoted to top-level)
- **Quarterly** as a baseline hygiene sweep, even when no recent change suggests it's needed

---

## What this audit does NOT do

- **Not a per-page audit.** For per-page source-traceability, tone, honesty, or visual checks, use the per-page workflow in `SKILL.md`.
- **Not a tone audit.** Em-dash counts, banned vocabulary, voice violations are out of scope here — they live in `audit-framework.md` §6 Mechanical Sweep Checks.
- **Not a design audit.** Inline-style density and raw hex literals are out of scope — they live in the per-page Phase 8 (Design-System Compliance).
- **Not a content-fidelity audit.** Whether a number on a page matches the source compilation is out of scope — that's the per-page Source Traceability phase.
