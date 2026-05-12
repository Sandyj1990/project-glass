# RetailVista — Page Spec (restructure)

**Status:** v0.9 in progress · 2026-05-01
**Mode:** Restructure of existing `/retail-vista/` page (was v0.8.4)
**Route:** `/retail-vista`
**Source content:**
- `docs/2026-04-30-farooq-mda-update-letter.md` — narrative anchor (RetailVista listed under Special Projects)
- `docs/retailvista-notes-compilation/RetailVista_Status_Update.pdf` — Karan Muley · 01-May-2026 · 3 tracks, Opportunity Explorer, adoption strategy, requirements, next steps
- `docs/retailvista-notes-compilation/RetailVista_ Geospatial Intelligence Platform Cornerstone - Nov 19, 2025 -2.pptx` — Feb-2026 cornerstone deck · 24 data categories, H3 details, RIL Steering Committee, architecture diagram, platform layers diagram
- Live screenshots from `https://retailvista-agentic.ucp.fynd.com/` captured 01-May-2026 — Home, Explorer (list / quick summary / full analysis with 10 LI dimensions / pipeline kanban), Workspace (list + AI co-pilot), Users
**Narrative anchor:** Replace the WhatsApp-driven, tribal site-selection process with one agentic spatial layer. Predict what a catchment can become — never just reflect its past.

---

## §0 · What's changing and why

The v0.8.4 page over-claims (12 IPs with proof points like "90% on-time delivery") that aren't traceable to current source material. The fresh Status Update reframes the platform around **three tracks** — Internal (UCP/JioMart), Google joint, Ved/JioGIS data unlock — and the agentic Opportunity Explorer is the primary live surface. The cornerstone deck adds the data-layer inventory (24 categories) and the RIL Steering Committee (Prateek Mathur, **Alex Thomas**, Gaurav Verma, Farooq Adam, Advait Pandit). The live app shows the actual modules (Home / Explorer / Workspace / Users) running today.

This restructure resets the page to honest, source-traceable claims and adds visual evidence from the live app.

---

## §3 · Page structure (Add / Keep / Remove)

| § | Title | Status | Notes |
|---|---|---|---|
| 0 | Hero | Restructure | Drop generic "Built by Fynd. Owned and run by Reliance." mono line; reframe lead around 3-track agentic geospatial intelligence; add status pills; add Sponsor + RIL counterpart tiles (Steering Committee names with Alex Thomas explicit) |
| 01 | Status (01-May-2026) · Three tracks | **Add** | 3-column live/building/roadmap from Status Update — Internal (UCP/JioMart), Google joint, Ved/JioGIS Data Unlock |
| 02 | What is live · Modules running today | **Add** | Module table for the agentic Opportunity Explorer surfaces (Home / Explorer / Workspace / Users) with screenshots from the live app — replaces the IP catalog grid |
| 03 | Architecture · 5 layers | Restructure | Sources → Spatial Aggregation → GIS Visualisation → Agentic Orchestration → Activation. Embed the cornerstone Platform Layers diagram |
| 04 | Deep dive · Opportunity Explorer | **Add** | 10 LI dimensions + composite scoring + pipeline kanban + AI co-pilot. Anchored by 5 live-app screenshots |
| 05 | Data foundation · 24 categories | **Add** | Table of 24 master data categories from cornerstone deck §1, with source / volatility / variable counts. The data unlock that makes the platform malleable |
| 06 | In flight · Adoption + scale-up | **Add** | Shadow → Pilot → Scaled → Institutional Standard from Status Update. Six requirements from the business (customer lat/long, JioGIS layers, format benchmarks, live leads, Kentrix MMR, sponsor commitment) |
| 07 | Roadmap · Use cases by Activation Layer | **Add** | From cornerstone deck Activation + Agentic Orchestration layers — New Stores, Pricing/Promotions, Customer Listening, Customer Sentiment Analysis, Transport & SCM Optimisation, Land Parcel Availability, Inventory Availability, TAM. The "older dates but accurate roadmap" |
| 08 | Built by · Team | **Add** | Steering Committee (with Alex Thomas explicit) + Architecture/Data/DS/GIS/Platform/Product owners from cornerstone deck §13 |

**Removed from v0.8.4:**
- 12-IP catalog grid + deep table (un-sourceable proof points like "90% on-time delivery")
- "Building Name Intelligence" standalone section (folded into data-foundation context if needed)
- "Recent leadership engagement" dated log (banned per skill register-wide pattern)
- "Connections" section (let mega-menu and inline links carry these)
- "Live pilots · two parallel tracks" — folded into §01 Three tracks

---

## §9 · Decisions

- **D1 · Section ordering deviation.** §05 Data foundation is inserted between §04 deep-dive and §06 in-flight. Reason: the 24-category data inventory is the single most distinctive credibility artefact in the cornerstone deck and earns its own section ahead of in-flight. Apex needs to see the breadth before reading the validation roadmap. Default ordering (per skill §4) puts §05 = "In flight"; this page swaps to: §04 Deep dive → §05 Data foundation → §06 In flight → §07 Roadmap.
- **D2 · No §08 Sources block.** Provenance lives in inline eyebrow citations and the spec. The page has 3 traceable artefacts, not a multi-source disambiguation case. (Skill §3 default-no rule.)
- **D3 · RIL Counterparts naming.** Steering Committee names from the cornerstone deck Slide 14 are surfaced in the hero tiles + §08 Built-by section. Alex Thomas explicitly named (per user request). RIL-side: Prateek Mathur, Alex Thomas, Gaurav Verma, Advait Pandit. Fynd-side: Farooq Adam.
- **D4 · No author / version line.** Per current convention (skill §4), no Author / Date / Version block in hero; footer carries only the copyright line.
- **D5 · Use cornerstone roadmap not Status Update roadmap.** Per user direction — Status Update PDF doesn't include explicit roadmap dates. Cornerstone deck's Activation Layer + Agentic Orchestration cells (New Stores, Pricing, Customer Listening, Customer Sentiment, Transport & SCM Optimisation, New Store Opening, Pricing Promotion, Land Parcel Availability, Catchment Analysis) form the "older dates but accurate roadmap".
- **D6 · Vision-vs-live honesty pills.** Live = running today (Internal track Opportunity Explorer with Mumbai NSO leads, Google MVP demoed end-to-end on Mumbai). Building = adoption rollout, JioGIS data unlock. Roadmap = Activation-layer use cases beyond first-set (NSO + dark-store drive time + catchment). Tag every claim.

---

## §10 · Out of scope

- Sub-pages (Research / etc.) — not in this restructure.
- 12-IP catalog from v0.8.4 — explicitly removed pending source verification.
- Detailed governance section — defer until a memo arrives.
- New screenshots from Google joint track — fold in next cycle when Google demo recording is shared.
