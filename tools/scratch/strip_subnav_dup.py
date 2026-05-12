"""One-shot: strip stale .subnav-link inline duplicates from 13 affected pages.
Pure duplicates of the pre-sweep canonical — removing them lets style.css win."""
from pathlib import Path

FILES = [
    "jcp/channels/index.html",
    "impetus/brands/index.html",
    "impetus/photoshoots/index.html",
    "impetus/photoshoots/ss26-plm-ai-photoshoot-pilot/index.html",
    "impetus/photoshoots/buda-jeans-harry-potter/index.html",
    "impetus/photoshoots/ajio-asos-plus-size-launch/index.html",
    "impetus/category-intel/index.html",
    "impetus/category-intel/midi-dress-ss27-india/index.html",
    "impetus/photoshoots/buda-jeans-valentines/index.html",
    "impetus/category-intel/mens-shirts-ss27-india/index.html",
    "impetus/category-intel/mens-polos-aw26-india/index.html",
    "impetus/category-intel/mens-tshirts-ss27-india/index.html",
    "pixelbin/videos/index.html",
]

OLD = """.subnav-link {
  font-family: 'JetBrains Mono', monospace; font-size: 11px;
  text-transform: uppercase; letter-spacing: 0.04em; color: var(--ink-muted);
  padding: 8px 14px; border-radius: 999px; border: 1px solid var(--border);
  transition: all 0.15s;
}
.subnav-link:hover { border-color: var(--ink); color: var(--ink); }
.subnav-link.active { background: var(--ink); color: white; border-color: var(--ink); }
"""


def main():
    for f in FILES:
        p = Path(f)
        src = p.read_text()
        count = src.count(OLD)
        if count == 0:
            print(f"SKIP {f}: block not found (already stripped?)")
            continue
        if count > 1:
            print(f"FAIL {f}: found {count} matches, expected 1")
            continue
        new = src.replace(OLD, "")
        p.write_text(new)
        delta = len(src) - len(new)
        ok = delta == len(OLD)
        print(f"{'OK  ' if ok else 'FAIL'} {f}: removed {delta} bytes")


if __name__ == "__main__":
    main()
