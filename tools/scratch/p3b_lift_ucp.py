"""P3b · Lift UCP block from /jcp/ → /ucp/ replacing the stub."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
UCP_TARGET = ROOT / "ucp" / "index.html"
EXTRACT = ROOT / "tools" / "scratch" / "jcp_extracts" / "section_ucp.html"

# New page body — hero (with crumb + section label + h1 + intro) + the captured UCP block.
BODY_TEMPLATE = """<section class="pt-16 pb-10 border-b" style="border-color: var(--border);"><div class="max-w-7xl mx-auto px-6">
  <div class="crumb mb-6"><a href="/">Home</a> <span class="sep">/</span> <span style="color: var(--ink);">UCP</span></div>
  <div class="section-label mb-3">UCP · Unified Customer Platform · Live</div>
  <h1 class="display text-5xl md:text-7xl mb-6" style="color: var(--ink);">UCP.</h1>
  <p class="text-lg max-w-3xl mb-8" style="color: var(--ink-muted);">One identity layer underneath every Reliance retail business — online and offline. Lifted from the JCP register; deeper extension to follow.</p>
</div></section>

{ucp_block}
"""


def main():
    ucp_block = EXTRACT.read_text()
    # Strip the id="ucp" — page IS UCP, the in-page anchor is meaningless here.
    ucp_block = ucp_block.replace('<section id="ucp" ', '<section ', 1)

    new_body = BODY_TEMPLATE.format(ucp_block=ucp_block)

    text = UCP_TARGET.read_text()
    # Replace from the first <section after </nav> to the closing </section> before <footer>.
    # The current stub has exactly one body section.
    import re
    new_text = re.sub(
        r'<section class="pt-20 pb-32">.*?</section>\n',
        new_body,
        text,
        count=1,
        flags=re.DOTALL,
    )
    if new_text == text:
        raise SystemExit("ERROR · stub section not found in /ucp/index.html — check selector")

    UCP_TARGET.write_text(new_text)
    print(f"  wrote {UCP_TARGET.relative_to(ROOT)}: {len(text):,} → {len(new_text):,} bytes")


if __name__ == "__main__":
    main()
