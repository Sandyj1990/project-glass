# UCP & Marketing OS · Restructure spec

**Status:** v0.1 · 2026-05-01 · **drafting**
**Owner:** Kushan Shah
**Route:** `/ucp/` (already live; this spec restructures it)
**Source content:** `docs/UCP Notes compilation/` + `docs/2026-04-30-farooq-mda-update-letter.md`
**Narrative anchor (per MDA letter, 30-Apr-2026):** UCP is the proven identity + data platform. Marketing OS is the **L4 Agentic** evolution being built on top — three new agentic surfaces (Marketing Intelligence cockpit, Brand Health cockpit, AI-Native UCP chat). The page must report what is live for RIL today + the agentic surfaces shipping now + the L4 endgame, with honest tier separation throughout.

**Built using:** `.claude/skills/website-section-authoring` (workflow) + `.claude/skills/website-tone-of-voice` (copy register).

---

## 0. Implementation status

| Stage | Deliverable | Where it lands |
|---|---|---|
| 0 raw | Source compilation folder | `docs/UCP Notes compilation/` (Release-Notes-Timeline.md + Analysis_Dashboard.html) |
| 1 spec | This file | `docs/ucp-marketing-os-spec.md` |
| 2 data | Single page · no YAML; copy authored inline | `ucp/index.html` |
| 3 assets | None — page is text + numbers; no screenshots in v1 | — |
| 4 build | Hand-authored HTML (single-page section, ≤6-card rule) | `ucp/index.html` |
| 5 nav | Already wired in mega-menu (`Platforms` column as "UCP & Mktg OS"); no nav edits needed | — |
| 6 verify | Local server walk + Chrome DevTools screenshot + console clean | — |

---

## 1. Why this page exists

**Audience.** RIL Apex leadership reviewing the register. Same audience as `/impetus`, `/jcp`, `/granary`, `/hirefirst`.

**Gap to close.** The current `/ucp` page (live, v0.8.4) is accurate but missing the architectural restructure that the 30-Apr-2026 MDA letter establishes — UCP and Marketing OS are now one platform line, with Marketing OS as the L4 agentic evolution. Specifically missing:

- The **UCP-foundation → Marketing-OS-evolution** narrative arc
- A clean **Status strip** that separates what's Live (UCP) vs Building (Marketing OS modules) vs Roadmap (full agentic chat)
- **§03 Architecture** — the 4-layer stack (Identity → Data → Activation → Agentic) that explains why Marketing OS can sit on UCP
- **Marketing Intelligence cockpit** — the Apr-2026 vertical-leader cockpit (Executive Cockpit + Business Deep Dive + Talk to Data)
- **Brand Health cockpit** — the Apr-2026 brand-perception cockpit (Funnel + Imagery + Talk to Data)
- **L-rung pills** on every Marketing OS module — current rung today + L4 target — matching the MDA letter framing of "path to L3/L4 this quarter"

**Two truth-states to honour.**

1. **Live for RIL today** — UCP foundation: 12 channels, 380M identities, 1.5M RPOS daily orders, 200+ profile attributes, 12 shipped releases Jan-2024 → Apr-2026. Already on the page; restructure preserves all of it.
2. **Marketing OS** — the three agentic surfaces. MI cockpit and Brand Health cockpit are shipped (per the Apr-2026 entries in the timeline). AI-Native UCP is demoed (YouTube link) and being built. Each surface gets an L-rung pill (current + target) so the register stays honest about where each sits today.

## 2. Source inventory

| File | Type | Key facts derivable |
|---|---|---|
| `docs/UCP Notes compilation/UCP-Release-Notes-Timeline.md` | Markdown release-notes compendium · 12 releases Feb-2025 → Apr-2026 + 3 cockpit/AI-Native sections | All shipping content for the page |
| `docs/UCP Notes compilation/Analysis_Dashboard.html` | Interactive RD DDD analysis dashboard | All RD DDD case-study numbers (already on the page; verify against this file) |
| `docs/2026-04-30-farooq-mda-update-letter.md` | MDA cover letter | UCP & Marketing OS as one platform line · L3/L4 framing · Apex audience |

