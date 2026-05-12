---
spec: path-to-l4
purpose: Add a "Path to L4" section to the 5 platform pages that have named agents from the `/agents/` directory. Surfaces the platform → named-agent mapping so an Apex reader on a platform page can answer "how does this become L4 agentic" without leaving the page. No copy changes on the other 17 platforms — honest absence is itself signal (the gap the agent program needs to close next).
status: signed-off · ready to implement
as-of: 03-May-2026
audience: RIL Apex leadership (MM Sir level)
owner: <fill>
---

# Path to L4 · spec

## 0 · Why

`/agents/` is the canonical directory of the 6 named AI Agents — Cortex Planning, Retail Vista, Category Intelligence, Trend-to-Design, Marketing, AI Cataloging. Each agent links *into* `/agents/<slug>/` from its parent platform pages, but the **reverse mapping is not on the platform pages**. An Apex reader on `/jcp/` or `/ucp/` cannot easily answer:

> *"What gets this platform to L4 agentic, and which named agents take it there?"*

The information exists — scattered across `/autonomous/` (the L0–L5 framework), `/agents/` (the agent inventory), and individual platform pages (Cortex on `/impetus/cortex/`, Marketing on `/ucp/`, etc.). The platform-side surfacing of *"these agents move me to L4"* is the missing piece.

This spec adds a single "Path to L4" section to **only** the 5 platforms that actually have named agents from the canonical 6-agent directory. The other 17 platforms get no copy changes — their absence from this surface is the honest signal of where the agent program hasn't yet landed.

---

## 1 · Goals · non-goals

**Goals**
- A standardised "Path to L4" section on the 5 platforms that have named agents from `/agents/`
- Per-platform: current autonomy rung (L0–L5 per `/autonomous/`) → named agents that bridge → what each agent unlocks for THIS platform
- Each agent name on the section is a hyperlink to `/agents/<slug>/` — bidirectional with the platform mentions already on the agent pages

**Non-goals**
- Adding the section to platforms without named agents (the other 17)
- Authoring new agent pages
- Changing the L0–L5 framework on `/autonomous/`
- Renaming, restructuring, or otherwise touching the existing 5 platform pages outside the new section

---

## 2 · Scope · the 5 platforms in

The 5 platforms with named agents from the `/agents/` directory:

| # | Platform | Page | Agents (proposed) |
|---|---|---|---|
| 1 | **Impetus** | `/impetus/` | Cortex Planning · Trend-to-Design · Category Intelligence |
| 2 | **JCP** | `/jcp/` | AI Cataloging |
| 3 | **UCP & Marketing OS** | `/ucp/` | Marketing |
| 4 | **Granary** | `/granary/` | Cortex Planning (shared with Impetus) |
| 5 | **RetailVista** | `/retail-vista/` | (the page IS the Retail Vista agent's deployment surface — see §4.5 special case) |

The exact per-platform agent list is **proposed**; page owners confirm in §8 O-2.

---

## 3 · Section anatomy

A new `§0X · Path to L4` section on each of the 5 platform pages. Standardised template across all 5 so an Apex reader trained on one knows the others.

**Position (resolved · Round 1 · 03-May-2026).** The section sits **immediately after `§02 · What's live`** — i.e., it becomes `§03 · Path to L4`, and every subsequent section on the existing page shifts down by 1 (Architecture → §04, Deep dive → §05, In flight → §06, Vision/Roadmap → §07). Rationale: surface the agent path early, while the reader still has "what's live" fresh; don't bury it at §06.

The existing §06 Vision/Roadmap section **stays as-is** on all 5 pages (resolved · Round 2). Path to L4 (the agent path) and Vision/Roadmap (broader product roadmap) cover different ground — agents vs full feature roadmap — and coexist.

**Template:**

```
§06 · PATH TO L4

H2: <short headline · what L4 means for THIS platform>

Lead (2-3 sentences):
  Where the platform sits today (current rung · L1 / L2 / L3) →
  what L4 looks like for this platform · which named agents close the gap.

Per-agent rows (table or card grid, one row per agent):
  Agent name (links to /agents/<slug>/) · current state pill (Live / Building / Roadmap)
  · target rung (typically L4) · 1-line "what it unlocks for THIS platform"
  · DRI / link to the agent page

Section CTA: 'Open all agents → /agents/'
```

**Visual treatment.** Inherits design.md tokens · `section-label`, `display-2`, `.platform-card` (for the agent rows) or `.grid-table` (for the table variant). Pick one per page; stay consistent. **No new component variant.**

---

## 4 · Per-platform content (proposed)

Each subsection is the spec for that platform's §06 Path to L4. Page owners review and confirm in §8 O-2.

### 4.1 · Impetus · `/impetus/`

- **Current rung:** L3 (planning agents in flight, foundation Live)
- **Target:** L4 (cross-domain agents close the loop on Plan → Buy → Make → Sell)
- **Agents (3):**
  | Agent | State | Target | Unlocks for Impetus |
  |---|---|---|---|
  | [Cortex Planning](/agents/cortex-planning/) | Building | L4 | Store-realistic Plan of Record + continuous, exception-led replanning across the Impetus stack |
  | [Trend-to-Design](/agents/trend-to-design/) | Live | L4 | Trend brief → manufacturable design package without humans in the design cycle middle |
  | [Category Intelligence](/agents/category-intelligence/) | Building | L4 | Category × season × geography → 40-50pp evidence-tagged trend report for buying teams |

### 4.2 · JCP · `/jcp/`

- **Current rung:** L3 (commerce platform Live; agentic surfaces in build)
- **Target:** L4 (catalog + agentic shopping close the loop end-to-end)
- **Agents (1, possibly 2 — confirm):**
  | Agent | State | Target | Unlocks for JCP |
  |---|---|---|---|
  | [AI Cataloging](/agents/ai-cataloging/) | Live | L4 | Mannequin or product image → enriched catalog page with model-on photo, attribute set, and motion video. 5 hours, not 15 days. |
  | (consider) AJIO ZIP / Kaily as the agentic-commerce surface inside JCP — but Kaily is its own page; spec keeps it separate per Round 1 R4 of home-redesign | — | — | — |

### 4.3 · UCP & Marketing OS · `/ucp/`

- **Current rung:** L3 (UCP foundation Live; Marketing OS cockpits building)
- **Target:** L4 (full agentic chat that drives campaigns end-to-end)
- **Agents (1):**
  | Agent | State | Target | Unlocks for UCP |
  |---|---|---|---|
  | [Marketing](/agents/agentic-marketing/) | Building | L4 | Goal in plain English → audience, creative, channel mix, send time, measurement — autonomously, with humans only on guardrails |

### 4.4 · Granary · `/granary/`

- **Current rung:** L2 (Phase 1 11-store Mumbai pilot · MAPE 41 %)
- **Target:** L4 (assortment + replenishment agents drive 12 K SKUs × 4 K stores)
- **Agents (1, shared):**
  | Agent | State | Target | Unlocks for Granary |
  |---|---|---|---|
  | [Cortex Planning](/agents/cortex-planning/) | Building | L4 | Store-realistic Plan of Record + continuous, exception-led replanning · same agent as Impetus, applied to grocery |

### 4.5 · RetailVista · `/retail-vista/` · special case

RetailVista is **both** a platform and the named agent — the page IS the agent's deployment surface. **Resolved · Round 1 · 03-May-2026:** RetailVista gets a standard Path to L4 section that **frames its 3 tracks as the agent's path**. The 3 existing tracks (Internal · Google · JioGIS) become the per-track rows of the Path to L4 table.

- **Current rung:** L3 (Internal Track Live · Opportunity Explorer at 68 scored leads)
- **Target:** L4 (cross-track Site Intelligence Agent driving end-to-end NSO decisioning)
- **Section content** — single-agent (Retail Vista), 3 deployment tracks. Use `.grid-table` pattern with rows = tracks rather than rows = agents:

| Track | State | Target | What this track unlocks |
|---|---|---|---|
| Internal · UCP / JioMart | Live | L4 | Opportunity Explorer · 68 scored leads · agentic decisioning end-to-end |
| Google · Joint MVP | Pilot | L4 | Cannibalisation, feasibility and site-selection agents on Vertex AI · Mumbai catchments |
| JioGIS | Building | L4 | Spatial reasoning core · Foundation model · feeds all 3 tracks once secured |

---

## 5 · Visual treatment

Pick **one** of two patterns per page (consistent within page):

**Pattern A · `.grid-table`** (recommended for pages with 2+ agents — Impetus):
```html
<table class="grid-table">
  <thead>
    <tr><th>Agent</th><th>State</th><th>Target</th><th>Unlocks for <Platform></th></tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="/agents/cortex-planning/">Cortex Planning</a></td>
      <td><span class="pill pill-build">Building</span></td>
      <td>L4</td>
      <td>Store-realistic Plan of Record + continuous, exception-led replanning…</td>
    </tr>
    …
  </tbody>
</table>
```

**Pattern B · `.platform-card` grid** (recommended for pages with 1 agent — JCP, UCP, Granary):
```html
<div class="grid sm:grid-cols-2 gap-3 max-w-3xl">
  <a href="/agents/<slug>/" class="platform-card">
    <div class="platform-card-head">
      <div class="platform-card-name">Cortex Planning</div>
      <span class="pill pill-build">BUILDING</span>
    </div>
    <div class="platform-card-desc">Store-realistic Plan of Record + continuous, exception-led replanning…</div>
    <div class="platform-card-foot"><span class="platform-card-tag">L4 target</span></div>
  </a>
</div>
```

Both inherit existing classes from `style.css`. **No new variants.**

---

## 6 · Bidirectional cross-link · `data/agents-x-platforms.yaml` registry

**Resolved · Round 2 · 03-May-2026:** build the registry + sweep tool now (instead of deferring to manual grep). Single source of truth, bulletproof verification.

When a platform page claims an agent in its Path to L4 section, the agent's `/agents/<slug>/` page **must** list that platform as a deployment. Honesty contract — if `/jcp/` claims `AI Cataloging` but `/agents/ai-cataloging/` doesn't list `/jcp/` as a deployment, one of them is wrong.

### 6.1 · Registry · `data/agents-x-platforms.yaml`

```yaml
# Single source of truth for agent → platform deployment claims.
# Each agent slug lists every platform it is deployed in.
# A sweep tool (tools/inject_path_to_l4.py) reads this and:
#   - injects the §03 Path to L4 section into each platform page
#   - injects the "deployed in" list into each agent page
#   - --check exits non-zero if either side drifts from the registry
agents:
  cortex-planning:
    name: "Cortex Planning Agent"
    state: "Building"          # Live | Building | Roadmap
    target_rung: "L4"
    deployments:
      - platform: impetus
        unlocks: "Store-realistic Plan of Record + continuous, exception-led replanning across the Impetus stack"
      - platform: granary
        unlocks: "Same agent applied to grocery — assortment + replenishment for 12 K SKUs × 4 K stores"
  trend-to-design:
    name: "Trend-to-Design Agent"
    state: "Live"
    target_rung: "L4"
    deployments:
      - platform: impetus
        unlocks: "Trend brief → manufacturable design package without humans in the design cycle middle"
  category-intelligence:
    name: "Category Intelligence Agent"
    state: "Building"
    target_rung: "L4"
    deployments:
      - platform: impetus
        unlocks: "Category × season × geography → 40-50pp evidence-tagged trend report for buying teams"
  ai-cataloging:
    name: "AI Cataloging Agent"
    state: "Live"
    target_rung: "L4"
    deployments:
      - platform: jcp
        unlocks: "Mannequin or product image → enriched catalog page with model-on photo, attribute set, and motion video. 5 hours, not 15 days."
  agentic-marketing:
    name: "Marketing Agent"
    state: "Building"
    target_rung: "L4"
    deployments:
      - platform: ucp
        unlocks: "Goal in plain English → audience, creative, channel mix, send time, measurement — autonomously, with humans only on guardrails"
  retail-vista:
    name: "Retail Vista"
    state: "Building"          # composite — Internal Live, Google Pilot, JioGIS Build
    target_rung: "L4"
    deployments:
      - platform: retail-vista
        unlocks: "Three-track agent: Internal (Opportunity Explorer Live · 68 scored leads) · Google (Vertex AI Pilot) · JioGIS (Foundation model Build)"

platforms:
  # Reverse index — auto-derived; the sweep tool generates this
  # so we don't hand-maintain two sides. Manual edits to this section
  # are blown away on next sweep.
  impetus: [cortex-planning, trend-to-design, category-intelligence]
  jcp: [ai-cataloging]
  ucp: [agentic-marketing]
  granary: [cortex-planning]
  retail-vista: [retail-vista]
```

### 6.2 · Sweep tool · `tools/inject_path_to_l4.py`

Mirrors the pattern of `tools/inject_chrome.py` and `tools/inject_meta_robots.py`. Reads `data/agents-x-platforms.yaml`, renders the §03 Path to L4 section into the 5 platform pages, renders the "deployed in" list into the 6 agent pages, and exposes `--dry` and `--check` flags.

```bash
python tools/inject_path_to_l4.py          # rewrite both sides
python tools/inject_path_to_l4.py --dry    # report what would change
python tools/inject_path_to_l4.py --check  # exit non-zero on drift (CI / pre-commit)
```

After every edit to `data/agents-x-platforms.yaml`, run `--check` before commit. Drift = bypass = fix.

Add `inject_path_to_l4 --check` to `website-page-reviewer` Phase 7 (Cross-Page Consistency).

---

## 7 · What's NOT in scope · the 17 platforms without agents

These pages get **zero copy changes** in this PR:

ALP · Retail Jarvis · Forge · Samarth Plus · HireFirst · SwapEasy · TMS · Fynd Konnect · Boltic · PixelBin · Ratl · Kaily · Fynd Kio · AutRi · Dark Factory · Fynd Horizon · Fynd Academy.

**Why no Path to L4 section there.**
- The honest answer for each is *"no named agent from `/agents/` yet"*. Adding a Path to L4 section that says that loudly is worse than not adding it — it reads as filler.
- Several of these platforms (Boltic, Kaily, Ratl) are themselves **agentic platforms** but don't pull from the canonical 6-agent directory. Their L4 narrative belongs in their own section structures, not in a copy-pasted Path to L4 template.
- The absence of Path to L4 on these pages **is itself the signal** to Apex: these are the platforms where the agent program hasn't yet landed. That's the gap the agent directory needs to close next.

**Caveat.** If a page owner believes their platform DOES have a named agent (e.g., RetailVista already counts itself), surface in §8 O-3.

---

## 8 · Resolutions · 03-May-2026

All 6 open items resolved across two interactive rounds. One item (O-2 JCP scope) deferred to the page owner during implementation.

| # | Question | Resolution |
|---|---|---|
| O-1 | Section position | **§03 · right after §02 What's live.** Pushes existing §03 Architecture → §04, etc. Rationale: surface the agent path early, while "what's live" is still in the reader's head. |
| O-2 | Agent → platform mapping | **Granary, RetailVista, UCP confirmed** as proposed. **JCP scope deferred** — page owner decides during implementation between (a) AI Cataloging only, (b) + Kaily/ZIP, (c) + Retail Vista, (d) all three. Default if no decision: AI Cataloging only (matches /agents/ canonical mapping). |
| O-3 | RetailVista special case | **Add a standard Path to L4 section that frames the 3 tracks as the agent's path.** Use `.grid-table` with rows = tracks (Internal Live · Google Pilot · JioGIS Build) rather than rows = agents (since there's only one agent — Retail Vista itself). See §4.5 above. |
| O-4 | Pattern choice | **Per-page discretion** — `.grid-table` when 2+ agents (Impetus), `.platform-card` grid when 1 agent (JCP, UCP, Granary). RetailVista uses `.grid-table` with tracks-as-rows (special case). |
| O-5 | Bidirectional verification | **Build `data/agents-x-platforms.yaml` registry + `tools/inject_path_to_l4.py` sweep tool now.** Single source of truth; sweep injects both the platform section AND the agent's deployed-in list, plus `--check` flag for CI / pre-commit. See §6 above. |
| O-6 | Current rung values | **Accepted as proposed** — Impetus L3 · JCP L3 · UCP L3 · Granary L2 · RetailVista L3. All target L4. |

