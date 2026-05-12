# AI Agents Catalog · Spec

**Status:** v0.8 · 2026-05-02 · **draft for sign-off** (v0.8 · simplification pass · drop §04 Architecture · drop §07 Status · drop ZIP/JIIA · D22 · D23 · D24)
**Owner:** Kushan Shah
**Route:** `/agents/` (new) + `/agents/<slug>/` × 17
**Source content:** `docs/agent-catalog-notes-compilation/` + `docs/accenture-2026-04-16-compilation/` + `~/Documents/work/trend-engine/` (Category Intelligence) + `kaily/` page + `docs/kaily-spec.md`
**Narrative anchor:** Farooq's *Operationalizing Autonomous Commerce for Retail* (15-Apr-2026), §4 *"Details of AI Agents"* — the canonical paper that maps AI agents to L4 (Agentic) workflows across Plan / Buy / Move / Sell. The Accenture deck slide 12 names the **6 Impetus AI Agents** verbatim. The Agentisation note adds the 6 agentised workstreams with named DRIs and dates.
**Inherits from:** `docs/website-orientation-spec.md` · `docs/impetus-restructure-spec.md` (15-platform precedent) · register copy via `website-tone-of-voice` skill

---

## 1. Why this page exists

**Audience.** RIL Apex leadership (MM Sir level). Copy must be apex-readable: factual, scannable, no marketing voice, no Fynd self-praise, names where they matter, claims that survive challenge.

**Gap to close.** Today the register answers "what platforms are deployed" (Impetus, JCP, Granary, etc.). It does **not** answer the parallel question Apex is asking after Farooq's Apr-15 paper landed: *"What AI Agents are running, at what level of autonomy, and how do we know they work?"* The 6-agent slide 12 of the Accenture deck and Paper 4 (§4 Details of AI Agents) of Farooq's note are the canonical inventory — they have no home on the site.

**Why this belongs in the apex register.** Three reasons:
1. **It's the unit of work that matters now.** Platforms are the substrate; agents are what executes. The autonomy ladder (L0 → L5) is a per-agent question, not a per-platform question.
2. **It de-duplicates the narrative.** Today "Trend-to-Design" appears on `/impetus/intelliloom/`, in the Cortex page, and in the Accenture slide deck — three different framings, no canonical detail page. The Catalog is the canonical surface; platform pages link to it.
3. **It carries the eval honesty contract.** Each agent gets one place where data, design patterns, and evals live — so an Apex challenge ("how do you know it works?") has a single page to answer to.

---

## 2. Source inventory

### A · Primary canonical sources

| Source | Type | Path | Key facts |
|---|---|---|---|
| Farooq · Operationalizing Autonomous Commerce for Retail | PDF · 31p | `docs/agent-catalog-notes-compilation/Operationalizing_Autonomous_Commerce_for_Retail.pdf` | §1 Autonomy Ladder L0-L5 · §1.4 21-workflow autonomy matrix · §2 35 data sources / 67 activities / 120 SOPs · §3 Command Centre architecture · **§4 Details of AI Agents · the canonical agent inventory** |
| Agentisation of an Organization | docx | `docs/agent-catalog-notes-compilation/Agentisation of an Organization.docx` | 6 agentised workstreams with **named DRIs and dates** (Chaitali M, Aushin G, Salman S, Mehul H, Saumil D, etc.) · Outcome / Workflow / Platform Capabilities / Execution Plan per agent · Appendix B = **10 design-pattern primitives** (tool calling, MCP, context engineering, agent memory, context graphs, wide research, deep agents, multi-agent orchestration, observability, evals) — the building-blocks vocabulary the Catalog is built on |
| Accenture deck · 16-Apr-2026 · slide 12 | pptx | `docs/accenture-2026-04-16-compilation/INDEX.md §3` | **The 6 AI Agents verbatim**: Trend-to-Design · Planning Agent (Cortex) · Agentic Marketing · Retail Vista · Retail Jarvis · Ask Impetus — *"Use for: `/impetus/` overview should ship this verbatim 6-card grid"* (per INDEX) — we elevate it to the standalone Catalog instead |

### B · Per-agent deep-dives

| Source | Type | Path | Powers |
|---|---|---|---|
| AI Design Agent Note v1 | PDF · 4p | `docs/agent-catalog-notes-compilation/AI_Design_Agent_Note_v1.pdf` | Trend-to-Design Agent · 8-step pipeline (Brief → Context → Artwork → Garment → Review → Costing → Variation → Deliver) · 43 category pods coverage map · **718 designs in <2 days** for Trend business · ~60% selection rate |
| Costing Agent Blueprint v4 | txt | `docs/agent-catalog-notes-compilation/Costing_Agent_Blueprint_V4.txt` | Costing Agent · production architecture · **45-80s vs 2-3hr manual · 85%+ accuracy · 751K+ pricing records · 77+ garment categories** · Temporal workflow · Gemini + GPT-5 + PostgreSQL · DRI Jitesh Rajpal |
| Autonomous Marketing Multi-Agent Framework | docx | `docs/agent-catalog-notes-compilation/Autonomous_Marketing_Platform_Multi_Agent_Framework.docx` | Agentic Marketing Agent · **11-agent topology** (Meta-Orchestrator + 9 Domain Agents + Compliance) · GCP-native · 30/60/90 roadmap · DRIs Saumil D / Prem N / Amogh D |
| RetailVista Agentic Platform Writeup | docx | `docs/agent-catalog-notes-compilation/RetailVista_Agentic_Platform_Writeup.docx` | Retail Vista · Opportunity Engine + Opportunity Explorer + Workspace Agent · H3 spatial primitives |
| RetailVista Business Overview | docx | `docs/agent-catalog-notes-compilation/RetailVista_Business_Overview.docx` | Retail Vista · 61 curated datasets · India basemap · DRIs Salman S / Saumil D |
| TIRA Catalog Enrichment Evals | PDF · 12p | `docs/agent-catalog-notes-compilation/[External]Reliance - TIRA Catalog Enrichment Evals.pdf` | AI Cataloging Agent · external evaluation methodology and results |
| Evals for AI catalog | PDF · 4p | `docs/agent-catalog-notes-compilation/Evals for AI catalog.pdf` | AI Cataloging Agent · internal eval framework |
| AI catalog enrichment workflow diagram | PNG | `docs/agent-catalog-notes-compilation/ai-catalog-enrichment-workflow.png` | AI Cataloging Agent · architecture diagram |
| Category intelligence workflow diagram | PNG | `docs/agent-catalog-notes-compilation/category-intelligence-workflow-diagram.png` | **Category Intelligence Agent** workflow visual (Tier A — extract & embed) |
| Trend Engine repo | code + PDFs | `~/Documents/work/trend-engine/` (outside repo) | **Category Intelligence Agent** deep-dive: 7-step pipeline (Brief → Research → Images → Build → Polish → Verify → Audit → Ship) · 5 review checkpoints · 40-50pp evidence-tagged PDF reports per category × season × geography · 31 automated quality checks · powered by Fynd Create · `midi-dress-ss27-india` worked example shipped |
| Kaily platform page + spec | HTML + spec | `kaily/index.html` + `docs/kaily-spec.md` | **ZIP** + **JIIA** + Netmeds Assistant — agent instances. Kaily is the agent-**builder** platform; the agents themselves are catalog entries. Kaily page stays the platform home; `/agents/zip/` and `/agents/jiia/` are the agent-instance detail pages. Internal architecture/eval detail thin in v1 — ship with public-facing stats and roadmap stub |

