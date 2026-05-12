# Per-page changelog · feat/jcp-parity-fixes · 03-May-2026

Branch: `feat/jcp-parity-fixes` (off master) · 3 commits · 35 files modified · +2300/-493 lines.

Commits:
- `8ada75f` · Wave 1+2 · 30 pages · em-dash + sticky TOC + tone sweep
- `81565e6` · Wave 3 · 5 worst pages structural lift
- `f1b0731` · Wave 3.5 · close content-fidelity findings (regressions, dates, banned constructions, hero subhead trims)

Excluded per scope (untouched): `jcp/*`, `impetus/*`, `granary/`, `ucp/`, `agents/*`, `ai-native/`.

---

## Tier 1 platform pages · Wave 1 only (already had sticky TOC from PR #46)

### `rcpl/index.html` (72 → ~75)
- Hero subhead trimmed 32w → 26w
- Stripped 1 stray arrow operator from body prose

### `alp/index.html` (65 → ~76)
- §0 numbering bug fixed (renamed top "§0 · Hero" comment)
- Hero subhead trimmed 31w → 27w
- 13 arrow operators removed from body prose (kept diagrammatic uses)

### `retail-vista/index.html` (68 → ~78)
- §0 numbering bug fixed
- Hero subhead trimmed 39w → 30w
- 19 arrow operators removed from body prose

### `retail-jarvis/index.html` (60 → ~74)
- §0 numbering bug fixed
- Hero subhead trimmed 33w → 29w
- 24 arrow operators removed from body prose (31 → 7)

### `forge/index.html` (55 → ~85, also got Wave 3)
- §0 numbering bug fixed (cleaned debug "(was §05)" / "(was §04)" comments too)
- Hero subhead trimmed 40w → 25w
- 11 arrow operators removed
- **Wave 3:** §04 pilot table converted to 5 themed lens cards · §06 Roadmap section authored (4 phase cards: Pilot Live · Plant-wide · Multi-plant · Industry 5.0 · each with exit gate) · §07 Receipts grid with 8 source links

### `hirefirst/index.html` (70 → ~80)
- §05 numbering gap closed (renamed comment markers §06→§05, §07→§06, §08→§07)
- Hero subhead trimmed 31w → 27w
- Banned word "Comprehensive" → "Per-action" in audit-logs row
- 5 arrow operators removed

### `swapeasy/index.html` (68 → ~78)
- §0 numbering bug fixed
- Hero subhead authored from existing content (0w → 30w)
- Banned construction "is not a feature ... It is the re-commerce operating system" → direct statement
- 2 arrow operators removed

### `samarth/index.html` (48 → ~85, also got Wave 3)
- §0 numbering bug fixed
- Hero subhead trimmed 64w → 24w
- 15 arrow operators removed
- **Wave 3:** expanded from 4 to 8 sections · §02 Architecture (4 lens cards: Surface · Eligibility engine · Learning + OJT · Admin tower) · §05 Shipped (6 phase cards Oct-2025 → Apr-2026) · §06 Roadmap (3 phase cards A/B/C) · §07 Receipts (6 source links from samarth-plus-notes compilation)
- **Wave 3.5: 16 unhyphenated `Mon YYYY` dates → `Mon-YYYY` format** (Apr-2026, Oct-2025, Nov-2025, Dec-2025 to Jan-2026, Feb-2026, Mar-2026)

---

## Tier 2 product pages · Wave 1+2

### `pixelbin/index.html` (58 → ~70)
- 2 em-dashes → 0
- Sticky TOC + scrollspy added (5 sections, IDs added)

### `pixelbin/glamar/index.html` (52 → ~72)
- 2 em-dashes → 0
- Sticky TOC + scrollspy added (5 sections, IDs added)
- **Wave 3.5: hero subhead 40w → 28w**

### `pixelbin/videos/index.html` (41 → ~50)
- 2 em-dashes → 0 (CSS comment + body copy swapped)
- Sticky TOC: skipped (gallery page · video grid not narrative)

