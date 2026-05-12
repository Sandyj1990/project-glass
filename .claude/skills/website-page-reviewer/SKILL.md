---
name: website-page-reviewer
description: >
  Audit and review pages on the Fynd × Reliance Retail register at
  reliance-retail-fynd.vercel.app for source traceability, tone-of-voice
  compliance, spec compliance, visual completeness, honesty register,
  cross-page consistency, and design-system compliance. Use whenever a page has been authored or restructured
  and needs an independent quality verification before sharing with Apex.
  Also trigger when the user says "review", "audit", "check", "QA", or
  "critique" in the context of a website page or section. This skill
  produces a structured audit report with scores, severity-ranked findings,
  and actionable fix recommendations. It does NOT generate the page itself —
  it evaluates an existing page against its spec, the website-tone-of-voice
  rules, the source compilation folder, and absolute quality standards.
user_invocable: true
---

# Website Page Reviewer Skill

Independently audit a page on the Fynd × Reliance Retail register for source rigor, copy register, structural compliance, visual completeness, honesty register, and cross-page consistency. Produces a scored audit report that the page author or an automated fix pass can act on.

## Core philosophy

Authoring a page and reviewing a page require different cognitive modes. The author optimises for narrative flow and getting the right material on the page. The reviewer optimises for traceability, tone discipline, and credibility. Combining both in one pass produces neither well. **Separation ensures the reviewer has no sunk-cost bias toward the prose it's evaluating.**

The reviewer is **adversarial by design**. Its job is to find every unsourced claim, every banned word, every overclaim, every broken image, every honesty drift, every cross-page inconsistency. A page that passes this audit is genuinely ready for RIL Apex's hands.

This skill reuses the rules already encoded in `.claude/skills/website-tone-of-voice.md` rather than restating them — that file is the canonical register. Read it during Phase 5.

## Inputs

The skill requires three inputs (the first two are mandatory):

1. **The page** — HTML file. The path under the repo (e.g., `granary/index.html`).
2. **The spec** — markdown file. The page-authoring spec the page was built against (e.g., `docs/granary-spec.md`). For pages without a spec, the audit runs against default standards in `references/audit-framework.md`.
3. **Source compilation folder** — the path to the raw material the page cites (e.g., `docs/Granary project documents dump/`). Used to verify that every claim on the page is traceable to a source file. If omitted, source-traceability scoring is skipped (and flagged as a gap).

Optional inputs:
- **Audit scope** — full audit (default) or targeted (e.g., "tone only", "sources only", "visuals only").
- **Sibling pages to cross-check** — defaults to `index.html` (home) and `catalog/index.html`. Add others if the page is referenced elsewhere.
- **A live dev-server URL** for the visual phase — defaults to `http://localhost:8765/<route>` if running.

## Output

A structured audit report (markdown, in chat) plus a machine-readable JSON file written to `docs/audits/<page-slug>-audit-<YYYY-MM-DD>.json`.

