# <Section Name> · Spec

**Status:** v0.1 · YYYY-MM-DD · draft for sign-off
**Owner:** <Author Name>
**Route:** `/<section-slug>/` (new | existing)
**Source content:** `docs/<section>-compilation/`
**Narrative anchor:** `docs/<cover-letter-or-deck>.md` — quote the specific ask this section answers (e.g., *"adoption with dedicated people involved"*). One sentence on why this section belongs in the register.
**Inherits from:** `docs/website-orientation-spec.md` · §3 page template · register copy via `website-tone-of-voice` skill

---

## 1. Why this page exists

**Audience.** RIL Apex leadership (MM Sir level) reviewing the register at `reliance-retail-fynd.vercel.app`. Copy must be apex-readable: factual, scannable, no marketing voice, no Fynd self-praise, names where they matter, claims that survive challenge.

**Gap to close.** What's missing from the register today that this section adds. Cite the specific page/card/link that points nowhere or omits this content.

**Why this belongs in the apex register.** Three to five lines. Tie back to the cover-letter ask. Name the unique angle this section covers that no other section does.

---

## 2. Source inventory

Table of every source file you'll cite, with key facts derivable from each.

| Source | Type | Path | Key facts |
|---|---|---|---|
| <descriptor> | PDF / pptx / md / images | `docs/<section>-compilation/<sub>/<file>` | one-line summary of what's there |

**Aggregate KPIs derivable from source:**
- Bullet list of the headline numbers this section can claim
- Each number must trace back to a row in the table above

---

## 3. Page structure

Section-by-section layout. Mirror the Impetus / Fynd Academy convention: `§0 Hero → §01 → §02 → … → §0N → Footer`. Do **not** add a §Sources section — see `website-tone-of-voice` §3 (rule established 2026-05-02). Provenance lives in inline source eyebrows, figure captions, and the spec itself.

For each section, specify:
- The H2 / section label
- The copy formula (number + scope + qualifier; or named formula from `website-tone-of-voice` §5)
- The component used (stat tile, card grid, prose, timeline)
- A worked example of the copy

### §0 · Eyebrow + Hero
- Crumb: `Home / <Section>`
- Section label: `<TRACK NN OR FRONTIER NN> · <SECTION SLUG IN CAPS> · LIVE`
- H1: **<Section Name>.**
- Subhead: *"<lead number>. <scope>. <differentiator>."* — under 30 words. Run through `website-tone-of-voice`.
- Stat tiles (4-8): label + number + context

### §01 · <First content section>
- Component: <card grid | stat strip | prose | timeline>
- Copy formula: <which one from website-tone-of-voice §5>
- Source: <which row(s) of §2 power this>

### §02 · …

### Footer
Standard footer. `Owner · <Name>` mono line. Last verified date.

---

## 4. Data model

Path: `data/<section>/<slug>.yaml` (one per sub-page; or one per logical entity for single-page sections).

Schema (extend `references/data-yaml-template.yaml`):

```yaml
slug: <kebab>
title: <Display>
status: live | pilot | build
date: YYYY-MM-DD
source_folder: docs/<section>-compilation/<sub>/
source_citation: "<verbatim citation>"

# Section-specific body fields below
# (Keep names consistent across all sub-pages of this section)
```

---

## 5. Asset pipeline

Source `docs/<section>-compilation/` → published `assets/<section>/`.

### Pass A · images
- Walk source folders, copy .jpg/.jpeg/.png to `assets/<section>/<slug>/`
- Normalise names (strip Unicode, lowercase, hyphenate)
- Resize to max 1600px wide, jpeg q80
- First/best image → `cover.jpg`

### Pass B · documents
- Copy PDFs as-is if <30MB, else downsample
- Convert pptx → slim PDF via `soffice --headless --convert-to pdf`
- Extract first page of training PDFs as `cover.jpg` for thumbnails

### GCS mirror
If asset count >20 or total >100MB:
```bash
gsutil -m cp -r assets/<section>/ gs://impetus-socialpilot/rrl-portfolio/assets/<section>/
```

---

## 6. Navigation wiring

See `references/nav-wire-checklist.md` for the six-file list. Tick off:
- [ ] Home page card linked
- [ ] Top-nav Tracks mega-menu (Platform | Vertical | Capability column)
- [ ] IP Catalog entry
- [ ] Footer "Other tracks" lists (strict | lazy — choose)
- [ ] Sibling section indexes that mention this one
- [ ] (If meta-page) More mega-menu

---

## 7. Build / verify

```bash
# Build
.venv/bin/python tools/build_<section>.py

# Verify
python3 -m http.server 8000
# Walk the §9 verify checklist from website-section-authoring skill
```

---

## 8. Phased delivery

| Phase | Scope | Time |
|---|---|---|
| **P1** | Spec + data YAMLs + assets | ~X hr |
| **P2** | Renderer (or hand-author) + index page | ~X hr |
| **P3** | Nav wiring | ~X min |
| **P4** | Verify + polish | ~X min |

Total v1: **~X hr.**

---

## 9. Decisions

Resolve every open question with AskUserQuestion *before* drafting copy. Lock answers here.

1. **<Question topic>** — <decision> (rationale: <why>)
2. **<Question topic>** — <decision>

---

## 10. Out of scope (v1)

Explicit list of what's deferred. Avoids future "why didn't you do X" questions.

- <Deferred item> — defer because <reason>
- <Deferred item>

---

**End of spec.** Awaiting sign-off before implementation.