**Aggregate facts to surface:**

- 12 channels integrated (JioMart 130M+, AJIO 80M+, Netmeds 35M+, Tira 1.3M+, Reliance Digital, Reliance Jewels, MilkBasket 2M+, FreshPik, Swadesh, Urban Ladder, RPOS 80+ formats / 15K+ stores, RBL retail-brand microsites)
- 380M+ identities unified across online + offline RR
- 200+ profile attributes
- 1.5M daily RPOS orders streaming in (within minutes of checkout)
- ~19 ms p50 API latency · ~300 ms event processing end-to-end · 500 events/sec sustained
- NPS at scale: 79 formats · ~7,000 stores · 7.2M orders processed · ~500K daily surveys · ~7K daily responses
- 12 major UCP releases timeline (preserved)
- RD DDD case study: 1.25M recipients · ₹20.39 Cr revenue · 5,693 buyers · 30.68% open · 0.56% click · 1.82% CTOR · transactor lift +25% / +314% / +234% (preserved)
- Marketing Intelligence cockpit · 3 surfaces (Executive Cockpit / Business Deep Dive / Talk to Data) · plan-aware · A2S, ROAS, CAC, LTV/CAC · grounded AI diagnostics · same shape across Ajio / JioMart / Tira / RD / F&L
- Brand Health cockpit · 3 surfaces · Total Awareness → Consideration → L1Y Usage → L3M Usage → MOUB · 20-attribute imagery analysis · zonal · ad testing · competitor swap (Blinkit/Zepto/Swiggy Instamart/Flipkart Minutes/Amazon Fresh/Bigbasket Now)
- AI-Native UCP · chat interface · speak to data · cohort generation · campaign config · creative generation · execution · retrospective · competitor analysis · next-best-action · YouTube demo (`youtu.be/9KCFnV6kXEU`)

## 3. Page structure (post-restructure)

Frame: **UCP foundation → Marketing OS evolution.** Add/Keep/Remove diff against the current 14-section page.

```
§0  Hero                              (KEEP — refine subhead to add Marketing OS framing)
§01 Status                            (NEW — 3-col Live/Building/Roadmap strip with L-rungs)
§02 What's live · UCP foundation      (KEEP & MERGE — current channels grid + perf stack into one section)
§03 Architecture · 4 layers           (NEW — Identity → Data → Activation → Agentic, with L-rung pills)
§04 Marketing OS · 3 cockpits         (NEW — MI + Brand Health + AI-Native, expanded copy with L-rungs)
§05 Case study · RD DDD               (KEEP — current dark card preserved, minor copy pass)
§06 Release timeline                  (KEEP — current 14-row timeline preserved)
§07 Built by                          (KEEP — current team table)
§08 Sources                           (NEW — link release-notes md + analysis dashboard + MDA letter + AI-Native demo)
Footer                                (KEEP)
```

### §0 · Hero — copy refinements

Keep crumb + section label + H1. Update subhead to carry both the live-foundation reportage AND the Marketing OS arc:

- **H1:** `UCP & Marketing OS.` (was just `UCP.`)
- **Subhead:** `One identity layer across every Reliance retail business — and the agentic marketing layer being built on top of it. UCP is live across 12 channels with 380M+ identities and 1.5M daily RPOS orders. Marketing OS — three agentic cockpits (Marketing Intelligence · Brand Health · AI-Native UCP) — climbing to <a href="/autonomous">Agentic L4</a>.`
- **Stat tiles (4):** keep current (Identities · Profile attributes · RPOS daily orders · Privacy-compliant). No L-rung in hero stats — those come in §01.

### §01 · Status

3-column strip mirroring the `/jcp` and `/granary` pattern. Each column carries a status pill + L-rung.

| Live · today | Building · this quarter | Roadmap · L4 endgame |
|---|---|---|
| **UCP foundation** · L3 | **Marketing Intelligence cockpit** · L3 today → L4 target | **AI-Native UCP** (full agentic chat) · L2 demo → L4 target |
| 12 channels · 380M identities · 1.5M daily RPOS orders | Plan-aware cockpit live across Ajio, JioMart, Tira, RD, F&L | Speak-to-data + cohort gen + campaign config + creative gen + execution + retrospective in one chat |
| **Campaign Manager** · L3 · 200+ formats with governance | **Brand Health cockpit** · L3 today → L4 target | |
| SMS · RCS · Meta · Google activation | 5-stage funnel + 20-attribute imagery + competitor swap | |

