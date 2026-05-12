# Samarth Plus · /samarth restructure spec

**Status:** v0.9 · update / restructure
**Mode:** Update (restructure existing `/samarth` page)
**Owner (Fynd-side DRI):** Nishant Amin (PM lead) · Ashish Agrawal (EM)
**Route:** `/samarth`
**Source content:** `docs/samarth-plus-notes-compilation/`
**Narrative anchor:** Farooq → MM Sir 30-Apr-2026 update letter — *"Special Projects — ALP, RetailVista, others"*. Samarth Plus is one of the named Special Projects deliverables.

---

## §0 · What's changing and why

The existing `/samarth` page conflates Samarth Plus (a focused App-in-App career platform inside People First) with a sprawling 11-IP "workforce + store-OS" survey grid (Store OS, POS, Companion App, Scan & Go, Endless Aisle, R-One Loyalty, Coupons, Trends 4.0, AI Cataloging, Workforce Intelligence, Samarth Plus core). That mega-grid belongs on a workforce-stack overview page, not on a Special Projects entry whose siblings (`/alp`, `/retail-vista`) are tightly focused single-product builds.

Two new source artefacts arrived in `docs/samarth-plus-notes-compilation/`:

1. **`MODULE_WORK_BREAKDOWN.pdf`** — Raunak Sharma's 7-month incremental delivery log (Oct 2025 → Apr 2026). Six phases. Cross-cutting challenges. The honest engineering story behind the launch.
2. **`Samarth Plus_HRBP_Training Deck_v0.pdf`** (20-Mar-2026) — the 6-step candidate journey (Pick Your Path → Quick Check → Skill Up → Practice → Get Certified → Progress) actually shown to associates inside the People First app, plus the "Growth · Recognition · Confidence" associate-value framing.

These together let the page tell the focused product story (what Samarth Plus *is* for an associate) and the focused engineering story (how it shipped from Supabase prototype → Reliance prod in 7 months).

**Why this matters at Apex.** The MDA letter promised transparent, evidence-backed Special Projects updates. Samarth Plus is the only Special Project that crossed from build → prod in this window. The page should read as an honest delivery log, not a workforce-stack catalogue.

---

## §3 · Page structure (Add / Keep / Remove diff)

