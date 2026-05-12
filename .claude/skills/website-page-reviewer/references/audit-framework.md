# Audit Framework

Scoring rubrics, pass/fail criteria, and detailed evaluation standards for the structural, honesty-register, and cross-page-consistency dimensions. Source-traceability and visual rubrics live in their own reference files.

## Table of Contents

0. Page-tier classification (run FIRST, before any scoring)
1. Structural Audit (Phase 2)
   - 1A · Canonical section ordering (default convention)
   - 1B · JCP parity matrix (platform pages only)
   - 1C · JCP 11-section shape (platform pages only)
2. Honesty Register Audit (Phase 5)
3. Cross-Page Consistency Audit (Phase 7)
4. Common failure patterns
5. Scoring weights & pass thresholds
6. Mechanical sweep checks (universal)

---

## 0. Page-tier classification

**Run this step before any scoring.** Different page types use different rubrics — applying the JCP parity matrix to `organisation/directory/` would manufacture failures the audit explicitly says don't apply. Every audit begins by placing the page in one of three tiers, then selecting the rubric for that tier.

### Tier A · Platform / product pages

Stories about a Fynd-built platform deployed at Reliance. The 11-section JCP shape (`bet · scale · coverage · people · architecture · properties · ai · path-to-l4 · shipped · roadmap · receipts`) and the full JCP parity matrix apply.

The 20 platform pages (as of the 03-May-2026 master audit):

```
rcpl, alp, retail-vista, retail-jarvis, forge, hirefirst, swapeasy,
samarth, pixelbin, autri, boltic, autonomous, dark-factory, fynd-horizon,
fynd-konnect, kaily, kio, ratl, tms, fynd-academy
```

