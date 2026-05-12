# Boltic page · Build spec

**Status:** v0.6 · 2026-05-01 · **shipped (page at v0.9.8)** — Tira CRM framing reverted to honest placeholder; Urban Ladder live RR case added with 4 in-production workflows
**Owner:** Kushan Shah
**Route:** `/boltic/` (placeholder live; this spec replaces it with the full hub page)
**Source content:** `docs/boltic-notes-compilation/Boltic - Retail Deck  | 2025.pptx` (33 slides)
**Narrative anchor:** Boltic is the AI-Native Workflow Automation OS Fynd brings to Reliance Retail. The deck is generic-for-Retail; this page is **Reliance Retail only** — generic customer logos, third-party brand testimonials, and non-Reliance case studies are stripped. What carries through is the platform itself (workflows, AI Agents, MCP, Serverless, Gateway, Tables, Storage, Monitoring), the retail-shaped use cases it targets, and the real product UI shipped today on Fynd's own production instance.
**Inherits from:** `docs/website-orientation-spec.md` · `docs/hirefirst-spec.md` (canonical single-page restructure template) · `website-tone-of-voice.md` for register.

**Built using:** `.claude/skills/website-section-authoring` (workflow) + `.claude/skills/website-tone-of-voice` (copy register).

---

## 0. Implementation status

| Stage | Deliverable | Where it lands |
|---|---|---|
| 0 raw | Source compilation folder (1 deck, 33 slides) | `docs/boltic-notes-compilation/` |
| 1 spec | This file | `docs/boltic-spec.md` |
| 2 data | Single page · no YAML; copy authored inline (≤6-card hand-author rule from skill) | `boltic/index.html` |
| 3 assets | 6 product screenshots from annexure slides + 1 platform-stack diagram, resized + web-named | `assets/boltic/screens/` + `assets/boltic/diagrams/` |
| 4 build | Hand-authored HTML, full-page rewrite of `boltic/index.html` per §3 | `boltic/index.html` |
| 5 nav | Already wired in mega-menu (`AI-Native` column, `agentic auto` suffix); no nav edits needed | — |
| 6 verify | Local server walk + Chrome DevTools screenshot + console clean | — |

---

## 1. Why this page exists

**Audience.** RIL Apex leadership reviewing the register. Same audience as `/impetus`, `/jcp`, `/granary`, `/hirefirst`.

