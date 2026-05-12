# CLAUDE.md

Project memory for AI assistants working on the **Fynd × Reliance Retail register** at `https://reliance-retail-fynd.vercel.app`.

A static internal-circulation site that reports the state of every Fynd-built platform deployed across Reliance Retail. Audience: **RIL Apex leadership (MM Sir level)**.

---

## Read first

1. `.ai/codebase-map.md` — folder structure, page conventions, lifecycle, gotchas. Read this before touching anything you haven't seen before.
2. `.claude/skills/website-tone-of-voice.md` — the canonical copy register. **Read in full** before drafting any user-facing string. Hero subhead ≤30 words, no banned vocab, no `we / our`, no exclamations, dates `DD-MMM-YYYY`, Indian numbers in `L Cr`.
3. `docs/design.md` — the canonical visual register. Tokens, components, spacing, motion, a11y. **Read before any edit that affects more than one page or introduces a new visual pattern.** Single source of truth for colors, font sizes, paddings, border styles, and the sweep deltas to converge to.
4. `.claude/skills/website-section-authoring/SKILL.md` — the workflow for adding a new top-level route (Stages 0-6).
5. `.claude/skills/website-page-reviewer/SKILL.md` — the audit protocol (8 phases, 7 dimensions, scored JSON).
6. `docs/path-to-l4-spec.md` + `data/agents-x-platforms.yaml` — agent ↔ platform deployment registry. Every claim that *"platform X uses agent Y"* anywhere on the site (platform page or agent page) is derived from this single YAML file via `tools/inject_path_to_l4.py`. **Read the spec before editing any platform's §03 Path to L4 section or any agent's "Deployed in" block** — direct edits get reverted on the next sweep. See the *Path to L4 · canonical-source rule* section below.
7. `docs/organisation-workflow.md` + `docs/organisation-spec.md` — the `/organisation` section (4 routes: Overview · Organogram · People Directory · External Commercialization). The workflow doc covers the full lifecycle (sources → build script → output → pages); the spec doc carries the §9 build-round changelog. **Read the workflow before editing anything in `organisation/`, `tools/build_org_data.py`, or `tools/build_roster_delta_pdf.py`.** See the *Org stats · canonical-source rule* section below.

---

## Workflow

- **Branch.** Always work on a feature branch. Never commit or push directly to `master`. PRs go from the feature branch → `master`.
- **Commits.** Use the dot-separated lowercase pattern: `<area> · <thing> · <descriptor>`. Examples: `dark-factory · v2 · factory internals`, `register · footer · drop Owner line`.
- **Spec-first for new sections.** New routes go through Stages 0-6 of `website-section-authoring`. Author `docs/<route>-spec.md` BEFORE the page when possible; backfill if not.
- **Audit before sharing with Apex.** Run `website-page-reviewer` against the live page; resolve HIGH + MEDIUM findings; write the audit JSON to `docs/audits/`.
- **Branch-switch sandbox gotcha.** The Claude Code sandbox protects `.claude/settings.json` and `.claude/skills/*` from writes (incl. `unlink`). If you `git checkout` a branch (or older commit on the same branch) where those paths are absent, git tries to delete them, sandbox refuses silently, files remain on disk as **untracked**, and every subsequent `checkout` / `pull` aborts with `untracked working tree files would be overwritten`. **Recovery:** re-run the blocking command with `dangerouslyDisableSandbox: true` (e.g. `git checkout -f <branch>`) — `-f` then cleanly replaces the orphaned files with the target branch's tracked versions. **Avoidance:** before switching, check that the target ref has `.claude/skills/` in its tree (`git ls-tree <ref> .claude/`); if not, expect the gotcha and pre-disable sandbox for that one command.

---

## Skills (when to invoke)

| Trigger | Invoke |
|---|---|
| User asks to add a new top-level route | `website-section-authoring` |
| User asks to draft / edit any user-facing string | `website-tone-of-voice` |
| User asks to "audit", "review", "check", or "QA" a page | `website-page-reviewer` |
| User asks for a visual / styling / typography / a11y change | Read `docs/design.md` first; edit `style.css` (single-file sweep) — don't introduce per-page hex literals or off-scale font sizes |

The skills live at `.claude/skills/`. Each is `user_invocable: true` — invoke via the `Skill` tool when the user types `/<skill-name>` or when you've identified a clear match.