Honesty notes:
- L-rung claims are **assertions about the surface today**, not promises. Reviewer can dispute any pill — that's the contract.
- Reference for L0-L5 definitions: `/autonomous`.

### §02 · What's live · UCP foundation

Merge today's two cards (channels grid + performance stack) into one section with a clearer header. Section label: **"02 · UCP foundation · what's running across Reliance Retail today"**.

Sub-blocks (preserve content from current page, tighten layout):

- **12 channels integrated** (table — unchanged from current)
- **Performance stack** (sub-second at scale, RRA enrichment, Boltic clickstream SDK — unchanged)
- **Capabilities live** (RRA v2, OTP/Auth, Address Optimisation, Sanctions Screening, Audience Builder, RPOS streaming, NPS at scale, Campaign Manager with coupons + governance — derive from timeline)

### §03 · Architecture · 4 layers

NEW. 4-card layered diagram (no image — text + pills). Each card carries a status pill.

| Layer | What it is | Status |
|---|---|---|
| **04 · Agentic** | Marketing OS — MI cockpit · Brand Health cockpit · AI-Native chat | `Building` · L3 today → L4 target |
| **03 · Activation** | Campaign Manager · SMS/RCS/Meta/Google · Coupons · Governance · Conversions tracking | `Live` · L3 |
| **02 · Data & Intelligence** | Single Customer View · Audience Builder · RRA enrichment · NPS at scale · RPOS real-time streaming · Boltic clickstream | `Live` · L3 |
| **01 · Identity** | Reliance Retail Account · OTP/Auth · DPDP consent · Unified Address Book · API-first integration · Sanctions Screening | `Live` · L3 |

One-line below: *"Each layer earns the next. Identity made unified data possible. Unified data made segmentation and activation possible. Activation at scale is what makes the agentic layer worth building."*

### §04 · Marketing OS · 3 cockpits

NEW. The defining Marketing OS section. 3 cards in a 1-3 grid (one per cockpit). Each card opens with a one-line definition + L-rung pill, then 3 named surfaces, then a "what makes it agentic" line.

#### Card A · Marketing Intelligence cockpit
- **Pill:** `Live · L3 today → L4 target`
- **One-line:** The cockpit for vertical leaders — AOP-vs-actuals, marketing efficiency, customer mix, platform health, in one view. Replaces the WBR-decks-plus-MarTech-dashboards stitch leaders did each month.
- **Three surfaces:**
  - **Executive Cockpit** — single scrollable canvas · Business Outcomes (Net Revenue · Orders · Customers · ABV with AOP achievement) · Marketing (Spend · A2S% · PM · Blended CAC · LTV/CAC) · Platform & Brand Health (MAU · DAU · Sessions · NPS). Every KPI carries an AOP-anchored comparison.
  - **Business Deep Dive** — outcome → cause → diagnosis. Revenue Story (actuals vs plan, 13-month trends, source splits New/Repeat/Winback, retention). Marketing Effectiveness (A2S, ROAS, Blended + PM CAC, LTV/CAC, approved-vs-actual budget, channel breakdown ATL/BTL/PM/Others). AI Diagnostic with colour-coded insight cards (Red material misses · Amber watchpoints · Green positive · Blue neutral).
  - **Talk to Data** — natural-language layer. *"Why did ABV drop in Feb?"* / *"Show me Tira CAC trend vs Ajio."* Charted, sourced answers without SQL.
- **What makes it agentic:** Plan-aware by default, grounded AI diagnostics that reference visible numbers, same shape across every vertical (Ajio, JioMart, Tira, Reliance Digital, F&L). Switch the vertical, get the same cockpit.

