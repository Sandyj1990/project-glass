# Master audit · 30 pages vs JCP gold standard · 03-May-2026

JCP (`/jcp/`) is the reference template after PR #46. This audit covers every page on the register **except** JCP, Impetus, Granary, UCP, and AI Agents.

**Headline:** every audited page scores below the 75 pass threshold. The gap splits into two layers · the 8 Tier-1 platform pages got the PR #46 sticky-TOC + em-dash sweep but never picked up the full 11-section JCP shape (no Receipts grid, no People bar chart, contiguity bug at §0). The other 22 pages are still pre-JCP-template · no sticky TOC, no scrollspy, em-dashes everywhere, banned tone constructions, raw tables instead of lens cards.

---

## Score table · ranked worst → best

| # | Page | Score | Em-dashes | Sticky TOC | Top blocker |
|---|---|---|---|---|---|
| 1 | `fynd-konnect/` | 35 | **42** | No | Catastrophic em-dash density · raw tables · no JCP frame |
| 2 | `autri/` | 38 | 12 | No | 12 em-dashes · we/our voice · no sticky TOC |
| 3 | `pixelbin/videos/` | 41 | 2 | No | No JCP shape at all · video gallery only |
| 4 | `boltic/` | 47 | 8 | No | No hero subhead · raw table architecture |
| 5 | `samarth/` | 48 | 0 | Yes | 64-word subhead · 4 of 11 sections only |
| 6 | `pixelbin/glamar/` | 52 | 2 | No | No hero subhead · 6 module cards as raw grid |
| 7 | `forge/` | 55 | 0 | Yes | No roadmap · 5 of 11 sections · §0 bug |
| 8 | `dark-factory/` | 55 | 5 | No | No subhead KPI tiles · status pills slash-formatted |
| 9 | `fynd-horizon/` | 58 | 9 | No | 9 em-dashes · banned word "picture" |
| 10 | `frameworks/` | 58 | 17 | No | 17 em-dashes · 11 raw hex colours |
| 11 | `pixelbin/` | 58 | 2 | No | Missing 6 of 11 sections · no smart narrative |
| 12 | `retail-jarvis/` | 60 | 0 | Yes | 31 arrow operators · §0 bug · no roadmap |
| 13 | `fynd-academy/` | 62 | 1 | No | No sticky TOC · 15 exclamations · raw module rows |
| 14 | `kaily/` | 64 | 3 | No | No sticky TOC · 13 exclamations |
| 15 | `alp/` | 65 | 0 | Yes | §0 bug · no hero subhead · 5 sections only |
| 16 | `docs/` | 65 | 1 | No | 44 inline styles · no section structure |
| 17 | `tms/` | 65 | 9 | No | 9 em-dashes · we/our voice · no sticky TOC |
| 18 | `ratl/` | 66 | 5 | No | No sticky TOC · 12 exclamations |
| 19 | `organisation/organogram/` | 66 | 4 | N/A | 4 em-dashes · avatar onerror hack |
| 20 | `kio/` | 68 | 2 | No | No sticky TOC · 9 exclamations · no KPI hero |
| 21 | `retail-vista/` | 68 | 0 | Yes | §0 bug · no hero subhead · 22 arrow operators |
| 22 | `swapeasy/` | 68 | 0 | Yes | §0 bug · "This is not X. It is Y." construction · no subhead |
| 23 | `index.html` (home) | 68 | 14 | No | 14 em-dashes · no section IDs · 56 inline styles |
| 24 | `organisation/` | 70 | 15 | No | 15 em-dashes · no section IDs · 32 inline styles |
| 25 | `organisation/external/` | 70 | 4 | No | 40 inline styles · no section IDs |
| 26 | `hirefirst/` | 70 | 0 | Yes | §05 numbering gap · banned word "Comprehensive" · 134 inline styles |
| 27 | `autonomous/` | 71 | 0 | No | No sticky TOC · workflow table not lens cards |
| 28 | `culture/` | 72 | 0 | No | 4 raw hex colours · 34 inline styles · no IDs |
| 29 | `organisation/directory/` | 72 | 8 | N/A | 8 em-dashes · 18 inline styles |
| 30 | `rcpl/` | 72 | 0 | Yes | Missing 5 of 11 sections · no Receipts grid · no People bar |

