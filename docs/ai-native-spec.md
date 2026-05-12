# AI-Native Engineering · Spec

**Status:** v0.1 · 2026-05-02 · draft for sign-off
**Route:** `/ai-native/` (new)
**Source content:** `docs/agent-catalog-notes-compilation/Agentisation of an Organization.docx` · §"AI Coding: Autocomplete to Agents" + the existing `/organisation/#ai-native` content block (10 principles + adoption survey + tools mix)
**Narrative anchor:** Apex reader question → *"Has Fynd actually become AI-native, or is it just talk?"* The page is the answer in one scroll: an evolution arc, the operating mandate, the repo as the operating system, the adoption numbers, and HireFirst as the proof that a single engineer + an agent can ship an enterprise platform in three days.
**Inherits from:** `docs/website-orientation-spec.md` · register copy via `website-tone-of-voice` skill

---

## 1. Why this page exists

**Audience.** RIL Apex leadership (MM Sir level). Reads in 2-3 minutes. No technical drill-down.

**Gap to close.** AI-native ways of working currently sit as a tab on `/organisation/` — buried under "who runs the twelve tracks". Apex readers visiting the org page are looking for the directory, not the operating model. The operating model deserves its own register entry, prominently linked, so it is searchable, citable, and not subordinated to org structure.

**Why this belongs in the apex register.** Three reasons:
1. **The arc is the story.** Software engineering itself has shifted in 2025-26. Apex needs a clean read on where Fynd sits on that arc — and that read is currently a tab title, not a page.
2. **The proof point is unmistakable.** HireFirst was prompted by an MM Sir WhatsApp, built end-to-end by 1 engineer + an AI coding agent in <3 days, now Live and used by Reliance. That datapoint deserves a destination.
3. **Adoption is measured.** 65% of the org reports AI-fluent or advanced use; 73% use AI tools daily; 7,989 hours per week saved on Claude alone (235 active users · ~34h each). Numbers like these earn an apex page.

---

## 2. Source inventory

| Source | Type | Path | Key facts |
|---|---|---|---|
| Agentisation of an Organization | docx | `docs/agent-catalog-notes-compilation/Agentisation of an Organization.docx` | §"AI Coding: Autocomplete to Agents" arc · HireFirst (Orion) story (1 engineer · <3 days · MM Sir WhatsApp prompt) · five HireFirst capabilities (JD creation · sourcing · shortlisting · interview design · final decision support) |
| Existing /organisation/#ai-native content | html | `organisation/index.html` lines 224-405 | 10 principles · two-survey adoption pulse (1,168 responses) · external tool mix · Fynd-built tool usage |
| Internal Fynd AI tooling surveys | survey · referenced in /organisation/ | (results live in /organisation/ data) | 65% fluent · 73% daily use · 7,989 hrs/wk saved on Claude · 235 active Claude users · ~34h/person/week |
| HireFirst page (cross-link target) | html | `hirefirst/index.html` | RIL-rebranded HR Tech platform · live on SIT · prod sign-off in flight |

**Aggregate KPIs derivable from source:**
- Engineering practice arc · 3 stages (autocomplete → IDE pair programming → agent-led SDLC)
- 10 operating principles · single mandate, issued to Product Engineering (Dev / PM / Program / QA)
- 1,168 survey responses · 65% AI-fluent · 73% daily use · 7,989 hrs/wk saved on Claude
- AI fluency distribution: Fluent 51% · Developing 28% · Advanced 14% · Just starting 6%
- HireFirst · 1 engineer · <3 days · 5 capabilities live

---

## 3. Page structure

Five sections plus hero. No §Sources block (per `website-tone-of-voice` §3, established 2026-05-02). All claims cite inline.

### §0 · Eyebrow + Hero
- Crumb: `Home / AI-Native Engineering`
- Section label: `AI-NATIVE · HOW FYND BUILDS NOW`
- H1: **Engineering, AI-native.**
- Subhead (under 30 words): *"What used to take a team weeks now ships in days. The repo replaces the wiki. Code is cheap; judgment, taste, and verification are the new constraints."*
- **Visual hook · arc strip** (3 stages, full-width): `Autocomplete · ~2021` → `IDE pair programming · ~2023` → `Agent-led SDLC · 2025-26 · current`. Each stage carries one line on what the engineer actually does.
- Stat tiles (4): `Org-wide AI fluency · 65%` · `Daily AI use · 73%` · `Hours saved per week · Claude · 7,989` · `HireFirst built in · <3 days · 1 engineer`

### §01 · What changed in the engineer's day
- Component: 3-card horizontal strip, one per arc stage
- Each card: stage label · year · what the engineer used to do · what they do now
- Closing line below grid: *"Today a single engineer + an agent can ship what a feature team shipped two years ago."*
- Source: Agentisation §"AI Coding"