---

## Local dev

Two servers, chosen by what you're touching. Auth is enforced server-side by `middleware.ts` (per `docs/glass-security-spec.md` §3.1) — the old client-side `auth.js` overlay and its `sessionStorage` bypass are gone.

| Working on… | Use | Gate runs? |
|---|---|---|
| Page content, copy, styles, sweeps, diagram work | `python3 -m http.server 8765` | No |
| Middleware code, challenge page, cookie flow, CSP, headers | `vercel dev` | Yes |

```bash
python3 -m http.server 8765
# open http://localhost:8765/<route>   →  workspace renders, no gate
```

```bash
vercel link                       # one-time, connect this folder to the Vercel project
vercel env pull .env.local        # one-time after env vars exist in Vercel
vercel dev
# open http://localhost:3000/    →  branded challenge appears, enter password,
#                                   cookie set, workspace loads
```

`.env.local` carries `GLASS_PW_HASH` and `GLASS_SIG_SECRET`; it is `.gitignore`d, never commit it.

For visual checks, prefer **Chrome DevTools MCP** over screenshots-via-shell: `new_page` → `take_screenshot` → `list_console_messages`. With `http.server` no auth step is needed; with `vercel dev` you authenticate once and the cookie sticks for the session.

---

## Nav + footer · the canonical-source rule

**Why nav items occasionally disappear:** the `<nav class="topnav">` and `<footer>` blocks are duplicated across ~70 pages. The system has a single source of truth at `tools/site_chrome.py` and a sweep tool at `tools/inject_chrome.py`. Edits made directly to a page's nav HTML get **silently reverted** the next time anyone runs `inject_chrome.py`. That's the disappearance mechanism.

**The rule · always edit `tools/site_chrome.py`, never the nav HTML directly.**

Workflow for any nav / footer change:
1. Edit the menu lists in `tools/site_chrome.py` (`PLATFORMS`, `SPECIAL_PROJECTS`, `AI_NATIVE`, `RECENT_INNOVATIONS`, `MORE_MENU`) or the `topnav()` / `footer()` renderers.
2. Run `python tools/inject_chrome.py --dry` to preview.
3. Run `python tools/inject_chrome.py` to sync all 69 register pages.
4. Verify with `python tools/inject_chrome.py --check` — exits non-zero if any page diverges.

After any commit that touches `<nav>` or `<footer>` HTML on a page, run `python tools/inject_chrome.py --check` before committing. If it reports drift, you bypassed the canonical — go fix `site_chrome.py` and re-sync.

Intentionally excluded by the sweep:
- `tools/` (EXCLUDE_DIRS) — scratch + build scripts
- Files not named `index.html` (e.g., `docs/impetus-index-backup-2026-04-30.html` is a frozen historical snapshot)

---

## Things to NEVER do

- Add a `§Sources` block to any page (always-remove rule, commit `e867725`).
- Add a `Source · …` or `Author · …` inline attribution line. Page-itself-as-artefact.
- Add an `Owner · {name} · v{version}` footer line. Footer is single copyright line only.
- Add a hero `Author / Date / Version` block.
- Use marketing voice. No `transformative`, `world-class`, `cutting-edge`, `game-changing`, `next-generation`, `best-in-class`, `empowers`, `enables`, `unlocks`, `leverages`, `harnesses`. Full list in tone-of-voice §7.
- Use `we` / `our` / first-person plural in user-facing copy.
- Use exclamation marks or emojis in copy or in commits.
- Push directly to `master`. Always go through PR.
- **Edit nav HTML directly on any page.** Always edit `tools/site_chrome.py` and run `python tools/inject_chrome.py`. Direct page edits get silently reverted on the next sync. See the *Nav + footer · the canonical-source rule* section above.
- **Quote org totals from any source other than `organisation/data.json`.** Headcount, on-RRL count, engineering %, project counts, "product builders" % — all of these have a single source of truth: `organisation/data.json`, generated by `tools/build_org_data.py` from `docs/org-notes-compilation/Team List Billed v2.xlsx`. See the *Org stats · canonical source* section below.
- **Restate org-wide totals (1,056 / 707 / 46% / 66%) on a platform page.** Those belong on `/organisation` only. Platform pages quote platform-specific stats (their own headcount, track split, engineering %) and link out to `/organisation` for org-wide context. See the *Platform page · org section · hydration* subsection below.
- **Hardcode an agent → platform deployment claim on any page.** Every "platform X uses agent Y" claim is derived from `data/agents-x-platforms.yaml` and rendered into pages via `tools/inject_path_to_l4.py`. Direct edits to the §03 Path to L4 section on a platform page OR the "Deployed in" block on an agent page get **silently reverted** on the next sweep. See the *Path to L4 · canonical-source rule* section below.
- **Reintroduce a client-side `auth.js` or any DOM-painted gate.** The middleware at `middleware.ts` is the single source of auth. Client-side gates ship the workspace HTML to unauthenticated clients (`curl`, JS-disabled browsers, View Source) and publish the password hash for offline brute-force. Both criticals were the reason auth moved server-side. The `inject_no_auth.py --check` build gate fails the deploy on any reintroduction. See `docs/glass-security-spec.md` §3.1 + §3.2.
- **Author a new register page without `<section>` direct children of `<body>`** (or skip the present.* wiring). Every register page must be presentable: structure the body as a sequence of top-level `<section>` blocks (each becomes one slide) AND load `/present.css` + `/present.js`. The Vercel build gate fails the deploy if either is missing. See the *Presentation Mode · canonical-source rule* section below.