Default §-ordering from `website-section-authoring` §4. Override: this page skips §03 Architecture-as-layered-diagram (substitute: §03 = the candidate journey deck, which IS the architecture from the user's POV) and skips §06 Vision-as-built-vs-full (the §05 in-flight roadmap + §06 honest cross-cutting challenges carry the honesty contract).

| § | Section | Action | Notes |
|---|---|---|---|
| 0 | Hero | **Keep + refine** | Keep eyebrow, H1, Built-by-Fynd line, subhead, "How Fynd transforms" sentence. Refresh status pill from `Live · production` to `Live · limited pilot · Apr 2026` (matches Phase 6 source language — "Build went to Prod this phase, with a limited set of pilot users"). Stat tiles: Live status · Role transitions ~160 · Form factor App-in-App · Formats covered 3. People tiles: PM lead · EM · RIL counterparts · Sponsors. |
| 01 | Status · what Samarth Plus does for Reliance | **Add** | 3-card Live / Building / Roadmap strip replacing the existing "Aim / Mechanism / Outcome" Scope row (which reads as deck-marketing). Live = Apr 2026 prod cutover with pilot users on People First. Building = bulk-upload tooling stabilisation, BU-master-driven role mapping. Roadmap = AI Interview Agent, Smart Proctoring, Action Learning Projects, LMS+IJP integration. |
| 02 | What's live · the candidate journey | **Add** | The 6-step journey from the HRBP deck rendered as a 6-card row: 1 Pick Your Path · 2 Quick Check · 3 Skill Up · 4 Practice (OJT) · 5 Get Certified · 6 Progress. Each card carries a one-line objective (from the HRBP deck Quick Reference table) and a key constraint (e.g. "100% module completion required", "OJT mandatory for K3→DM transitions"). Source eyebrow: HRBP Training Deck v0 · 20-Mar-2026. |
| 03 | Four employee pillars + admin tower | **Keep + restyle** | Already on the page. Re-titled to "Platform pillars · what's wired into the App-in-App" so it reads as the *implementation* under the journey rather than a separate framing. Restyled as 2×2 + admin row. |
| 04 | How we got here · 7-month delivery (Oct 2025 → Apr 2026) | **Add** | The 6 delivery phases from Raunak's MODULE_WORK_BREAKDOWN, rendered as a phase-table with: Phase · Window · Environment · Headline. This is the honest engineering log. Source eyebrow: Module Work Breakdown · Raunak Sharma. |
| 05 | What was hard · cross-cutting challenges | **Add** | The 8 cross-cutting challenges from the same doc, condensed to 6 cards: prod-data normalisation; Career Tree multi-source-of-truth; SCORM packages; Fortify scan loop; journey-context propagation; Reliance infra constraints. Apex reads this as "what we'd do differently next time" — earns the page. |
| 06 | Squad · who built it | **Keep + refine** | Reorder to put EM + dev pair first (the people who landed it), then PM, QA, ops. Add Vikas Singh + Yash on UI/SSO collaboration (per source doc). |
| 07 | Roadmap · 6-12 mo | **Keep** | Q1 AI Interview Agent · Q2 Smart Proctoring · Q3 Action Learning Projects · Q4 LMS + IJP integration. Source: existing page (held over from prior comms; not contradicted by new sources). |
| 08 | Sources | **Add** | Two source cards: HRBP Training Deck v0 (PDF) + Module Work Breakdown (PDF). Both linked to the compilation folder paths. Per `website-tone-of-voice` §3, the Sources block earns its place here because the page combines two distinct artefacts that an Apex reader might want to cross-check. |
| — | Sub-IPs grid (Store OS, POS, Companion App, Scan & Go, Endless Aisle, R-One, Coupons, Trends 4.0, AI Cataloging, Workforce Intelligence, Samarth Plus core) | **REMOVE** | Belongs on `/jcp/`-level workforce overview, not on a focused Special Projects page. Each sub-IP already has (or will have) its own home. Keeping it here reads as Samarth Plus laying claim to the whole store-OS surface — which it doesn't. |
| — | Sub-IP Deep cards table | **REMOVE** | Same reason as above. |

**Final section count:** 9 sections (0-08), down from 8 in the current page — but with two heavy redundant grids cut and four focused sections added.

---

## §9 · Decisions (locked)

- **D1 · Section ordering override.** Skip canonical §03 Architecture (4-layer diagram). Substitute the 6-step candidate journey at §02 — for Samarth Plus the user-visible journey *is* the architecture an Apex reader wants to see. The platform-pillars 2×2 at §03 carries the implementation-side counterpart.
- **D2 · Status pill honesty.** Pill reads `Live · limited pilot · Apr 2026`, not `Live · production`. Source: Phase 6 doc — *"Build went to Prod this phase, with a limited set of pilot users."* Overclaiming here would erode trust at first scroll.
- **D3 · Drop the 11-IP grid.** Sub-IPs and Deep-cards table cut entirely. Reasoning above. If a workforce-stack-survey page is ever needed, it lives at `/workforce` or as a section inside `/jcp` — not on `/samarth`.
- **D4 · Author/Date/Version line.** Per `website-section-authoring` §4 — no Author / Date / Version line in hero, no Owner / version line in footer. Provenance is in this spec + git.
- **D5 · Sources block included** (departing from the default-no Sources rule) because the page combines two distinct external artefacts (HRBP deck + engineering breakdown) and an Apex reader cross-checking the page would reasonably want to know which fact came from where.
- **D6 · No screenshots in v0.9.** The HRBP deck has UI screenshots embedded but they're People First app screens (red Reliance branding, not the Samarth Plus iframe). Pulling them in would add visual confusion without earning their place. Defer to v0.9.1 if a reviewer asks for visual evidence.

---

## §10 · Out of scope

- Screenshot extraction from the HRBP deck (D6).
- Workforce-stack overview / sub-IPs catalogue page (extracted out of `/samarth`).
- Live URL or login credentials for the running instance (limited pilot; not for register publication).
- Cross-page nav edits beyond `/samarth` itself — home card already exists and reads correctly; Tracks mega-menu already lists `/samarth`.