#### Card B · Brand Health cockpit
- **Pill:** `Live · L3 today → L4 target`
- **One-line:** Where Marketing Intelligence answers *"are we hitting the plan?"*, Brand Health answers *"do consumers know us, prefer us, use us, trust us — and how do we compare to the competition?"*
- **Three surfaces:**
  - **Executive Cockpit** — side-by-side funnel · anchor brand (left) vs chosen competitor (right). Five stages: Total Awareness → Consideration (T2B) → L1Y Usage → L3M Usage → MOUB. Each stage shows absolute score, ±pp delta vs prior wave, relative % change, conversion ratios. Competitor selector swaps comparison brand without leaving the view (Blinkit, Zepto, Swiggy Instamart, Flipkart Minutes, Amazon Fresh, Bigbasket Now).
  - **Business Deep Dive** — Brand Imagery Analysis (20 attributes across functional / commercial / emotional, gaps table sorted by magnitude, top-5 movers QoQ). Usage Funnel (trial → habitual, vs best-in-class named explicitly). Purchase Behaviour (Kirana / Quick-commerce / Modern Trade). Zonal Performance (North / South / East / West). Ad Testing Results (creative-level masked brand-recall). AI Analysis (4 pillars · Perception / CX / Growth / Marketing) with the same Red/Amber/Green/Blue cards.
  - **Talk to Data** — *"How has JioMart's MOUB tracked vs Blinkit over the last 4 waves?"* / *"Which imagery attributes improved the most in South zone?"* Charted, sourced answers.
- **What makes it agentic:** Gap-first rather than score-first design (the delta matters more than the absolute in mature categories), side-by-side competitor comparison built into every metric, creative recall closing the loop from campaign spend to brand equity.

#### Card C · AI-Native UCP
- **Pill:** `Building · L2 demo → L4 target`
- **One-line:** A complete CDP in a single chat interface. The endgame for Marketing OS — every step of the marketing workflow (data → cohort → campaign → creative → execution → retrospective) happens conversationally, with AI models powering each step.
- **Eight conversational steps** (compact 2x4 grid, preserved from current page):
  - Speak to your data · AI-built cohorts · Configure campaigns · Generate creatives · Execute campaigns · Retrospective analysis · Competitor intelligence · Next-best-action
- **Demo:** `youtu.be/9KCFnV6kXEU`
- **What makes it L4:** No dashboards. No tool-switching. Governance guardrails built in. The reviewer can ask the question and get a charted, sourced answer that ends in a launched campaign.

### §05 · Case study · RD Digital Discount Days

KEEP current treatment (dark card with KPIs strip + transactor lift table + category mix). Minor copy pass to align with the §04 Marketing OS framing — frame the case study as *"this is what UCP today + a glimpse of Marketing OS already does."*

### §06 · Release timeline

KEEP current 14-row timeline (Jan-2024 → Apr-2026). Add 2 new rows at top for MI cockpit and Brand Health cockpit (both Apr-2026, sourced from release notes). Verify dates against release-notes md.

New rows:
- **Apr - 2026 · Marketing Intelligence cockpit live** — Executive Cockpit + Business Deep Dive + Talk to Data. Plan-aware across Ajio, JioMart, Tira, RD, F&L.
- **Apr - 2026 · Brand Health cockpit live** — 5-stage funnel + 20-attribute imagery + competitor swap + ad-testing module + AI analysis (Perception / CX / Growth / Marketing).

### §07 · Built by

KEEP current team block. No edits needed unless the source release notes name new people for MI / Brand Health.

### §08 · Sources

NEW. Card list, register-standard:
- `docs/UCP Notes compilation/UCP-Release-Notes-Timeline.md` — 14 release entries + MI + Brand Health + AI-Native UCP descriptions.
- `docs/UCP Notes compilation/Analysis_Dashboard.html` — interactive RD DDD analysis dashboard (charts not embedded on this page; numbers sourced here).
- `docs/2026-04-30-farooq-mda-update-letter.md` — MDA letter framing UCP & Marketing OS as one platform line, with L3/L4 framing.
- `youtu.be/9KCFnV6kXEU` — AI-Native UCP demo.

## 4. Data model

No YAML. Single-page section, hand-authored HTML (per skill §1: ≤6 sub-pages → hand-author; this page has zero sub-pages).

## 5. Asset pipeline

