"""One-shot: pull slides 31-35 (JCP material) out of the Accenture PPTX.

Writes:
  - tools/scratch/jcp_slides_31_35.txt   (concatenated text per slide)
  - tools/scratch/jcp_slide_images/<slide_n>/<imgN.png|jpg>  (embedded images)

PPTX is a zip — no soffice or python-pptx needed.
"""
from __future__ import annotations

import re
import shutil
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
PPTX = ROOT / "docs" / "jcp-notes-compilation" / "Updated Retail Platforms+Agents_ Accenture - Apr 16, 2026-2.pptx"
OUT_TXT = Path(__file__).parent / "jcp_slides_31_35.txt"
OUT_IMG = Path(__file__).parent / "jcp_slide_images"

NS = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
}

SLIDES_WANTED = list(range(31, 36))  # 31, 32, 33, 34, 35


def text_of_slide(z: zipfile.ZipFile, name: str) -> str:
    root = ET.fromstring(z.read(name))
    runs = []
    for t in root.iter("{http://schemas.openxmlformats.org/drawingml/2006/main}t"):
        if t.text:
            runs.append(t.text)
    return "\n".join(runs)


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
            # paths are relative to the slide; resolve to ppt/media/...
            normalized = target.replace("../", "ppt/")
            targets.append(normalized)
    return targets


def main():
    if OUT_IMG.exists():
        shutil.rmtree(OUT_IMG)
    OUT_IMG.mkdir(parents=True)

    text_chunks = []
    with zipfile.ZipFile(PPTX) as z:
        slide_names = sorted(
            (n for n in z.namelist() if re.match(r"ppt/slides/slide\d+\.xml$", n)),
            key=lambda n: int(re.search(r"slide(\d+)\.xml", n).group(1)),
        )
        print(f"Total slides: {len(slide_names)}")
        for n_str in SLIDES_WANTED:
            slide_name = f"ppt/slides/slide{n_str}.xml"
            if slide_name not in z.namelist():
                print(f"  · slide {n_str} not found — skipping")
                continue
            text = text_of_slide(z, slide_name)
            text_chunks.append(f"================ SLIDE {n_str} ================\n{text}\n")
            # Pull images
            slide_dir = OUT_IMG / f"slide_{n_str}"
            slide_dir.mkdir()
            for i, rel in enumerate(image_rels_for(z, slide_name), start=1):
                if rel not in z.namelist():
                    continue
                ext = rel.split(".")[-1].lower()
                out = slide_dir / f"img_{i:02d}.{ext}"
                out.write_bytes(z.read(rel))
            n_imgs = len(list(slide_dir.iterdir()))
            print(f"  · slide {n_str}: text {len(text)} chars · {n_imgs} images")

    OUT_TXT.write_text("\n".join(text_chunks))
    print(f"\nWrote {OUT_TXT}")
    print(f"Wrote images under {OUT_IMG}")


if __name__ == "__main__":
    main()