**Gap to close.** The current `/boltic` page is a placeholder. The 2026-04-30 letter to MM Sir names Boltic as one of three AI-Native agentic-automation platforms (alongside PixelBin and Ratl) on offer to Reliance Retail. The hub page must explain:
- What Boltic is (the workflow automation platform — workflows, AI Agents, MCP, Serverless, Gateway, Tables, Storage, Monitoring)
- Why retail (where it fits in Reliance Retail's operations: sales/replenishment, order/supply chain, customer support)
- Real product evidence (screenshots from the live product, not mockups)
- What's live for Reliance Retail today vs. on the roadmap

**Reliance-only filter.** The source deck is a generic Boltic-for-Retail sales deck. Three categories of source material are deliberately excluded:
- **Customer logo bars** (slide 21's brand grid) — replaced with the Fynd-Reliance frame.
- **Third-party brand case studies** (slide 16 beauty CRM, slide 17 mattress logistics, slide 14 testimonials) — dropped entirely.
- **Workflow / table names that show non-Reliance brand identifiers** (e.g. "PUMA X FYND", "Guess_capi", "puma_clickpost" surfaces from slides 26 and 30) — those screenshots are skipped in favor of cleaner annexure shots.

**Honesty contract.** Boltic the *platform* is Live (it runs Fynd's own production workflows today; the screenshots are real). Boltic *for Reliance Retail* is **Building** — the platform is positioned and ready, RIL-specific deployments are scoped but the production beachhead inside Reliance Retail is not yet enumerated in source material we have. Pills used: `Live · Platform`, `Building · For RIL`, `Roadmap`. Every claim that crosses the live-vs-RIL line carries an explicit pill.

---

## 2. Source inventory

| File | Type | Key facts derivable |
|---|---|---|
| `docs/boltic-notes-compilation/Boltic - Retail Deck  | 2025.pptx` | 33-slide retail sales deck (2025) | Platform positioning · 8 product modules (Workflows, AI Agents, MCP, Serverless, Gateway, Storage, Tables, Monitoring) · Boltic Edge (6 native solutions: Emails, Tables, Extract, SMS, Crawler, IDP) · Boltic Express (prompt-to-workflow) · Boltic MCP (auth-once, AI-driven actions across 500+ apps) · 3 retail capability pillars (Sales & revenue optimization · Order & supply chain workflows · Customer support automation) · platform principles (customised workflows · rapid deployments · run-it-your-way deployment · omnichannel · SOC 2 + GDPR · 24/7 enterprise support) · 9 product UI annexure screenshots (Dashboard, Workflows, Workflow Analytics, AI Agents, MCP, Tables, Serverless, Monitoring, Gateway) |
| 2026-04-30 letter to MM Sir (`docs/2026-04-30-farooq-mda-update-letter.md`) | Cover letter | Boltic listed as AI-Native · Agentic Automation alongside PixelBin and Ratl · being deployed across the value chain |

**Aggregate facts to surface:**
- 8 platform modules in the Boltic stack
- 6 Boltic Edge ready-to-use solutions
- 500+ third-party app integrations available
- 3 retail capability pillars (Sales optimization · Order/supply chain · Customer support automation)
- Compliance posture: SOC 2 · GDPR
- Deployment options: Boltic-managed cloud, customer cloud (run-it-your-way)
- Real product evidence: 9 annexure screens of the live UI

**Aggregate facts deliberately NOT surfaced:**
- 61% revenue uplift / 40% cost reductions / 4.8× productivity claims (slide 7, 15) — these come from generic source citations (IBM, RandGroup, EY, PwC, Market Research, McKinsey) and aren't Reliance-validated. Kept out of hero/stat tiles to preserve the honesty register. Mentioned only as platform-level industry benchmarks if at all, never as our claim.
- Customer logos (slide 21) and beauty-brand / mattress-brand case studies (slides 16-17, 14)
- Pricing tiers (slide 20) — commercial, not register material
- Partner program (slide 19) — not relevant for Apex

---

## 3. Page structure

Hand-authored single page following the canonical section ordering from `website-section-authoring` §4. Sections numbered §0-§07.

```
§0   Hero                                 (eyebrow + H1 + subhead + 4 stat tiles · platform-only stats · no source line)
§01  What Boltic is for Reliance          (Problem · Solution · Impact 3-col)
§02  The platform · 8 modules · live UI   (8 module cards + 6 product UI screenshots merged into one section)
§03  Architecture · full-stack system     (NEW · 4-layer native diagram from slide 13)
§04  Tira · live RR · operations on Boltic (Live · RR · Tira pill · honest placeholder · 1-line acknowledgement, detail to follow)
§05  Urban Ladder · live RR · event collector (Live · RR · Urban Ladder pill · Challenge / Primary use case 2-col + 4-row in-production workflow table)
Footer                                    (standard · no Sources, no In Flight, no capability pillars, no Why-Boltic — page ends at Urban Ladder)
```

**v0.2 (intermediate) — REVERTED.** The v0.1 audit's C1 finding (cross-page underclaim) was wrong. The home register's *"Boltic + Ratl. AI-first testing · 1,300 test cases on AJIO×JCP · vibe-coded prototypes in JCP"* line attributes the testing capability to **Ratl**, not Boltic — Boltic is the workflow-automation OS, Ratl is the AI-first testing platform. Inserting a §03 "Live for Reliance Retail · AJIO × JCP" with `Live · RR` pills on Boltic was a category error: Boltic's role in that estate (orchestration / glue) is not documented in source material, so it cannot carry a Live · RR pill. The AJIO × JCP testing claim belongs on `/ratl`, not `/boltic`.

**v0.3 corrections (2026-05-01).** Reverted v0.2's new §03; restored sequencing §01-§07. Hero stat tile 4 reverted from `Live RR estate · AJIO × JCP · 1,300 test cases` → `Deployment · Cloud or your-cloud`. Hero subhead 1 now states only Boltic-specific platform telemetry: *"Running on Fynd's own operations · 198 workflows · 1.79M monthly executions on the live console."* (sourced from slide 27). All AJIO / test-estate references stripped. Honest position on Boltic-for-RR is restored: platform = Live · Platform; RR-specific deployments = Building / scoped (per §05 in-flight strip).

**v0.4 changes (2026-05-01) — direct user feedback after v0.3.**
1. Removed redundant `Source · Boltic Retail Deck · slides 4, 8, 18 · annexure slides 25-33` line below hero stat tiles — sources now anchored per-section where claims live (§03 cites slide 13, §04 cites slide 16).
2. Removed `· Reliance Retail deployment scoped` from hero section-label.
3. Merged §04 (Inside Boltic · product evidence) into §02 (The platform · 8 modules) — modules above, 6 product UI screenshots immediately below in a 2-col grid. Section title now reads `02 · The platform · 8 modules · live UI`.
4. Inserted new **§03 Architecture** — native HTML/CSS layered diagram of slide 13's "Inside Boltic: A full-stack system": Layer 01 Pre-built Solutions (8 industry tiles), Layer 02 Platform Core (8 module tiles), Layer 03 AI Models (OpenAI · Google · Anthropic · Meta with model strings), Layer 04 Apps + Data (500+ connectors strip).
5. Inserted new **§04 Tira · CRM on Boltic** — Challenge / Solution / Impact 3-col card with `Live · RR · Tira` pill. Tira identified by user as Reliance Retail's beauty brand running the slide-16 "beauty brand CRM" case study, so this surfacing earns Live · RR pill placement.
6. Removed §05 In flight for Reliance Retail (was: 3 Building cards with DRI · TBD · {context}). Roadmap content moved out of the page; in-flight communication will land via the next status update outside the register.
7. Removed §07 Sources section (the "Where this page comes from" 2-card block + Reliance-only filter callout). Sources now live as inline `cap-num · Source · Boltic Retail Deck · slide N` lines at the foot of §03 + §04 only.

**v0.4 honesty register update.** The Tira surfacing flips Boltic's RR posture from "Building (no Live RR documented)" to "Live · RR · Tira (one named brand · 4 event-driven flows)" — based on the deck's own slide-16 case study and user confirmation that the unnamed "beauty brand" in that slide is Tira. This is the only `Live · RR` claim on the page; everything else stays `Live · Platform` (Fynd internal) or `Building · For RIL` (scoped capability pillars).

**v0.5 changes (2026-05-01) — direct user feedback after v0.4.**
1. `BigQuery` → `Data-lake` in the Tira solution card (line "CRM → Data-lake sync · with deduplication"). Generic data-lake naming preserves the technical claim without naming a specific GCP product the user hasn't sanctioned in this register.
2. Removed both inline source-attribution `cap-num` lines (`Source · Boltic Retail Deck · slide 13` at end of §03 and `Source · Boltic Retail Deck · slide 16` at end of §04). The page no longer carries any per-section source citations.
3. Removed §05 Boltic for Retail & Ecommerce (the 3 capability-pillar block · "Three operational pillars at Reliance Retail.") — the Tira live case earns the RR positioning by itself; the speculative "Building · For RIL" pillars don't add information.
4. Removed §06 Why Boltic · platform principles ("Why this stack, not a stitched one." 6-card strip) — pitch material, doesn't survive the register's restraint test.

**Final shape: 4 numbered sections + hero + footer.** §01 Problem/Solution/Impact · §02 8 modules + 6 product UI screenshots · §03 Architecture (4-layer native diagram) · §04 Tira · CRM on Boltic. Page ends at the Tira case — that's the final beat.

**v0.6 changes (2026-05-01) — direct user feedback after v0.5.**
1. **Tira section reset.** v0.5's Tira content (CRM-to-warehouse / MOQ reports / Order Data MCP / 4× / 86%) was a wrong representation — the slide-16 "beauty brand" content was either not Tira or not how Tira actually uses Boltic. Stripped the 3-card Challenge/Solution/Impact body. Section now carries only: header `Tira · operations on Boltic`, `Live · RR · Tira` pill, and a single honest line — *"Reliance Retail's beauty brand Tira runs operational workflows on Boltic. Detailed deployment view to be added in the next status update."* Placeholder, not fabrication.
2. **NEW §05 Urban Ladder · Boltic as event collector.** Full live-RR case study from user-supplied content. Urban Ladder is Reliance Retail's home-and-interiors brand (acquired by RRVL Nov-2020). Section structure:
   - Header `Urban Ladder · Boltic as event collector` + `Live · RR · Urban Ladder` pill
   - Lead paragraph: heterogeneous stack (storefront, OMS, Kapture CRM, CleverTap, GA4, Sentry); Boltic as central event-collection + routing layer
   - 2-card grid: **Challenge** (3 bullets — fan-out events, stitch cross-system flows, Sentry alert routing) + **Primary use case** (Boltic as event collector · 2 broad outcomes: CRM lift + orchestration layer)
   - **In-production workflow table** (4 rows): Interiors communication (Kapture → Boltic → CleverTap), NPS campaign (UL OMS → Boltic → CleverTap), Lead creation (FE → Boltic → Kapture), Sentry alerts (Sentry → Boltic → notification channels)
3. **Honesty register update.** Page now carries two named Live · RR brands (Tira + Urban Ladder), but only Urban Ladder ships specific workflow detail. Tira is acknowledged but not fabricated. This is the correct register move.

**v0.2 fixes that survive into v0.3** (these were independent of the C1 correction):
- All `today` / `production operations` / `right now` / `from day one` / `earns its rent` / `ready for` constructions remain stripped per tone-of-voice §2 + §7.
- §05 in-flight cards retain explicit `DRI · TBD · {scoping context}` lines per honesty register.
- Inline `cap-num` source citations remain in hero, §02, §03, §04 intros.
- §05 Workflow Analytics caption retains `Sep-2025 single-month sample` date-bind.
- §02 Boltic Edge accent card retains the `Plus` framing.

**Why no separate Architecture section (§03 default).** The platform itself *is* the architecture for an automation OS. The §02 module strip carries the layered story — modules listed in stack order (Workflows surface, AI Agents + MCP intelligence, Gateway + Serverless + Storage + Tables + Monitoring infrastructure). Adding a separate diagram-led architecture section duplicates §02 and isn't earned by the source material. → Recorded as **D1** in §9.

**Why no Vision / 13-module-built-vs-full table.** Boltic is a shipped product, not a vision-state platform. Built-vs-full table makes sense for Granary (where 5 of 37 routes are live); for Boltic the platform is fully built and the gap is only RIL-specific deployment progression. The §05 In-flight section covers that gap. → Recorded as **D2** in §9.

### §0 · Hero — copy

- **Crumb:** Home / Boltic
- **Section label:** Track · AI-Native · Agentic automation · Boltic
- **H1:** **Boltic.** *AI workflow automation, ready for Reliance Retail.*
- **Subhead 1:** "Boltic is Fynd's AI-Native Workflow Automation OS — workflows, AI agents, MCP servers, serverless, and a gateway, all in one platform. Live and running Fynd's own production operations today."
- **Subhead 2:** "Positioned for Reliance Retail across sales optimization, supply-chain workflows, and customer-support automation — the three places repetitive operations cost the most recruiter and merchandiser time."
- **Stat tiles** (4):
  1. Platform modules · **8** · Workflows · Agents · MCP · Serverless · Gateway · Storage · Tables · Monitoring
  2. Pre-built integrations · **500+** · across SaaS, ERP, CRM, support
  3. Compliance · **SOC 2 · GDPR** · enterprise security posture
  4. Deployment · **Cloud or your-cloud** · Boltic-managed or self-host

### §01 · What Boltic is for Reliance

3-column block translating slides 2-3 (Problem) and slides 4, 8 (Solution) into Apex register:

- **Problem.** Operations teams stitch fragmented tools by hand · data silos across channels · manual reconciliation across order, inventory, pricing · campaign data scattered across BUs.
- **Solution.** A single AI workflow OS · visual builder + AI agents + MCP servers · 500+ pre-built integrations · runs in Boltic cloud or Reliance cloud.
- **Impact for Reliance Retail.** Operations teams stop maintaining glue scripts and start governing outcomes · long-running back-office processes get monitored end-to-end · AI handles repetitive ops while humans handle exceptions.

### §02 · The platform · 8 modules

3×3 grid (one cell empty for breathing room). Each card carries `Live · Platform` pill — these are shipped product surfaces, demonstrably running on Fynd's own instance.

| # | Module | One-liner |
|---|---|---|
| 01 | Workflows | Visual builder for AI-powered automations with branching, conditions, and scheduled triggers |
| 02 | AI Agents | Agents that act across connected systems in real time with human-in-the-loop oversight |
| 03 | MCP | Standard-protocol servers so AI tools can call your apps and workflows directly |
| 04 | Serverless | Run custom code securely inside workflows with no infrastructure to manage |
| 05 | Gateway | Connect, secure, and monitor APIs powering automations · adaptive scaling |
| 06 | Storage | Manage and automate unstructured data — files, logs, media |
| 07 | Tables | Structured data storage built for operational workflows · AI-prompt to schema |
| 08 | Monitoring | Track workflow execution, page-load checks, broken-link checks · success-rate dashboards |

### §03 · Boltic for Retail & Ecommerce

3 capability cards translating slide 15 into the Reliance frame. Sub-pillars carry `Building · For RIL` pills since these are scoped use cases, not yet enumerated as live Reliance Retail deployments in our source.

| # | Pillar | Use case examples |
|---|---|---|
| 01 | **Sales & revenue optimization** | Predict demand · optimize replenishment · connect POS, supply chain, and external market signals into one workflow |
| 02 | **Order & supply chain workflows** | Sync orders, inventory, deliveries across channels · cut manual handoffs · event-based shipment + rider mapping |
| 03 | **Customer support automation** | Classify queries · draft responses · route tickets across email, chat, and apps for faster resolution |

### §04 · Inside Boltic · product evidence

6 product UI screenshots from the deck annexure (slides 25, 27, 28, 29, 32, 33). Real Boltic UI from Fynd's production instance. Each screenshot is captioned with what it shows. This is the "show, don't tell" beat.

| Slot | File | Caption |
|---|---|---|
| 01 | `screens/dashboard.jpg` | **Dashboard** · the operator control surface · workflow library, integrations, recent activity |
| 02 | `screens/workflow-analytics.jpg` | **Workflow Analytics** · live execution telemetry · 1.79M total executions · 967k succeeded · 817k failed surfaced for triage |
| 03 | `screens/ai-agents.jpg` | **AI Agents** · agent inventory and deployment status · custom agents for retail-specific tasks |
| 04 | `screens/mcp.jpg` | **MCP servers** · standard-protocol bridges so AI tools can act on your data |
| 05 | `screens/monitoring.jpg` | **Monitoring** · uptime, page-load, broken-link, and workflow-health checks |
| 06 | `screens/gateway.jpg` | **Gateway** · API surfaces with end-to-end security and adaptive scaling |

### §05 · In flight for Reliance Retail

3-card honest in-flight strip. These threads are the Reliance-Retail-specific deployment work, not platform features. Pills: `Building`.

- **Reliance Retail beachhead workflows** — first cohort of automation flows scoped to a Reliance BU. Selection by ops priority. Owner + start date to be confirmed in next status update.
- **Run-on-Reliance-cloud option** — Boltic deploys into Reliance's preferred cloud and IDC connectivity model (matches the HireFirst / Granary deployment patterns). Infra readiness in scope.
- **Catalog of pre-built retail templates** — Boltic Templates (slide 10) curated for Reliance Retail use cases: replenishment alerts, PO automation, weekly sales review, ERP-to-support sync.

### §06 · Why Boltic

6-card strip from slide 18. Platform principles, no inflated claims.

- **Customised workflows** — designed by Boltic engineers to fit complex operations
- **Rapid deployments** — ready-to-go workflows built by experts, in hours not quarters
- **Run it your way** — deploy on Reliance cloud or use Boltic-managed infrastructure
- **Omnichannel** — voice, chat, video, WhatsApp, mobile, all connected
- **Enterprise security** — SOC 2 and GDPR compliant
- **Enterprise support** — 24/7 onboarding, chat, and implementation assistance

### §07 · Sources

Card list. Files + paths. Standard pattern.

- `docs/boltic-notes-compilation/Boltic - Retail Deck  | 2025.pptx` (33pp)
- `docs/2026-04-30-farooq-mda-update-letter.md`

---

## 4. Data model

No YAML. Single-page section, hand-authored HTML per skill §1 (≤6-card rule; this page has 8 modules + 6 screens but copy is bespoke per-block, no value in a renderer).

## 5. Asset pipeline

Extract and process the following from the pptx (already extracted to `/tmp/boltic-extract/`):

- **6 product screenshots** from annexure slides:
  - `slide25_img1.png` → `assets/boltic/screens/dashboard.jpg`
  - `slide27_img1.png` → `assets/boltic/screens/workflow-analytics.jpg`
  - `slide28_img1.png` → `assets/boltic/screens/ai-agents.jpg`
  - `slide29_img1.png` → `assets/boltic/screens/mcp.jpg`
  - `slide32_img1.png` → `assets/boltic/screens/monitoring.jpg`
  - `slide33_img1.png` → `assets/boltic/screens/gateway.jpg`
- **Resize:** `sips -Z 1600 -s format jpeg -s formatOptions 80` per skill §6.
- **Skipped on purpose** (would expose non-Reliance brand identifiers):
  - `slide26_img1.png` (Workflow list — has "PUMA X FYND STORE RETURN DETAILS" prominent)
  - `slide30_img1.png` (Tables list — has "puma_clickpost", "Guess_capi" tile names visible)
  - `slide11_img1.png` (Boltic Express prompt — Slack/Gmail logos OK as integrations, but the screenshot is mostly whitespace; not earning a slot)
- **Skipped customer-logo bars and case-study slides** (slides 14, 16, 17, 21) — explicitly out per the Reliance-only filter.
- All images expected <400KB each. Total <2.5MB. **No GCS mirror needed** (under skill threshold).

## 6. Navigation wiring

Already wired in mega-menu **AI-Native** column on every page (suffix `agentic auto`). No nav edits required.

## 7. Build / verify

- Hand-author rewrite of `boltic/index.html` per §3.
- Local: `python3 -m http.server 8000` then visit `http://localhost:8000/boltic`.
- Chrome DevTools MCP: `evaluate_script` to set `sessionStorage.fyndrrl_auth_v1='1'`, `take_screenshot fullPage:true`, `list_console_messages`.
- Verify checklist:
  - [ ] Every screenshot loads
  - [ ] No third-party customer logos appear anywhere on the page
  - [ ] No third-party brand testimonials or case studies appear
  - [ ] Every Live / Building pill is sourceable
  - [ ] Hero stat tiles are derived only from platform-level facts (not industry-benchmark claims)

## 8. Phased delivery

| Phase | Scope | Time |
|---|---|---|
| **P1** | Spec (this file) | done |
| **P2** | Asset extraction + resize (6 screens) | ~10 min |
| **P3** | Hand-author `boltic/index.html` per §3 | ~60 min |
| **P4** | Local verify · screenshot · console clean | ~10 min |

## 9. Decisions

1. **D1 · Section ordering override · drop Architecture (§03 default).** The 8-module strip in §02 carries the layered story for an automation OS; a separate Architecture section duplicates it and isn't earned by source material. **How to apply:** §02 Module strip is the layered narrative; no diagram needed.
2. **D2 · Section ordering override · drop Vision/built-vs-full table (§06 default).** Boltic the platform is fully shipped; the only gap is RIL-specific deployment progression, covered in §05 In flight. **How to apply:** §05 carries the honest in-flight RIL beachhead story; no separate vision table.
3. **D3 · Honesty register.** `Live · Platform` for module cards (shipped product). `Building · For RIL` for retail-pillar use cases and §05 in-flight threads. No `Live · RIL` claims without source-material proof. **How to apply:** Don't paint Boltic as already-deployed-at-RR; paint it as ready-and-positioned.
4. **D4 · Reliance-only filter.** Explicitly skip customer-logo bars, third-party brand case studies, brand-named workflows in screenshots. Keep platform integrations (Slack, Gmail, etc.) since those are platform features, not customer logos. **How to apply:** Use only annexure screenshots that don't expose third-party brand identifiers; pick clean UI shots.
5. **D5 · No outsized industry-benchmark claims in hero/stats.** The deck cites IBM 61% revenue uplift, RandGroup 40% cost reductions, EY 12% PDP-to-cart, etc. — all generic, none Reliance-validated. **How to apply:** Stat tiles use only platform-counted facts (modules, integrations, compliance, deploy options).

## 10. Out of scope (this pass)

- Pricing tiers (slide 20) — commercial material, not register material.
- Partner program (slide 19) — not relevant for Apex audience.
- Per-module sub-pages (`/boltic/workflows/`, `/boltic/ai-agents/`, etc.) — single hub page is enough for v1.
- Animations, video embeds.
- GCS mirror (assets are small).
- Updating other pages' nav blocks (Boltic mega-menu link already correct).

---

**End of spec.** Implementing immediately per user instruction.
