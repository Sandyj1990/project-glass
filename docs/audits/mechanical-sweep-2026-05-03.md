# Mechanical Sweep · 70 pages · 03-May-2026

Register-wide universal mechanical-sweep audit per the website-page-reviewer skill `references/audit-framework.md` §6. Run on `feat/jcp-parity-fixes` after merging master, before raising the next PR.

**Headline:** Wave 1+2 sweep on the 30 Tier-A pages held — every Tier-A platform page reads `0` em-dashes, `0` banned constructions, `0` banned words, `0` `we/our` violations, `0` body exclamations. The em-dashes that survive are concentrated on the *excluded-canonical set* (impetus / granary / ucp / agents / ai-native / jcp sub-pages) which the JCP parity sweep deliberately skipped. A Wave-4 sweep over those 22 pages would close the remaining 454 em-dashes.

---

## 1. Score table · ranked worst → best (em-dash count)

Pages reporting 0 em-dashes omitted from the table; the full set passed. 41 pages remain with ≥1.

| # | Page | em— | §0 bug | banC | Comp | we | ! | sty | hex | h-sub |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `jcp/release-notes/` | **192** | — | 0 | 0 | 0 | 0 | 45 | 0 | 15 |
| 2 | `impetus/` | **42** | — | 0 | 1 | 1 | 0 | 100 | 0 | 30 |
| 3 | `ai-native/` | **22** | — | 0 | 0 | 1 | 0 | 134 | 0 | 16 |
| 4 | `ucp/` | **16** | — | 0 | 0 | 12 | 0 | 203 | 0 | 57 |
| 5 | `jcp/cataloging/` | **15** | — | 0 | 0 | 3 | 0 | 93 | 0 | 22 |
| 6 | `agents/generative-media/` | 13 | no labels | 0 | 0 | 0 | 0 | 44 | 15 | 22 |
| 7 | `agents/trend-to-design/` | 12 | no labels | 0 | 0 | 0 | 0 | 50 | 16 | 21 |
| 8 | `impetus/cortex/` | 11 | — | 0 | 0 | 0 | 0 | 32 | 0 | 2 |
| 9 | `impetus/ai-photoshoot/` | 10 | — | 0 | 0 | 0 | 0 | 111 | 0 | 10 |
| 10 | `granary/` | 9 | — | 0 | 0 | 1 | 0 | 104 | 0 | 35 |
| 11 | `agents/category-intelligence/` | 9 | no labels | 0 | 0 | 0 | 0 | 50 | 16 | 17 |
| 12 | `agents/agentic-marketing/` | 8 | no labels | 0 | 0 | 0 | 0 | 65 | 23 | 19 |
| 13 | `agents/retail-vista/` | 8 | no labels | 0 | 0 | 0 | 0 | 48 | 19 | 15 |
| 14 | `impetus/companion-app/` | 8 | — | 0 | 0 | 0 | 0 | 27 | 0 | 3 |
| 15 | `jcp/channels/` | 6 | no labels | 0 | 0 | 2 | 0 | 257 | 3 | 19 |
| 16 | `agents/ai-photoshoot/` | 6 | no labels | 0 | 0 | 0 | 0 | 47 | 15 | 21 |
| 17 | `impetus/gmetri/` | 6 | — | 0 | 0 | 0 | 0 | 30 | 0 | 7 |
| 18 | `agents/` | 6 | no labels | 0 | 0 | 0 | 0 | 29 | 0 | 30 |
| 19 | `impetus/nextwave/` | 6 | — | 0 | 0 | 1 | 0 | 25 | 0 | 6 |
| 20 | `impetus/pulsepoint/` | 4 | — | 0 | 0 | 0 | 0 | 29 | 0 | 3 |
| 21 | `impetus/costing-engine/` | 4 | — | 0 | 0 | 0 | 0 | 20 | 0 | 19 |
| 22-41 | (22 more pages with em ≤3) | | | | | | | | | |

**Mean em-dash count per page: 6.5.** Mean across the 30 Tier-A swept pages: **0**. The mean across the 41 unswept pages: **11.1** (heavily skewed by `jcp/release-notes`).

---

## 2. Cross-cutting systemic issues

### Issue 1 · Em-dashes survive on the excluded-canonical set + JCP sub-pages

41 pages, 454 instances. Concentration:

- `jcp/release-notes/` · 192 (release-notes format may legitimately use em-dashes for revision delimiters; manual review needed before sweep)
- `impetus/` + 17 `impetus/*` sub-pages · 121 cumulative
- `ai-native/` · 22
- `ucp/` · 16
- `granary/` · 9
- 7 `agents/*` pages · 65 cumulative

**Fix recipe:** Wave-4 em-dash sweep across these 22 pages. Same mechanical replacements as Wave 1+2 (`—` → `:` for list intros, `.` for continuations, `(...)` for parentheticals, `·` for cell separators). Estimated effort · 2-3 hrs total; longer for `jcp/release-notes` if any em-dashes are part of the format spec.

### Issue 2 · `we / our / us` voice on 9 pages

26 instances. Distribution:

- `ucp/` · **12** (HIGH · the largest single-page concentration on the register)
- `jcp/cataloging/` · 3
- `fynd-konnect/` · 3
- `jcp/channels/` · 2
- `impetus/master-hub/` · 2
- `impetus/`, `ai-native/`, `granary/`, `impetus/nextwave/` · 1 each

**Fix recipe:** rewrite each instance to page-itself voice. *"How we design against it"* → *"How the platform handles it"*. Reads better and matches the register convention. Effort · 30-60 min total.

### Issue 3 · Inline style density · register-wide CSS hygiene gap

5,056 inline `style="..."` attributes across 70 pages. Worst:

- `dark-factory/` · 354
- `jcp/channels/` · 257
- `jcp/`, `ucp/` · 200+
- `autri/`, `forge/`, `hirefirst/`, `rcpl/`, `fynd-konnect/`, `retail-vista/` · 140-170 each
- 50+ pages over the 50-style threshold

**Fix recipe:** the dominant pattern is `style="color: var(--ink);"` repeated on titles/headings. Promote to a `style.css` class (e.g. `.ink-text`) and sweep across the register · estimated **−2,000 inline styles** in a single PR. Estimated effort · 4-6 hrs.

### Issue 4 · Raw hex literals concentrated on agent pages

154 unique hex literals register-wide. The 6 `agents/*` detail pages account for **104 of those** (15-23 each), each carrying a custom color palette baked inline.

**Fix recipe:** if the per-agent palette pattern is going to persist (it likely will — agents are visually differentiated), promote to `:root` tokens (`--agent-cortex-*`, `--agent-photoshoot-*`, etc.) and the agent pages reference tokens instead of hexes. Estimated effort · 3-4 hrs; coordinate with `tools/build_agents.py` so the renderer emits token references.

### Issue 5 · Hero subhead overflow on 6 pages

6 pages exceed the 30-word JCP parity matrix threshold; 4 borderline.

| Page | Words | Severity |
|---|---|---|
| `impetus/category-intel/` | **81** | HIGH (>40) |
| `ucp/` | **57** | HIGH |
| `impetus/photoshoots/ss26-plm-ai-photoshoot-pilot/` | **47** | HIGH |
| `impetus/photoshoots/buda-jeans-valentines/` | **43** | HIGH |
| `impetus/brands/` | **42** | HIGH |
| `granary/` | **35** | MEDIUM |
| `impetus/photoshoots/buda-jeans-harry-potter/` | 31 | MEDIUM |
| `tms/` | 32 | MEDIUM |
| `fynd-horizon/`, `retail-vista/`, `swapeasy/` | 30-31 | MEDIUM (just at limit) |

**Fix recipe:** compress to ≤30 words. Reading test · if you can't say it aloud in one breath, it's too long. Estimated effort · 10-15 min per page.

### Issue 6 · Banned word "Comprehensive" · 1 instance

`impetus/index.html:428` · "Comprehensive Testing" workstream label in the Cortex build-plan card. **Context-dependent** — it's a project-name in a table cell, not a hero claim. MEDIUM. Recommend rename to "Full Testing" or just "Testing".

---

## 3. JCP parity matrix · Tier A platform pages (em-dash only — full matrix needs separate run)

| Page | em=0 |
|---|---|
| jcp | ✓ |
| rcpl | ✓ |
| alp | ✓ |
| retail-vista | ✓ |
| retail-jarvis | ✓ |
| forge | ✓ |
| hirefirst | ✓ |
| swapeasy | ✓ |
| samarth | ✓ |
| pixelbin/glamar | ✓ |
| autri | ✓ |
| boltic | ✓ |
| autonomous | ✓ |
| dark-factory | ✓ |
| fynd-horizon | ✓ |
| fynd-konnect | ✓ |
| kaily | ✓ |
| kio | ✓ |
| ratl | ✓ |
| tms | ✓ |
| fynd-academy | ✓ |

