# Cross-Navigation · v0.1 spec

**Author** · Kushan Shah · **Date** · 2026-05-02 · **Owner** · Fynd

A hand-curated "See also" block at the bottom of each page that surfaces 2–4 editorial connections to other pages on the register. Complements [Site Navigation v0.1](/docs/site-nav-spec.md), which handles *getting to a different track*; this spec handles *getting from one page to its natural neighbours*.

---

## §1 · Why now

The topnav (per [`site-nav-spec.md`](/docs/site-nav-spec.md)) lets the reader jump between **tracks** — Impetus, JCP, Granary, Special Projects, AI-Native, Recent Innovations — and to utility pages via the More menu. That solves "where else can I go on the site" but not "what other page on this site is directly relevant to what I just read."

Concretely, a reader landing on `/impetus/ai-photoshoot` has no path to:
- `/impetus/cortex` — the search/enrichment engine that powers AI Photoshoot.
- `/impetus/photoshoots` — the case-study gallery showing the work in production.
- `/impetus/plm` — the catalog surface that consumes the photoshoot output.

…other than going back to `/impetus` and clicking down into each. The connections exist in the work but are invisible to the page.

The same pattern repeats across the site:

- **`/jcp/cataloging` ↔ `/impetus/plm`** — same product attributes, two sides of the vendor flow. Neither page mentions the other.
- **`/autonomous`** — every Impetus sub-platform asserts an L0–L5 level. None of those pages link back to the framework page that defines the levels.
- **`/frameworks`** — Farooq's four working papers. Cited in conversation across Impetus, JCP, and Organisation, but inbound links from those pages are zero.
- **`/granary/research/transforming-retail-forecasting`** — a research paper that expands one of the four working papers. The link from `/frameworks` to this paper does not exist.
- **`/culture`, `/organisation`, `/numbers`, `/fynd-academy`** — utility pages that sit in the More menu. Inbound links from the work pages are zero, despite each work page implicitly relying on culture, headcount, adoption numbers, and trained users.

The site reads as 50 standalone pages connected only by a topnav, when in fact it is a graph.

---

## §2 · Decision · editorial, not systematic

Two viable approaches:

| Approach | What it looks like | Why we are not picking it |
|---|---|---|
| **Auto-generated "Related" grid** | Component reads page metadata (track, tags) and renders a 4-up "More from Impetus" block. | Reads as CMS-grid filler. Fails the no-marketing-voice rule. Adds nothing the Impetus hub page doesn't already offer. |
| **Bucket-based "Other platforms in this track"** | Hard-coded by track — JCP pages link to other JCP pages, etc. | Same problem — the per-platform subnav strip already does this. Doesn't surface *cross-track* connections (the high-value ones). |
| **Hand-curated editorial "See also" block** ✓ | 2–4 links per page, hand-picked, each with a one-line context written in the same register as the rest of the page. Cross-track connections allowed and encouraged. | Reads as content. Surfaces the connections that actually matter. Cost: someone has to make ~150 editorial calls (50 pages × ~3 links each). |

We pick the third. The cost is bounded — each call takes ~1 minute, and the spec for each new page can include its 2–4 cross-links from day one.

---

## §3 · Two cross-link surfaces

This spec covers the **structural block** (§4–§5). It also notes a **second, lighter pattern** for inline cross-refs inside prose, which is editorial and not standardised.

### §3.1 · Structural block · `see-also`
A bordered block above the footer, below the last `<section>`, on every page. 2–4 cards. Same `card` base class as the rest of the site. Built from a single `tools/cross_links.py` map. Subject of this spec.

### §3.2 · Inline cross-refs · prose discretion
When a paragraph naturally names another platform / framework / page, that name should be the link. Example, on `/impetus/ai-photoshoot`:

> *"Vertex Search ([Cortex](/impetus/cortex)) runs the enrichment loop; output flows into [Impetus PLM](/impetus/plm) for vendor approval."*

Not standardised — the rule is "if you mention a page that exists on this register, link it the first time." Pages that pass [`website-page-reviewer`](/.claude/skills/website-page-reviewer) get this checked.

