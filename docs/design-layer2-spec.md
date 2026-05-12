# Design system · Layer 2 cleanup spec

Spec for the **structural moat** work that completes `docs/design.md`. After this, the design system is enforced by file structure (not discipline), and the page-reviewer's `design_compliance` dimension goes from "useful detector" to "near-zero false positives".

**Status:** not started · **Estimated effort:** 6-10 focused hours · **Risk:** low

---

## Why

`docs/design.md` is the visual canonical and the page-reviewer skill audits against it. Today there are three places where pages can drift even when authors try to follow the spec:

1. **Per-page inline `<style>` blocks** — every page has at least one. Some recurring patterns (`lens-card`, `num-display`, `hero-grad`, `platform-card-*`) are duplicated across multiple pages instead of living in `style.css`.
2. **Hard-coded hex literals on pages** — ~28 distinct hexes appear in page HTML/inline-CSS that aren't in the `:root` token list. Some are legitimately decorative (architecture-diagram fills), but several are structural near-duplicates of tokens (`#E5E7EB` used 43 times where `var(--border)` would do).
3. **Off-scale ad-hoc sizes** — a handful of `font-size: 11.5px` and `text-[Npx]` Tailwind arbitraries that bypass the documented scale.

Layer 2 closes these gaps so any future page change either uses tokens / classes that exist or fails the `website-page-reviewer` design-compliance phase.

---

## Acceptance criteria

A pass means **all four** are true:

1. **No structural hex literals on pages.** Greps below return zero results except for whitelisted decorative hexes:
   ```bash
   # Hex literals in page HTML / inline styles
   grep -hoE '#[0-9A-Fa-f]{6}' --include='*.html' -r . \
     | grep -v -f docs/design-layer2-decorative-hexes.txt \
     | sort -u
   ```
2. **No off-scale font sizes.** Greps below return zero results:
   ```bash
   # Inline style font-sizes
   grep -hnE 'font-size:\s*[0-9.]+px' --include='*.html' -r . \
     | grep -vE ':\s*(10|11|12|13|14|15|16|18|24|32|36|48|64|72)px'

   # Tailwind arbitrary text sizes
   grep -hnE 'text-\[[0-9.]+px\]' --include='*.html' -r .
   ```
3. **Recurring inline patterns promoted.** The CSS classes listed in §3 below are defined once in `style.css`, not duplicated across pages. Each page that uses a pattern uses the canonical class.
4. **Visual diff is null.** Before/after screenshots of the home page, jcp/, impetus/, granary/, pixelbin/ are visually identical (apart from any pixel-level rendering noise).

---

## Scope (in)

