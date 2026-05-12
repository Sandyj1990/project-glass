---
name: website-section-authoring
description: End-to-end authoring playbook for new sections of the Fynd × Reliance Retail register at reliance-retail-fynd.vercel.app. Use when adding a new top-level route (e.g., /fynd-academy, /granary, /jcp/<sub>) — covers raw collection, spec, data, assets, build, nav wiring, and verify. Pairs with website-tone-of-voice (which governs copy register).
user_invocable: true
---

# Website Section Authoring

The playbook for adding a new section to the Fynd × Reliance Retail register. Codifies the same lifecycle Impetus and Fynd Academy followed, so every future section ships through the same gates with the same artifacts in the same paths.

This skill governs the **workflow**. Copy register is governed by `website-tone-of-voice` — invoke it for every user-facing string.

---

## 1. The lifecycle

Seven stages, 0 to 6. Each stage produces a named artifact at a known path. Skip nothing.

```
0 · raw           docs/<section>-compilation/      (source PDFs, decks, descriptions, images)
1 · spec          docs/<section>-spec.md           (translates raw → page structure)
2 · data          data/<section>/<slug>.yaml × N   (one per sub-page; verbatim from source)
3 · assets        assets/<section>/<slug>/         (images, PDFs, processed for web)
4 · build         tools/build_<section>.py         (reads data/+assets/, emits HTML)
5 · nav           edits to home, mega-menu, etc.   (see references/nav-wire-checklist.md)
6 · verify        local server + checklist         (see §9)
```

**Two shapes a section can take:**

- **Single-page section** (e.g., `/fynd-academy/`). Stage 2 = one YAML; Stage 4 may be a hand-authored `index.html` instead of a renderer (skippable for ~6 cards or fewer).
- **Multi-page section** (e.g., `/impetus/` with 15 sub-platforms). Stage 2 = N YAMLs; Stage 4 = renderer always.

When in doubt about the cutoff: **6 sub-pages or fewer → hand-author; 7+ → write a renderer.**

**Two modes the lifecycle runs in:**

- **New section** — first time a route exists. All seven stages from scratch. Use the full `references/spec-template.md`.
- **Update / restructure** — page already lives at the route, source material has shifted (new release notes, a deck arrived, scope changed). The lifecycle still runs but the spec is *lighter*: open with §0 "what's changing and why", and frame §3 page-structure as a diff (Add / Keep / Remove / Renumber) instead of an empty scaffold. Skip §1 audience and §2 source inventory if neither has changed. Reference: `docs/hirefirst-spec.md` is the canonical update spec.

---

## 2. Folder conventions

Every section uses these exact paths. Do not vary the names.

| Stage | Path | Notes |
|---|---|---|
| 0 raw | `docs/<section>-compilation/` | One folder. Sub-folders by month or by source if helpful. Never tracked in git for files >5MB; rely on the spec to describe what's there. |
| 1 spec | `docs/<section>-spec.md` | Single file. Filename matches section slug. |
| 2 data | `data/<section>/<slug>.yaml` | One YAML per sub-page (or one per logical entity for single-page sections). |
| 3 assets · web | `assets/<section>/<slug>/` | Web-ready images and PDFs. Naming: `cover.jpg`, `01-<descriptor>.jpg`, `<doc>.pdf`. |
| 3 assets · GCS mirror | `gs://impetus-socialpilot/rrl-portfolio/assets/<section>/<slug>/` | For large or numerous assets. Public URLs at `https://socialassets.impetusz0.de/rrl-portfolio/assets/<section>/<slug>/<file>`. |
| 4 build | `tools/build_<section>.py` | Reads `data/<section>/`, writes to `<section>/<slug>/index.html`. See `references/build-script-skeleton.py`. |
| 5 output | `<section>/index.html` + `<section>/<slug>/index.html` | One index per section, one page per data file. Vercel `cleanUrls: true` handles trailing-slash. |

---

## 3. Stage 0 · Raw collection

**Goal:** get all source material into one folder where the spec can reference it.

- Land everything under `docs/<section>-compilation/`. Use sub-folders if it helps (`oct-nov-2025/`, `accenture-deck/`, etc.).
- Do not rename source files. The spec will reference them by filename.
- If a file is >50MB (e.g. master pptx), note in the spec that it'll be converted in Stage 3, not hosted as-is.
- If raw material is in Drive/Slack/elsewhere, copy it locally first. The site cannot depend on external links the reviewer doesn't have access to.

**Done when:** every source you'll cite in the spec is sitting under the compilation folder.

---

## 4. Stage 1 · Spec

**Goal:** translate raw material into a written plan for the page(s).

Use `references/spec-template.md` as the scaffold. Every spec opens with the same header block (status, owner, route, source content, narrative anchor) and the same numbered sections.

