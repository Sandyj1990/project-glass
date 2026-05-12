# HireFirst page · Restructure spec

**Status:** v0.1 · 2026-05-01 · **drafting**
**Owner:** Kushan Shah
**Route:** `/hirefirst/` (already live; this spec restructures it)
**Source content:** `docs/hirefirst-docs-compilation/`
**Narrative anchor:** Orion is Fynd's AI-Native Hiring OS. HireFirst is the RIL-branded deployment of Orion. Page must report what is live for RIL today + the broader Orion architecture + roadmap, with vision-only capabilities tagged.
**Inherits from:** `docs/website-orientation-spec.md` · §3 page template · `website-tone-of-voice.md` for register.

**Built using:** `.claude/skills/website-section-authoring` (workflow) + `.claude/skills/website-tone-of-voice` (copy register).

---

## 0. Implementation status

| Stage | Deliverable | Where it lands |
|---|---|---|
| 0 raw | Source compilation folder | `docs/hirefirst-docs-compilation/` (release note + 26-page Orion deck) |
| 1 spec | This file | `docs/hirefirst-spec.md` |
| 2 data | Single page · no YAML; copy authored inline | `hirefirst/index.html` |
| 3 assets | 5 module screenshots + 2 architecture diagrams from Orion deck | `assets/hirefirst/{modules,diagrams}/` |
| 4 build | Hand-authored HTML (single-page section, ≤6-card rule from skill) | `hirefirst/index.html` |
| 5 nav | Already wired in mega-menu (`Special Projects` column); no new nav edits | — |
| 6 verify | Local server walk + Chrome DevTools screenshot + console clean | — |

---

## 1. Why this page exists

**Audience.** RIL Apex leadership reviewing the register. Same audience as `/impetus`, `/jcp`, `/fynd-academy`.

**Gap to close.** The current `/hirefirst` page (live, v0.8.4) reports the April-2 release note material accurately but is missing:
- The Orion architectural framing — that HireFirst is one tenant of a broader Hiring OS
- The 7-stage end-to-end hiring flow
- The 5 intelligence modules (Job, Candidate, Interview, Vendor, Decision) with their AI sub-features
- Governance & security posture (RBAC, SSO/SAML, audit, encryption)
- Tech stack
- Phased strategic roadmap (Stability → Enterprise → Integrations → Intelligence)
- Competitive landscape vs Workday, Greenhouse, Zoho Recruit, Keka, TurboHire, Expertia

**Two truth-states to honour.**
1. **Live for RIL today** — release-note material + SAP integration + 9 SIT modules. Current page covers this; restructure preserves it.
2. **Orion product vision** — broader platform capability documented in the Feb-2026 Orion deck. Some of this is shipped on Fynd's instance but not yet enabled for RIL (AI Decision Council with multi-persona orchestration, bias detection, RAG semantic search, AI proctoring). All such items get a **`Roadmap · Orion`** pill so the register stays honest.

## 2. Source inventory

| File | Type | Key facts derivable |
|---|---|---|
| `docs/hirefirst-docs-compilation/HireFirst \| Release Note & Updates \| April 2, 2026` | Plaintext channel announcement | 5 releases: Auto Enrich (Apollo.io), Instant Interview Quick Job, HireFirst branding swap, RIL Prod + SIT envs live, SAP connectivity verified |
| `docs/hirefirst-docs-compilation/Orion _ February 2026.pdf` | 26-page product deck (Google-authored) | Strategic positioning · Hiring Challenges · Orion Vision · 4-layer architecture · 7-stage flow · 5 module deep-dives (Job/Candidate/Interview/Vendor/Decision) · Governance · Live deployments (Reliance + Fynd) · Team · Tech stack · 4-phase roadmap · Competitive landscape |

**Aggregate facts to surface:**
- 9 modules live on RIL SIT (current page §02)
- 6 modules in active build (current page §03)
- 7-stage hiring flow: AI Job Creation → Intelligent Sourcing → AI Screening → Automated Scheduling → AI Interview → AI Decision Council → Offer & Governance
- 5 intelligence modules: Job, Candidate, Interview, Vendor, Decision
- 2 live deployments: Reliance + Fynd
- 4-phase roadmap: Stability → Enterprise → Integrations → Intelligence
- Competitive set: Workday, Greenhouse, Zoho Recruit, Keka, TurboHire, Expertia AI

## 3. Page structure (post-restructure)

Numbered sections. Reverses today's order slightly so the strategic frame opens, then the live-for-RIL block, then the platform deep-dive, then the roadmap.