### `autri/index.html` (38 → ~85, Wave 3)
- 12 em-dashes → 0
- Sticky TOC + scrollspy added (9 sections)
- 7 we/our pronouns rewritten ("Tells us" → "Signal that"; "How we design against it" → "Mitigation")
- **Wave 3:** §02 6-dimension compliance table → 6 lens cards (Product presence · Product placement · Facing count · Price tag accuracy · Promotional execution · Shelf cleanliness) · §03 architecture flow caption added · §10 Receipts grid with 8 cards

### `boltic/index.html` (47 → ~80, Wave 3)
- 8 em-dashes → 0
- Sticky TOC + scrollspy added (5 sections, missing `<style>` block also added)
- **Wave 3:** Hero KPI tiles converted from 3 → 4 (modules · integrations · live RR brands · monthly executions) · §03 4-layer architecture as 4 lens cards (Pre-built · Platform core · AI · Apps + Data) · §06 Receipts grid with 9 source cards (6 console screenshots)

### `autonomous/index.html` (71 → ~80)
- 0 em-dashes (literal, already clean) · **Wave 3.5: 19 `&mdash;` HTML entities → 0** (Wave 1 missed entities, only swept literal `—`)
- Sticky TOC + scrollspy added (7 sections)
- 1 we/our rewrite ("How we measure progress" → "How progress is measured") · **Wave 3.5: 2nd we/our fix ("how do we use AI" → "how is AI used")**
- **Wave 3.5: 4 banned constructions "is not X. It is Y." rewritten** (lines 181, 193, 194, 304 · keep meaning, restructure form)
- **Wave 3.5: 3 "leverage" instances → "reach per decision" / rewrites** (lines 291, 413, 423)
- **Wave 3.5: hero subhead 49w → 26w**

### `dark-factory/index.html` (55 → ~70)
- 5 em-dashes → 0 (literal) · **Wave 3.5: 2 `&mdash;` HTML entities → 0**
- Sticky TOC + scrollspy added (11 sections)
- Status pills split: "Proposed/awaiting decision", "Alpha/Building", "Roadmap/Beta&Gamma" → 4 separate pills (Building / Pilot / Roadmap)

### `fynd-academy/index.html` (62 → ~70)
- 1 em-dash → 0
- Sticky TOC + scrollspy added (5 sections)
- Banned word "leveraging" → "applying"

### `fynd-horizon/index.html` (58 → ~75)
- 9 em-dashes → 0
- Sticky TOC + scrollspy added (8 sections)
- Banned word "Full-body picture" → "Full-body image"

