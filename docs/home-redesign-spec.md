---
spec: home-redesign
purpose: Re-architect `/index.html` for an Apex-leadership read. Replace the current hero → 27-platform-grid flow with a hero → impact-at-a-glance → 7 storyline sections → grid → confidentiality flow, organised in the order of the 30-Apr-2026 letter to MM Sir.
status: signed-off · ready to implement
as-of: 03-May-2026
audience: RIL Apex leadership (MM Sir level)
owner: <fill>
---

# Home redesign · spec

## 0 · Why

The current `/index.html` is a **hero + filterable 27-platform grid + dark footer**. Two problems for an Apex read:

1. **No "what has Fynd delivered" answer.** A leader scrolling past the hero immediately hits 27 sibling cards. There is no aggregate scale moment, no answer to *"what should I take away in the first 30 seconds"*. The 25-platform claim is in the hero copy but the proof points are scattered across 25 sub-pages.
2. **No structural correspondence to how the work is described upward.** The 30-Apr-2026 letter to MM Sir (`docs/2026-04-30-farooq-mda-update-letter.md`) names a specific 7-bucket structure: Impetus → JCP → UCP/Marketing OS → Granary → Special Projects → AI-Native (Agentic Automation + Agentic Commerce) → Recent Innovations. The home page should mirror that order so the read starts where the letter starts.