```
§0  Eyebrow + Hero                   (existing — minor copy update to add OS framing)
§01 What HireFirst is for Reliance   (NEW — Problem → Solution → Impact, 3-col)
§02 Live for RIL today               (RENAMED from "Live on SIT" — 9 cards, today's content + April-2 releases)
§03 The Orion architecture           (NEW — embed structure.jpg diagram + 4-layer narrative)
§04 End-to-end hiring flow           (NEW — embed e2e-flow.jpg + 7-stage strip)
§05 Five intelligence modules        (NEW — 5 cards with module screenshots, RIL-live vs roadmap pill on each sub-feature)
§06 In development for RIL           (PRESERVED from current §03 — 6 modules in flight)
§07 Governance & security            (NEW — RBAC, SSO/SAML, audit, encryption, residency)
§08 Tech stack                       (NEW — Node, React, Electron, Azure Postgres/Redis, Synapse, GCP for RIL)
§09 Strategic roadmap                (NEW — 4 phases, Stability → Intelligence)
§10 Competitive landscape            (NEW — table vs Workday/Greenhouse/Zoho/Keka/TurboHire/Expertia)
§11 Built by                         (PRESERVED from current §04 — team table)
§12 Why HireFirst matters            (PRESERVED from current §05 — 3 wins + strategic context box)
§13 Sources                          (NEW — link release note + Orion deck)
Footer                               (existing)
```

### §0 Hero — copy refinements

Keep current crumb + section label + author line. Update H1 + subhead to carry the OS framing without losing the live-status reportage:

- H1: **HireFirst.** *Hiring on rails for Reliance.* (unchanged)
- Subhead update: keep the codename Orion / brand HireFirst sentence, then add *"HireFirst is the RIL-branded deployment of Orion — Fynd's AI-Native Hiring OS. Live on SIT at `ril.sit.fyndx1.de`. Production target sign-off `15-Jun-2026` at `hiring.ril.com`."*
- 4 stat tiles: keep RIL counterpart · SIT env · Prod · SAP OM sync. (Already correct.)

### §01 · What HireFirst is for Reliance

3-column block (Problem · Solution · Impact). Copy translated from Orion deck p.3 into Apex register:

- **Problem.** Fragmented ATS · manual screening · inconsistent vendor SLAs · no cross-BU talent visibility.
- **Solution.** AI-Native Hiring OS · unified workflow · AI-assisted evaluation · centralised governance.
- **Impact for RIL.** Recruiter day shifts from data entry to judgement · standardised evaluation across BUs · SAP OM remains source of truth · vendor performance becomes measurable.

### §02 · Live for RIL today

Preserve today's 9-card block. Minor copy passes for tone. Section label becomes **"02 · Live for RIL today · 9 modules shipped to SIT"**.

### §03 · The Orion architecture

- Embed `assets/hirefirst/diagrams/structure.jpg` (Orion 4-layer pyramid: Enterprise · BU/Hiring Ops + AI/Interview · Intelligence Core · Integration Layer).
- Below image, 4 short paragraphs naming each layer's job. Source line at end: *"Source · Orion product deck · Feb 2026 · p.6"*.

### §04 · End-to-end hiring flow

- Embed `assets/hirefirst/diagrams/e2e-flow.jpg` (7-stage strip).
- Below image, 7 small cards naming each stage with one factual line + a `Live for RIL` or `Roadmap · Orion` pill:
  - 01 AI Job Creation — `Live (basic)` · Quick Job Creation shipped 02-Apr; Prompt-to-JD on roadmap
  - 02 Intelligent Sourcing — `Roadmap · Orion`
  - 03 AI Screening — `Live` · resume scoring + downvote feedback loop
  - 04 Automated Scheduling — `Live (partial)` · email templates + manual scheduling; auto-assign on roadmap
  - 05 AI Interview — `Roadmap · Orion` · Interview Chatbot in build for RIL
  - 06 AI Decision Council — `Roadmap · Orion` · multi-persona orchestration not yet enabled for RIL
  - 07 Offer & Governance — `Live (partial)` · offer routing manual; digital offer on roadmap

### §05 · Five intelligence modules

5 cards in a 2-3 grid. Each card = one Orion module with screenshot + 3 sub-features. Sub-features carry the RIL-live vs Orion-roadmap pill explicitly (per §1 honesty rule).

| Card | Image | Sub-features (with pills) |
|---|---|---|
| **01 · Job Intelligence** | `modules/job.jpg` | Prompt-to-JD `Roadmap · Orion` · Similar Job Detection `Roadmap · Orion` · Auto Stage Configure `Roadmap · Orion` · Quick Job Creation `Live · RIL` |
| **02 · Candidate Intelligence** | `modules/candidate.jpg` | Semantic / RAG search `Roadmap · Orion` · Automated dedup `Roadmap · Orion` · Profile enrichment via Apollo.io `Live · RIL` |
| **03 · Interview Intelligence** | `modules/interview.jpg` | Real-time transcription `Roadmap · Orion` · Intelligent follow-ups `Roadmap · Orion` · Bias detection `Roadmap · Orion` · Auto interview summary `Roadmap · Orion` · Instant Interview flow `Live · RIL` |
| **04 · Vendor Management** | `modules/vendor.jpg` | SLA tracking `Roadmap · Orion` · Vendor ranking `Roadmap · Orion` · Conversion analytics `Roadmap · Orion` · Status control `Roadmap · Orion` |
| **05 · AI Decision Council** | `modules/council.jpg` | Multi-model orchestration `Roadmap · Orion` · Persona configuration `Roadmap · Orion` · Consolidated reporting `Roadmap · Orion` |