None for v1. Page is text + numbers + status pills. No screenshots needed. (Future v2 may add MI cockpit and Brand Health screenshots if Amogh / Prem ship deck slides.)

## 6. Navigation wiring

Already wired. `/ucp` appears in the mega-menu **Platforms** column on every page that has the v0.8.4 nav. No nav edits.

Update mega-menu label from `UCP & Mktg OS` → `UCP & Marketing OS` for consistency. Single sed sweep across ~25 nav blocks.

## 7. Build / verify

Hand-author `ucp/index.html` directly. No renderer. After save:

```bash
python3 -m http.server 8000
# open http://localhost:8000/ucp
# bypass auth gate in DevTools console:
# sessionStorage.setItem('fyndrrl_auth_v1', '1'); location.reload()
```

Walk through:
- [ ] Section index loads
- [ ] All hero stats render
- [ ] Status strip renders 3 columns at desktop, stacks on mobile
- [ ] Architecture 4-card layer block renders (no broken pills)
- [ ] Marketing OS 3-cockpit cards render with all 3 surfaces visible
- [ ] RD DDD case study card preserved
- [ ] Release timeline preserved
- [ ] Sources section all links resolve
- [ ] Mobile (375px) renders OK
- [ ] Console clean
- [ ] Every URL clickable (no plain `<span>` URLs)

## 8. Phased delivery

- **P1** (this commit) · Spec + new `ucp/index.html` with §0–§08 wired. ETA 2h.
- **P2** (later) · Add MI cockpit + Brand Health cockpit screenshots if Amogh / Prem deliver. Decision deferred — not blocking.
- **P3** (later) · Embed selected RD DDD charts inline if requested. Currently rejected per D3.

## 9. Decisions

D1 · **Page frame · UCP foundation → Marketing OS evolution.**
**Why:** Most honest narrative — UCP is shipping for 2 years and Apex already values it. Marketing OS is the L4 evolution but is honest about being mid-build. Two-half framing flattens the story; Marketing-OS-led undersells the foundation.
**How to apply:** Hero opens both in one breath. §01 Status separates them. §02–§03 establish UCP. §04 introduces Marketing OS as evolution, not replacement. §05–§06 close with proof + history.

D2 · **Marketing OS scope · MI + Brand Health + AI-Native chat.**
**Why:** All three are net-new since Jan-2026, all carry the agentic/cockpit DNA, all are described in the Apr-2026 release notes as the new agentic surface area. Excluding any one of the three creates an arbitrary line.
**How to apply:** §04 has three cards (one per cockpit). MI + Brand Health carry `Live · L3 today → L4 target`. AI-Native carries `Building · L2 demo → L4 target`. Don't conflate the three — each gets its own card with its own three-surfaces structure.

D3 · **RD DDD case study · keep current treatment.**
**Why:** The current dark card with 5 KPIs + lift table + category mix is the right size. Embedding 3 charts doubles the section length without adding new insight. The full Analysis_Dashboard.html stays available as the source link for anyone who wants to drill in.
**How to apply:** Preserve current §05 dark card. Link the dashboard in §08 Sources.

D4 · **L-rungs · explicit per module, with current rung + L4 target.**
**Why:** MDA letter explicitly frames the path as "L3/L4 this quarter." Per-module rungs are defensible per-claim (reviewer can challenge any specific pill). Single-statement framing in hero would be weaker per-claim.
**How to apply:** Every Marketing OS module in §01 Status, §03 Architecture, §04 cockpits carries an L-rung pill `LN today → L4 target`. UCP foundation carries `L3` (mature). Reference link to `/autonomous` for L0-L5 definitions.

## 10. Out of scope

- Embedding interactive charts from Analysis_Dashboard.html (rejected D3).
- Screenshots of MI cockpit or Brand Health cockpit (none in source folder; deferred to P2).
- New sub-pages (`/ucp/marketing-intelligence`, `/ucp/brand-health`) — single page covers it for the register; can split later if Apex asks for depth.
- Updating sibling pages' "Other tracks" backlinks (lazy strategy per skill §8).
- New entries in the home page card (the existing card already says "UCP & Marketing OS"; verify and proceed).
