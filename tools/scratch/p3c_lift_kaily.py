"""P3c · Lift ZIP (AJIO) + JIIA (JioMart) cards from /jcp/'s Agentic Commerce
section into /kaily/ (replacing the stub). Adds slide-37 ZIP image as hero."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
KAILY = ROOT / "kaily" / "index.html"

# Hero + cards. ZIP image lives on CDN.
BODY = """<section class="pt-16 pb-10 border-b" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
  <div class="crumb mb-6"><a href="/">Home</a> <span class="sep">/</span> <span style="color: var(--ink);">Kaily</span></div>
  <div class="section-label mb-3">Kaily · agentic commerce · Live</div>
  <h1 class="display text-5xl md:text-7xl mb-6" style="color: var(--ink);">Kaily.</h1>
  <p class="text-lg max-w-3xl mb-8" style="color: var(--ink-muted);">Agentic commerce live on AJIO and JioMart. Two production agents — ZIP on AJIO, JIIA on JioMart — that turn natural-language intent into product discovery and checkout. Built by Fynd. Owned and run by Reliance.</p>
</div></section>

<section class="py-16 border-b" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
<div class="section-label mb-3">ZIP · AJIO Commerce Agent</div>
<h2 class="display-2 text-3xl md:text-4xl mb-4" style="color: var(--ink);">An AI Agent That Shops With You, Not Just For You.</h2>
<p class="text-base max-w-3xl mb-8" style="color: var(--ink-muted);">Added to AJIO.com to enable natural-language search and recommendation via chat &amp; voice. Replaces menu-driven navigation for vague-intent shoppers.</p>

<div class="grid md:grid-cols-3 gap-6 items-start mb-6">
<div class="md:col-span-2">
  <div class="grid grid-cols-3 gap-4 mb-6">
    <div class="card p-5"><div class="cap-num mb-2">Positive CX</div><div class="display-2 text-3xl accent">88%</div></div>
    <div class="card p-5"><div class="cap-num mb-2">Catalog covered</div><div class="display-2 text-3xl accent">86%</div></div>
    <div class="card p-5"><div class="cap-num mb-2">Discovery chats</div><div class="display-2 text-3xl accent">2M+</div></div>
  </div>
  <p class="text-sm" style="color: var(--ink);">Chats directly helped product discovery for 86% of users · 88% positive customer engagement · 2M+ products covered by chatbot via real-time catalog sync. Source · Accenture · Updated Retail Platforms+Agents · Apr-16-2026 · slide 37.</p>
</div>
<div>
  <div class="card overflow-hidden">
    <img src="https://socialassets.impetusz0.de/rrl-portfolio/assets/accenture-2026-04-16/slide_37/img_01.png" alt="ZIP Commerce Agent on AJIO" style="width:100%;display:block;" />
    <div class="p-3 text-xs" style="color: var(--ink-muted);">Accenture · 16-Apr-2026 · slide 37</div>
  </div>
</div>
</div>
</div></section>

<section class="py-16 border-b" style="border-color: var(--border); background: var(--bg-soft);"><div class="max-w-7xl mx-auto px-6">
<div class="section-label mb-3">JIIA · JioMart Agentic Shopping Assistant</div>
<h2 class="display-2 text-3xl md:text-4xl mb-4" style="color: var(--ink);">Showcased on the Google Cloud Next '26 main stage.</h2>
<p class="text-base max-w-3xl mb-8" style="color: var(--ink-muted);">Agentic shopping assistant powered by a Gemini multimodal pipeline reading 40M+ JioMart catalog images. Live on the JioMart app. Keynote · 29-Apr-2026.</p>

<div class="grid grid-cols-3 gap-4 max-w-3xl mb-6">
  <div class="card p-5"><div class="cap-num mb-2">Images indexed</div><div class="display-2 text-3xl" style="color: var(--ink);">40M+</div></div>
  <div class="card p-5"><div class="cap-num mb-2">Pipeline</div><div class="display-2 text-3xl" style="color: var(--ink);">Gemini</div><div class="text-xs mt-1" style="color: var(--ink-muted);">multimodal</div></div>
  <div class="card p-5"><div class="cap-num mb-2">Status</div><div class="display-2 text-3xl accent">Live</div><div class="text-xs mt-1" style="color: var(--ink-muted);">JioMart app</div></div>
</div>

<p class="text-sm max-w-3xl" style="color: var(--ink);">Team · <strong>Punit Kalro · Shreyash · Abhay · Sukhpreet · Raj Pratap · Kapil · Manish Kumar · Bijan Kundu</strong>. Lead · <strong>Ashish Chandorkar</strong>.</p>
</div></section>
"""


def main():
    text = KAILY.read_text()
    new_text = re.sub(
        r'<section class="pt-20 pb-32">.*?</section>\n',
        BODY,
        text,
        count=1,
        flags=re.DOTALL,
    )
    if new_text == text:
        raise SystemExit("ERROR · stub section not found in /kaily/index.html")
    KAILY.write_text(new_text)
    print(f"  wrote {KAILY.relative_to(ROOT)}: {len(text):,} → {len(new_text):,} bytes")


if __name__ == "__main__":
    main()