Plus the **excluded-from-this-tier-because-already-canonical** set, which is held to its own bespoke shape (don't penalize against JCP parity, but DO apply universal checks):

```
jcp (the master template itself), impetus/*, granary, ucp, agents/*, ai-native
```

### Tier B · Specialty content pages

Pages with a meaningful narrative shape that isn't the platform template. Examples: home (`index.html` — register, not a platform pitch), `autonomous` (framework page), `frameworks` (methodology register), `culture` (values + life at Fynd), `docs` (internal index).

Apply: universal checks (§6) **+** *flexed* parity (sticky TOC strongly recommended; KPI hero / Receipts / People optional) **+** page-type-specific shape (no fixed canonical ordering — judge against the page's own spec).

### Tier C · Reference / interactive pages

Data-driven hydration surfaces or interactive tools that don't tell a narrative. Examples: `organisation/directory/` (employee directory hydrated from `data.json`), `organisation/organogram/` (interactive org chart). These pages don't need a sticky TOC, KPI hero, Receipts grid, or any of the platform-shape patterns.

Apply: universal checks (§6) **only**. Skip the JCP parity matrix entirely. Skip §1A canonical section ordering. Don't penalize missing TOC, KPI hero, lens cards, etc. — those are platform-page conventions, not register-wide rules.

### Selection logic

```
1. Is the page in the "already-canonical" exclusion set?
   → YES · apply universal checks + page's own spec; skip JCP parity scoring
2. Is the page in the Tier A platform list?
   → YES · apply universal checks + canonical ordering + JCP parity matrix + 11-section shape
3. Is the page a data-driven / interactive surface (no narrative)?
   → YES · apply universal checks ONLY
4. Otherwise (specialty content):
   → apply universal checks + flexed parity + page-specific spec
```

Record the selected tier in the JSON output's `tier` field (`A` / `B` / `C` / `excluded-canonical`).

---

## 1. Structural Audit

### Spec-compliance check

> **The spec is the truth, not sibling-page patterns.** Section presence and order are judged against the page's own spec (`§3 page structure`), not against patterns observed on other pages. If a page intentionally drops a "Recent Apex engagement" log or a "Connected platforms" grid because the author scoped it that way, the audit must NOT flag the absence as a structural gap. The canonical ordering convention in §1A below is the *default* — pages override it deliberately, and overrides are recorded in the spec's §9 Decisions.

For each section listed in the spec's `§3 page structure`, score:

| Check | Points | Criteria |
|---|---|---|
| Section present | 3 | The section exists with its spec'd label or close equivalent |
| Section in correct order | 2 | Appears in the position the spec puts it in |
| Section content matches spec intent | 3 | The block does what the spec said it would (e.g., "table with built-% per module" actually contains a table with built-% per module) |
| Section divider / chrome | 1 | Visual separation from the previous section (border, background-shift, label) |
| Section label numbering correct | 1 | The `<div class="section-label">NN · …</div>` matches the spec position |

**Max 10 points per section. Score = (total points / max possible points) × 100.**

### 1A · Canonical section ordering (default convention)

The register has converged on a section ordering — first applied at `/hirefirst` v0.9, then `/granary` v0.9.2 — that mirrors how an Apex reviewer reads top-to-bottom: status first, then what's running, then how it's built, then deep-dive, then forward-looking, then context, then evidence, then sources.

**Default order (8 sections + hero):**

| § | Title pattern | What it does | Notes |
|---|---|---|---|
| 0 | Hero | Eyebrow + H1 + 2-line subhead + status pills + stat tiles + (optional) format-cards strip | Cards strip absorbs short "Where this is live" sections |
| 01 | **Status** *(date)* / **What X is for Reliance** | 3-column Live/Building/Roadmap strip, OR the Problem/Solution/Impact framing | Picks the lens that earns the page |
| 02 | **What's live** / **Live for RIL today** | Module table with status pills + DRI + anchor outcome | The "running today" beat |
| 03 | **Architecture** *(N layers)* | 4-card layered diagram with status pills | Always positioned 03 — the "how it's built" answer Apex asks once |
| 04 | **Deep dive** (Command Centre / Five intelligence modules / etc.) | Visual-evidence section with screenshots or feature cards | The "show, don't tell" beat |
| 05 | **In flight** / **In development for RIL** | What's shipping in the next 1-4 weeks with named owners and gating steps | Building pills throughout |
| 06 | **Vision / Roadmap** *(scorecard)* | Honest built-vs-full table OR competitive landscape OR governance — context-broadener | The honesty fulcrum |
| 07 | **Research / Evidence** *(optional)* | Embedded paper, deep PDF, governance doc, or tech-stack section | Use when there's an authored artefact (research paper, governance brief) that earns its own section |
| 08 | **Sources** | Card list of every file cited, with paths and date stamps | Always last |

**Why this order earns its keep.** Apex skims top-down. *Status* tells them what's live. *What's live* shows the modules. *Architecture* answers "how is this built" once, so they don't ask three sections later. *Deep dive* gives evidence. *In flight* shows momentum. *Vision/Roadmap* is the honesty contract. *Research* is the authored evidence. *Sources* is the receipts.

**Exceptions / overrides — explicit list of acceptable deviations:**
- Skip §07 Research when the page has no authored research artefact (most pages won't).
- Drop §06 Vision when the page is small enough that the honesty contract sits in the §02 module table itself (e.g., single-product pages).
- Replace §03 Architecture with **Tech stack** when the page is more about the technology choices than layered abstractions (`/hirefirst` does this with §07 Tech Stack alongside §03 Architecture; either or both is fine).
- Insert **Governance & security** between §05 and §06 when compliance/audit is a load-bearing reader concern (`/hirefirst` §06).
- Insert **Competitive landscape** at §08 (before Sources) when comparison vs Workday/Greenhouse/etc. is the close (`/hirefirst` §08).
- Add **Built by / Team** as the second-last section, before Sources, when the team itself is part of the credibility story (`/hirefirst` §09).
- Move §07 Research **after** §06 Vision but **before** §08 Sources — never split it across the spine.

**How overrides are recorded.** Any deviation from the default ordering goes in the spec's §9 Decisions block as a `D{N} · Section ordering override` entry, with the *why* and the *how to apply*. The audit checks the spec for these entries; an undocumented override is a MEDIUM finding.

**What is NOT in the canonical ordering** (these are page-specific patterns, never required):
- "Connected platforms" grids (cards linking to sibling tracks)
- "Recent Apex engagement" dated logs (register-wide pattern, not page-specific)
- "Where this is live" 3-format strips (absorb into hero per /granary v0.9.2 precedent)

If the audit finds any of the above as standalone sections, it's not a violation — but worth flagging as LOW with a note: "consider absorbing into hero or moving to a sibling page if the section is not earning its rent". The reviewer is offering the convention, not enforcing the absence of these.

### 1B · JCP parity matrix · TIER A ONLY

`/jcp/` is the master template for platform/product pages (codified by the 03-May-2026 master audit, after PR #46). When auditing a Tier A page, score each binary check below. Each fail is a HIGH finding when missing on a platform page; do NOT apply to Tier B/C pages.

| Check | Pass criterion | How to verify |
|---|---|---|
| **Sticky TOC** | `.story-toc` block present in HTML; IntersectionObserver scrollspy fires on scroll | `grep -n 'class="story-toc"' <page>/index.html` AND open in browser, scroll, confirm active states change |
| **Hero subhead** | Present (not zero words), ≤30 words | Count words in the `<p>` directly under `<h1>` |
| **KPI tiles** | 4-tile hero KPI strip below the subhead | `grep -c 'class="num-display\|kpi-tile' <page>/index.html` ≥ 4 |
| **Lens cards** | Smart-narrative lens cards (NOT raw `<table>` for module/property listings) | Sections that quote modules/properties use `<div class="card">` blocks with explanatory copy, not `<table>` rows |
| **Receipts grid** | `§receipts` section with proof artefacts (PDFs, JPGs, internal links) | `grep -n 'id="receipts"' <page>/index.html` AND visual confirm of artefact grid |
| **People bar chart** | `§people` section with bar-chart pattern | `grep -n 'id="people"' <page>/index.html` AND visual confirm |
| **§nn contiguous** | Section labels are `01 02 03 …` — no `§0`, no gaps | `grep -n 'section-label mb-3">[0-9]' <page>/index.html` (see also §1 contiguity check) |
| **Em=0** | Zero em-dashes (`—`) in body copy | `grep -c '—' <page>/index.html` (excluding inline `<style>` blocks if any) |

**Severity calibration:** missing Receipts grid OR missing People bar chart OR missing sticky TOC are each HIGH on a Tier A page. Em-dashes >0, §0 contiguity bug, hero subhead >30 words are each MEDIUM (mechanical to fix). Lens cards missing where raw tables are present is HIGH (structural rewrite needed).

### 1C · JCP 11-section shape · TIER A ONLY

The full canonical platform-page shape, also codified by the 03-May-2026 master audit:

```
bet · scale · coverage · people · architecture · properties · ai · path-to-l4 · shipped · roadmap · receipts
```

For a Tier A page, list which of these 11 sections are present and which are missing. Sections missing on the JCP master template itself (none today) become exceptions; sections missing only on the audited page become findings.

**How to verify:** for each section in the list, grep the page for an `id="<section-name>"` or a `section-label` text matching the section. Aggregate into a coverage table:

| Section | Present? | Notes |
|---|---|---|
| bet | ✓/✗ | |
| scale | ✓/✗ | |
| coverage | ✓/✗ | |
| people | ✓/✗ | + bar chart? |
| architecture | ✓/✗ | |
| properties | ✓/✗ | |
| ai | ✓/✗ | |
| path-to-l4 | ✓/✗ | + auto-rendered from `data/agents-x-platforms.yaml`? |
| shipped | ✓/✗ | |
| roadmap | ✓/✗ | |
| receipts | ✓/✗ | + artefacts resolve? |

Severity per missing section: **MEDIUM** by default; **HIGH** if it's a flagship beat (people, path-to-l4, receipts).

Pages from the "already-canonical excluded set" (impetus, granary, ucp, agents/*, ai-native) get scored against their *own* spec's section ordering, not against the JCP 11-section shape. Their shape diverges deliberately.

### Page-chrome check

Every page on the register must include this chrome. Each missing item is a HIGH-severity finding:

| Item | Required | Severity if missing |
|---|---|---|
| `<nav class="topnav">` mega-menu block | Yes | HIGH |
| Crumb (`<div class="crumb">…</div>`) | Yes | MEDIUM |
| Section-page subnav (Overview / Research / etc.) | If page has subroutes | HIGH |
| `<div class="section-label">…</div>` opening every numbered section | Yes | MEDIUM |
| H1 (`<h1 class="display">…</h1>`) | Yes | HIGH |
| Footer with single copyright line (`© YYYY RRVL · Jio Platforms Limited · Fynd · Strict internal circulation only`) | Yes | HIGH |
| `<script src="/auth.js">` | Yes | HIGH (page won't be gated otherwise) |
| Tailwind CDN link | Yes | HIGH |
| `style.css` link | Yes | HIGH |

### Section-label contiguity

The page's section labels (e.g., `01 · Status today`, `02 · What's live in production`, …) must be a contiguous run with no gaps and no skips.

```bash
grep -n 'section-label mb-3">[0-9]' <page>/index.html
```

The numbers should be `01 02 03 04 …` in order. If a section was deleted mid-page, every subsequent label must shift down. A skipped number is a MEDIUM finding.

### Version-pill consistency

The nav pill (`<span class="nav-version">v0.X.Y</span>`) is the only version-display element that survives. There's no Hero author line and no footer Owner-version line to cross-check against — both have been deprecated (see *Forbidden chrome* below). The nav pill is purely developer-facing tracking.

### Forbidden chrome (presence is a finding)

The register has explicitly *removed* these chrome elements; a page that still carries them needs a fix.

| Item | Severity if PRESENT | Notes |
|---|---|---|
| Hero `<strong>Author:</strong> … <strong>Date:</strong> … <strong>Version:</strong> …` line | HIGH | Page-level metadata belongs in git history + the spec, not on the page. Apex doesn't review version numbers. Use `tools/scratch/strip_author_owner.py` to sweep. |
| Footer `Owner · {name} · v{version}` line | HIGH | Same rationale as above. |
| Standalone "Connected platforms" / "Recent Apex engagement" / "Where this is live" sections | LOW (note, not block) | See §1A canonical ordering — these patterns are not part of the convention; absorb into hero or sibling pages. |

---

## 2. Honesty Register Audit

The site uses three status pills as the honesty contract: `Live`, `Building`, `Roadmap` (`Pilot` is also present in legacy CSS but is gradually being subsumed by `Building`).

### Pill-presence check

For every status claim on the page, verify it carries a pill or is explicitly tagged inline with one of the three states:

- ✓ `<span class="pill pill-live">Live</span>` adjacent to the claim
- ✓ Inline qualifier: *"engine Live; UI in build"*
- ✗ Bare claim: *"Command Centre is the unified platform"* without specifying its state

### Pill-source-match check

For each pill, the surrounding sentence must match what the most-recent source file says. Use the source compilation folder to verify.

| Pill on page | Source must support |
|---|---|
| `pill-live` | Source explicitly says "live", "in production", "deployed", "shipped", or equivalent |
| `pill-build` | Source says "in build", "in test", "in SIT", "deployed in SIT but UI in design", "dev complete pending test" |
| `pill-phase2` (Roadmap) | Source lists it under future plans, planned, upcoming, next-horizon |

If the source says "in build" and the pill says `Live`, that is a CRITICAL overclaim. If the source says "live" and the pill says `Building`, that is a HIGH underclaim (Apex reads it as Fynd hedging).

### Mixed-tier-in-one-sentence check

A sentence cannot mix pill tiers without inline tagging. Flag any sentence that asserts a Live thing and a Building/Roadmap thing without distinguishing them.

- ✗ *"Cortex Planning, the Command Centre, and Consensus Forecasting consolidate the planning surface."* (Live + Building + Roadmap, all undifferentiated)
- ✓ *"Cortex Planning (Live) feeds the Command Centre (in build); Consensus Forecasting is on the roadmap."*

### Forward-looking phases without dates

Per `website-tone-of-voice.md` §3 last bullet:

> Forward-looking phases without dates. *"Phase 0: Stability · Phase 1: Enterprise · Phase 2: Integrations · Phase 3: Intelligence."* Marketing-deck register, not Apex register. If a section makes time-promises, every promise carries a date or a named DRI. Otherwise cut the section.

Flag any "Phase X / Phase Y" strip on the page where phases lack dates or named DRIs. HIGH severity. Reference: HireFirst v0.9 cut its 4-phase strip for exactly this reason.

### Vision-vs-live framing check

If the source compilation folder includes a status report with built-% per module, verify the page's vision section (if present) matches that report. Drift is MEDIUM unless the drift overclaims (then CRITICAL) or underclaims by 2+ points (then HIGH).

---

## 3. Cross-Page Consistency Audit

The site's pages cross-reference each other through several mechanisms. When one page changes, sibling pages drift.

### Mega-menu drift

The top-nav mega-menu HTML block is duplicated on every page (~25 files). If this page changed any mega-menu entry (added, renamed, dropped a section), every other page drifts until updated. To check:

```bash
grep -l 'mega-link">Granary' --include='*.html' -r .
# Compare each occurrence's mono-suffix and spelling to this page's nav block.
```

Stale mega-menu on a sibling page is a LOW finding per page (the user has accepted lazy-strategy in the past); but if the section was renamed (not just refreshed), that's a HIGH finding because the old name is now an inconsistency.

### Home page card

`index.html` typically carries a card linking to the page (e.g., `<a href="/granary" class="card card-hover p-6 block">`). The card has a status pill and a 1-2-line summary that often quotes a key stat from the page. To check:

```bash
grep -n -A 4 'href="/<slug>"' index.html | head -30
```

For each stat on the home card:
- Is the same number on the page? (HIGH if mismatch — Apex reads both)
- Is the status pill matched? (HIGH if mismatch)
- Are dates / cohort sizes / lead names current? (MEDIUM if stale by < 2 weeks; HIGH if stale by > 1 month)

### Catalog page

`catalog/index.html` lists the section under its own header with a row-table of the section's IPs (Live / Pilot / Build status, owner, summary). When the page drops or renames an IP (e.g., Granary v0.9 dropped Price & Promotion Intelligence), the catalog still lists it. Sweep:

```bash
grep -n '<section name>' catalog/index.html | head -20
```

Any IP listed in catalog as `Live` that the page does not show is a HIGH finding (catalog overclaims).

### Numbers, dates, names

Build a table of the top 10-15 facts from the page (numbers, dates, named people). Grep each across all sibling HTML files. Each mismatch is a finding. Examples:

- "11 Mumbai stores" — does any page still say "10 Mumbai stores"?
- "+3.8pp on-shelf availability" — appears identically everywhere it appears?
- "Mayank Jain" — never spelt "Mayank Jaine" or "Mayank J." anywhere?

---

## 4. Common Failure Patterns

These recur across audits. Spot them early.

### Source-traceability failures

- **Hero stat without a source line.** A `48M rows` tile without "Source · …" beneath is acceptable only if the same stat is sourced elsewhere on the page. Otherwise MEDIUM.
- **Date attribution drift.** Page says "case study 17-Apr-2026" but source folder has the file dated 04-Dec-2025. Investigate; either update the page date or surface the discrepancy.
- **Names from memory.** A name appears once (Vincent Braganza) and is correct, then appears later as "Vincent Braganza, COO" but the source doesn't carry the title. MEDIUM — title needs source.

### Tone-of-voice failures

- **"World-class" / "industry-leading" sneaking back in via a card lede.** Often introduced when the author paraphrases a source rather than restating in register. HIGH.
- **Trailing summary at end of a section.** *"In summary, this section showed…"* HIGH; reader scrolled past it.
- **"Empowers / Enables / Unlocks" filler verbs.** Replace with the actual verb. MEDIUM.
- **Date format drift.** *"April 28, 2026"* instead of *"28 - Apr - 2026"*. MEDIUM (only LOW if it appears once in a non-prominent spot).
- **Engineering jargon in hero / above-the-fold tiles.** `routes`, `endpoints`, `UAT tables`, `IRM`, `ODBC`, `RBAC`, `multi-tenant backend`, `production`, `prod deploys`, `production-grade`, etc. Apex reads these as developer-talk; the numbers may be true but they don't carry meaning to the reviewer. HIGH if in hero stat tiles, MEDIUM in body copy, LOW deep in §03 architecture or §04 deep-dive (where the surrounding context earns the term). See `website-tone-of-voice.md` §7 Engineering jargon translation table for substitutes.
- **Reliance entity confusion.** `RIL` (parent group) vs `RRL` (Reliance Retail) is load-bearing — using `RIL counterparts` when the actual counterparts are at RRL is a HIGH finding. Same for any entity-name mix-up.

### Honesty register failures

- **"All modules complete" / "Phase 1 done" framing when source says "5 of 37 routes wired".** CRITICAL — the kind of overclaim Apex catches.
- **Pill-less status statement in hero.** Hero is the most-read part; missing pill is HIGH.
- **Vision table with built-% but no source citation.** MEDIUM.

### Cross-page failures

- **Home card refreshed but catalog not.** HIGH — the catalog is a sibling Apex looks at often.
- **Mega-menu mono-suffix drift.** Section renamed in one page's nav, not in others. LOW per page, HIGH if new name and old name both circulate.

---

## 5. Scoring weights & pass thresholds

Restated from SKILL.md for convenience:

| Dimension | Weight | Threshold |
|---|---|---|
| Source Traceability | 25% | 75 |
| Tone of Voice | 20% | 80 |
| Honesty Register | 20% | 80 |
| Structural Compliance | 15% | 85 |
| Visual Completeness | 10% | 85 |
| Cross-Page Consistency | 10% | 70 |

Overall pass: **75/100**.

A page can pass overall while failing one dimension; flag this in the summary. A page that fails Source Traceability or Honesty Register cannot pass overall regardless of other dimensions — those are the two non-negotiables for an Apex register.

---

## 6. Mechanical sweep checks (universal · all tiers)

These are grep-based hygiene checks. Every audit runs all of them regardless of page tier — they're tone / typography / CSS-hygiene rules that don't care whether the page is a platform story, a methodology page, or an interactive directory. Codified after the 03-May-2026 master audit found these recurring across 30 pages.

### 6.1 · Em-dash count

**Check.** Body copy must have zero `—` (U+2014). The em-dash sneaks in via paste-from-deck and Markdown autoformatters; over time pages drift to dozens.

**Run.**
```bash
grep -c '—' <page>/index.html
```

**Severity.** Any count > 0 is **MEDIUM** (mechanical to fix). Counts ≥10 are **HIGH** (suggests systemic drift, not isolated lapse).

**Fix recipe.** Replace `—` per context:
- List intros · `→` `:` (e.g., "Three threads — A, B, C" → "Three threads: A, B, C")
- Continuations · `→` `.` (split into two sentences)
- Parentheticals · `→` `(...)` (e.g., "X — the Y of Z — does W" → "X (the Y of Z) does W")
- Cell separators in cap-num / inline copy · `→` `·` (Indian middle dot, the register's preferred separator)

### 6.2 · §0 → §01 contiguity bug

**Check.** Section labels must start at `§01`, never `§0`. Pages authored before the convention solidified often start at `§0 Hero` and number outward; the JCP master uses `§0 Hero` (untitled) followed by `§01 Bet`, but many sibling pages drifted to `§0 Status / §1 Live / §2 Architecture` (no leading zero, started at zero, or both).

**Run.**
```bash
grep -n 'section-label mb-3">[0-9]' <page>/index.html | head -3
```

**Severity.** First label is `§0` (instead of `§01` or absent) → **MEDIUM** (mechanical bump). Numbering gap (§01 §02 §04) → **MEDIUM** (per §1 contiguity rule). On a Tier A page, repeated §0 bug is **HIGH** because it's part of the JCP parity matrix.

**Fix recipe.** Bump every section label by one and update TOC anchors to match. The hero section can stay un-numbered (no `<div class="section-label">` at all) or be `§0` reserved for hero — both are acceptable; what's not acceptable is content sections starting at `§0`.

### 6.3 · Banned constructions (not just banned words)

**Check.** The tone-of-voice ruleset bans specific phrasings. Already covered in `website-tone-of-voice.md` §3 — restated here as a grep-able sweep:

```bash
grep -inE 'this is not [a-z]+\.\s*it is|in summary|strong interest in|has shifted the mindset|comprehensive (audit|security|view)|full-body picture' <page>/index.html
```

**Severity.** **HIGH** (these are reading red flags; one instance changes Apex's read of the page).

**Fix recipe.** Restructure the offending sentence. "This is not X. It is Y." → "Y." (lead with the affirmative); parallel-list constructions → break into separate sentences with concrete subjects.

### 6.4 · Banned words beyond the existing list

The 03-May-2026 master audit surfaced two banned-word violations not previously enumerated:

- `Comprehensive` (hirefirst) — a hedge word for "we listed a lot of things and want credit for thoroughness". Replace with a specific list or drop entirely.
- `picture` as a visual metaphor (fynd-horizon · "Full-body picture for the customer profile") — tech jargon dressed up as natural language. Replace with `image` (literal), `capture` (act of recording), or restructure.

**Run.** Augment the existing `website-tone-of-voice.md` §7 grep with `\bComprehensive\b` and `\bpicture\b` (the latter requires manual scan — `picture` has legitimate uses for actual photos).

**Severity.** **HIGH** for `Comprehensive`. **MEDIUM** for `picture` (false positives possible — confirm context).

### 6.5 · `we / our` voice violations

**Check.** Per `website-tone-of-voice.md`, the page itself is the artefact — never `we` or `our`. The 03-May-2026 audit found violations in `autri/` (multiple) and `tms/` (1).

**Run.**
```bash
grep -inwE 'we|our|us|let us' <page>/index.html | grep -v '<!--' | grep -v 'noscript\|website-tone'
```

**Severity.** **HIGH** in body copy. **MEDIUM** if buried in a section subhead (still wrong, less prominent).

**Fix recipe.** Rewrite to page-itself voice. *"How we design against it"* → *"How the platform handles it"* / *"The design response"*.

### 6.6 · Exclamation marks in body copy

**Check.** Banned per `website-tone-of-voice.md`. Master audit found counts ≥5 on home, fynd-academy, kaily, kio, ratl, tms, frameworks.

**Run.**
```bash
grep -nE '!(?!important|=|DOCTYPE|--)' <page>/index.html | head -20
```

(Filter out CSS `!important`, JS `!=`, HTML `!DOCTYPE`, comment `<!--`. Manual scan still recommended.)

**Severity.** **HIGH** if any in hero / above-the-fold. **MEDIUM** elsewhere in body copy.

**Fix recipe.** Drop the exclamation mark. The rule of thumb: if removing the `!` makes the sentence feel wrong, the underlying claim was overclaiming, not the punctuation.

### 6.7 · Arrow operator (`→`) noise in body prose

**Check.** Excessive `→` in narrative text reads as developer-flowchart spilling into prose. Acceptable in flow diagrams (arch SVGs, SENSE → PLAN → SOURCE chains, build-plan workstreams). Not acceptable in body sentences.

**Run.**
```bash
grep -c '→' <page>/index.html
```

Then visually classify: how many are inside `<svg>` / diagram blocks vs in `<p>` / prose? Master audit found prose-arrow noise on `retail-jarvis/` (31), `retail-vista/` (22), `samarth/` (20), `forge/` (19).

**Severity.** Body-prose count >10 → **MEDIUM**. Diagram-only counts → not a finding.

**Fix recipe.** In prose, replace with `:` (intro), `then` (sequence), or `·` (separator).

### 6.8 · Inline style density

**Check.** Repeated `style="color: var(--ink);"` on titles, eyebrows, and section headings indicates a CSS class is missing from `style.css`. Master audit measured 134 inline styles on `hirefirst/` and `rcpl/` each.

**Run.**
```bash
grep -c 'style="' <page>/index.html
```

**Severity.** **LOW** per page (no functional break) but **MEDIUM** at the system level (the same per-page weight × N pages = compounding cleanup debt). Per-page threshold: count ≥50 = report as MEDIUM cleanup target with a note to promote the repeated declaration to a `style.css` class.

### 6.9 · Raw hex literals on page

**Check.** Per `docs/design.md` §1.1 — every color must come from a `var(--*)` token. Direct `#RRGGBB` on the page is a violation.

**Run.**
```bash
grep -nE '#[0-9a-fA-F]{6}\b' <page>/index.html
```

**Severity.** **MEDIUM** per occurrence. **HIGH** if the same non-token hex repeats >5 times (likely a missing token in `style.css :root`).

**Fix recipe.** Look up the closest token in `style.css :root` and replace. If no token matches, propose adding one to `:root` rather than hardcoding the hex on the page.

### 6.10 · Hero subhead word count

**Check.** Per CLAUDE.md and the JCP parity matrix — hero subhead must be ≤30 words.

**Run.**
```bash
# Manual: grep the hero <p>, count words
grep -A2 '<h1' <page>/index.html | head -10
```

**Severity.** **MEDIUM** if 31-40 words. **HIGH** if >40 words (samarth had 64). Zero words (no subhead) on a Tier A page is **HIGH** per JCP parity matrix §1B.

**Fix recipe.** Compress. Reading test: if you can't say it aloud in one breath, it's too long.

---

## 7. Multi-page synthesis report (register-wide audit mode)

When auditing >5 pages at once (a wave-fix verification, a tier-A baseline scan, a pre-deploy hygiene sweep), produce a markdown synthesis report instead of N individual JSONs. Format codified by `docs/audits/MASTER-AUDIT-2026-05-03.md`:

```
1. SCORE TABLE · ranked worst → best
   - Columns: # · Page · Score · Em-dashes · Sticky TOC · Top blocker
   - Rows sorted by score ascending
   - Mean score at bottom; pass-rate (count above 75)

2. CROSS-CUTTING SYSTEMIC ISSUES (numbered)
   - Issue · description · worst-offender list (top 6-8 pages with counts)
   - Fix recipe (one-line, mechanical)

3. JCP PARITY MATRIX · Tier 1 platform pages
   - Binary checkmark grid: Page × 8 parity checks
   - Legend: ✓ matches JCP · ✗ missing or broken · ⚠ present but out of spec · partial = some

4. RECOMMENDED FIX ORDER (waves)
   - Wave 1 · mechanical sweeps (1 day)
   - Wave 2 · structural sweeps (2-3 days)
   - Wave 3 · per-page structural lift (1-2 weeks)
   - Each wave: ordered task list with effort estimates

5. WHAT TO LEAVE ALONE (for now)
   - JCP itself (master template)
   - Excluded set (impetus, granary, ucp, agents, ai-native)
   - Reference pages with different rubric (organisation/directory, organisation/organogram, docs)

6. SUGGESTED BRANCHING PLAN
   - Per the always-from-master rule
   - One branch per wave; per-page or per-tier branching for Wave 3

7. VERIFICATION CHECKLIST · pre-push (every branch)
   - inject_present.py --check
   - inject_chrome.py --check
   - inject_path_to_l4.py --check
   - Plus content sweeps relevant to the branch's scope

8. AUDIT METADATA
   - Date · auditor · pages audited · pass threshold · pages cleared · master template ref · reference rules
```

Output path: `docs/audits/MASTER-AUDIT-<YYYY-MM-DD>.md`. Also produce a `MASTER-CHANGELOG-<YYYY-MM-DD>.md` (per `docs/audits/MASTER-CHANGELOG-2026-05-03.md`) when the audit closes a wave — annotate the per-page outcomes from that wave.
