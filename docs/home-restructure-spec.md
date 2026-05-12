---
name: home-restructure-spec
description: Restructure /index.html from audit-register matrix to "frontier AI-enabled retailer" narrative, anchored on Unlocking Growth deck slides 5/6/8/9.
type: spec
status: spec sign-off pending · §9 decisions locked 2026-05-02
mode: update / restructure
route: /
---

# Home page · v0.10 restructure spec

This is an **update / restructure** spec (per `website-section-authoring` §1, mode B). The home page already exists at `/index.html` (~813 lines, 11 sections). The route, audience, and overall asset budget are unchanged. What changes is the **narrative anchor** and the **section ordering**.

---

## §0 · Why this change · what's shipping

**Anchor shift.** Today the home page is structured as an **audit register** — a dense matrix (IP × Plan-Buy/Make-Move-Sell × Fashion/Grocery/Electronics/Beauty) followed by a 12-track grid, two product spotlights, and capability frontiers. That structure earns its rent for an MM-Sir-grade reader who arrives knowing what they want to verify, but it does not lead a fresh reader to a thesis.

The new anchor is the line Farooq has been using publicly: **Fynd is making Reliance Retail the world's frontier AI-enabled retailer.** The page should land that thesis in the hero, prove it in three lenses (AI-Powered Jio Commerce / AI for Supply Chain / Unified Customer Platform), show the unified AI-native commerce stack in a single layered diagram, then let the reader interactively explore the ~25 platform pages by layer.

**Source.** Slides 5, 6, 8, 9 of `docs/org-notes-compilation/Fynd - Unlocking Growth.pdf` are the inspiration:
- Slide 5 · Fynd's Impact (Reliance numbers + brand logos)
- Slide 6 · How Fynd Transformed Reliance Retail (3-column lenses)
- Slide 8 · Unified AI Native Commerce Platform (layered architecture diagram)
- Slide 9 · Fynd Capabilities (the same layers expanded with named products)

Slide 7 (From SaaS to Outcomes) is **deliberately skipped** — that's a Fynd-internal story (AI Survey, Create/Forge), not a Reliance-impact story.

**Implementation status.** Spec is draft. No HTML changes until the user signs off on §3 page-structure and §9 decisions.

---

## §3 · Page structure · diff against current

Notation: **ADD** = new section, **KEEP** = stays largely intact, **REWORK** = same intent, restructured copy/layout, **REMOVE** = drops from the page (may move elsewhere), **RENUMBER** = section number shifts.

### Proposed new ordering

| § | Title | Status | Source from current page | Note |
|---|---|---|---|---|
| 0 | Hero | REWORK | current Hero | New H1 lands the "frontier AI-enabled retailer" thesis. Stats strip kept, focus shifted to AI signal. |
| 01 | The transformation · in three lenses | ADD | — | Three-column section mirroring deck slide 6. Each column links to its hub. |
| 02 | The unified AI-native commerce stack | ADD | — | Layered diagram from deck slides 8 & 9. Five horizontal layers + two side guards + a culture base. |
| 03 | Explore every platform | ADD (INTERACTIVE) | absorbs current §04 "12 tracks" | Single grid with filter chips by stack layer. ~25 platform cards. Goal: this is the **navigation hub** the user described. |
| 04 | Scale · today | KEEP | current §03 dark band | Reliance Retail FY26 numbers + Fynd footprint. Light tweaks to lead with AI density numbers. |
| 05 | This month · what Fynd shipped | KEEP | current "Live feed" | 5–6 cards. Currently second section, moves down. |
| 06 | Apex review trail | KEEP | current §08 | 4 timeline events, unchanged. |
| 07 | Sources | ADD | — | Per canonical ordering (`website-section-authoring` §4). Cites the deck + each hub page. |

### What gets cut from the page (per the canonical-ordering "removals" guidance)

