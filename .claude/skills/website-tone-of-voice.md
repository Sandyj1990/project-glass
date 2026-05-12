---
name: website-tone-of-voice
description: Apex-readable copy register for the Fynd × Reliance Retail register at reliance-retail-fynd.vercel.app. Use whenever drafting or editing user-facing strings on this site — page heros, section copy, card content, stat labels, button text. Audience is RIL Apex leadership (MM Sir level). Copy must be factual, scannable, name names, and survive challenge.
user_invocable: true
---

# Website Tone of Voice — Fynd × Reliance Retail Register

You are writing for **RIL Apex leadership (MM Sir level)** reviewing the register at `reliance-retail-fynd.vercel.app`. Every string on this site — hero subheads, card copy, stat labels, prose sections, button text — must follow this register. Do not soften, do not add marketing voice, do not add Fynd self-praise.

This is **not** the Farooq Adam working-paper voice (that's `fa-voice`, used for strategic essays and frameworks). This is **website data-sheet voice** — terse, factual, scannable. Different register, different purpose.

---

## 1. The five rules

Every line of copy must pass all five:

1. **Factual.** Every claim is verifiable from a named source — a PDF in `docs/`, a release compendium, an Apex deck, a dated commit, an attendance sheet. If you cannot point at the source, do not write the line.
2. **Scannable.** Apex leadership reads in seconds, not minutes. Numbers up front. Names up front. Verbs early. No throat-clearing openers.
3. **No marketing voice.** No "trust layer", "habit you build", "missing rung", "game-changing", "transformative", "next-generation", "world-class", "best-in-class", "step-change". No metaphors that aren't strict equivalences.
4. **No Fynd self-praise.** Do not say Fynd is excellent, leading, innovative, or trusted. Show the work; let the reader infer the quality. Reliance owns the outcome — Fynd built the platform. Frame it that way.
5. **Names where they matter.** When a Reliance leader requested a thing, name them (Vincent Braganza, Brijkishor Singh, Arunoday Ray). When a Fynd person owns a deliverable, name them (Salman Saudagar, Raghav Mehra, Jigar Dafda). Anonymous claims read as evasive.

---

## 2. Voice & stance

### Stance
- **Reporting, not pitching.** Stating what is true today, with dates and numbers. Not selling a vision.
- **Restraint.** When a metric is impressive, the metric does the work; do not add adjectives. `1.6M JioMart orders/day` is impressive without "incredible".
- **Reliance-owned framing.** Default phrasing: *"Built by Fynd. Owned and run by Reliance."* The page belongs to Reliance's register; Fynd is the supplier.
- **No urgency, no hype.** No exclamation marks. No "now". No "today". Use specific dates instead.

### Person
- **Impersonal/institutional voice** by default. The site reports on platforms, sessions, deployments — not on what "we" did.
- **"Fynd"** when the actor must be named (e.g. *"Fynd built the platform; Reliance runs it"*).
- **"Reliance"** when the actor or owner is on the Reliance side.
- **Never "we", "our team", "our people"** in user-facing copy. They read as Fynd self-promotion.
- **"You"** is rarely used. The reader is not addressed directly.

---

## 3. Sentence construction

### Rhythm
- **Short, declarative sentences.** Most are 6-15 words. A 25-word sentence is the maximum tolerable.
- **Lists over prose** wherever the content is enumerable. A 4-item list reads faster than 4 connected sentences.
- **Numbers and dates open the line** when they are the point: *"600+ Reliance employees trained, Oct-2025 to Apr-2026."* not *"Since October 2025, the program has reached over 600 Reliance employees."*

### Signature patterns

These patterns recur across the site and should be used consistently:

1. **Number + unit + qualifier** — for stat tiles and intro lines:
   - *"68 channels live · +5 Pilot · +5 Build"*
   - *"380M+ identities · unified across RR"*
   - *"2,000+ active users · across F&L"*

2. **Date + verb + object** — for timeline entries and recent-shipped cards:
   - *"03-Apr-2026 · UCP × RPOS real-time live across 15K+ stores"*
   - *"14-Apr-2026 · Fynd Horizon unveiled to MDA at RCP"*

3. **`{Reliance entity} · {Fynd platform} · {metric}`** — for adoption claims:
   - *"Reliance Trends · Companion App · 3,000+ stores"*
   - *"RIL Industries L&D · two online sessions · 400+ participants"*

4. **DRI line at end of card** — `DRI: <name>` is the standard convention. Do not embellish.

5. **Source citation in `cap-num` style** — for any non-obvious claim: *"Source · Q1 2026 Release Compendium · p. 47"*. Source line should be inline, never as a footnote. **A short eyebrow citation is enough — do not add a separate §08 Sources block at the bottom of the page just to repeat what the eyebrow already said. See the "default-no Sources block" rule under Banned constructions below.**

6. **Negative framing only when it carries information**:
   - Good: *"Replaces Freshdesk · ₹55L/year saved."* (negation = the displaced thing has a name and a number)
   - Bad: *"Not just a chatbot — a true agent."* (negation = marketing puffery)

### Banned constructions

- **Engineering-jargon stat tiles in the hero or above-the-fold band.** Apex reads "Backend endpoints · live · 33" and "UI routes · live · 5/37" as developer-talk. The numbers may be true, but they don't *mean* anything to a reviewer who isn't building the system. Translate to outcomes ("Pilot stores · 11", "Forecast scale · 48M rows") or drop. The exception: deeper sections (architecture, deep-dive) can carry mild jargon when surrounded by enough context that the reader earns the term.
- **"Strong interest in…"** — vague. Either name the next booked session or omit.
- **"…has shifted the mindset…"** — un-measurable. State the booking that followed instead.
- **"This is not X. It is Y."** — that's Farooq's working-paper move, not website voice. Do not import it.
- **"World-class", "best-in-class", "industry-first"** — only use when there is a citable comparator.
- **"Cutting-edge", "next-generation", "transformative"** — never.
- **"Empowers", "enables", "unlocks"** — replace with the actual verb. *"Lets buyers approve POs from mobile"* not *"Empowers buyers with mobile PO approval"*.
- **Trailing summaries** — *"In summary, this section covered…"* never. The reader scrolled past it.
- **Forward-looking phases without dates.** *"Phase 0: Stability · Phase 1: Enterprise · Phase 2: Integrations · Phase 3: Intelligence."* Marketing-deck register, not Apex register. If a section makes time-promises, every promise carries a date or a named DRI. Otherwise cut the section — the credible roadmap is the in-dev list with named owners. (Worked example: `/hirefirst/` cut its 4-phase strip during the v0.9 restructure for exactly this reason.)
- **"X-month ROI payback" / "Implementation cost recovery" tiles** — defaultly cut unless there's a citable cost-recovery analysis behind the number. Apex reads them as deck-style boilerplate. (Worked example: `/jcp/` v0.7 dropped the `ROI payback · 1-2 mo` tile in feedback round 4.)
- **Decorative `↗` arrows on cards that link to the same target as the card body.** When the whole card is clickable, drop the inline arrow — it adds no information and breaks when the URL fallback routes to a homepage. If the card body isn't clickable, make the URL itself the prominent hyperlink instead. One target per card. (Worked example: `/jcp/channels/` mobile cards dropped the `↗` in feedback round 4 because for apps without a `play_package_id`, the fallback Play Store URL was a dead-end homepage.)
- **`§Sources` block · never use.** Apex pages do not carry a Sources block. The page itself is the artefact; provenance lives in git, the spec, and figure captions on screenshots. A trailing §Sources section is leadership-deck residue — the reader has reached the end of the page; restating where the page came from adds nothing the body didn't already cite. Established 2026-05-02 on the AI Agents Catalog rule sweep · prior carve-outs ("3+ external artefacts" / "reader will navigate to files") are revoked. Worked examples: `/jcp/`, `/jcp/release-notes/`, `/jcp/7eleven/`, `/jcp/channels/` all dropped Sources blocks in feedback rounds 3-4 with no loss of credibility.
- **Internal source-document references in body copy · never use.** Do not name internal source documents by their developer-facing IDs in user-facing text — *"Accenture s37"*, *"Farooq §1.4"*, *"Agentisation §3.2"*, *"Q1 2026 Release Compendium · pp. 47-49"*, *"slide 14"*, *"per Accenture s4 Retail Clock"*, *"L4 ladder cell · Farooq §1.4 row 1.5"*, *"Public-facing pitch on Accenture s37"* — none of these belong on the page. They name internal artefacts the Apex reader hasn't read, has no incentive to read, and treats as Fynd-internal jargon. The SAME claim is fine when it cites a public-facing source the reader recognises (*"Google Cloud Next '26 keynote · 29-Apr-2026"*, *"published live on AJIO.com"*, *"shown at the Reliance Retail Apex review on 16-Apr-2026"*) — public-facing sources are credibility-positive; internal sources are credibility-noise. Rule: if a citation names a Fynd-internal deck, paper, slide number, or section number, it gets stripped at render time. Provenance on those facts moves to YAML metadata (`source_citations:` field) — developer-facing only. Established 2026-05-02 on the AI Agents Catalog rule sweep.
- **Cross-channel scope claims rendered as Live across all channels.** Source posts often phrase reach aspirationally — *"a single enriched source of truth across channels (RD, JioMart, Tira, AJIO, Netmeds, etc.)"* — the *"etc."* and present tense are the giveaway. Pages then render this as fact: *"feeds Reliance Digital · JioMart · Tira · AJIO · Netmeds — same attributes, same vocabulary, same channel-agnostic API."* That's an overclaim if only one channel is actually Live. Two acceptable patterns: (a) change the verb to *"Designed to feed"* / *"Targeted to feed"* — declares scope without asserting present-tense reach; (b) keep the present-tense verb but add an inline per-channel status row: `Live · Tira × Akind &nbsp; · &nbsp; Measured · Netmeds, Reliance Digital &nbsp; · &nbsp; Build · at-scale rollout`. Never assert cross-channel Live without per-channel evidence. (Worked example: `/jcp/cataloging` v0.9.0 §03 Reach card was flagged in audit F2 for the unmodified-source-post overclaim; v0.9.1 added the explicit status row.)

---

## 4. Numbers, dates, and units

This is a register; precision matters more than prose flow.

- **Dates** as `DD-MMM-YYYY`. Hyphens, not slashes. *"30-Apr-2026"* not *"30/4/2026"*.
- **Indian number format** for Indian-context numbers: `₹3.30L Cr`, `15.08 Cr`, `1,06,892`. Use `L` for lakh, `Cr` for crore.
- **Western format** for international/operational metrics: `1.6M`, `380M+`, `2,000+`.
- **Approximations** carry a `~` prefix: *"~50 participants"*. Better than rounding silently.
- **Ratings** as `4.6 / 5` (with spaces around the slash).
- **Percentage** as `83%` not "eighty-three percent".
- **Time ranges** with en-dash or `→`: *"55 → 30 days"*, *"Oct-2025 → Apr-2026"*.

When a number is verified, treat it as canonical and reuse the exact same string across the site. *"68 of 78"* should appear identically on every page that mentions JCP channels — never *"68 out of 78"* in one place and *"68/78"* in another.

---

## 5. Page-element copy patterns

### Hero subhead
**Formula:** *"{lead number}. {scope}. {differentiator}."* Three sentences, max 30 words total.

- ✓ *"600+ Reliance employees trained across six sessions, Oct-2025 to Apr-2026. Five Reliance entities: RIL L&D, RCP, Reliance Jewels, HSEF, Reliance Marketing. All sessions delivered on request from the Reliance side."*
- ✗ *"Discover how Fynd Academy is transforming AI literacy across Reliance through industry-leading training programmes."*

### Stat tile
**Formula:** `<label>` (cap-num style, 2-4 words) + `<number>` (large) + `<context>` (small, optional).

- ✓ Label: *"Active vendors"* · Number: *"1,316"* · Context: *"FY26"*
- ✗ Label: *"Vendor ecosystem reach"* · Number: *"1,316 vendors"* · Context: *"showing strong partner engagement"*

### Card lede
**Formula:** *"{Function} for {audience}. {One concrete capability}. {Number that proves it works}."*

- ✓ *"Vendor co-creation platform · used by Shein. DSD: 5-day turnaround (industry first)."*
- ✗ *"Empowering vendor partnerships through cutting-edge co-creation capabilities."*

### "Why this matters" prose
**One to two short paragraphs — leadership often cuts to one.** Design so paragraph 1 stands alone. If you write two, the second is supporting evidence (names, ratings, a Reliance leader who requested the work), not a continuation of the argument.

Drop the *"platform claim with verifiable numbers"* opener if those numbers already appear in the section's stat tiles — repeating them in prose reads as filler at apex level.

- ✓ *"Demand is Reliance-led. Sessions are requested by Reliance L&D, COOs (Vincent Braganza, Reliance Jewels), and functional teams (HSEF Copilot enablement, Reliance Marketing). Average session rating to date: 4.6 / 5. The Dec-2025 RCP Train-the-Trainer cohort rated 5 / 5 and now serves as a local-trainer base for further rollout."*

### Source line
Below any non-trivial claim, add a `cap-num` source line: *"Source · Q1 2026 Release Compendium · pp. 47-49 · 30-Apr-2026"*. Apex leadership wants to know they could verify this.

### DRI / Owner
- In a footer: `Owner · Raghav Mehra` (single mono line).
- In a card: `DRI: Raghav Mehra` (inline, end of card).
- Never use *"led by"*, *"spearheaded by"*, *"under the leadership of"*.

---

## 6. Reliance-side framing

This site reports to Reliance Apex. The register belongs to Reliance. Frame accordingly:

- **Subject-of-sentence preference.** When something happened, the Reliance entity is usually the subject. *"Reliance Jewels ran a full-day AI workshop with Fynd"* — not *"Fynd delivered a workshop to Reliance Jewels"*.
- **Pull-not-push for everything Academy.** Always note who at Reliance requested the work. *"Requested by Vincent Braganza, COO, Reliance Jewels"* is the canonical phrasing.
- **Outcomes belong to Reliance.** *"₹55L/year saved"* not *"Fynd saved Reliance ₹55L/year"*. The savings accrue to Reliance; the build was supplied.
- **Standard footer line:** *"Built by Fynd. Owned and run by Reliance."* Use as is, do not reword.

### When to name a "Lead" or "DRI" inside a section subhead

Naming an individual is high-signal — and high-cost when wrong. Use these tests before adding a `Lead: <name>` line inside a deep-dive subhead (not the page-level DRI footer line, which is the standard convention):

- **Yes, name them when:** the named person is on the Reliance side and asked for the work (e.g. *"Requested by Vincent Braganza, COO, Reliance Jewels"*), OR the named person is the externally-cited author of a memo the page is summarising (the memo's author signs the source).
- **No, don't name them when:** the named person is a Fynd engineer / IC who shipped the work. The page shows what shipped, not who shipped it. The footer can carry the page-level DRI; the section subhead should not. Naming a Fynd IC inside a section reads as Fynd self-attribution at exec level even when factually correct. (Worked example: `/jcp/` v0.7 dropped *"Lead: Vidit Kumar Gupta"* from the Vertex Search subhead in feedback round 4 — the lead is a Fynd IC, the named attribution wasn't earning anything for an Apex reader.)

---

## 7. Vocabulary

### Use
- British English: *organisation, capitalise, prioritise, behaviour, defence*. Match the rest of the site.
- Reliance entity names exactly: *RIL, RRVL, RRL, RBL, RCPL, JPL, RCP, HSEF, JioMart, AJIO, Tira, Reliance Trends, Reliance Jewels, Smart Bazaar*. Case and spacing matter.
- Fynd platform names exactly: *JCP, UCP, Impetus, Granary, PixelBin, Boltic, Ratl, Kaily, Fynd Horizon, AutRi, GMetri, IntelliVerse, NextWave, PulsePoint, InstaDesk, Cortex*.
- Operating verbs: *built, ships, runs, deployed, processed, replaces, unifies, dispatches*.
- Quantitative qualifiers: *daily, peak, FY26, YoY, on-platform, in-production, live*.

### Do not use
- Adjective inflators: *transformative, revolutionary, game-changing, next-generation, cutting-edge, world-class, best-in-class, leading, premier, innovative, robust*.
- Hedge words: *perhaps, may, could potentially, arguably, it appears that*.
- Filler verbs: *empowers, enables, unlocks, drives, facilitates, leverages, harnesses*. Canonical substitutes when the source-post wording is one of these:

  | Banned verb | Use instead | When to apply |
  |---|---|---|
  | unlocks | **delivers · produces · changes** (or just state the outcome) | *"What this unlocks"* → *"What this delivers"* / *"What this changes"*. (Worked example: `/jcp/cataloging` v0.9.0→v0.9.1 audit F1.) |
  | empowers | **lets · gives** (with the actual verb the user does) | *"Empowers buyers to approve POs from mobile"* → *"Lets buyers approve POs from mobile"*. |
  | enables | **lets · supports · runs** (or drop entirely if the verb is already in the next clause) | *"Enables real-time inventory sync"* → *"Syncs inventory in real time"*. |
  | drives | **produces · increases · raises** (with the metric) | *"Drives conversion"* → *"Lifts conversion 3.5×"* (with the number). |
  | facilitates | **runs · handles · automates** | *"Facilitates order routing"* → *"Routes orders automatically"*. |
  | leverages | **uses · runs on** | *"Leverages Gemini multimodal"* → *"Uses Gemini multimodal"* / *"Runs on Gemini multimodal"*. |
  | harnesses | **uses · taps** | *"Harnesses the Reliance ecosystem"* → *"Uses the Reliance ecosystem"*. |
- Trailing connectors: *moreover, furthermore, additionally, in addition, importantly*.
- Fluffy phrases: *at the end of the day, in today's fast-paced world, in a competitive landscape*.
- Marketing closers: *the future is now, ready for what's next, tomorrow, today*.
- Emojis. Ever.
- Exclamation marks. Ever.

### Engineering jargon — translate at exec read level

Apex leadership doesn't run the system. Words that are precise for engineers read as opaque to a CXO. **Default rule: where a term carries the same information in plain English, prefer the plain term.** Where the technical term is genuinely load-bearing (e.g., "Databricks" naming the actual product), keep it but pair with a verb the reader recognises ("ML pipelines on Databricks · 48M-row daily refresh" not "ML pipelines deployed against the Databricks cluster · 48M-row hot table").

| Engineering term | Exec-read substitute | Notes |
|---|---|---|
| routes / UI routes | screens · operator screens · pages | "5 of 37 screens running on live data" reads cleanly. |
| endpoints / API endpoints | data services · live integrations · data feeds | "33 data services live" or just drop — surfaced as a count it rarely earns its place in a hero tile. |
| UAT tables · DB tables | data tables · live data | Drop entirely if the count isn't load-bearing. |
| scaffolded · stubbed | in build · in design | "27 screens in build" not "27 routes scaffolded". |
| in production · prod deploys · production-grade | live · running · daily updates · battle-tested | `production` is engineering shorthand for "running on real users / real data". To Apex it sounds like the system is being demoed somewhere else. Use `live` (matches the pill convention) or `running today`. "Daily prod deploys" → "daily updates". "Foundation is production-grade" → "Foundation is live" or "battle-tested". |
| schema · ORM · multi-tenant backend | foundation · platform · production-grade | Compress 2-3 engineering nouns into one exec word. |
| IRM · IP whitelisting · ODBC · RDIP | access provisioning · data pipeline · integration | OK to use the precise term *once* with the plain term in parens — "SAP integration · IRM whitelisting (network access)". After the first mention, use the plain version. |
| SSH tunnel · Redis · RBAC | secure · cached · permissioned | Internal-architecture terms rarely belong on an Apex page at all; if they do, use one-word descriptors. |
| latency · throughput · QPS | speed · volume · peak load | "1.6M peak orders/day" not "QPS of 18.5". |
| webhook · cron · poll | scheduled · triggered · automated | |
| LLM · embedding · RAG · vector store | AI model · retrieval · search index | Keep the plain term unless the audience is technical (research subpages can use the precise terms). |

**Where execs CAN handle the technical word**: deep-dive sections that have already established the frame. By the time a reader reaches §03 Architecture or §04 Command Centre deep-dive, "data services" is fine to elide back into "endpoints" because the surrounding cards make the term unambiguous. The hero, status strip, and stat tiles are where the rule bites hardest.

**Where the technical word is the brand**: keep it. "Databricks", "SAP", "Cortex" are product names — never paraphrase. "Power BI" is a product, "dashboards" is the plain term — use both: "dashboards (Power BI)".

---

## 8. Worked examples (drawn from this site)

### Example 1 — Hero subhead

**Wrong (marketing voice):**
> *"How Reliance learns AI. 600+ people trained in 7 months across L&D, business COOs, and functional teams — pulled in by request, not pushed by Fynd, taught on the same platforms they'll use the next morning."*

**Right (apex-readable):**
> *"600+ Reliance employees trained across six sessions, Oct-2025 to Apr-2026. Five Reliance entities: RIL L&D, RCP, Reliance Jewels, HSEF, Reliance Marketing. All sessions delivered on request from the Reliance side."*

The wrong version uses metaphor ("pulled in by request"), embellishment ("the next morning"), and a quasi-rhetorical opener ("How Reliance learns AI"). The right version states only verifiable facts in scannable order: number, scope, names, demand signal.

### Example 2 — "Why this matters" prose

**Wrong (essay voice):**
> *"Adoption is not a feature you ship. It's a habit you build. The register lists big platform numbers — every one of those numbers is a Reliance employee choosing to use a Fynd-built tool instead of the way they did the job last year. Academy is the room where that choice happens."*

**Right (register voice):**
> *"Platform adoption depends on trained users. The register reports 2,000+ users on Impetus, 1,605 of 1,926 stores on PulsePoint, and ~7,000 daily UCP-NPS responses. Academy is the channel by which Reliance teams move from awareness to working use."*
>
> *"Demand is Reliance-led. Sessions are requested by Reliance L&D, COOs (Vincent Braganza, Reliance Jewels), and functional teams (HSEF Copilot enablement, Reliance Marketing). Average session rating to date: 4.6 / 5."*

The wrong version is a Farooq-essay. It would land on the wrong site. The right version names verifiable platform numbers in para 1 and verifiable demand signals (with names) in para 2.

### Example 3 — Card body

**Wrong:**
> *"Strong interest in integrating Claude Cowork into day-to-day workflow."*

**Right:**
> *"Internal Fynd run-through scheduled for the following week."* (if true)

Or simply omit the line. *"Strong interest"* is unverifiable; a booked follow-up is verifiable.

### Example 4 — Stat tile

**Wrong:**
- Label: *"Industry-leading platform reach"*
- Number: *"68 channels"*
- Context: *"and growing fast"*

**Right:**
- Label: *"Channels Live"*
- Number: *"68"*
- Context: *"+5 Pilot · +5 Build · 78 total"*

---

## 9. Pre-publish checklist

Before any user-facing string ships, run it past these:

- [ ] Can I point at the source for every number?
- [ ] Are the dates in `DD-MMM-YYYY` format?
- [ ] Are Indian numbers in `L Cr` format and Western in `M / K`?
- [ ] Does it open with the most important number, name, or fact?
- [ ] Is it under 30 words for a hero subhead, under 15 words for a card lede, under 60 words for a "why this matters" paragraph?
- [ ] Is every adjective doing real work? (If you removed it, would the meaning change?)
- [ ] Are Reliance names spelled and cased correctly? (`RRL` not `RIL` for Reliance Retail counterparts; `RIL` is the parent group.)
- [ ] Does any sentence sound like a Fynd brochure? If yes, rewrite.
- [ ] If a Reliance leader requested or owns the thing, are they named?
- [ ] No emojis, no exclamation marks?
- [ ] Hero stat tiles read in plain English — no `routes`, `endpoints`, `UAT tables`, or other engineering jargon? (See §3 banned constructions and §7 jargon-translation table.)
- [ ] Page does NOT carry an Author / Date / Version line in the hero?
- [ ] Footer is the single copyright line — no Owner / version line?

---

## 10. When in doubt

When unsure between two phrasings, choose the one that:

1. **Names a name** over the one that does not.
2. **Cites a number** over the one that uses an adjective.
3. **States a date** over *"recently"* or *"now"*.
4. **Reports** what happened over **claims** what it means.
5. **Is shorter.**

If the user provides draft copy, rewrite it through these ten sections. If the user provides a topic or a card brief, draft the copy directly in this register.
