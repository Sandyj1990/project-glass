---
name: agent-diagram-standards
description: Visual + structural standards for hand-authored inline workflow SVGs on agent detail pages (`/agents/<slug>/`). Use when authoring a new agent's `workflow_svg` field in `data/agents/<slug>.yaml`, when fixing overlap / overflow / alignment issues on an existing diagram, or when sweeping consistency across the catalog. Pairs with `docs/agents-spec.md` (template) and `docs/design.md` (visual register). Establishes the 3-zone convention, viewBox contract, font-size scale, connector grid, padding rules, and a 12-point pre-publish checklist.
user_invocable: true
---

# Agent Diagram Standards · Fynd × Reliance Retail Register

The 7 active agent pages each carry a hand-authored inline SVG workflow diagram in `data/agents/<slug>.yaml` `workflow_svg:` field. They render via `tools/build_agents.py` `render_inline_svg()` into `agents/<slug>/index.html` §02. They are the load-bearing visual on every agent page — Apex reads them top-to-bottom in 5 seconds.

This skill captures the conventions every diagram should follow + the 7 issue patterns that surface across the catalog today + a 12-point pre-publish checklist + the per-agent fix list from the 2026-05-03 survey.

---

## 1. Why this skill exists

A 2026-05-03 visual audit of the 7 agent diagrams (cortex-planning · trend-to-design · category-intelligence · retail-vista · agentic-marketing · ai-photoshoot · generative-media) surfaced 14 specific issues across 4 categories:

- **viewBox inconsistency** · 5 diagrams use `1200×540`, 2 newer ones use `1240×620`. Two different aspect ratios across the same template.
- **Text overflow / truncation** · 4 diagrams have visible card-text overflow (Evidence Tags `FORECAST` clipped, Step 03 `... rates · ...` truncated, Meta-Orchestrator `rou...` cut, Step 02 `treatment` spillover).
- **Zone-header omission** · 5 older diagrams have no `INPUTS` / `WORKFLOW` / `OUTPUTS` zone headers; 2 newer ones do. A reader can't tell the bands apart at a glance on the older five.
- **Connector tangle** · several diagrams fan many connector lines from one band to another at sharp diagonals, crossing each other (worst on AI Photoshoot input → row-1 fan-out, also visible on Cortex inputs and Generative Media inputs).

Without standards, every new agent diagram restarts the same craft problems. With them, an author opens the spec, copies the canonical viewBox + zone block, and lands a clean diagram on the first try.

---

## 2. The canonical 3-zone architecture

Every agent workflow diagram is a **3-zone horizontal layout**:

```
┌────────────────────────────────────────────────────────────────────────┐
│ INPUTS               │ WORKFLOW · N stages           │ OUTPUTS         │
│ (left, blue)         │ (centre, grey)                │ (right, green)  │
│                      │                               │                 │
│ ─ Source 1 ─────────┐│  ┌── 01 ──┐  ┌── 02 ──┐ ...  │┌── Output 1 ──┐│
│ ─ Source 2 ─────────┼├──┤        │  │        │ ──────┤              ││
│ ─ Source 3 ─────────┘│  └────────┘  └────────┘      │└──────────────┘│
│                      │                               │                 │
└────────────────────────────────────────────────────────────────────────┘
   Inputs zone           Workflow zone (sub-bands)        Outputs zone
   width 220             width 740                        width 220
```

The reader's eye scans left → middle → right. The middle zone may have **sub-bands** (gates, loops, eval blocks) drawn as full-width rectangles inside the workflow column.

### Zone widths (canonical)

| Zone | Width | x position |
|---|---|---|
| Inputs | 220px | 14-234 |
| Workflow | 740px | 250-990 |
| Outputs | 220px | 1006-1226 |

Total viewBox width: **1240px**. Total height: **620px** (default). Height can stretch to 720px if a diagram needs more sub-bands; keep increments to 100px.

### Reference exemplar

`data/agents/ai-photoshoot.yaml` `workflow_svg:` field is the canonical reference for the 3-zone + sub-bands pattern. When in doubt, copy that structure and edit content.

---