| Section in current | Reason to cut | Where it goes |
|---|---|---|
| 60-second exec summary (5 numbers · 3 commitments · 3 asks) | The **new hero + §01 + §02 IS the summary**. Three blocks of dense bullets duplicate what hero stats + transformation columns will carry. | Move the **3 commitments + 3 asks** to `/numbers` (where they're already implied) — that's the right home for time-bound commitments. |
| The matrix · IP × Plan-Buy/Make-Move-Sell × Fashion/Grocery/Electronics/Beauty/Others | This is the **audit-register lens**, not the **frontier-AI-retailer lens**. It's a brilliant artifact but it asks the reader to read horizontally and vertically simultaneously, which is the opposite of an exploratory home page. | Move to `/catalog` (the IP catalog page is the right home for an IP × outcome matrix). Add a hero CTA on the new home that says "Auditing the IP map? See /catalog." |
| Companion App spotlight | Already exists in detail on `/jcp` and `/jcp/channels`. Spotlight on home duplicates and dilutes "explore platforms" goal. | Keep verbatim section on `/jcp`. Reference once on home from §02 stack diagram (it sits in the Sell layer). |
| Fynd Studio spotlight | Same logic — exists on `/impetus` and is part of Gen Media frontier. | Reference once from §02 stack diagram (Buy/Make layer). |
| Five capability frontiers | Subsumed by the §02 stack diagram. The "frontiers" framing was a 2-axis reframe; the layered stack from the deck is the canonical 1-axis frame Fynd has converged on. | Drop from page. The Frontier Pool ask remains on `/numbers`. |

**Net effect:** ~813 lines → expected ~550–650 lines. Page becomes a navigation hub, not an audit document.

---

## §3.1 · Section detail · what each new/reworked section contains

### §0 · Hero · REWORK

```
[Confidential · For Apex leadership]
[Last reconciled · 30 - Apr - 2026 · /numbers]

Making Reliance Retail the world's
frontier AI-enabled retailer.

One AI-native commerce stack. Five layers, live across 79 channels and 3.8M+ retailers.
Built by Fynd · owned and run by Reliance.

[Read the thesis →]   [25 platforms]   [The team]

[6-tile stats strip — refreshed]
  Channels Live · 68
  JioMart daily orders · 1.6M
  UCP identities · 380M+
  RPOS daily transactions · 1.5M
  Fynd people on Reliance · ~430
  Peak orders / hour · 350K
```

The H1 is the only thing that meaningfully changes. Subhead carries the "one stack, five layers" claim that §02 will visualise.

### §01 · The transformation · in three lenses · ADD

Mirrors deck slide 6 directly. Three columns, each a card-with-bullets format. Each column links to its hub page.

```
01 · The transformation
How Fynd transformed Reliance Retail.
One stack. Every retail moment. Live across 3.8M+ retailers.

┌──────────────────────────┬──────────────────────────┬──────────────────────────┐
│ AI-Powered Jio Commerce  │ AI for Supply Chain      │ Unified Customer         │
│ Platform across verticals│ Design to Shelf in 21d   │ Platform                 │
│                          │                          │                          │
│ • End-to-End Commerce    │ • Project Impetus (F&L)  │ • Unifying Profiles &    │
│   at Scale               │   460k+ POs auto         │   Identities · 380M+     │
│   100+ brands across     │   720k articles/day      │   identities unified     │
│   Fashion, Electronics,  │   43 brands live         │   across Reliance Retail │
│   FMCG, replatformed to  │                          │                          │
│   Jio Commerce           │ • Project Granary        │ • Lower acquisition cost │
│                          │   (Grocery)              │   & higher customer      │
│ • Faster GTM with        │   12K+ stores · accurate │   spend                  │
│   modular API-first      │   forecasting · reduced  │   Real-time profile      │
│   architecture           │   spoilage · lean        │   enrichment, one-click  │
│                          │   delivery               │   login, personalised    │
│ → /jcp                   │ → /impetus + /granary    │   engagement (SMS/Email/ │
│                          │                          │   WhatsApp via JioCX)    │
│                          │                          │ → /ucp                   │
└──────────────────────────┴──────────────────────────┴──────────────────────────┘
```

Copy is verbatim from the deck slide 6 (per `website-tone-of-voice` — quote, don't rewrite). Linkouts at the bottom.

### §02 · The unified AI-native commerce stack · ADD

This is the **load-bearing visual** of the new page. Mirrors deck slide 8/9 with the 5-layer architecture.

**Layout** (text-first wireframe — final visual TBD per §9 D2):

```
02 · The stack
One AI-native commerce stack. Five layers, two side guards, one culture base.

                        ┌───────────────────────────────────────┐
                        │ SELL                                  │
                        │ Storefront · POS · Companion App ·    │
                        │ Kiosk (Kio) · Endless Aisle · Konnect │
                        │ · Client Telling · Virtual Try-On     │
                        │ · Loyalty (R-One) · Agentic (Kaily)   │
                        ├───────────────────────────────────────┤
   Store Health         │ MOVE                                  │   New Store
   ┌────────────┐       │ WMS · Logistics · OMS · TMS ·         │   ┌────────────┐
   │ Retail     │       │ Onshelf (AutRi) · Vista (delivery)    │   │ ALP        │
   │ Jarvis     │       ├───────────────────────────────────────┤   │ Retail     │
   └────────────┘       │ BUY / MAKE                            │   │ Vista      │
                        │ Auto Tech-Pack · Photoshoot ·         │   └────────────┘
                        │ Auto Purchase Request · Cataloging ·  │
                        │ Forge MES · Dark Factory              │
                        ├───────────────────────────────────────┤
                        │ PLAN / DESIGN                         │
                        │ Fashion Design · Cortex · Assortment  │
                        │ Planning · Sales Calendar · Pricing   │
                        ├───────────────────────────────────────┤
                        │ DATA & FEEDBACK                       │
                        │ UCP (Customer Profile) · Ask Impetus  │
                        │ · Boltic · Ratl · Fynd Intelligence · │
                        │ PulsePoint NPS                        │
                        └───────────────────────────────────────┘

                        ┌───────────────────────────────────────┐
                        │ CULTURE                               │
                        │ Fynd Academy · Community · Storytelling│
                        └───────────────────────────────────────┘
```

**Behaviour**: layers are clickable. Clicking a layer scrolls down to §03 with that layer's filter pre-applied. Side guards (Retail Jarvis, ALP, Retail Vista) and base (Culture) link directly to their pages.

**Footer line under diagram:**
> Each layer links to the platforms inside it. Side guards (Retail Jarvis · ALP · Retail Vista) cover store health and new-store opening. Culture (Fynd Academy) is the base.

### §03 · Explore every platform · ADD (interactive nav hub)

The exploration surface the user asked for. **Single filterable grid**.

```
03 · Explore
Twenty-five platforms. Pick a layer to explore.

[ All ] [ Sell ] [ Move ] [ Buy / Make ] [ Plan / Design ] [ Data & Feedback ]
[ Store Health ] [ New Store ] [ Culture ]

[Grid of ~25 platform cards. Each card has:]
  - Platform name (links to its detail page)
  - Layer tag(s) — drives the filter
  - 1-line description
  - Status pill (Live · Pilot · Build)
  - Anchor metric (most-quotable single number)

[Cards filter client-side via JS — no page reload.]
```

**Card-to-layer mapping** (drives the filter; locked in this spec, pending §9 D3):

| Platform | Layer(s) | Status |
|---|---|---|
| /jcp | Sell · Move | Live |
| /impetus | Plan/Design · Buy/Make · Sell | Live |
| /granary | Plan/Design · Buy/Make · Move · Sell | Live (Phase 1) |
| /ucp | Data & Feedback | Live |
| /alp | New Store | Live (MVP) |
| /retail-vista | New Store · Plan/Design | Live |
| /retail-jarvis | Store Health | Building |
| /samarth | Culture | Live |
| /forge | Buy/Make | Pilot |
| /hirefirst | Culture | Live |
| /swapeasy | Sell | Live |
| /tms | Move | Live |
| /fynd-konnect | Sell · Move | Live |
| /boltic | Data & Feedback | Live |
| /pixelbin | Buy/Make · Sell | Live |
| /ratl | Data & Feedback | Live |
| /kaily | Sell | Live |
| /kio | Sell | Pilot |
| /autri | Move | Pilot |
| /dark-factory | Buy/Make | Build |
| /fynd-horizon | Sell | Live |
| /fynd-academy | Culture | Live |
| /culture | Culture | Live |
| /organisation | Culture | Live |
| /autonomous | (cross-cuts) | Live |

24 entries above + `/numbers` and `/catalog` if we want them. Card layout matches the existing 12-tracks grid for visual continuity.

### §04 · Scale · today · KEEP (light rework)

Current dark band stays. Two minor edits:
- Lead the Fynd-footprint subgroup with **AI-density** stats (e.g., "AI decisions/day", "Agentic interactions/day") if we have credible numbers. Current "78 channels · 300M+ customers · 350K peak/hr · ~430 people" is fine if we don't.
- Drop the "RIL Group · FY26 ₹10.7L Cr · JPL ₹30K Cr · JioMart +300% · RCPL ₹20K Cr" middle band — that's audit-register-grade, not home-grade. Move to `/numbers`.

### §05 · This month · KEEP

Current 5-card live feed. Compress to 4–6 cards if we re-order it later in the page. No copy changes.

### §06 · Apex review trail · KEEP

Current 4-event timeline. No copy changes.

### §07 · Sources · ADD

Per canonical ordering. Card list:
- `docs/org-notes-compilation/Fynd - Unlocking Growth.pdf` · slides 5, 6, 8, 9 (transformation lenses + stack diagram)
- Per-platform hub pages (linked already in §03 grid)
- `/numbers` (canonical numbers reconciliation)

---

## §4 · Data model

No YAML files. Single hand-authored `/index.html` (per `website-section-authoring` §7 single-page rule). The platform-card grid in §03 is the only "data" — it lives as a JS array at the top of a `<script>` block in the page itself. ~25 entries × 5 fields = trivial.

```js
const platforms = [
  { slug: '/jcp',        name: 'JCP · Jio Commerce Platform', layers: ['sell','move'],          status: 'live',  metric: '79 channels · 68 live' },
  { slug: '/impetus',    name: 'Impetus · F&L AI',           layers: ['plan','make','sell'],   status: 'live',  metric: '15 sub-platforms' },
  // ...
];
```

Filter chip click → re-render grid with platforms whose `layers` include the chosen layer.

---

## §5 · Asset pipeline

**Two image extractions** from the deck (Stage 3 of authoring skill):

1. **Slide 5 · Reliance brand-logo strip** — optional. If we use it, extract via `pdfimages -j` (text-heavy slide; per `website-section-authoring` §6). Target: `assets/home/reliance-brands.jpg` (or use as inline logos).
2. **Slide 8 · Layered architecture diagram** — extract as `pdftoppm` page (diagram-only, full-bleed, no surrounding text), then crop title bar in PIL. Target: `assets/home/stack-diagram.jpg`.
   - Decision pending §9 D2 — may also be hand-built in HTML/SVG instead of bitmap-extracted.

Both assets stay local (small file count, single page → no GCS mirror needed).

---

## §6 · Navigation wiring

Home is itself the top of every nav. Two consequences:
- **Nothing to add** to mega-menus, /catalog, or sibling-section indexes.
- **Cards in §03 must link to existing routes** that already work. Verify each link 200s before commit (per `website-section-authoring` §9).

---

## §7 · Build / verify

Same single-page workflow as Fynd Academy:
```
python3 -m http.server 8000
# open http://localhost:8000/
sessionStorage.setItem('fyndrrl_auth_v1', '1');  // bypass auth
```

Verify checklist (per `website-section-authoring` §9):
- [ ] All 25 §03 cards link to a 200-returning page
- [ ] Filter chips toggle the grid correctly (client-side, no reload)
- [ ] §02 layer click scrolls + applies §03 filter
- [ ] Mobile (375px): hero stacks, §01 columns stack, §02 stack still legible, §03 filter chips wrap
- [ ] Auth gate still gates the page in a fresh incognito session
- [ ] Lighthouse pass (no regression vs current home)

---

## §8 · Phased delivery

Single phase (P1, ~3–5 hours). The whole restructure ships in one commit because the new sections replace, not augment, the old.

---

## §9 · Decisions · LOCKED 2026-05-02

- **D1 · Matrix table** — **REMOVE entirely** (not moved to /catalog). The IP×Value Chain × Retail Type lens is dropped from the register on this restructure. /catalog stays as-is for now; if a future Apex review wants the audit grid back it can re-emerge there as a separate scope.
  - **How to apply:** delete the entire `<section id="thesis">` (matrix) block. No replacement copy on home. No CTA to /catalog from hero.
- **D2 · §02 stack diagram** — **Hand-built HTML/SVG**, not bitmap. Layers are clickable. Clicking a layer scrolls to §03 with the layer's filter pre-applied.
  - **How to apply:** SVG group per layer with `data-layer="sell"` etc; click handler scrolls to `#explore` and dispatches the matching chip. Side guards (Retail Jarvis · ALP · Retail Vista) and Culture base are HTML cards flanking/under the SVG, each linking direct to its hub.
- **D3 · Platform-to-layer mapping** — **lock as drafted in §3.1** above. Open to fix on review.
- **D4 · 60-second exec summary** — **DROP entirely**. New hero + §01 carry the load. The 3 commitments + 3 asks do **not** auto-migrate to /numbers in this scope; if /numbers wants them, that's a separate edit.
- **D5 · Companion App + Fynd Studio spotlights** — **DROP both from home**. Both already live in detail on `/jcp` and `/impetus`. They appear as platform cards in the new §03 grid — that's the only home reference.

**One open question deferred to build time** (cheap to fix later, doesn't change the spec): whether the §03 filter is single-select (one layer at a time) or multi-select (toggle several). Defaulting to **single-select** for clarity. Easy to flip if the user wants multi.

---

## §10 · Out of scope for this restructure

- Editing the existing 24 platform detail pages. They're untouched.
- Adding/renaming any platform. The §03 grid uses today's 25 routes verbatim.
- Mobile drawer redesign for the topnav (still in `docs/site-nav-spec.md` §8).
- Any change to `/numbers`, `/catalog`, `/organisation`, `/culture`. (D1 + the 60-sec-summary move *will* require small additions to `/numbers` and `/catalog` — those are tracked separately.)
- New auth-gate behaviour or new-tab lightbox patterns (no new screenshots on this page).