---

## §4 · Component · `see-also`

### §4.1 · Position
Immediately after the last `<section>` of page content, immediately before `<footer>`. Visible on every page that has a `CROSS_LINKS` entry. Pages with no entry render no block (rather than an empty one).

### §4.2 · Structure

```
SEE ALSO
┌────────────────────────────┐ ┌────────────────────────────┐ ┌────────────────────────────┐
│ Cortex                     │ │ Impetus PLM                │ │ Autonomy framework         │
│ Vertex Search runs the     │ │ Same product attributes,   │ │ Cataloging Live = L1.      │
│ enrichment loop.           │ │ internal-vendor side.      │ │                            │
└────────────────────────────┘ └────────────────────────────┘ └────────────────────────────┘
```

- **Eyebrow** · `cap-num` style: `SEE ALSO`. No suffix.
- **Card label** · the page's role *from this page's perspective*, not always its title. Example: from `/jcp/cataloging`, Cortex is labelled "Cortex" (its name); but from `/impetus/cortex`, the link to `/jcp/cataloging` might be labelled "JCP Cataloging" (because that is what it is, on the cataloging side).
- **Card context** · one short line, ≤15 words, explaining the connection. **Why** this link matters from the source page, not what the target page is about.
- **No metric, no date, no DRI** in the see-also card. Those belong on the destination page.
- **2–4 cards.** Less than 2 means the page doesn't have natural neighbours and the block is dropped. More than 4 means the editorial call wasn't sharp enough — pick the best 4.

### §4.3 · Copy register

Same five rules as `website-tone-of-voice.md`:

| Wrong | Right |
|---|---|
| *"Discover the powerful Cortex engine that powers our AI Photoshoot platform."* | *"Vertex Search runs the enrichment loop."* |
| *"Learn more about how PLM enables vendor onboarding."* | *"Same product attributes, internal-vendor side."* |
| *"Related: Autonomy."* | *"Cataloging Live = L1."* |

Banned phrasings in see-also context cards: *learn more, discover, explore, see how, find out, dive into, related, more from*.

### §4.4 · Visual
- Use the existing `card` base class.
- Background slightly lighter than the page (e.g. `var(--paper-soft)`) to distinguish the block from page content.
- Card body is the entire clickable target. Per `website-tone-of-voice.md` §3 banned constructions: no decorative `↗` arrow.
- Block top padding equal to the section spacing used elsewhere on the page (no special hero treatment).

---

## §5 · Implementation

### §5.1 · Source of truth · `tools/cross_links.py`

```python
# tools/cross_links.py
CROSS_LINKS: dict[str, list[dict]] = {
    "/jcp/cataloging": [
        {"href": "/impetus/plm",     "label": "Impetus PLM",         "context": "Same product attributes, internal-vendor side."},
        {"href": "/impetus/cortex",  "label": "Cortex",              "context": "Vertex Search runs the enrichment loop."},
        {"href": "/autonomous",      "label": "Autonomy framework",  "context": "Cataloging Live = L1."},
    ],
    "/impetus/ai-photoshoot": [
        {"href": "/impetus/cortex",       "label": "Cortex",       "context": "Powers the search and enrichment behind every shoot."},
        {"href": "/impetus/photoshoots",  "label": "Photoshoots",  "context": "Case studies — AJIO, Buda Jeans, SS26 PLM pilot."},
        {"href": "/impetus/plm",          "label": "Impetus PLM",  "context": "Where the approved photoshoot output lands."},
    ],
    # … one entry per page that has natural neighbours
}

def render_see_also(page_path: str) -> str:
    """Return the see-also block HTML, or empty string if no entry."""
    ...
```

`page_path` is the page's URL path, normalised with leading slash and no trailing slash. Builders pass `page_path` explicitly.

### §5.2 · Builder integration

- `tools/build_impetus.py` — render `render_see_also(path)` between the last section and `footer()`.
- `tools/build_jcp_channels_page.py` — same.
- Static `index.html` files — covered by `tools/inject_cross_links.py` (next).