## 3. Foundations · viewBox · font sizes · colours

### 3.1 viewBox contract

**Always:**
```svg
<svg viewBox="0 0 1240 620" xmlns="http://www.w3.org/2000/svg" role="img"
     preserveAspectRatio="xMidYMid meet"
     style="width:100%;height:auto;display:block;">
```

- viewBox is the canonical coordinate space. **1240×620 is the standard** (matches AI Photoshoot + Generative Media).
- `preserveAspectRatio="xMidYMid meet"` keeps the diagram centred when the wrapper changes width.
- `style="width:100%;height:auto;display:block;"` lets the diagram scale fluidly within `.diagram-wrap` (max-width inherited from the page).

### 3.2 Font-size scale (SVG-internal)

| Element | Font size | Family | Weight | Use |
|---|---|---|---|---|
| Zone header (`INPUTS · WORKFLOW · OUTPUTS`) | 11px | JetBrains Mono | 600 | Top of each zone, uppercase |
| Workflow step number (`01` `02` …) | 11px | JetBrains Mono | 700 | Top-left of each step card, accent colour |
| Step card title (`Brief intake`) | 12.5px | Inter | 600 | Below step number |
| Step card sub-text | 10.5px | Inter | 400 | Two-line body inside step card |
| Input / Output card title | 12px | Inter | 600 | Top of each side card |
| Input / Output card sub-text | 10.5px | Inter | 400 | One-to-two-line body |
| Sub-band label (gate / loop) | 10px | JetBrains Mono | 600 | Eyebrow on sub-band rectangles |
| Eval-gate footer body | 10.5px | Inter | 400 | Multi-line eval description |

These are the **only acceptable sizes** inside agent SVG diagrams. Pre-existing 11.5px and 12.5px sizes are tolerated for workflow titles (12.5 is on-spec); avoid any other off-scale value.

### 3.3 Colour palette (SVG-internal)

Per `docs/design.md` §1.1 the page-level rule is "no new hex literals". Inside SVG diagrams, decorative fills are exempted (whitelisted use). The agent-diagram palette:

| Role | Hex | Use |
|---|---|---|
| Inputs zone background | `#EFF6FF` | Pale blue band |
| Inputs zone border | `#BFDBFE` | Card stroke |
| Inputs card title | `#1E40AF` | `.src-ttl` |
| Inputs card sub-text | `#475569` | `.src-sub` |
| Workflow zone background | `#F8FAFC` | Pale grey band |
| Workflow zone border | `#E2E8F0` | Card stroke |
| Workflow step number | `#6B5BD6` | Accent (matches site `--accent`) |
| Workflow step title | `#0A0A0A` | Ink |
| Workflow step sub-text | `#6B7280` | Ink-muted |
| Outputs zone background | `#F0FDF4` | Pale green band |
| Outputs zone border | `#BBF7D0` | Card stroke |
| Outputs card title | `#14532D` | Dark green |
| Outputs card sub-text | `#166534` | Mid green |
| Gate / human-in-loop sub-band | `#FFF7ED` bg · `#FDBA74` border · `#B45309` label | Orange, signals brand-review checkpoints |
| Loop / retry connector | `#B45309` stroke `dasharray` | Orange dashed, matches gate band |
| Routing / fail-route arrow | `#9333EA` stroke `dasharray` | Purple dashed, signals exception path |
| Eval-gate footer card | `#F0FDF4` bg · `#86EFAC` border | Pale green, deeper saturation |

Zone backgrounds should always have a `1px` border in the matching `border` colour at `rx="14"` corners.

### 3.4 Card text padding · the canonical scale

Inside every card (Inputs · Outputs · step cards · sub-band labels), text must follow this padding scale. The reader notices cramped or top-heavy spacing before they read a single word.

| Position | Distance | Where it lives |
|---|---|---|
| Horizontal (text x → card edge) | **12px** both sides | text x = card x + 12 |
| Top padding (card top → first text baseline) | **20px** | first `<text>` y = card y + 20 |
| Line spacing · 12px+ font (title → first sub-text) | **18px** between baselines | sub-text y = title y + 18 |
| Line spacing · 10.5px font (sub-text → sub-text) | **16px** between baselines | next sub y = prev sub y + 16 |
| Bottom padding (last text baseline → card bottom) | **≥ 12px** | card y + card h − last text y ≥ 12 |