### `fynd-konnect/index.html` (35 → ~88, Wave 3)
- 42 em-dashes → 0 (largest sweep)
- Sticky TOC + scrollspy added (6 sections, then 7 with Receipts)
- **Wave 3:** Hero 4 KPI tiles authored (~800 JioMart 3P brands · 3-4 L shipments/mo · 13 RBL capabilities 12mo · 50+ marketplaces) · Pillar 1 aggregator ecosystem table → 6 lens cards · Pillar 2 case-study metric tiles converted from `metric-tile` → canonical `card p-4` + `cap-num` + `display-2` pattern (4 tiles: 73% · 8.8% · 20% · 100%) · §07 Receipts grid with 6 source links
- **Wave 3.5:**
  - "7 platforms · 6 cards" inconsistency fixed: EasyEcom + OMSGuru combined card split into 2 separate cards (now 7 lens cards in §04 Pillar 1, matching the page's "7 platforms" claim)
  - 8 date format issues: `01 - May - 2026` (spaces) → `01-May-2026` · `May '25 - May '26` (4 sites) → `May-2025 to May-2026` · `between May 2025 and May 2026` (3 sites) → hyphenated
  - `<!-- §0 · HERO -->` comment → `<!-- §00 · HERO -->` (cosmetic)
  - Cross-ref miswiring fixed: `<a href="#pillar-1">§02 above</a>` → `<a href="#pillar-1">§04 above</a>` (link text now matches target section)

### `kaily/index.html` (64 → ~74)
- 3 em-dashes → 0
- Sticky TOC + scrollspy added (7 sections)
- **Wave 3.5: hero subhead 46w → 28w**

### `kio/index.html` (68 → ~75)
- 2 em-dashes → 0
- Sticky TOC + scrollspy added (7 sections)

### `ratl/index.html` (66 → ~76)
- 5 em-dashes → 0
- Sticky TOC + scrollspy added (6 sections)
- **Wave 3.5: hero subhead 35w → 27w**

### `tms/index.html` (65 → ~76)
- 9 em-dashes → 0
- Sticky TOC + scrollspy added (3 sections)
- 1 we/our pronoun fixed ("numbers we cannot cite" → "numbers without a citation")
- Hero subhead tightened ~40w → 30w · **Wave 3.5: en-dash 10–30 → "10 to 30"** (en-dash variant slipped past em-dash sweep)

---

## Meta + home

### `index.html` (home) (68 → ~78)
- 14 em-dashes → 0 (4 CSS comments + 10 body)
- Sticky TOC + scrollspy added (10 sections, all already had IDs)
- No content rewrite, no structural reorg

### `frameworks/index.html` (58 → ~75)
- 17 em-dashes → 0
- Sticky TOC + scrollspy added (3 sections, IDs `four-papers`, `how-connects`, `full-papers`)
- Banned word "harness" → "direct" (2 instances in body prose; Farooq fw-quote blockquotes left intact per spec)
- 1 we/our rewrite ("we have debated" → "the debate has been")
- **Wave 3.5: 4 banned constructions "is not X. It is Y." rewritten** in body paragraphs (technology gap → tempo gap; future prediction → present reality; identity → adoption rephrasing; AI Nirvana identity shift)

### `culture/index.html` (72 → ~76)
- 0 em-dashes (already clean)
- Sticky TOC + scrollspy added (5 sections)
- 1 we/our rewrite ("What our people say" → "What Fynd people say")
- 4 raw hex colours **left as-is** (no equivalent CSS vars exist in style.css)

### `docs/index.html` (65 → ~67)
- 1 em-dash → 0 (JS fallback string)
- Sticky TOC: skipped (reference / data-driven UI)

### `organisation/index.html` (70 → ~78)
- 15 em-dashes → 0 (2 CSS comments + 1 hero + 1 body + 7 JS placeholder + 4 JS comments)
- Sticky TOC + scrollspy added (4 sections, IDs `leadership`, `rr-platforms`, `shared-foundation`, `external`)

### `organisation/directory/index.html` (72 → ~75)
- 8 em-dashes → 0 (1 hero subhead + 7 JS template literal cell fallbacks)
- Sticky TOC: skipped (search/filter reference page)

### `organisation/external/index.html` (70 → ~73)
- 4 em-dashes → 0 (2 body + 2 JS strings)
- Sticky TOC: skipped (data-driven reference page)

### `organisation/organogram/index.html` (66 → ~70)
- 4 em-dashes → 0 (1 JS comment + 3 JS string literals)
- Sticky TOC: skipped (interactive tree page)

---

## Summary numbers

| Metric | Before | After |
|---|---|---|
| Em-dashes total | ~155 | 0 |
| Pages with sticky TOC | 9 (jcp + 8 Tier-1) | 27 |
| §0 numbering bugs | 7 platform pages | 0 |
| Banned vocabulary instances | ~6 | 0 |
| Banned constructions | 1 (swapeasy) | 0 |
| Pages with 4 hero KPI tiles | 9 | 14 |
| Pages with Receipts grid | 1 (jcp) | 6 (jcp + 5 Wave-3) |
| Pages with smart-narrative lens cards | 1 (jcp) | 6 (jcp + 5 Wave-3) |

---

## What was NOT touched (correctly excluded)

- `jcp/*` (master template, no edits to gold standard)
- `impetus/*` (all sub-pages)
- `granary/`
- `ucp/`
- `agents/*` (AI agents directory)
- `ai-native/`

---

## How to verify a page

For each page, run:
```
cd /Users/salmansaudagar/reliance-retail-fynd
grep -c "—" {page}/index.html         # must be 0
grep -c "story-toc" {page}/index.html # ≥6 on narrative pages, 0 on reference/gallery
grep -E '§0[^0-9]' {page}/index.html  # must be empty
```

Or visit `http://localhost:8765/{route}/` after running `python3 -m http.server 8765` from the repo root and confirm:
- TOC strip is sticky and visible on scroll
- Active TOC link highlights as you scroll past each section
- For the 5 Wave-3 pages: 4 hero KPI tiles render, lens cards render, Receipts grid renders at the bottom