**Mandatory sections:**
1. Why this page exists — audience, gap to close, narrative anchor (cite the cover letter or Apex deck this section answers)
2. Source inventory — table of source files + key facts derivable
3. Page structure — section-by-section layout (§0 hero → §N) with copy formulas
4. Data model — YAML schema with example
5. Asset pipeline — how raw images/docs become web-ready
6. Navigation wiring — which routes need editing (defer to `references/nav-wire-checklist.md`)
7. Build / verify — local-server steps
8. Phased delivery — P1, P2, … with hour estimates
9. Decisions — locked answers to open questions (use AskUserQuestion to resolve before drafting)
10. Out of scope — explicit list of what's deferred

**Audience reminder.** Open Section 1 with: *"Audience. RIL Apex leadership (MM Sir level)…"* — sets the register for everything downstream.

**Resolve open questions early.** Use AskUserQuestion before drafting copy. Decisions become §9 of the spec. Do not ship with open questions in the spec itself.

**Vision-vs-live honesty rule.** When the source's scope is broader than the page's audience scope (e.g., Orion product deck describes the whole platform but `/hirefirst` is the RIL deployment), every borrowed claim must carry an explicit status pill: `Live` ships today, `Building` is in active dev, `Roadmap` is platform-built but not enabled. The pill is the honesty contract. Don't mix tiers in one sentence without tagging. Resolve "show as live" vs "mark as roadmap" via AskUserQuestion before drafting; the answer becomes a §9 decision.

**Codename / brand-name dual identity.** When a product has both a Fynd-internal codename and a RIL-facing brand name (Orion → HireFirst is the recurring case), the page uses the brand name throughout. Mention the codename only when load-bearing — typically: a one-liner in the hero explaining the relationship, the rebrand-event card if there is one, and source-document filenames. Anywhere else creates reader confusion. Pill qualifiers like `Live · RIL` / `Roadmap · Orion` become noise once the surrounding column header already establishes the frame — strip the suffix.

**No author / version metadata on the page.** The page itself never carries an Author / Date / Version line in the hero, nor an Owner / version line in the footer. Provenance lives in git (commit history, blame, the spec file, the audit JSON) — not on the page. Apex doesn't review version numbers. Specifically:

- **Hero**: no `<strong>Author:</strong> … <strong>Date:</strong> … <strong>Version:</strong> …` block. The crumb + section-label + H1 + subhead is enough to orient the reader.
- **Footer**: only the copyright line (`© YYYY RRVL · Jio Platforms Limited · Fynd · Strict internal circulation only`). Drop the `Owner · {name} · v{version}` line.
- **Nav version pill** (small `v0.X.Y` dot in top-right): keep — it's developer-facing tracking and doesn't compete with content for Apex attention. If pruned register-wide later, prune everywhere together.

If a sibling page still carries the deprecated lines, use `tools/scratch/strip_author_owner.py` to sweep — pattern is well-defined and the script is idempotent.

**Canonical section ordering (default).** The register has converged on a default §3 page-structure that mirrors how an Apex reviewer reads top-to-bottom. Use this ordering unless the page has a *documented* reason to deviate (and that reason becomes a §9 Decision):

| § | Title pattern | Purpose | Notes |
|---|---|---|---|
| 0 | Hero | Eyebrow + H1 + 2-line subhead + status pills + stat tiles + (optional) format-cards strip | Cards strip absorbs short "Where this is live" sections |
| 01 | **Status** *(date)* / **What X is for Reliance** | 3-column Live/Building/Roadmap strip OR Problem/Solution/Impact framing | Picks the lens that earns the page |
| 02 | **What's live** / **Live for RIL today** | Module table with status pills + DRI + anchor outcome | The "running today" beat |
| 03 | **Architecture** *(N layers)* | 4-card layered diagram with status pills | Always positioned 03 — the "how it's built" answer Apex asks once |
| 04 | **Deep dive** (Command Centre / Five intelligence modules / etc.) | Visual-evidence section with screenshots or feature cards | The "show, don't tell" beat |
| 05 | **In flight** / **In development for RIL** | Threads shipping in the next 1-4 weeks with named owners and gating steps | Building pills throughout |
| 06 | **Vision / Roadmap** *(scorecard)* | Honest built-vs-full table OR competitive landscape OR governance — context-broadener | The honesty fulcrum |
| 07 | **Research / Evidence** *(optional)* | Embedded paper, deep PDF, governance doc, or tech-stack section | Use when there's an authored artefact that earns its own section. Last section if used. |

**When this ordering doesn't fit — explicit override patterns:**

