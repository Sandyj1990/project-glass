# `data/` · the source-of-truth folder

Every IP that powers https://reliance-retail-fynd.vercel.app lives here as structured data.

The website is a **render** of this folder. If a track page on the site disagrees with the data here, this folder wins.

## Folder layout

```
data/
  README.md                  # this file
  SCHEMA.md                  # the schema each IP folder follows
  index.json                 # master index of every IP with its slug, status, tags
  ips/
    <ip-slug>/
      meta.json              # canonical metadata: name, status, DRI, dates, web anchors
      narrative.md           # canonical Markdown narrative · what the IP does, why it matters
      metrics.yaml           # numeric KPIs the website cites
      team.yaml              # DRIs, leads, mentors, RIL counterparts
      releases.yaml          # release timeline · dates + outcomes
      links.yaml             # external URLs · production, demos, docs
      slack-extracts/        # extracted Slack messages (JSON or MD) where available
      assets/                # any binaries we've actually attached (images, video stills)
        decks/               # PDFs, PPTX (only if the file is small enough or critical)
        docs/                # Markdown copies of canonical docs
        images/              # screenshots, photos
        videos/              # video files or `.url` shortcut files pointing to YouTube/Drive
```

Big binaries (decks, full videos) live in Drive, not here. We **link** to them from `links.yaml`. Only small, frequently-referenced assets sit in `assets/`.

## Conventions

- **Slug** · lowercase, hyphenated, stable. Used as the folder name and as the URL anchor on the relevant track page (e.g. `/jcp#ucp`).
- **Status** · `Live | Pilot | Build`. Definitions in `SCHEMA.md`. Do not invent new states without updating the schema.
- **Dates** · ISO 8601 (`2026-04-30`) inside YAML/JSON. The website renders them as `30 - Apr - 2026`.
- **Numbers** · always cite source and confidence. See `/numbers` page for the canonical denominator sheet.
- **DRIs** · one human name per role. Not "the team", not a function. The website breaks if a DRI cell is empty.

## How the website uses this folder

The current build is hand-edited HTML referencing this folder by convention. The next iteration will add a build pipeline (`tools/render_site.py`) that generates the HTML from this folder, so a single edit here updates every page that mentions the IP.

For now, the contract is:

1. When you change a number, change it here AND update the website page.
2. When you ship a release, add it to `releases.yaml` AND update the homepage feed and track page.
3. When DRIs change, update `team.yaml` AND the org page.

## Generating / refreshing

```bash
python3 tools/build_data/build.py
```

This regenerates every `data/ips/<slug>/` folder from the master spec in `tools/build_data/spec.py`. Hand edits to generated files survive only if they're outside the generator (e.g. files in `assets/` or `slack-extracts/` are never touched).

## Authoritative sources currently linked

- RIL Q4 FY26 investor deck · for Reliance Retail revenue, customer counts
- JCP Migration Tracker (Salman Saudagar) · for channel counts and status
- Impetus Sell Track IPs sheet (Devam Gosalia) · for Sell-track IP roster
- AI Assessment survey + analysis (Aishwarya Pattanaik) · for org AI fluency
- HR Roster (Akshata Kadam) · for headcount, founder dates
- UCP Release Notes Timeline (Amogh Dubey) · for UCP release timeline + RD Digital Discount Days case study

These are referenced in individual IP `links.yaml` files where applicable.
