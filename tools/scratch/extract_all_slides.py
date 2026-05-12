"""Extract text + images from every slide in the Accenture pptx.

Writes:
  - tools/scratch/accenture_all_slides.json  (machine-readable index)
  - tools/scratch/accenture_all_slides.md    (human-readable preview)
  - tools/scratch/jcp_slide_images/slide_<n>/img_<NN>.<ext>  (every embedded image)
"""
from __future__ import annotations

import json
import re
import shutil
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
PPTX = ROOT / "docs" / "jcp-notes-compilation" / "Updated Retail Platforms+Agents_ Accenture - Apr 16, 2026-2.pptx"
OUT_DIR = Path(__file__).parent
OUT_JSON = OUT_DIR / "accenture_all_slides.json"
OUT_MD = OUT_DIR / "accenture_all_slides.md"
OUT_IMG = OUT_DIR / "jcp_slide_images"


def text_of_slide(z: zipfile.ZipFile, name: str) -> list[str]:
    root = ET.fromstring(z.read(name))
    runs = []
    for t in root.iter("{http://schemas.openxmlformats.org/drawingml/2006/main}t"):
        if t.text and t.text.strip():
            runs.append(t.text.strip())
    return runs


def image_rels_for(z: zipfile.ZipFile, name: str) -> list[str]:
    rels_path = name.replace("slides/slide", "slides/_rels/slide") + ".rels"
    try:
        rels_root = ET.fromstring(z.read(rels_path))
    except KeyError:
        return []
    targets = []
    for rel in rels_root.findall("{http://schemas.openxmlformats.org/package/2006/relationships}Relationship"):
        target = rel.get("Target", "")
        if "/media/" in target:
            normalized = target.replace("../", "ppt/")
            targets.append(normalized)
    return targets


def main():
    if OUT_IMG.exists():
        # Don't wipe existing slide_31..35 dirs (already curated). Only refresh missing slides.
        pass
    OUT_IMG.mkdir(parents=True, exist_ok=True)

    index = []
    with zipfile.ZipFile(PPTX) as z:
        slide_names = sorted(
            (n for n in z.namelist() if re.match(r"ppt/slides/slide\d+\.xml$", n)),
            key=lambda n: int(re.search(r"slide(\d+)\.xml", n).group(1)),
        )
        print(f"Total slides: {len(slide_names)}")
        for slide_name in slide_names:
            n = int(re.search(r"slide(\d+)\.xml", slide_name).group(1))
            runs = text_of_slide(z, slide_name)
            text = " · ".join(runs)
            # Extract images
            slide_dir = OUT_IMG / f"slide_{n}"
            if not slide_dir.exists():
                slide_dir.mkdir(parents=True)
                for i, rel in enumerate(image_rels_for(z, slide_name), start=1):
                    if rel not in z.namelist():
                        continue
                    ext = rel.split(".")[-1].lower()
                    out = slide_dir / f"img_{i:02d}.{ext}"
                    out.write_bytes(z.read(rel))
            n_imgs = len(list(slide_dir.iterdir()))
            # Title heuristic = first run
            title = runs[0] if runs else "(no text)"
            index.append({
                "slide": n,
                "title": title[:120],
                "n_runs": len(runs),
                "text_chars": len(text),
                "n_images": n_imgs,
                "text": text,
            })
            print(f"  · slide {n:>2}: {title[:70]}  ({n_imgs} imgs)")

    OUT_JSON.write_text(json.dumps(index, indent=2))
    # Build a readable markdown index
    lines = ["# Accenture deck · all slides text + image counts\n"]
    lines.append("> Source: `docs/jcp-notes-compilation/Updated Retail Platforms+Agents_ Accenture - Apr 16, 2026-2.pptx`")
    lines.append(f"> Extracted: 2026-05-01 · {len(index)} slides total\n")
    for it in index:
        lines.append(f"## slide {it['slide']} · {it['title']}")
        lines.append(f"_{it['n_images']} images · {it['text_chars']} chars text_")
        lines.append("")
        if it["text"]:
            lines.append("```")
            lines.append(it["text"])
            lines.append("```")
        lines.append("")
    OUT_MD.write_text("\n".join(lines))
    print(f"\nWrote {OUT_JSON} ({len(index)} slides)")
    print(f"Wrote {OUT_MD}")


if __name__ == "__main__":
    main()
