# JCP — AI Cataloging surface · Spec

**Status:** v0.1, 2026-04-30
**Owner:** Kushan Shah
**Track:** JCP (`/jcp/`)
**Inherits visual system from:** main register (post-v0.8.0 mega-menu nav)

---

## 1. Purpose

A single surface inside the JCP track that consolidates the AI Cataloging milestones and pipeline studies Fynd has shipped (or is shipping) for Reliance brands. The story is **pipeline stats + sample throughput**: hard numbers for what's gone live, what's been measured, and how attribute-level accuracy is evaluated.

Audience: same as the rest of the register — MDA / executive / RRVL apex reviewers. Read in 2-4 minutes.

---

## 2. Where it sits

```
/jcp/                          (existing — JCP track overview)
/jcp/cataloging/               NEW · single page, all content sections inline
```

- One page only — no detail/sub-routes in v1.
- Linked from `/jcp/index.html` body (a "What AI Cataloging has shipped" section, similar to the design-portfolio cross-link block on `/impetus/index.html`).
- Listed in the "Tracks" mega-menu under JCP if more cataloging sub-pages emerge later. For v1, the JCP body link is enough.

---

## 3. Visual inheritance

Strict inheritance from the main register, **post-v0.8.0**. That means:

- Top nav is the **mega-menu** form (Tracks · Numbers · Asks · Gaps · More), not the older flat nav. Hand-write the page to match `/jcp/index.html` chrome — do NOT use `tools/build_pages.py` (its `topnav()` still emits the older nav).
- `auth.js` script tag in `<head>` (matches all other gated pages).
- Same `style.css` design tokens (Inter, JetBrains Mono, ink/border/accent CSS vars).
- Same hero pattern: breadcrumb → `§ TRACK · LABEL` eyebrow → H1.
- Same inverted dark footer.

---

## 4. Page structure

The page is a **single scroll**. Each section corresponds to one entry in `data/cataloging.json`. Sections render in document order; the most-significant story should be first (in v1: Tira × Akind × Google).

### 4.1 Hero strip
- Breadcrumb: `Home › JCP › AI Cataloging`
- Eyebrow: `§ JCP · AI CATALOGING · LIVE`
- H1: "AI Cataloging."
- Lede: 1-2 sentences framing the work — *"Production catalog enrichment via Google AI + Web Grounding. Live across multiple Reliance brands; release-noted milestone is Tira × Akind × Google."*
- Counter strip (3 stat blocks, Inter 700 / large numerals):
  - `89%` accuracy vs. ground truth (Tira pilot)
  - `~95%+` time reduction (Netmeds study)
  - `75%` first-pass attribute auto-fill (Reliance Digital study)
- Note: the page surfaces release-noted milestones only. Other brands are also live but without published release notes — they're not enumerated to avoid implying a specific count.

### 4.2 Section order on the page (v1, locked)

1. **§01 · Throughput study · Netmeds** — leads with the punchiest numbers (95%+ time reduction, near-zero marginal cost).
2. **§02 · Throughput study · Reliance Digital** — second study, capacity & cost scenarios.
3. **§03 · Release milestone · Tira × Akind × Google** — the only release-noted production milestone (other brands are also live but not enumerated, per the §1 framing).
4. **§04 · Methodology · Attribute Accuracy** — full inline section, prominent at the foot of the page; the `89%` accuracy stat in the Tira section anchor-links here for the "Detailed Explanation" callout.

No team credits, no roadmap / "what's next" strip — the page only surfaces shipped or measured work.

### 4.3 Section layouts (3 kinds)

Each section dispatches its layout on `kind`:

#### Kind: `release-milestone` (e.g. Tira × Akind × Google)
- Section header: `§ NN · RELEASE MILESTONE · LIVE`
- H2: title (`Tira × Catalog Cloud × Google AI`)
- Subtitle row: brand chips + partner chip + status pill (`LIVE · IN PRODUCTION`)
- Overview paragraph
- 3 stat panels in a row:
  - **Time taken** — Tira team vs Google AI
  - **Attributes filled** — totals + fill rates (overall / mandatory / non-mandatory)
  - **Accuracy** — Google AI vs ground truth
- "Why this matters" callout card (light accent background)
- Footer: `Next phase · <description>`

#### Kind: `throughput-study` (e.g. Reliance Digital, Netmeds)
- Section header: `§ NN · THROUGHPUT STUDY · <BRAND>`
- H2: title (`Web Grounding · Reliance Digital`)
- Headline strip (1-line big text): the punchline (`35–40% faster · +50–64% throughput · 75% auto-fill`)
- Executive summary (3 bullets, large)
- Comparison table — `metric · as-is · with web grounding · impact` columns
- (Optional) Scenarios row: 2 cards side-by-side for capacity-unlock vs cost-takeout

#### Kind: `methodology` (e.g. Attribute Accuracy)
- Section header: `§ NN · METHODOLOGY`
- H2: title (`Attribute Accuracy`)
- Description paragraph
- 3 verdict cards in a row: `Exact match or similar` · `Partial Match` · `No Match` — each with its definition
- Findings panel: "Sample analysis · observations on the No Match bucket" with bullet list
- Sample calculator table — `Ground Truth · Enriched Value · Verdict · Explanation`
  - Verdict column uses status pills color-coded: green for exact, amber for partial, red for no-match

### 4.4 Footer link
- Cross-link back to `/jcp/` — "View the full JCP track →"

---

## 5. Tech stack

