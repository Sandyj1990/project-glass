# Dark Factory · spec

**Mode:** update / restructure (page exists at `dark-factory/index.html`; spec backfilled after the page reached v3 — captures the as-built shape so future revisions follow the lifecycle).

**Status:** shipped · v4 · 2026-05-03

**Owner:** Fynd-side DRI pending. Reliance-side DRI for the alpha trial: pending the decision-ask sign-off referenced in the 30-Apr-2026 letter to MM Sir.

**Route:** `/dark-factory/`

**Source content:**
- `docs/mtm-notes-compilation/Mobile Neo Tailor Concept Note.pdf` — 11-page concept note · 30-Apr-2026 · canonical source for v4 · supersedes the formatted markdown
- `docs/mtm-notes-compilation/Mobile_Tailor_Concept_Note_Formatted.md` — earlier markdown formatting of the concept note (kept for diff reference)
- `docs/mtm-notes-compilation/Custom made Clothing 300426 (1).pptx` — 18-slide deck on factory internals (body measurement, pattern engineering, cutting, sewing, finishing, folding, factory area workings, indicative layout, personalization, customer benefits)
- `docs/mtm-notes-compilation/MTM- process flow.pptx` — process-flow deck for demand + supply loops
- `docs/2026-04-30-farooq-mda-update-letter.md` — Apex cover letter naming Dark Factory under Recent Innovations

**Narrative anchor:** Dark Factory is the lights-out, Reliance-owned manufacturing back-end that scales Fynd Horizon's MTO promise beyond the Tirupur partner factory. Concept-note title is "Mobile Neo Tailor"; the Apex-facing register name (per the cover letter) is "Dark Factory (Made to Measure)". Page uses **Dark Factory** as the primary brand (factory-side framing) and **Mobile Neo Tailor** as the customer-facing app surface name (per v4 PDF rename · the in-app short form is **M-Tailor**).

---

## §0 · Implementation status

| Stage | Artefact | Status |
|---|---|---|
| 0 raw | `docs/mtm-notes-compilation/` (4 files) | ✓ |
| 1 spec | `docs/dark-factory-spec.md` (this file, backfilled) | ✓ |
| 2 data | n/a (single-page section, no YAML schema) | ✓ |
| 3 assets | `assets/dark-factory/01-cutting-morgan-italia.jpg`, `02-sewing-juki-automat.jpg`, `03-folding-epa-5001.jpg` (3 product photos extracted from deck) | ✓ |
| 4 build | hand-authored `dark-factory/index.html` (single page, no renderer) | ✓ |
| 5 nav | mega-menu entry in all sibling pages (consistent); home-page card at `index.html:188` | ✓ |
| 6 verify | local dev server + Chrome DevTools MCP audit · v3 audit JSON at `docs/audits/dark-factory-audit-2026-05-02-v3.json` | ✓ |

---

## §1 · Audience · why this page exists

**Audience:** RIL Apex leadership (MM Sir level).

**Gap closed:** The 30-Apr-2026 cover letter to MM Sir names "Dark Factory (Made to Measure)" under Recent Innovations. The page exists so the link in the letter resolves to a real artefact rather than a placeholder. Apex needs to see what Dark Factory is, how it relates to Fynd Horizon (the live front-end), what the factory internals look like, and what decision is pending.

**Narrative anchor:** Front-end captures the customer (Horizon); Dark Factory makes the garment. The proposal asks for capex and an alpha trial sign-off; the page is honest that nothing is built yet.

---

## §3 · Page structure

11 sections + hero. Section labels run contiguously 01-11.

| § | Section | Purpose | Notes |
|---|---|---|---|
| 0 | Hero | H1 + 14-word PDF tagline deck + 49-word intro paragraph + Three Goals 3-card grid + Operating intent card | See D15 for the deck-vs-body two-line treatment. No Live pills. |
| 01 | How this fits · Customer → Horizon → Dark Factory → Doorstep | Native 4-card flow with SVG arrows; Dark Factory is the inverted dark anchor | Establishes the front-end / back-end split up-front |
| 02 | Status · 30-Apr-2026 | 3-col Specified / Pending / Roadmap | Honest about what's pending sign-off |
| 03 | Strategic shift | 6-row comparison table (ready-made/tailor → Dark Factory) + customer-promise card | |
| 04 | Customer journey · 8 steps · two entry points | Two entry blocks (Home / Store) + 8 numbered step cards matching v4 PDF revision (Discover / Companion / M-Tailor tab / Pick / Scan / Adjust / Customise+pay / Track+receive) + YouTube short embed (XKxBTMx7RWk) | Step 7 (Customise + pay) is the accent step |
| 05 | What the customer customises · 4 levers | Design / Fabric / Trims / Embroidery as 4 cards + framing footer card | Added in v4 from PDF page 3. Carries Proposal pill. |
| 06 | Factory internals · how a single garment is made | Native body-measurement SVG diagram + 5 equipment cards (Pattern · Cutting · Sewing · Finishing · Folding) | 3 product photos from the deck; cards 2 + 5 text-only |
| 07 | Factory layout · 15,326 sq ft · single floor | Native floor-plan diagram (Zone A entrance / Zone B Cutting / Zone C Sewing / Zone D south wall) + 3 annotation cards | Carries Proposal pill; positions sourced from concept note |
| 08 | Live Kitchen · the customer watches her garment get made | 5-stage horizontal timeline with photo placeholder zones | Photo zones swap to real customer-stage photos at alpha |
| 09 | Operating model · two loops, one customer | Demand loop (in app) + supply loop (in factory) | |
| 10 | Outcomes · customer wins + business wins | 4 customer-win cards + 4 business-win cards in a paired column layout, each with a single tracked metric (alpha → gamma) | Recast in v4 from the prior 10-row table. Carries Proposal pill. NO capex line per D4 update. |
| 11 | Phase-gate plan | Alpha / Beta / Gamma cards with exit criteria | Exit criteria sourced; dates pending sign-off |