Mean score: **62/100** · all 30 pages below pass threshold · zero pages match JCP shape end-to-end.

---

## Cross-cutting systemic issues

### 1 · Em-dashes still in body copy on 22 pages
Total em-dashes across the audited set: **~155**. Tier 1 platform pages were swept clean by PR #46 (all 8 read 0). Everything else still drifts.

Worst offenders:
- `fynd-konnect/` · 42
- `frameworks/` · 17
- `index.html` (home) · 14
- `autri/` · 12
- `tms/` · 9
- `fynd-horizon/` · 9
- `boltic/` · 8
- `organisation/directory/` · 8

Fix recipe is mechanical: replace `—` with `:` (list intros), `.` (continuations), `(...)` (parentheticals), or `·` (cell separators). 30-min task per heavy page.

### 2 · Sticky TOC + scrollspy missing on 22 pages
PR #46 rolled the `.story-toc` + IntersectionObserver pattern to 8 platform pages only. Every other page has zero scrollspy.

Pages missing the pattern: `fynd-konnect`, `autri`, `pixelbin/*`, `boltic`, `dark-factory`, `fynd-horizon`, `frameworks`, `fynd-academy`, `kaily`, `kio`, `ratl`, `tms`, `autonomous`, `culture`, `docs`, `index` (home), `organisation/*`.

Fix recipe: copy the JCP `.story-toc` block + IntersectionObserver JS verbatim, then add `id="..."` to each page's existing sections. ~30 min per page if section IDs exist, ~1 hr if they need to be authored.

### 3 · §0 numbering contiguity bug on 7 of 8 Tier 1 platform pages
`alp`, `retail-vista`, `retail-jarvis`, `forge`, `samarth`, `swapeasy` (and partly hirefirst with §05 gap) all start the section numbering at `§0` rather than `§01`. RCPL is the only Tier 1 page that gets this right. Quick mechanical fix.

### 4 · 11-section JCP shape missing across the board
JCP's full pattern: `bet · scale · coverage · people · architecture · properties · ai · path-to-l4 · shipped · roadmap · receipts`. None of the 30 audited pages match it.

Most consistent gaps:
- **Receipts grid** · 30 of 30 pages (only JCP has it)
- **People bar chart** · 30 of 30 pages (only JCP has it)
- **path-to-l4 section** · 27 of 30 pages
- **shipped section** · ~25 of 30 pages

Note · not every page needs all 11 sections. The home page, organisation pages, and some specialty pages (culture, docs, frameworks) need a different shape. The JCP gold standard applies most directly to platform/product pages: `rcpl, alp, retail-vista, retail-jarvis, forge, hirefirst, swapeasy, samarth, pixelbin, autri, boltic, autonomous, dark-factory, fynd-horizon, fynd-konnect, kaily, kio, ratl, tms, fynd-academy`. That's **20 platform pages** that should aim for the full shape.

### 5 · Banned vocabulary and constructions slip through
Confirmed in the actual files:
- `hirefirst/` · `Comprehensive audit logs · real-time security alerts` (banned word "Comprehensive" + parallel-list construction)
- `fynd-horizon/` · `Full-body picture for the customer profile` (banned word "picture")
- `swapeasy/` · `SwapEasy's destination is not a feature ... It is the re-commerce operating system` (banned construction "This is not X. It is Y.")
- `autri/` · we/our voice violations in body copy and section headers (`How we design against it`, `we need to`, `allows us to`)
- `tms/` · 1 we/our pronoun

### 6 · Inline style density (260+ violations)
High-density pages: `hirefirst/` 134, `rcpl/` 134, `retail-vista/` 129, `forge/` 107, `alp/` 75, `swapeasy/` 72, `samarth/` 65. The pattern is mostly `style="color: var(--ink);"` repeated on titles/eyebrows · should be a CSS class. Lower-priority cleanup but a substantial cumulative footprint.