- **Plain HTML** hand-written at `/jcp/cataloging/index.html`.
- **No generator** in v1 — the integration team has been hand-massaging every track page to keep nav consistent, and `tools/build_pages.py` would emit the older nav. If multiple cataloging detail pages emerge later we can revisit.
- **Tailwind via CDN + style.css** (matches all other pages).
- **auth.js** in `<head>` — same client-side gate as the rest of the register.
- **No JS framework** — the page is static. Verdict color-coding is plain CSS classes; comparison tables are static markup; no fetch/JS-driven sections.

---

## 6. Data contract — `data/cataloging.json`

Hand-curated; no script in v1. The page reads it visually (page is generated FROM this data, but by hand for now — automate if it grows).

```json
{
  "generatedAt": "...",
  "note": "...",
  "sections": [
    { "id": "...", "kind": "release-milestone" | "throughput-study" | "methodology", ... }
  ]
}
```

### Per-section fields

**All:** `id`, `kind`, `title`.

**`release-milestone`** (Tira × Akind × Google in v1):
- `status`, `subtitle`, `brands[]`, `partners[]`, `phase`, `nextPhase`
- `overview` (string)
- `results.time` — `tiraTeam`, `googleAI`
- `results.attributesFilled` — `totalAttributes`, `manualByTiraTeam`, `withGoogleAI`, `overallFillRate`, `mandatoryFillRate`, `nonMandatoryFillRate`
- `results.accuracy` — `googleAI`, optional `note`
- `whyItMatters` (string)

**`throughput-study`** (Reliance Digital, Netmeds in v1):
- `brand`, `headline` (1-line punchline)
- `executiveSummary[]` (bullets)
- `comparisonTable.title` + `.footnote` + `.rows[]` — each row has `metric`, `asIs`, `withWebGrounding`, `impact`
- (Optional) `scenarios[]` — each has `id`, `label`, `tagline`, `metric`, `value`, `subValue`

**`methodology`** (Attribute Accuracy in v1):
- `description`
- `categories[]` — each has `label` + `definition`
- `findings.title` + `.items[]`
- `calculatorExamples[]` — each has `groundTruthAttribute`, `groundTruthValue`, `enrichedAttribute`, `enrichedValue`, `verdict` (`exact` | `partial` | `no-match`), `verdictLabel`, `explanation`

---

## 7. Vocabulary

**Brands** referenced by cataloging entries (separate registry from design-portfolio brands):
`tira`, `akind`, `reliance-digital`, `netmeds`. Will grow as more pilots ship.

**Partners:** `google` (Google AI / Catalog Cloud).

**Section kinds:** `release-milestone`, `throughput-study`, `methodology`.

**Verdict slugs:** `exact`, `partial`, `no-match` — color-coded green / amber / red respectively in the Attribute Accuracy calculator table.

**Status pills:** `LIVE · IN PRODUCTION` (Tira/Akind has a published release note; other live brands exist but aren't enumerated), `STUDY` (the throughput pieces).

---

## 8. Decisions resolved · Open items

### Resolved (Apr 30 review)

| # | Decision | Outcome |
|---|---|---|
| 1 | Section ordering | Throughput studies first (Netmeds → Reliance Digital), Tira milestone third, Attribute Accuracy methodology fourth. "Here's the impact" framing, not "here's what shipped". |
| 2 | Methodology placement | Full inline section, prominent. At the foot of the page so the throughput numbers read first, but the methodology gets full real estate (3 verdict cards + sample calculator table) — not a sidebar / accordion. |
| 3 | Team credits | None. Match the rest of the register; per-IP attribution lives in `/catalog/`, not on individual surfaces. |
| 4 | Roadmap / what's next | Skip. Page only shows shipped or measured work. Per-section `nextPhase` (in `data/cataloging.json`) stays for record but isn't rendered as a standalone roadmap strip. |
| 5 | Brand count in hero | Don't claim "N brands live" — other brands are live without published release notes; counter strip lists 3 measurable headline numbers instead (89% accuracy, ~95%+ time reduction, 75% auto-fill). |
| 6 | Auth | `auth.js` included, same as all other gated pages. |

### Still open

1. **Tira "Detailed Explanation" link** — points to the Attribute Accuracy methodology section on the same page (`#methodology` anchor). Self-resolved by §4.2 ordering. If a Tira-specific methodology gets published later, swap the anchor for that link.
2. **Brand-specific landing pages** — none in v1. Revisit if the page outgrows ~6-8 sections.

---

## 9. Phased plan

### Phase 1 — single-page build (1-2 hours)
- Hand-write `/jcp/cataloging/index.html` with all 4 sections from `data/cataloging.json`.
- Match `/jcp/index.html` chrome (mega-menu nav, auth.js, style.css).
- Cross-link from `/jcp/index.html` body.
- Deploy to Vercel preview.

### Phase 2 — content additions (open-ended)
- Add new throughput studies as more brand pilots run.
- Add new release milestones as more brands go live.
- Update the hero counter strip's headline numbers.

### Phase 3 (optional) — automate
- If sections grow beyond ~10 or new brand-specific pages emerge, port the page generation into `tools/build_pages.py` (and update its `topnav()` to match the v0.8.0 mega-menu first).

---

## 10. Out of scope (v1)

- Per-brand sub-pages.
- Inline charts / interactive comparisons.
- Live data pull from any production system — content is curated by hand.
- Cross-track navigation beyond a single back-link to `/jcp/`.
- Full IP-Catalog integration (`/catalog/`) — AI Cataloging is a JCP IP; the IP-Catalog page already lists every IP.
