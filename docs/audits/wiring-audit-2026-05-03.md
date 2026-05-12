# Inter-page wiring audit · 2026-05-03

Branch: `feat/jcp-parity-fixes`
Repo: `/Users/salmansaudagar/reliance-retail-fynd/`
Preview: `http://localhost:8765/` (Python SimpleHTTP)
Production routing: Vercel `cleanUrls: true`, `trailingSlash: false`

## Summary

- HTML pages scanned: 75 (excluding `tools/scratch/*` extracts and `docs/impetus-index-backup-2026-04-30.html`)
- Internal absolute href values (unique): 166
- Internal HTML routes (after stripping asset paths): 49 unique
- Anchor links (`#fragment`): 162 unique values across pages
- Internal asset references (`/assets/`, `/docs/`, `/images/`, `/data/`): 72 unique
- External (https://) links: 162 unique
- HTTP-only (insecure): 0
- mailto / tel: 1 / 0

Net result: routing is in solid shape. **2 broken HTML routes** in canonical chrome (1 sub-nav, 1 mega-menu sub-link), **0 broken anchors on same page**, **0 missing assets**, **0 surviving `/jcp/rcpl/` HTML route refs**, chrome injection clean across the board.

---

## Findings by severity

### Critical (navigation / canonical chrome)

#### C1 · `/granary/research/` is wired into the canonical Granary sub-nav but the page does not exist
- Source · `tools/site_chrome.py:206-208` (canonical sub-nav definition for Granary), injected into `granary/index.html:87`
- Target file expected · `granary/research/index.html`
- Status · file missing on disk; preview returns `HTTP 404`
- Impact · every visitor to `/granary` sees a "Research" tab in the page chip-nav, which 404s on click
- Suggested fix · either (a) ship a stub `granary/research/index.html` page or (b) remove the entry from `tools/site_chrome.py` SUB_NAVS["granary"] and re-run `inject_present.py` to scrub the chip from `granary/index.html`

#### C2 · `/impetus/photoshoots/` mega-menu sub-link has no `index.html`; resolves only because Python SimpleHTTP shows a directory listing
- Source · `tools/site_chrome.py:202` (Impetus sub-nav: `{"href": "/impetus/photoshoots", "label": "Photoshoots"}`)
- Target file expected · `impetus/photoshoots/index.html`
- Status · directory exists with 4 child case-study pages, but no parent index. Local preview returns `HTTP 200` with a Python `Directory listing for /impetus/photoshoots/` page. **On Vercel (production) this will 404** because Vercel does not auto-list directories.
- Impact · clicking "Photoshoots" in the Impetus chip-nav 404s in production even though it works locally — silent regression that won't surface until deploy
- Suggested fix · ship `impetus/photoshoots/index.html` (an index of the four case studies), or drop the entry from `SUB_NAVS["impetus"]` in `tools/site_chrome.py`

### High (in-body broken)

None. Every in-body card / button / inline anchor that points at an internal HTML route resolves to an existing `index.html`.

### Medium (Receipts / footnotes)

None. All 28 spot-checked Receipts asset paths across the 5 Wave-3 pages (fynd-konnect, boltic, autri, forge, samarth) resolve on disk. Full asset sweep below shows 0/72 missing.

### Low (in JS / comments / archived files)

#### L1 · `/catalog`, `/numbers`, `/rbl`, `/impetus/videos` referenced from `docs/impetus-index-backup-2026-04-30.html`
- That file is an explicit backup snapshot per its name. It is not linked from any live page (verified — 0 live references).
- Containment is good. Suggested fix · move the backup to `docs/_archive/` or rename with a leading underscore so future audits ignore it cleanly.

#### L2 · `/jcp#autri` cross-page anchor referenced only from the same backup file
- Same containment as L1. No action needed beyond archiving the backup.

---

## Mega-menu audit

Source of truth · `tools/site_chrome.py` — `MENU_PLATFORMS` (5), `MENU_PLATFORMS_MORE` (8), `MENU_AGENTS` (10), `MENU_INITIATIVES` (3), `MENU_FYND` (6) = **32 top-level entries**, plus sub-nav entries for jcp/impetus/granary/pixelbin = **+11 sub-links**.

| Area | Routes | All resolve? |
|---|---|---|
| Top-level mega-menu | 32 | yes (32/32) |
| `SUB_NAVS["jcp"]` | 5 | yes |
| `SUB_NAVS["impetus"]` | 4 | **no** — `/impetus/photoshoots` (no `index.html`, see C2) |
| `SUB_NAVS["granary"]` | 2 | **no** — `/granary/research` (no dir at all, see C1) |
| `SUB_NAVS["pixelbin"]` | 3 | yes |

### Orphan top-level pages (exist on disk, not in mega-menu)

None. Every top-level directory with an `index.html` is reachable from the mega-menu. Spot-checked:
- `agents`, `ai-native`, `alp`, `autonomous`, `autri`, `boltic`, `culture`, `dark-factory`, `forge`, `frameworks`, `fynd-academy`, `fynd-horizon`, `fynd-konnect`, `granary`, `hirefirst`, `impetus`, `jcp`, `kaily`, `kio`, `organisation`, `pixelbin`, `ratl`, `rcpl`, `retail-jarvis`, `retail-vista`, `samarth`, `swapeasy`, `tms`, `ucp` — all in `MENU_*` lists.

Sub-pages NOT advertised in mega-menu but reachable from their parent (deliberate, not orphans):
- `agents/agentic-marketing`, `agents/ai-cataloging`, `agents/ai-photoshoot`, `agents/category-intelligence`, `agents/cortex-planning`, `agents/retail-vista`, `agents/trend-to-design` — child cards on `/agents`
- `impetus/*` (analytics, brands, category-intel, companion-app, cortex, costing-engine, gmetri, instadesk, intelliloom, intelliverse, master-hub, nextwave, plm, pulsepoint, recollect, uvp, ai-photoshoot) — sub-IPs surfaced from `/impetus`
- `impetus/category-intel/{mens-polos-aw26-india, mens-shirts-ss27-india, mens-tshirts-ss27-india, midi-dress-ss27-india}` — case studies under category-intel
- `impetus/photoshoots/{ajio-asos-plus-size-launch, buda-jeans-harry-potter, buda-jeans-valentines, ss26-plm-ai-photoshoot-pilot}` — case studies under photoshoots (parent index missing — see C2)
- `jcp/{7eleven, cataloging, channels, release-notes}` — surfaced via JCP sub-nav (verified resolves)
- `organisation/{directory, external, organogram}` — surfaced via internal nav on `/organisation`
- `pixelbin/{glamar, videos}` — surfaced via PixelBin sub-nav
- `docs/index.html` — internal docs index, deliberately unlisted
- `data/ips/ucp/assets/decks/{RD-Digital-Discount-Days-Dashboard,UCP-Release-Notes-Timeline}.html` — embedded asset decks linked from `/ucp`

### RCPL promoted to top-level Platforms entry

Verified · `tools/site_chrome.py:28` includes `{"href": "/rcpl", "label": "RCPL", "suffix": "FMCG B2B"}` in `MENU_PLATFORMS`. `rcpl/index.html` exists and resolves with `HTTP 200`. Old route `/jcp/rcpl/*` returns 0 HTML route references in live pages.

---

## Anchor / TOC audit

- Pages with anchor links (`href="#..."`): 70 of 75
- Total anchor link instances: 162 unique fragment values
- **Orphan anchors (link with no matching `id` on the same page): 0**

Every `href="#xxx"` resolves to a corresponding `id="xxx"` on the same page. Sticky TOC ("story-toc") on the Wave-3 pages is fully wired.

### Cross-page anchors

- `href="/impetus/ai-photoshoot#section-04"` — referenced from 4 places (impetus index, plus 3 photoshoot case-study breadcrumbs). Target `id="section-04"` exists in `impetus/ai-photoshoot/index.html`. **Resolves.**
- `href="/jcp#autri"` — found only in `docs/impetus-index-backup-2026-04-30.html`. Anchor `id="autri"` does **NOT** exist in `jcp/index.html`. Low severity (backup file only, not linked from any live page).

---

## Redirected routes audit

| Old path | Live HTML route refs | Asset path refs (legitimate) |
|---|---|---|
| `/jcp/rcpl/` (HTML route) | **0** ✓ | n/a |
| `/assets/jcp/rcpl/*.jpg` (asset path) | n/a | 9 image refs, all from `rcpl/index.html`, all 9 image files exist under `assets/jcp/rcpl/` ✓ |

Note · the `assets/jcp/rcpl/` image directory is unrelated to the deprecated HTML route. Legacy asset path; everything resolves. Optional cleanup: `git mv assets/jcp/rcpl assets/rcpl` and update the 9 `<img>` srcs in `rcpl/index.html`. Not blocking.

Other deprecated paths:
- `/catalog`, `/numbers`, `/rbl`, `/impetus/videos` — only in `docs/impetus-index-backup-2026-04-30.html`. Backup file is not linked from any live page.

---

## Receipts deep-check (Wave 3 pages)

| Page | Receipts asset links | All resolve? |
|---|---|---|
| `fynd-konnect` | 4 PDF/JPG + 2 internal page links (`/jcp`, `/`) | yes (6/6) |
| `boltic` | 6 screen JPGs + 3 internal (`/agents`, `/ai-native`, `/`) | yes (9/9) |
| `autri` | 2 docs (md+json) + 4 assets + 2 internal | yes (8/8) |
| `forge` | 2 doc folders + 1 audit json + 3 PDFs + 1 JPG + 1 xlsx + 2 internal (`/dark-factory`, `/`) | yes (10/10) |
| `samarth` | 3 PDFs + 1 spec md + 2 audit jsons + 1 internal (`/organisation/`) | yes (7/7) |

**Total · 40/40 Receipts links resolve.**

Full asset sweep across all 75 pages: **72/72 unique `/assets/`, `/docs/`, `/images/`, `/data/` references resolve on disk. 0 missing.**

---

## Live preview HTTP checks

| Route | Status |
|---|---|
| `/` | 200 |
| `/jcp/` | 200 |
| `/rcpl/` | 200 |
| `/fynd-konnect/` | 200 |
| `/boltic/` | 200 |
| `/autri/` | 200 |
| `/forge/` | 200 |
| `/samarth/` | 200 |
| `/organisation/` | 200 |
| `/culture/` | 200 |
| `/granary/research/` | **404** ← C1 |
| `/impetus/photoshoots/` | 200 (Python directory listing — will 404 on Vercel; see C2) |
| `/catalog`, `/numbers`, `/rbl` (only-in-backup) | 404 (expected, no live refs) |

---

## Chrome consistency

| Tool | Result |
|---|---|
| `python3 tools/inject_chrome.py --check` | **clean** · 0 patched, 72 unchanged, 0 no-nav |
| `python3 tools/inject_present.py --check` | **clean** · 0 patched, 71 unchanged, 1 no-style-link, 0 no-slides |
| `python3 tools/inject_path_to_l4.py --check` | **clean** · 0 patched, 12 unchanged |

No drift. Topnav, footer, presentation chrome, and L4-path chrome are all canonical across every page they're meant to be on.

---

## External links (sanity)

- 162 unique external URLs, all `https://` (zero plain HTTP).
- High-traffic destinations spot-checked: linkedin.com, github.com, fynd.com, ril.com, jiomart.com, reliancedms.com — all on current canonical domains.
- No obviously stale subdomains. No action.

---

## Recommendations (ordered by impact)

1. **C1 — Fix `/granary/research/` 404.** Either ship a stub page or drop it from `tools/site_chrome.py` `SUB_NAVS["granary"]` and re-inject. (~15 min either way.)
2. **C2 — Fix `/impetus/photoshoots/` 404 in production.** This is silent — works locally on Python SimpleHTTP, will 404 on Vercel. Ship `impetus/photoshoots/index.html` as a 4-case-study index (recommended) or remove the chip from `SUB_NAVS["impetus"]`.
3. **L1/L2 — Archive the backup.** Move `docs/impetus-index-backup-2026-04-30.html` to `docs/_archive/` so future audits don't pick up dead refs (`/catalog`, `/numbers`, `/rbl`, `/impetus/videos`, `/jcp#autri`).
4. **Optional cleanup — Move `assets/jcp/rcpl/` → `assets/rcpl/`.** Currently the 9 RCPL screenshots still live under the old `assets/jcp/rcpl/` path. Not broken (all 9 files resolve), but the on-disk path still encodes the deprecated parent route. Update the 9 `<img>` srcs in `rcpl/index.html` after the move.
5. **No further action needed** on anchors, mega-menu coverage, Wave-3 Receipts, asset hygiene, chrome consistency, or external links.