**Vision/Roadmap retention (Round 2 follow-up question raised by O-1 = §03 placement):** Existing §06 (now §07 after the Path to L4 insertion shifts everything) Vision/Roadmap **stays unchanged** on all 5 pages. Path to L4 covers the agent path; Vision/Roadmap covers the broader product roadmap; they coexist.

---

## 9 · Implementation sequence

All §8 items resolved; ready to implement.

1. **Author `data/agents-x-platforms.yaml`** with the 6 agent → platform mappings per §6.1. Single commit. (Page owner can override JCP scope here per O-2 default.)
2. **Build `tools/inject_path_to_l4.py`** sweep tool per §6.2. Single commit.
3. **Run sweep · platform side.** `python tools/inject_path_to_l4.py` injects §03 Path to L4 into the 5 platform pages. Renumbers existing §03–§NN to §04–§(NN+1). One commit per platform so any single page can be reverted without unwinding the rest:
   - 9.3a — Impetus §03 Path to L4 (3 agents · grid-table pattern)
   - 9.3b — JCP §03 Path to L4 (1 agent · platform-card pattern · default to AI Cataloging only unless owner extends per O-2)
   - 9.3c — UCP §03 Path to L4 (1 agent · platform-card pattern)
   - 9.3d — Granary §03 Path to L4 (1 agent · platform-card pattern)
   - 9.3e — RetailVista §03 Path to L4 (3 tracks · grid-table pattern · per §4.5)