### §02 · Ten principles · the operating mandate
- Component: 2-column card grid (10 cards), lifted verbatim from `/organisation/#ai-native` §01
- Lede: *"Issued to all of Product Engineering — Dev, PM, Program, QA. Repos, knowledge hubs, agent design, team shape, role boundaries, QA automation, architecture restraint, curiosity."*
- No date, no individual attribution (per §9 D2)

### §03 · The repo is the operating system
- Component: visual collapse diagram (replaces the v0.1 text-heavy 2-col + repo-tree)
- H2: *"Disciplines collapse into skills."*
- Lede: *"One repo per product. Frontend, backend, QA, SRE, UI/UX, DevOps, security, docs — what used to be eight teams with eight stacks now live as skills inside the repo. Any engineer or agent invokes any skill."*
- **Diagram structure** (single white card containing three stacked layers):
  1. **Yesterday row** — 8 small silo cards in a horizontal grid (Frontend / Backend / QA / SRE / UI/UX / DevOps / Security / Docs), each with the discipline name + 2-word old-toolchain hint
  2. **Funnel** — 8 ↓ arrows, one per silo column, visually pulling each discipline down into the repo
  3. **Today: the repo** — dark `product-repo/` box. Header line shows the path + `.claude/skills/ · /docs` tag. Inside, a 4×2 grid of **skill cards**: each card has a small accent ribbon naming the discipline that collapsed into it (`FRONTEND` / `BACKEND` / etc.), the mono filename, and a one-line description
  4. **Invoker strip** below — three pill chips: `Any engineer · Any PM/QA/designer · Any agent` (agent in accent purple). Caption: *"All read from the same skills. The repo is the contract."*
- Closing line: *"Long-term target: ~25 repos for the entire company. Microservices preserved — consolidation happens at the code-repo layer so the surface an agent indexes stays bounded."*
- **Why this works**: the diagram makes the abstract "disciplines collapse" claim concrete in seconds. An exec sees the silos at top, the funnel, and the same disciplines reappearing as skill files inside the repo. The invoker strip closes the loop — anyone reads from the same source.

### §04 · How it shows up · adoption + the HireFirst proof
- **Top half · adoption** (lifted from `/organisation/#ai-native` §02, condensed):
  - 4 stat tiles: `65% fluent` · `73% daily AI use` · `7,989 hrs/wk saved on Claude` · `235 active Claude users`
  - 2 bar-chart cards side by side: AI fluency distribution + Claude surface usage
  - 1 narrow strip · external tool mix as inline chips (ChatGPT 570 · Cursor 424 · Gemini 268 · Claude 221 · Perplexity 88 · Lovable 80 · Antigravity 52 · Codex 43)
- **Bottom half · HireFirst proof point** (full-width card):
  - Eyebrow: *"PROOF POINT"*
  - One-line claim: *"HireFirst — Reliance HR Tech platform — built end-to-end by 1 engineer + an AI coding agent in <3 days. Prompted by an MM Sir WhatsApp message."*
  - **Day-by-day micro-timeline** (Day 1 · Day 2 · Day 3) — each day with one line of what shipped
  - Five capability bullets: AI-Powered JD Creation · Smart Sourcing · AI Shortlisting · Interview & Evaluation Design · Final Decision Support
  - Single CTA link to `/hirefirst/`

### Footer
Standard copyright line only. No Owner / version line (per spec convention §1).

---

## 4. Data model

This is a single-page section, hand-authored. **No YAML required.** All copy lives inline in `ai-native/index.html` because:
- No sub-pages to drive
- No N×repeat content; every section is bespoke
- The existing `/organisation/` material is being lifted literally — re-encoding it in YAML adds no value

If a renderer is needed later (e.g., adding deep-dives per principle), schema would be:

```yaml
slug: ai-native
title: AI-Native Engineering
status: live
date: 2026-05-02
source_folder: docs/agent-catalog-notes-compilation/
arc:
  - stage: autocomplete
    year: ~2021
    used_to_do: ...
    do_now: ...
principles:
  - n: 1
    title: ...
    body: ...
adoption:
  fluent_pct: 65
  daily_use_pct: 73
  hours_saved_week: 7989
hirefirst_proof:
  engineers: 1
  days: 3
  prompt_source: "MM Sir WhatsApp"
  capabilities: [...]
```

Stick with hand-authored HTML for v1.

---

## 5. Asset pipeline

**No image assets in v1.** All visuals are CSS / inline SVG:
- Arc strip: 3 cards in a flex row with connector lines (CSS borders)
- Repo-tree mock: monospace `<pre>` block with text-based tree characters
- Bar charts: existing `.bar` / `.bar-fill` classes from `style.css`
- HireFirst day-by-day: 3 cards in a flex row with day labels

If we later want a screenshot of HireFirst (to illustrate the proof point with a real UI), we lift the existing `/hirefirst/` cover screenshot — no new asset pipeline needed.