- **Skip §07 Research** when the page has no authored research artefact (most pages won't).
- **Drop §06 Vision** when the page is small enough that the honesty contract sits in the §02 module table itself (single-product pages, sub-pages).
- **Replace §03 Architecture with Tech stack** when the page is more about technology choices than layered abstractions.
- **Insert Governance & security** between §05 and §06 when compliance/audit is a load-bearing reader concern (`/hirefirst` does this).
- **Insert Competitive landscape** as the closing section when comparison vs external players is the close (`/hirefirst` does this).
- **Add Built by / Team** as the closing section when the team itself is part of the credibility story (`/hirefirst` does this).
- **Never add a §Sources section.** Provenance lives in inline source eyebrows (e.g. *"Q1 2026 Release Compendium · pp. 47-49"*), figure captions on screenshots, and the spec itself. See `website-tone-of-voice` §3 (rule established 2026-05-02).

**What is NOT in the canonical ordering** (these are page-specific patterns that we've moved away from as standalone sections):

- "Connected platforms" grids (cards linking to sibling tracks) — let the mega-menu and inline links carry these. If you must, lift into a 1-line mention inside the relevant section.
- "Recent Apex engagement" dated logs — register-wide pattern, not page-specific. Use the page itself as the artefact, not a re-list of when it has been seen.
- "Where this is live" 3-format strips — absorb into hero (the `/granary` v0.9.2 precedent).

**How to record an override.** Every deviation from the default ordering goes in the spec's §9 Decisions block as a `D{N} · Section ordering override` entry, with the *why* and the *how to apply*. The `website-page-reviewer` skill checks the spec for these entries and treats undocumented deviations as findings.

**Reference implementations.** `/hirefirst` v0.9 was the first page built on this convention; `/granary` v0.9.2 is the most recent. Both demonstrate the override pattern (HireFirst adds Governance/Tech/Competitive/Built-by; Granary skips them for a leaner page with §07 Research). Read either before writing a new spec.

**Done when:** spec is committed and the user has signed off on the shape.

---

## 5. Stage 2 · Structured data

**Goal:** extract the source content into machine-readable YAML, one file per sub-page.

**Schema norms** (see `references/data-yaml-template.yaml`):

```yaml
# Header (always)
slug: <kebab-case>
title: <Display Name>
status: live | pilot | build
date: 2026-04-07           # primary date, ISO format
source_folder: docs/<section>-compilation/<sub>/   # back-reference
source_citation: "Q1 2026 Release Compendium · pp. 47-49"

# Body fields — vary per section
# (use whatever fields the page template needs; keep field names consistent within a section)
```

**Rules:**
- **Verbatim from source.** Body content is pulled from the compilation folder, not paraphrased. Paraphrasing loses the citation chain.
- **One YAML per sub-page.** Even single-page sections benefit from a YAML per logical entity (Fynd Academy: one per session).
- **Approximations carry `~`.** `~50`, `~40` — never silently round.
- **Dates as ISO** in YAML (`2026-04-07`). The renderer converts to `DD-MMM-YYYY` for display.
- **Asset paths are absolute web paths**, not filesystem paths. `/assets/<section>/<slug>/cover.jpg`, not `assets/...`.

**Done when:** every sub-page has a YAML; every field is sourceable to the compilation folder.

---

## 6. Stage 3 · Asset pipeline

**Goal:** convert raw images, PDFs, and decks into web-hosted, sized-for-web artifacts.

### Images

```bash
# Source: docs/<section>-compilation/<sub>/<original>.jpg
# Target: assets/<section>/<slug>/<descriptor>.jpg

# Resize to max 1600px wide, jpeg q80
# (use Pillow, ImageMagick, or sips on macOS)
sips -Z 1600 -s format jpeg -s formatOptions 80 \
  "<source>.jpg" --out "<target>.jpg"
```

- Normalise filenames: lowercase, hyphenated, no spaces, no Unicode (macOS narrow no-break space U+202F is the usual offender — strip it).
- First/best image becomes `cover.jpg`. Numbered after that: `01-<descriptor>.jpg`.

### PDFs

- Copy as-is if <30MB. Otherwise downsample.
- For training PDFs: extract page 1 as `cover.jpg` for card thumbnails. Use `pdftoppm -r 144 -jpeg -jpegopt quality=80 -f 1 -l 1 <input.pdf> <prefix>`.
  - Output filename varies by version: older `pdftoppm` writes `<prefix>-1.jpg`, newer zero-pads to `<prefix>-01.jpg`. **Use a glob: `<prefix>-*.jpg`** — don't hard-code the suffix.
  - Write the prefix directly into the assets folder (not `/tmp` — see §10).

### Embedded UI screenshots inside text-heavy PDFs

When the PDF is a release-notes / scope-of-work / write-up document — text bullets above and below an embedded admin or storefront screenshot — **do NOT use `pdftoppm`** to render the page. The screenshot will come out illegible because it's surrounded by bullet text the page already shows.

Use `pdfimages` to extract the embedded source images directly:

```bash
pdfimages -j -f 1 -l 45 input.pdf /tmp/imgs/img
# -j = output as JPEG when source is JPEG; PPM otherwise.
# Then convert PPM → JPEG via PIL or sips, and pick the meaningful ones
# (filter by area > 100,000 px to skip logos/icons).
```

Auto-trim residual whitespace via PIL (works because most extracted UIs sit on a white background):

```python
from PIL import Image, ImageChops
im = Image.open(p).convert('RGB')
bg = Image.new('RGB', im.size, (255,255,255))
bbox = ImageChops.difference(im, bg).getbbox()
im.crop(bbox).save(p, 'JPEG', quality=85, optimize=True)
```

For a multi-screenshot PDF with N marquee shots needed, view a sample of the extracted images, pick the cleanest one per area, rename to `<NN>-<area>.jpg`, then upload. Reference: `docs/jcp-reorient-spec.md` §11.4 — switching from `pdftoppm` to `pdfimages -j` was the mid-task fix that made `/jcp/release-notes/` screenshots legible.

### Diagram-only crops (slide image extraction)

When extracting a single diagram from a slide deck (e.g., an architecture diagram), `pdftoppm` of just that page is correct. After extraction, crop in PIL to remove the slide title, presenter logo, page number, etc.:

```python
w, h = im.size
im.crop((0, int(h*0.11), int(w*0.96), h))  # drop top 11% (title) + right 4% (logo)
```

Constrain the displayed `<img>` `max-width` to a sensible upper bound (~1100px) so the diagram doesn't appear over-scaled in a wide container.

### PPTX / large decks

- Preferred: `soffice --headless --convert-to pdf <file>.pptx --outdir <target_dir>`.
- **`soffice` may not be installed.** Check with `which soffice` first. If missing, fall back in this order:
  1. Ask the user to convert manually in Keynote / PowerPoint and drop the PDF in the compilation folder.
  2. Install LibreOffice: `brew install --cask libreoffice` (~600MB, requires user OK).
  3. Use a cloud converter (CloudConvert, ConvertAPI) — only if user-approved.
- Target output <30MB. If output exceeds, downsample images and re-export.
- Never host the original `.pptx` if >50MB.

### GCS mirror

Mirror to GCS when assets exceed 20 files or 100MB total — **or whenever the user requests CDN delivery** (e.g., for any binary >10MB worth offloading from git).

Two-step procedure (always do both — uploading without rewriting paths leaves the page serving local assets):

```bash
# 1. Upload
gsutil -m cp -r assets/<section>/ \
  gs://impetus-socialpilot/rrl-portfolio/assets/<section>/

# 2. Rewrite asset paths in the page from local to CDN
sed -i.bak 's|/assets/<section>/|https://socialassets.impetusz0.de/rrl-portfolio/assets/<section>/|g' \
  <section>/index.html
rm <section>/index.html.bak

# 3. Verify a sample of CDN URLs return 200
for u in <list of representative URLs>; do
  printf "%s  %s\n" "$(curl -s -o /dev/null -w '%{http_code}' "$u")" "$u"
done
```

The published assets folder also stays committed to git (matches Impetus convention — belt + suspenders against CDN outage).

**Small-file-count carve-out (1-3 files).** When you're uploading just a handful of one-off binaries (e.g. two keynote screenshots for a single section update), the `gsutil -m cp -r` whole-folder rsync above is overkill. Use a direct multi-file `cp`:

```bash
# 1. Upload the specific files
gsutil -m cp <file1> <file2> \
  gs://impetus-socialpilot/rrl-portfolio/assets/<page>/<event-or-context>/

# 2. Verify each URL is 200 before rewriting page paths
for u in \
  https://socialassets.impetusz0.de/rrl-portfolio/assets/<page>/<event>/<file1> \
  https://socialassets.impetusz0.de/rrl-portfolio/assets/<page>/<event>/<file2>; do
  printf "%s  %s\n" "$(curl -s -o /dev/null -w '%{http_code}' "$u")" "$u"
done

# 3. Rewrite page paths (use Edit replace_all for 1-3 refs; sed for many)
```

For the small-file case the **local mirror is optional** — if you're CDN-only, delete the local `assets/<page>/` folder you staged for upload so the repo doesn't carry the bytes twice. Make this an explicit decision in the commit message ("CDN-only: removed local copy, rely on socialassets") rather than a silent omission. (Worked example: `/kaily` v0.9.3 Google Cloud Next '26 keynote — 2 screenshots uploaded, local `assets/kaily/` removed; the page references `https://socialassets.impetusz0.de/rrl-portfolio/assets/kaily/google-cloud-next-26/` directly.)

**Cache invalidation when re-uploading the same filename.** The `socialassets.impetusz0.de` CDN serves `cache-control: public, max-age=3600` and **ignores query strings** — `?v=2` does NOT bust the cache. To force a fresh fetch after re-uploading the same filename, use a versioned filename:

```bash
# WRONG: re-uploading 09-payments.jpg after re-cropping leaves the
# cached version live for up to 1 hour, even with explicit Cache-Control
# headers, even with ?v= query params.

# RIGHT: rename the new asset and re-upload as a new filename.
cp 09-payments.jpg 09-payments-v2.jpg
gsutil -h "Cache-Control:public,max-age=3600" -m cp *-v2.jpg \
  gs://impetus-socialpilot/rrl-portfolio/assets/<section>/

# Then sed-rewrite HTML to point to the v2 filename:
sed -i.bak 's|/<section>/09-payments\.jpg|/<section>/09-payments-v2.jpg|g' \
  <section>/index.html
```

Once the version-bumped filename is live, leave the old filename to expire naturally — do not manually delete CDN-hosted assets without explicit user approval (deletion is destructive and other pages may still reference the old URL). Reference: `docs/jcp-reorient-spec.md` §11.4 — the v2/v3 suffix dance was the only way to ship trimmed screenshots after the originals had been served once.

### Image display · in-page lightbox, never new tab

**Convention.** Any product / UI / admin screenshot rendered on a page must be **clickable** and open as an **in-page modal overlay** (lightbox). Not as a `target="_blank"` link to the raw asset, and not as a static `<img>` with no enlargement path. Apex readers expect to click a thumbnail and see the full-size view dimmed against the page they were just reading — opening a new tab to a bare JPG is jarring and breaks the reading flow.

**Wrap every screenshot `<img>` in a `<a class="js-lightbox" href="<asset-url>">`** and drop in the lightbox markup + script once at the end of `<body>`. The handler (a) intercepts plain clicks to open the overlay, (b) preserves cmd/ctrl/shift/middle-click as new-tab fallbacks, (c) closes on overlay click, ESC key, or close button, (d) locks page scroll while open.

**Reusable snippet** — paste before `</body>`. One per page (the script is idempotent at the per-page level since it queries `a.js-lightbox`):

```html
<!-- Lightbox overlay (vanilla JS, no deps) -->
<div id="lightbox" role="dialog" aria-modal="true" aria-label="Screenshot preview" style="display:none; position:fixed; inset:0; z-index:1000; background:rgba(10,10,10,0.92); align-items:center; justify-content:center; padding:32px; cursor:zoom-out;">
  <button type="button" id="lightbox-close" aria-label="Close preview" style="position:absolute; top:20px; right:24px; background:transparent; border:0; color:#fff; font-size:32px; line-height:1; cursor:pointer; padding:8px 12px;">&times;</button>
  <img id="lightbox-img" src="" alt="" style="max-width:100%; max-height:100%; object-fit:contain; box-shadow:0 20px 60px rgba(0,0,0,0.5); cursor:auto;" />
</div>
<script>
(function(){
  var box = document.getElementById('lightbox');
  var img = document.getElementById('lightbox-img');
  var closeBtn = document.getElementById('lightbox-close');
  function open(src, alt){ img.src = src; img.alt = alt || ''; box.style.display = 'flex'; document.body.style.overflow = 'hidden'; }
  function close(){ box.style.display = 'none'; img.removeAttribute('src'); document.body.style.overflow = ''; }
  document.querySelectorAll('a.js-lightbox').forEach(function(a){
    a.addEventListener('click', function(e){
      if(e.metaKey || e.ctrlKey || e.shiftKey || e.button === 1) return;
      e.preventDefault();
      var inner = a.querySelector('img');
      open(a.getAttribute('href'), inner ? inner.getAttribute('alt') : '');
    });
  });
  box.addEventListener('click', function(e){ if(e.target === box || e.target === img) close(); });
  closeBtn.addEventListener('click', close);
  document.addEventListener('keydown', function(e){ if(e.key === 'Escape' && box.style.display === 'flex') close(); });
})();
</script>
```

**Wrapping pattern** — every screenshot `<img>` becomes:

```html
<a href="/assets/<section>/<file>.jpg" target="_blank" rel="noopener" title="Open full-size screenshot" class="js-lightbox">
  <img src="/assets/<section>/<file>.jpg" alt="<descriptive alt>" class="rounded-md border w-full mb-3 hover:opacity-90 transition-opacity" style="border-color: var(--border); max-height: 360px; object-fit: contain; background: #fff; cursor: zoom-in;" />
</a>
```

The `target="_blank" rel="noopener" href` on the `<a>` is the **graceful-degradation fallback** — if JS fails to load the lightbox still has a working new-tab path. The handler hijacks plain clicks; modified clicks still get the fallback behaviour.

**Gotcha · `hidden` attribute vs inline `display:` style.** Do not use `<div hidden style="display:flex; ...">` to toggle the overlay. The browser's user-agent rule `[hidden] { display: none }` *loses* to any inline `display:` declaration, so the box stays permanently visible and the click handler appears to do nothing (the overlay is already up). The fix in the snippet above: omit the `hidden` attribute entirely and toggle `box.style.display` between `'none'` and `'flex'` from JS. Same applies to any future overlays / modals / tooltips on this register — never combine the `hidden` attribute with a non-`none` inline `display` style. (Reference: `/samarth` v0.9.5 — first lightbox impl shipped with `hidden` + `display:flex` and silently swallowed every click; v0.9.6 fixed it.)

**Where this convention applies.** Every page that hosts product / UI screenshots (`/samarth` candidate journey, `/jcp/release-notes/`, `/hirefirst` module deep-dive, `/granary` Command Centre, `/impetus` sub-platform pages, etc.). Pages without screenshots can skip the snippet entirely.

**Done when:** every YAML's asset paths resolve to a real, web-sized file AND every page reference points at a 200-returning URL.

---

## 7. Stage 4 · Build / render

**Goal:** generate `<section>/index.html` and `<section>/<slug>/index.html` from data + assets.

Use `references/build-script-skeleton.py` as the starting point. It includes:
- `topnav()` — the v0.8.4+ shared mega-menu
- `footer()` — the standard footer block
- `page()` — full HTML wrapper with `style.css` and Tailwind CDN
- A `main()` with `--all` and single-slug invocation

**Conventions:**
- Renderer reads `data/<section>/*.yaml`. One file per output page.
- Renderer writes to `<section>/<slug>/index.html`. Vercel handles cleanUrls.
- The section index (`<section>/index.html`) is rendered separately by the same script — usually from a derived list of all YAMLs plus a small section-config YAML.
- All copy strings produced by the renderer must pass the `website-tone-of-voice` checklist. Run them through it.

**Run locally:**

```bash
.venv/bin/python tools/build_<section>.py            # build all pages
.venv/bin/python tools/build_<section>.py <slug>     # build one page
```

**For single-page sections (≤6 sub-pages):** skip the renderer. Hand-author `<section>/index.html` from the YAML. Cheaper than maintaining a 200-line script for a page that changes monthly.

**Done when:** every URL in the spec resolves locally.

---

## 8. Stage 5 · Navigation wiring

**Goal:** make the new section discoverable from every entry point.

A new section needs links in **six places**. The full list with exact line ranges and snippet templates is in `references/nav-wire-checklist.md`. The high-level list:

1. **Home page card** (`index.html`) — wrap or add the section's card with `<a href="/<section>">…</a>`
2. **Top-nav mega-menu · Tracks** — Platform / Vertical / Capability column (whichever the section belongs to)
3. **Top-nav mega-menu · More** — only if the section is a meta-page (Organisation, Culture, IP Catalog)
4. **IP Catalog** (`/catalog`) — add the section as an entry
5. **Footer "Other tracks" lists** on every track page — there are ~12 of these and the lists are duplicated, not shared. Either edit all of them (5 min) or accept that backlinks lag for a release.
6. **Sibling section indexes** — if the new section is mentioned on a sibling page (e.g., Fynd Academy mentioned in `/numbers`), update the sibling.

**Note on duplication.** The top-nav HTML block is repeated on every page (~25 files). When a *new entry* is added to the Tracks/More menus, every page gets stale. Two strategies:
- **Strict:** edit all ~25 files in one commit. Use `grep -rl 'mega-link">Granary' --include='*.html'` to find them.
- **Lazy:** edit home + the new section only. Backlinks lag. OK for v1 of a section nobody links to yet.

**Done when:** the new section is reachable from at least the home page card and the Tracks mega-menu.

---

## 9. Stage 6 · Verify / ship

**Goal:** prove the section works before declaring done.

### Local verify

```bash
python3 -m http.server 8000
# open http://localhost:8000/<section>
```

**Auth gate bypass.** Every page imports `/auth.js` which displays a `Confidential.` overlay. To bypass for local verify, run this once in DevTools console (or via Chrome DevTools MCP `evaluate_script`):

```js
sessionStorage.setItem('fyndrrl_auth_v1', '1'); location.reload();
```

For visual checks, the **Chrome DevTools MCP** is the fastest tool — `new_page` → `evaluate_script` to bypass the gate → `take_screenshot` (full page or viewport) → `list_console_messages` to surface errors.

Walk through:
- [ ] Section index loads
- [ ] All sub-page links resolve (no 404s)
- [ ] Hero stats render with correct numbers
- [ ] All photos load (no broken-image icons)
- [ ] All material download links resolve (PDFs open)
- [ ] Internal cross-links (to other sections) work
- [ ] Footer "Other tracks" includes the new section (if Stage 5 was strict)
- [ ] Mobile viewport renders OK (resize browser to 375px)
- [ ] **Every URL or domain reference in user-facing copy is wrapped in `<a href target="_blank" rel="noopener">`.** Plain `<span class="mono">https://…</span>` for a URL is a fail — readers expect to click. Sweep stat tiles, card body copy, sources section.

### Overlap detection pass

Multi-lens pages (release-note + flow + architecture + governance) routinely double-count the same items. After v1 lands, do a cross-reference pass:

1. List every Live / Building / Roadmap claim in the page (a quick `grep` of pills works).
2. For each claim, note every section it appears in.
3. If a claim shows up in **3+ sections**, it's redundant. Surface to the user with named A/B/C resolution options (e.g., "drop the per-stage cards", "drop the modules section", "compress §02 to a status strip"). Don't unilaterally cut — the user picks the lens that earns its rent.

Reference: `docs/hirefirst-spec.md` §0 + the §08 `drop strategic roadmap` commit show the worked example. The 4-phase strip got cut because every phase duplicated content already in §05 in-dev / §06 governance / §04 module roadmap pills, with no time-binding to redeem it.

### Copy verify

For every user-facing string in the new section:
- [ ] Passed the `website-tone-of-voice` pre-publish checklist (§9 of that skill)
- [ ] Numbers traceable to source folder
- [ ] Names spelled correctly (Vincent Braganza, Brijkishor Singh, etc.)
- [ ] Dates in `DD-MMM-YYYY`
- [ ] No marketing voice, no Fynd self-praise

### Source verify

- [ ] Spec's source inventory still matches what's in `docs/<section>-compilation/`
- [ ] Every YAML's `source_citation` field points at a real page/file
- [ ] No claim on a page that isn't backed by a source line

### Ship

- [ ] Spec status updated to "shipped"
- [ ] Single commit per logical change (don't bundle data + nav + build in one commit)
- [ ] Branch pushed; PR opened if applicable

---

## 10. Common issues to watch for

- **Sandbox `mkdir` denied.** Creating `.claude/skills/<dir>/` requires `dangerouslyDisableSandbox: true`. Same for any path outside the allowed write list.
- **`/tmp` is sandbox-blocked.** Writing to `/tmp/...` silently fails (the next read returns "no such file"). Use `$TMPDIR` (auto-set in sandbox) or write directly into the target assets folder.
- **Bash CWD persists between commands.** A `cd docs/...` in one Bash call carries over. The next call assuming repo-root will fail. Use absolute paths, or reset with `cd /Users/.../reliance-retail-fynd && ...` at the top of each call.
- **Auth.js gate blocks local verify.** Every page loads `/auth.js` which puts up the Confidential overlay. Bypass via DevTools console: `sessionStorage.setItem('fyndrrl_auth_v1', '1')`. See §9.
- **Asset paths with spaces.** Source filenames often have spaces ("WhatsApp Image …"). Always rename in Stage 3. Browsers tolerate `%20` but it complicates everything else.
- **Unicode in filenames.** macOS screenshot filenames use narrow no-break space (U+202F, bytes `e2 80 af`). Detect via `xxd` or Python (`' ' in filename`) and replace before web hosting.
- **PPT > 50MB.** GitHub will warn at 50MB and reject at 100MB. Convert to PDF in Stage 3, never commit the raw pptx.
- **`soffice` not installed.** The skill defaults to LibreOffice for pptx → PDF. Check `which soffice` first; if missing, ask the user to convert manually rather than installing a 600MB package without consent.
- **GCS mirror without path rewrite.** Uploading to GCS but forgetting to `sed`-rewrite the page's asset paths leaves it serving local assets. Always run both steps. See §6 Stage 3 GCS mirror.
- **Mega-menu drift.** When adding a new entry to Tracks/More, the same edit must land in every page's nav block (~25 files). `grep -rl 'mega-link">Granary' --include='*.html'` is your friend. Lazy strategy is acceptable for v1.
- **YAML headcount as int.** `headcount: ~50` is invalid YAML (the `~` parses as null). Use `headcount: "~50"` (string) for approximations.
- **`cleanUrls: true` doesn't strip `index.html`.** A link to `/fynd-academy/index.html` works but should be written as `/fynd-academy` for consistency.
- **Page-1 cover extraction.** `pdftoppm -f 1 -l 1 <pdf> <prefix>` writes either `<prefix>-1.jpg` or `<prefix>-01.jpg` depending on version. Use a glob `<prefix>-*.jpg` to handle both.
- **Tailwind CDN cache.** When iterating on classes, hard-reload (Cmd-Shift-R) or append `?v=N` to the URL. CDN caches aggressively.
- **Renumber tax after section deletes.** When iteration cuts a `§NN` section mid-spec, every later section's *visible label* (`<div class="section-label">NN · …</div>`) AND the HTML comment (`<!-- §NN · … -->`) must shift down. Easy to miss either. Quick check after a delete: `grep -n 'section-label mb-3">[0-9]' <page>/index.html` — the numbers should be a contiguous run.
- **PDF-page screenshots include surrounding bullet text and read as illegible noise at apex grain.** Do not use `pdftoppm` to render whole pages of release-notes / scope-of-work / write-up PDFs as "screenshots". Use `pdfimages -j` to extract the embedded UI image directly. See §6 Stage 3 above.
- **`tools/inject_subnavs.py` TARGETS list is hand-maintained.** Adding a new sub-page to `SUBNAV[track]` does NOT auto-inject the chip into that new page (or sibling pages not in TARGETS). Two fixes after a SUBNAV edit:
  1. Add the new page's path to `TARGETS` so the injector touches it.
  2. If a sibling page is built by a separate script (e.g., `/jcp/channels/` is built by `tools/build_jcp_channels_page.py`), re-run that script — it calls `subnav_html()` inline and won't reflect SUBNAV changes until rebuilt.
- **CDN cache ignores query strings.** Re-uploading `09-payments.jpg` after re-cropping leaves the cached version live for up to 1 hour. `?v=2` does not bypass it. Use a versioned filename (`09-payments-v2.jpg`) and `sed`-rewrite the HTML — see §6 GCS mirror.
- **Decorative arrows on cards that link to the same place as the card body** add no information and break when the URL fallback routes to a homepage. If the whole card is clickable, drop the inline `↗`. If the card body is not clickable, make the URL itself the prominent hyperlink.
- **`<details>`/`<summary>` flex layout with 3 children + `justify-content: space-between` puts the middle child in the middle of available space**, not aligned to the right edge. Use `margin-left: auto` on the right-side text to push it next to the trailing icon. (Reference: `/jcp/release-notes/` accordion alignment fix in feedback round 2.)

---

## 11. Reference implementations

Three canonical examples in this repo. Read them before starting work.

| Section | Shape | Mode | Use as reference for |
|---|---|---|---|
| `/impetus/` | Multi-page (15 sub-platforms), heavy renderer | New | Stage 2 YAML schema, Stage 3 PDF asset extraction (122 screenshots), Stage 4 renderer at scale |
| `/fynd-academy/` | Single-page (6 cards), no renderer | New | Stage 1 lightweight spec, Stage 5 minimum-nav wiring |
| `/hirefirst/` | Single-page (10 sections), no renderer | **Update / restructure** | Update-mode spec (§0 implementation status + §3 page-structure as Add/Keep/Remove diff), vision-vs-live honesty pills (`Live` / `Building` / `Roadmap`), codename-vs-brand-name handling (Orion / HireFirst), interior-page PDF asset extraction (5 module screenshots + 2 architecture diagrams), overlap-detection pass after v1 |

**Spec to copy from:**
- `docs/impetus-restructure-spec.md` — full-fat new section
- `docs/fynd-academy-spec.md` — lightweight new section
- `docs/hirefirst-spec.md` — restructure of an existing section

**Renderer to copy from:** `tools/build_impetus.py`.

---

## 12. Templates in references/

Four files bundled with this skill. Copy and adapt — do not edit in place.

| File | Purpose |
|---|---|
| `references/spec-template.md` | Scaffolded section spec with all 10 mandatory sections |
| `references/data-yaml-template.yaml` | Annotated YAML showing schema norms and required fields |
| `references/build-script-skeleton.py` | Minimal Python renderer with topnav/footer/page helpers |
| `references/nav-wire-checklist.md` | Six-file edit list with exact paths and snippet templates |

---

## 13. Final gate

A section is shippable when:

- [ ] Stages 0-6 all complete
- [ ] Spec §0 (status) shows ✓ for every deliverable
- [ ] Local verify checklist passed (§9 above)
- [ ] All copy strings passed `website-tone-of-voice` pre-publish checklist
- [ ] Single named DRI (Fynd-side) in spec footer line
- [ ] Single named Reliance entity in the page (the section answers a Reliance need)
- [ ] Commits attributed; PR linked

If any box is unchecked, the section is not done. Do not declare ship.