---

## Org stats · the canonical-source rule

**The roster (`organisation/data.json`) is the single source of truth for every org-wide number on the site** — total headcount, on-RRL count, engineering %, "product builders" %, per-project totals (JCP / Impetus / Granary / Infrastructure / etc.). Decks, MDA letters, Keka snapshots, and the previous v1 xlsx are not authoritative — they're sources we extract from but the live number always comes back to `data.json`.

**Why this rule exists:** the homepage `§09` quoted `1,100+ people · 68 % product builders` for months while `/organisation` quoted `1,056 · 46 % engineering`. Apex saw two different totals on the same site. The mismatch came from someone hardcoding rounded numbers from an older deck instead of reading `data.json`.

**The rule · always derive from `data.json`, never hardcode from external sources.**

| If you need to quote… | Read from |
|---|---|
| Total people | `data.meta.totals.rows` (currently 1,056) |
| On RRL count | `data.meta.totals.onRRL` (currently 707) |
| Engineering % | `data.meta.totals.engineeringPct` (currently 46) |
| Product Builders % | `data.meta.totals.productBuildersPct` (currently 66 — broad definition: Engineering + Product + Design + Data Analysis/Science/Annotator + QA + Research + Design Research + Fashion Design = 699 / 1,056) |
| Per-project headcount | `data.pivot[i].total` |
| Per-track headcount | `data.pivot[i].tracks[j].count` |
| Department distribution | derive from `data.rows[].department` |

**Workflow when an org-stat needs to land on a page:**
1. Re-derive the number from `organisation/data.json` (or run `tools/build_org_data.py` if the xlsx changed).
2. Edit the page.
3. After any change to the xlsx or `tools/build_org_data.py`, sweep the site for stale quotes: `grep -rnE --include='*.html' "1,?0[0-9]{2}|\\b[6-9][0-9]\\s*%\\s*product" .` and reconcile.

The `/organisation` page itself is data-driven — it hydrates hero stats from `data.json` at load — so it is automatically consistent. **Other pages must be manually reconciled** because they bake numbers into their HTML at write-time.

**Acceptable exceptions:** approximations explicitly marked as such (e.g., "~ 200 in 2014" — historical rounding) or non-roster metrics (e.g., the 78% AI-daily-use stat from the AI Assessment, the 7,989 hrs/wk Claude usage stat). When in doubt, prefer the precise roster number over a rounded one.

### Platform page · org section · hydration

Any platform page (`/jcp`, `/impetus`, `/granary`, `/ucp`, `/retail-vista`, `/boltic`, etc.) that carries a §People-equivalent section follows this hydration protocol. The protocol exists so that 22 platform pages don't drift independently each time the xlsx changes.

**Two rules:**

1. **Don't restate org-wide totals.** No `1,056 people · 707 on RRL · 46% engineering · 66% product builders` on a platform page. Those are `/organisation`'s job. Platform pages link to `/organisation` for that context.
2. **Quote only platform-specific stats** derived from `organisation/data.json` filtered to that project. Use the helper script — never read numbers off a deck or memory.

