"""P3a · /jcp/index.html rewrite per docs/jcp-update-spec.md v0.4 §3.1.

Performs (in order):
  1. Capture sections being moved/cut to scratch files (for P3b/c/d/e/f).
  2. Replace hero stat strip + intro paragraph with slide-35 + slide-31 numbers.
  3. Insert NEW Ecosystem section (slide-35 verbatim · 9 capability cards).
  4. Cut: Full B2C roster + headcount + extra channel tables (lines 136-360).
  5. Cut: Sub-IPs · 19 modules (lines 362-411) — already captured for /catalog/.
  6. Cut: Deep cards (lines 413-477).
  7. Cut: UCP (lines 479-604) — already captured for /ucp/.
  8. Cut: Agentic Commerce (lines 606-645) — already captured for /kaily/ + /pixelbin/.
  9. Replace AI Cataloging block (lines 676-688) with a CTA card.

Re-runnable: it works off the original captured snapshot at
tools/scratch/jcp_extracts/_original.html, so re-running just regenerates
the rewrite with any patched logic.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
SRC = ROOT / "jcp" / "index.html"
EXTRACTS = ROOT / "tools" / "scratch" / "jcp_extracts"

EXTRACTS.mkdir(parents=True, exist_ok=True)
ORIGINAL = EXTRACTS / "_original.html"


def line_slice(lines: list[str], start: int, end: int) -> str:
    """1-indexed inclusive slice."""
    return "".join(lines[start - 1:end])


# Lines (1-indexed) match the spec's analysis. If /jcp/index.html drifts,
# re-run the analysis grep first.
ROSTER_BIG_BLOCK   = (136, 360)   # B2C roster + headcount + extra tables
SUB_IPS            = (362, 411)
DEEP_CARDS         = (413, 477)
UCP                = (479, 604)
AGENTIC_COMMERCE   = (606, 645)
AI_CATALOGING      = (676, 688)
HERO_STAT_BLOCK    = (83, 110)    # includes the "Channel coverage · verified" cap-num at line 83


# ---------------------------------------------------------------------------
# New content
# ---------------------------------------------------------------------------

NEW_HERO_STATS = '''
<div id="scale" class="cap-num mt-2 mb-3">FY 2025-26 · Accenture · 16-Apr-2026 · slide 35</div>
<div class="grid grid-cols-2 md:grid-cols-4 gap-3 max-w-4xl">
<div class="card p-4"><div class="cap-num mb-1">Orders / day</div><div class="display-2 text-3xl accent">700K+</div></div>
<div class="card p-4"><div class="cap-num mb-1">Orders / min · peak</div><div class="display-2 text-3xl accent">50K+</div></div>
<div class="card p-4"><div class="cap-num mb-1">Customers · FY26</div><div class="display-2 text-3xl accent">200M+</div></div>
<div class="card p-4"><div class="cap-num mb-1">Stores served</div><div class="display-2 text-3xl accent">30K+</div></div>
</div>

<div id="channel-coverage" class="cap-num mt-6 mb-3">Channel coverage · slide 31 + Channel Coverage PDF (Feb-2026)</div>
<div class="grid grid-cols-2 md:grid-cols-4 gap-3 max-w-4xl">
<div class="card p-4"><div class="cap-num mb-1">Total channels</div><div class="display-2 text-3xl" style="color: var(--ink);">78</div><div class="text-xs mt-1" style="color: var(--ink-muted);">68 live · 5 in-progress · 5 planned</div></div>
<div class="card p-4"><div class="cap-num mb-1">B2C businesses</div><div class="display-2 text-3xl" style="color: var(--ink);">105</div></div>
<div class="card p-4"><div class="cap-num mb-1">B2B businesses</div><div class="display-2 text-3xl" style="color: var(--ink);">7</div></div>
<div class="card p-4"><div class="cap-num mb-1">Verticals covered</div><div class="display-2 text-3xl" style="color: var(--ink);">10</div><div class="text-xs mt-1" style="color: var(--ink-muted);">F&L · Grocery · Electronics · Beauty · Furniture · Pharma · Jewellery · Home Decor · Fresh Food · Digital Top-Up</div></div>
</div>

<div class="grid grid-cols-2 md:grid-cols-3 gap-3 max-w-4xl mt-3">
<div class="card p-4"><div class="cap-num mb-1">CPO</div><div class="font-semibold" style="color: var(--ink);">Ashish Chandorkar</div></div>
<div class="card p-4"><div class="cap-num mb-1">Engineering lead</div><div class="font-semibold" style="color: var(--ink);">Pratik Patel · Jainish Jain</div></div>
<div class="card p-4"><div class="cap-num mb-1">RIL counterpart</div><div class="font-semibold" style="color: var(--ink);">Jeyandran · Vineeth Nair</div></div>
</div>
'''.strip("\n")


# Slide 35 verbatim · 9 capability cards
NEW_ECOSYSTEM_SECTION = '''
<!-- ECOSYSTEM · slide 35 (Accenture · 16-Apr-2026) -->
<section class="py-16 border-b" style="border-color: var(--border); background: var(--bg-soft);"><div class="max-w-7xl mx-auto px-6">
<div class="section-label mb-3">Ecosystem · scale of retail transformation · FY 2025-26</div>
<h2 class="display-2 text-3xl md:text-4xl mb-4" style="color: var(--ink);">Why JCP scales the way it does.</h2>
<p class="text-base max-w-3xl mb-10" style="color: var(--ink-muted);">Nine capability claims from the Accenture deck (16-Apr-2026 · slide 35) — verbatim. The properties that let one stack carry 700K+ orders a day across 78 channels.</p>

<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
<div class="card p-6"><div class="cap-num mb-2">01</div><h3 class="font-semibold text-lg mb-2" style="color: var(--ink);">Microservice-Based Platform</h3><p class="text-sm" style="color: var(--ink-muted);">Modular, scalable, and interoperable services.</p></div>
<div class="card p-6"><div class="cap-num mb-2">02</div><h3 class="font-semibold text-lg mb-2" style="color: var(--ink);">Accelerated Go-To-Market</h3><p class="text-sm" style="color: var(--ink-muted);">Pre-built features accelerate launches.</p></div>
<div class="card p-6"><div class="cap-num mb-2">03</div><h3 class="font-semibold text-lg mb-2" style="color: var(--ink);">Eliminating Redundancy</h3><p class="text-sm" style="color: var(--ink-muted);">Streamlined workflows for faster cycles.</p></div>
<div class="card p-6"><div class="cap-num mb-2">04</div><h3 class="font-semibold text-lg mb-2" style="color: var(--ink);">Cross-Tech Leverage</h3><p class="text-sm" style="color: var(--ink-muted);">15+ retail extensions enhance efficiency.</p></div>
<div class="card p-6"><div class="cap-num mb-2">05</div><h3 class="font-semibold text-lg mb-2" style="color: var(--ink);">Optimized Resourcing</h3><p class="text-sm" style="color: var(--ink-muted);">Unified tech stack lowers manpower needs.</p></div>
<div class="card p-6"><div class="cap-num mb-2">06</div><h3 class="font-semibold text-lg mb-2" style="color: var(--ink);">AI Documentation &amp; Learning</h3><p class="text-sm" style="color: var(--ink-muted);">Strengthening the ecosystem with Danswer.</p></div>
<div class="card p-6"><div class="cap-num mb-2">07</div><h3 class="font-semibold text-lg mb-2" style="color: var(--ink);">Modular &amp; Flexible Architecture</h3><p class="text-sm" style="color: var(--ink-muted);">Adaptable across diverse business verticals.</p></div>
<div class="card p-6"><div class="cap-num mb-2">08</div><h3 class="font-semibold text-lg mb-2" style="color: var(--ink);">Centralized Governance</h3><p class="text-sm" style="color: var(--ink-muted);">Centralized compliance ensures alignment.</p></div>
<div class="card p-6"><div class="cap-num mb-2">09</div><h3 class="font-semibold text-lg mb-2" style="color: var(--ink);">Seamless Scalability</h3><p class="text-sm" style="color: var(--ink-muted);">Easily scalable infrastructure solutions.</p></div>
</div>

<p class="text-xs mt-6" style="color: var(--ink-muted);">Source · Accenture · Updated Retail Platforms+Agents · Apr-16-2026 · slide 35</p>
</div></section>
'''.strip("\n")


# Replacement for the in-place AI Cataloging block — shrunk to a CTA card
NEW_CATALOGING_CTA = '''
<section class="py-16 border-b" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
<div class="section-label mb-3">AI Cataloging · catalog enrichment via Google AI + Web Grounding</div>
<h2 class="display-2 text-3xl md:text-4xl mb-4" style="color: var(--ink);">From manual enrichment to <span class="accent">~14 seconds</span> per brand.</h2>
<p class="text-base max-w-3xl mb-6" style="color: var(--ink-muted);">Latest Accenture deck (16-Apr-2026 · slide 19) reports <strong>15 days → 5 hours</strong> for full AI Photoshoot + cataloguing pipeline. Deep-dive page covers the architecture, model library, and per-brand outcomes.</p>
<a href="/jcp/cataloging" class="btn-secondary inline-block" style="padding: 10px 18px;">Open AI Cataloging deep-dive →</a>
</div></section>
'''.strip("\n")


# ---------------------------------------------------------------------------
# Pipeline
# ---------------------------------------------------------------------------


def main() -> int:
    if not ORIGINAL.exists():
        ORIGINAL.write_text(SRC.read_text())
        print(f"  saved snapshot → {ORIGINAL.relative_to(ROOT)}")

    text = ORIGINAL.read_text()
    lines = text.splitlines(keepends=True)

    # Capture
    (EXTRACTS / "section_sub_ips.html").write_text(line_slice(lines, *SUB_IPS))
    (EXTRACTS / "section_deep_cards.html").write_text(line_slice(lines, *DEEP_CARDS))
    (EXTRACTS / "section_ucp.html").write_text(line_slice(lines, *UCP))
    (EXTRACTS / "section_agentic_commerce.html").write_text(line_slice(lines, *AGENTIC_COMMERCE))
    print(f"  captured 4 sections to {EXTRACTS.relative_to(ROOT)}/")

    # Build the rewritten file
    out = []

    # 1. Lines 1-82: head + topnav + crumb + author + h1 + intros (drops the
    # vestigial "Channel coverage · verified 21 - Feb - 2026" cap-num at 83).
    head = "".join(lines[0:82])
    # Rewrite the second intro paragraph to align numbers with slide 35.
    head = head.replace(
        "78 channels · 300M customers · 50K orders/min",
        "78 channels · 200M+ customers · 700K+ orders/day",
    )
    out.append(head)

    # 2. NEW hero stats (replaces lines 84-110)
    out.append(NEW_HERO_STATS + "\n")

    # 3. Lines 111-134: B2C + B2B Snapshot sections (retain)
    #    Note: 111 is blank line; 112 opens, 134 closes. Add 135 (blank) too.
    out.append("</div></section>\n")
    out.append("\n")
    out.append("".join(lines[111:135]))

    # 4. NEW Ecosystem section (slide 35) — placed after B2B snapshot
    out.append("\n" + NEW_ECOSYSTEM_SECTION + "\n\n")

    # 5. Lines 136-477 are CUT (rosters, headcount, sub-IPs, deep cards, agentic).
    #    Lines 479-604 (UCP) + 606-645 (Agentic) ALSO cut.
    #    Skip ahead to line 648 (Vertex Search start).

    # 6. Lines 647-674: Vertex Search (retain)
    out.append("".join(lines[646:675]))

    # 7. NEW AI Cataloging CTA (replaces lines 676-688)
    out.append("\n" + NEW_CATALOGING_CTA + "\n\n")

    # 8. Lines 689-714: AJIO migration + closer (retain)
    out.append("".join(lines[688:715]))

    # 9. Lines 716-end: footer (retain)
    out.append("".join(lines[715:]))

    new_text = "".join(out)
    SRC.write_text(new_text)

    n_old = len(text.splitlines())
    n_new = len(new_text.splitlines())
    print(f"  rewrote {SRC.relative_to(ROOT)}: {n_old} lines → {n_new} lines  ({n_new - n_old:+d})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