---

## 6. Navigation wiring

Strict-vs-lazy decision: **lazy for v1.** Land in two places only.

- [x] Home page card · `index.html` · add `/ai-native/` as a new card alongside Organisation and Culture
- [x] Top-nav `More` mega-menu · add `<a href="/ai-native">AI-Native Engineering</a>` next to Organisation
- [ ] IP Catalog entry (`/catalog`) — defer to v0.2
- [ ] Footer "Other tracks" lists on every track page — defer (lazy strategy)
- [ ] Sibling section indexes that mention this one — N/A on v1

Nav block on every other page (~25 files) keeps the existing menu — no entry yet for `/ai-native/` until v0.2 sweep.

---

## 7. Build / verify

Hand-authored single page. No build script.

```bash
# Serve locally
python3 -m http.server 8765
# Open http://localhost:8765/ai-native/
# Bypass auth gate: sessionStorage.setItem('fyndrrl_auth_v1','1') in DevTools console
```

**Verify checklist** (subset of `website-section-authoring` §9):
- [ ] Section index loads
- [ ] All stat numbers match source
- [ ] Arc strip renders cleanly mobile + desktop
- [ ] 10 principles cards render in 2-col on desktop, 1-col on mobile
- [ ] Repo-tree mock is monospace and readable
- [ ] Bar charts render correctly
- [ ] HireFirst CTA link resolves to `/hirefirst/`
- [ ] Console clean (no JS errors)
- [ ] Mobile viewport (375px) renders OK
- [ ] Every URL in copy is wrapped in an `<a>` (no plain text URLs)

---

## 8. Phased delivery

| Phase | Scope | Time |
|---|---|---|
| **P1** | Spec (this file) | ~30 min |
| **P2** | Hand-author `ai-native/index.html` (~600 lines) | ~90 min |
| **P3** | Nav wiring (home card + More mega-menu) | ~10 min |
| **P4** | Verify + tone-of-voice sweep + screenshots | ~20 min |
| **P5** | (separate confirm) Strip §01-§03 from `/organisation/#ai-native` | ~15 min |

Total v1 (excluding P5): **~2.5 hr.**

---

## 9. Decisions

Locked from the brainstorm round:

1. **D1 · Route = `/ai-native/` · new page · /organisation/ keeps directory.** AI-native ways of working get their own register entry. /organisation/ §01-§03 (principles + adoption + tools) move here. /organisation/ keeps Org Structure tab + leaders + directory only.
2. **D2 · Hero lens = arc-led.** Open with the 3-stage timeline (Autocomplete → IDE chat → Agent-led SDLC). Adoption numbers and HireFirst proof appear in stat tiles, not as the lead.
3. **D3 · Repo-as-OS gets a standalone §03 section.** Lifted out of Principle 02 and given dedicated framing. Echoes the "harness engineering" idea but in our own register.
4. **D4 · Length = short · 4-5 sections · 2-3 min read.** No deep-dives, no per-principle expansions, no agent-architecture deep dive. The /agents/ catalog covers that.
5. **D5 · HireFirst (not Orion) throughout.** The page reports the Reliance-facing brand name. Orion is mentioned only in source-folder context (Agentisation docx). The proof story stays the same: 1 engineer · <3 days.
6. **D6 · Drop the date and the named author from the principles block.** Present the 10 principles as the operating mandate without "Issued by Salman Saudagar on …". Page-level DRI lives in git, not on the page.
7. **D7 · No author / version line in hero or footer.** Per `website-section-authoring` §4 convention. Copyright line only.
8. **D8 · Cross-page implications acknowledged.** /organisation/ strip is a separate confirmation step, not bundled into the v1 ship.

---

## 10. Out of scope (v1)

- **Per-principle deep-dives** (one page per principle). Principles are punchy enough as a 2-col card grid; expanding would dilute.
- **Eval framework deep-dive.** Mentioned briefly via "evals" in the repo-as-OS section; a full eval-process page belongs in `/agents/` or a future `/quality/` route.
- **Agent architecture deep-dive** (tool calling, context engineering, multi-agent orchestration, observability). All of this is in the Agentisation docx Appendix B, but it belongs on `/agents/` not here. This page is about *engineering practice*, not *agent design*.
- **Org-wide tooling rollout playbook.** How Fynd onboards a team to Cursor / Claude Code / Boltic — operational detail, not apex content.
- **Footer "Other tracks" sweep across ~25 pages.** Deferred to v0.2 nav clean-up.
- **IP Catalog entry.** Deferred to v0.2.
- **Strip of /organisation/#ai-native §01-§03.** Done as a separate confirmation step (P5) after v1 of `/ai-native/` is accepted.

---

**End of spec.** Sign-off received from brainstorm round (route, lens, repo framing, length all locked). Proceeding to build.