**Card height minimums** (so the padding rule is satisfiable):

| Card type | Lines | Minimum height |
|---|---|---|
| Input / Output card · 1 title + 2 sub-text | 3 | **66px** |
| Step card · 1 num + 1 title + 2 sub-text | 4 | **86px** |
| Step card · 1 num + 1 title + 1 sub-text | 3 | **70px** |
| Sub-band footer (eval gate · routing) | 3 | **84px** |

**Sub-band wrapping a row of step cards (loop / gate band):** the band's vertical extent must include three things, in order top → bottom: (1) a band header label band of ≥ 20px height (header text baseline at band-top + 20), (2) any connector that loops *above* the step cards — give it ≥ 16px clearance from the header label baseline, (3) the step cards themselves with ≥ 12px bottom padding inside the band. Total: header band 20 + connector band 16 + step card height (86) + bottom padding 12 = **134px minimum**. Use 144px to allow the connector to clear comfortably and avoid a Tetris-tight feel. Anti-pattern: routing a loop arrow at the same y as the band header text — letters overlap with the connector stroke.

**Max sub-text length per card width** (Inter 10.5px, ~5.5px avg char width, after 12px×2 horizontal padding):

| Card width | Usable text width | Max sub-text length |
|---|---|---|
| Input / Output card · 184px | 160px | **~28 characters** |
| Step card · 138px | 114px | **~20 characters** (use 2 lines) |
| Step card · 200px | 176px | **~32 characters** |
| Sub-band footer · 660px (full workflow zone) | 636px | **~115 characters** |
| Sub-band footer · 712px (full workflow zone, generous) | 688px | **~125 characters** |

If a sub-text line exceeds the limit, do one of: (a) shorten the prose · (b) split into two `<text>` elements at different y values (cascading vertical, costs sub-band height per §3.4 bottom rule) · (c) widen the card if there's room in the zone. Never let text spill past the visible card border. **Verify by counting characters during authoring** — tools won't catch this, only visual eyeballing or a render pass.

**Anti-patterns to flag in audit:**

- Last text baseline within 8px of the card bottom edge (looks like text is falling out of the card).
- 13px or smaller line spacing between baselines for 10.5px sub-text (lines smush into each other).
- Asymmetric vertical balance — top padding 20px while bottom padding 7px (top-heavy, content wants to sink).
- Cards under 60px tall trying to hold 3 text lines (mathematically impossible to satisfy the rule).

### 3.5 Connector strokes

| Type | Colour | Width | Dash | Marker |
|---|---|---|---|---|
| Default flow | `#6B7280` | 1.4 | none | `arrow` (filled triangle) |
| Loop / retry | `#B45309` | 1.4 | `4 3` | `arrow-loop` (orange) |
| Routing / fail-out | `#9333EA` | 1.4 | `4 3` | `arrow-route` (purple) |

Marker definitions go in `<defs>`; reuse three IDs prefixed with the agent's slug initials (e.g. `cp-arr` for cortex-planning) to avoid collisions if multiple diagrams ever load on one page.

---

## 4. The 12-point pre-publish checklist

Before committing a new or modified `workflow_svg`, verify each:

1. **viewBox is `0 0 1240 620`** (or `1240 720` if more vertical room is genuinely needed).
2. **Zone backgrounds present** · `<rect>` for Inputs (x=14, w=220), Workflow (x=250, w=740), Outputs (x=1006, w=220), all with `rx=14` + matching border.
3. **Zone headers present** · `<text class="zh">INPUTS</text>`, `WORKFLOW · N stages`, `OUTPUTS` at y=40, top of each zone.
4. **No card-text overflow** · every `<text>` element fits inside its parent `<rect>` width minus 24px padding (12px each side). For Inputs/Outputs cards (width 184), max sub-text length ~36 characters at 10.5px Inter.
5. **No truncation ellipses** (`...`) in any sub-text. If content doesn't fit, shorten the source phrase or drop a less-important detail — never abbreviate with `...`.
6. **Step card uniformity** · within a row, all step cards have identical width and height. Don't mix 138px and 200px widths in the same row.
7. **Connector grid alignment** · connector arrow start/end coordinates land on the centre of card edges (top, right, bottom, left midpoints) — never at random offsets.
8. **No connector tangle on input fan-out** · when 5+ input cards feed into one workflow step, route the lines through a vertical "trunk" first (all inputs converge to a single x-coordinate, then the trunk turns right to the step). See `cortex-planning` after the standards-sweep for the canonical fan-in pattern.
9. **Sub-band rectangles aligned to workflow zone bounds** · gate / loop / eval-gate sub-bands sit at x=268-980 (full workflow width minus 18px each side).
10. **Loop arrows don't cross zone boundaries** · a retry loop should curve back inside the workflow zone, not pass through Inputs or Outputs.
11. **`<title>` and `<desc>` set** · `<title>{Agent name} · {workflow shape}</title>` and a 1-2 sentence `<desc>` for accessibility readers (Apex screen-reader scenarios are real).
12. **Mobile-hidden via the @media rule** · `tools/build_agents.py` LOCAL_STYLES already hides `.diagram-wrap` below 768px; the step strip below carries the load on phones. No SVG-side action needed, but verify your step strip has parity with the SVG content.
13. **Card text padding follows the canonical scale (§3.4)** · 12px horizontal, 20px top to first baseline, 18px between title→sub-1, **16px between sub-1→sub-2** (never 13px), ≥12px bottom. Card heights meet the minimums in §3.4 so the rule is satisfiable: 66px for 3-line input/output cards, 86px for 4-line step cards. Any card with <12px bottom padding or <16px sub-text line spacing fails.
14. **Sub-text length fits the card width (§3.4 char-width table)** · count characters before committing. Sub-band footer cards (gate / loop / eval at 660px width) cap at ~115 chars; 184px input/output cards cap at ~28 chars; 200px step cards cap at ~32 chars. SVG does not clip overflowing `<text>` — the prose renders past the card border into the zone background and looks like a printer error.

---

## 5. Issue patterns to prevent

These 7 patterns recurred in the 2026-05-03 audit:

### 5.1 Card-text overflow
**Pattern:** A subtitle string longer than the card width gets clipped, visibly spills over the next card, OR — for sub-band footer cards (gate / loop / eval) — runs past the visible border into the workflow zone background. The latter is sneaky because the SVG doesn't clip; the text just keeps rendering.
**Examples:**
- Step-card subtitles · `category-intelligence` Evidence Tags card (`FORECAST` cut), `agentic-marketing` Meta-Orchestrator subtitle (`rou...` cut), `generative-media` Step 02 `treatment` spillover.
- Sub-band footer cards · `generative-media` (pre-fix): Storyboard Review gate sub-text was 135 chars in a 660px-wide card (max ~115); Performance loop sub-text was 141 chars; Eval line-2 was 113 chars. All three rendered with text bleeding past the right edge of their orange/purple/green borders.
**Fix:** Per §3.4 char-width table, count characters and pick: (a) shorten the prose to fit the per-width budget (preferred; matches the terse tone register · `generative-media` 2026-05-04 fix) · (b) split into 2 lines using a second `<text>` element with a `dy` offset (costs vertical band height per §3.4 sub-band rule) · (c) widen the card if there's room. Never insert `...` to truncate visibly.

### 5.2 Truncation ellipses
**Pattern:** A 3-dot `...` ellipsis used to indicate cut content.
**Example:** `retail-vista` Step 03 `competition · accessibility · rates · ...`.
**Fix:** Pick the most-load-bearing items, drop the `...`. The reader can scroll to the §02 step strip prose for the full list.

### 5.3 Loop arrow crossing zone boundary
**Pattern:** A retry / monitor / feedback arrow drawn from one zone, through another zone, back to the workflow zone.
**Example:** `cortex-planning` orange `delivers` arrow runs vertically through the Outputs zone, partially obscuring the output cards.
**Fix:** Curve the loop arrow back inside the workflow zone using a 90° bend at the workflow zone edge (x=980 or x=268). Don't traverse other zones.