### §06 · In development for RIL

Preserve today's 6-card block (Ideal Candidate Profile, Interview Chatbot, AI prompt autofill, Native SAP, LinkedIn extension, Domain split). These are RIL-specific in-flight items.

### §07 · Governance & security

4-row table (Access · Auth · Monitoring · Data Protection) per Orion deck p.18. Each row notes RIL-live vs Orion-platform status:

| Layer | Capability | RIL status |
|---|---|---|
| Access | RBAC · org isolation · BU segregation | Live · partial (RBAC live) |
| Auth | SSO / SAML · MFA | Roadmap · Orion |
| Monitoring | Audit logs · real-time security alerts | Live · Cloud Run + GCP audit |
| Data Protection | E2E encryption · enterprise data residency | Live · IDC GCP residency |

### §08 · Tech stack

Compact 4-column block. Source · Orion deck p.21:

- Languages · Node.js · TypeScript · React · Electron
- Database · Azure PostgreSQL (Fynd) / Cloud SQL Postgres (RIL) · Redis cache · Firebase
- Cloud · Azure (Fynd) · GCP via IDC connectivity (RIL) · Event Hub · Service Bus · Cloud Run · Bastion · Artifact Registry
- CI/CD · GitHub + GitHub Actions
- Data warehouse · Synapse Analytics
- Storage · Azure Blob

### §09 · Strategic roadmap

4-phase strip per Orion deck p.23:

- **Phase 0 · Stability** — infra hardening · perf optimisation · critical bug fixes
- **Phase 1 · Enterprise** — advanced RBAC · SSO/SAML · multi-tenant architecture for scale
- **Phase 2 · Integrations** — deep ERP, HRIS, third-party assessment connectivity
- **Phase 3 · Intelligence** — predictive workforce analytics · cross-BU talent reuse · advanced AI matching

### §10 · Competitive landscape

Table per Orion deck p.24. 6 capability rows × 3 columns (Traditional ATS · Point AI tools · Orion). Logos at bottom row: Workday, Greenhouse, Zoho Recruit, Keka, TurboHire, Expertia AI.

### §11 · Built by

Preserve today's 8-row team table.

### §12 · Why HireFirst matters

Preserve today's 3-card win block + strategic context box.

### §13 · Sources

- `docs/hirefirst-docs-compilation/HireFirst | Release Note & Updates | April 2, 2026`
- `docs/hirefirst-docs-compilation/Orion _ February 2026.pdf` (26pp)
- Live envs: `https://hiring-ril.sit.fyndx1.de/` · `https://hiring.ril.com` (target Prod)

## 4. Data model

No YAML. Single-page section with hand-authored HTML (per skill §1: ≤6 sub-pages → hand-author). All copy lives in `hirefirst/index.html`.

## 5. Asset pipeline

- 5 module screenshots from Orion PDF pages 8, 10, 12, 14, 16 — extracted via `pdftoppm -r 220 -jpeg -jpegopt quality=85`, resized to 1600px wide via `sips -Z 1600`.
- 2 architecture diagrams from PDF pages 6, 7 — same pipeline.
- Output: `assets/hirefirst/modules/{job,candidate,interview,vendor,council}.jpg` + `assets/hirefirst/diagrams/{structure,e2e-flow}.jpg`.
- All under 350KB. Total <1.6MB. No GCS mirror needed (under skill threshold of 20 files / 100MB).

## 6. Navigation wiring

Already wired. `/hirefirst` appears in the mega-menu **Special Projects** column on every page that has the v0.8.4 nav. No new edits needed.

## 7. Build / verify

- Hand-author update to `hirefirst/index.html`.
- Local: `python3 -m http.server 8000` then visit `http://localhost:8000/hirefirst`.
- Chrome DevTools MCP: `evaluate_script` to set `sessionStorage.fyndrrl_auth_v1='1'`, `take_screenshot fullPage:true`, `list_console_messages`.

## 8. Phased delivery

| Phase | Scope | Time |
|---|---|---|
| **P1** | Spec (this file) | done |
| **P2** | Asset extraction (5 modules + 2 diagrams) | done |
| **P3** | Restructure `hirefirst/index.html` per §3 above | ~90 min |
| **P4** | Local verify · screenshot · console clean | ~15 min |

## 9. Decisions (confirmed 2026-05-01 with user)

1. **Scope** — Full restructure around Orion narrative arc, not surgical addition.
2. **Vision vs live** — Mark all Orion-but-not-yet-RIL capabilities with explicit `Roadmap · Orion` pill. Apex register honesty rule.
3. **Asset extraction** — Extract all 5 module screenshots + 2 architecture diagrams from Orion PDF and embed.

## 10. Out of scope (this pass)

- Per-module sub-pages (`/hirefirst/job-intelligence/` etc.) — single page is enough for v0.9.
- Animations, video embeds (Orion deck p.25 user-guide video isn't in compilation folder).
- GCS mirror (assets are small).
- Updating other pages' nav blocks (already correct).

---

**End of spec.** Implementing immediately per user instruction.
