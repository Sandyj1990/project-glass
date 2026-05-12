# Autri · section spec

**Status:** drafted · 2026-05-02
**Mode:** new section (replaces the placeholder hub at `/autri/`)
**Owner (Fynd-side DRI):** Saaket Chawali · Product
**Route:** `/autri/`
**Source content:** `docs/accenture-2026-04-16-compilation/Autri_Agentic_Planogram_Compliance_for_Grocery.pdf` (13 pp · authored by Saaket Chawali, 21-Apr-2026)
**Narrative anchor:** the 30-Apr-2026 Farooq → MM Sir letter names "Autri" under **Recent Innovations** alongside Fynd Horizon and Dark Factory. This page makes that name navigable for Apex.

---

## §0 · Why this page exists

Audience. RIL Apex leadership (MM Sir level), reading at Apex grain. The current `/autri/` page is a stub ("Page in progress") with no substance. The 30-Apr-2026 letter promises a real-time transparency surface for every named platform; Autri is on that list.

The substantive content for the page now exists: a 13-page write-up by Saaket (Product) describes Autri as **Fynd Necleus' Agentic Planogram Compliance for Grocery** — a self-verifying loop where the Autri robot scans grocery shelves, Gmetri reads them against the active planogram, an Agentic Command Center decides what's off, PulsePoint routes a fix to the right person, and the *next* Autri scan closes the ticket only when compliance is verified.

The honesty contract: Autri is **already deployed and scanning** as a standalone analytics tool. The agentic loop (Gmetri integration + Command Center triage + PulsePoint auto-ticketing + verify-by-rescan closure) is **being built** — it's not running end-to-end yet. Every claim on the page must carry the status pill that earns it.

## §1 · Source inventory

| File | Pages | What's in it |
|---|---|---|
| `Autri_Agentic_Planogram_Compliance_for_Grocery.pdf` | 13 | The full write-up: use case, today vs agentic flow, 5-step loop, 3-layer architecture + master data plane, 4-stage plan, 9 outcome targets, 5 risks-and-mitigations |
| `2026-04-30-farooq-mda-update-letter.md` | 1 | Names Autri as a Recent Innovation; positions the page in the broader update narrative |

Embedded image inventory (extracted via `pdfimages -j` from the source PDF):