### 7 · Raw hex literals (28+ violations outside JCP)
`frameworks/` 11 · `docs/` 10 · `culture/` 4 · scattered ones across `fynd-konnect`, `retail-vista`, `forge`, `index`, `organisation/external`. JCP itself still carries 88 (the `Architecture SVG colour token sweep` open item from the session context). Token sweep is its own commit per design.md §1.1.

### 8 · Arrow operator (`→`) noise on Tier 1 pages
Excessive use clutters prose. Worst: `retail-jarvis/` 31 · `retail-vista/` 22 · `samarth/` 20 · `forge/` 19. Acceptable in flow diagrams; not in body sentences. ~10–15 min cleanup per page.

---

## JCP parity matrix · Tier 1 platform pages

| Page | Sticky TOC | Hero subhead | KPI tiles | Lens cards | Receipts | People bar | §nn contiguous | Em=0 |
|---|---|---|---|---|---|---|---|---|
| jcp | ✓ | ✓ (≤30w) | ✓ (4) | ✓ | ✓ | ✓ | ✓ | ✓ |
| rcpl | ✓ | ✓ | ✓ | partial | ✗ | ✗ | ✓ | ✓ |
| alp | ✓ | ✗ (0w) | ✓ | partial | ✗ | ✗ | ✗ (§0) | ✓ |
| retail-vista | ✓ | ✗ (0w) | ✓ | partial | ✗ | ✗ | ✗ (§0) | ✓ |
| retail-jarvis | ✓ | ✗ (0w) | ✓ | partial | ✗ | ✗ | ✗ (§0) | ✓ |
| forge | ✓ | ✗ (0w) | ✓ | partial | ✗ | ✗ | ✗ (§0) | ✓ |
| hirefirst | ✓ | ⚠ (31w) | ✓ | partial | ✗ | ✗ | ✗ (§05 gap) | ✓ |
| swapeasy | ✓ | ✗ (0w) | ✓ | partial | ✗ | ✗ | ✗ (§0) | ✓ |
| samarth | ✓ | ✗ (64w) | ✓ | partial | ✗ | ✗ | ✗ (§0) | ✓ |

Legend · ✓ = matches JCP · ✗ = missing or broken · ⚠ = present but out of spec · partial = some lens cards but not the full smart-narrative pattern.

---

## Recommended fix order

The work splits cleanly into three waves. Each wave is a separate branch off master.

### Wave 1 · Fast mechanical sweeps · 1 day
Single-script-able fixes that lift every page closer to baseline.

1. **Em-dash sweep on 22 pages** (~3 hrs)
   - Replace `—` with `:`, `.`, `(...)`, or `·` per context
   - Highest density first: fynd-konnect, frameworks, home, autri, tms, fynd-horizon

2. **§0 → §01 contiguity fix on 7 platform pages** (~30 min)
   - alp, retail-vista, retail-jarvis, forge, samarth, swapeasy (and §05 gap on hirefirst)
   - Mechanical: bump section labels and toc anchors

3. **Banned vocabulary fixes** (~30 min)
   - "Comprehensive" → "Audit logs · real-time security alerts" (hirefirst)
   - "picture" → "image" or "capture" (fynd-horizon)
   - "This is not X. It is Y" → restructure (swapeasy)
   - we/our → page-itself voice (autri, tms)

4. **Exclamation mark sweep** (~1 hr)
   - Body-copy exclamation marks across home, fynd-academy, fynd-horizon, fynd-konnect, kaily, kio, ratl, tms, frameworks
   - Verify HTML/JS/CSS `!` usages are not body-copy

5. **Hero subhead authoring on Tier 1 pages** (~2 hrs)
   - alp, retail-vista, retail-jarvis, forge, swapeasy: write a ≤30-word subhead each
   - samarth: collapse 64w → ≤30w
   - hirefirst: trim 31w → ≤30w

**Wave 1 deliverable** · zero em-dashes on 30 pages, zero §0 errors, zero banned vocabulary, zero exclamation marks in body copy, every Tier 1 page has a compliant hero subhead.

### Wave 2 · Sticky TOC rollout to 22 pages · 2–3 days
Copy the JCP `.story-toc` + IntersectionObserver pattern to every page that doesn't have it. Effort scales with whether section IDs already exist.