The redesign keeps the existing platform grid (it's still the best random-access surface) but stops leading with it. Lead with the aggregate impact and the 7 storyline buckets; let the grid sit beneath as a directory.

---

## 1 · Goals · non-goals

**Goals**
- A first-fold *"what has Fynd delivered for Reliance"* moment with 5-7 platform-scale numbers — sourced, datable, traceable.
- 7 in-page storyline sections in MDA-letter order, each a one-screen-fold: scale + 2-4 platform tiles + a CTA per tile to go deeper.
- Preserve the existing 27-tile filterable directory below the storylines for random-access.
- Preserve the Project Glass auth gate, the canonical chrome (nav + dark footer), and the existing platform-card design tokens.

**Non-goals**
- Authoring new platform pages. Every linked target already exists.
- Changing the auth flow.
- Re-pricing tone-of-voice. Same register: no `we/our`, no marketing vocab, dates `DD-MMM-YYYY`, Indian numbers `L Cr`, hero subheads ≤ 30 words.
- Adding any platform NOT named in the letter (NAM, CPP, UBOC from the Accenture deck are future-state — out of scope for this home).

---

## 2 · Page architecture · before vs after

### Before (today)

```
01 NAV (canonical)
02 HERO · "Making Reliance Retail the world's frontier AI-enabled retailer"
03 §01 EXPLORE · 27 filterable platform cards
04 FOOTER (canonical · dark)
```

### After (proposed)

```
01 NAV (canonical · unchanged)
02 HERO · unchanged headline + new mono cap subhead (Move E) + single CTA only ("Explore 22 platforms"; The Team CTA dropped Round 5)
03 §01 IMPACT · 6 big-number tiles · "What Fynd has delivered for Reliance"
04 §02 IMPETUS · F&L AI platform
05 §03 JCP · Jio Commerce Platform
06 §04 UCP & MARKETING OS
07 §05 GRANARY · Grocery AI
08 §06 SPECIAL PROJECTS · ALP, RetailVista, Retail Jarvis, Samarth, HireFirst, SwapEasy (Forge dropped per MDA letter; RCPL deferred Round 4)
09 §07 AI-NATIVE PLATFORMS · Agentic Automation (Boltic · PixelBin · Ratl) + Agentic Commerce (Kaily)
10 §08 RECENT INNOVATIONS · Fynd Horizon · AutRi · Dark Factory
11 §09 ORGANISATION · highlights · drill-down to /organisation, /culture, /ai-native, /fynd-academy (added Round 5)
12 §10 EVERY PLATFORM · existing 27-card filterable directory (former §01)
13 FOOTER (canonical · dark · unchanged)
```

Net: nav + hero + footer untouched. One existing section (§01 Explore) becomes §09. Seven new storyline sections + one impact section inserted between hero and grid.

---

## 3 · §01 IMPACT · "what Fynd has delivered for Reliance"

**Intent.** The first 30 seconds of an Apex scroll. A one-line preface that grounds the read in Reliance Retail's own scale, then nine big-number tiles that show what Fynd has delivered into that scale — two rows of platform/customer scale, one row of ecosystem & people reach.

**Visual.** Preface line full-width centred — `.cap-num` class · 12 px JetBrains Mono · color `#4B5563` (the design.md Tier 1 caption-color target) · letter-spacing 0.04em · uppercase. Below: 3×3 grid (desktop) → 2×5 (tablet) → 1×9 (mobile). Each tile uses the existing `.card` (12 px radius, 1 px `var(--border)`, `p-6` padding — `p-6` is the spacing-token choice for this card type, see design.md §1.3 + §2.1). Inside each tile: `.num-display` (Inter 800 · -0.04em letter-spacing · 0.9 line-height · sized inline 64-96 px) + `font-variant-numeric: tabular-nums` for stable digit columns; below it a 2-line caption in body Inter at 14 px. No icons.

**Section header.**
- Preface (mono cap, centred): `Reliance Retail · $39 B FY 25 · 19,979 stores · 378 M+ customers · #1 in Grocery, Electronics, Fashion (India)`
- Below preface (display-2): `Fynd is the AI-native operating layer underneath. Six numbers · what's been delivered.`
- Source for the preface: `docs/accenture-2026-04-16-compilation/INDEX.md` §1 (Accenture deck slide 3).

**Tiles** — sourced from `docs/homepage-notes-compilation/Fynd - Unlocking Growth.pptx` (slide 6, 25, 29) and `docs/accenture-2026-04-16-compilation/INDEX.md`. Listed in scan-order:

| # | Big number | Caption | Source |
|---|---|---|---|
| 1 | `380 M+` | Customer identities unified across Reliance Retail · UCP foundation across 100 % of formats (RR registered customers · 387 M) | Unlocking Growth · slide 6 (deck says 400 M+; audit corrected to 380 M+ to stay defensibly under the 387 M RR registered count); matches `/ucp/` |
| 2 | `100+` | Brands replatformed to Jio Commerce Platform · 79 channels · 68 live · 700 K+ orders / day | Unlocking Growth · slide 6; matches `/jcp/` |
| 3 | `15.08 Cr` | Pieces delivered FY 26 via Impetus F&L · 11.06 L POs FY 26 · 43 brands live | Unlocking Growth · slide 6; matches `/impetus/` |
| 4 | `88 %+` | Positive customer engagement · AJIO ZIP agentic shopping · 86 % chat-driven discovery on 2 M+ products | Accenture INDEX §14 (slide 37); matches `/kaily/` |
| 5 | `20 K+` | Stores connected on JCP across the Reliance Retail estate | Unlocking Growth · slide 29 (Platform Health Metrics); matches `/jcp/` |
| 6 | `25` | Platforms running today · across Plan · Buy · Make · Move · Sell · Data · Store Health · HR Tech | the inventory itself; matches `/index.html` PLATFORMS array |
| 7 | `1 K+` | Vendors transacting on Impetus across the Reliance F&L supply base | Annual Board Update 2025-2 · slide 7 (Reliance column) |
| 8 | `2.3 K+` | Reliance employees trained across platforms | Annual Board Update 2025-2 · slide 7 (Reliance column) |
| 9 | `1.2 K+` | Developer contributors across Jio Commerce Platform + Impetus | Annual Board Update 2025-2 · slide 7 (Reliance column) |

**Resolved · 03-May-2026.** Granary 12 K dropped from §01 (per Round 2 feedback). Tile #4 now `88 %+ positive engagement · AJIO ZIP` — surfaces the agentic-commerce outcome, complements the platform-scale tiles with a UX-impact dimension. Granary still gets its full storyline at §05.

**Resolved · 03-May-2026.** §01 expanded from 6 → 9 tiles. Row 3 (`1 K+ vendors · 2.3 K+ trained · 1.2 K+ developers`) opens a new dimension the page lacked: ecosystem & people reach. All three are Reliance-tagged on slide 7 of the Annual Board Update 2025-2, so they belong here, not in §02. Grid is now a clean 3×3.

**Resolved · 03-May-2026.** JCP framing in tile #2 uses the steady-state daily number (`700 K+ orders / day`), not the peak-hourly capacity.

**Resolved · 03-May-2026.** No `Sources · …` line under §01 IMPACT. Numbers stand on their own per CLAUDE.md "no §Sources block" rule. Provenance lives only in this spec.

**Alternatives considered for tile #4** (rejected, kept here for sign-off audit):
- `90 %+ time reduction · Catalog creation · 15 days → 5 hours` (Accenture INDEX §7) — strong speed proof but reads as a single-capability story
- `460 K+ POs automated · Impetus operations` — duplicates the Impetus story already in tile #3
- `7,989 hrs / wk saved on Claude · Fynd engineering` — internal Fynd productivity, not RR-delivered impact

---

## 4 · §02 – §08 · the seven storyline sections

Same template per section. Each is **one viewport tall** (so a leader can read by tapping `Page Down` once per section).

```
[section-label]   §0X · BUCKET NAME (mono caps)
[display-2]       One-line headline · what this bucket is for Reliance
[lead]            2-3 sentence framing · scale + intent · no marketing voice
[card grid]       2-4 platform tiles · same .platform-card design as §09
[CTA strip]       "Open the <bucket>" → links to bucket landing OR every tile is its own CTA
```

Per-section content:

### §02 · IMPETUS · F&L AI Platform

- **Hero number (Move B):** `15.08 Cr` · *Pieces shipped FY 26.*
- **Headline:** *F&L from design to shelf in 21 days · one AI-native platform.*
- **Lead:** *Plan · Buy · Make · Sell on a single fabric for Fashion & Lifestyle. 11.06 L POs FY 26 · 460 K+ POs automated · 720 K articles packed / day · 43 brands live across the AJIO + Trends + Reliance Retail F&L estate. 6 named AI Agents — Trend-to-Design · Cortex Planning · Agentic Marketing · Retail Vista · Retail Jarvis · Ask Impetus.*
- **Tiles** (4) — **resolved · 03-May-2026 · IntelliLoom out → Photoshoots in**: Photoshoots · Cortex Planning · Master Hub · Companion App. Status pill on each. Open-deeper CTA per tile pointing into `/impetus/<sub>/`.
  - **Why Photoshoots replaces IntelliLoom.** AI Cataloging / Photoshoots ships the strongest single-line proof in the F&L line — *15 days → 5 hours* (Accenture INDEX §7, slide 19). IntelliLoom (the AI-native design IP) is real but its proof point — Superdry SDX *120 designs in 5 days* — is one brand. Photoshoots is platform-wide.
  - **Alternatives considered:** Trend-to-Design (named in the 6-agent canonical list, but lives at `/agents/trend-to-design/`, not under `/impetus/`); NextWave (trend research, less Apex-relevant); Category Intelligence (own page, but narrower story).
- **Section CTA:** `Open Impetus →` → `/impetus/`
- **Source backing:** Unlocking Growth slide 6 + Accenture INDEX §3-§7 (slides 10-19). Numbers cross-checked.

### §03 · JIO COMMERCE PLATFORM (JCP)

- **Hero number (Move B):** `100+` · *Brands on one commerce stack.*
- **Headline (resolved · 03-May-2026):** *Enterprise commerce platform · powering Reliance Retail.* Direct framing from Accenture deck slide 32 ("Jio Commerce Platform: Enterprise Commerce") and slide 35 ("Scale of Retail Transformation FY 2025-26"). Replaces the previous "commerce spine" framing.
- **Lead:** *Enterprise-grade commerce platform supporting large-scale operations for Reliance Retail. 79 channels · 68 live · 30 K+ stores served · 700 K+ orders / day · 50 K+ orders / minute peak · 200 M+ customers. Hosts AJIO, JioMart, Reliance Digital, Tira, Trends and 100+ other brands across 10 clusters — website, in-store, marketplace, OMS. AJIO ZIP — agentic shopping inside JCP — at 88 % positive engagement.*
- **Tiles (resolved · 03-May-2026 · RCPL out → 3 tiles):** Channels Overview · AI Cataloging · Release Notes. RCPL deferred — placement to be decided by the page owner separately.
- **Section CTA:** `Open JCP →` → `/jcp/`
- **Source backing:** Accenture INDEX §13 + §14 (slides 31-35, 37); existing `/jcp/` content; `docs/jcp-update-spec.md`.

### §04 · UCP & MARKETING OS

- **Hero number (Move B):** `380 M+` · *Customers · one profile.*
- **Headline:** *Every Reliance Retail customer · one profile · ready to act on.*
- **Lead (resolved · 03-May-2026 · jargon stripped):** *380 M+ customers — across AJIO, JioMart, Reliance Digital, Trends, Tira, Smart Bazaar and 75+ other formats — unified into a single profile. The marketing layer above decides what to send to whom and when, in real time. Campaign cycles that took weeks now run in minutes, with offers personalised per customer per moment. Lower acquisition cost, higher repeat spend, fewer wasted touches.*
- **Tiles** (3) — labels stay simple, no L0–L5 jargon on the home (Apex won't decode the autonomy framework):
  - `UCP Foundation` · status `Live` · *Identity, profile, real-time activation across every format.*
  - `Marketing Cockpits` · status `Building` · *Marketing Intelligence · Brand Health · JCP Coupons · Self-serve scale-up.*
  - `AI-Native UCP` · status `Roadmap` · *Speak-to-data → cohort → campaign → creative → execution → retro · all conversational.*
- **What was stripped from the prior draft:** "200+ profile attributes" · "1.5 M RPOS orders/day from 75+ formats / 15 K+ stores" · "~19 ms p50 API latency" · "L3 → L4 agentic" · "DPDP-compliant" · "Built on Jio Cloud". All true, all engineering jargon. The page that owners will follow into (`/ucp/`) carries the technical depth — the home only needs the impact.
- **Section CTA:** `Open UCP & Marketing OS →` → `/ucp/`
- **Source backing:** existing `/ucp/` page; Unlocking Growth slide 6.

### §05 · GRANARY · Grocery AI

- **Hero number (Move B):** `Phase 1` · *Live · 11 Mumbai stores.*
- **Headline:** *Agentic planning + assortment for Grocery.*
- **Lead:** *48 M-row daily forecast across 12 K SKUs × 4 K stores. Phase 1 live across an 11-store Mumbai pilot — Smart Bazaar + Smart Point — at MAPE 41%. Cortex Planning (Assortment Intelligence + MBQ Automation + Range Review) live; STP, CDT, Consensus Forecasting on the roadmap. 12,000+ stores served via the wider Granary stack.*
- **Tiles** (2): Granary Overview · Granary Research.
- **Section CTA:** `Open Granary →` → `/granary/`
- **Source backing:** Unlocking Growth slide 6; existing `/granary/` page.

### §06 · SPECIAL PROJECTS

- **Hero number (Move B):** `6` · *Builds for Reliance.* (caption corrected post-audit · was "Builds · live for Reliance" · 5 of 6 are LIVE, 1 (Retail Jarvis) is BUILD, so the original wording overclaimed by 1)
- **Headline:** *Six projects beyond the platforms · taken on by Fynd, shipped for Reliance.*
- **Lead:** *Net-new builds where Fynd took on a problem Reliance hadn't yet solved · ALP for new-store opening · RetailVista for site intelligence · Retail Jarvis for non-intrusive CX sensing · Samarth Plus for the frontline career platform · HireFirst for AI-native hiring · SwapEasy for in-store re-commerce.*
- **Tiles (resolved · Round 4 · 03-May-2026 · RCPL deferred again):** 6 independent tiles in a 3+3 grid in the order Farooq's letter names:
  - Row 1: ALP · RetailVista · Retail Jarvis
  - Row 2: Samarth Plus · HireFirst · SwapEasy
  - **No connecting glyphs between tiles.** Each is a standalone project — visually independent, separated only by the standard grid gap. No `→`, no `·`, no inferred sequence; especially Samarth Plus and HireFirst, which are entirely separate projects.
  - Status pill on each — uses existing `.pill-live / -pilot / -build / -phase2` only. Cards use the standard `.platform-card` (no new variant per design.md §2.1) — the visual "compactness" comes from the 3-column row width, not a smaller card.
- **Forge** removed from §06 because the MDA letter does not name it. Forge stays on `/forge/` and in the §09 EVERY PLATFORM grid; no storyline tile here.
- **RCPL** also not in §06 (Round 4 reversal of Round 3). Stays on `/jcp/rcpl/` and in the §09 grid; placement on the home is deferred for a separate call.
- **Section CTA:** `Open every special project →` jumps to the §09 grid filtered to the **`Special Projects`** chip.
- **Source backing:** `docs/2026-04-30-farooq-mda-update-letter.md`; existing pages.

### §07 · AI-NATIVE PLATFORMS

- **Hero number (Move B):** `88 %` · *Positive engagement · AJIO ZIP.*
- **Headline:** *Agentic Automation + Agentic Commerce.*
- **Lead, two sub-headers:**
  - **Agentic Automation** — *Boltic, PixelBin, Ratl. The platforms that automate work, not workflows.*
  - **Agentic Commerce** — *Kaily, live in JioMart (JIIA) and AJIO (ZIP). Agents that talk, think, act inside the customer journey.*
- **Tiles** (4) — **resolved · Kaily as one combined tile**: Boltic · PixelBin · Ratl in the Agentic Automation row; Kaily as a single tile in Agentic Commerce with combined metrics caption (`88% AJIO ZIP · 96% Netmeds · live in JioMart`). Match the existing `/kaily/` page framing.
- **Section CTA:** `Open every AI-Native platform →` jumps to the §09 grid filtered to "Data" + "Sell" (or a new filter "AI-Native").
- **Source backing:** Farooq letter; existing pages; AI Agents directory at `/agents/`.

### §08 · RECENT INNOVATIONS

- **Hero number (Move B):** `7 days` · *Order → doorstep · Fynd Horizon MTO.*
- **Headline:** *The next horizon · already shipping.*
- **Lead:** *Fynd Horizon — Ultra Fast Retail · made-to-measure in 24 hours · live at RCP and Mumbai cluster. AutRi — agentic planogram compliance · Phase 1 live at FreshPik Powai with Fynd Nucleus. Dark Factory — lights-out micro-factory + Mobile Tailor app inside AJIO · awaiting capex + alpha sign-off.*
- **Tiles** (3): Fynd Horizon · AutRi · Dark Factory.
- **Section CTA:** `Open every Recent Innovation →` jumps to §10 grid (no filter — they're scattered across status pills).
- **Source backing:** Farooq letter; existing pages.

### §09 · ORGANISATION (added Round 5 · 03-May-2026)

- **Hero number (Move B):** `1,100+` · *People building Fynd · 14 years.*
- **Headline:** *The team behind 22 platforms.*
- **Lead:** *Founder-led. Engineering-heavy. AI-native by design. 1,100+ people · 14 years building · 68 % product builders. The same team that turned 0 to $ 2.5 B platform GMV (~₹ 20,000 Cr) is now turning every workflow autonomous.*
- **Highlight tiles (4)** — use the existing `.card p-5` (default card · 12 px radius · 20 px padding) per design.md §2.1. Inside each: a `.num-display` value (Inter 800 · `tabular-nums` · sized 32-48 px — smaller than §01 IMPACT tiles to set hierarchy) over a `.cap-num` label. **No new card variant** — same default `.card` everyone else uses.
  - `1,100+` · *People · founder-led · ~200 in 2014 → 1,091 in 2025*
  - `68 %` · *Product Builders · engineering-heavy by design*
  - `78 %` · *Use AI daily · 66 % advanced · 7,989 hrs / wk saved on Claude*
  - `10` · *Core Values · disagree but commit · brutal honesty · ethical & accountable*
- **Drill-down tiles (4)** — standard platform-card pattern, link out to deeper pages:
  - `Organisation` → `/organisation/` · *founders · CTPOs · CBOs · the leadership stack + the employee directory*
  - `Culture` → `/culture/` · *the 10 values lived · life at Fynd · awards · Glassdoor reviews*
  - `AI-Native Engineering` → `/ai-native/` · *how Fynd builds now · autocomplete → IDE pair → agent-led SDLC*
  - `Fynd Academy` → `/fynd-academy/` · *talent + training · 600+ trained · 5 Reliance entities served*
- **Section CTA:** None at the section level — the four drill-down tiles each carry their own CTA.
- **Source backing:** Unlocking Growth deck slides 16, 17, 20, 21, 22, 23, 25; existing `/organisation/`, `/culture/`, `/ai-native/`, `/fynd-academy/` pages.
- **Why this section sits at §09 (not §01).** Per Round 5 feedback: org is *the team behind the work*, not the work itself. Putting it after the seven storyline sections + Recent Innovations keeps the read on what Fynd has shipped first; org is the answer to "who built this" once the reader is convinced of the work.

---

## 5 · §10 · Every platform · the existing grid (now repositioned)

The current §01 Explore section moves down whole — same 27 cards, same filter chips, same JS, same data. Two micro-changes:

1. **Section label** changes from `01 · Explore` to `10 · Every platform` (renumbered Round 5 to make room for new §09 ORGANISATION).
2. **Add a `Special Projects` filter chip** (resolved · matches MDA-letter wording + the existing mega-menu column) so the §06 section CTA has a target. The filter chip is computed from a new `track` field on the inventory entries — non-disruptive, additive only. The 7 entries flagged: ALP · RetailVista · Retail Jarvis · Forge · Samarth Plus · HireFirst · SwapEasy.

**No content changes** to platform cards or the inventory.

---

## 6 · Visual + interaction treatment

- **Section rhythm.** Alternate `var(--bg)` and `var(--bg-soft)` between sections — design.md §1.1 surface tokens. Whitelist: §02 IMPETUS · §04 UCP · §06 SPECIAL PROJECTS · §08 RECENT INNOVATIONS · §01 IMPACT use `--bg`. §03 JCP · §05 GRANARY · §07 AI-NATIVE · §09 ORGANISATION · §10 EVERY PLATFORM use `--bg-soft`.
- **Section spacing.** Vertical rhythm constrained to design.md §1.3's 48/64/96/128 stops. `py-32` (=128 px) desktop · **`py-16`** (=64 px) mobile. (Replaces the off-rhythm `py-20` from the prior draft.)
- **Tiles.** `.platform-card` (existing class) — 14 px radius, `translateY(-2px)` on hover (design.md §1.6 documented exception). **No new card variant introduced.** §06's "compact" feel comes from the 4-column-row column width, not a new CSS variant — design.md §2.1 forbids invented variants.
- **Numbers.** All numeric tiles use `.num-display` (Inter 800 · -0.04em letter-spacing · 0.9 line-height · `tabular-nums`). Sizes:
  - §01 IMPACT tiles: 64-96 px
  - Storyline section hero numbers (Move B, adopted Round 3): 96-128 px on desktop · 64-80 px tablet · 56 px mobile.
  - Layout: 2-column flex per section — hero number column ~30 % width, body column ~70 %. On mobile, stack: hero number on top, body below. Implementation lives in `index.html`'s page-level `<style>` block per design.md §3 ("Page-level inline `<style>` is acceptable for one-off layouts"). Promote to `style.css` as `.section-hero-split` only if reused on another page.
  - All numbers carry a unit qualifier in the caption (`/ day`, `· FY 26`, `· peak`) per design.md §2.9.
- **CTAs.** Per design.md §2.3 there are only two button variants — `.btn-primary` (filled) and `.btn-secondary` (outline). The hero already drops `.btn-secondary` in Round 5 (single primary CTA: `Explore 22 platforms`). The arrow `→` is rendered as a separate `<span>` after the label, not baked into the string, matching existing nav and platform-card patterns. Per-tile drill-in is the existing `.platform-card` link pattern (entire card is the anchor; no extra button inside).
- **Pills.** §02-§08 status pills use existing `.pill-live / -pilot / -build / -phase2` only. **No new pill variant** (design.md §2.2 forbids adding without docs). Pill sizing inherits the Tier 1 sweep (10 → 11 px mono).
- **Anchor links.** Each section has an `id` (`#impact`, `#impetus`, `#jcp`, …) for deep-linking. Hero CTA target is `#explore` (existing). No cycle-through.
- **Focus + reduced motion.** Implementation must include the design.md Tier 3 sweep items in the same PR — global `:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; border-radius: 4px; }` and `prefers-reduced-motion` reset. Both land in `style.css`.

---

## 7 · What stays · what changes

| Asset | Status |
|---|---|
| Auth gate (`auth.js`, Project Glass) | unchanged |
| Top nav (`tools/site_chrome.py`) | unchanged |
| Hero headline + gradient | unchanged |
| Hero CTAs | **Round 5: drop "The team" secondary CTA.** Keep only "Explore 22 platforms" primary. (Adopting Move E's mono cap subhead; org now lives at §09 not as a hero CTA.) |
| Dark footer (canonical) | unchanged |
| `style.css` design tokens | unchanged |
| `<head>` SEO defence (meta robots, vercel.json header, robots.txt) | unchanged |
| `PLATFORMS` JS inventory | augmented with a `track` field; no card-content changes |
| Section §01 Explore | renamed §09, moved below storylines |
| Sections §02–§08 | new |

Diff scope: one file (`index.html`) — section ordering + 7 new sections + 1 impact section + minor JS-array augment.

---

## 8 · Resolutions

### Round 1 · 03-May-2026 · open items resolved

| # | Question | Resolution |
|---|---|---|
| 1 | JCP framing in §01 tile #2 | **`700 K+ orders / day`** (steady state). Reject `350 K/hour peak`. |
| 2 | §01 inline `Sources · …` line | **Strip.** No source line on the page; provenance stays in this spec. |
| 3 | §06 SPECIAL PROJECTS layout (R1) | **All 7 tiles, compact 4+3 grid.** Superseded by R2-6 below. |
| 4 | §07 Kaily layout | **One tile, combined metrics.** Caption: `88 % AJIO ZIP · 96 % Netmeds · live in JioMart`. |
| 5 | NAM on the home now? | **Skip.** Stick to MDA letter; NAM lands when there is a real page. |
| 6 | §09 new filter-chip label | **`Special Projects`.** Matches MDA letter + existing mega-menu wording. |

### Round 2 · 03-May-2026 · feedback after first spec read

| # | Feedback | Resolution |
|---|---|---|
| R2-1 | Drop Granary 12 K from §01 highlights | §01 tile #4 swapped to **`88 %+ positive engagement · AJIO ZIP`** (Accenture INDEX §14 / slide 37). Granary still gets its full storyline at §05. |
| R2-2 | Replace IntelliLoom with another Impetus tile | §02 tile swapped to **Photoshoots** — strongest concrete impact line in the F&L value chain (15 days → 5 hours, Accenture INDEX §7). Alternatives audit-logged in §4 §02. |
| R2-3 | JCP headline must follow Accenture slide wording | §03 headline now reads **"Enterprise commerce platform · powering Reliance Retail"** — direct framing from slide 32 ("Jio Commerce Platform: Enterprise Commerce") and slide 35 ("Scale of Retail Transformation FY 2025-26"). Lead body uses the slide's own scale numbers (30 K+ stores · 700 K+ orders/day · 50 K+ orders/min · 200 M+ customers). |
| R2-4 | Drop RCPL from §03 JCP tiles | §03 now **3 tiles**: Channels Overview · AI Cataloging · Release Notes. RCPL placement to be decided separately by the page owner. |
| R2-5 | UCP / Marketing OS — strip jargon, lead with impact | §04 lead **rewritten**. Out: 200+ profile attributes · 1.5 M RPOS orders/day · 19 ms p50 latency · L3 → L4 agentic · DPDP-compliant · Built on Jio Cloud. In: every-customer-one-profile framing · weeks→minutes campaign cycles · lower CAC + higher repeat spend. Tile labels also stripped of L0–L5 references. |
| R2-6 | §06 SPECIAL PROJECTS — MDA-letter order + drop Forge | §06 now **6 tiles in 3+3** in the order Farooq's letter names: ALP, RetailVista (named explicitly), then Retail Jarvis, Samarth Plus, HireFirst, SwapEasy ("others"). Forge dropped — not in the letter. Forge stays on `/forge/` and in the §09 grid. Supersedes R1-3. |

---

## 9 · Implementation sequence (after sign-off)

1. **Sign-off** on §3 numbers + §8 open items.
2. **Add `track` field** to every entry in the `PLATFORMS` JS array; add the corresponding filter chip in the §09 grid.
3. **Author §01 IMPACT** as a new section directly below the hero. Single commit.
4. **Author §02 – §08 storyline sections** in MDA-letter order. One commit per section so any individual section can be reverted without unwinding the rest.
5. **Move §01 Explore → §09 Every platform.** Renumber the section label only (no CSS / JS change).
6. **Verify.**
   - `python tools/inject_chrome.py --check` exits 0
   - `python tools/inject_meta_robots.py --check` exits 0
   - DOM check via Chrome DevTools MCP: each section has a unique `id`; the §09 grid still renders all 27 cards; the new filter chip works
   - Tone-of-voice grep: no banned words, no `we / our`, no exclamations
   - Date format grep: every visible date is `DD-MMM-YYYY`
7. **Audit.** Run `website-page-reviewer` against the new home; resolve HIGH + MEDIUM findings; write the audit JSON to `docs/audits/`.
8. **PR** from `fynd-create-portfolio` → `master`.

---

## 10 · What this spec does NOT do

- Touch the auth gate, nav, footer, or any other page.
- Add new platforms or pages.
- Change the platform-card design or inventory content.
- Add `§Sources` blocks, attribution lines, or owner footers (banned per CLAUDE.md).
- Introduce marketing vocab, `we/our`, or exclamations.
- Implement anything before sign-off on §8 open items.

---

## 11 · Max-impact thinking · Round 2 proposals

The Round 1 spec covered structure. Round 2 feedback and a fresh pass surface five amplifier moves that lift the page from "well-organised" to "Apex-memorable". Each is independent — the page works without any of them; each adds proportional impact for proportional effort. Marked `(adopted)` if already folded in above.

### Move A · RR macro preface above §01 IMPACT · `(adopted)`

A single mono cap-num line frames the entire page in Reliance Retail's own scale before any Fynd numbers appear:

> *Reliance Retail · $39 B FY 25 · 19,979 stores · 378 M+ customers · #1 in Grocery, Electronics, Fashion (India)*
> **Fynd is the AI-native operating layer underneath.**

**Why it works.** Apex sees their own scale first — that creates emotional buy-in. The Fynd-delivered numbers below then read as *contributions to that scale*, not as standalone vendor stats. The Accenture deck slide 3 already speaks this language — mirroring it on the home aligns the read with how the deck frames it upward.

**Status.** Adopted in §3 above.

### Move B · Per-section hero number in display-size

Today each storyline §02–§08 has scale numbers inline within the lead paragraph (body size, easy to skip). Proposal: elevate **one** number per section to display-size on the left, with the lead paragraph wrapped to the right.

| Section | Hero number | Caption |
|---|---|---|
| §02 IMPETUS | `15.08 Cr` | Pieces shipped FY 26 |
| §03 JCP | `100+` | Brands on one stack |
| §04 UCP & Marketing OS | `380 M+` | Customers · one profile |
| §05 GRANARY | `Phase 1` | Live · 11 Mumbai stores |
| §06 SPECIAL PROJECTS | `6` | Builds · live in production |
| §07 AI-NATIVE | `88 %` | Positive engagement · ZIP |
| §08 RECENT INNOVATIONS | `7 days` | Order → doorstep · Horizon |

**Why it works.** A leader scrolling at speed reads one display number per section in 2 seconds. Numbers from §01 IMPACT echo here — repetition reinforces, which is what an Apex read needs.

**Tradeoff.** §01 IMPACT and per-section hero numbers will partly overlap (§04 hero `380 M+` = §01 tile #1, etc.). That's deliberate — `§01` is the index, the per-section hero is the proof.

**Effort.** Moderate. Layout requires a 2-column flex per storyline (number left, body right) — adds ~30 lines of CSS but no new tokens.

### Move C · Velocity strip · "shipped this month"

A one-line band at the very end of §08, before §09 grid:

> *Shipped 01 - Apr - 2026 → 03 - May - 2026 · ALP GJ-cluster live · Samarth prod cutover · Fynd Horizon Mumbai cluster · ZIP on AJIO live · Project Glass register live*

**Why it works.** Static state ("25 platforms running") tells you what *exists*. A velocity line tells you what *moved*. The combination is the difference between an inventory and an operating cadence.

**Tradeoff.** Needs a maintenance discipline — the line goes stale within ~30 days unless someone updates it. Suggest making it a `<!-- LAST_UPDATED: YYYY-MM-DD -->` block with a once-a-month sweep, OR auto-generate from `git log` of section commits.

**Effort.** Low (one HTML line). High maintenance unless automated.

### Move D · Alternate section background to break the wall

Seven storyline sections in a row risks a wall-of-content feel. Alternate `background: white` and `background: var(--bg-soft)` between sections:

- White: §02 IMPETUS · §04 UCP · §06 SPECIAL PROJECTS · §08 RECENT INNOVATIONS
- Soft: §03 JCP · §05 GRANARY · §07 AI-NATIVE
- §01 IMPACT: white (matches hero)
- §09 EVERY PLATFORM: soft (matches today)

**Why it works.** Subtle visual rhythm. Existing CSS tokens — no new design.

**Status.** Already in §6; calling out here for visibility.

### Move E · Hero subhead reinforces the scroll

Today's hero subhead is implicit (no subhead — just the H1 + CTA). Proposal: add one mono cap-num subhead under the H1, immediately previewing what's below:

> Current H1: *Making Reliance Retail the world's frontier AI-enabled retailer.*
> Add subhead (mono cap, ink-muted, 12-13 px, centred or left): *22 platforms · live · in production · scroll for the proof.*

**Why it works.** Tells the reader exactly what they'll find by scrolling. Removes ambiguity. Pairs with the Explore CTA that already exists.

**Effort.** Trivial. One line of HTML.

### Move F · Anchor-jump nav (skip if v1)

Convert the Tracks dropdown in the top nav to also offer in-page jumps to §02 IMPETUS, §03 JCP, etc. for the home page only. Lets a leader jump to a specific bucket without scrolling.

**Tradeoff.** Adds nav complexity. Apex audience is more likely to scroll than to click into nav micro-targets. Skip for v1, revisit if the page proves long.

---

### Round 3 adoption status

| Move | Status | Lands in |
|---|---|---|
| A · RR macro preface | **Adopted** | §3 above |
| B · Per-section hero number | **Adopted** | §02–§08 above + §6 visual treatment |
| C · Velocity strip | **Skipped** | — |
| D · Alternate section background | **Adopted** | §6 visual treatment |
| E · Hero subhead | **Adopted** | hero block (Move E wording: *"22 platforms · live · in production · scroll for the proof."*) |
| F · Anchor-jump nav | Deferred | revisit post-launch |

Implementation sequence (§9) gets two extra steps for the adopted Round 3 moves:

- **9.4a** — Hero subhead (Move E) — single Edit on `index.html`
- **9.5a** — Per-section hero-number layout for §02–§08 (Move B) — adds a 2-column flex template per storyline section

---

## 12 · Round 3 resolutions · 03-May-2026

All five outstanding decisions resolved by the page owner. Spec is now fully locked; no remaining blockers for implementation.

| # | Decision | Resolution |
|---|---|---|
| O-1 | Move B · per-section hero number | **Adopt.** Each §02–§08 elevates one number to display size on the left; lead body wraps right. Hero numbers locked per Move B table — see each section above for the chosen number + caption. |
| O-2 | Move C · velocity strip | **Skip.** Page reads as inventory of state, not cadence. No "shipped this month" line. (O-5 moot.) |
| O-3 | Move E · hero subhead | **Adopt.** Add mono cap subhead under H1: *"22 platforms · live · in production · scroll for the proof."* |
| O-4 | RCPL placement (Round 3) | Was: **Add to §06 SPECIAL PROJECTS as a 7th tile.** **Reversed in Round 4** — see §13 below. RCPL deferred entirely; revisit placement separately. |
| O-5 | Velocity-strip wording | n/a — Move C skipped. |

---

## 13 · Design system inheritance

`docs/design.md` is the canonical visual register. This section locks every design choice in §3-§9 to a specific design.md token, class, or rule — so the implementation cannot drift. **Reading order for the implementer:** read this section first, then return to §3-§9 for the per-section content.

### 13.1 · Token + class map · per home section

| Home component | design.md class / token | design.md ref |
|---|---|---|
| Page surface alternation | `var(--bg)` and `var(--bg-soft)` (no other backgrounds) | §1.1 |
| Hero H1 | `.display` class · period at end intentional | §1.2 + Page anatomy |
| Hero subhead (Move E) | `.cap-num` · 12 px JetBrains Mono · color `#4B5563` · letter-spacing 0.04em · uppercase | §1.2 + Tier 1 |
| §01 IMPACT preface | same as hero subhead — `.cap-num` · 12 px mono · `#4B5563` | §1.2 + Tier 1 |
| §01 IMPACT tile container | `.card p-6` · 12 px radius · 1 px `var(--border)` (post-Tier-1: `#D4D4D4`) | §2.1 + Tier 1 #4 |
| §01 IMPACT tile number | `.num-display` · Inter 800 · `tabular-nums` · 64-96 px sized inline | §1.2 + §2.9 |
| §01 IMPACT tile caption | `.cap-num` (label) + body Inter 14 px (description) | §2.9 |
| §02-§08 storyline section | Outer `<section>` · `py-32` desktop · `py-16` mobile (= 128 px / 64 px on the design.md 48/64/96/128 rhythm) | §1.3 |
| §02-§08 section label | `.section-label mb-3` · `§ ` prefix auto-injected via `::before` (don't hand-type) · contiguous numeric run | §2.8 |
| §02-§08 section H2 | `.display-2` · -0.03em letter-spacing · 1.05 line-height | §1.2 |
| §02-§08 hero number (Move B) | `.num-display` · `tabular-nums` · 96-128 px desktop / 64-80 px tablet / 56 px mobile | §1.2 + §2.9 |
| §02-§08 platform tiles | `.platform-card` (existing) · 14 px radius · `translateY(-2px)` hover (allowed exception per §1.6) | §2.1 |
| §02-§08 status pills | `.pill-live / .pill-pilot / .pill-build / .pill-phase2` only — no new variants | §2.2 |
| §02-§08 per-tile drill-in | Whole `.platform-card` is the anchor (existing pattern) — no inner button | §2.1 |
| §06 SPECIAL PROJECTS layout | Standard `.platform-card` in 3+3 grid — no "compact" variant | §2.1 |
| §09 ORGANISATION highlight tiles | `.card p-5` · `.num-display` (32-48 px) + `.cap-num` label | §2.1 + §2.9 |
| §09 ORGANISATION drill-down tiles | `.platform-card` (same as storyline sections) | §2.1 |
| Hero CTA | `.btn-primary` only (Move E + Round 5 dropped secondary) · 999 px radius · arrow `→` as separate `<span>` after label | §2.3 |
| Section CTAs | `.btn-secondary` per section · 999 px radius · arrow `→` as separate `<span>` | §2.3 |
| Numbers · Indian large | `L` and `Cr` (`200 Cr`, `15.08 Cr`, never `2,000,000,000`) | §2.9 |
| Numbers · approximations | Carry `~` in caption (`~200 in 2014`) | §2.9 |
| Numbers · units | Always carry a unit qualifier in caption (`/ day`, `· FY 26`, `· peak`) | §2.9 |
| Motion · all transitions | 150-300 ms · transform + opacity only · no bounce | Motion |
| Page-local CSS | Page-level `<style>` block in `<head>` for one-offs (Move B's 2-col flex). Promote to `style.css` as `.section-hero-split` only if reused. | Page anatomy + §3 code conventions |

### 13.2 · Sweep items adopted in this PR

These design.md §7 sweep items must land in the same PR as the home redesign — three of them are visible on every new section the home ships, so launching the home without them would advertise the readability tax we're trying to remove.

| design.md ref | Change | Edit |
|---|---|---|
| Tier 1 #1 | Bump 11 px mono → **12 px** on `.section-label`, `.crumb`, `.subnav-link`, `.cap-num`, `table.grid-table th`, `.nav-version`, `.mega-col-label` | `style.css` (single sweep) |
| Tier 1 #2 | Bump 10 px mono → **11 px** on `.pill`, `.mega-link .mono-suffix` | `style.css` |
| Tier 1 #3 | Darken caption color `--ink-muted` → `#4B5563` on `.section-label`, `.crumb`, `.cap-num`, `table.grid-table th`, `.mega-col-label` | `style.css` |
| Tier 1 #4 | Darken `--border` token `#E5E5E5` → `#D4D4D4` (cascades to cards, tables, mega-panel, pills) | `style.css :root` |
| Tier 3 #8 | Global `:focus-visible` ring with `--accent` outline | `style.css` |
| Tier 3 #10 | `prefers-reduced-motion` reset (zero all transitions and animations) | `style.css` |

All six are single-file edits to `style.css`; together they're roughly 15 lines of diff that cascade across all 70 pages.

### 13.3 · Sweep items deferred (out of this PR)

| design.md ref | Why deferred |
|---|---|
| Tier 2 #5 — body line-height 1.55 | Touches every page; risk of subtle layout shift. Separate PR. |
| Tier 2 #6 — `.prose { max-width: 70ch }` | Needs per-page application; not on home. Separate PR. |
| Tier 2 #7 — button text 14 → 15 px + padding `12 22` → `13 24` | Visible on every page; ship as a coordinated visual sweep. Separate PR. |
| Tier 3 #9 — Crumb anchor tap-area padding | No crumbs on the home; not needed here. Separate PR for crumb-bearing pages. |
| Tier 3 #11 — `aria-label` on icon-only links/buttons | Per-page audit needed; separate PR after a sitewide grep. |
| Tier 4 #12 — typed scale tokens | Bigger call; revisit once Tier 1-3 sweep settles. |
| Tier 4 #13 — `.tabular` utility class | Until then, use inline `font-variant-numeric: tabular-nums` on home (already specified in §13.1). |
| Tier 4 #14 — Decide on `translateY(-2px)` hover | Editorial call deferred; home keeps existing behaviour. |

### 13.4 · Anti-patterns to avoid · drawn from design.md "Don't" list

These are the design.md "Don't"s that this implementation could realistically violate if not flagged:

- ❌ **No new hex literals.** Every color in the home page must come from `:root` tokens. If a tile background isn't `--bg` or `--bg-soft`, stop and use a token.
- ❌ **No new pill variant.** §02-§08 status pills use only `.pill-live / .pill-pilot / .pill-build / .pill-phase2`. If a status word doesn't fit those four, change the word, not the CSS.
- ❌ **No off-rhythm spacing.** Section padding must be on the 48/64/96/128 stops; card padding must be `p-4 / p-5 / p-6 / p-8`. No `13`, `18`, `20`, `30` anywhere.
- ❌ **No off-scale font sizes.** No `text-[Npx]` Tailwind arbitrary classes for font-size. Stay on the documented scale (18 / 16 / 15 / 14 / 13 / 12 / 11 px per §1.2).
- ❌ **No new card hover lift.** `.card-hover` darkens border only. The two `translateY(-2px)` exceptions (`.lens-card`, `.platform-card`) are documented; don't add a third.
- ❌ **No bounce / elastic motion.** Linear/default easing only.
- ❌ **No editing nav or footer HTML in `index.html` directly.** If §06's `Special Projects` filter chip needs a nav-side mention, edit `tools/site_chrome.py`.
- ❌ **No color-only status.** Every pill carries a text label.
- ❌ **No mono < 11 px.** Especially relevant if any tile-suffix or status-line tries to fit smaller.
- ❌ **No `we / our` / first-person plural** (CLAUDE.md tone-of-voice rule, not design.md, but co-located with this implementation).

### 13.5 · Verification commands · post-implementation

Run these after the home implementation lands and before opening the PR:

```bash
# 1 · Section labels are a contiguous numeric run on the home
grep -n 'section-label mb-3">[0-9]' index.html
# expect: 01 02 03 04 05 06 07 08 09 10 (no skips)

# 2 · No new hex literals introduced on the home
grep -nE '#[0-9A-Fa-f]{3,8}' index.html | grep -vE '#fafa|#fff|#ffffff|#1a1a' | head
# expect: empty (every color comes from a :root token)

# 3 · No off-scale font-size literals
grep -nE 'text-\[[0-9]+px\]|font-size:\s*[0-9]+px' index.html | head
# expect: only the documented 64/96/128 px display sizes for .num-display

# 4 · No new pill class
grep -oE 'pill pill-[a-z0-9-]+' index.html | sort -u
# expect: only pill-live / pill-pilot / pill-build / pill-phase2 / pill-accent

# 5 · Chrome canonical sweep still clean
python tools/inject_chrome.py --check
# expect: exit 0

# 6 · Meta-robots sweep still clean
python tools/inject_meta_robots.py --check
# expect: exit 0

# 7 · No banned tone-of-voice vocab
grep -oE '\b(transformative|world-class|cutting-edge|game-changing|next-generation|best-in-class|empowers|enables|unlocks|leverages|harnesses)\b' index.html
# expect: empty

# 8 · No we/our
grep -oE '\b(we|our|We|Our)\b' index.html | head
# expect: empty (or only inside <code> / <pre> if any)
```

### 13.6 · Pre-flight before opening the PR

- [ ] Run §13.2 sweep edits in `style.css` and confirm no visual regression on three reference pages: `/jcp/`, `/impetus/`, `/granary/`.
- [ ] Run all eight verification commands in §13.5.
- [ ] Run `website-page-reviewer` skill against the new home; resolve all HIGH and MEDIUM findings.
- [ ] DOM check via Chrome DevTools MCP — each section has its `id`, all anchor links resolve, `:focus-visible` ring renders on a Tab through the page.
- [ ] Mobile check at 375 px and 768 px viewports.
- [ ] Hard refresh in incognito to confirm `auth.js` Project Glass gate still renders cleanly above the redesigned home.

### Round 4 · 03-May-2026 · post-Round-3 corrections

| # | Correction | Resolution |
|---|---|---|
| R4-1 | RCPL not in §06 SPECIAL PROJECTS after all | **§06 reverts to 6 tiles in a 3+3 grid.** Hero number drops from `7` to `6`. RCPL's home placement deferred — handle in a separate call. |
| R4-2 | Samarth Plus and HireFirst are independent projects | **No connecting glyphs between any tiles in §06.** Tiles separated only by the standard grid gap. The `→` used in the spec summary to denote row break was notation only — never a UX element. Adding an explicit "no connecting glyphs" rule to §06 to prevent any visual implication of sequence, especially between Samarth Plus and HireFirst. |

### Round 5 · 03-May-2026 · org section + hero CTA cleanup

| # | Feedback | Resolution |
|---|---|---|
| R5-1 | Add a section on the org with highlights + drill-down to deeper pages | **New §09 ORGANISATION** added between §08 Recent Innovations and the platform grid. Hero number `1,100+ people · 14 years`. Four small numeric highlight tiles (people, builders, AI-native, values) + four drill-down platform-card tiles linking to `/organisation/`, `/culture/`, `/ai-native/`, `/fynd-academy/`. Sources: Unlocking Growth deck slides 16, 17, 20, 21, 22, 23, 25. |
| R5-2 | Drop "The team" CTA from the first-fold hero | **Hero now has one CTA only:** `Explore 22 platforms →`. The Team secondary CTA removed to avoid undue org focus on first read; org gets its own §09 section deep into the scroll. |
| R5-3 | EVERY PLATFORM grid renumbered §09 → §10 | Mechanical change to make room for §09 ORGANISATION. §08 Recent Innovations CTA wording updated to point at §10 grid (was §09). Section label on the grid changes from `09 · Every platform` to `10 · Every platform`. |
| R5-4 | Swap 3.8 M+ retailers tile in §01 IMPACT | **Replace tile #5 with `20 K+` stores connected on JCP** (Unlocking Growth slide 29 · Platform Health Metrics). Conservative reading of stores served — Accenture slide 35 says 30 K+, Unlocking Growth slide 29 says 20 K+; using the lower number to stay defensible. Caption: *Stores connected on JCP across the Reliance Retail estate*. Pivots the angle from B2B retailer count to physical store reach — easier for an Apex read to land. |

### Round 6 · 03-May-2026 · post-audit fixes (audit `docs/audits/home-redesign-audit-2026-05-03.json`)

The page-reviewer skill flagged 8 findings on the v1 implementation (1 CRITICAL, 2 HIGH, 4 MEDIUM, 1 LOW). All applied; spec updated to lock the corrected values so future revisions don't pull stale inputs.

| # | Audit ref | Finding | Resolution |
|---|---|---|---|
| R6-1 | C1 (CRITICAL · source) | §09 ORG `₹2,500 Cr platform GMV` was off by 10× — Unlocking Growth slide 25 says `$2.5 B Annual Platform GMV` | Page + spec render `$ 2.5 B platform GMV (~₹ 20,000 Cr)`. |
| R6-2 | H1 (HIGH · source) | `79 channels live` overclaim in §01 tile #2 + §03 lead — only 68 of 79 are live | Both render `79 channels · 68 live · 700 K+ orders / day`. Matches existing /jcp PLATFORMS metric. |
| R6-3 | H2 (HIGH · cross-page) | Hero claimed `25 platforms` but PLATFORMS array had 27 entries (17 platforms + 10 context-pages) | Drop the 5 context-page entries from PLATFORMS (`/culture`, `/organisation`, `/autonomous`, `/agents`, `/ai-native`) — those live in §09 ORG drill-down tiles + the `/more` mega-menu column. Updated count: **22 platforms**. All 4 copy locations updated (hero CTA, hero subhead, §01 IMPACT tile #6, §09 ORG headline, §10 grid H2 + counter). |
| R6-4 | M1 (MED · source) | `11.06 L POs automated` conflated two metrics — Unlocking Growth slide 6 says `460 K+ POs automated`; `11.06 L POs FY 26` is the total POs from /impetus PLATFORMS metric | §01 tile #3: `11.06 L POs FY 26 · 43 brands live`. §02 IMPETUS lead: `11.06 L POs FY 26 · 460 K+ POs automated · 720 K articles packed / day · 43 brands live`. Both metrics surfaced; "automated" qualifier no longer over-applied. |
| R6-5 | M2 (MED · honesty) | §06 hero `6 · Builds · live for Reliance` overclaimed — Retail Jarvis is BUILD, not LIVE | Caption now reads `6 · Builds for Reliance` (drops the "live" overclaim; the per-tile pills still show the honest LIVE / BUILD split). |
| R6-6 | M3 (MED · design) | `.impact-tile { padding: 32px 28px; }` — 28px off the design.md 4/8 padding rhythm | Now `padding: 32px;` uniform (matches design.md §1.3 `p-8` spec). |
| R6-7 | M4 (MED · source) | §04 UCP lead said `70+ other formats`; existing /ucp page + /ucp PLATFORMS metric say `75+ formats` | §04 lead now reads `…and 75+ other formats…`. |
| R6-8 | L1 (LOW · design) | §01 section-label had `style="display: inline-block;"` workaround | Inline override removed — works fine without it inside the `text-center` parent. |
| R6-9 | (paired w/ R6-1) | UCP identity count: page + 7 underlying .md files said `400 M+`. Per page owner direction · 03-May-2026: Reliance Retail registered customer count is 387 M, so `380 M+` is the defensible UCP identity number | Sweep applied across `index.html` (4 occurrences), `ucp/index.html` (4), `docs/home-redesign-spec.md` (4), `docs/ucp-marketing-os-spec.md` (4), `docs/home-restructure-spec.md` (2), `data/SCHEMA.md` (1), `data/ips/ucp/narrative.md` (1), `.claude/skills/website-tone-of-voice.md` (1 example). Tile #1 caption now appends `(RR registered customers · 387 M)` for transparency. |

**What's NOT updated** (intentional, per audit-trail integrity):
- `data/research/2026-04-29-farooq-mda-persona-review.md` and `data/research/2026-04-30-mda-second-review.md` — these are *historical research notes* that documented the customer-number inconsistency at the time. Overwriting them would erase the audit trail showing how the 380 M+ resolution was reached. They stay as-is.
