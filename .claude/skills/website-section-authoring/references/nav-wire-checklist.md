# Navigation wiring checklist

Six places to edit when adding a new section to the register. Today the nav is duplicated across pages (no shared header); strict wiring touches ~25 files. Lazy wiring touches 2.

Use the strict path for sections that will be heavily linked (Impetus, JCP). Use the lazy path for sections that stand alone (Fynd Academy v1).

---

## 1 · Home page card (mandatory)

**File:** `index.html`

Find the existing card for the section (it usually pre-exists as a Capability Frontier or Track tile pointing nowhere). Wrap it in an anchor:

```html
<a href="/<section>" class="card p-6 block hover:border-black transition">
  <div class="cap-num mb-3">NN</div>
  <h3 class="font-semibold text-lg mb-2" style="color: var(--ink);"><Section Name></h3>
  <p class="text-sm" style="color: var(--ink-muted);">
    <Existing or new descriptor copy. Must pass website-tone-of-voice.>
    DRI: <Name>.
  </p>
</a>
```

Search aid: `grep -n "<Section Name>" index.html` to find the existing card.

---

## 2 · Top-nav Tracks mega-menu (mandatory)

**File:** `index.html` (and every other page if going strict — see §6 below)

The Tracks mega-panel has three columns: Platform, Vertical, Capability. Decide which column the section belongs in.

| Column | Members today | Use when |
|---|---|---|
| Platform | JCP, Impetus, Granary | Section is a horizontal platform serving multiple verticals |
| Vertical | Samarth, RCPL, RBL, Retail Vista, Retail Jarvis, ALP, Forge, HireFirst | Section is a vertical / customer / partner-specific surface |
| Capability | Autonomous, AI Cataloging, Studio · Videos, AI Photoshoots, Brand designs, Category intel | Section is a cross-cutting capability layer |

Add a single line in the chosen column:

```html
<a href="/<section>" class="mega-link"><Section Name> <span class="mono-suffix"><stat></span></a>
```

**Active state convention.** On the section's *own* page, the entry uses `class="mega-link active"` (highlights the user's current location in the menu). On all other pages it stays `class="mega-link"` (no `active`). When you copy the topnav block into a new section's `index.html`, remember to add `active` to its own entry.

Search aid: find the line `<div class="mega-col-label">Capability</div>` and add the new entry below it (or whichever column matches).

---

## 3 · Top-nav More mega-menu (only if meta-page)

**File:** `index.html`

The More menu holds meta-pages: Organisation, Culture, IP Catalog. Only add a new section here if it's a meta-page (cross-cutting reference, not a track).

```html
<a href="/<section>" class="mega-link"><Section Name> <span class="mono-suffix"><stat></span></a>
```

For most new sections, **skip this**.

---

## 4 · IP Catalog (mandatory)

**File:** `catalog/index.html`

The IP catalog is the canonical "all IPs" list. Every section's primary IP(s) get an entry. Find the right table/grid for the section's category and add a row.

Search aid: open `catalog/index.html`, find the closest existing entry, copy the row pattern.

---

## 5 · Footer "Other tracks" lists

**Decision point:** strict or lazy?

### Strict (recommended for sections that other tracks will link to)

Every track page has a footer with an "Other tracks" list. This list is duplicated, not shared. Add the new section to all of them.

Find them:
```bash
grep -rln 'section-label mb-3">Other tracks' --include='*.html'
```

For each result, find the `<ul>` block under `Other tracks` and add:
```html
<li><a href="/<section>" class="hover:underline"><Section Name></a></li>
```

Time: ~5 minutes for ~12 files.

### Lazy (acceptable for v1 of a section nobody links to)

Skip §5 entirely. Add the section to the footers later, in a "nav backfill" commit. Acceptable when the section is new and no sibling page references it yet.

---

## 6 · Sibling section pages (per-section judgment)

If the new section is mentioned on a sibling page (e.g., the home page card mentions "RIL Jewels" and we now have a `/fynd-academy/` page that documents that session), update the sibling to link.

Search aid:
```bash
grep -rln "<Reliance entity name>\|<Session keyword>" --include='*.html'
```

For each result, decide whether the mention should become a link.

---

## Verify after wiring

```bash
python3 -m http.server 8000
```

- [ ] Click the new section's link from the **home page card**
- [ ] Open the **Tracks mega-menu** from any page; click the new section entry
- [ ] (If meta) Open the **More mega-menu**; click the new section entry
- [ ] Open `/catalog`; find the new section listed
- [ ] (If strict §5) Open a sibling track page; check footer "Other tracks" includes the new section
- [ ] Click any sibling link added in §6

If any link 404s or routes wrong, fix before declaring nav wired.

---

## Snippet bank

For pasting:

**Tracks mega-link with stat suffix:**
```html
<a href="/<section>" class="mega-link"><Section Name> <span class="mono-suffix"><e.g. 600+ trained></span></a>
```

**Footer Other-tracks `<li>`:**
```html
<li><a href="/<section>" class="hover:underline"><Section Name></a></li>
```

**Home page card (full):**
```html
<a href="/<section>" class="card p-6 block hover:border-black transition">
  <div class="cap-num mb-3">NN</div>
  <h3 class="font-semibold text-lg mb-2" style="color: var(--ink);"><Section Name></h3>
  <p class="text-sm" style="color: var(--ink-muted);">
    <One-line apex-readable descriptor. Number + scope + DRI.>
  </p>
</a>
```
