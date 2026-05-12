# /ratl/ · section spec

| Field | Value |
|---|---|
| Status | drafting v0.1 |
| Owner | Salman Saudagar (COO, Fynd) |
| Route | `/ratl/` |
| Mode | Update (existing stub at `ratl/index.html`) |
| Source content | `docs/ratl-notes-compilation/` (showcase doc + 4 screenshots + Master Deck PDF), `docs/accenture-2026-04-16-compilation/` slides 47-48, `docs/2026-04-30-farooq-mda-update-letter.md` |
| Narrative anchor | Farooq's 30-Apr letter to MM Sir names Ratl alongside Boltic and PixelBin in the Agentic Automation list. The current `/ratl/` is a 1-card placeholder; this spec brings it to the same line as `/boltic/` and `/granary/`. |

---

## §0 · What's changing and why

The route already exists but ships a "Page in progress" card. With the showcase doc (`docs/ratl-notes-compilation/ratl_jio_showcase.md`) and four production screenshots in hand, plus the 2-line Accenture confirmation (slides 47-48), there is enough on-source material to ship a v0.1 page on the same template as `/boltic/`.

Scope of this rev: full page replacement. No backwards compatibility — the placeholder is dropped.

## §1 · Audience

RIL Apex leadership (MM Sir level). Reading top-to-bottom to verify (a) what Ratl ships today across Jio + RBL + Retail, (b) the engineering it replaces, (c) the per-storefront impact numbers. Same register as `/boltic/`, `/granary/`, `/hirefirst/`.

## §2 · Source inventory

| File | Used for |
|---|---|
| `docs/ratl-notes-compilation/ratl_jio_showcase.md` | Canonical pitch doc · §01-§06 substance, every stat traceable here |
| `docs/ratl-notes-compilation/Ratl Master Deck_Nov_25.pdf` | Reference (not embedded; cite as source) |
| `docs/ratl-notes-compilation/release-intelligence.png` | §04 deep-dive screenshot |
| `docs/ratl-notes-compilation/synthetic-monitoring.png` | §04 deep-dive screenshot |
| `docs/ratl-notes-compilation/compliance-monitoring.png` | §04 deep-dive screenshot |
| `docs/ratl-notes-compilation/catalog-siteops.png` | §05 Catalog Intelligence screenshot |
| `docs/accenture-2026-04-16-compilation/all-slides-text.md` slides 47-48 | One-line verbatim platform definition |
| `docs/2026-04-30-farooq-mda-update-letter.md` | Confirms Ratl's place in the AI-Native register |

## §3 · Page structure

Mirrors `/boltic/` template — Apex reviewers should not have to re-learn the page on each track.

| § | Section | Substance |
|---|---|---|
| 0 | Hero | Eyebrow + H1 ("Ratl. The agentic quality OS for Reliance Retail.") + 2-line subhead + status pill (`Live · Jio + RBL + Retail`) + 3 stat tiles (productivity, release-cycle, automation-coverage) |
| 01 | What Ratl is for Reliance | Problem / Solution / Impact triptych |
| 02 | What's live · seven engines | Card grid: Release Intelligence · Autonomous Testing · Synthetic Monitoring · Mobile AI Automation · Compliance & Security · Automation Utilities · Catalog Intelligence — every card pilled `Live · Platform` |
| 03 | Architecture · the agentic SDLC layer | 4-layer diagram: Signals (API/Web/Mobile/Load/Security/Catalog) → Agentic engines (test gen, exec, failure clustering, RCA) → Release Intelligence (confidence score, risk class, go/no-go) → SDLC surfaces (developer, release, oncall) |
| 04 | Deep dive · the live console | 3 screenshot cards: Release Intelligence · Synthetic Monitoring · Compliance Monitoring |
| 05 | Catalog Intelligence · the Jiomart OS foundation | Standalone block — what it watches, business impact, 1 screenshot, Jiomart OS evolution beat |
| 06 | Outcomes · the running scorecard | Numbered scorecard table, one row per impact area with evidence |
| 07 | Sources | Card list of source files |

Override note (§9 Decision D1): no separate §06 Vision/Roadmap — the page is small enough that the honesty contract sits in the §02 module table itself. Catalog Intelligence's "evolving into Jiomart OS foundation" claim is the only forward-looking line and gets a `Building` pill on its sub-card.

## §4 · Data model

Single hand-authored `ratl/index.html`. No `data/ratl/` YAML, no renderer — the page is one entity, not an inventory of N sub-pages.

## §5 · Asset pipeline

4 PNG screenshots from `docs/ratl-notes-compilation/` resized to max 1600px wide JPEG q80 → `assets/ratl/<name>.jpg`. Master Deck PDF stays in source folder; not hosted (it's the reference, not the artifact).

```bash
sips -Z 1600 -s format jpeg -s formatOptions 80 \
  "docs/ratl-notes-compilation/release-intelligence.png" \
  --out "assets/ratl/release-intelligence.jpg"
# ...repeat for the other 3
```

No GCS mirror needed — 4 files, well under the 20-file / 100MB threshold.

## §6 · Navigation wiring

Already wired. `/ratl` exists in the AI-Native column of every page's mega-menu. No nav edit needed. Optional: the home-page card (if Ratl has its own card) — verify and update mono-suffix from "agentic auto" if a more precise label fits.

## §7 · Build / verify

```bash
python3 -m http.server 8000
# DevTools: sessionStorage.setItem('fyndrrl_auth_v1', '1'); location.reload()
# open http://localhost:8000/ratl
```

## §8 · Phased delivery

P1 (this rev, ~1 hr): full page replacement, screenshots in place, sources block populated.

## §9 · Decisions

- **D1 · Section ordering override** — drop §06 Vision/Roadmap. *Why*: page is single-product, narrative reads cleanly without it; forward-looking claims sit on individual cards. *How to apply*: §05 Catalog Intelligence carries the only `Building` pill (Jiomart OS foundation evolution).
- **D2 · Honesty pills** — single `Live · Jio + RBL + Retail` in hero; per-card `Live · Platform` on §02; no Building/Roadmap unless explicitly forward-looking. *Why*: user confirmed all showcase stats represent Live deployments.
- **D3 · No renderer** — single hand-authored `index.html`. *Why*: one entity, no sub-pages, edits will be infrequent.

## §10 · Out of scope

- Per-storefront breakdown (e.g., AJIO vs Tira vs JioMart deep-dive cases) — would need a sibling source doc per brand.
- Embedded video / QR demo (Accenture slide 48 references a video) — not provided in source folder.
- Master Deck PDF embed — not requested; the showcase doc is the canonical pitch surface.