### 5.4 Input fan-out tangle
**Pattern:** 5+ input cards each connecting to a different workflow step in row 1 with diagonal lines that cross each other.
**Example:** `ai-photoshoot` 5 inputs → 5 row-1 cards (Upload, Analyse, Avatar/Pose, Background, Prompt) — 5 diagonals form an X-cross.
**Fix:** Route through a vertical trunk. All inputs end at x=234 (right edge of Inputs zone). A single trunk runs vertically from min-y to max-y at x=240. Then individual horizontal arrows leave the trunk at each card's y-midpoint and travel right to the step card. No diagonals.

### 5.5 Missing zone headers
**Pattern:** Older diagrams (pre-2026-05-03) have no `INPUTS` / `WORKFLOW` / `OUTPUTS` text labels at the top of each zone.
**Fix:** Add the 3 headers at y=40 (16px from top of zone background at y=14):
```svg
<text x="32" y="40" class="zh">Inputs</text>
<text x="268" y="40" class="zh">Workflow · N stages</text>
<text x="1024" y="40" class="zh">Outputs</text>
```

### 5.6 viewBox drift
**Pattern:** Two different viewBox sizes across the catalog (`1200×540` vs `1240×620`).
**Fix:** Standardise on `1240×620`. When upgrading an old diagram, expand the workflow zone width from 700 to 740 (gain 40px for breathing room around step cards).

### 5.7 Cramped text padding · cards too short for their content
**Pattern:** A 3-line input/output card at 60px height with 13px line spacing between the two sub-text rows. Top padding is 20px but bottom padding ends up at 7px, the lines smush, and the card feels top-heavy. Or a step card's second sub-text sits 11px from the card bottom edge with no breathing room.
**Examples:** `ai-photoshoot` (pre-fix) input cards at h=60 with sub-text at y=98 / y=111 (13px gap) inside a card ending at y=118 — bottom pad 7px. Same on output cards. Step cards row 1 at h=86 with sub-text at y=118 / y=131 — 13px gap, 17px to card bottom, but the 13px line spacing reads tight.
**Fix:** Apply the canonical text-padding scale (§3.4) — 12px horizontal, 20px top, 18px title→sub-1, 16px sub-1→sub-2, ≥12px bottom. If the existing card height can't satisfy ≥12px bottom, bump the card height to the §3.4 minimum (66px for 3-line input/output, 86px for 4-line step). The fix on `ai-photoshoot` 2026-05-03: bumped input/output cards 60→66, shifted sub-2 baselines from 13px gap to 16px gap, then re-aligned input/output connector arrows to the new card midpoints (+3px y-shift).

### 5.8 Connector colliding with sub-band header label
**Pattern:** A loop or gate sub-band (orange band wrapping a row of step cards) has its header label at the top edge AND a horizontal loop-arrow segment routed at almost the same y-coordinate. The arrow's stroke crosses the cap-height of the header letters; the result reads as a smudge. Often paired with a redundant arrow-annotation label (`retry · max 2`) that overlaps the band header (`Detect → Edit → Check loop · max 2 attempts`) word-for-word.
**Examples:** `ai-photoshoot` (pre-fix) loop band header at y=246 with retry arrow horizontal at y=236 — the dashed line cuts through the top of `D`, `E`, `C`, `k`, `l` in the header. The `retry · max 2` text at y=232 sat literally on top of the header, with both elements competing for the same 20px band.
**Fix:** Give the connector its own dedicated band inside the sub-band, separated from the header. Per §3.4 sub-band rule, allocate header (20px) + connector clearance (16px) + step cards + bottom padding. Concretely: extend the sub-band height (typically 128px → 144px), keep the header label at top (y = band-top + 20), put step cards at the bottom of the band, and route the loop arrow in the empty band between (y = step-card-top − 10). Drop redundant arrow annotations when the header already conveys the same information (`max 2 attempts` in the header → the `retry · max 2` arrow label is dead weight).