```
1. AUDIT SUMMARY
   - Overall score (0-100)
   - Pass/Fail determination (threshold: 75)
   - Score breakdown by dimension
   - Top 5 critical findings
   - What the page does well (counter-balance to fix list)

2. STRUCTURAL AUDIT
   - Section-by-section spec compliance
   - Section-label contiguity (§01 → §NN, no gaps)
   - Crumb / subnav / footer present
   - Mega-menu version pill matches page version

3. SOURCE TRACEABILITY AUDIT
   - Every numbered claim mapped to a source file
   - Unsourced claims flagged
   - Numbers, dates, names matched against source compilation
   - Inline source eyebrows present under non-trivial claims (per `website-tone-of-voice` §5)
   - **No §Sources block** anywhere on the page (per `website-tone-of-voice` §3 · rule established 2026-05-02 · prior carve-outs revoked)

4. TONE-OF-VOICE AUDIT (runs the website-tone-of-voice 5 rules + banned-words check)
   - Banned constructions (Section 3 of tone-of-voice)
   - Banned vocabulary (Section 7 — adjective inflators, filler verbs, hedge words)
   - Date format compliance (DD-MMM-YYYY)
   - Number-format compliance (Indian L Cr vs Western M K)
   - Names spelled and cased correctly
   - Reliance-owned framing preserved
   - Pre-publish checklist (Section 9) row by row
   - **§Sources block · always flag for removal as CRITICAL.** Per tone-of-voice §3 (rule established 2026-05-02), Apex pages never carry a §Sources block. Provenance lives in inline source eyebrows, figure captions, and the spec. Prior "3+ external artefacts" / "reader-will-navigate" carve-outs are revoked. Any page with a §Sources section is a CRITICAL finding regardless of cite count.
   - **"X-month ROI payback" / "Implementation cost recovery" stat tiles** — flag and require a citable cost-recovery analysis or removal.
   - **Lead / DRI inside section subheads** — flag any `Lead: <Fynd-side IC name>` line in a section subhead. Page-level DRI in the footer is OK; subhead-level Fynd IC attribution is not.

5. CARD/LINK PATTERN AUDIT (new — surfaces UX-as-tone issues)
   - **One target per card** — flag any card that has both a clickable body AND a decorative `↗` linking to the same target.
   - **Dead-end fallbacks** — flag URLs that route to a homepage/search via fallback (e.g., Play Store search when `play_package_id` is missing). Either fix the URL or drop the link.
   - **Storefront URLs as text** — when the card's target is a public URL, surface the URL itself as a prominent underlined hyperlink, not as muted mono caption text.

5. HONESTY REGISTER AUDIT
   - Every claim that needs a status pill carries one (Live / Building / Roadmap / Pilot)
   - No mixing of tiers in a single sentence without tagging
   - No section overclaims relative to the source (e.g., 5/37 routes wired ≠ "Command Centre is Live")
   - Forward-looking phases without dates are flagged (per tone-of-voice §3)

6. VISUAL AUDIT
   - All images load (200 status); no broken-image icons
   - Embeds (PDFs, videos) load and render correctly
   - Section labels render as a contiguous run
   - Mobile (375px) renders without overflow
   - Console clean (only the standard Tailwind CDN dev warning is acceptable)
   - Auth gate bypass works for local verify
   - **Screenshot legibility** — for each `<img>` claiming to be a UI / admin / storefront capture, the image must be readable on its own without surrounding context. Whole PDF-page renders with bullet text bleeding into the screenshot are a fail (use `pdfimages -j` or a manual crop instead).
   - **Architecture / diagram crops** — confirm the image displays at a sensible resolution (not over-scaled in a wide container). If native is >1500px wide, the container `max-width` should be capped (~1100px) so the diagram doesn't appear soft.
   - **Accordion right-text alignment** — for `<details>`/`<summary>` blocks with 3 children, the meta text must be `margin-left: auto` and not centered between the title and the icon (3-child `space-between` puts it in the middle).
   - **Stale CDN assets** — when a versioned filename suffix (e.g., `-v2`, `-v3`) is in use, confirm the HTML points at the latest version and the prior versions are not referenced anywhere.
   - **Screenshot click-to-overlay (lightbox) convention** — every product / UI / admin `<img>` on the page must be wrapped in `<a class="js-lightbox" href="<asset>">`, AND the page must include the lightbox overlay markup + script before `</body>` (see `website-section-authoring` §6 "Image display · in-page lightbox, never new tab"). Flag any of: (a) bare `<img>` with no clickable wrapper, (b) `<a target="_blank">` wrapper without the `js-lightbox` class (opens raw asset in a new tab — breaks reading flow), (c) lightbox markup present but uses `<div hidden style="display:flex">` (UA `[hidden] { display:none }` loses to inline `display:`, box is permanently visible and clicks silently no-op). Verify with Chrome DevTools MCP: click a screenshot and confirm `document.getElementById('lightbox').style.display === 'flex'` after.

7. CROSS-PAGE CONSISTENCY AUDIT
   - Numbers used on this page also appear correctly on home page card, catalog, mega-menu suffixes
   - Names spelled identically across pages
   - Status pills on home card match the page's actual register
   - Sibling pages don't reference dropped/renamed items as if still present

8. DESIGN-SYSTEM COMPLIANCE AUDIT (mechanical, not aesthetic — see `docs/design.md`)
   - **Tokens, not hex literals.** Inline `<style>` blocks and class attributes must reference `var(--*)` tokens. Flag any hex literal that is not in the `:root` token list (`docs/design.md` §1.1) or whitelisted decorative use (architecture-diagram fills).
   - **On-scale font sizes.** Every `font-size` in inline styles and every `text-[Npx]` Tailwind arbitrary must be on the documented scale (10/11/12/13/14/15/16/18/24/32/36/48/64/72px per `docs/design.md` §1.2). Flag off-scale values (e.g., `text-[11.5px]`, `font-size: 13.5px`).
   - **Caption color target.** All mono captions (`.section-label`, `.crumb`, `.cap-num`, table `<th>`, `.mega-col-label`) should use the target caption color `#4B5563`, not the legacy `--ink-muted` (`#6B7280`). Flag legacy uses once the sweep has landed (`docs/design.md` §7 Tier 1 #3).
   - **On-scale paddings.** Padding values on cards / sections must be on the 4/8 rhythm (`p-4`, `p-5`, `p-6`, `p-8`). Flag off-rhythm paddings.
   - **Border default token.** Borders should use `var(--border)`, not random hexes like `#E5E7EB` or `#D1D5DB`. Flag direct hex border declarations.
   - **Pill, button, card variants.** Every pill / button / card on the page must match a documented variant in `docs/design.md` §2. Flag undocumented hand-styled variants.
   - **Lightbox convention.** If the page has product / UI / admin `<img>`, every such image must be wrapped in `<a class="js-lightbox">` AND the lightbox markup + script must be present before `</body>` (already covered in §6 Visual; restated here for design compliance).
   - **`prefers-reduced-motion`.** Confirm no animations or transitions ignore the global reduced-motion reset (currently being added in `docs/design.md` §7 Tier 3).
   - **`:focus-visible` rings.** Confirm interactive elements without a documented hover-only affordance (cards, pills, custom buttons) carry the global focus ring.
   - **No new visual patterns without documenting.** If the page introduces a new card / pill / hero / table style not in `docs/design.md` §2, flag as a finding — either promote it to `docs/design.md` and `style.css` or revert to a documented variant.

