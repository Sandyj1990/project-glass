# Impetus · Path to L4 · Build Plan + AI Photoshoot Agent · Spec

**Status:** v0.1 · 2026-05-03 · approved for build
**Owner:** Kushan Shah
**Routes:**
- `/agents/ai-photoshoot/` (new — 7th agent in the catalog)
- `/agents/` (updated — 7-card grid)
- `/impetus/` (updated — §03 PATH TO L4 gains a Milestone column · new §04 PATH TO L4 · the build plan · existing §04 Design Portfolio renumbers to §05)
**Source content:**
- `docs/agent-catalog-notes-compilation/AI_Photoshoot_Note_v1.docx` — 6-section agent write-up (10-step pipeline · 11-row category coverage · Trends Reboot delivery · Lingerie unlock · Auto-Edit/Eval scoring · what's next)
- `docs/agent-catalog-notes-compilation/F&L AI Projects.xlsx` — chairman-facing 3-week build plan (Project Impetus Cortex pivot · AI Photoshoot · AI Design Agent), reference date 04-May-2026
**Inherits from:**
- `docs/agents-spec.md` (v0.8 · agent template, 7-section detail page after §Architecture and §Status drops)
- `docs/path-to-l4-spec.md` (canonical agent ↔ platform registry)
- `docs/impetus-restructure-spec.md` (15-platform precedent, page section spine)
- `.claude/skills/website-tone-of-voice.md` (copy register, dates `DD-MMM-YYYY`, no marketing voice)

---

## 1. Why this spec exists

Today the `/impetus/` §03 PATH TO L4 table (canonical, sweep-rendered from `data/agents-x-platforms.yaml`) shows three agents (Cortex Planning · Trend-to-Design · Category Intelligence) with Agent / State / Target Rung / What it Unlocks columns. There is **no time-bound milestone visible**, **no AI Photoshoot row**, and **no home for the chairman-facing 3-week roadmap** that landed on 02-May-2026 in `F&L AI Projects.xlsx`.

The Apex reader on `/impetus/` today can answer "what agents close the gap to L4?" but not "by when?" or "what's the build plan?". This spec closes both gaps without a new top-level route.

Three additions, in order of dependency:

1. **AI Photoshoot agent page** at `/agents/ai-photoshoot/` — 7th agent in the catalog, source-grounded in `AI_Photoshoot_Note_v1.docx`. Status `Live`, autonomy `L4`, primary platform `/impetus/ai-photoshoot/`. Renders the existing 7-section template via `tools/build_agents.py`.
2. **Milestone column on §03 PATH TO L4** — a 5th `Next milestone` column added to the canonical injector at `tools/inject_path_to_l4.py`, sourced from a new optional `next_milestone:` field in `data/agents-x-platforms.yaml`. Dates pulled verbatim from the xlsx for Impetus deployments.
3. **§04 PATH TO L4 · the build plan** — new hand-authored section on `/impetus/index.html`, three project cards rendering the full 3-week roadmap inline (per user direction · all-inline, no deep page). Existing §04 Design Portfolio renumbers to §05.

**Why this belongs on `/impetus/` and not on a deep route:**
- The roadmap is *Impetus-scoped* (the three projects are all Impetus-internal: Cortex pivot, AI Photoshoot category expansion, AI Design pod completion). It doesn't sit naturally under `/agents/` (agent-scoped) or `/autonomous/` (framework-scoped).
- Apex landing on `/impetus/` after the §03 question ("how does this become L4?") needs the answer to *"by when?"* on the same scroll — splitting it across pages buries the temporal honesty.
- v1 ships inline. If the data starts changing weekly, lift to `data/impetus-l4-roadmap.yaml` + a render script in v2.

---

## 2. Source inventory

### A · Primary canonical sources

| Source | Type | Path | Key facts |
|---|---|---|---|
| AI Photoshoot Note v1 | docx | `docs/agent-catalog-notes-compilation/AI_Photoshoot_Note_v1.docx` | Agent write-up · 10-step pipeline (Upload → Analyse → Avatar/Pose → Background → Prompt → Generate → Detection → Auto-Edit → Quality → Deliver) · 11-row category coverage · Trends Reboot 47,473 images / 2,975 styles / 12 shots per product · Lingerie pipeline unlock with text-based identity workaround · Auto QC 8.06/10 · scoring rule (10 base, ≥7.0 Approved, identity penalty −4.0) |
| F&L AI Projects · xlsx | xlsx | `docs/agent-catalog-notes-compilation/F&L AI Projects.xlsx` | Chairman-facing build plan, reference date 04-May-2026. **Project 1 · Cortex pivot to category-led** · 28 deliverables · Day-0 04-May → Go/No-Go 25-May. **Project 2 · AI Photoshoot** · pipeline 10/10 Live · 11 categories (7 Live + 3 Partial + 1 Upcoming · Ethnic Wear 28-May). **Project 3 · AI Design Agent** · 8-step pipeline (all Live) · 43 pods (28 Live · 5 Partial · 7 Upcoming · 3 N/A) · improvement windows 21-May, 25-May, 28-May, 30-May |

### B · Cross-link sources (existing surfaces we wire to)

- `data/agents/cortex-planning.yaml` — structural template for the new `data/agents/ai-photoshoot.yaml` (7 sections + workflow SVG + step strip + stats + patterns + evals + in_flight + linked_platforms + source_citations).
- `data/agents/_catalog.yaml` — index hero config; bumps to 7 agents.
- `data/agents-x-platforms.yaml` — agent ↔ platform registry; new `ai-photoshoot:` block + `next_milestone:` field added per Impetus deployment.
- `tools/inject_path_to_l4.py` — sweep tool; extends grid-table renderer with milestone column.
- `tools/build_agents.py` — index + detail page renderer; auto-picks-up `ai-photoshoot.yaml`.
- `impetus/index.html` — hand-authored Impetus index; receives the new §04 inline.
- `impetus/ai-photoshoot/index.html` — existing platform sub-page (built by `tools/build_impetus.py`); optional pill backlink to `/agents/ai-photoshoot/`.

### C · Per-agent milestone dates (derived from xlsx for the §03 column)

| Agent on Impetus | next_milestone (verbatim destination string) |
|---|---|
| Cortex Planning | `25-May-2026 · Pilot Hit/Year Go/No-Go (category-led pivot)` |
| Trend-to-Design | `30-May-2026 · Saree drape (Pod 15) + Indian designer (Pod 42) + sherwani craft (Pod 7) improvement window` |
| Category Intelligence | `—` (no source roadmap entry · honest blank, per Q&A) |
| AI Photoshoot (new) | `28-May-2026 · Ethnic wear pipeline (kurtas, kurta sets, ethnic dresses)` |

---

## 3. Page structure

### A · `/agents/ai-photoshoot/` (new detail page)

Strict 7-section template per `docs/agents-spec.md` (D22 + D23 dropped Architecture and Status). Every section identical shape to the other 6 agents.

#### §0 · Hero
- Crumb: `Home / AI Agents / AI Photoshoot Agent`
- Section label: `AI AGENTS · AI-PHOTOSHOOT · LIVE`
- H1: **AI Photoshoot Agent.**
- Sub-title: *"Flat-lay or mannequin product image → on-model 4K catalogue shoot in 2-4 minutes, with autonomous detection, surgical edit, and Ajio-standard delivery."*
- Status pills: `Live` · `SELL` · `L4` · `Powered by → AI Photoshoot`
- Stat tiles (4):
  - **47,473** images · *Trends Reboot delivered for Ajio*
  - **12** shots/product · *front · back · side · closeups · across 12 camera views*
  - **8.06/10** Auto QC score · *current crop-extraction pipeline*
  - **L4** Catalog Photoshoot · *fully agentic detect → edit → check loop*

#### §01 · The job to be done
- Pain · "Catalogue photoshoots gate every retail launch. Studio booking · model availability · stylists · post-production cuts down 4 weeks per category drop. Lingerie alone runs 3-4× standard cost on talent and lighting; turnaround stretches to 6 weeks."
- What it does · paraphrased from Note §1 · 3-mode generation · agentic detect/edit/check loop.
- Human role · brand QC on flagged-below-7.0 images · category onboarding for new pods · final approval before go-live to Ajio.

#### §02 · How it works · the closed loop
- **Inline SVG diagram** (3-zone layout matching `cortex-planning.yaml`):
  - Left band · Inputs (Product references · Avatar selection · Pose pool · Background image · Prompt assembly)
  - Centre band · 10 workflow steps in 2 rows of 5 · with the Detection → Auto-Edit → Check sub-loop drawn explicitly (penalty values inline)
  - Right band · Outputs (4K images on GCS · CDN · Ajio-standard naming `style_id/color_id/product_id/MODEL.jpg`)
  - Loop arrow · Quality < 7.0 → Manual QC routing
- **Step strip · 10 entries** (verbatim from Note §2)

#### §03 · Underlying data
| Source | Classification | Key entities |
|---|---|---|
| Product reference store | Human-Created | Front/back/side images, garment metadata |
| Brand pose library | Human-Created | 12 camera view types, gender × age × ethnicity matrix |
| Product reference DB | Mixed | Fabric · colour · pattern · silhouette extracted by Analyse step |
| Background catalogue | Human-Created | Studio · lifestyle · seasonal backgrounds with extracted lighting profiles |
| Generated image store | Machine-Created | All output images, scored, with detection/edit traces |

Refresh cadence · per-job (Instant 2-4 min · Batch async). KPIs moved · cost per shot · time-to-catalogue · style coverage · Auto QC pass rate.

#### §04 · Design patterns used
- **Tool Calling** · Detection Agent uses code execution for zoom/crop inspection of fine details (logos, embroidery, text).
- **Multi-Agent Orchestration** · Detection · Edit · Check · validate-retry loop with max 2 attempts. Canonical example of the pattern across the catalog.
- **Wide Research** · Generates N candidate images per pose in parallel batches (up to 20 concurrent), scores, picks above-threshold.
- **Context Engineering** · Per-pose NL prompt assembly (product + avatar + theme + view-aware lighting + filtered accessories).
- **Observability** · Every image carries a structured score breakdown (issues found · confidence · penalty applied · final score).
- **Evals** · 10-base scoring rule with deductions runs on every output before delivery.

#### §05 · Evals · how we know it works
- Status: `in-production` (not in-development — this agent ships with its eval loop running)
- Approach · Auto-Detection runs on every generated image. 10.0 base; deduct = `total_issues × (avg_confidence / 100) × 1.5`. Score ≥ 7.0 → Approved · below routes to Manual QC.
- Gates:
  - Auto QC ≥ 7.0 to ship
  - Identity preservation enforced · face change penalty −4.0 · background change −3.0 · new regression −2.0 each
  - Realism weighted: Human Realism 55% · Product Details 30% · Scene Composition 15%
  - Current crop-extraction pipeline at 8.06/10 (Note §5)

#### §06 · Linked platforms (drop "Impetus " prefix per agents-spec D21)
- AI Photoshoot · `/impetus/ai-photoshoot/` · *Primary execution surface*
- PixelBin · `/pixelbin/` · *Resolution optimisation + CDN delivery layer*
- IntelliLoom · `/impetus/intelliloom/` · *Reads design + range outputs upstream of shoot*

### B · `/agents/` index (updated)

- Hero `total_agents: 7` · subhead revised to *"7 agents shipping in v1, executing across Plan, Buy and Sell."*
- Sell band gains 3rd card: AI Photoshoot Agent (alongside Marketing Agent, AI Cataloging Agent).
- Stat tile · `workflows_at_l4: 7`.

### C · `/impetus/` §03 PATH TO L4 (canonical injector)

Same pattern as today — `<table class="grid-table">` rendered between `<!-- PATH-TO-L4-START -->` markers. Adds:
- 5th column header: **Next milestone**
- Per-row: `<td><span class="cap-num">{next_milestone}</span></td>` — picks up monospace token already in use for the L4 pill alongside.
- 4th row: AI Photoshoot Agent · `Live` · `L4` · `28-May-2026 · Ethnic wear pipeline …` · *"Flat-lay or mannequin product image → on-model 4K catalogue shoot …"*
- Foot-link inside §03 paragraph: *"See the 3-week build plan ↓"* anchoring to `#path-to-l4-buildplan`.

### D · `/impetus/` §04 PATH TO L4 · the build plan (new inline section)

Hand-authored. Inserted after `<!-- PATH-TO-L4-END -->` marker, before existing Design Portfolio section.

- Section label: `04 · PATH TO L4 · the build plan`
- ID anchor: `id="path-to-l4-buildplan"`
- H2: *"How Impetus gets there. Reference date 04-May-2026."*
- Lead paragraph: *"Three projects, one Go/No-Go gate. Pivot to category-led planning · AI Photoshoot category expansion · AI Design pod completion. Status against the chairman-facing build plan as of 03-May-2026."*
- Honesty register note (small text, var(--ink-muted)): *"Reference date 04-May-2026 — Day-0 baseline. Today's date 03-May-2026, so the build window starts tomorrow."*
- Up-link: `↑ §03 Path to L4` anchoring to `#path-to-l4`.

**3 project cards** — each card is a `<details>` block summary-row that expands to show the full deliverable table. Default: Card 1 expanded, Cards 2-3 collapsed.

#### Card 1 · Cortex · Pivot to Category-Led Planning
- Header strip: pill `Building` · `28 deliverables` · `Day-0 04-May` · `Go/No-Go 25-May` · `3-week build`
- Sub-tables in order:
  - **Pre-work** (2 rows · `Pre-req` pill · due 04-May)
  - **Week 1 · Foundation** (8 workstreams · `Planned` pill · 05-May → 11-May)
  - **Week 2 · Experience & Downstream** (9 workstreams · `Planned` pill · 12-May → 18-May)
  - **Week 3 · Test, Validate, Train** (8 workstreams + 1 milestone · 19-May → 25-May)
  - **Post Go-Live** (2 workstreams · 26-May onwards)

#### Card 2 · AI Photoshoot · Category & Pipeline Expansion
- Header strip: pill `Live` · `Pipeline 10/10 Live` · `11 categories: 7 Live · 3 Partial · 1 Upcoming` · `Ethnic Wear 28-May`
- Sub-tables:
  - **Pipeline (10 steps)** — all `Live` · numbered 01-10
  - **Category coverage (11 rows)** — with status pill per row · ethnic wear shows date `28-May-2026`
  - **Execution track record (2 rows)** — Trends Reboot 47,473 images · Lingerie pipeline unlock
  - **What's next (6 items)** — Ethnic Wear (28-May) · Washed Denim (TBD post-May) · Pipeline Stitching (Live) · Segmentation (01-Jun) · Auto-Edit at scale (01-Jun) · Continuous accuracy

#### Card 3 · AI Design Agent · 43 Pod Completion
- Header strip: pill `Live` · `Pipeline 8/8 Live` · `Pods: 28 Live · 5 Partial · 7 Upcoming · 3 N/A`
- Sub-tables:
  - **Pipeline (8 steps)** — all `Live`
  - **Men's Apparel (Pods 1-9)** — 6 Live · 2 Partial (Pods 7, 8) · 1 N/A (Pod 9)
  - **Women's Apparel (Pods 10-18)** — 5 Live · 3 Partial (Pods 11, 15, 17) · 1 N/A (Pod 18)
  - **Kids Apparel (Pods 19-21)** — 3 Live
  - **Footwear & Accessories (Pods 22-28, 34)** — 2 Partial · 4 Upcoming
  - **Quick Fashion (Pods 29-33)** — 3 Live · 2 Upcoming
  - **Premium / BTL & Luxury (Pods 35-43)** — 5 Live · 2 Upcoming · 1 Partial · 1 N/A
  - **Execution track record (2 rows)** — Trend Business 718 designs · Superdry SDX 20 launches
  - **What's next · Improvements** (3 windows: 21-25 May · 25-28 May · 28-30 May)
  - **What's next · Strategic** (5 items: Variation Engine · Premium via Variations · Closed Loop · Delta Categories · Eval-driven)

#### Status legend (footer of §04, small text)
`Live` · `Partial` · `Upcoming` · `Pre-req` · `Milestone` · `Planned` — pill samples + verbatim definition from xlsx legend.

### E · Renumber existing §04 → §05
`04 · Design portfolio · what Impetus has shipped` → `05 · Design portfolio · what Impetus has shipped`. Single label edit. No downstream references.

---

## 4. Data model

### A · `data/agents/ai-photoshoot.yaml` (new)

Identical schema to `data/agents/cortex-planning.yaml`. Notable choices:

```yaml
slug: ai-photoshoot
name: AI Photoshoot Agent
sub_title: "Flat-lay or mannequin product image → on-model 4K catalogue shoot in 2-4 minutes, with autonomous detection, surgical edit, and Ajio-standard delivery."
status: live
status_label: Live
track: sell
autonomy_level: L4
primary_workflow: "Catalog Photoshoot"

primary_platform:
  name: "AI Photoshoot"
  route: "/impetus/ai-photoshoot/"

stats:
  - { label: "Trends Reboot delivered", value: "47,473", context: "images for Ajio · 2,975 styles · 3,957 products" }
  - { label: "Shots per product",       value: "12",     context: "across 12 camera view types" }
  - { label: "Auto QC score",           value: "8.06/10", context: "current crop-extraction pipeline" }
  - { label: "Workflow level",          value: "L4 Agentic", context: "Detect → Edit → Check loop" }

# workflow_svg: hand-authored, 3-zone layout matching cortex-planning.yaml
# workflow_steps: 10 entries verbatim from Note §2
# data: 5 sources, refresh per-job, KPIs moved
# patterns: Tool Calling · Multi-Agent Orchestration · Wide Research · Context Engineering · Observability · Evals
# evals: in-production, scoring formula + identity gates
# in_flight: 28-May (Ethnic Wear), 01-Jun (Segmentation, Auto-Edit at scale)
# linked_platforms: AI Photoshoot, PixelBin, IntelliLoom
# source_citations: AI_Photoshoot_Note_v1.docx + F&L AI Projects.xlsx
```

### B · `data/agents/_catalog.yaml` (updated)

```yaml
hero:
  total_agents: 7              # was 6
  workflows_at_l4: 7           # was 6
  subhead: |
    7 agents shipping in v1, executing across Plan, Buy and Sell. Each maps to one or more Reliance platforms. Each carries data, design patterns, and evals. More agents to follow.

order:
  plan: [cortex-planning, retail-vista, category-intelligence]
  buy:  [trend-to-design]
  sell: [agentic-marketing, ai-cataloging, ai-photoshoot]   # added
```

### C · `data/agents-x-platforms.yaml` (updated · two changes)

**Change 1 · add `ai-photoshoot:` block:**
```yaml
ai-photoshoot:
  name: "AI Photoshoot Agent"
  state: Live
  target_rung: L4
  deployments:
    - platform: impetus
      unlocks: "Flat-lay or mannequin product image → on-model 4K catalogue shoot in 2-4 minutes, with autonomous detection, surgical edit, and Ajio-standard delivery."
      next_milestone: "28-May-2026 · Ethnic wear pipeline (kurtas, kurta sets, ethnic dresses)"
```

**Change 2 · add `next_milestone:` to existing Impetus deployments:**
```yaml
cortex-planning.deployments[0].next_milestone: "25-May-2026 · Pilot Hit/Year Go/No-Go (category-led pivot)"
trend-to-design.deployments[0].next_milestone: "30-May-2026 · Saree drape (Pod 15) + Indian designer (Pod 42) + sherwani craft (Pod 7) improvement window"
category-intelligence.deployments[0].next_milestone: "—"
```

(Granary deployment for cortex-planning gets `next_milestone: "—"` — no Granary-scoped roadmap in source · honest blank.)

### D · `tools/inject_path_to_l4.py` (extended)

Two changes:
1. `parse_registry()` already captures arbitrary `key: value` pairs into the deployment dict — no change needed. The new `next_milestone:` field flows through automatically.
2. `_agents_for_platform()` (line 158) returns dicts; add `"next_milestone": d.get("next_milestone", "—")` to the return.
3. Grid-table render (line 263-282): add 5th `<th>Next milestone</th>` and per-row `<td>{next_milestone}</td>`.
4. Update the "agents close the gap" `pcap` paragraph to append `<a href="#path-to-l4-buildplan">See the 3-week build plan ↓</a>` only for `platform == "impetus"`.

The platform-card path (single-agent platforms: JCP, UCP, Granary) is **not** modified in v1 — those agents have no source-grounded date. Schema supports the field; renderer just doesn't surface it. Mark as a v2 follow-up.

### E · `impetus/index.html` (hand-edit)

- §03 block is auto-rebuilt by the injector — no direct edit.
- New §04 block · static HTML, ~250-350 lines · uses `<details>` for collapsible cards · reuses existing `pill pill-live` / `pill-build` / `pill-phase2` classes from `style.css`. New pill variants if needed (`pill-pre`, `pill-milestone`) added inline as scoped `<style>` block at top of section · or fall back to existing classes (preferred).
- Existing §04 label edit · `04 ·` → `05 ·`.

---

## 5. Asset pipeline

No new assets in v1. The AI Photoshoot agent page renders fully from inline SVG (workflow diagram) + text. The §04 build plan section is text/table only — no diagrams, no screenshots.

Defer for v2:
- AI Photoshoot output gallery thumbnail on the agent page §06 (link to `/impetus/ai-photoshoot/` already serves this surface)
- Architecture SVG (per agents-spec D22 — architecture metadata stays in YAML, not rendered)

---

## 6. Navigation wiring

- **No new top-level routes.** `/agents/ai-photoshoot/` lives under the existing `/agents/` parent — no menu changes.
- **Impetus mega-menu** — no change. AI Photoshoot is already listed under Impetus sub-platforms (`/impetus/ai-photoshoot/`).
- **`/agents/` index card grid** — auto-renders the 7th card from `_catalog.yaml` order block.
- **`/impetus/ai-photoshoot/` backlink** — optional v1 addition · "Powered by AI Agent → AI Photoshoot Agent" pill near hero. Defer if risky.
- **Anchor cross-links** — §03 → §04 via `<a href="#path-to-l4-buildplan">` foot-link · §04 → §03 via `<a href="#path-to-l4">` up-link.

After all edits run:
```bash
python tools/inject_chrome.py --check       # nav drift gate · must exit 0
python tools/inject_path_to_l4.py --check   # registry drift gate · must exit 0
```

---

## 7. Build / verify

```bash
# 1. AI Photoshoot agent page
.venv/bin/python tools/build_agents.py ai-photoshoot
.venv/bin/python tools/build_agents.py --index

# 2. Path-to-L4 sweep · syncs §03 milestone column on Impetus + Deployed-in on agent pages
python tools/inject_path_to_l4.py --dry
python tools/inject_path_to_l4.py
python tools/inject_path_to_l4.py --check       # must exit 0

# 3. Nav/footer gate (no nav change expected)
python tools/inject_chrome.py --check           # must exit 0

# 4. Local server walk-through
python3 -m http.server 8765
# DevTools console: sessionStorage.setItem('fyndrrl_auth_v1', '1'); location.reload();
```

**Verify checklist:**
- `http://localhost:8765/agents/` → 7-card grid · AI Photoshoot in Sell band
- `http://localhost:8765/agents/ai-photoshoot/` → all 7 sections render · SVG draws cleanly · Deployed-in block populated
- `http://localhost:8765/impetus/` → §03 has 4 rows + Milestone column with dates · foot-link to #path-to-l4-buildplan works
- `http://localhost:8765/impetus/` → §04 build plan renders · 3 cards · expand/collapse works · status legend shows
- `http://localhost:8765/impetus/` → §05 Design Portfolio (renumbered) still works
- Honesty register: §04 lead reads correctly · today (03-May) vs Day-0 (04-May) called out

Use Chrome DevTools MCP to capture before/after of `/impetus/` §03 + §04 and the new `/agents/ai-photoshoot/` page.

---

## 8. Phased delivery

| Phase | Scope | Time |
|---|---|---|
| **P1 · Spec** | This doc | 30 min (now) |
| **P2 · Agent YAML** | `data/agents/ai-photoshoot.yaml` · 7 sections · workflow SVG (hand-authored) · stats · patterns · evals · in_flight · linked_platforms · source_citations | ~2 hr |
| **P3 · Catalog + registry updates** | `_catalog.yaml` · `agents-x-platforms.yaml` (new agent + milestone field) · injector update | ~45 min |
| **P4 · Build + sweep** | `build_agents.py ai-photoshoot` + `--index` · `inject_path_to_l4.py` | ~10 min |
| **P5 · §04 build plan section** | Hand-edit `impetus/index.html` · 3 collapsible project cards · status legend · anchors | ~2 hr |
| **P6 · Verify** | Local server walk-through · DevTools MCP screenshots · drift gates · honesty checks | ~30 min |

**Total: ~6 hr** in one working session.

---

## 9. Decisions

1. **D1 · Roadmap surfacing · all-inline on /impetus/** (user sign-off 03-May). Three project cards in a new §04 on the Impetus index page. No deep `/impetus/path-to-l4/` route in v1. Trade-off: page gets longer · revisit in v2 if scroll becomes unwieldy. Alt rejected: separate deep route (would split the §03→§04 read flow).
2. **D2 · Category Intelligence milestone column · honest blank** (user sign-off 03-May). Show `—` rather than fabricate or pull from non-source state. Blank > inferred when the question is "by when?".
3. **D3 · Cards collapsible via `<details>`, Card 1 default-expanded.** Keeps the section scannable; the chairman roadmap is real detail (28 + ~25 + ~50 rows). Apex reader scans the summary strip; opens what they want.
4. **D4 · No new pill colours.** Reuse `pill-live` / `pill-build` / `pill-phase2` from `style.css`. Map xlsx statuses: Live → `pill-live` · Partial → `pill-build` (yellow) · Upcoming → `pill-phase2` (purple/blue) · Pre-req → `pill-build` · Milestone → `pill-live` (green badge) · Planned → neutral pill. If `pill-pre` doesn't exist and the visual collapses, add a single one-off scoped style; do **not** sprawl new tokens.
5. **D5 · §04 sits between §03 and §05 (formerly §04).** Renumber existing Design Portfolio. The L4 narrative (where → how → when) belongs contiguous; the design portfolio is the "what we shipped" coda after.
6. **D6 · AI Photoshoot agent shipped at status `Live`, autonomy `L4`.** Note describes "fully agentic" with autonomous Detect → Edit → Check loop · 47,473 images delivered. Honest fit. (Cortex Planning sits at `Building` because Plan of Record is internal-pilot only; AI Photoshoot has shipped output to Ajio.)
7. **D7 · Honesty note in §04 lead** · "Reference date 04-May-2026 · Day-0 baseline. Today 03-May-2026, build window starts tomorrow." Reader should never wonder why "Planned" rows have no progress yet.
8. **D8 · Milestone column on platform-card render (JCP, UCP, Granary) deferred to v2.** Schema in `agents-x-platforms.yaml` supports it; renderer change is small. Defer because no source-grounded dates exist for those agents today.
9. **D9 · `/impetus/ai-photoshoot/` platform-page backlink optional.** Adds a "Powered by AI Agent → " pill if it slots cleanly into the existing hero. Skip if it requires structural changes — backlink is also covered by the agent page's §06 Linked Platforms going the other way.
10. **D10 · No new top-level route, no nav-menu changes.** Keeps the change surgical. `/agents/ai-photoshoot/` is auto-discoverable from `/agents/` index and from the Impetus §03 Path to L4 link.

---

## 10. Out of scope (v1)

- Deep `/impetus/path-to-l4/` route (per D1).
- Milestone column on JCP / UCP / Granary §03 cards (per D8).
- Architecture SVG for AI Photoshoot (per agents-spec D22 — metadata stays in YAML).
- Auto-rebuild of §04 from `data/impetus-l4-roadmap.yaml` (defer to v2 if dates start changing weekly).
- AJIO ZIP / JIIA Kaily-platform agents (still v2 per agents-spec D24).
- Output gallery on the agent page (the platform page already serves this).
- Sources block on either page (never per CLAUDE.md always-remove rule).

---

**End of spec.** Ready for build.
