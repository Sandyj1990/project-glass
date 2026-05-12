# /organisation · AI Native Ways of Working tab · spec

**Status:** Drafting · 2026-05-02 · update mode (fills the placeholder shipped in `/organisation` v0.10.1)
**Route:** `/organisation/#ai-native`
**Source content:**
- `docs/ai-native-notes-compilation/Fynd_ New AI Ways of Working.docx.pdf` — 10 principles, v1.0
- `docs/ai-native-notes-compilation/AI Assessment Survey_ AI Survey Report Reponses.xlsx` — 929 responses, Dec-2025
- `docs/ai-native-notes-compilation/Claude AI Usage Survey (Responses)-2.xlsx` — 239 responses, Mar-2026
- `docs/ai-native-notes-compilation/AI_Assessment_Analysis.pptx` — internal analysis, Dec-2025
**Narrative anchor:** Farooq's 30-Apr-2026 letter to MM Sir lists the AI-Native dimension across Impetus + Fynd retail projects. This tab is the *register-side answer* to "how does Fynd actually operate AI-natively today?"

---

## §0 · What's changing and why

The `#ai-native` tab is currently a "Coming soon · instructions pending" placeholder. The compilation folder now has the source material to fill it: a CTPO-authored 10-principle operating doc and two recent internal surveys (one Dec-2025 org-wide, one Mar-2026 Claude-specific).

This update is **single-tab, hand-authored HTML** inside the existing `/organisation/index.html`. No new route, no renderer, no new YAML — the source material is small and stable. If a third survey lands, swap the numbers; if Jigar's doc revs to v2.0, swap the principles.

---

## §3 · Page structure (Add / Keep / Remove)

| Action | Section | Reason |
|---|---|---|
| KEEP | Tab heading + section label | Existing tab chrome stays |
| REMOVE | "Coming soon · instructions pending" placeholder card | Replace with real content |
| ADD | §01 · How Fynd works AI-natively · the 10 principles | Authoritative content from CTPO doc |
| ADD | §02 · Measured adoption · combined survey snapshot | Stat strip + breakdown bars |
| ADD | §03 · Tools in active use · top external + Fynd-built | Validates the principles with what people actually run |

**No §04 Sources block.** Per tone-of-voice §3 banned constructions: source provenance lives inline as eyebrow citations on each section, not as a redundant bottom-of-page list. The two source datasets are named where the numbers are cited.

---

## §3.1 · Section copy

### §01 · The 10 principles

Ten cards in a 2-column grid (1-col on mobile). Each card:
- Number (mono, large) — `01` through `10`
- Title (verbatim from the PDF, lightly truncated where >60 chars)
- 2-3 line summary (rewritten in register voice — keep the meaning, drop "Let's", "you guys", "best edge", and other addressed-to-team locutions that don't read at Apex)
- A 1-line "what this changes" or "what this means" closer

Section eyebrow: `Source · Fynd CTPO · "Embrace New AI Ways of Working" v1.0`. No personal author name (D1).

### §02 · Measured adoption

Combined-frame stat strip (D2). Four tiles:

| Label | Number | Context |
|---|---|---|
| Org-wide AI fluency | 65% | 607 of 929 respondents fluent or advanced |
| Daily AI use | 73% | 675 of 929 use AI tools daily |
| Hours / wk saved · Claude | 7,989 | Across 235 active Claude users · avg 34h/person/wk |
| Leadership clarity | 73% | 682 of 929 agree direction is clear |

Below the strip, two horizontal-bar mini-charts:

- **AI fluency distribution** — Fluent · Advanced · Developing · Just starting
- **Claude surface · daily users** — Chat · Code · Cowork · Chrome (out of 239 respondents)

Inline source line: *"Combined data from two internal surveys: AI Assessment · 929 responses · Dec-2025 and Claude Usage · 239 responses · Mar-2026."*

### §03 · Tools in active use

Two columns:

- **External tools mentioned** (top 8 from the 929-response Q4): ChatGPT 570, Cursor 424, Gemini 268, Claude 221, Perplexity 88, Lovable 80, Antigravity 52, Codex 43
- **Fynd-built AI tools used internally** (top 6 from Q13): Boltic 300, PixelBin 192, Kaily 71, Ratl 53, GlamAR 32, Ask Impetus 6

Each row: name · count · small bar. Fynd-built rows link to the platform page.

---

## §6 · Decisions

- **D1 · Author attribution.** No personal author name on the page. Cite as institutional source: *"Fynd CTPO · Embrace New AI Ways of Working v1.0"*. **Why:** user direction 2026-05-02. **How to apply:** every reference to the 10-principle doc uses institutional framing.
- **D2 · Survey framing.** Combined headline numbers, single stat strip. Inline citation discloses both source surveys + dates + response counts. **Why:** user direction 2026-05-02. **How to apply:** the strip pulls the most striking aggregate; provenance is one inline line, not two named blocks.
- **D3 · Section ordering override.** Standard register order is §01 Status → §02 Live → §03 Architecture. This tab uses §01 Principles → §02 Adoption → §03 Tools because the page is operating-model + measurement, not a product page. **Why:** the canonical ordering assumes a shipping product; this tab documents how the org works. **How to apply:** numbering is local to the tab and does not need to mirror the rest of the site.
- **D4 · No Sources block.** Source citations live inline as eyebrows. **Why:** tone-of-voice §3 default-no rule; both source datasets are already named where the numbers appear. **How to apply:** skip §04.
- **D5 · Tab-local section numbering.** Both tabs in `/organisation/` use their own §01 → §NN sequence. Org Structure tab: §01 Project × Track, §02 Directory. AI-Native tab: §01 Principles, §02 Adoption, §03 Tools. **Why:** each tab is a self-contained read; readers never see them as a single sequence (only one pane is visible at a time). **How to apply:** future audits should treat tab-local numbering as compliant; cross-tab `section-label` contiguity is not a finding.

---

## §7 · Out of scope

- Restructuring of Tab 1 (Org Structure). This update only touches `#tab-ai-native`.
- New nav wiring. The tab already exists; the URL `/organisation/#ai-native` already works.
- Changes to `/culture` or any other meta page.
- Per-team adoption breakdowns — the survey data permits this but adds noise at Apex.

---

## §8 · Acceptance

- [ ] `/organisation/#ai-native` loads three numbered sections (01 principles, 02 adoption, 03 tools), no placeholder
- [ ] All 10 principles rendered, each with a numeric eyebrow + title + 2-3 line summary
- [ ] Stat strip carries 4 numbers, each verifiable from the source spreadsheets
- [ ] Source eyebrow on §01 cites the CTPO doc · v1.0 (no personal author name)
- [ ] Source eyebrow on §02 cites both surveys + response counts + dates
- [ ] Fynd-built tool names link to their platform pages
- [ ] No emojis, no exclamation marks, no banned register words
- [ ] Mobile (375px wide) renders the 2-col card grid as 1-col