9. FIX LIST
   - Prioritised list of fixes (Critical / High / Medium / Low)
   - Each fix: what's wrong, where (file path : line), why it matters, how to fix it
```

## Workflow

```
Phase 1: INGEST + TIER CLASSIFICATION
├── Read the page HTML (full file; build a structural map: sections, claims, pills, images, embeds, links)
├── Read the spec markdown (extract §3 page-structure as the ground-truth diff)
├── List the source compilation folder (capture filenames + sizes; do not deep-read all yet)
├── List sibling pages (index.html, catalog/index.html, others if specified)
├── Confirm the local dev server is reachable (or note skip)
└── CLASSIFY THE PAGE INTO A TIER (see references/audit-framework.md §0):
    - Tier A · Platform / product page (apply universal checks + canonical ordering + JCP parity matrix + 11-section shape)
    - Tier B · Specialty content page (apply universal checks + flexed parity + page-specific spec)
    - Tier C · Reference / interactive page (apply universal checks ONLY; skip parity matrix)
    - Excluded-canonical · jcp / impetus / granary / ucp / agents / ai-native (apply universal checks + page's own spec; skip JCP parity scoring)
    Record the tier in the JSON output. The selected tier determines which checks fire in Phases 2 and 8.

Phase 2: STRUCTURAL AUDIT → references/audit-framework.md §1
├── Compare page sections against spec §3
├── Flag missing / extra / renamed sections
├── Check section-label contiguity: grep -n 'section-label mb-3">[0-9]' must be a contiguous run
├── Check the standard-page chrome: <nav>, crumb, subnav, footer, version pill
├── Check that the version pill in the nav matches the version in the footer
├── IF Tier A · run JCP parity matrix (audit-framework.md §1B) — 8 binary checks
├── IF Tier A · run JCP 11-section shape coverage (audit-framework.md §1C)
├── IF Tier B · run flexed parity (sticky TOC strongly recommended; KPI hero / Receipts / People optional)
├── IF Tier C · skip the parity matrix entirely (interactive surfaces don't need it)
├── Run the universal mechanical sweeps (audit-framework.md §6) regardless of tier:
│   - Em-dash count · §6.1
│   - §0 → §01 contiguity bug · §6.2
│   - Banned constructions · §6.3
│   - Banned words ("Comprehensive", "picture") · §6.4
│   - we / our voice · §6.5
│   - Exclamation marks in body · §6.6
│   - Arrow operator (→) noise in prose · §6.7
│   - Inline style density · §6.8
│   - Raw hex literals · §6.9
│   - Hero subhead word count · §6.10
└── Score: structural compliance (0-100)

Phase 3: SOURCE TRACEABILITY AUDIT → references/source-audit-protocol.md
├── For every numerical claim, named-person, date, or status statement, locate the source
├── Match against source compilation folder filenames and (where needed) file content
├── Flag any claim that cannot be traced to a source file
├── Flag any §Sources block as CRITICAL — must be removed (per tone-of-voice §3)
├── Spot-check 3-5 high-stakes claims by reading the source file directly
└── Score: source traceability (0-100)

Phase 4: TONE-OF-VOICE AUDIT → read .claude/skills/website-tone-of-voice.md (FULL — it is the rule-set)
├── Grep for banned vocabulary (Section 7 list): transformative, world-class, cutting-edge,
│   game-changing, next-generation, best-in-class, premier, robust, leverages, harnesses,
│   empowers, enables, unlocks, perhaps, could potentially, arguably, moreover, furthermore,
│   additionally, in addition, importantly, the future is now
├── Grep for banned constructions (Section 3): "Strong interest in", "has shifted the mindset",
│   "This is not X. It is Y.", "In summary", trailing summaries
├── Check date format: every visible date matches DD-MMM-YYYY (e.g., 28 - Apr - 2026)
├── Check number format: Indian numbers use L Cr, Western use M K, approximations carry ~
├── Verify Reliance entity names: case + spacing exact (RIL, RRVL, RRL, RBL, RCPL, JPL, RCP,
│   HSEF, JioMart, AJIO, Tira, Reliance Trends, Reliance Jewels, Smart Bazaar, Smart Point,
│   FreshPik)
├── Verify Fynd platform names: case + spacing exact (JCP, UCP, Impetus, Granary, PixelBin,
│   Boltic, Ratl, Kaily, Fynd Horizon, AutRi, GMetri, IntelliVerse, NextWave, PulsePoint,
│   InstaDesk, Cortex)
├── Verify Reliance-owned framing: outcomes attributed to Reliance, not Fynd
├── Run the pre-publish checklist (Section 9) line by line against a sample of 5+ user-facing strings
├── Flag emojis or exclamation marks (banned)
└── Score: tone-of-voice compliance (0-100)

Phase 5: HONESTY REGISTER AUDIT → references/audit-framework.md §3
├── Identify every status claim on the page (Live / Building / Roadmap / Pilot / Phase 1 / etc.)
├── For each, check that it carries a pill matching the source's actual state
├── Cross-check pills against the source compilation folder's most-recent status report
├── Flag overclaims: "Live" where source says "in build" or "in test"
├── Flag underclaims (rare but possible): "Roadmap" where source says "shipped"
├── Check forward-looking phase strips for date-binding (per tone-of-voice §3 last bullet)
└── Score: honesty register (0-100)

Phase 6: VISUAL AUDIT → references/visual-audit-checklist.md
├── Confirm dev server is reachable (curl http://localhost:8765/<route>)
├── Use Chrome DevTools MCP: new_page → bypass auth via sessionStorage → list_console_messages,
│   list_network_requests for image + document resourceTypes
├── For each <img> on the page, confirm 200 status; flag any 404 / image not loaded
├── For each <embed>, <iframe>, confirm renders + content loads
├── Take a hero screenshot at 1280×900; take a mobile screenshot at 375×812; take a
│   full-page screenshot for archive
├── Visual scan the screenshots for: pill overlap, broken layouts, missing images,
│   overflow on mobile
└── Score: visual completeness (0-100)

Phase 7: CROSS-PAGE CONSISTENCY AUDIT → references/audit-framework.md §4
├── Grep the home page (index.html) for references to the page's slug; check stats match
├── Grep catalog/index.html for the section header and any item-row references; check status pills match
├── Grep the mega-menu block (present in every page's nav) for the section's mono-suffix; check it matches
├── Check all sibling pages for stale references (e.g., a sibling page that quotes a number that the page just changed)
└── Score: cross-page consistency (0-100)

Phase 8: DESIGN-SYSTEM COMPLIANCE AUDIT → docs/design.md (FULL — it is the visual rule-set)
├── Grep the page's inline <style> blocks and class attributes for hex literals: every #RRGGBB
│   must either appear in style.css :root tokens (docs/design.md §1.1) OR be whitelisted as
│   decorative (architecture/diagram fills). Flag any other ad-hoc hex.
├── Grep for off-scale font-sizes: `font-size: \d+(\.\d+)?px` in inline styles AND `text-\[[\d.]+px\]`
│   in class attributes. Every value must be on the documented scale (10/11/12/13/14/15/16/18/24/32/36/48/64/72).
│   Flag off-scale values with file:line.
├── Verify caption color target (post-sweep): mono captions render at #4B5563, not legacy #6B7280.
│   If the global sweep has landed, flag any direct use of `--ink-muted` on .section-label / .crumb /
│   .cap-num / table th / .mega-col-label.
├── Verify on-rhythm paddings: cards use p-4 / p-5 / p-6 / p-8 only. Flag p-3.5, p-7, etc.
├── Verify pill / button / card variants are documented in docs/design.md §2. Flag undocumented
│   hand-styled variants (e.g., a one-off rounded-2xl card or a custom button color).
├── Confirm `:focus-visible` and `prefers-reduced-motion` rules are present in style.css and not
│   overridden inline.
├── Confirm lightbox convention if the page has product / UI / admin <img> (already in Phase 6).
└── Score: design-system compliance (0-100)

Phase 9: SYNTHESIS
├── Calculate overall score (weighted average — see scoring model)
├── Determine pass/fail (≥75 = pass)
├── Compile top 5 critical findings
├── List 3-5 things the page does well (counter-weight)
├── Generate prioritised fix list (each with file:line, severity, what/where/why/how)
├── Write audit report to chat
└── Write audit-findings JSON to docs/audits/<page-slug>-audit-<YYYY-MM-DD>.json
```

## Machine-readable output

Always write `docs/audits/<page-slug>-audit-<YYYY-MM-DD>.json` as the final synthesis step. Schema:

```json
{
  "page": "granary/index.html",
  "spec": "docs/granary-spec.md",
  "audit_date": "2026-05-01",
  "tier": "A | B | C | excluded-canonical",
  "score": 88,
  "grade": "B+",
  "pass": true,
  "dimensions": {
    "structural_compliance": 95,
    "source_traceability": 90,
    "tone_of_voice": 85,
    "honesty_register": 92,
    "visual_completeness": 95,
    "cross_page_consistency": 70,
    "design_compliance": 88
  },
  "findings": [
    {
      "id": "H1",
      "severity": "CRITICAL | HIGH | MEDIUM | LOW",
      "dimension": "tone_of_voice | source_traceability | honesty_register | structural_compliance | visual_completeness | cross_page_consistency | design_compliance",
      "section": "§01",
      "issue": "One sentence: what's wrong",
      "fix": "One sentence: what to do",
      "files": ["granary/index.html:LINE"],
      "auto_fixable": true
    }
  ],
  "strengths": [
    "Single-sentence statement of what the page does well — name 3-5 specific items"
  ]
}
```

`auto_fixable` is `true` only when the fix is mechanical (rewrite a string, swap a banned word, add a citation, retag a pill). Set `false` for fixes requiring human judgement (regenerate a screenshot, decide whether to drop a section, restructure the page).

## Scoring model

```
OVERALL SCORE = weighted average of 7 dimensions:

Dimension                Weight    Threshold (pass)
─────────────────        ──────    ────────────────
Source Traceability       22%         75
Tone of Voice             18%         80
Honesty Register          18%         80
Structural Compliance     14%         85
Design Compliance         10%         80
Visual Completeness        9%         85
Cross-Page Consistency     9%         70

OVERALL PASS THRESHOLD: 75/100

GRADE SCALE:
90-100  A   Publishable. Minor polish only.
80-89   B   Strong. Specific fixes needed; foundation solid.
70-79   C   Acceptable with revisions. Meaningful gaps.
60-69   D   Below standard. Significant rework required.
<60     F   Fail. Fundamental gaps. Rework or restructure.
```

## Severity classification

| Severity | Definition | Example |
|---|---|---|
| **CRITICAL** | Page credibility compromised. Must fix before sharing with Apex. | Fabricated number. Unsourced claim presented as fact. Banned construction in hero. Live pill on a not-yet-built module. |
| **HIGH** | Significant gap that an Apex reviewer will notice. Fix before sharing. | Banned vocabulary in body copy. Date format wrong. Stale stat on home card. Section missing per spec. |
| **MEDIUM** | Quality gap that reduces professionalism. Fix if time allows. | Numbers that match source but use Western format where Indian was expected. Sibling page lists a renamed item under the old name. Slight overclaim that source supports loosely. |
| **LOW** | Polish item. Nice to fix. | Inconsistent spacing in mono-suffix. Section-label punctuation drift. Missing alt-text on a decorative image. |

## Reference files

Read these during the corresponding audit phase:

| File | When to read | What it contains |
|---|---|---|
| `references/audit-framework.md` | Phases 1, 2, 5, 7 | **§0 Page-tier classification** (read FIRST), structural rubric, **§1B JCP parity matrix · Tier A only**, **§1C JCP 11-section shape · Tier A only**, honesty-register rubric, cross-page consistency rubric, scoring weights, **§6 universal mechanical sweeps**, **§7 multi-page synthesis report format** |
| `references/source-audit-protocol.md` | Phase 3 | Step-by-step protocol for tracing every claim to a source file. Failure patterns. Sample-vs-exhaustive trade-offs. |
| `references/visual-audit-checklist.md` | Phase 6 | Chrome DevTools MCP recipe, image-load check, mobile-render check, console-message classification |
| `references/wiring-audit-protocol.md` | Wiring sweep mode (separate from per-page) | Register-wide route resolution, anchor integrity, mega-menu coverage, sub-nav targets, Vercel-vs-local divergence trap, canonical chrome consistency |
| `.claude/skills/website-tone-of-voice.md` | Phase 4 | The canonical tone-of-voice ruleset. Read in full — it is the rule, not a summary of it. |
| `docs/design.md` | Phase 8 | The canonical visual / design ruleset. Tokens, components, font scale, paddings, motion, a11y. Read in full during the design-compliance phase. |

## Usage modes

### Full audit (default)
```
Input: page.html + spec.md + source compilation folder
Output: full 8-section audit report + JSON
Duration: ~15-20 minutes
```

### Targeted audit
```
Input: page.html + scope="tone" (or "sources" or "honesty" or "visual")
Output: that single dimension's audit + targeted fix list
Duration: ~3-5 minutes
```

### Pre-share quick check
```
Input: page.html only
Output: tone-of-voice + structural sweep, pass/fail go-no-go
Duration: ~2-3 minutes
```

### Delta audit (after a fix pass)
```
Input: page.html + previous audit JSON
Output: re-scores only the dimensions that had findings; verifies fixes were applied
Duration: ~5-8 minutes
```

### Register-wide audit (multi-page synthesis)
```
Input: list of N pages (or a sub-tree like `jcp/*` or `Tier A platform pages`)
Output: MASTER-AUDIT-<YYYY-MM-DD>.md per audit-framework.md §7 — score table ranked
        worst→best, cross-cutting systemic issues, JCP parity matrix grid, recommended
        fix waves, suggested branching plan, verification checklist
Duration: ~30-60 minutes (delegate per-page scoring to parallel Explore agents, synthesize
        in the orchestrator)
Use when: pre-deploy hygiene sweep · post-restructure verification · register baseline
```

### Wiring audit (whole register · routes / anchors / chrome)
```
Input: repo root (default `.`) + optional sub-tree filter
Output: wiring-audit-<YYYY-MM-DD>.md per references/wiring-audit-protocol.md — internal
        route resolution, anchor integrity, mega-menu coverage, sub-nav target validation,
        Vercel-vs-local divergence trap, asset resolution, chrome consistency
Duration: ~20-30 minutes
Use when: before any deploy that touches site_chrome.py or top-level routes · after a
        rename / promotion / multi-page restructure · quarterly hygiene baseline
```

## Quality bar for the audit itself

The audit must be:

- **Specific.** *"`granary/index.html:84` says `−19.5%` but the source `Granary Cortex case study` p.3 says `−19.5%`"* — not "numbers check out".
- **Actionable.** Every finding includes file:line, the offending string, and the fix string.
- **Fair.** Acknowledge what the page does well. The summary should call out 3-5 strengths. A purely-negative audit is a worse audit.
- **Calibrated.** Don't mark everything CRITICAL. A spacing inconsistency is LOW. A fabricated stat is CRITICAL. Severity must match impact on Apex usability.
- **Citation-grounded.** When you flag a tone-of-voice violation, cite the rule (e.g., "tone-of-voice §3 banned constructions"). Don't invent rules; the existing skill is the source of truth.

## What this skill is NOT

- **Not a re-author.** When the audit finds a tone-of-voice violation, it reports the offending string and the recommended replacement. It does not rewrite the page. The fix pass is a separate operation.
- **Not a fact-source.** When a claim cannot be traced to a source file, the skill flags it as a gap; it does not make a judgement call about whether the claim is true. That judgement belongs to the page author.
- **Not a design critic.** Visual issues are limited to "does it load, render, fit on mobile, look broken?" — not "is the layout beautiful?". For design critique, use `impeccable:critique` or `impeccable:audit`.