Order by impact:
1. **High-traffic platform pages first** · pixelbin, boltic, dark-factory, fynd-horizon, fynd-academy, fynd-konnect, kaily, kio, ratl, tms, autri, autonomous (~30–60 min each)
2. **Home + organisation pages** · index.html, organisation/, organisation/external/ (longer pages, may need section ID authoring · 60–90 min each)
3. **Specialty pages** · culture, docs, frameworks (~45 min each)

Skip · `organisation/directory/` and `organisation/organogram/` (reference/interactive pages that don't need TOC).

**Wave 2 deliverable** · 28 of 30 pages carry sticky TOC + scrollspy.

### Wave 3 · Structural lift · 1–2 weeks
Bring 20 platform pages to full JCP shape (Receipts grid, People bar chart pattern, smart-narrative lens cards, path-to-l4).

Order by current score (lowest first, biggest lift):
1. `fynd-konnect` · 35 → target 80 · table-to-lens-cards rewrite + KPI hero + Receipts/People (~12 hrs)
2. `autri` · 38 → target 80 · em-dash + voice rewrite + lens cards + arch diagram (~8 hrs)
3. `pixelbin/videos` · 41 → reframe as JCP page or accept as gallery (~6 hrs)
4. `boltic` · 47 → 80 · KPI hero + lens cards + case study expansion (~6 hrs)
5. `samarth` · 48 → 80 · expand from 4 to 8+ sections (~6 hrs)
6. `pixelbin/glamar` · 52 → 80 · hero + 6-module lens cards (~5 hrs)
7. `forge` · 55 → 80 · add roadmap + receipts + path-to-l4 (~5 hrs)
8. `dark-factory` · 55 → 80 · hero KPIs + status pill cleanup + lens cards (~5 hrs)
9. `fynd-horizon` · 58 → 80 · em-dash + lens cards (~4 hrs)
10. Continue down the list to RCPL (72) which only needs Receipts + People + 5 missing sections.

**Wave 3 deliverable** · all 20 platform pages match JCP's 11-section shape with smart-narrative lens cards.

---

## What to leave alone (for now)

- **JCP itself** · master template, only open item is the SVG hex token sweep (separate commit, design.md §1.1)
- **Excluded per user** · jcp/*, impetus/*, granary/, ucp/, agents/*, ai-native/
- **Reference pages** that don't need full JCP shape · organisation/directory, organisation/organogram, docs (these are interactive/index surfaces)

---

## Suggested branching plan

Per the branching rule (always from master):

```
master
├── feat/jcp-parity-wave1-mechanical-sweeps     · em-dash + §0 + banned words + exclamations + hero subheads
│
├── feat/jcp-parity-wave2-sticky-toc-rollout    · 22 pages get sticky TOC + scrollspy
│
└── feat/jcp-parity-wave3-{page}                · per-page structural lift, one branch per page or grouped
```

Push wave 1 first as a single PR (low-risk mechanical sweep). Wave 2 as a single PR (visible UX upgrade across the register). Wave 3 broken into per-page or per-tier PRs for review velocity.

---

## Verification checklist · pre-push (every branch)

```
cd /Users/salmansaudagar/reliance-retail-fynd
python3 tools/inject_present.py --check && \
python3 tools/inject_chrome.py --check && \
python3 tools/inject_path_to_l4.py --check
```

Plus for content-quality sweeps:
- `grep -rn "—" *.html jcp/ rcpl/ ...` to confirm em-dash zero across the affected pages
- Spot-check sticky TOC: open `http://localhost:8765/<route>/` and scroll to confirm scrollspy active states fire

---

## Audit metadata

- Date · 03-May-2026
- Auditors · 4 parallel Explore agents · final synthesis by orchestrator
- Pages audited · 30 (excludes jcp, impetus/*, granary, ucp, agents/*, ai-native)
- Pass threshold · 75/100 · 0 pages cleared
- Master template · `jcp/index.html` · 11 sections, sticky TOC + scrollspy, 4-tile KPI hero, smart-narrative lens cards, Receipts grid, People bar chart, zero em-dashes
- Reference rules · `.claude/skills/website-tone-of-voice.md` · `.claude/skills/website-page-reviewer/SKILL.md` · `docs/design.md`