**Helper · single command, paste-ready output:**
```bash
python tools/derive_platform_org.py <project>     # case-insensitive
# e.g.
python tools/derive_platform_org.py jcp
python tools/derive_platform_org.py granary
```
Output: total · dedicated/shared track split · engineering % · product builders % · location mix · billing mix · per-track bar list with route classification. Copy the relevant numbers into the page.

**What each platform page may quote (all platform-scoped, not org-wide):**

| What | Source field |
|---|---|
| Total | `pivot[project].total` |
| Track count + dedicated/shared split | `pivot[project].tracks[]` (dedicated = `trackRoute` matches platform route prefix or is null; else shared with adjacent platform) |
| Engineering % | filter `rows[project=PROJ]`, count `department == "Engineering"` |
| Product builders % | filter `rows[project=PROJ]`, count `department in {Engineering, Product, Design, Data Annotator, QA, Research, Design Research, Data Analysis, Data Science, Fashion Design}` |
| Location mix | filter `rows[project=PROJ]`, group by `.location` |
| Billing mix | filter `rows[project=PROJ]`, group by `.billing` (RRL / Fynd / RBL / RCPL) |

**Re-sync trigger.** After any rebuild of `organisation/data.json` (i.e., after `tools/build_org_data.py` runs against a new xlsx), re-run `derive_platform_org.py` for each platform that has a §People section and reconcile any drift in track counts, names, percentages.

**Reference implementation:** `/jcp` §04 People — uses the canonical 2-column layout (tracks bar chart on left, named accountability on right) and quotes only JCP-specific numbers.

---

## Path to L4 · the canonical-source rule

**The agent ↔ platform mapping has a single source of truth: `data/agents-x-platforms.yaml`** — derived by the `website-page-reviewer` audit + the home-redesign work. Every page that asserts *"agent X is deployed in platform Y"* is rendered from this registry. Hand-edits to either side get silently reverted by the next sweep.

**Why this rule exists:** before the registry, an Apex reader on a platform page could not answer *"how does this become L4 agentic"* — the mapping lived only on the `/agents/` directory side, not back on the platform pages. Adding the platform-side surfacing without a registry would have meant maintaining two sides by hand, and they would drift the moment an agent's state or unlocks line changed.

**The rule · always edit `data/agents-x-platforms.yaml`, never the rendered HTML.**

Workflow for any agent ↔ platform change:
1. Edit `data/agents-x-platforms.yaml` (add a new agent, change a state pill, swap an "unlocks" string, add a new deployment).
2. Run `python tools/inject_path_to_l4.py --dry` to preview what changes.
3. Run `python tools/inject_path_to_l4.py` to sync both sides — the §03 Path to L4 section on each affected platform page AND the "Deployed in" block on each affected agent page.
4. Verify with `python tools/inject_path_to_l4.py --check` — exits non-zero if any required marker is missing or either side drifts.

After any commit that touches a §03 Path to L4 section OR a "Deployed in" block, run `python tools/inject_path_to_l4.py --check` before committing. If it reports drift, you bypassed the canonical — go fix `agents-x-platforms.yaml` and re-sync.

**5 platforms in scope** (resolved · `path-to-l4-spec.md` §2): Impetus · JCP · UCP · Granary · RetailVista. The other 17 platforms get **no** §03 Path to L4 section — their absence is itself the signal of where the agent program hasn't yet landed.

**6 agents in the registry** (the canonical 6 from `/agents/`): Cortex Planning · Trend-to-Design · Category Intelligence · AI Cataloging · Marketing · Retail Vista.