### C · Cross-link sources (existing pages we'll wire to)

Confirmed live: `/impetus/cortex/` · `/impetus/intelliloom/` · `/impetus/plm/` · `/impetus/costing-engine/` · `/impetus/intelliverse/` · `/impetus/uvp/` · `/impetus/ai-photoshoot/` · `/impetus/master-hub/` · `/retail-vista/` · `/retail-jarvis/` · `/ucp/` · `/forge/` · `/hirefirst/` · `/pixelbin/` · `/jcp/cataloging/`. Every agent page routes to ≥1 of these.

### Aggregate KPIs derivable from source

- **17 named agents** across Plan / Buy / Move / Sell / Customer / HR
- Live · Building · Scoping counts locked in P2 (each YAML carries the status)
- **5 of 21 retail workflows reach L4 (Agentic)** in the 90-day plan (Farooq §1.5: *"29% reach L4"*)
- **35 data sources · 67 activities · 120 SOPs** (Farooq §2 — the substrate every agent draws from)
- Per-agent anchor stats: 718 designs in <2 days · 45-80s costing · 15 days → 5 hours cataloging · 90% design-time reduction (Superdry SDX) · 88% positive engagement (ZIP) · 11 specialized agents (Marketing) · 8-step pipeline (AI Design)

---

## 3. Page structure

Two distinct surfaces:

**A · `/agents/` index** — catalog summary view, all agents on one page
**B · `/agents/<slug>/` × ~14** — homogeneous detail-page template, every agent identical shape

### A · `/agents/` index page