### 5.9 Wide subtitle on a header card
**Pattern:** Large card at the top of the workflow zone (e.g., Meta-Orchestrator) with a long descriptive subtitle that overflows.
**Example:** `agentic-marketing` Meta-Orchestrator `decomposes intent into a workflow DAG · parses goal · plans tasks in parallel where independent · rou[tes]`.
**Fix:** Split the subtitle across 2 lines using two `<text>` elements at different y values, OR shorten to under 70 characters.

---

## 6. The per-agent fix list (2026-05-03 audit)

| Agent | viewBox | Issues to apply |
|---|---|---|
| **cortex-planning** | 1200×540 (defer) | ~~(a) zone headers~~ ✓ already present (Inputs · Workflow · 6 steps · Outputs) · ~~(b) orange `exception → replan` loop arrow~~ ✓ vertical segment moved x=905 (inter-zone gap competing with outputs) → x=885 (just inside workflow zone right edge x=890 per §5.3). Label x=912 → x=895 (still in gap for readability, adjacent to interior arrow). Note: the spec §6 originally said "delivers" loop but the loop is actually labelled "exception → replan"; "delivers" is the unrelated grey one-way arrow at y=290. · **follow-up:** viewBox upgrade + workflow column widening (700→740) deferred to cross-diagram sweep |
| **trend-to-design** | 1200×540 (defer) | ~~(a) zone headers~~ ✓ already present (Inputs · Pipeline · 8 autonomous steps · Outputs) · ~~(b) VLM fail · regen loop re-route~~ ✓ shifted vertical segment x=295→x=280 (from cramped position 15px from step card left edge into the no-zone gap with 30px clear space) · rotated label moved with it · **follow-up:** viewBox upgrade deferred to cross-diagram sweep |
| **category-intelligence** | 1200×540 (defer) | ~~(a) zone headers~~ ✓ already present (Inputs · Pipeline · 7 steps · 4 review pauses · Outputs) · ~~(b) Evidence Tags card overflow~~ ✓ split tags across 2 lines (RUNWAY · RETAIL · SEARCH / SOCIAL · TRADE · FORECAST) · card h 62→78 · Autonomy card shifted down 16px to make room · **follow-up:** viewBox upgrade deferred to cross-diagram sweep |
| **retail-vista** | 1200×540 (defer) | ~~(a) zone headers~~ ✓ already present (Inputs · Pipeline · 4 stages + workspace · Outputs) · ~~(b) Step 03 ellipsis~~ ✓ dropped `...` · workflow_steps detail below already lists all 10 dimensions in full so the SVG card just shows 7 representative dims with no trailing truncation marker · **follow-up:** viewBox upgrade deferred to cross-diagram sweep |
| **agentic-marketing** | 1200×540 (defer) | ~~(a) zone headers~~ ✓ already present (Inputs · 11-agent topology · Outputs) · ~~(b) Meta-Orchestrator subtitle truncation~~ ✓ root cause was missing `text-anchor:middle` on the inline `<text>` style — sub-text rendered LTR from card center · spilled past right edge · also shortened 78 → 60 chars · ~~(c) OUTCOME SIGNALS footer caption~~ ✓ shortened 89 → 65 chars · was bleeding past both card edges in uppercase mono · **follow-up:** viewBox 1200×540 → 1240×620 upgrade · the orange outcome-loop arrow currently crosses from outputs zone up to workflow zone (§5.3 anti-pattern) — both deferred to a cross-diagram viewBox sweep PR covering cortex / trend-to-design / category-intel / retail-vista / agentic-marketing |
| **ai-photoshoot** | 1240×620 ✓ | (a) **fix input fan-out tangle** — route 5 inputs through a vertical trunk at x=240 then horizontal to row 1 · (b) verify zone headers render cleanly |
| **generative-media** | 1240×620 ✓ | ~~(a) Step 02 sub-text overflow~~ ✓ · ~~(b) VIA CLAUDE / VERTEX agent-label~~ ✓ folded into sub-2 · ~~(c) zone headers~~ ✓ · ~~(d) input fan-out tangle (4 diagonals + missing input #5 connector)~~ ✓ replaced with 5 short horizontals + entry arrow per §5.4 · ~~(e) output fan-out tangle (4 diagonals)~~ ✓ replaced with single exit + 4 short horizontals · ~~(f) row-1→gate and gate→row-2 diagonals~~ ✓ orthogonal verticals (Step 03 ↓ gate ↓ Step 04) · ~~(g) performance loop diagonal~~ ✓ orthogonal · drop output→perf-card arrow, perf body text covers it |

**Estimated effort:** ~2 hours total for the 5 older diagrams (viewBox upgrade + zone headers + per-fix), ~30 min for the 2 newer (targeted fixes only). Each diagram is independent; can be done incrementally.

---

## 7. Application workflow

When applying these standards to an agent diagram:

```bash
# 1. Read current state of the YAML
cat data/agents/<slug>.yaml | sed -n '/^workflow_svg:/,/^[a-z]/p'

# 2. Edit data/agents/<slug>.yaml workflow_svg + workflow_diagram_caption fields

# 3. Rebuild the agent page
.venv/bin/python tools/build_agents.py <slug>

# 4. Re-sync DEPLOYED-IN markers (always idempotent · does no harm)
.venv/bin/python tools/inject_path_to_l4.py

# 5. Visual verify via Chrome DevTools MCP
#    new_page → /agents/<slug>/ → auth bypass → scroll to .diagram-wrap → take_screenshot

# 6. Run the 12-point checklist against the screenshot

# 7. Drift gates
.venv/bin/python tools/inject_path_to_l4.py --check  # must exit 0
.venv/bin/python tools/inject_chrome.py --check     # must exit 0
.venv/bin/python tools/inject_present.py --check    # must exit 0
```

---

## 8. When NOT to apply this skill

- **Architecture diagrams** — the agent template (`docs/agents-spec.md` D22) drops §04 Architecture from the rendered page. Architecture SVGs stay in YAML metadata only and are never rendered. No standards apply.
- **Platform pages** — JCP / Granary / Impetus etc. carry their own bespoke SVGs (e.g., the JCP §01 architecture diagram). Different visual conventions apply; this skill is agent-pages-only for now.
- **Diagrams below 200px wide on mobile** — the agent SVG is already hidden below 768px via `@media` rule in `build_agents.py`. The step strip below carries the load. Don't try to make a complex SVG mobile-readable; the strip is the answer.

---

## 9. Glossary

| Term | Meaning |
|---|---|
| **Zone** | One of the three vertical bands in the diagram: Inputs (left), Workflow (centre), Outputs (right). |
| **Sub-band** | A horizontal rectangle inside the Workflow zone that highlights a gate (human-in-loop), loop (retry / feedback), or eval block. |
| **Step card** | A rectangle inside the Workflow zone representing one numbered workflow stage. |
| **Connector** | A `<path>` arrow between two cards or between a sub-band and a card. |
| **Trunk** | A single vertical connector line that gathers multiple input lines before fanning out to multiple targets — used to prevent fan-out tangles. |
| **Marker** | An SVG `<marker>` element defining the arrowhead shape on a connector. |
| **Loop arrow** | A connector that returns from a later step to an earlier one (orange, dashed). |
| **Routing arrow** | A connector that exits the main flow into an exception path like Manual QC (purple, dashed). |

---

## 10. Spec changelog

| Date | Version | Change |
|---|---|---|
| 2026-05-03 | v0.1 | Initial spec. Captures 2026-05-03 audit findings · 14 issues across 7 diagrams. Per-agent fix list + 12-point checklist + 3-zone canonical architecture. |
| 2026-05-03 | v0.2 | Added §3.4 canonical text-padding scale (12px x · 20px top · 18px / 16px line spacing · ≥12px bottom · card-height minimums) + checklist item #13 (padding rule) + pattern §5.7 (cramped text padding). Triggered by ai-photoshoot input/output cards needing rebalance after the fan-out fix landed. |
| 2026-05-03 | v0.3 | Added §3.4 sub-band internal-padding rule (header band 20 + connector band 16 + step cards + 12 bottom = 134px min, use 144px) + pattern §5.8 (connector colliding with sub-band header label). Triggered by ai-photoshoot Detect→Edit→Check loop block where the retry arrow stroke at y=236 cut through the band header at y=246 and the redundant `retry · max 2` annotation overlapped the band header word-for-word. Fix: extended loop block 128→144px, dedicated 16px band between header and step cards for the loop arrow, dropped the redundant annotation. |
| 2026-05-04 | v0.3.1 | generative-media · all cited + uncited diagram issues fixed in one pass: Step 02 sub-text overflow (3 lines now fit, agent-label folded into sub-2), input fan-out tangle (5 short horizontals + entry arrow per §5.4 · was 4 diagonals + missing input #5), output fan-out tangle (single exit + 4 short horizontals · was 4 diagonals), row-1→gate / gate→row-2 connectors orthogonalized to clean verticals (Step 03 ↓ gate ↓ Step 04), performance loop orthogonalized (perf card → input #5 only · output→perf-card arrow dropped since perf body text covers it). |
| 2026-05-04 | v0.3.2 | agentic-marketing · text overflow fixes only · root cause for Meta-Orchestrator subtitle truncation captured: `<text>` element with x at card center but missing `text-anchor:middle` on inline style → rendered left-to-right starting from card center, spilling past right edge. Fix: add `text-anchor:middle` AND shorten if needed (78 → 60 chars here). Outcome footer separately shortened (89 → 65 chars uppercase mono, was bleeding past both edges of 540px card at ~7px/char). viewBox upgrade + cross-zone loop arrow deferred to a planned cross-diagram sweep covering all 5 older 1200×540 diagrams. |
| 2026-05-04 | v0.3.3 | category-intelligence · Evidence Tags overflow fix · 52-char tag list in 228px card (overflowed by ~86px · "FORECAST" clipped to "F"). Split across 2 sub-text lines (RUNWAY · RETAIL · SEARCH / SOCIAL · TRADE · FORECAST). Card h 62→78. Adjacent Autonomy card shifted down 16px so it lands flush with zone bottom (y=440 h=80, ends at zone bottom y=520). viewBox upgrade deferred to cross-diagram sweep. |
| 2026-05-04 | v0.3.4 | retail-vista · Step 03 ellipsis fix · dropped trailing `...` from `competition · accessibility · rates · ...` per spec §5.2. The full 10-dimension list already lives in the workflow_steps Step 03 detail prose below the SVG; the card shows 7 representative dims with no truncation marker. viewBox upgrade deferred to cross-diagram sweep. |
| 2026-05-04 | v0.3.5 | trend-to-design · VLM fail · regen loop arrow re-route · vertical segment shifted x=295→x=280 (from 15px clearance off step card left edge to 30px in the no-zone gap between inputs zone end and workflow zone start). Rotated label x=287→x=272 in tandem · gives the loop a clear visual band rather than competing with step card borders. viewBox upgrade deferred. |
| 2026-05-04 | v0.3.6 | cortex-planning · `exception → replan` orange loop arrow re-route · pre-fix vertical segment at x=905 sat in the inter-zone gap (workflow ends 890, outputs starts 920) and the rotated label at x=912 was visually crowding the outputs zone left edge. Per §5.3 vertical segment pulled to x=885 (just inside workflow zone right edge). Label moved x=912 → x=895 — still in inter-zone gap (where it remains readable) but now adjacent to the now-interior arrow. Also discovered: spec §6 cortex-planning row called this the "delivers" loop, but `delivers` is actually an unrelated grey one-way arrow at y=290; the actual loop label is `exception → replan`. Spec text corrected. **All 5 surgical-fix diagrams (agentic-marketing · category-intel · retail-vista · trend-to-design · cortex-planning) now have cited issues addressed.** Only outstanding cross-cutting work is the viewBox 1200×540 → 1240×620 sweep (catalog uniformity) — defers to a final dedicated sweep PR. |

---

**End of skill.** Apply via the workflow in §7. Verify via the 12-point checklist in §4. The reference exemplar is `data/agents/ai-photoshoot.yaml` (already passes most of the checklist; needs only fan-out fix per §6).