**Markers · the injection points.** Each platform page in scope must carry `<!-- PATH-TO-L4-START -->` … `<!-- PATH-TO-L4-END -->` at the §03 slot (right after §02 What's live). Each agent page must carry `<!-- DEPLOYED-IN-START -->` … `<!-- DEPLOYED-IN-END -->`. The sweep tool replaces only what's between these markers — surrounding HTML is untouched.

---

## Presentation Mode · the canonical-source rule

**Every register page is a deck.** Pressing `P` (or clicking the floating Present pill bottom-right) opens the page as a slide deck — each `<section>` direct child of `<body>` becomes one slide. The feature is implemented by `/present.js` + `/present.css` and wired into every page's `<head>` by `tools/inject_present.py`.

**Why this rule exists:** the deck only works if (a) the page imports the present.* assets AND (b) it has at least one top-level `<section>`. Without both, the Present button becomes a silent no-op — the kind of breakage that ships unnoticed because nothing throws an error. The Vercel build gate prevents this.

**The rule · two invariants every register page must honor.**

1. **Wiring · `/present.css` and `/present.js` must be loaded in `<head>`** right after `/style.css`. Always inject via the sweep, never edit the link tags by hand.
2. **Structure · `<body>` must contain at least one top-level `<section>` element.** Each section becomes a slide; the slide title is derived from `.section-label`, then `<h1>`, then `<h2>`. Sections nested inside wrapper divs are not slides.

**Workflow when adding a new register page:**
1. Author the page following the `<section>`-per-§ convention (the `website-section-authoring` skill already enforces this — §0 Hero · §01 … · §NN Sources are all top-level `<section>` blocks).
2. Run `python tools/inject_present.py` to wire the new page (the sweep finds it via the `/style.css` import anchor).
3. Verify with `python tools/inject_present.py --check` — exits non-zero on either DRIFT (missing wiring) or NO-SLIDES (zero top-level `<section>` elements).

**Build gate.** `vercel.json > buildCommand` runs `inject_present.py --check && inject_chrome.py --check && inject_path_to_l4.py --check && inject_no_auth.py --check` on every Vercel deploy. A failure on any of the four blocks the deploy. This is the canonical safety net — pre-commit hooks are local-only and skippable; the build gate is not.

**Excluded by the sweep:** files in `tools/`, `.venv/`, `node_modules/`, `.git/`, `.vercel/`, and any `index.html` that doesn't import `/style.css` (asset folders, partial fragments, generated artifacts).

---

## Things to ALWAYS check

- Section labels are a contiguous run: `grep -n 'section-label mb-3">[0-9]' <page>/index.html` — must be `01 02 03 …` no skips.
- Mega-menu changes sweep all ~70 pages: `grep -l 'mega-link">…' --include='*.html' -r .`
- Image asset paths after CDN upload: `sed`-rewrite local paths to CDN URLs and verify `200` for each.
- Date format: `DD-MMM-YYYY` (e.g., `30-Apr-2026`) in user-facing copy; ISO in YAML.
- Reliance entity casing: `RIL`, `RRVL`, `RRL`, `RBL`, `RCPL`, `JPL`, `RCP`, `HSEF`, `JioMart`, `AJIO`, `Tira`, `Reliance Trends`, `Reliance Jewels`, `Smart Bazaar`, `FreshPik`. Never lowercase, never abbreviate beyond this list.
- Hero subhead word count: max 30 words.
- After any nav / footer edit: `python tools/inject_chrome.py --check` must exit 0.
- After any visual / CSS edit: confirm the change uses tokens from `style.css :root` and on-scale font sizes (`docs/design.md` §1.2). No new hex literals on pages; no `text-[Npx]` Tailwind arbitrary sizes outside the documented scale.
- After any rebuild of `organisation/data.json`: sweep the site for stale org-totals (per the *Org stats · canonical source* section above) and reconcile any drift before committing.
- After any edit to `data/agents-x-platforms.yaml` OR any §03 Path to L4 / "Deployed in" block: `python tools/inject_path_to_l4.py --check` must exit 0.
- After authoring any new `index.html`: `python tools/inject_present.py --check` must exit 0 — confirms both the present.* wiring and the body-has-`<section>` invariants. The Vercel build runs this same check and fails the deploy on drift.
- After any edit to `middleware.ts`, `lib/auth.ts`, `lib/challenge.ts`, or any header in `vercel.json`: run `vercel dev` then `curl -sI http://localhost:3000/` and confirm the full security-header set + `401` from the no-cookie state. After cookie auth, `curl -sI -H "Cookie: glass_v1=<value>" http://localhost:3000/` returns `200` with the same headers.
- After any new HTML page: `python tools/inject_no_auth.py --check` must exit 0 — confirms no client-side `auth.js` reference was reintroduced. The Vercel build runs this same check.

---

## Memory hygiene

You have a persistent file-based memory at `~/.claude/projects/-Users-kushanshah-Documents-work-reliance-retail-fynd/memory/`. Use it for user preferences, project state that doesn't live in code, and feedback that should survive future conversations. Don't duplicate things that this CLAUDE.md or `.ai/codebase-map.md` already cover.
