"""Extract text + images from selected slides of the GlamAR pptx.

Usage: edit SLIDES below; outputs go to tools/scratch/glamar_slides/.
"""
from __future__ import annotations

import re
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
PPTX = ROOT / "docs" / "glamar-notes-compilation" / "AI & SaaS | GlamAR.pptx"
OUT_DIR = Path(__file__).parent / "glamar_slides"

SLIDES = [16, 20, 26]


def text_of_slide(z: zipfile.ZipFile, name: str) -> list[str]:
    root = ET.fromstring(z.read(name))
    return [
        t.text.strip()
        for t in root.iter("{http://schemas.openxmlformats.org/drawingml/2006/main}t")
        if t.text and t.text.strip()
    ]


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
            targets.append(target.replace("../", "ppt/"))
    return targets


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(PPTX) as z:
        for n in SLIDES:
            slide_name = f"ppt/slides/slide{n}.xml"
            if slide_name not in z.namelist():
                print(f"slide{n} not found")
                continue
            text = text_of_slide(z, slide_name)
            img_paths = image_rels_for(z, slide_name)
            slide_dir = OUT_DIR / f"slide_{n}"
            slide_dir.mkdir(parents=True, exist_ok=True)
            (slide_dir / "text.txt").write_text(" · ".join(text))
            for i, p in enumerate(img_paths, start=1):
                ext = Path(p).suffix
                try:
                    data = z.read(p)
                except KeyError:
                    print(f"  missing media {p}")
                    continue
                (slide_dir / f"img_{i:02d}{ext}").write_bytes(data)
            print(f"slide {n} · {len(text)} text runs · {len(img_paths)} images")


if __name__ == "__main__":
    main()