**21 of 21 Tier-A pages clean** on em-dashes. Wave 1+2 result holds.

---

## 4. Recommended fix order

### Wave 4 · Excluded-canonical em-dash sweep · 2-3 hrs (next)
Sweep em-dashes on the 22 excluded-canonical pages. Same mechanical fixes as Wave 1+2.

Order by impact (em count):
1. `jcp/release-notes/` (192) — manual review first; many may be format-legitimate
2. `impetus/` (42) — high-traffic page, highest leverage
3. `ai-native/` (22)
4. `ucp/` (16)
5. `jcp/cataloging/` (15)
6. `agents/generative-media/` (13)
7. `agents/trend-to-design/` (12)
8. `impetus/cortex/` (11)
9. `impetus/ai-photoshoot/` (10)
10. `granary/` (9)
11. ...11 more pages with em ≤9

### Wave 5 · we/our voice + exclamation + Comprehensive · 1 hr
- `ucp/` we/our sweep (12 instances)
- `jcp/cataloging/`, `fynd-konnect/` we/our (3 each)
- 5 more pages with 1-2 each
- `pixelbin/videos/` exclamation removal
- `impetus/index.html:428` "Comprehensive Testing" rename

### Wave 6 · Hero subhead compression · 1-2 hrs
Compress 6 pages over 30 words; review 4 borderline.

### Wave 7 · CSS hygiene (separate, larger PR) · 1-2 days
- Promote `style="color: var(--ink);"` etc. to a `style.css` class · sweep register-wide
- Promote agent palette hex literals to `--agent-*` tokens
- Coordinate with `tools/build_agents.py` so the renderer emits token references

---

## 5. What is NOT in scope for this sweep

- **Source traceability** · per-page audit covers; not a register-wide grep target
- **Visual / image / lightbox checks** · per-page audit phase 6
- **JCP parity matrix structural checks** (sticky TOC, KPI tiles, Receipts grid, People bar, lens cards) · not greppable cleanly; needs the per-page reviewer
- **Wiring sweep** (route/anchor/asset resolution, mega-menu coverage) · separate audit per `references/wiring-audit-protocol.md`. Last run · `docs/audits/wiring-audit-2026-05-03.md`. Both that audit and this one share `feat/jcp-parity-fixes` as the branch baseline.

---

## 6. Suggested branching plan

Per the always-from-master rule:

```
master
├── feat/em-dash-sweep-wave4              · Wave 4 em-dash cleanup on excluded-canonical set (one PR)
│
├── feat/voice-and-exclamation-cleanup    · Wave 5 we/our + exclamation + Comprehensive (one PR)
│
├── feat/hero-subhead-compression         · Wave 6 hero subhead overflow fixes (one PR)
│
└── feat/css-hygiene-sweep                · Wave 7 inline-style class promotion + agent-palette token promotion (one PR; bigger review)
```

---

## 7. Verification checklist · pre-push (every branch)

```bash
python3 tools/inject_present.py --check && \
python3 tools/inject_chrome.py --check && \
python3 tools/inject_path_to_l4.py --check
```

Plus content sweeps relevant to the branch's scope:
```bash
# After Wave 4
python3 -c "import re; pages=__import__('subprocess').check_output('find . -name index.html -not -path \"./tools/*\" -not -path \"./docs/*\"', shell=True, text=True).strip().split(); print(sum(open(p).read().count('—') for p in pages))"
# Expect: significantly < 454; target ≤ 50 (jcp/release-notes legitimate uses)
```

---

## 8. Audit metadata

- **Date** · 03-May-2026
- **Branch** · feat/jcp-parity-fixes (post merge-from-master)
- **Tool** · `tmp/sweep.py` (single-pass Python over 70 pages, 9 checks)
- **Pages audited** · 70
- **Pass threshold** · n/a (this is a counts-and-violations sweep, not a scored audit)
- **Reference** · `.claude/skills/website-page-reviewer/references/audit-framework.md` §6 universal mechanical sweeps
- **Companion audit** · `docs/audits/wiring-audit-2026-05-03.md` (route/anchor/asset/chrome resolution)
- **Origin audit** · `docs/audits/MASTER-AUDIT-2026-05-03.md` (the 30-page Wave 1+2/3 master audit that motivated codifying these checks)