#### §0 · Eyebrow + Hero
- Crumb: `Home / AI Agents`
- Section label: `AI AGENTS · CATALOG · LIVE`
- H1: **AI Agents.**
- Subhead: *"17 agents executing across Plan, Buy, Move, Sell, Customer and HR. Each maps to one or more Reliance platforms. Each carries data, design patterns, and evals."*
- Stat tiles (5):
  - **17** AI Agents catalogued
  - **Live · Building · Scoping** counts (lock in P2 once each YAML's status is set)
  - **5 of 21** retail workflows at L4 (Agentic)
  - **35** data sources · 67 activities · 120 SOPs
  - **L0 → L5** autonomy ladder (link to `/autonomous/`)

#### §01 · How to read this catalog
- Component: 3-column strip
- Three short blocks:
  - **What an "AI Agent" means here** — verbatim from Farooq §1.3 / Appendix B vocabulary
  - **The autonomy ladder** — L0 manual → L5 autonomous · per-agent target level (link to `/autonomous/`)
  - **The honesty contract** — Live = production today · Building = active dev with date · Scoping = problem framed, no code

#### §02 · The 14 agents · grouped by value-chain stage
- Component: 4-band card grid (Plan · Buy · Move · Sell · HR cross-cutting)
- One card per agent. Each card shows:
  - Agent name + 1-line description
  - Status pill (Live / Building / Scoping)
  - Autonomy level pill (L2 / L3 / L4)
  - Powered-by-platform chip (clickable → platform page)
  - Anchor outcome stat (e.g., "718 designs in <2 days")
  - "View detail →" link to `/agents/<slug>/`

Order — **17 agents across 6 tracks**, leading with the most-Live customer-facing AI:
- **Customer** (2) · ZIP (AJIO) · JIIA (JioMart) — *agent instances built on the Kaily agent-builder platform · `/kaily/` is the platform page · the catalog hosts the deployments*
- **Plan** (4) · Ask Impetus · Cortex Planning Agent · Retail Vista · Category Intelligence
- **Buy** (3) · Trend-to-Design · Costing Agent · Procuro
- **Move** (2) · IntelliMake · Agentic Control Tower
- **Sell** (5) · Retail Jarvis · Agentic Marketing · AI Cataloging · AI Photoshoot · Generative Media
- **HR** (1) · Orion (HireFirst)

#### §03 · The autonomy matrix · where each agent sits today
- Component: compressed 21-workflow × L0-L5 matrix from Farooq §1.4 — **same diagram already on `/autonomous/`** (reuse `assets/autonomous/matrix-1.jpg`)
- Cells coloured by current state; each agent's name pinned to the workflow it governs
- One paragraph framing: *"5 of 21 workflows reach L4 in the 90-day plan. The remaining 16 sit at L2-L3 deliberately — strategy stays human, brand stays human-curated, compliance stays human-accountable."*

#### §04 · The 10 building blocks · how every agent is constructed
- Component: 5×2 grid of pattern cards (verbatim from Agentisation Appendix B)
- Tool Calling · Standard Tool Interfaces (MCP) · Context Engineering · Agent Memory · Context Graphs · Wide Research · Deep / Hierarchical Architecture · Multi-Agent Orchestration · Observability · Evals
- Each card: 1-line definition + which agents use it most heavily
- Cards link to a stable anchor on the relevant agent detail page

#### Footer
Standard footer block. No author/version line per the canonical convention. **No §Sources section** — provenance lives in inline source eyebrows on individual claims, figure captions on screenshots, and the YAML's `source_citations:` field as developer-facing provenance metadata. Per tone-of-voice §3 (rule established 2026-05-02).

---

### B · `/agents/<slug>/` detail page · homogeneous template

Every agent gets the same 9 sections in the same order. Empty sections render as "Pending" rather than being dropped, so the template stays comparable.

#### §0 · Eyebrow + Hero
- Crumb: `Home / AI Agents / <Agent Name>`
- Section label: `AI AGENTS · <SLUG IN CAPS> · <STATUS>`
- H1: **<Agent Name>.**
- Sub-title: 1-line role (e.g., *"AI Business Analyst — answers "why," quantifies impact, recommends next best fix."*)
- Status pills row:
  - Status: `Live` / `Building` / `Scoping`
  - Track: `PLAN` / `BUY` / `MOVE` / `SELL` / `HR`
  - Autonomy: `L2` / `L3` / `L4` (link to `/autonomous/`)
  - Powered by: `→ Cortex` / `→ Retail Vista` / etc. (clickable)
- Stat tiles (3-5): anchor outcome numbers from source, verbatim

#### §01 · The job to be done
- Component: 3-block strip
- **The pain** (1 short paragraph) — what the operator does today without the agent
- **What the agent does** (1 paragraph) — verbatim from source's Outcome bullets
- **What the human still does** (1 paragraph) — intent / exceptions / approvals · the autonomy contract

#### §02 · How it works · the closed-loop workflow

**Uniform shape: numbered step strip on every agent page.** 4-8 step cards in HTML/CSS, each with a step number, a verb-led title, and a 1-line detail (verbatim from the Agentisation doc's "Workflow" bullets). Renderer reads the `workflow_steps:` array from YAML — identical component on every page.

**Optional visual above the step strip** — only when source provides one. Don't fabricate diagrams; an Apex reader can tell. The honesty contract beats the visual contract. Tiered by what source actually offers:

| Tier | Agents | Visual | Asset action |
|---|---|---|---|
| **A · real diagram in source** | Trend-to-Design · AI Cataloging · (Category Intelligence if D3 flips) | Polished diagram extracted from PDF / PNG | `pdftoppm` extract + crop · save to `assets/agents/<slug>/01-workflow.jpg` |
| **B · UI screenshot showing workflow** | Cortex Planning · Agentic Control Tower · Retail Jarvis · Agentic Marketing | Existing Accenture s14 / s15 / s25 / s37 screenshot | `workflow_image:` points at existing CDN URL — zero extraction |
| **C · ASCII flow in source** | Costing Agent | Render the ASCII as a styled `<pre>` block — looks technical-honest | No extraction; embed as code block above step strip |
| **D · prose only** | Ask Impetus · Procuro · IntelliMake · AI Photoshoot · Generative Media · Orion | None — step strip alone | Skip image; step strip is sufficient |

YAML adds two optional fields:
```yaml
workflow_image: "/assets/agents/trend-to-design/01-pipeline.jpg"   # Tier A/B
workflow_image_caption: "Source · AI Design Agent Note v1 · p. 1"
workflow_image_kind: image | cdn | ascii                           # ascii uses workflow_ascii field
workflow_ascii: |                                                  # Tier C only
  ┌────────────────┐
  │ USER INPUT     │
  └─────┬──────────┘
  …
```

Renderer logic: if `workflow_image` set → render image + caption + lightbox. If `workflow_image_kind: ascii` → render `<pre>` block. If neither → step strip alone. Owner column on the step strip names who reviews/approves at each gate (drawn from Agentisation doc's roadmap tables).

#### §03 · Underlying data
- Component: 2-column table
- Left column · **Data sources** consumed (from Farooq §2 — POS, RFID, OMS, UCP, Anytrack, etc.)
- Right column · **Data classification** (Human-Created / Machine-Created / Machine-Readable)
- Row 1 · key entities · refresh cadence (real-time / minute / hour / shift / daily — from the Retail Clock in Accenture s4)
- Row 2 · KPIs the agent moves (verbatim from §2.1.4-2.1.9 of Farooq)

#### §04 · How it's built · architecture
- Component: prose + tech-stack chips
- Agent topology: single-agent / hierarchical / multi-agent (cite the topology pattern)
- Models: Gemini / Claude / GPT-5 / VLM (verbatim where source specifies)
- Tools / MCP integrations (named)
- Memory layers used (short-term / episodic / semantic / procedural)
- Where it runs: GCP Vertex / AWS / on-prem
- Optional architecture diagram (cataloging + costing have these in source)

#### §05 · Design patterns used
- Component: pattern chips with one-line "how this agent uses it"
- Drawn from the 10-pattern vocabulary (§04 of index page). Most agents use 4-7 patterns.
- Each chip cross-links to the same definition on `/agents/#building-blocks`

#### §06 · Evals · how we know it works
- Component: stat strip + measure table
- For Live agents: current pass rates · golden-test counts · regression-gate thresholds
- For Building/Scoping: planned eval suite + gate criteria + DRI for evals
- AI Cataloging is the worked example — has 2 dedicated eval PDFs in source
- Open question for thinly-evaled agents: stub with **"Eval framework in development · DRI: <name>"** rather than fabricating numbers — see §9 D5

#### §07 · Live for RIL today / In flight / Roadmap
- Component: 3-column strip with status pills
- **Live for RIL today** — brands / formats / store count / volume served
- **In flight** — next milestone with date (DRIs intentionally not surfaced on the page per D15)
- **Roadmap** — beyond 90 days · honest about what's not built

#### §08 · Linked platforms
- Component: card grid · 1-3 cards per agent
- Each card: platform name + 1-line role + clickable link to `/<platform>/`
- E.g., Cortex Planning Agent → `[Cortex]` `[IntelliLoom]` `[Retail Vista]`

#### Footer
Standard footer. **No §Sources section** — see index page §Footer note. Provenance survives inline (workflow steps citing Farooq §1.4, image captions citing Accenture s37, etc.) and in YAML metadata.

---

## 4. Data model

Path: `data/agents/<slug>.yaml` — one YAML per agent. Plus `data/agents/_catalog.yaml` for index-page header config.

```yaml
slug: cortex-planning
name: Cortex Planning Agent
sub_title: "Store-level Plan of Record + continuous, exception-led replanning"
status: build
status_label: Building
track: Plan         # Plan | Buy | Move | Sell | HR
autonomy_level: L4  # L2 | L3 | L4
date: 2026-04-15
source_folder: docs/agent-catalog-notes-compilation/
source_citations:
  - "Farooq · Operationalizing Autonomous Commerce · §4.2 Plan · pp. 30"
  - "Agentisation of an Organization · §3.2 Planning Agent — Impetus Cortex"
  - "Accenture deck · slide 12 · 6 AI Agents · Planning Agent"

# § Hero stat tiles
stats:
  - label: "Workflow level"
    value: "L4 Agentic"
    context: "Space Planning workflow"
  - label: "Replanning cadence"
    value: "Continuous"
    context: "vs monthly today"
  - label: "Output granularity"
    value: "Fixture · slot"
    context: "store-specific VM layouts"

# § 01 · Job to be done
job:
  pain: |
    Today, planning is monthly, spreadsheet-driven, store-agnostic.
    Plans land in stores with assumptions baked in that no longer match
    real space, real inventory, or real demand.
  what_it_does: |
    Builds a store-realistic Plan of Record. Converts targets into
    fixture-level and slot-level VM layouts. Replans on exception, not
    on calendar.
  human_role: |
    Planner sets targets and reviews replans. Agent does not replace
    planning. It makes planning continuous.

# § 02 · Workflow
workflow_steps:
  - step: "Ingest unified inputs"
    detail: "Sales · returns · inventory · margin · targets · store space · VM rules · real-time inventory"
  - step: "Build store-first Plan of Record"
    detail: "WSSI · OTB · assortment · scenario simulation (assortment × intake × price) · select on margin / risk / feasibility"
  # ... etc

# § 03 · Data
data:
  sources:
    - { name: "Impetus", classification: "Mixed", entities: "OTB, Plan of Record, WSSI" }
    - { name: "POS", classification: "Machine-Created", entities: "Sell-through %, ROS" }
    - { name: "SAP F&L", classification: "Mixed", entities: "Stock Positions, Margin" }
  refresh_cadence: "Daily for plan; real-time for exception triggers"
  kpis_moved:
    - "Forecast accuracy"
    - "GMROF"
    - "Aged inventory %"

# § 04 · Architecture
architecture:
  topology: "Hierarchical (Planner → 4 specialist sub-agents → integrator)"
  models: ["Gemini 2.5 Pro", "Claude Opus 4.X"]
  tools: ["WSSI calculator", "Scenario simulator", "VM constraint solver"]
  memory: ["semantic (store traits)", "episodic (prior replans)", "procedural (fallback rules)"]
  runtime: "GCP Vertex AI"

# § 05 · Design patterns used
patterns:
  - { name: "Tool Calling",        usage: "Pulls live OTB · WSSI · stock from Impetus + SAP" }
  - { name: "Context Engineering", usage: "Compresses store traits + active VM rules into per-replan context" }
  - { name: "Agent Memory",        usage: "Episodic memory of prior replans → avoids re-asking solved questions" }
  - { name: "Wide Research",       usage: "Generates N candidate plans, scores on margin × risk × feasibility, picks one" }
  - { name: "Deep / Hierarchical", usage: "Planner delegates to specialist sub-agents per planning dimension" }

# § 06 · Evals
evals:
  status: "in-development"
  approach: "Replay historical seasons; score plan vs actual sell-through and margin."
  dri: "Aushin G + Shahid K"
  gates:
    - "Margin within 2% of best-case manual plan on holdout season"
    - "Replan latency < 4 hours from exception trigger"

# § 07 · Status
live_today:
  body: "Internal pilot on Yousta. Plan of Record generation working end-to-end. Not yet production for any RIL brand."
in_flight:
  - { date: "2026-01-15", milestone: "Cortex Allocation & Redistribution + Merchandise Financial Planning + OTB modules", dris: ["Aushin G", "Shahid K"] }
  - { date: "2026-03-06", milestone: "Range Plan + Buy Plan + Distribution Plan modules · Pre/In-Season forecasting models", dris: ["Aushin G", "Shahid K"] }
  - { date: "2026-04-06", milestone: "Agentic forecasting engine + autonomous workflow execution + Rules Engine", dris: ["Aushin G", "Shahid K"] }
roadmap:
  - "Cross-format cannibalisation detection (L4 ladder cell)"
  - "Unified demand sensing (L5 ladder cell)"

# § 08 · Linked platforms
linked_platforms:
  - { name: "Impetus Cortex",     route: "/impetus/cortex/",      role: "Primary execution surface" }
  - { name: "Impetus IntelliLoom", route: "/impetus/intelliloom/", role: "Reads design + range outputs" }
  - { name: "Retail Vista",        route: "/retail-vista/",         role: "Reads spatial / catchment context" }
```

**Index file `data/agents/_catalog.yaml`:**

```yaml
hero:
  total_agents: 14
  live: 5
  building: 8
  scoping: 1
  workflows_at_l4: 5
  total_workflows: 21
  data_sources: 35
  activities: 67
  sops: 120
order:
  plan:  [ask-impetus, cortex-planning, retail-vista]
  buy:   [trend-to-design, costing, procuro]
  move:  [intellimake, agentic-control-tower]
  sell:  [retail-jarvis, agentic-marketing, ai-cataloging, ai-photoshoot, generative-media]
  hr:    [orion]
```

---

## 5. Asset pipeline

Source `docs/agent-catalog-notes-compilation/` → published `assets/agents/<slug>/`.

### Pass A · workflow / architecture diagrams (the highest-leverage assets)

Per the §02 tiering — extract only Tier A diagrams from source. Tier B uses existing CDN URLs (no extraction). Tier C is inline `<pre>`. Tier D has no image.

**Tier A extractions:**
- `ai-catalog-enrichment-workflow.png` → `assets/agents/ai-cataloging/01-workflow.jpg`
- `category-intelligence-workflow-diagram.png` → `assets/agents/ai-cataloging/02-category-intel.jpg` (or its own agent — see §9 D3)
- AI Design Agent PDF p.1 (8-step pipeline) → `assets/agents/trend-to-design/01-pipeline.jpg` via `pdftoppm` + PIL crop

**Tier B references (no extraction):**
- Cortex Planning → `https://socialassets.impetusz0.de/rrl-portfolio/assets/accenture-2026-04-16/slide_14/img_01.png`
- Agentic Control Tower → Accenture slide_15
- Retail Jarvis → Accenture slide_25
- Agentic Marketing → Accenture slide_37 (ZIP) — confirm with user if D9 framing should pull a different slide

**Tier C inline:**
- Costing Agent · ASCII flow → embedded as `<pre class="workflow-ascii">` block in `data/agents/costing.yaml` `workflow_ascii:` field — styled in `style.css` (per D6, settled)

**Reuse for index page:**
- `assets/autonomous/matrix-1.jpg` + `matrix-2.jpg` for §03 of index (no new asset; just reference)

### Pass B · per-agent UI screenshots (where source provides)

- Cortex / Command Centre screenshots already exist at `assets/impetus/cortex/` and `assets/impetus/_accenture/s14/` — reuse via path reference, do not re-host
- Ask Impetus mobile dashboard screenshot exists at `assets/impetus/cortex/ask-impetus-mobile.jpg` — reuse
- Retail Jarvis · pull from `assets/accenture-2026-04-16/slide_25/` (CDN) — no new asset
- AJIO ZIP screenshot at `assets/accenture-2026-04-16/slide_37/img_01.png` (CDN) — reuse for Agentic Marketing

### Pass C · source PDFs hosted for "view source" links

- `Operationalizing_Autonomous_Commerce_for_Retail.pdf` → already hosted at `https://socialassets.impetusz0.de/rrl-portfolio/assets/autonomous/` (verify)
- `AI_Design_Agent_Note_v1.pdf` → `assets/agents/trend-to-design/AI_Design_Agent_Note_v1.pdf` (1.3MB · keep local)
- TIRA + AI Catalog eval PDFs → `assets/agents/ai-cataloging/` (small, keep local)
- Costing Blueprint v4 txt → render as a `<details>` block on costing page · do not host the txt (33KB plain text · reads as a leak)

### GCS mirror

Asset count likely <30 and total <30MB — **no GCS mirror needed for v1**. Keep all assets local. Revisit if §9 D6 (Costing flow rendering) pushes past 100MB.

### Lightbox

Every UI / diagram screenshot wraps in `<a class="js-lightbox">`. Single overlay snippet at end of `<body>`. Per the §6 image-display convention.

---

## 6. Navigation wiring

Per `references/nav-wire-checklist.md`:

- [ ] **Home page card** (`index.html`) — add a new "AI Agents" card in the AI-Native row · 1-line description · "14 catalogued · 5 Live"
- [ ] **Top-nav Tracks mega-menu** — add `AI Agents · catalog` under the **Capability** column, alongside `/autonomous/`. (Pair: `/autonomous/` answers *"the framework"* · `/agents/` answers *"the inventory"*.)
- [ ] **IP Catalog** (`/catalog`) — add Agents as a track entry
- [ ] **Footer "Other tracks"** — strict sweep across ~25 pages (lazy is OK for v1 if tight on time — see §9 D7)
- [ ] **Sibling section indexes** that mention agents:
  - `/impetus/cortex/` — already lists Trend-to-Design, Planning, Marketing as "AI Agents" sub-section · convert each to a clickable link to `/agents/<slug>/`
  - `/impetus/intelliloom/` — Trend-to-Design + AI Design Agent backlinks
  - `/impetus/costing-engine/` — Costing Agent backlink
  - `/impetus/ai-photoshoot/` — AI Photoshoot Agent backlink
  - `/impetus/intelliverse/` — Procuro · IntelliMake backlinks
  - `/jcp/cataloging/` — AI Cataloging backlink
  - `/retail-vista/` — Retail Vista (New Store Opportunity) backlink
  - `/retail-jarvis/` — Retail Jarvis backlink
  - `/ucp/` — Agentic Marketing backlink
  - `/forge/` — IntelliMake backlink
  - `/hirefirst/` — Orion backlink
  - `/autonomous/` — anchor link from each "agent powers this workflow" cell back to the agent page
- [ ] **More mega-menu** — not applicable (Catalog is a Tracks/Capability entry, not a meta-page)

The **bidirectional link** is the load-bearing piece — every platform that hosts an agent gets a "Powered by AI Agent → " card with a clickable link to the agent's catalog page, AND the agent page links back. This satisfies the user's brief: *"each agent maps to a platform hence the detail page needs to route to respective platform pages (and vice versa as well)"*.

### Naming normalization sweep (per D12)

P7 includes a one-time grep-and-rename pass to align every existing reference to the catalog's canonical agent name:

- `grep -rn "Store Intelligence Agent" --include='*.html' --include='*.yaml' --include='*.md'` → rename to `Retail Vista`
- `grep -rn "New Store Opportunity Agent"` → rename to `Retail Vista`
- `grep -rn "In-Store Experience Agent"` → rename to `Retail Jarvis`
- `grep -rn "Customer Listening + Action Agent"` → rename to `Retail Jarvis`
- `grep -rn "Purchase Automation"` → rename to `Procuro` (when it's the agent; leave platform/feature mentions alone)
- `grep -rn "Planning Agent"` (bare) when context = the agent → rename to `Cortex Planning Agent`

Spec docs (`docs/*-spec.md`) and source compilation folders are out of scope — the rename is for **published pages**, not source provenance.

---

## 7. Build / verify

```bash
# Build all 14 agent pages + index
.venv/bin/python tools/build_agents.py

# Build a single agent page
.venv/bin/python tools/build_agents.py cortex-planning

# Local verify
python3 -m http.server 8000
# open http://localhost:8000/agents
# Run §9 verify checklist from website-section-authoring skill
```

`tools/build_agents.py` follows the `tools/build_impetus.py` pattern (proven for 15-platform scale). Single renderer · reads `data/agents/*.yaml` · emits `agents/<slug>/index.html` + `agents/index.html`.

---

## 8. Phased delivery

| Phase | Scope | Time |
|---|---|---|
| **P1 · Spec sign-off** | This doc · resolve §9 decisions · lock the 14-agent inventory | ~1 hr (now) |
| **P2 · Data extraction** | 17 YAMLs · verbatim from sources · DRIs / dates / stats locked · ZIP + JIIA stubs · pull Category Intelligence DRI from trend-engine repo | ~5 hr |
| **P3 · Asset pipeline** | Pipeline + workflow diagrams extracted · cross-refs to existing CDN assets | ~1 hr |
| **P4 · Renderer** | `tools/build_agents.py` · index + detail template · lightbox snippet | ~3 hr |
| **P5 · Index page** | `/agents/index.html` · 14-card grid · autonomy matrix re-use · 10 building-blocks grid | ~2 hr |
| **P6 · Detail pages** | 17 pages × hero + 9 sections · render + verify each | ~4 hr (parallel-friendly with renderer) |
| **P7 · Bidirectional nav wiring + name normalization** | Mega-menu · home card · ~13 platform-page backlinks · `/autonomous/` cross-links · D12 grep-rename sweep across published HTML | ~3 hr |
| **P8 · Verify + polish** | Local server walk-through · tone-of-voice sweep · source-citation audit | ~1 hr |

Total v1: **~20 hr** spread across 3 working sessions (was 17 at v0.2 · +3 for the 3 new agents and the name-normalization sweep).

---

## 9. Decisions

Resolve every open question before drafting copy. **My recommendation in bold**; alternatives listed.

1. **D1 · Route slug** — **`/agents/`** (matches `/autonomous/`, `/forge/`, `/hirefirst/` cadence — short, lowercase, no hyphen). Alt: `/ai-agents/` (more explicit, but every other route assumes "AI" context).
2. **D2 · Status taxonomy** — **3 tiers · `Live` / `Building` / `Scoping`** (matches HireFirst convention). The Agentisation doc uses "Live / In-progress / Scoping" — collapse "In-progress" → "Building" for consistency with the rest of the register.
3. **D3 · Inventory size · LOCKED at 17 agents** (v0.3 · 2026-05-02 user sign-off). Plan: 4 · Buy: 3 · Move: 2 · Sell: 5 · Customer: 2 · HR: 1. Adds since v0.2: **Category Intelligence** (Plan · sourced from `~/Documents/work/trend-engine/`) · **ZIP (AJIO)** + **JIIA (JioMart)** (Customer · Kaily-platform-built deployments). Granary Cortex Planning Agent excluded for v1 (sibling of Impetus Cortex; cross-platform expansion deferred). Marketing's 11 sub-agents stay on the Marketing detail page only.
4. **D4 · Page-template uniformity vs flexibility** — **Strict template, 9 sections, every agent identical shape, "Pending" stub for empty sections.** Apex readers compare across agents; uneven pages defeat that. Alt: per-agent flexibility — rejected because it makes the catalog incomparable.
5. **D5 · Eval section for thinly-evaled agents** — **Render `Eval framework in development · DRI: <name>` rather than fabricate**. Honesty contract beats completeness theatre. Alt: drop the §06 Evals section for those agents — rejected because it creates uneven shape.
6. **D6 · Costing Agent flow diagram** — **Render the ASCII flow as a styled `<pre>` block on the page.** Looks technical-honest, no asset extraction needed. Alt: convert to a polished SVG diagram — defer to v2 if time permits.
7. **D7 · Footer backlink sweep** — **Strict.** ~25 pages get the new "AI Agents" entry in their footer's "Other tracks" list. ~30 min via grep. The catalog is too important to ship with stale backlinks.
8. **D8 · Autonomy-matrix duplication** — **Reuse `assets/autonomous/matrix-1.jpg` + matrix-2.jpg via reference**, do not duplicate. The matrix is the same diagram; one canonical home (`/autonomous/`) plus a referenced thumbnail on `/agents/` is correct.
9. **D9 · "Powered by Impetus" framing** — Agents that live on the Impetus stack should say *"Powered by Impetus Cortex"* (etc.), not *"Built by Fynd"*. The Reliance-facing brand is the platform, not the vendor. Confirmed by `/hirefirst/` and `/granary/` precedent (hides "Orion" / "GranaryOS" codenames from the page).
10. **D10 · Agentic Control Tower vs Cortex** — **Treat as a distinct agent** (own page). It's the exception-orchestration layer of Cortex, but it operates differently (governs Move workflows, not Plan), and Farooq's §4.4 Move section names it specifically. Alt: fold into Cortex Planning page — rejected because it conflates Plan and Move autonomy stories.
11. **D11 · §02 workflow visuals · tiering vs uniform diagrams** — **Tiered: extract real source diagrams (Tier A) · reuse existing Accenture CDN screenshots (Tier B) · inline ASCII for Costing (Tier C) · step-strip only for the rest (Tier D).** Every agent page gets the same numbered step strip; the visual above it is a bonus when source provides one. Rejected: uniform Mermaid/SVG · text-to-image AI · hand-authored SVGs — all fail the honesty contract or the v1 budget. Updated counts post-D3: Tier A = 4 agents (Trend-to-Design · AI Cataloging · Category Intelligence · AI Design pipeline); Tier B = 4 (Cortex · Control Tower · Jarvis · Marketing/ZIP); Tier C = 1 (Costing); Tier D = 8 (the rest).
12. **D12 · Naming · normalize, don't alias.** Each agent on the catalog uses **one canonical name** across the page, the index card, and the platform backlink — no parenthetical aliases like *"also called Store Intelligence Agent"* / *"also known as In-Store Experience Agent"*. The Apex reader should never wonder which name to use. **In-scope normalization sweep** (catalog launch P7): rename references in source pages to match the catalog's canonical name. Locked names: **Retail Vista** (drop "Store Intelligence Agent" / "New Store Opportunity Agent") · **Retail Jarvis** (drop "In-Store Experience Agent" / "Customer Listening + Action Agent") · **Procuro** (drop "Purchase Automation Agent" — Procuro is the Reliance-facing IntelliVerse module name) · **IntelliMake** (Forge MES is the Electronics-vertical sibling, not an alias) · **Cortex Planning Agent** (drop bare "Planning Agent" / "Impetus Cortex" when referring to the agent specifically). Codenames stay only in source-document filenames and git history.
13. **D13 · Kaily as agent-builder · ZIP + JIIA as agent instances.** Kaily is the **platform** that builds customer-facing conversational agents. The catalog hosts the agents themselves: **ZIP** (AJIO deployment · 88% positive engagement · 86% chats helped discovery · 2.6M+ catalog) and **JIIA** (JioMart deployment · 40M+ image catalog · validated at Google Cloud Next '26 keynote 29-Apr-2026). `/kaily/` stays the platform home and links *up* into the catalog. Each agent page links *down* to `/kaily/` as Powered-by. Internal architecture/eval detail will be thin in v1 (no source deck for either deployment yet) — ship with public-facing stats + roadmap stub + a *"Detail expanding · ETA <date>"* note. Netmeds Assistant deferred to v2 (less load-bearing than ZIP/JIIA in current Apex narrative).
14. **D14 · Category Intelligence · Plan track · sourced from Trend Engine.** Source repo at `~/Documents/work/trend-engine/` (outside this repo). Workflow diagram in `docs/agent-catalog-notes-compilation/category-intelligence-workflow-diagram.png` (Tier A). The agent: takes a category × season × geography, runs a 7-step pipeline (Brief → Research → Images → Build → Polish → Verify → Audit → Ship) with 5 review checkpoints, produces a 40-50pp evidence-tagged PDF report with 31 automated quality checks. Powered by Fynd Create. Worked example shipped: Women's Midi Dresses · SS27 · India.
15. **D15 · DRI field dropped (v0.4 user sign-off).** No DRI line on agent cards or detail pages. The Agentisation doc's named owners stay in the spec source as provenance, but never render to the page. Reason: 8 of 17 agents have no source-named DRI; rendering "DRI · TBD" creates incomplete-looking pages, and rendering inferred DRIs from `data/impetus/<platform>.yaml` would be wrong (those are platform owners, not agent owners). Owners live in source-of-truth systems (`/organisation/`, git, JIRA), not on the catalog. YAML data model: drop `dris:` from `in_flight:` entries.
16. **D16 · Customer track first (v0.4 user sign-off).** `/agents/` index orders bands as: **Customer → Plan → Buy → Move → Sell → HR**. Lead with the most-Live customer-facing AI (ZIP / JIIA) — they're what an Apex reader will most viscerally recognize. Back-office L4 follows in value-chain order. HR closes. Reason: scannability + landing impact; the most-deployed agents in the estate sit above the fold.
17. **D17 · Status \(Live/Building/Scoping\) · per-agent, locked on review (v0.4 user sign-off).** I produce 17 YAMLs with my best judgement against source; user flips on review. No automatic preference for Agentisation-strict or Accenture-loose framing.
18. **D18 · No §Sources block on any page (v0.5 user sign-off).** Index page drops §05 Sources; detail-page template drops §09 Sources. Provenance lives in (a) figure captions on public-facing screenshots, (b) the YAML's `source_citations:` field as developer-facing provenance metadata never rendered to the page. Section count: detail page goes from 10 sections (Hero + §01-§09) to 9 (Hero + §01-§08). Index page goes from 6 sections to 5. Matches tone-of-voice §3 rule update of the same day.
19. **D19 · Scrub internal source-document references from body copy (v0.6 user sign-off).** No mention of *"Accenture s37"*, *"Farooq §1.4"*, *"Agentisation §3.2"*, *"per Accenture s4 Retail Clock"*, *"slide 12"*, *"L4 ladder cell · Farooq §1.4 row 1.5"*, *"Public-facing pitch on Accenture s37"*, etc. on any agent page. These are developer-facing artefact names the Apex reader doesn't read and treats as Fynd-internal jargon. Public-facing source mentions (*"Google Cloud Next '26 keynote · 29-Apr-2026"*, *"shown at the Reliance Retail Apex review · 16-Apr-2026"*, *"published live on AJIO.com"*) are credibility-positive and stay. Sweep covers: `stats[].context`, `data.refresh_cadence`, `roadmap[]`, `evals.approach`, `architecture.note_pending`, `workflow_image_caption`. YAML's `source_citations:` field stays as developer-facing metadata, never rendered. Matches tone-of-voice §3 rule update of the same day.
20. **D20 · Inline SVG diagrams in §02 (workflow) and §04 (architecture) · matches the JCP / dark-factory convention (v0.7 user sign-off · revises Mermaid from v0.6).** Every agent page renders **hand-authored inline SVG**, fed by YAML fields `workflow_svg:` and `architecture_svg:`. The SVG matches the JCP `/jcp/index.html` §01 architecture pattern — coloured zones (`<rect rx="14">` zone backgrounds), `<rect>` cards inside, `<text>` labels with `class="zh"` (zone header) / `class="stp-ttl"` (card title) / `class="stp-sub"` (card body), and `<path class="conn">` connectors with `<marker>` arrowheads. Diagrams fold the §03 data sources in as input nodes / cards (the user's *"data points can be part of the diagram"* directive). **Why inline SVG, not Mermaid:** the rest of the register is hand-authored SVG. Mixing in client-side-rendered Mermaid diagrams looks visually distinct (different fonts, different node styles, different stroke weights) and breaks the apex-readable consistency. The cost is real — each diagram is ~150 lines of SVG taking 30-60 min to author per agent. **Trade-off:** diagrams will land per-agent over multiple sessions rather than all at once; no agent page ships without its diagrams complete. Step strip retained as a captioned list *below* the diagram for readers who want to read details. Public-facing UI screenshots (was Tier B in D11) can sit alongside the SVG when relevant. Reference exemplar: `data/agents/cortex-planning.yaml` `workflow_svg:` field — 1200×540 viewBox, three zones (Inputs · Workflow · Outputs), 6-step flow with monitor loop.
21. **D21 · Linked-platform names drop the "Impetus " prefix.** On agent detail pages §08, render *"Cortex"* not *"Impetus Cortex"*; *"IntelliLoom"* not *"Impetus IntelliLoom"*; *"PLM"* not *"Impetus PLM"*. The route (`/impetus/cortex/`) and the page context already establish that these are Impetus sub-platforms — repeating the family name in the card label is noise. Cross-family platforms (Retail Vista, Kaily, JCP, UCP, Forge, HireFirst, PixelBin, Boltic, Ratl) keep their bare names — they were never prefixed. Matches the convention used on `/impetus/index.html` itself (cards there are labelled "Cortex", "IntelliLoom", "PLM", not "Impetus Cortex").
22. **D22 · §04 Architecture section dropped from template (v0.8 user sign-off).** Architecture detail (topology · models · tools · memory layers · runtime) is too internal for the Apex reader. The page is *what the agent does*, not *how it's wired*. Architecture detail stays in the YAML's `architecture:` field as developer-facing metadata; never rendered. Section count: detail page goes from 9 to 8 sections (Hero + §01-§07 → Hero + §01-§06).
23. **D23 · §07 Status section dropped from template (v0.8 user sign-off).** Live / In-flight / Roadmap detail belongs on the linked platform page, not duplicated on the agent page. Reader navigates via §08 Linked Platforms to see status. Removes a recurring honesty-failure mode (past-date In-flight milestones — H3 in the v1 audit). YAML's `live_today:` / `in_flight:` / `roadmap:` fields stay as developer-facing metadata; never rendered. Section count: detail page goes from 8 to 7 sections (Hero + §01-§06).
24. **D24 · Drop ZIP and JIIA from v1 catalog (v0.8 user sign-off · supersedes D13).** Customer-facing agents (Kaily-built deployments) deferred to v2. Reasons: (a) thin internal source — no architecture, no eval framework, no DRI from the Kaily team yet; (b) the `note_pending` "detail expanding" pattern reads as incomplete on a launch catalog; (c) `/kaily/` already exists as the canonical surface for ZIP / JIIA / Netmeds Assistant. Catalog now 15 agents across **5 tracks** (Plan · Buy · Move · Sell · HR). Customer track removed from `_catalog.yaml` band ordering. User has signalled they may further reduce the agent list before ship — current 15 is the upper bound for v1.

---

## 10. Out of scope (v1)

- **Per-agent runtime telemetry** (live trace counts, pass rates piped from Vertex / Databricks). Manual numbers only in v1.
- **Interactive autonomy matrix** (clickable cells linking to agents). Static image with anchored cells in v1; interactive in v2.
- **Agent-to-agent dependency graph** (which agents call which). The Building-Blocks section lists patterns per agent; the dependency graph is a v2 addition.
- **Eval test-suite browser** (clickable list of golden tests per agent). Eval *framework* described in §06; eval *results* surfaced as numbers; the suite browser is v2.
- **Multi-language support** for agent pages.
- **Agent comparison views** ("Show me all L4 agents in Sell" filterable).
- ~~Category Intelligence as a 15th agent~~ — **promoted to v1** (see D3 / D14)
- **Granary Cortex Planning Agent** — defer to v2; sibling of Impetus Cortex Planning Agent. Adding pulls cross-platform scope into a v1 that intentionally stays Impetus + customer-facing.
- **Netmeds Assistant** — defer to v2 per D13; less load-bearing than ZIP/JIIA in the current Apex narrative.
- **Autri Agentic Command Center** — distinct domain (grocery shelf compliance), lives at `/autri/` for v1.
- **NAM ShopOS · 13 future agents** — aspirational; one-line callout on the catalog index *"+13 future agents in NAM scope → /nam/"* but no per-agent pages.
- **Marketing's 11 sub-agents** — stay on the Marketing detail page §04 architecture card; no individual catalog entries.
- **A standalone `/building-blocks/` page** for the 10 design patterns. The grid lives on `/agents/` index for v1; if it grows substantively, lift to its own page in v2.

---

**End of spec.** Awaiting sign-off before implementation.