| Source image | Content | Use as |
|---|---|---|
| img-000 | Autri Sessions dashboard · "My Sessions" with 42 total / 11 active / 17 completed / 11 failed at Fresk Pik Powai 68219 | `01-sessions-dashboard.jpg` (today's UI) |
| img-004 | Session detail page · scan tasks broken down by 50 grocery categories, 98/100 done | `02-session-detail.jpg` |
| img-006 | High-density grocery shelf with AI bounding boxes detecting individual SKUs (Global Flavours wall) | `03-shelf-bounding-boxes.jpg` |
| img-007 | Cooking-sauces shelf with bounding-box detections | `04-shelf-bounding-boxes-2.jpg` |
| img-010 | Brand-by-shelf-level analytics + Product Distribution Across Shelf Levels heatmap | `05-brand-shelf-analytics.jpg` |
| img-012 | 5-step loop diagram · SCAN → READ → DECIDE → ACT → VERIFY (with re-scan loop) | `06-loop-diagram.jpg` |
| img-013 | Architecture diagram · Master Data + Action + Data + Intelligence layers | `07-architecture-diagram.jpg` |
| img-015 | End-to-end sequence diagram · 17-step swimlane (Store Ops → Autri → Image Repo → Gmetri → Command Center → PulsePoint → Store Staff) | `08-end-to-end-flow.jpg` |

## §2 · Page structure (canonical ordering)

Single page. No sub-pages. Hand-authored `autri/index.html` (no renderer — well under the 6-card cutoff for that decision).

| § | Title | Purpose | Anchor source |
|---|---|---|---|
| 0 | Hero · *Autri.* | Eyebrow ("Recent Innovations · Agentic Planogram Compliance for Grocery") + H1 + 2-line subhead + 3 status pills (Live · scanning today / Building · agentic loop / Roadmap · chain-wide rollout) + 4 stat tiles + first hero image (sessions dashboard) | PDF §1, §3.1 |
| 01 | What's live today vs the agentic flow | 2-column compare: Autri today (analytics tool) vs Autri in the agentic flow (high-fidelity producer + loop closer) | PDF §3 |
| 02 | The 6 compliance dimensions | Table: dimension → what's checked → example non-compliance | PDF §1.1 |
| 03 | Architecture · 3 layers + 1 master data plane | 4-card layered diagram + the source architecture image | PDF §5 |
| 04 | The 5-step loop | 5 cards (Scan → Read → Decide → Act → Verify) + the loop diagram image | PDF §4, §6 |
| 05 | Per-dimension handling | Table: dimension → detected by → decided by → acted on | PDF §5.1 |
| 06 | Plan · 4 stages | 4-card stages (Foundation → Intelligence → Action → Pilot & scale) with deliverables and exit criteria — all carry **Building** or **Roadmap** pills | PDF §7, §7.1 |
| 07 | Design choices for grocery | 3 cards: velocity-weighted severity, promotional-execution lane, scans timed to restocking | PDF §8 |
| 08 | Outcome targets | Table: outcome → target → why it matters | PDF §9 |
| 09 | Risks & how we design against them | Table: risk → mitigation | PDF §10 |

§10 Sources removed entirely (post-audit user instruction). PDF download moved to an inline source eyebrow under the hero subhead, per tone-of-voice §3 default-no-Sources-block rule. Provenance lives in git, the spec, and the inline eyebrow.

**Override notes** (per playbook §4):
- §02 and §05 are **two tables of compliance dimensions** in the source. They're cousins, not duplicates: §02 is the "what" (definition of compliance), §05 is the "how" (which agent touches each dimension). Both earn their rent.
- No `/research/` section — there is no research artefact beyond the source PDF itself; Sources section covers it.
- No tech stack block — the architecture section already names the systems (Autri robot, Gmetri, Command Center, PulsePoint).
- No competitive landscape — out of scope for an internal Apex page.
- No team / built-by — single DRI in the spec footer is enough.

## §3 · Data model

No YAML — single hand-authored page. All copy lives directly in `autri/index.html`, sourced from the PDF text.

## §4 · Asset pipeline

8 marquee images extracted from the source PDF via `pdfimages -j` (text-heavy PDF pattern from playbook §6). Resize to max-width 1600px, JPEG q82, save as `assets/autri/<NN>-<descriptor>.jpg`. Mirror to GCS at `gs://impetus-socialpilot/rrl-portfolio/assets/autri/` and rewrite in-page paths to the `socialassets.impetusz0.de` CDN since two of the source images are >2 MB raw.

Lightbox snippet (playbook §6) embedded once at end of `<body>` so every screenshot is click-to-enlarge.

Source PDF itself copied to `assets/autri/autri-planogram-compliance.pdf` and linked from §10 Sources for the Apex reader who wants the original.

## §5 · Navigation wiring

Mega-menu link to `/autri` is **already wired** in the global topnav (line 55 of every page) under **Recent Innovations**. No new entries needed — only the placeholder note in the page itself comes off.

Home-page card check: confirmed `/autri/` is reachable from at least the Tracks mega-menu. No card on the home page yet (single-line entry under Recent Innovations is enough for v1; can promote later if asked).

## §6 · Build / verify

Local: `python3 -m http.server 8765` → `http://localhost:8765/autri/`. Auth bypass: `sessionStorage.setItem('fyndrrl_auth_v1','1')` in DevTools console.

Verify checklist (playbook §9): all images load · all sources resolve · 6 compliance dimensions match the PDF table verbatim · 4 stages and 9 outcomes match the PDF · status pills consistent with §0 honesty contract.

## §7 · Phased delivery

Single phase. ~3 hours: 1 hr asset processing + CDN mirror, 1.5 hr page authoring, 0.5 hr verify.

## §8 · Decisions

| ID | Decision | Why |
|---|---|---|
| D1 | Page name = **Autri** (the robot brand). Mention **Fynd Nucleus** once in the hero subhead as the broader system name; do not repeat. Note: the source PDF spells the system "Necleus" — corrected to **Nucleus** to match the home-grid card and the rest of the register. | Codename / brand-name dual identity rule (playbook §4). Route is `/autri/`; reader has been told "Autri" in the cover letter. |
| D2 | Phase 1 pilot named in hero: **FreshPik Powai** with Fynd Nucleus. | Confirmed against `index.html:460` home-grid card text ("Phase 1 with Fynd Nucleus at FreshPik Powai"). The PDF screenshot tenant name "Fresk Pik Powai" is the same store. |
| D3 | Status pills: **Pilot** for FreshPik Powai today; **Building** for the agentic loop end-to-end (Gmetri integration → Command Center → PulsePoint auto-ticketing → verify-by-rescan); **Roadmap** for the chain-wide rollout (Stage 4) and the 9 outcome targets. | Honesty contract per playbook §4 vision-vs-live rule. The doc itself draws this exact line ("§3.1 Today" vs "§3.2 In the Agentic Flow"). The home-grid status was already "Pilot", so we mirror it. |
| D4 | Show the original PDF as a downloadable artefact in §10 Sources. | Apex readers asked for the original `cb` brief that drove the page; one-click access via assets folder. |
| D5 | No "Connected platforms" sidebar; mention **Gmetri** and **PulsePoint** inline in the architecture and loop sections only. | Playbook §4 — drop sibling-grids, let mega-menu carry. |
| D6 | Section ordering deviates from the canonical default by **inserting §02 (compliance dimensions) before §03 (architecture)** rather than after. | Reader needs to know what counts as compliance before the architecture has anywhere to land. The PDF itself uses this ordering. |

## §9 · Open questions for the user (post-ship)

1. Where is Autri scanning today? (Pilot store/format/cluster.) Will inform a "Live · <store>" pill in the hero like Fynd Horizon's.
2. Is "Fynd Necleus" the registered name of the broader compliance system — or an internal codename to be stripped before this page goes to Apex?
3. Pilot stores for Stage 4 — known yet, or TBD pending Stage 1-3 sign-off?
4. Should the page reference the Granary platform (`/granary`) — Autri sits in the Grocery vertical and Granary is the AI-native grocery platform; is this the same product family or two parallel programs?

## §10 · Out of scope

- Per-dimension drill-downs (would need 6 sub-pages — not warranted for v1).
- Live data feed from Autri's actual dashboard (the page shows screenshots, not embedded surfaces).
- Cross-page wiring beyond the existing mega-menu link.
- Renderer / data layer — page is hand-authored single page, not a multi-sub-page renderer pattern.

---

**End of spec.**
