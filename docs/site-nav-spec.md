# Site Navigation · v0.1 spec

**Author** · Kushan Shah · **Date** · 2026-05-01 · **Owner** · Fynd

A single coherent navigation across the entire Fynd × RRVL · JPL register, mirroring the structure of [Farooq's MM Sir update letter](/docs/2026-04-30-farooq-mda-update-letter.md) and engineered for rapid extension as new sections land in the next few hours / days.

---

## §1 · Why now

The current nav has three problems:

1. **Duplication.** `/jcp` lives in the *Platform* column and `/jcp/channels` + `/jcp/cataloging` repeat in the *Capability* column. Same for `/impetus` (Platform) vs `/impetus/videos`, `/impetus/photoshoots`, `/impetus/brands`, `/autonomous` (Capability). Users see "JCP" and "Impetus" in two places.
2. **Wrong axes.** The menu is grouped *Platform · Vertical · Capability*, but a platform IS a capability and the *Vertical* column conflates customers (RBL, RCPL) with platforms (Samarth, ALP, Forge, HireFirst, etc.). The taxonomy is inconsistent with how leadership talks about the work.
3. **Inelastic.** Nav HTML is hand-rolled inline across **25 files** in two different generations. Adding a new section means editing 25 places, by hand, and they drift.

Farooq's letter to MM Sir (2026-04-30) names the canonical taxonomy. We adopt it as the source of truth.

---

## §2 · Page inventory (50 pages today)

### Top-level (6)
- `/` · home register
- `/numbers`
- `/organisation`
- `/culture`
- `/catalog` · IP Catalog
- `/docs`

### Track A · Impetus · F&L AI (24)
- `/impetus` · overview
- 16 sub-platforms · `ai-photoshoot`, `analytics`, `autonomy`, `companion-app`, `cortex`, `costing-engine`, `gmetri`, `instadesk`, `intelliloom`, `intelliverse`, `master-hub`, `nextwave`, `plm`, `pulsepoint`, `recollect`, `uvp`
- 4 capability galleries · `brands`, `photoshoots`, `videos`, `category-intel`
- 4 category-intel reports · `mens-polos-aw26-india`, `mens-shirts-ss27-india`, `mens-tshirts-ss27-india`, `midi-dress-ss27-india`
- 4 photoshoots case studies · `ajio-asos-plus-size-launch`, `buda-jeans-harry-potter`, `buda-jeans-valentines`, `ss26-plm-ai-photoshoot-pilot`

### Track B · JCP · Jio Commerce Platform (3)
- `/jcp` · overview
- `/jcp/channels` · 78 channels gallery
- `/jcp/cataloging` · AI Cataloging surface

### Track C · Granary · Grocery AI (2)
- `/granary` · overview
- `/granary/research/transforming-retail-forecasting` · research paper

### Track D · Special Projects (8)
Standalone platforms / verticals that ride alongside the major tracks:
- `/alp` · Activity Linked Pay
- `/retail-vista` · planning + analytics
- `/retail-jarvis` · ops AI
- `/samarth` · workforce
- `/forge` · MES
- `/hirefirst` · HR Tech
- `/rbl` · brand house (currently top-level)
- `/rcpl` · consumer products (currently top-level)

### Stand-alone & utility (6)
- `/autonomous` · L0–L5 autonomy framework (referenced by every platform page)
- `/fynd-academy` · talent / training
- `/numbers` · KPI dashboard
- `/organisation` · ~430 on RR
- `/culture`
- `/catalog` · IP Catalog
- `/docs` · internal docs index

### Not yet built (named in Farooq's letter)
- `/ucp` · UCP & Marketing OS
- `/boltic` · agentic automation
- `/pixelbin` · agentic automation
- `/ratl` · agentic automation
- `/kaily` · agentic commerce (live in JioMart and AJIO)
- `/fynd-horizon`
- `/autri`
- `/dark-factory` · Made-to-Measure

The structure must accommodate these placeholders today so they can be linked the moment each page is created.

---

## §3 · Taxonomy from Farooq's letter

> "Impetus: details of all sub-platforms deployed, adoption across the value chain of F&L."
>
> "Fynd – Retail Projects: details of all platforms, adoption with dedicated people involved. Platforms involved:
> Jio Commerce Platform · UCP & Marketing OS · Granary · Special Projects (ALP, RetailVista, others) · AI-Native Platforms (Boltic, PixelBin, Ratl; Kaily) · Recent Innovations (Fynd Horizon, Autri, Dark Factory)."

This collapses into **6 buckets**:

| # | Bucket | Hub | Today | Coming |
|---|--------|-----|-------|--------|
| A | **Impetus** | `/impetus` | 24 pages | — |
| B | **Jio Commerce Platform** | `/jcp` | 3 pages + sub-page rollouts (RBL, RCPL) | — |
| C | **UCP & Marketing OS** | `/ucp` | — | hub + sub-pages |
| D | **Granary** | `/granary` | 2 pages | — |
| E | **Special Projects** | (no hub — chips only) | ALP, RetailVista, Retail Jarvis, Samarth, Forge, HireFirst | — |
| F | **AI-Native Platforms** | (no hub — chips only) | — | Boltic, PixelBin, Ratl, Kaily |
| G | **Recent Innovations** | (no hub — chips only) | — | Fynd Horizon, Autri, Dark Factory |

Plus utility pages (Numbers, Org, Culture, Catalog, Autonomy framework, Fynd Academy, Docs).

---

## §4 · Proposed structure

### §4.1 · Topnav — global, identical on every page

```
[Fynd × RRVL · JPL]   Home   Tracks ▾   Numbers   More ▾                v0.8.4
```

### §4.2 · Tracks mega-menu — 3 columns

```
TRACKS ▾
┌─────────────────────────────────────────────────────────────────────────────┐
│ PLATFORMS                SPECIAL PROJECTS        AI-NATIVE                  │
│ Impetus      · F&L AI    ALP                     Boltic      · agentic auto │
│ JCP          · 78 ch     Retail Vista            PixelBin    · agentic auto │
│ Granary      · Grocery   Retail Jarvis           Ratl        · agentic auto │
│ UCP & Mktg OS            Samarth                 Kaily       · commerce     │
│                          Forge MES                                          │
│                          HireFirst    · HR Tech                             │
│                                                  RECENT INNOVATIONS         │
│                                                  Fynd Horizon               │
│                                                  Autri                      │
│                                                  Dark Factory · made-to-… │
└─────────────────────────────────────────────────────────────────────────────┘
```

Properties:
- The mega-menu only shows **hub links** — never sub-pages — so JCP appears once, Impetus appears once.
- Right-hand column stacks AI-Native (top half) + Recent Innovations (bottom half) with a label divider between them.
- Empty rows under each column reserve space; new entries slot in.

### §4.3 · Per-platform subnav — chips at the top of each hub

Each hub page renders its own subnav strip just below the breadcrumb. This is where sub-pages of the hub live — they are *not* duplicated in the mega-menu.

**`/jcp` subnav** (and on every `/jcp/*` page)
```
[ Overview ] [ Channels ] [ AI Cataloging ] [ RBL ] [ RCPL ]
```
RBL and RCPL move under JCP because they are customer rollouts of the JCP platform, not standalone platforms.

**`/impetus` subnav** (and on every `/impetus/*` page)
```
[ Overview ] [ Brands ] [ Photoshoots ] [ Videos ] [ Category Intel ] [ Autonomy ]
```
The 16 sub-platform pages (Cortex, PLM, NextWave, etc.) are reached from the `/impetus` overview hub itself — too many for a chip strip.

**`/granary` subnav**
```
[ Overview ] [ Research ]
```

**Special Projects, AI-Native, Recent Innovations** — these buckets have no hub page. Each entry IS a hub. No subnav needed unless an entry sprouts sub-pages later.

### §4.4 · More menu — 6 utility links

```
MORE ▾
┌─────────────────────────────────────────┐
│ Numbers                                 │  (also a top-level chip)
│ Autonomy framework         · L0–L5     │
│ Organisation               · ~430 RR    │
│ Culture                                 │
│ IP Catalog                 · all IPs    │
│ Fynd Academy               · talent     │
└─────────────────────────────────────────┘
```

Numbers appears both as a top-level chip (for prominence) and inside More (for completeness).

### §4.5 · What disappears

- The current "Vertical" column (Samarth, RCPL, RBL, Retail Vista, Retail Jarvis, ALP, Forge, HireFirst) — entries get redistributed into Special Projects (their real home) or under JCP (RBL, RCPL).
- The current "Capability" column entirely — its entries are either hubs (which move to Platforms) or sub-pages (which move to per-hub subnav strips).
- All in-line variation across 25 hand-rolled topnav blocks.

---

## §5 · Implementation

### §5.1 · Source of truth · `tools/site_chrome.py`

A single Python module exposes:

```python
PLATFORMS         = [...]   # mega-menu column 1
SPECIAL_PROJECTS  = [...]   # mega-menu column 2
AI_NATIVE         = [...]   # mega-menu column 3 (top)
RECENT_INNOVATIONS = [...]  # mega-menu column 3 (bottom)
MORE_MENU         = [...]   # More dropdown
SUBNAV            = {       # per-track chip strips
  "jcp":     [...],
  "impetus": [...],
  "granary": [...],
}

def topnav() -> str: ...
def footer() -> str: ...
def subnav_html(track: str, active_href: str = "") -> str: ...
```

**Adding a new section** = append one dict to the right list → rerun `tools/inject_chrome.py` → done. No HTML editing.

### §5.2 · Builder integration

- `tools/build_impetus.py` — replace its inline `topnav()` / `footer()` functions with `from site_chrome import topnav, footer`.
- `tools/build_jcp_channels_page.py` — same.
- Future builders (UCP, AI-Native, Recent Innovations hubs) — import the same module.

### §5.3 · Static HTML migration · `tools/inject_chrome.py`

A one-shot script that:
1. Globs every `index.html` under the repo root (excluding `.venv`, `node_modules`, `.git`, `.vercel`).
2. Locates the `<nav class="topnav">…</nav>` block via a marker scan.
3. Replaces it with the rendered `site_chrome.topnav()` HTML.
4. Same for `<footer …>…</footer>`.
5. Idempotent — running it again on already-converted pages is a no-op (the nav block is byte-equal).

Runs in seconds across all 25 files.

### §5.4 · Cache & rollout

Topnav HTML is inline (no separate request) so no cache busting needed. Re-deploy via Vercel; new nav lands on next build.

---

## §6 · Migration plan

| Step | Action | Owner | Status |
|------|--------|-------|--------|
| 1 | Land this spec | Kushan | _draft_ |
| 2 | Implement `tools/site_chrome.py` per §5.1 | Claude | done (draft, awaits review) |
| 3 | Wire `build_impetus.py` + `build_jcp_channels_page.py` to import from `site_chrome` | Claude | pending |
| 4 | Implement `tools/inject_chrome.py` per §5.3 | Claude | pending |
| 5 | Run injector across all 25 static `index.html` files | Claude | pending |
| 6 | Add `subnav_html("jcp", current_path)` to `/jcp/index.html`, `/jcp/cataloging/index.html`, `/jcp/channels/index.html` | Claude | pending |
| 7 | Add equivalent subnav to `/impetus/index.html` + each `/impetus/*/index.html` (or do it in `build_impetus.py`) | Claude | pending |
| 8 | Add subnav to `/granary` + `/granary/research/*` | Claude | pending |
| 9 | Sanity sweep — load each top-level page in browser, click every nav link, confirm no 404s | Claude + Kushan | pending |
| 10 | Stub-page sweep — for the 8 unbuilt sections (UCP, Boltic, PixelBin, Ratl, Kaily, Fynd Horizon, Autri, Dark Factory), decide whether to ship a "coming soon" placeholder so links don't 404 | Kushan | pending |

---

## §7 · Extending the nav · adding a new section

To add (say) `/kaily` with a sub-page `/kaily/jiomart`:

1. Edit `tools/site_chrome.py`:
   ```python
   AI_NATIVE = [
       ...,
       {"href": "/kaily", "label": "Kaily", "suffix": "live in JioMart + AJIO"},
   ]
   SUBNAV["kaily"] = [
       {"href": "/kaily",         "label": "Overview"},
       {"href": "/kaily/jiomart", "label": "JioMart rollout"},
   ]
   ```
2. Run `python tools/inject_chrome.py` → nav updates everywhere.
3. Build the new pages (`kaily/index.html`, `kaily/jiomart/index.html`) and include `{topnav()}` / `{footer()}` from site_chrome.

That's it. No grep-and-replace across the site.

---

## §8 · Open questions

- **`/autonomous` placement.** It's a framework page referenced by every platform's "path to L3/L4" section. Currently put it in **More** menu under "Autonomy framework". Could also be a chip in Tracks. Defaulting to More for now — re-visit if engagement shows users hunt for it.
- **Mobile nav.** This spec covers desktop only. Below `md` breakpoint the topnav collapses today (no `nav-mega` panels). Need a separate mobile drawer pattern — out of scope for this pass.
- **Cross-section search.** With 50+ pages a small `⌘K`-style command palette would help. Future work.
