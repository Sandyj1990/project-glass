# /kaily · page spec · v0.9.3

**Page:** `kaily/index.html` · `https://reliance-retail-fynd.vercel.app/kaily`
**Version:** v0.9.3 (v0.9.1 rebuild · v0.9.2 applied audit-v2 findings · v0.9.3 added Google Cloud Next '26 keynote detail to §05 JIIA + two CDN keynote screenshots)
**Owner (page):** Kushan Shah · **Owner (Kaily-on-RR):** Sreeraman MG (footer line only, per D5)

---

## §1 · Audience and intent

RIL Apex (MM Sir level). Reports the Live Reliance Retail Kaily footprint — three production agents (ZIP on AJIO, JIIA on JioMart, Netmeds Assistant) — plus the platform shape that powers them.

Page exists because Farooq's MDA letter (2026-04-30) names Kaily as agentic commerce live in JioMart and AJIO; the home register and `/autonomous` further establish Netmeds Assistant as the canonical Live RR Kaily proof. This page consolidates all three on one surface.

---

## §2 · Source compilation

| Source | Path | Used for |
|---|---|---|
| Kaily Master Deck · 2026 | `docs/kaily-notes-compilation/Kaily Master Deck | 2026 .pptx` (50 slides) | Hero, §01, §02 (Talks/Thinks/Acts framework slide 4), §03 (architecture slide 6), §04 (slide 26 ZIP numbers), §07 (slide 36 pillars) |
| Accenture deck · 16-Apr-2026 · slide 37 | `docs/accenture-2026-04-16-compilation/all-slides-text.md` | §04 ZIP image + secondary numbers |
| Farooq cover letter · 30-Apr-2026 | `docs/2026-04-30-farooq-mda-update-letter.md` | Hero scope (named JioMart + AJIO Kaily) |
| `/autonomous` register · §08 AI Customer Service agent | `autonomous/index.html` lines 210-216, 321-329 | Hero count, §01 Impact, §06 Netmeds Assistant numbers + Sreeraman MG DRI |
| Google Cloud Next '26 opening keynote · 29-Apr-2026 | `https://www.youtube.com/live/11PBno-cJ1g?t=4843` + two stage screenshots on `gs://impetus-socialpilot/rrl-portfolio/assets/kaily/google-cloud-next-26/` (`keynote-jiia-birthday-party.png`, `keynote-customer-logos.png`) | §05 JIIA detail (birthday-party intent example, Gemini multimodal pipeline, customer-deployment showcase framing) |

---

## §3 · Page structure

| § | Section label | Purpose |
|---|---|---|
| Hero | AI-Native · Agentic commerce + service · Kaily · Live on AJIO, JioMart, and Netmeds | 3-agent count, scope, headline numbers (ZIP 88%, JIIA Google Cloud Next '26, Netmeds 850K/96%), DRI Sreeraman MG, 3 stat tiles |
| §01 | What Kaily is for Reliance | Problem · Solution · Impact · 3-card with 3-agent stat span (88% ZIP, 96% Netmeds, 40M+ JIIA) |
| §02 | Capability framework · Talks · Thinks · Acts | 3-card capability frame from deck slide 4 |
| §03 | Architecture · the full-stack system | 4-layer diagram (Channels → Agent core → Data sources → Live retail systems) from deck slide 6 |
| §04 | AJIO · ZIP · live | Pill `Live · RR · AJIO`, 3-stat block (88% / 90% / 100% catalog 2.6M+), Challenge/Solution/Outcome cards, slide_37 image |
| §05 | JioMart · JIIA · live · Google Cloud Next '26 | Pill `Live · JPL · JioMart`, 3-stat block (40M+ / Gemini / Live), team list with Ashish Chandorkar lead |
| §06 | Netmeds · AI customer service agent · live | Pill `Live · RR · Netmeds`, 3-stat block (850K / 96% / Live · DRI Sreeraman MG), Stack/Outcome/Next cards |
| §07 | Why Kaily · platform fit for Reliance | 6 pillars — last pillar is "Reliance vertical fluency" linking the 3 deployments to one fabric |
| Footer | © 2026 RRVL · Jio Platforms Limited · Fynd · Strict internal circulation only · `Owner · Sreeraman MG · Kaily-on-RR` (mono · D5) | Standard + page-level DRI line |

---

## §4 · Cross-page surfaces touched

- `index.html:314` ZIP stats updated to canonical set (88% +ve CX · 100% catalog (2.6M+ SKUs) · 90% chats helped discovery)
- `catalog/index.html:146` ZIP row updated (same)
- `catalog/index.html:147` JIIA team list updated (Lead · Ashish Chandorkar · 8 names)
- `catalog/index.html:298` AI Search Vertex row ZIP evidence updated
- `autonomous/index.html:221, 335` ZIP evidence updated

---

## §9 · Decisions

**D1 · §02 holds capability framework, not module status table.**
*Why:* Page has only three live RR agents (small surface area). A "what's live" module table at §02 would duplicate §04/§05/§06.
*How to apply:* Capability framework (Talks/Thinks/Acts) sits at §02; per-agent modules at §04-§06.

**D2 · Brand-customer references (Being Human, GUESS, Cole Haan) excluded.**
*Why:* Kaily Master Deck slides 27-29 do not establish AJIO channel or RR context for these deployments — they describe each brand's own e-commerce assistant. Including them would repeat the category-error pattern caught in the Boltic v0.9.4→v0.9.5 audit (attributing Ratl AJIO×JCP test estate to Boltic).
*How to apply:* If a future spec wants to surface these for credibility, do so on a separate Kaily.ai marketing surface, not on the RR register.

**D3 · No Boltic-as-backbone pillar.**
*Why:* Deck slide 15 shows Boltic powering an EMI-query example in the BFSI vertical only; no source establishes that ZIP, JIIA, or Netmeds Assistant route through Boltic.
*How to apply:* If Sreeraman MG / Punit Kalro confirm Boltic underpins any of the three RR agents, add a pillar with that source.

**D4 · Netmeds numbers cite the /autonomous register, not the Kaily deck.**
*Why:* The Kaily Master Deck has no Netmeds slide. The 850K msgs / 96% favourable figures live in `/autonomous` (`§08 AI Customer Service agent` and per-IP detail card at line 321), with Sreeraman MG as the DRI.
*How to apply:* If a Netmeds-specific source (status report, screenshot) becomes available, replace the cross-reference with the primary citation.

**D6 · Google Cloud Next '26 keynote detail enriches §05 JIIA, not a new section.**
*Why:* The keynote is a recognition / validation event for the JIIA deployment that already had its own §05 — splitting it into a new section would fragment the JIIA narrative. Two CDN-hosted stage screenshots embedded in §05 (birthday-party intent flow + customer-deployment logo wall with Reliance Retail). The catalog-enrichment-with-Gemini foundation that powers JIIA gets its own section on `/jcp/cataloging/` §03 Showcased, with cross-link.
*How to apply:* Keep keynote-specific evidence (Gemini multimodal pipeline, structured attribute extraction, customer-deployment showcase) anchored to §05. Cataloging foundation lives on `/jcp/cataloging/`. No Fynd-IC names per D5.

**D5 · No §08 Sources block. Page-level DRI in footer only.**
*Why:* Tone-of-voice §3 default-no rule for Sources blocks (provenance lives in inline source eyebrows under each section; §08 block repeats what eyebrows already disambiguate; worked examples /jcp/, /jcp/release-notes/, /jcp/7eleven/, /jcp/channels/ all dropped Sources blocks in feedback rounds 3-4). Tone-of-voice §6 last subsection: don't name Fynd ICs in section subheads (worked example: /jcp/ v0.7 dropped 'Lead: Vidit Kumar Gupta' from Vertex Search subhead). Both rules added after the v1 audit; applied via v0.9.2 fix pass.
*How to apply:* No §08 block; every cited fact carries its inline eyebrow. Page-level DRI sits as a single mono line in the footer (`Owner · Sreeraman MG · Kaily-on-RR`). Cross-page DRI continuity preserved by `catalog/index.html:243` and `/autonomous` references.