### §5.3 · Static HTML migration · `tools/inject_cross_links.py`

Modelled directly on `tools/inject_chrome.py`:

1. Glob every `index.html` under repo root (excluding `.venv`, `node_modules`, `.git`, `.vercel`, `tools/scratch`).
2. For each file, derive its `page_path` from the file's relative path.
3. Look up `CROSS_LINKS[page_path]`. If absent, skip.
4. Locate the existing `see-also` block via marker comments (`<!-- see-also:start -->` / `<!-- see-also:end -->`) — if absent, insert a new block immediately before `<footer`.
5. Replace its contents with the rendered HTML.
6. Idempotent — running it on already-converted pages is a no-op (block contents are byte-equal).

### §5.4 · No cache concerns
HTML is inline. Re-deploy via Vercel; new see-also blocks land on next build.

---

## §6 · Initial cross-link graph · proposal

This is **not** the full map (~150 link decisions across 50 pages) — that gets built in §7 step 2 with per-page review. This is a representative sample of the dense connections, to validate the approach.

### §6.1 · Impetus internals (high-density)

| From | → | To | Context |
|---|---|---|---|
| `/impetus` | → | `/autonomous` | The L0–L5 frame every Impetus surface uses. |
| `/impetus` | → | `/frameworks` | Why F&L AI looks the way it does — Farooq's four papers. |
| `/impetus` | → | `/jcp/cataloging` | Where Impetus product attributes meet the channel side. |
| `/impetus/cortex` | → | `/impetus/ai-photoshoot` | Cortex powers the photoshoot enrichment loop. |
| `/impetus/cortex` | → | `/impetus/nextwave` | Same Vertex Search base. |
| `/impetus/cortex` | → | `/jcp/cataloging` | Vertex Search powers cataloging too. |
| `/impetus/ai-photoshoot` | → | `/impetus/cortex` · `/impetus/photoshoots` · `/impetus/plm` | (See §5.1 example.) |
| `/impetus/plm` | → | `/jcp/cataloging` · `/impetus/cortex` | Vendor side ↔ channel side; enrichment engine. |
| `/impetus/nextwave` | → | `/impetus/category-intel` · `/impetus/cortex` | What it produces; what it runs on. |

### §6.2 · JCP internals

| From | → | To | Context |
|---|---|---|---|
| `/jcp` | → | `/jcp/channels` · `/jcp/cataloging` · `/jcp/rcpl` | The three live JCP surfaces. |
| `/jcp/cataloging` | → | `/impetus/plm` · `/impetus/cortex` · `/autonomous` | (See §5.1 example.) |
| `/jcp/channels` | → | `/jcp/rcpl` · `/jcp/7eleven` · `/kaily` | Where the 78 channels show up downstream. |
| `/jcp/rcpl` | → | `/jcp` · `/jcp/cataloging` | RCPL is a JCP customer rollout. |

### §6.3 · Cross-track

| From | → | To | Context |
|---|---|---|---|
| `/granary` | → | `/frameworks` · `/autonomous` | Expands one of Farooq's papers; uses the L0–L5 frame. |
| `/granary/research/transforming-retail-forecasting` | → | `/frameworks` · `/granary` | Source paper; product surface. |
| `/alp` | → | `/samarth` · `/organisation` | Workforce adjacency; org headcount context. |
| `/forge` | → | `/dark-factory` | Made-to-measure adjacency. |
| `/hirefirst` | → | `/organisation` · `/fynd-academy` | Talent intake → talent training. |

### §6.4 · Utility pages

| From | → | To | Context |
|---|---|---|---|
| `/organisation` | → | `/culture` · `/fynd-academy` · `/numbers` | The three pages that close the org loop. |
| `/culture` | → | `/organisation` · `/frameworks` | Who; why. |
| `/fynd-academy` | → | `/organisation` · `/numbers` · `/impetus` | Trained-user → adoption → platform reach. |
| `/frameworks` | → | `/granary/research/transforming-retail-forecasting` · `/impetus` · `/autonomous` | Where Farooq's papers actually land in product. |
| `/autonomous` | → | `/impetus/cortex` · `/jcp/cataloging` · `/granary` | Examples of Live L1, Live L2, Pilot L3. (Pick the four sharpest.) |

