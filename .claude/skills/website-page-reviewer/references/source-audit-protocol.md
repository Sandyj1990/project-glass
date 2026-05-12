# Source Audit Protocol

Step-by-step protocol for tracing every claim on the page to a source file in the compilation folder. This is the rigour that turns a register from "polished" into "Apex-defensible".

## The traceability principle

Every numerical claim, named person, date, status statement, or material assertion must have a source. The source is one of:

1. A file in the page's source compilation folder (preferred).
2. A file already cited in the page's `§Sources` block (must point at it).
3. A canonical document elsewhere in the repo (e.g., `docs/2026-04-30-farooq-mda-update-letter.md`) that the page author explicitly referenced in the spec.
4. An external URL with `<a target="_blank">` — only acceptable if the URL is accessible to the Apex audience.

A claim with **none of the above** is unsourced. Unsourced claims get flagged.

## Workflow

### Step 1 · Build the claim list

Read the page top-to-bottom. For each section, extract:

- **Numbers**: any digit-bearing claim (`11 stores`, `+3.8pp`, `48M rows`, `5 of 37 routes`, `~15-20%`, `12K SKUs × 4K stores`).
- **Dates**: any DD-MMM-YYYY or year reference (`28 - Apr - 2026`, `13 - Nov - 2025`, `Q1 2026`).
- **Named people**: `Mayank Jain`, `Aushin Ganguli`, `Damodar Mall`, `Saurabh Sharma`, etc.
- **Status assertions**: every `pill-live` / `pill-build` / `pill-phase2` and any inline status word ("in test", "live since", "in build").
- **Specific claims**: "33 backend endpoints", "27 routes mock", "9 reason codes", "MAPE 41%", "100+ stores NCR".

Build a table with columns: `Claim · Section · Source candidate · Verified Y/N`.

### Step 2 · Map each claim to a source candidate

For each claim, identify which file in the source compilation folder is most likely to contain it. Use filename heuristics:

- Status updates → `*Update*.md`, `*Weekly*.md`
- Backend / frontend route counts → status report `.txt`
- Verified outcomes (the headline numbers) → case-study PDF / docx
- Module scope → architecture doc / V3 PDF
- Roadmap items (STP / CDT / Consensus Forecasting) → leadership update sections labelled "Planned" / "Roadmap"

### Step 3 · Verify by reading the source

For high-stakes claims (the ones in the hero, the ones in headline pills, the case-study numbers), open the source file and grep for the exact value. Do not trust filename alone.

```bash
grep -n "11 pilot stores" "docs/Granary project documents dump/Granary_Update_Apr28.md"
grep -n "3.8" "docs/Granary project documents dump"/*.md
```

If the value matches, mark Verified Y. If not, flag.

### Step 4 · Spot-check 5+ claims by direct read

Don't grep your way through the entire claim list — do exhaustive grep for hero claims and pill-statuses, but for body-copy claims sample 5-7 across the page (avoid clustering all in one section). For each spot-check, read the source paragraph and confirm the page's statement is faithful.

A faithful page may compress, reorder, or summarise the source — but cannot invent or shift magnitudes. *"~50 participants"* covering a source's *"about 50"* is faithful; *"50+ participants"* is a shift (it now implies upside) and is HIGH severity.

### Step 5 · Audit the §Sources block

If the page has a §Sources block, verify:

1. **Coverage**: every file the page actually cites is listed.
2. **No padding**: every file listed is actually cited somewhere on the page.
3. **Pathing**: paths are correct and the files exist on disk.

Mismatches are MEDIUM. A §Sources block listing a file that doesn't exist is HIGH (Apex who clicks gets a 404).

## Failure patterns

### Pattern 1 — Number drift

The page says `48M rows` but the source says `48.3M rows`. Flag as MEDIUM unless the rounding is clearly intentional and consistent (e.g., all hero numbers rounded to 2 sig figs).

### Pattern 2 — Implied magnitude inflation

The source says "Smart Bazaar and Smart Point teams are validating". The page says "Smart Bazaar and Smart Point validating against control across the 11-store pilot." The "against control" detail isn't in the source — it's an inferred claim. Flag MEDIUM unless the page author confirms with a separate source.

### Pattern 3 — Status confidence drift

The source says "expected to close this week". The page says "closing this week". The page is now making a confidence claim the source hedges. Flag MEDIUM. (Bonus: also flag the "Forward-looking dates" check — "this week" without an explicit Friday date is fragile.)

### Pattern 4 — Name drift

The source has "Aushin Ganguli". The page in one place says "Aushin Ganguli", in another "Aushin G.", in a third "Aushin". Inconsistency is LOW; misspelling is MEDIUM.

### Pattern 5 — Date drift

The source file is dated 2026-04-28 (filename or content). The page says the source is from 27-Apr-2026. Flag LOW unless the date is load-bearing (e.g., the page argues "as of 28-Apr the count was 11" — then HIGH).

### Pattern 6 — Source-folder absence

The page makes a claim that no file in the source folder supports. The author may have used another source not in the compilation folder. Flag MEDIUM — the audit can't disprove the claim, just note that the source pipeline is broken for it.

### Pattern 7 — Cross-source contradiction

Two source files say different things and the page picks one without acknowledgement. (E.g., one update says "10 stores", a later update says "11 stores".) Flag LOW only if the page picks the most-recent source; HIGH if the page picks the older source over a newer one.

## Sample size guidance

For a typical page (10-15 sections, 50-100 distinct claims):

- **Exhaustive verification**: hero stats (every one), pill statuses (every one), §Sources block entries.
- **Sample verification**: 1 claim from each non-hero section, plus 2-3 randomly from body prose. Aim for ~10-15 sampled claims total.
- **Skip**: paragraph-level adjective inflators (handled by tone-of-voice phase), CSS or markup, navigation chrome.

The aim is to detect drift, not to re-author the page. If the sample finds 0 issues, source traceability is high. If 2+ issues in a sample of 10, traceability is in trouble — escalate to exhaustive verification.

## Scoring

```
Source Traceability score:

100 — Every hero stat verified, §Sources block accurate, sample of 10 body claims all verified.
 90 — All hero stats verified; 1 minor body-claim drift found; §Sources block clean.
 80 — Hero stats clean; 1-2 body drifts; §Sources block needs minor fix.
 70 — Hero stat with drift, OR §Sources missing entirely with no inline citations, OR 3+ body drifts.
 60 — Multiple hero drifts OR a fabricated stat OR a CRITICAL unsourced load-bearing claim.
<60 — Page cannot be defended in front of Apex without rework.
```

A single fabricated stat or load-bearing unsourced claim caps Source Traceability at 60 regardless of what else is clean. This is the non-negotiable.
