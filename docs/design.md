# Design System · Fynd × Reliance Retail register

The visual register for `https://reliance-retail-fynd.vercel.app`. Audience: **RIL Apex leadership**. Personality: **engineered, precise, quiet-confident** — closer to a typeset technical report than a SaaS landing page.

This document is the single source of truth for visual conventions. It captures **what we follow today** (extracted from `style.css` and observed page conventions) and **what we should converge to** (the deltas that need to be applied in a sweep). Implementation-side, almost all changes live in one file: `style.css`. Per-page inline-style overrides are called out where they exist.

Pairs with:
- `.claude/skills/website-tone-of-voice.md` — copy register
- `.ai/codebase-map.md` — folder structure and lifecycle
- `CLAUDE.md` — workflow rules

---

## Table of contents

1. [Foundations](#foundations)
   - [1.1 Color](#11-color)
   - [1.2 Typography](#12-typography)
   - [1.3 Spacing](#13-spacing)
   - [1.4 Border radius](#14-border-radius)
   - [1.5 Borders & dividers](#15-borders--dividers)
   - [1.6 Shadows & elevation](#16-shadows--elevation)
2. [Components](#components)
   - [2.1 Cards](#21-cards)
   - [2.2 Pills (status & labels)](#22-pills-status--labels)
   - [2.3 Buttons](#23-buttons)
   - [2.4 Tables](#24-tables)
   - [2.5 Top navigation & mega-menu](#25-top-navigation--mega-menu)
   - [2.6 Per-track subnav](#26-per-track-subnav)
   - [2.7 Crumbs](#27-crumbs)
   - [2.8 Section labels](#28-section-labels)
   - [2.9 Stat tiles](#29-stat-tiles)
   - [2.10 Lightbox (image gallery)](#210-lightbox-image-gallery)
3. [Page anatomy](#page-anatomy)
4. [Motion](#motion)
5. [Accessibility](#accessibility)
6. [Code conventions](#code-conventions)
7. [The sweep · what to change](#the-sweep--what-to-change)
8. [Don't / Do quick reference](#dont--do-quick-reference)

---

## Foundations

### 1.1 Color

Light theme only — never build dark. Tokens live in `style.css:1-14`.

#### Ink (text)

| Token | Hex | Contrast on white | Usage |
|---|---|---|---|
| `--ink` | `#0A0A0A` | 19.5:1 | Primary text. Headings, body, active nav, button labels on white. |
| `--ink-muted` | `#6B7280` | 4.83:1 | Captions, breadcrumb text, table headers, section labels. **Borderline AA at 11px mono — see §1.2 target.** |
| `--ink-soft` | `#9CA3AF` | 2.85:1 | Decorative dividers, separator dots in crumbs. **Decorative-only.** Never use for text that conveys meaning. |

#### Surface

| Token | Hex | Usage |
|---|---|---|
| `--bg` | `#FFFFFF` | Default page background. |
| `--bg-soft` | `#FAFAFA` | Subtle surface for table headers, hover states, raised panels. |

#### Borders

| Token | Hex | Usage |
|---|---|---|
| `--border` | `#E5E5E5` | Card outlines, dividers, default borders. **Target: darken to `#D4D4D4`** (already done for `.subnav-link`). |
| `--border-soft` | `#F0F0F0` | Inner separators on stat tiles, very-low-contrast splits. |

#### Accent (use sparingly)

| Token | Hex | Usage |
|---|---|---|
| `--accent` | `#6B5BD6` | Active nav indicator, link hover, pill-accent. Single accent across the site. |
| `--accent-soft` | `#EDE9FE` | Background of `.pill-accent`. |

#### Status semantics

Used in pills, dots, and inline status text. Never use color alone — always pair with a label.

| Token | Hex | Used in |
|---|---|---|
| `--green` | `#16A34A` | `pill-live`, status dots |
| `--amber` | `#D97706` | status dots only |
| `--red` | `#DC2626` | `pill-red`, status dots |

Pill background/text/border colors are hand-tuned per status — see §2.2.

#### Color rules

- **Never introduce a new hex.** Use an existing token. If the design needs a new color, add it to `:root` first and document it here.
- **Do not use color alone** to convey status. Pair with a text label (e.g. `pill-live` always reads "Live", not just a green dot).
- **Decorative grayscale only:** `--ink-soft` is for visual ornament, not for any text the reader needs to parse.

---

### 1.2 Typography

#### Font stack

| Family | Used for |
|---|---|
| **Inter** (400, 500, 600, 700, 800, 900) | All body, display, button, nav, table cell text. |
| **JetBrains Mono** (400, 500, 600) | Captions, eyebrows, breadcrumbs, table headers, section labels, pill text, stat-tile units. The "engineered" signal of the site. |

Loaded from Google Fonts in every page `<head>`. Antialiased + `text-rendering: optimizeLegibility` set on `body`.

#### Display tier (Inter)

| Class | Computed | Letter-spacing | Line-height | Usage |
|---|---|---|---|---|
| `.display` | (sized inline; usually 64-96px) | -0.04em | 1.0 | Page H1. |
| `.display-2` | (sized inline; usually 36-48px) | -0.03em | 1.05 | Section H2. |

#### Body & utility scale

Body is browser default (16px Inter). Utility sizes used in components:

| Px | Family | Usage today | Target |
|---|---|---|---|
| 18 | Inter 700 | H3 (lens-card titles) | Keep |
| 16 | Inter 400 | Body text, table cells | Keep |
| 15 | Inter 700 | Platform-card name | Keep |
| 14 | Inter 500 | Buttons | **Bump to 15px** (see Sweep §7) |
| 13 | Inter 500 | Nav links, mega-link, body of cards | Keep |
| 11 | Mono 500 | Section labels, crumbs, subnav, table th, cap-num, nav-version | **Bump to 12px** |
| 10 | Mono 500 | Pills, mega-link suffix, mega-col-label | **Bump to 11px** |

**Why the bump:** mono fonts at 10-11px on white are below the comfortable reading threshold. JetBrains Mono renders cleanly at 12px and the page reads ~10% lighter on the eyes without changing layout or character.

#### Font weights

| Weight | Used for |
|---|---|
| 400 | Body paragraphs |
| 500 | Nav, mega-link, pill text, table headers, buttons |
| 600 | Mono labels (sometimes); inline `<strong>` |
| 700 | H3, platform-card name, table emphasis numbers |
| 800-900 | `.num-display` (large metric tiles, hero numbers) |

#### Line-height

- Body: browser default (~1.5) — **target: lock to 1.55 explicitly** in `body { }`
- Display 1: 1.0
- Display 2: 1.05
- H3: ~1.3
- Card body / `.lens-bullet`: 1.5-1.55
- Caption (mono): 1.0-1.2 (tight)

#### Caption color

Captions in `--ink-muted` (#6B7280). At 11px mono on white this is 4.83:1 — borderline AA. **Target: darken caption color to `#4B5563` (7.6:1)** for `.section-label`, `.crumb`, `.cap-num`, `.mega-col-label`, table headers.

---

### 1.3 Spacing

Tailwind's default 4px scale, used via utility classes (`mt-2`, `gap-3`, `py-32`, etc.). Common values seen in the codebase:

| Tailwind | px | Usage |
|---|---|---|
| `1` | 4 | Inline icon-text gap, status-dot offset |
| `2` | 8 | Standard inline gap, pill internal gap |
| `3` | 12 | Card grid gap, button icon gap, badges row |
| `4` | 16 | Card padding, section spacing |
| `5` | 20 | Card padding (medium) |
| `6` | 24 | Card padding (large), grid gap on mid-density grids |
| `8` | 32 | Card padding (lens-card), section internal padding |
| `12` | 48 | Inter-section vertical rhythm |
| `16` | 64 | Major section breaks |
| `24` | 96 | Hero top/bottom (`pt-24` `pb-24`) |
| `32` | 128 | Hero on large pages (`pt-32 pb-32`) |

**Rules:**
- Stay on the 4/8 rhythm. No `13px`, no `18px` paddings.
- Section-to-section vertical rhythm should be one of: 48 / 64 / 96 / 128.
- Inside a card, padding is one of: 16 (`p-4`), 20 (`p-5`), 24 (`p-6`), 32 (`p-8`). Pick one per card type and stay with it.

---

### 1.4 Border radius

| Value | Where |
|---|---|
| `4px` | `.pill` (status chips) |
| `8px` | `.nav-link` background, `.mega-link` background, hover surfaces |
| `12px` | `.card` (default), tables containers |
| `14px` | `.nav-mega-panel`, `.platform-card` |
| `20px` | `.lens-card` (3-column lens layout) |
| `999px` | `.btn-primary`, `.btn-secondary`, `.subnav-link`, `.nav-version`, filter chips |

**Rules:**
- New cards default to `12px` unless they sit inside a hero or use the lens-card pattern.
- Pills are `999px` (full); status chips are `4px`.
- Don't introduce intermediate values (`6`, `10`, `16`).

---

### 1.5 Borders & dividers

- **Default border:** `1px solid var(--border)` (currently #E5E5E5). **Target: `#D4D4D4`.**
- **Inner separators inside dense components** (e.g. between rows of stat-tile groups): `1px solid var(--border-soft)` (#F0F0F0).
- **Strong divider** (under section headers, footer top): `1px solid var(--ink)` is acceptable on table-header bottoms only.
- **Hover:** border transitions to `var(--ink)` over 150ms. This is the primary hover affordance for cards (no shadow, no lift unless explicitly designed).

---

### 1.6 Shadows & elevation

The site is intentionally flat. Shadows are reserved for **floating panels only**:

| Where | Shadow |
|---|---|
| `.nav-mega-panel` (open mega menu) | `0 16px 48px rgba(10,10,10,0.08), 0 2px 8px rgba(10,10,10,0.04)` |
| `.card-hover` on hover | `0 1px 3px rgba(0,0,0,0.05)` (very subtle) |
| Lightbox overlay | inherited from lightbox markup |

**Rules:**
- Cards do not lift on hover (no `translate`, no big shadow). The border color change is the affordance.
- Two exceptions: `.lens-card` and `.platform-card` lift `translateY(-2px)` on hover. Don't add this elsewhere.
- Never introduce a shadow palette beyond what's listed above. If a new pattern needs depth, use border darkening or `--bg-soft` background instead.

---

## Components

### 2.1 Cards

Defined in `style.css:41-50`. The default card is white-on-white with a subtle border and a hover border-darken.

```html
<div class="card p-6">
  ...
</div>

<!-- with hover affordance (clickable cards / links) -->
<a href="..." class="card card-hover p-6 block">
  ...
</a>
```

**Specs:**
- Background: white
- Border: `1px solid var(--border)`
- Radius: `12px` (`.card`)
- Padding: pick one per card type — `p-4` / `p-5` / `p-6` / `p-8`. Stay consistent within a section.
- Transition: `border-color 0.15s, box-shadow 0.15s`

**Variants in use:**

| Class | Padding | Notes |
|---|---|---|
| `.card p-4` | 16 | Tight info card (release-notes row) |
| `.card p-5` | 20 | Default content card |
| `.card p-6` | 24 | Spacious card with multiple regions |
| `.card p-8` | 32 | Hero-adjacent feature card |
| `.lens-card` | 32 | 3-column "lens" layout · radius 20px · `translateY(-2px)` on hover |
| `.platform-card` | 20 | Home-page platform grid · radius 14px · `translateY(-2px)` on hover |

**Card hover rule:**
- `.card-hover:hover` → border becomes `var(--ink)` + `0 1px 3px rgba(0,0,0,0.05)` shadow
- This is the **only** acceptable hover affordance for standard cards.

---

### 2.2 Pills (status & labels)

Defined in `style.css:98-118`. All pills are 4px-radius rectangles, mono uppercase, monochrome by default.

```html
<span class="pill">Default</span>
<span class="pill pill-live">Live</span>
<span class="pill pill-pilot">Pilot</span>
<span class="pill pill-build">Build</span>
<span class="pill pill-phase2">Phase 2</span>
<span class="pill pill-accent">Accent</span>
<span class="pill pill-red">Critical</span>
```

**Specs (current):**
- Font: JetBrains Mono 500, **10px** (target: 11px), uppercase, letter-spacing 0.04em
- Padding: `4px 8px`
- Radius: 4px
- Border + bg + text colored per status

**Variant palette:**

| Class | bg | text | border |
|---|---|---|---|
| `.pill` (default) | `--bg-soft` | `--ink-muted` | `--border` |
| `.pill-live` | `#ECFDF5` | `#047857` | `#A7F3D0` |
| `.pill-pilot` | `#FFF7ED` | `#C2410C` | `#FED7AA` |
| `.pill-build` | `#FFFBEB` | `#B45309` | `#FDE68A` |
| `.pill-phase2` | `#F3F4F6` | `--ink-muted` | `#D1D5DB` |
| `.pill-accent` | `--accent-soft` | `--accent` | `#DDD6FE` |
| `.pill-red` | `#FEF2F2` | `#B91C1C` | `#FECACA` |

**Rules:**
- Don't add new pill variants without adding them here.
- Pill text is always uppercase. If a status has a long name, shorten it (`Build` not `In Build`).

---

### 2.3 Buttons

Defined in `style.css:52-78`. Two variants only: primary (filled ink) and secondary (outline).

```html
<a class="btn-primary">Primary action →</a>
<a class="btn-secondary">Secondary action</a>
```

**Specs:**
- Font: Inter 500, **14px** (target: 15px)
- Padding: `12px 22px` (target: `13px 24px`)
- Radius: 999px (full pill)
- Gap between icon and label: 8px
- Transition: `opacity 0.15s` (primary) or `border-color 0.15s` (secondary)

**Hierarchy rule:** one primary CTA per section. Use `.btn-secondary` for secondary actions.

**Don't** create new button variants. If you need a "ghost" or "destructive" button, document it here first.

---

### 2.4 Tables

Defined in `style.css:80-96`. The table is the workhorse of the deep-dive sections.

```html
<table class="grid-table">
  <thead>
    <tr>
      <th>Metric</th>
      <th>Value</th>
      <th>Finding</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Revenue per search</td>
      <td>₹92.13 → ₹98.77 · <strong>+7.39%</strong></td>
      <td>+9% avg across verticals</td>
    </tr>
  </tbody>
</table>
```

**Specs:**
- Width: 100%, `border-collapse: collapse`
- Cell padding: `18px 20px`
- Cell border-bottom: `1px solid var(--border)`
- Header: JetBrains Mono 500 **11px** (target: 12px), uppercase, `letter-spacing: 0.04em`, color `--ink-muted` (target: #4B5563), bg `--bg-soft`, bottom border `1px solid var(--ink)`

**Rules:**
- Always wrap a comparison table in `class="grid-table"` — never style ad-hoc.
- Numbers: emphasize deltas with `<strong>` (Inter 700) inline. Don't bold the entire cell.
- For dense numerical tables, use `font-variant-numeric: tabular-nums` on cells (target: add `.tabular` utility class).

---

### 2.5 Top navigation & mega-menu

Defined in `style.css:127-220`. Generated by `tools/site_chrome.py`. **Never edit nav HTML directly — see CLAUDE.md "Nav + footer · canonical-source rule".**

**Specs:**
- `nav.topnav`: sticky, blurred (`backdrop-filter: blur(14px)`), bg `rgba(255,255,255,0.92)`, bottom border
- `.nav-link`: Inter 500 13px, padding `8px 14px`, radius 8px, hover bg `--bg-soft` + color `--accent`
- Active nav: `--accent` color + 2px underline at the bottom of the link
- `.nav-mega-panel`: floating dropdown, radius 14px, padding 18px, shadow as listed in §1.6, transition 180ms opacity + transform
- Invisible 12px hover-bridge between trigger and panel — see comment at `style.css:158`
- `.mega-link`: Inter 500 13px; suffix `.mono-suffix` is **10px mono** (target: 11px) `--ink-muted`
- `.mega-col-label`: 10px mono uppercase (target: 11px)

**Rules:**
- All nav changes go through `tools/site_chrome.py` then `python tools/inject_chrome.py`.
- Don't add a third level of menu (nested mega-menu).
- Each mega-menu column has a `.mega-col-label` heading.

---

### 2.6 Per-track subnav

Defined in `style.css:244-256`. Pill-strip below crumbs on multi-page tracks (jcp, impetus, granary, pixelbin, rcpl).

```html
<div class="flex flex-wrap gap-2 mb-8">
  <a href="/jcp" class="subnav-link active">Overview</a>
  <a href="/jcp/channels" class="subnav-link">Channels</a>
  ...
</div>
```

Generated by `site_chrome.subnav_html()` and injected by `tools/inject_subnavs.py`.

**Specs (current, post-affordance fix):**
- Font: JetBrains Mono **11px** (target: 12px), uppercase, `letter-spacing: 0.04em`
- Padding: `8px 14px`
- Radius: 999px (full pill)
- Default: text `--ink`, border `#D4D4D4`, bg white
- Hover: border `--ink`, bg `--bg-soft`
- Active: bg `--ink`, text white, border `--ink`

**Rules:**
- Always use `subnav_html()` to render. Never hand-author pill links.
- One pill is `.active` per page (the current route).

---

### 2.7 Crumbs

Defined in `style.css:228-240`. Inline mono breadcrumb under the topnav.

```html
<div class="crumb"><a href="/">Home</a> <span class="sep">/</span> JCP</div>
```

**Specs:**
- Font: JetBrains Mono **11px** (target: 12px), uppercase, `letter-spacing: 0.04em`, color `--ink-muted` (target: #4B5563)
- Anchor color: `--ink-muted`; hover `--ink`
- Separator (`<span class="sep">`): `--ink-soft`

**Target tweaks (a11y sweep):**
- Pad anchors to a 24px+ tap height: add `padding: 4px 6px; margin: 0 -6px;` so layout doesn't shift
- Add `:focus-visible` ring (see §5)

---

### 2.8 Section labels

Defined in `style.css:28-36`. Every numbered section opens with `<div class="section-label">01 · WHAT'S LIVE</div>`.

**Specs:**
- Font: JetBrains Mono 500 **11px** (target: 12px), uppercase, `letter-spacing: 0.05em`
- Color: `--ink-muted` (target: #4B5563)
- Prefix: `§ ` (in `--ink-soft`) injected via `::before`

**Rules:**
- Section labels are a **contiguous run** (`01`, `02`, `03`…). No skips. Verify before commit:
  ```bash
  grep -n 'section-label mb-3">[0-9]' <route>/index.html
  ```

---

### 2.9 Stat tiles

Pattern, not a class — used in hero stat strips and inline metric tiles.

```html
<div>
  <div class="cap-num">Orders / day</div>
  <div class="text-3xl font-bold">700K+</div>
</div>
```

**Specs:**
- Label: `.cap-num` → JetBrains Mono **11px** (target: 12px), `--ink-muted` (target: #4B5563)
- Number: Inter 700-800, sized via Tailwind utility (`text-2xl`, `text-3xl`, `text-4xl`) or inline 32-72px. Use `tabular-nums` if the number animates.

**Rules:**
- Numbers always carry a unit qualifier in the caption (`/ day`, `· peak`, `· FY26`).
- Approximations carry `~` (`~50` not `50`).
- Indian large numbers in `L` and `Cr` (`200 Cr`, never `2,000,000,000`).

---

### 2.10 Lightbox (image gallery)

Convention only — not a CSS class. Wrap image elements that should open full-screen in `<a class="js-lightbox">`. Add the lightbox CSS + script block once per page above `</body>`.

```html
<a href="/assets/<route>/<file>.jpg" class="js-lightbox">
  <img src="/assets/<route>/<file>.jpg" alt="..." />
</a>
```

**Rules:**
- If a page has zero `<img>` to bind, **strip the lightbox infrastructure** — no dead JS.
- Lightbox source: see existing implementations in `impetus/photoshoots/index.html` or `impetus/brands/index.html`.

---

### 2.11 Section hero split (number + body)

Two-column layout that pairs a giant display number with a body paragraph. Used on the home page for the §02–§09 storyline section heroes (per `docs/home-redesign-spec.md` Move B). Promote to `style.css` as `.section-hero-split` if any other page adopts the pattern; until then, page-level `<style>` is acceptable.

```html
<div class="section-hero-split">
  <div>
    <div class="num-display section-hero-num">11 stores</div>
    <div class="section-hero-cap">Mumbai pilot · MAPE 41 %</div>
  </div>
  <div>
    <p class="text-base">Body paragraph wraps right of the hero number…</p>
  </div>
</div>
```

**Specs:**
- Layout: CSS Grid · `grid-template-columns: auto 1fr` · `gap: 56px` · `align-items: start`
- Hero number: `.num-display` + `.section-hero-num` · Inter 800 · `font-size: clamp(56px, 6vw, 96px)` · `white-space: nowrap` · `tabular-nums` (inherited from `.num-display`)
- Caption under the number: `.section-hero-cap` · 13 px JetBrains Mono · `var(--caption)` · letter-spacing 0.04em · uppercase
- Mobile (`max-width: 768px`): single column · `grid-template-columns: 1fr` · `gap: 16px` · hero number drops to a fixed `56 px`

**Rules — the load-bearing one:**
- **Hero column MUST auto-size to its content** (`auto 1fr`), NOT a fixed-width column. Multi-word display numbers like `11 stores` or `7 days` overflow visually into the body column when the hero column is constrained to a fixed width AND `white-space: nowrap` is set. The auto column expands to fit the actual content; short heroes (`88 %`, `100+`) keep a narrow column, long heroes get the room they need. (Worked example: home v1 used `minmax(0, 280px) 1fr` + `nowrap` → §05 GRANARY's `11 stores` overflowed into the body paragraph at 1280 px viewport. Fixed by switching to `auto 1fr` + lowering the font-size cap from 128 px → 96 px.)
- **Cap the upper bound at `96 px`.** Even with `auto 1fr`, a runaway display number at 128 px crowds the body column too aggressively at common laptop viewports. The `clamp(56px, 6vw, 96px)` keeps the hero impressive without dominating.
- **Keep `white-space: nowrap`** on the hero number. Multi-token heroes (`7 days`, `11 stores`, `380 M+`, `15.08 Cr`, `Phase 1`) must render on a single line; without `nowrap` the digit and the unit can split across lines (visibly broken in v1 of the home page on `7 days`).
- **Hero number stays a number, not a phrase.** The display slot is for a single noun-phrase scale anchor (`100+ brands`, `400 M+ identities`, `7 days`). Don't put a sentence in there — that's body copy. (Worked example: home v1 used `Phase 1` as the §05 GRANARY hero — read as too phase-centric per the page-owner; swapped for `11 stores` so the slot carries a real, defensible scale.)

---

## Page anatomy

Every register page follows the same skeleton:

```
┌─ <nav class="topnav"> ─────────────────────────────────┐  ← canonical, from site_chrome.py
├─ <div class="crumb"> Home / Track ───────────────────  ─┤
├─ subnav_html() pill strip (multi-page tracks only) ─── ─┤
├─ <section class="hero-grad"> ─────────────────────────  ┤
│   <div class="section-label">TRACK 01 · …</div>          │
│   <h1 class="display">Page Title.</h1>                   │
│   <p>Hero subhead (≤30 words)</p>                        │
│   stat strip / lead numbers                              │
├─ §01 Status                                              │
├─ §02 What's live                                         │
├─ §03 Architecture                                        │
├─ §04 Deep dive                                           │
├─ §05 In flight                                           │
├─ §06 Vision / Roadmap                                    │
├─ §07 Research                                            │
└─ <footer> © YYYY RRVL · JPL · Fynd · Internal only ───  ┘
```

**Section ordering** is canonical — overrides documented in each `docs/<route>-spec.md` §9.

**Hero specs:**
- Top padding: 96-128px (`pt-24` to `pt-32`)
- Optional `hero-grad` background: radial gradient of `--accent` at 8% opacity (page-level inline `<style>`)
- H1 always carries the `.display` class
- Period at end of H1 is intentional ("Jio Commerce Platform.")

**Page-level inline `<style>`** is acceptable for one-off layouts (lens-card, num-display, hero-grad) but new patterns that recur should be promoted to `style.css`.

---

## Motion

All transitions are short, monochrome, and serve affordance — never decoration.

| Where | Property | Duration | Easing |
|---|---|---|---|
| Card hover | `border-color, box-shadow` | 150ms | default |
| Button hover | `opacity, border-color` | 150ms | default |
| Subnav-link hover | `all` | 150ms | default |
| Mega-menu open | `opacity, transform, visibility` | 180ms | default |
| Nav-link hover | `background, color` | 150ms | default |
| Mega-menu chevron rotate | `transform` | 150ms | default |
| Lens-card / platform-card hover | `transform, border-color` | 200ms | default |

**Rules:**
- Animate `transform` and `opacity` only. Never animate `width`, `height`, `top`, `left`, `margin`, `padding`.
- Keep durations 150-300ms. The mega-menu's 180ms is the upper bound for chrome.
- No bounce / elastic / overshoot. The register is "engineered, precise" — physics curves break that.
- **Target: add `prefers-reduced-motion` reset** that zeros all animations and transitions site-wide. Currently missing.

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    transition-duration: 0.01ms !important;
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
  }
}
```

---

## Accessibility

Target: **WCAG 2.2 AA · respect `prefers-reduced-motion`**.

### Color contrast (audit results)

| Pair | Ratio | Status |
|---|---|---|
| `--ink` on white | 19.5:1 | AAA |
| `--ink-muted` (#6B7280) on white at 16px | 4.83:1 | AA |
| `--ink-muted` on white at 11px mono | 4.83:1 | **Borderline AA** — bump caption color to `#4B5563` (7.6:1) |
| `--ink-soft` on white | 2.85:1 | Decorative-only — never use for text |
| `--accent` on white | 4.41:1 | AA at 14px+ |
| Pill text on pill bg | varies | All current pills meet AA |

### Focus

**Currently missing on most interactive elements.** Target: add a single global rule:

```css
:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
  border-radius: 4px;
}
```

Components that already have a hover affordance (cards, pills) still need a focus ring for keyboard users.

### Touch targets

| Element | Current | Target |
|---|---|---|
| Nav links | 32-36px tall | OK |
| Subnav pills | ~32px tall | OK |
| Buttons | ~44px tall | OK |
| Crumb anchors | **17px tall** | **Pad to 24px+ tap area** |
| Pill links (when interactive) | ~22px tall | Pad to 24px+ if used as link |

### Icons & labels

- Icon-only links / buttons must have `aria-label`. Current site has none — audit and add.
- Status pills always carry text — never color-only.
- Mega-menu trigger uses an SVG chevron + visible label ("Tracks ▾") — fine.

### Other

- All images have `alt` text per spec — verified.
- Tables use `<th>` for headers — `grid-table` enforces this.
- Section labels are not headings (intentionally `<div>`); H1/H2/H3 hierarchy is contiguous within each page.

---

## Code conventions

### File map

| File | Owns |
|---|---|
| `style.css` | All shared styles, tokens, components. **Single source of truth — edit here for any change that affects more than one page.** |
| `tools/site_chrome.py` | Topnav HTML, footer HTML, mega-menu data, subnav data. **Never edit nav/footer HTML in pages directly.** |
| `tools/inject_chrome.py` | Sweep tool to apply `site_chrome.py` changes across ~70 pages. Run after every `site_chrome.py` edit. |
| Per-page `<style>` block | One-off layout (lens-card, num-display, hero-grad). Promote to `style.css` if it recurs. |
| Tailwind via CDN | Utility classes for spacing, grid, flex, type-size shortcuts. |

### When to edit which file

| Goal | Edit |
|---|---|
| Adjust a token (color, radius, font size) site-wide | `style.css` `:root` block |
| Tune a component (card, pill, button, table) | `style.css` component block |
| Add or rename a nav item | `tools/site_chrome.py` → run `python tools/inject_chrome.py` |
| Add a new track subnav | `tools/site_chrome.py` `SUBNAV` dict → run `python tools/inject_subnavs.py` |
| Page-only one-off styling | Inline `<style>` in that page's `<head>` |
| Static class in a single component | Page-level utility classes (Tailwind) |

### Verification commands

```bash
# Check nav/footer hasn't drifted from canonical
python tools/inject_chrome.py --check

# Find every page using a class
grep -rl 'class="<class-name>' --include='*.html' .

# Section labels contiguous
grep -n 'section-label mb-3">[0-9]' <route>/index.html
```

---

## The sweep · what to change

These are the deltas to apply in one pass to converge the codebase to this spec. All but #6 are **single-file edits to `style.css`** that propagate to all 16 (subnav-using) / ~70 (nav-using) pages.

### Tier 1 · Readability (apply first)

| # | Change | File | Lines |
|---|---|---|---|
| 1 | Bump 11px mono → **12px** | `style.css` | `.section-label`, `.crumb`, `.subnav-link`, `.cap-num`, `table.grid-table th`, `.nav-version`, `.mega-col-label` |
| 2 | Bump 10px mono → **11px** | `style.css` | `.pill`, `.mega-link .mono-suffix` |
| 3 | Darken caption color from `--ink-muted` to `#4B5563` | `style.css` | `.section-label`, `.crumb`, `.cap-num`, `table.grid-table th`, `.mega-col-label` |
| 4 | Darken `--border` token from `#E5E5E5` → `#D4D4D4` | `style.css:7` | one-line token change cascades to cards, tables, mega-panel, pills |

Net visual effect: page reads ~10% lighter on the eyes, no layout shift, no character change.

### Tier 2 · Body & buttons

| # | Change | File |
|---|---|---|
| 5 | Lock body line-height: add `body { line-height: 1.55 }` | `style.css` |
| 6 | Add `.prose { max-width: 70ch }` for long-form paragraph blocks; apply on copy-heavy pages | `style.css` + page edits |
| 7 | Bump button text 14 → 15px, padding `12px 22px` → `13px 24px` | `style.css` `.btn-primary`, `.btn-secondary` |

### Tier 3 · A11y delta

| # | Change | File |
|---|---|---|
| 8 | Global `:focus-visible` ring with `--accent` outline | `style.css` |
| 9 | Crumb anchor tap-area padding (`4px 6px / -mx 6px`) | `style.css` `.crumb a` |
| 10 | `prefers-reduced-motion` reset (zero all transitions/animations) | `style.css` |
| 11 | Add `aria-label` to all icon-only links/buttons | per page (audit grep) |

### Tier 4 · Bigger calls (ask first)

| # | Change | Why |
|---|---|---|
| 12 | Add typed scale tokens (`--text-xs / sm / base / md / lg / xl`) and replace literals | One-line future tuning |
| 13 | Add `.tabular` utility (`font-variant-numeric: tabular-nums`) for stat tiles + tables | Number alignment |
| 14 | Decide whether to keep `.lens-card` and `.platform-card` `translateY(-2px)` hover or remove for stricter flatness | Editorial vs interactive register call |

---

## Don't / Do quick reference

### Don't

- **Don't** introduce a new hex value. Use a token from `:root`.
- **Don't** edit `<nav>` or `<footer>` HTML in any page. Edit `tools/site_chrome.py` and run `inject_chrome.py`.
- **Don't** use `--ink-soft` for any text the reader needs to parse.
- **Don't** create a new pill variant without adding it to §2.2 and `style.css`.
- **Don't** use mono at less than 11px (target: 12px). Tiny mono on white is the dominant readability tax.
- **Don't** add card hover lift / shadow beyond what §1.6 documents.
- **Don't** introduce non-4/8 spacing (`13px`, `18px` paddings).
- **Don't** add bounce / elastic / overshoot motion.
- **Don't** add an `aria-hidden` icon link without an `aria-label`.
- **Don't** use color alone to convey status — pair with a label.

### Do

- **Do** edit `style.css` first when a change affects more than one page.
- **Do** stay on the 4/8 spacing rhythm and the 12px/8px/4px radius family.
- **Do** verify `python tools/inject_chrome.py --check` exits 0 after any nav/footer commit.
- **Do** keep section labels a contiguous numeric run (01, 02, 03…).
- **Do** use `tabular-nums` (or the planned `.tabular` class) for any number column.
- **Do** add a focus ring to any custom interactive element.
- **Do** strip the lightbox block from pages with zero `<img>` to bind.
- **Do** put approximations as `~50` (caption side) and Indian large numbers as `200 Cr` / `40 L`.

---

## Change log

| Date | Change |
|---|---|
| 2026-05-03 | Initial document. Captures current state of `style.css` + observed conventions across 70 pages, plus the readability/a11y sweep deltas (Tier 1-4). |
