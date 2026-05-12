# AI Photoshoot · update spec

**Status.** Draft → in progress (v1)
**Owner.** Kushan Shah
**Route.** `/impetus/ai-photoshoot/`
**Mode.** UPDATE / RESTRUCTURE — page already lives at the route; replacing internals from a new source deck.
**Source.** `docs/WIP | Snap.pptx` (38 slides, 89 embedded images, May 2026 product collateral) plus the existing Q1 2026 Release Compendium adoption stats already on the page.

---

## §0 · Implementation status

| # | Stage | Status |
|---|---|---|
| 0 | Raw collected to `docs/snap-compilation/raw-extract/` | ✓ |
| 1 | Spec | ✓ (this file) |
| 2 | Data | n/a (single page, inline content) |
| 3 | Assets curated + uploaded to GCS | ⚠ in progress |
| 4 | Page authored | ⚠ in progress |
| 5 | Nav wiring | ✓ no change (page exists; landing tile + crumb already correct) |
| 6 | Verify + audit | ✗ |

---

## §3 · Page structure (Add / Keep / Remove diff)

Current page (pre-update) shape:
- §01 hero · IMPETUS · AI PHOTOSHOOT · LIVE
- §02 What it does for you
- §03 How Many People Use It
- §04 What improved
- §05 Updates shipped (timeline)
- §06 Screenshots (3 platform UI captures)
- §07 Output gallery (links to /impetus/photoshoots sub-pages)

New page (post-update) shape — deck-first, Reliance-as-credibility:

| § | Title | Source | Action |
|---|---|---|---|
| 0 | Hero | deck S01 + existing FY26 stats | **Replace.** Hero subhead from S01. Codename "Fynd Snap" mentioned once. Stats tiles preserved (verbatim from current §01 stat card values). |
| 01 | What it does for you | deck S04-S05 (8 capabilities) + S03 (5 differentiators) | **Replace.** Two stacked sub-blocks: 8 capability cards (Flatlay→Model, Mannequin→Model, Model Swap, 3D Render→Model, AI Videos, Face Consistency, Ensemble Shots, Face Swap) followed by a "Why this approach" 5-bullet differentiator strip. |
| 02 | Why AI photoshoot · the problem with traditional | deck S02 + S06 | **Add.** 5-card problem grid (cost, representation, time-to-market, video need, conversion impact) + a Traditional vs AI Photoshoot comparison row taken from S06. |
| 03 | Examples · input → output | deck S08-S26 | **Add.** 10 curated example cards. Each card shows input image, 1-2 outputs, capability label. Curated to cover every capability category at least once (Mannequin, Flatlay, 3D Render, Ensemble, Video, Product, Kidswear). |
| 04 | Platform screenshots | deck S30-S32 | **Replace.** 3 UI captures, lightboxed, captioned. |
| 05 | Collaboration · how a brand onboards | deck S33-S37 | **Add.** 5-step horizontal flow (Brand Onboarding → Input Review → Creative Alignment → Sample Round → Delivery + Feedback). |
| 06 | Reliance adoption · today | existing §03 + §04 + §05 content | **Compress.** Pull the strongest stats (~4,000 videos · 88% first-pass · 90% cost reduction · 25K+ photoshoots on Tira) into a single status strip. Keep timeline `<details>` for those who want it. |
| 07 | Output gallery → /impetus/photoshoots | existing §07 | **Keep.** Single CTA card linking to the photoshoots gallery (the user explicitly asked for this link). |

Removed from current page:
- §03 "How Many People Use It" — folded into §06 status strip
- §04 "What improved" — folded into §06 status strip
- §05 timeline — collapsed into a `<details>` block inside §06

---

## §6 · Asset pipeline

- 89 raw images extracted from `docs/WIP | Snap.pptx` to `docs/snap-compilation/raw-extract/` via python-pptx.
- Curate 10 example cards (input + output pairs), 3 platform screenshots, 5 collaboration step diagrams (text-only — no extraction needed for collab slides).
- Resize to ≤1600px wide, jpeg q80.
- Stage to `assets/impetus/ai-photoshoot/snap/` locally.
- Upload to `gs://impetus-socialpilot/rrl-portfolio/images/impetus/ai-photoshoot/snap/`.
- Wire onclick lightbox via the existing `openImpetusLightbox()` snippet already on the page.

---

## §9 · Decisions

- **D1 · Lens.** Product overview (deck-first) with Reliance framing as credibility anchor. Decided 2026-05-02.
- **D2 · Brand name.** "AI Photoshoot" as the canonical name throughout (per the rename round done earlier 2026-05-02). Codename "Fynd Snap" mentioned once in the hero subhead. Decided 2026-05-02.
- **D3 · Example count.** 10 curated examples covering each capability category. Other ~75 raw images stay in `docs/snap-compilation/raw-extract/` for reference. Decided 2026-05-02.
- **D4 · Section ordering override.** Page does NOT use the canonical §03 Architecture section — there is no architecture diagram in the source deck and the "how it's built" beat doesn't earn its weight on a creative-platform page. Replaced with §03 Examples per the deck's emphasis. Recorded per skill §4.

---

## §10 · Out of scope (v1)

- Per-brand case studies (Reliance Trends specific outputs vs AJIO specific) — keep flat for v1.
- Pricing tiers / SLA tables — not in source deck.
- Detailed face-swap consent / governance copy — collateral hints at it ("Refresh Your Old Catalogue") but no governance language to source from. Defer.