### §6.5 · What the graph reveals
- **`/autonomous` and `/frameworks` are the two most under-linked pages** today. Both are framework artefacts that most work pages implicitly rely on; almost none link back. Highest-value additions.
- **`/jcp/cataloging` ↔ `/impetus/plm` ↔ `/impetus/cortex`** is a tight triangle that no current page surfaces.
- **Utility pages (`/culture`, `/organisation`, `/fynd-academy`)** have zero inbound links from work pages. The see-also block is the cheapest fix.

---

## §7 · Migration plan

| Step | Action | Owner | Status |
|---|---|---|---|
| 1 | Land this spec | Kushan | _draft_ |
| 2 | Walk every page (~50). For each, propose 2–4 cross-links with one-line context. Output as a draft `CROSS_LINKS` dict for review | Claude | pending |
| 3 | Kushan review pass — line-edit context strings, drop weak entries, add missing ones | Kushan | pending |
| 4 | Implement `tools/cross_links.py` per §5.1 with the reviewed map | Claude | pending |
| 5 | Implement `tools/inject_cross_links.py` per §5.3 | Claude | pending |
| 6 | Run injector across all `index.html` files that have a map entry | Claude | pending |
| 7 | Wire `tools/build_impetus.py` and `tools/build_jcp_channels_page.py` to call `render_see_also(path)` | Claude | pending |
| 8 | Sanity sweep — load 10 sample pages, click every see-also link, confirm no 404s and that the context line still matches the destination page | Claude + Kushan | pending |
| 9 | Update `website-section-authoring` skill — every new page spec must propose its 2–4 cross-links from day one (and propose any inbound links it expects from existing pages) | Claude | pending |
| 10 | Update `website-page-reviewer` skill — add a check for inline cross-refs (§3.2) and for see-also block presence/quality | Claude | pending |

---

## §8 · Extending · adding cross-links to a new page

When `/kaily` (say) lands, its spec includes:

```python
"/kaily": [
    {"href": "/jcp/channels",  "label": "JCP Channels",  "context": "JioMart and AJIO sit in the channel list."},
    {"href": "/ratl",          "label": "Ratl",          "context": "Adjacent agentic surface — QA side."},
    {"href": "/autonomous",    "label": "Autonomy framework", "context": "Kaily Live = L2."},
],
```

…plus any **inbound** links from pages that should now point at Kaily (`/jcp/channels`, `/ratl`). The page spec carries both directions; the spec author makes the editorial call.

Run `python tools/inject_cross_links.py` → blocks update everywhere.

---

## §9 · Open questions

- **Reciprocity.** If A links to B in see-also, must B link back to A? Default: **no, not required.** The block is editorial, not a graph. A→B can be a strong connection (the engine that powers the page) while B→A is one of many downstream consumers and not worth a slot. Reciprocity is a smell to check, not a rule to enforce.
- **Mobile treatment.** Below `md` breakpoint the cards stack. No collapsible / hide behaviour — the block is short enough (4 cards × ~30 words) that it stays cheap on mobile.
- **Inline cross-ref discoverability.** §3.2 says "if you mention a page on this register, link it." Currently this is reviewer-enforced, not tooled. A `tools/audit_cross_refs.py` could grep for known platform names in prose and warn where they aren't linked. Not in scope for v0.1.
- **What counts as "natural neighbours"?** The editorial bar: a reader who finished page A would *meaningfully benefit* from page B, beyond what the topnav already gives them. If the only honest justification is "they're both Impetus", drop it. The topnav handles that.
- **Ownership when pages drift.** If `/impetus/cortex` changes scope, the see-also context lines that point at it from 4 other pages may go stale. We rely on the page-reviewer skill (step 10) to catch this; no tooling for now.