| Area | What |
|---|---|
| Recurring inline CSS patterns | Promote to `style.css`. See §3 for the full list of candidates. |
| Structural hex literals | Replace with `var(--*)` tokens. See §4. |
| Off-scale font sizes | Snap to nearest documented size. See §5. |
| Per-page CSS that references the legacy `--border` (#E5E5E5) directly via inline style | Replace with `var(--border)`. |

## Scope (out)

| Area | Why |
|---|---|
| Decorative hex colors in architecture diagrams (e.g., the colored boxes in the JCP architecture chart) | Diagram-specific palette; promoting to tokens has no benefit. Whitelist them in `docs/design-layer2-decorative-hexes.txt`. |
| Inline `<style>` blocks that are genuinely one-off (only used on one page, for a one-off layout) | Promotion would add to `style.css` weight without reuse. Keep as inline. |
| Spec / tone / data changes | This is purely a structural CSS cleanup. No copy edits. |
| The `tools/scratch/_original.html` file | Frozen snapshot, intentionally untouched. |
| `docs/impetus-index-backup-2026-04-30.html` | Frozen historical snapshot. |

---

## §1 · Discovery (do this first)

Spawn the Explore agent with this prompt to map the leak surface concretely:

```
Audit every index.html file in this repo (excluding tools/, docs/) for:
1. Each <style> block: list its CSS rules (selector + key properties), and which file it's in
2. Each hex literal (#RRGGBB) in inline style attributes or in <style> blocks
3. Each font-size: Npx in inline styles
4. Each text-[Npx] Tailwind arbitrary in class attributes
5. Each padding-[Npx] / w-[Npx] / etc. Tailwind arbitrary

Output a CSV with columns: file, line, leak_type (style-block | hex | font-size | tw-arbitrary), value, context (the selector or surrounding class).

Limit to 200 lines max. Sample if larger.
```

Save the output to `tools/scratch/layer2-leak-audit.csv`. Use it as the work plan for §3-§5.

---

## §2 · Update `docs/design.md` first

Before any code changes:
- Add the decorative-hex whitelist file path to `docs/design.md` §1.1 ("Color rules" sub-section): "Decorative diagram hexes are whitelisted in `docs/design-layer2-decorative-hexes.txt`. Anything not in `:root` and not in the whitelist is a violation."
- Document the canonical names of the patterns being promoted in §3 below — add them to `docs/design.md` §2 "Components" with their specs.

This keeps design.md the single source of truth.

---

## §3 · Promote recurring inline patterns to `style.css`

Candidates identified from existing `<style>` blocks. The exact list to promote depends on §1's audit — these are the obvious recurring ones:

### Already promoted (verify, no work needed)
- `.card` / `.card-hover` (style.css)
- `.btn-primary` / `.btn-secondary` (style.css)
- `.pill` + variants (style.css)
- `.section-label`, `.crumb`, `.cap-num`, `.subnav-link`, `.mega-link`, `.nav-version` (style.css)
- `.grid-table` (style.css)

### To promote (currently duplicated in multiple page `<style>` blocks)

| Class | Currently in | Promote to `style.css` as |
|---|---|---|
| `.lens-card` | `index.html` (home page hero) | `.lens-card { background: white; border: 1px solid var(--border); border-radius: 20px; padding: 32px; transition: border-color 0.2s, transform 0.2s; display: flex; flex-direction: column; height: 100%; }` + hover variant |
| `.lens-title` / `.lens-eyebrow` / `.lens-bullet` | `index.html` | Promote as a group with the lens-card |
| `.platform-card` + sub-classes (`-head`, `-name`, `-desc`, `-foot`, `-tag`, `-metric`) | `index.html` | Promote as a group |
| `.num-display` | `index.html`, several stat-tile pages | `.num-display { font-family: 'Inter', sans-serif; font-weight: 800; letter-spacing: -0.04em; line-height: 0.9; }` |
| `.hero-grad` | `index.html`, `jcp/index.html`, others | `.hero-grad { background: radial-gradient(ellipse at top, rgba(107,91,214,0.08) 0%, transparent 60%); }` |
| `.timeline-rail` / `.timeline-dot` | `index.html` | Promote as a group |
| `.filter-chip` | `index.html` | Promote (used on home filter strip) |
| `.ink-grad` | `index.html` | Promote |

**For each promotion:**
1. Add the rule(s) to `style.css` in the appropriate section.
2. Remove the duplicate from each page's inline `<style>` block.
3. Visual-diff the page in Chrome DevTools to confirm zero pixel change.
4. Document the new class in `docs/design.md` §2.

**For one-off patterns** (used on only one page): leave inline. Add a comment in `docs/design.md` §2 "When to inline" noting which pages own which one-off styles.

---

## §4 · Replace structural hex literals with tokens

From the leak audit (§1), build a sed-rewrite script:

```bash
# Example — adapt to actual finds
sed -i '' 's/#E5E7EB/var(--border)/g' <files>  # gray-200 → border token
sed -i '' 's/#1E293B/var(--ink)/g' <files>     # slate-900 → ink (only if it's text/border, not a diagram fill)
sed -i '' 's/#6B7280/var(--ink-muted)/g' <files>  # gray-500 → muted token
```

**Rules:**
- Inspect each hex's usage before rewriting. A `#1E293B` used as a diagram-box fill is decorative; a `#1E293B` used as text color should become `var(--ink)`.
- Don't rewrite hexes inside `<svg>` paths or `<img>` src attributes.
- Don't rewrite hexes inside JS strings (rare but possible — e.g., chart configs).
- After rewrite, run a visual diff per affected page.

**Decorative whitelist file** (create at `docs/design-layer2-decorative-hexes.txt`):
- Each line is one decorative hex value that is allowed to appear without being a token.
- Examples: architecture-diagram fills (`#DBEAFE`, `#BBF7D0`, `#FED7AA` outside the pill variants), Reliance brand colors, third-party logo colors.
- Format: one hex per line, optionally followed by `# reason`.

---

## §5 · Snap off-scale sizes

Documented scale is `10 / 11 / 12 / 13 / 14 / 15 / 16 / 18 / 24 / 32 / 36 / 48 / 64 / 72`px.

For each off-scale find:
- `11.5px` → `12px`
- `13.5px` → `14px`
- `text-[19px]` → `text-lg` (18) or `text-xl` (20) — pick the closer
- Any value < 10 → bump to 10

Snap up by default unless the visual diff shows a regression.

---

## §6 · Add the linter (optional but recommended)

Once §3-§5 are clean, add `tools/check_design.py` so future drift is caught at commit time:

```python
# Pseudocode
ALLOWED_FONT_SIZES = {10, 11, 12, 13, 14, 15, 16, 18, 24, 32, 36, 48, 64, 72}
WHITELIST_HEXES = read('docs/design-layer2-decorative-hexes.txt')
TOKEN_HEXES = {extract from style.css :root}

for html_file in walk_register_pages():
    for hex_match in extract_hexes(html_file):
        if hex_match.value not in TOKEN_HEXES and hex_match.value not in WHITELIST_HEXES:
            error(html_file, hex_match.line, f"Off-token hex {hex_match.value}")

    for size_match in extract_font_sizes(html_file):
        if size_match.value not in ALLOWED_FONT_SIZES:
            error(html_file, size_match.line, f"Off-scale font-size {size_match.value}px")

# Exit non-zero if any errors
```

Wire it into a pre-commit hook or CI check — same model as `tools/inject_chrome.py --check`.

---

## §7 · Verification

Per page touched (jcp/, impetus/, granary/, pixelbin/, home, plus any sub-pages of those tracks):

1. **Computed-style snapshot:** before-and-after `getComputedStyle()` for `.section-label`, `.cap-num`, `.crumb`, `.card`, `.pill`, `.btn-*`, `table.grid-table th` — should be identical.
2. **Visual diff:** Chrome DevTools MCP screenshot before-and-after at 1280×900. Any pixel change is a finding.
3. **Console clean:** only the standard Tailwind CDN warning is acceptable.
4. **Page-reviewer audit:** run `website-page-reviewer` on each touched page; the `design_compliance` dimension should score ≥90.

---

## §8 · Effort breakdown

| Task | Hours | Tools |
|---|---|---|
| §1 Discovery (Explore agent) | 1-2 | Agent + grep |
| §2 Update design.md | 0.5 | Read + Edit |
| §3 Promote 5-8 recurring patterns | 2-3 | Read + Edit per page; visual verify |
| §4 Replace structural hex literals | 1-2 | sed across pages; visual verify |
| §5 Snap off-scale sizes | <1 | sed; visual verify |
| §6 Add linter (optional) | 1-2 | Python script |
| §7 Verification across affected pages | 1-2 | Chrome DevTools MCP + page-reviewer |

**Total: 6-10 hours** for a focused sitting. Stretch to 8-12 hours if including §6 linter.

---

## §9 · Sequencing

Recommended order — optimised so each step is independently reviewable:

1. §1 Discovery (gives you the work plan)
2. §2 Update `docs/design.md` to reflect the planned promotions
3. §3 Promote one pattern at a time, commit each (`design · promote-<name> · move from inline to style.css`)
4. §4 Hex sweep, one related cluster at a time, commit each (`design · token-sweep · replace #XXX with var(--*)`)
5. §5 Off-scale snap (one commit, since it's small)
6. §6 (optional) Add `tools/check_design.py` — separate commit
7. Run §7 verification, capture audit JSONs to `docs/audits/`

---

## §10 · Things to NEVER do during Layer 2

- **Don't change visual appearance.** Layer 2 is structural cleanup. If a promotion changes pixels, it's wrong — adjust until pixel-identical.
- **Don't touch tone or data.** No copy edits, no number updates.
- **Don't add new visual patterns.** This is a consolidation pass, not a redesign.
- **Don't promote one-off patterns** that genuinely belong on one page only — keep them inline with a comment in `docs/design.md` §2.
- **Don't bypass the canonical-source rule** — every promoted class must be documented in `docs/design.md` §2.

---

## §11 · After Layer 2

Once complete:
- Tier 4 from `docs/design.md` §7 ("Bigger calls") becomes safe to attempt — typed scale tokens (`--text-xs / sm / base / md / lg / xl`) and the `.tabular` utility can land in one CSS edit and propagate cleanly.
- The `website-page-reviewer` design-compliance dimension's threshold can be raised from 80 to 90.
- New section authoring (`website-section-authoring`) can include a checklist row: "Run `tools/check_design.py` before committing — must exit 0".

---

## Change log

| Date | Change |
|---|---|
| 2026-05-03 | Initial spec. |