---

## §9 · Decisions (overrides + key calls)

| ID | Decision | Why | How to apply |
|---|---|---|---|
| D1 | No §03 Architecture in canonical position | Page is operational concept (a manufacturing line), not an engineering platform with software architecture layers. Replaced with §03 Strategic shift. | Page-reviewer audits should not flag the canonical §03 Architecture absence as a structural gap. |
| D2 | No "What's live" section | Page is proposal-stage; nothing is live. The §02 Status block carries the proposal-state explicitly. | Apply Live pills only to Fynd Horizon (cross-section reference in §01); never to anything Dark Factory builds. |
| D3 | Two custom deep-dive sections (§05 Factory internals + §06 Factory layout) | The deck (Custom made Clothing pptx) has 18 slides of factory-internals depth that the concept note compresses to a few lines. Apex needs the depth on the page, not buried in the deck. | Sections sit between Customer journey (§04) and Live Kitchen (§07). |
| D4 | **No capex anywhere on the page** (v4 update) | Per user direction 2026-05-03: "Capex is not to be included anywhere. Its only for the proposal page. Our page is a showcase of the work being done." Supersedes the v3 carve-out that allowed the headline ₹8.27 Cr in the hero / §02. The full capex story (headline number, line items, payback) lives only in the concept-note proposal. | Do not surface ₹8.27 Cr, payback, or the 18-row equipment table on the page. Operational facts (200 pieces / day, 15,326 sq ft, alpha/beta/gamma capacity ramp) stay. The home page card and platform registry must also avoid capex framing — see audit `docs/audits/dark-factory-audit-2026-05-03.json` finding H1. |
| D5 | No §Decision Ask on page | Same reasoning as D4 — the asks live in the proposal note. The §02 Status block still surfaces "what's pending sign-off". | Do not re-add a Decision Ask section. |
| D6 | No §Unit Economics on page | Same reasoning — pricing-detail tables live in the proposal note. | Do not re-add. |
| D7 | No §Sources block | Per skill rule update (commit e867725 · always-remove). Provenance lives in inline `Source · …` lines (hero), this spec, and git history. | Do not add a §Sources block to this or any other page. |
| D8 | Body-measurement diagram is a native SVG, not the deck infographic | Per user direction (this session): "build a native diagram in our design language instead of directly using from the raw material". The 14 measurement points and the 4 signal sub-cards are sourced; the silhouette is stylized. | When the figure needs revision, edit the SVG path inline in `dark-factory/index.html` §05 Card 1; do not embed a raster diagram. |
| D9 | Factory layout is a native CSS-grid floor plan, not the deck EMF | Same reasoning — slide 15 is an EMF (Windows vector) that doesn't render in browsers and isn't in our register. Rebuilt as a 4-zone grid in our card vocabulary. | When zone breakdown changes (e.g. percentages confirmed from slide 14), update the §06 zone cards inline. |
| D10 | Equipment photos use deck source as-is | Per user direction (this session): real-world artifact photos (machinery in a factory) are not "designed diagrams in someone else's register" — they're product/factory photographs. Wrapped in our card vocabulary; lightbox-clickable. | When new equipment photos arrive, place under `assets/dark-factory/<NN>-<descriptor>.jpg`, max 1600px wide, JPEG q82. |
| D11 | Vendor name reconciliation: Morgan Italia | Both source documents say "Morgan Italia" (concept note rows 5-7 capex table; deck slide 7 caption). Product photo on the equipment shows "MorganTecnica" branding — Morgan Tecnica srl is the Italian manufacturer in Carpi. v3 audit M1 flagged the page using "Morgan Tecnica"; corrected to "Morgan Italia" to match source. | Match the source documents. If a future source clarifies the brand-name canonical, update both the page and this entry together. |
| D12 | Hero subhead at 29 words, lead with `30-second` | tone-of-voice §5 caps hero subhead at 30 words. Subhead follows formula: lead-number → scope → differentiator. | When updating, keep ≤30 words and lead with the headline number. |
| D13 | Reliance Trends full name on first mention | tone-of-voice §7 entity-name list. First mention in hero subhead, §03 lead-in. Subsequent body mentions can elide to "Trends". | Apply to any new sections that mention Trends. |
| D14 | YouTube short embed in §04 | Customer-journey demo video (https://www.youtube.com/shorts/XKxBTMx7RWk) embedded as iframe in §04 below the 8 steps · vertical 9:16 aspect-ratio frame, max-width 280px, lazy-loaded. Sits in a 12-col card with copy on the left (col-7) and the iframe on the right (col-5). | If the video URL changes, update the iframe `src` and the `Open on YouTube` link together. If the embed proves unreliable, replace with a static thumbnail linking to the YouTube short. |
| D15 | Hero deck-vs-body two-line treatment | The PDF tagline ("A tailor inside the AJIO app. Designed in 2 minutes. Delivered in 7 days.") is the **canonical hero subhead** at 14 words — passes the ≤30-word rule from tone-of-voice §5. The 49-word body paragraph that follows it is **intro prose**, not a subhead — its job is to introduce the Mobile Neo Tailor / Dark Factory naming pair and is unconstrained by the subhead word-cap. | When the hero is revised, treat the deck line as the constrained subhead; treat the body paragraph as flexible intro prose. |
| D16 | Mega-menu suffix uses Mobile Neo Tailor | Per v4 PDF rename, the mega-menu suffix for `/dark-factory` is `Mobile Neo Tailor` (not `made-to-measure`). Set in `tools/site_chrome.py` RECENT_INNOVATIONS; sweep applied to all 70 pages via `python tools/inject_chrome.py`. | Edit `tools/site_chrome.py` and run inject_chrome — never edit per-page nav HTML directly (it gets reverted on next sync). |
| D14 | Lightbox infrastructure: present when ≥1 product photo binds, stripped otherwise | v1 had zero photos and shipped lightbox dead-code (audit L2). v3 has 3 product photos so the lightbox is wired with `a.js-lightbox` + `img.zoomable`. | If photos are removed in a future revision and the page goes back to text-only, strip the lightbox CSS + markup + script. |

---

## §10 · Out of scope

- Cost comparison tables (PDF page 5) — proposal-document content; page intentionally does not carry these (D4/D5/D6).
- ~~Personalization options~~ — moved on-page in v4 as §05 (4 customisation levers from PDF page 3). No longer out of scope.
- Customer benefits prose (slide 18) — overlaps with §03 Strategic shift; not added.
- Factory area workings (slide 14) — EMF source; per-zone floor percentages were briefly fabricated in v3 (audit H1) and dropped in the H1 fix. If the EMF is converted and the percentages confirmed, re-add to §07 zone cards (renumbered from §06 in v4).
- Spec for the Mobile Neo Tailor app surface itself — that's a product-spec, not a register-page spec.
- Capex headline number, equipment line items, payback — all proposal-only per D4 (v4 update). Off the showcase page entirely.
- Decision Ask block, Unit Economics table, per-piece selling prices — all proposal-only per D4/D5/D6.

---

## §11 · Audit history

| Date | Version | Score | Grade | Notes |
|---|---|---|---|---|
| 2026-05-02 | v1 | 86 | B | Initial build · `docs/audits/dark-factory-audit-2026-05-02.json` |
| 2026-05-02 | v2 | 86 | B | Re-audit after deeper protocol pass · `docs/audits/dark-factory-audit-2026-05-02-v2.json` |
| 2026-05-02 | v3 | 88 | B+ | Post-restructure (factory internals + layout added) · `docs/audits/dark-factory-audit-2026-05-02-v3.json` |
| 2026-05-02 | v3 fix-pass | (pending re-audit) | — | H1 fab percentages dropped · M1 Morgan Italia · M2 §06 Proposal pill · L1 silhouette improved · L3 Card 1 H3 reworded · M3 spec backfill (this file) |
| 2026-05-03 | v4 | 83 | B | PDF v2 (Mobile Neo Tailor Concept Note.pdf) consumed · `docs/audits/dark-factory-audit-2026-05-03.json` · Mobile Neo Tailor naming added to hero · Three Goals block in hero · §04 8-step diagram rebuilt to PDF revision · YouTube demo card embedded in §04 · new §05 customisation levers section · §06-§11 renumbered · §10 outcomes recast as paired Customer / Business Wins · capex stripped per D4 update |
| 2026-05-03 | v4 fix-pass | (pending re-audit) | — | H1 home-card capex stripped · H2 home-registry author line dropped · H3 Mobile Tailor → Mobile Neo Tailor sweep · M1+M2 §05 currency+pricing dropped · M3 Proposal pills on §05+§10 · M4 p-7 → p-6 · L2 verb-command rephrased · L3 fallback disclaimer cut · L4 mega-menu suffix swept to Mobile Neo Tailor (70 pages) |