4. **Run sweep · agent side.** Same script injects "deployed in: [platforms]" list into each of the 6 `/agents/<slug>/` pages. Single commit (sweep across all 6 agent pages).
5. **Verify.**
   - `python tools/inject_path_to_l4.py --check` exits 0
   - `python tools/inject_chrome.py --check` exits 0 (no nav / footer drift)
   - `python tools/inject_meta_robots.py --check` exits 0
   - Section labels remain a contiguous numeric run on each updated page (now starts at §01, ends at §08 instead of §07 — adds one)
   - Tone-of-voice grep clean (no banned vocab introduced)
   - Bidirectional grep · for each platform page that claims an agent, verify the agent page lists it back (the sweep enforces this, but spot-check)
6. **Audit.** Run `website-page-reviewer` against each updated platform page (5) and each updated agent page (6). Resolve HIGH + MEDIUM findings. Write audit JSONs to `docs/audits/`.
7. **PR** from `fynd-create-portfolio` → `master`.

---

## 10 · What this spec does NOT do

- Touch any platform page outside the 5 listed.
- Author new agent pages or change the canonical 6-agent directory.
- Change the L0–L5 framework on `/autonomous/`.
- Add `§Sources` blocks, attribution lines, or owner footers (banned per CLAUDE.md).
- Promise dates the source can't back. Where an agent is "Building" with no committed L4-arrival date, the section says "Building" without a target date.
- Implement anything before sign-off on §8 open items.
