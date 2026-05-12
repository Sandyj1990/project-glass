# /jcp/cataloging · page spec · v0.9.1

**Page:** `jcp/cataloging/index.html` · `https://reliance-retail-fynd.vercel.app/jcp/cataloging`
**Version:** v0.9.1 (v0.8.4 baseline · v0.9.0 added §03 Showcased · v0.9.1 applied audit findings F1-F3)
**Owner (page):** Kushan Shah
**Subnav:** child of `/jcp` · siblings: Overview · Channels · AI Cataloging · 7-Eleven · Release Notes · RBL · RCPL

---

## §1 · Audience and intent

RIL Apex (MM Sir level). Reports on Fynd's AI-cataloging pipeline (Web Grounding · Gemini multimodal · web grounding · CAM sheet intelligence) deployed across Reliance brands. Three-step chain of evidence: **measured** (against existing manual processes at Netmeds and Reliance Digital), **shipped** (live in production for Tira × Akind), **showcased** (Google Cloud Next '26 keynote, 29-Apr-2026), with **methodology** that explains how every accuracy number on the page is calculated.

---

## §2 · Source compilation

| Source | Path / URL | Used for |
|---|---|---|
| Accenture deck · 16-Apr-2026 · slide 19 | `docs/accenture-2026-04-16-compilation/all-slides-text.md` · slide 19 | §00 pitch summary (15 days → 5 hours) |
| Netmeds + Reliance Digital throughput study | Internal benchmarks (referenced in §01 prose) | §01 measured · table comparisons |
| Tira × Akind release-noted milestone | Release notes · production log | §02 shipped · 89% accuracy / 332-of-382 attributes / ~14 sec |
| Google Cloud Next '26 opening keynote | `https://www.youtube.com/live/11PBno-cJ1g?t=4843` + Slack/announcement post (2026-05-01) | §03 Showcased · Gemini multimodal + web grounding + CAM sheet intelligence detail |
| Attribute-Accuracy methodology | Internal · embedded in page §04 | §04 methodology · verdict bucketing |

---

## §3 · Page structure

| § | Section label | Anchor | Purpose |
|---|---|---|---|
| Hero | JCP · AI Cataloging · Live | — | Title · subhead · 4-card "What's on this page" nav (#throughput · #shipped · #showcased · #methodology) |
| §00 | Accenture · 16-Apr-2026 · slide 19 | — | Pitch summary · 15 days → 5 hours · 4-image strip |
| §01 | 01 · Measured · Throughput across brands | `#throughput` | Netmeds vendor-replacement + Reliance Digital in-house comparisons |
| §02 | 02 · Shipped · Live in production | `#shipped` | Tira × Akind · 89% accuracy · 332/382 attributes |
| §03 | 03 · Showcased · Google Cloud Next '26 main stage | `#showcased` | Catalog enrichment with Gemini · 3-card I/O/Reach explainer · what-this-delivers list |
| §04 | 04 · How we know · Methodology | `#methodology` | Attribute-Accuracy verdict bucketing |
| Footer | © 2026 RRVL · Jio Platforms Limited · Fynd · Strict internal circulation only | — | Standard |

---

## §9 · Decisions

**D1 · §03 Showcased was inserted between §02 Shipped and §04 Methodology, not appended at the end.**
*Why:* The keynote moment validates what shipped (§02). Showcased belongs adjacent to Shipped, not after the Methodology deep-dive. Reader scans top-down: measured → shipped → showcased → methodology.
*How to apply:* Future keynote/recognition events related to AI Cataloging continue to live at §03 (or under it). Methodology stays last as the "how we know" appendix.

**D2 · No Fynd-IC names in §03 subhead or body.**
*Why:* Tone-of-voice §6 last subsection (worked example: `/jcp/` v0.7 dropped 'Lead: Vidit Kumar Gupta'). The source Slack post named ~7 Fynd ICs (Kapil, Manish Kumar, Bijan Kundu, Abhishek Gupta, Shubham Negi, Abhishek Jain, Shriyash) plus lead Ashish Chandorkar. None surfaced on the page.
*How to apply:* Page-level DRI (when needed) lives in the footer Owner line. Cross-page DRI continuity sits on `catalog/index.html:147` (JIIA team list).

**D3 · §03 Reach card carries explicit Live/Measured/Build status row.**
*Why:* Audit F2 flagged the original wording ("One enriched catalog layer feeds RD · JioMart · Tira · AJIO · Netmeds") as overclaim — only Tira × Akind is Live; Netmeds + RD are Measured (per §01); JioMart + AJIO at-scale are in Build. The status row makes the destination-vs-state distinction explicit.
*How to apply:* When any of the channels move to Live, update the row pills. Do not soften the per-channel honesty contract.

**D4 · No §08 Sources block.**
*Why:* Tone-of-voice §3 default-no rule. Inline source eyebrows under each section cite the relevant artefact. Worked examples: `/jcp/`, `/jcp/release-notes/`, `/jcp/7eleven/`, `/jcp/channels/` all dropped Sources blocks in feedback rounds 3-4.
*How to apply:* Provenance lives in inline citations + this spec.
