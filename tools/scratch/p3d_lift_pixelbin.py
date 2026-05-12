"""P3d · Replace /pixelbin/ stub with slide-41 umbrella + GlamAR card lifted
from /jcp/'s Agentic Commerce section."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
PIXELBIN = ROOT / "pixelbin" / "index.html"

BODY = """<section class="pt-16 pb-10 border-b" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
  <div class="crumb mb-6"><a href="/">Home</a> <span class="sep">/</span> <span style="color: var(--ink);">PixelBin</span></div>
  <div class="section-label mb-3">PixelBin · AI marketing media · Live</div>
  <h1 class="display text-5xl md:text-7xl mb-6" style="color: var(--ink);">PixelBin.</h1>
  <p class="text-lg max-w-3xl mb-8" style="color: var(--ink-muted);">New-age marketing and entertainment with AI. Umbrella for four production sub-products: PixelBin core (image transforms), Fynd Studios (AI ads), Fynd Snap (AI photoshoots), and GlamAR (3D / AR / VR commerce). Built by Fynd. Owned and run by Reliance.</p>
</div></section>

<section class="py-16 border-b" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
<div class="section-label mb-3">Sub-products · scale</div>
<h2 class="display-2 text-3xl md:text-4xl mb-6" style="color: var(--ink);">Four products under the PixelBin umbrella.</h2>

<div class="grid grid-cols-2 md:grid-cols-4 gap-4">
  <div class="card p-6"><div class="cap-num mb-2">PixelBin</div><div class="display-2 text-3xl" style="color: var(--ink);">5,000+</div><div class="text-xs mt-1" style="color: var(--ink-muted);">images</div></div>
  <div class="card p-6"><div class="cap-num mb-2">Fynd Studios</div><div class="display-2 text-3xl" style="color: var(--ink);">50+</div><div class="text-xs mt-1" style="color: var(--ink-muted);">AI ads</div></div>
  <div class="card p-6"><div class="cap-num mb-2">Fynd Snap</div><div class="display-2 text-3xl" style="color: var(--ink);">25K</div><div class="text-xs mt-1" style="color: var(--ink-muted);">photoshoots</div></div>
  <div class="card p-6"><div class="cap-num mb-2">GlamAR</div><div class="display-2 text-3xl" style="color: var(--ink);">200+</div><div class="text-xs mt-1" style="color: var(--ink-muted);">AR / VR experiences</div></div>
</div>

<p class="text-xs mt-6" style="color: var(--ink-muted);">Source · Accenture · Updated Retail Platforms+Agents · Apr-16-2026 · slide 41</p>
</div></section>

<section class="py-16 border-b" style="border-color: var(--border); background: var(--bg-soft);"><div class="max-w-7xl mx-auto px-6">
<div class="section-label mb-3">GlamAR · Immersive Commerce</div>
<h2 class="display-2 text-3xl md:text-4xl mb-4" style="color: var(--ink);">Live on Sephora · Vision Express · LensCrafters · WestElm.</h2>
<p class="text-base max-w-3xl mb-8" style="color: var(--ink-muted);">AI-first 3D, AR, and VR commerce platform. Increases conversion and reduces returns across online and in-store journeys. Surfaces: VTO, AI Skin Analysis, AI Style Studio, virtual store, 3D AR ad banners.</p>

<div class="grid grid-cols-3 gap-4 max-w-3xl mb-6">
  <div class="card p-5"><div class="cap-num mb-2">Return reduction</div><div class="display-2 text-3xl accent">40%</div></div>
  <div class="card p-5"><div class="cap-num mb-2">Revenue / visit</div><div class="display-2 text-3xl accent">+106%</div></div>
  <div class="card p-5"><div class="cap-num mb-2">Engagement lift</div><div class="display-2 text-3xl accent">+90%</div></div>
</div>

<p class="text-sm max-w-3xl" style="color: var(--ink);"><strong>Saturdays</strong> · VTO users convert at 32% vs 9% non-VTO (3.5× lift). <strong>Foxtale</strong> · AI Skin Analysis drives 1.6× higher conversion. Source · Accenture · Updated Retail Platforms+Agents · Apr-16-2026 · slide 38.</p>
</div></section>
"""


def main():
    text = PIXELBIN.read_text()
    new_text = re.sub(
        r'<section class="pt-20 pb-32">.*?</section>\n',
        BODY,
        text,
        count=1,
        flags=re.DOTALL,
    )
    if new_text == text:
        raise SystemExit("ERROR · stub section not found in /pixelbin/index.html")
    PIXELBIN.write_text(new_text)
    print(f"  wrote {PIXELBIN.relative_to(ROOT)}: {len(text):,} → {len(new_text):,} bytes")


if __name__ == "__main__":
    main()
