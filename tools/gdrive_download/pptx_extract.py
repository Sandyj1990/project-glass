"""Extract embedded images from a .pptx file, slide by slide.

A .pptx is a ZIP. Each slide's relationships file lists the media items it
references; the slide XML itself defines the visual order (z-order) and
positioning of each picture. We walk the slide XML in document order so the
exported sequence matches the visual layout.

Output layout (designed for GCS / CDN serving):

    <output_root>/<brand>/<linesheet_slug>/slide-NNN/SS.<ext>

`SS` is the 1-based sequence within the slide (z-order).
"""

from __future__ import annotations

import hashlib
import io
import logging
import re
import zipfile
from dataclasses import asdict, dataclass, field
from pathlib import Path
from xml.etree import ElementTree as ET

from PIL import Image

log = logging.getLogger(__name__)

NS = {
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "rels": "http://schemas.openxmlformats.org/package/2006/relationships",
}

EMU_PER_PIXEL = 9525  # PowerPoint EMU → pixels at 96 DPI


def slugify(text: str) -> str:
    """URL-safe slug suitable for path segments and CDN URLs."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-") or "untitled"


# Canonical category slugs. Map every recognized variant to the canonical form
# used in the index and pivot views. Keep canonical names singular to match
# retail catalog conventions.
CATEGORY_ALIASES = {
    "t-shirt": "t-shirt",
    "t-shirts": "t-shirt",
    "stripe-shirt": "stripe-shirt",
    "stripe-shirts": "stripe-shirt",
    "printed-shirts": "printed-shirt",
    "printed-shirt": "printed-shirt",
    "aop-polos": "aop-polo",
    "aop-polo": "aop-polo",
    "aop-shirts": "aop-shirt",
    "aop-shirt": "aop-shirt",
    "polo-t-shirts": "polo",
    "polo": "polo",
    "leggings": "leggings",
    "shirt": "shirt",
    "shirts": "shirt",
    "shacket": "shacket",
    "sweatshirt": "sweatshirt",
    "sweatshirts": "sweatshirt",
    "henley-tee": "henley-tee",
    "co-ord-sets": "co-ord-set",
    "co-ord-set": "co-ord-set",
}


def category_slug(raw: str) -> str:
    """Slugify a category and apply alias normalization."""
    base = slugify(raw)
    return CATEGORY_ALIASES.get(base, base)


def _slide_sort_key(name: str) -> int:
    m = re.search(r"slide(\d+)\.xml$", name)
    return int(m.group(1)) if m else 0


def _emu_to_px(emu: str | None) -> int | None:
    try:
        return int(emu) // EMU_PER_PIXEL if emu else None
    except (TypeError, ValueError):
        return None


@dataclass
class ImageRecord:
    brand: str
    linesheet: str
    linesheet_slug: str
    source_file: str
    slide_number: int
    slide_title: str
    seq_in_slide: int
    path: str  # relative to output root, used as CDN key
    original_media: str
    mime_type: str
    bytes: int
    width: int | None
    height: int | None
    sha256: str
    slide_position_emu: dict | None = None  # {"x", "y", "cx", "cy"} from <a:xfrm>
    gender: str | None = None  # "womens" | "mens" | "kids" | "kids-boys" | "kids-girls" | None
    category: str | None = None  # raw extracted, e.g. "Shirt Dress"
    category_slug: str | None = None  # slugified, e.g. "shirt-dress"
    theme: str | None = None  # optional concept/theme tag (e.g. Lee Cooper "Sun Drenched Escape")
    theme_slug: str | None = None

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class LinesheetResult:
    brand: str
    linesheet: str
    linesheet_slug: str
    source_file: str
    slide_count: int
    images: list[ImageRecord] = field(default_factory=list)
    slide_texts: dict[int, str] = field(default_factory=dict)  # slide_num -> joined text


def _parse_rels(z: zipfile.ZipFile, slide_name: str) -> dict[str, str]:
    """Return {rId: media path inside zip} for one slide."""
    rels_name = slide_name.replace("ppt/slides/", "ppt/slides/_rels/") + ".rels"
    try:
        data = z.read(rels_name)
    except KeyError:
        return {}
    root = ET.fromstring(data)
    out: dict[str, str] = {}
    for rel in root.findall(f"{{{NS['rels']}}}Relationship"):
        target = rel.get("Target", "")
        if "../media/" not in target:
            continue
        # Targets are relative to ppt/slides/, so '../media/imageX.png' → 'ppt/media/imageX.png'.
        media_path = "ppt/" + target.split("../", 1)[1]
        out[rel.get("Id", "")] = media_path
    return out


def _extract_text(slide_root: ET.Element) -> str:
    parts: list[str] = []
    for t in slide_root.iter(f"{{{NS['a']}}}t"):
        if t.text:
            parts.append(t.text)
    # Collapse whitespace.
    text = " ".join(parts)
    return re.sub(r"\s+", " ", text).strip()


def _find_pictures_in_order(slide_root: ET.Element) -> list[tuple[str, dict | None]]:
    """Walk the slide tree in document order and return [(rId, position_dict_or_None), ...].

    Document order matches PowerPoint z-order, which is a stable proxy for visual order.
    """
    results: list[tuple[str, dict | None]] = []
    for pic in slide_root.iter(f"{{{NS['p']}}}pic"):
        blip = pic.find(f".//{{{NS['a']}}}blip")
        if blip is None:
            continue
        r_embed = blip.get(f"{{{NS['r']}}}embed")
        if not r_embed:
            continue
        position: dict | None = None
        xfrm = pic.find(f".//{{{NS['p']}}}spPr/{{{NS['a']}}}xfrm")
        if xfrm is not None:
            off = xfrm.find(f"{{{NS['a']}}}off")
            ext = xfrm.find(f"{{{NS['a']}}}ext")
            position = {
                "x": int(off.get("x")) if off is not None and off.get("x") else None,
                "y": int(off.get("y")) if off is not None and off.get("y") else None,
                "cx": int(ext.get("cx")) if ext is not None and ext.get("cx") else None,
                "cy": int(ext.get("cy")) if ext is not None and ext.get("cy") else None,
            }
        results.append((r_embed, position))
    return results


def _image_dimensions(data: bytes) -> tuple[int | None, int | None]:
    try:
        with Image.open(io.BytesIO(data)) as img:
            return img.size
    except Exception:
        return None, None


# ============================================================================
# Per-deck slide metadata strategies.
#
# A strategy is a callable that takes the full {slide_num: slide_text} dict
# and returns {slide_num: {category, gender, theme}}. Any of the inner keys
# may be omitted; missing values fall back to deck-level config.
# Returning a sparse dict (only design slides) is fine.
# ============================================================================

_NUMBERED_DESIGN_RE = re.compile(r"^\s*\d+\.\s+(.+?)\s+Silhouette\s*:", re.IGNORECASE)
_RANGE_PLAN_RE = re.compile(r"^(.+?)\s+Range\s+Plan\s*:\s*\d+\s*/\s*\d+", re.IGNORECASE)


def _normalize_category(text: str) -> str:
    """Collapse whitespace and fix split words like "T- Shirts" → "T-Shirts"."""
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"\b([A-Za-z]+)-\s+([A-Za-z]+)\b", r"\1-\2", text)
    return text


def _strategy_numbered_design(slide_texts: dict[int, str]) -> dict[int, dict]:
    """Cross-brand deck: "1. Dress Silhouette: Tiered Dress ..."."""
    out: dict[int, dict] = {}
    for sn, text in slide_texts.items():
        if not text or "Silhouette" not in text:
            continue
        m = _NUMBERED_DESIGN_RE.match(text)
        if m:
            cat = m.group(1).strip()
            if len(cat) <= 60:
                out[sn] = {"category": cat}
    return out


def _strategy_jpj_range_plan(slide_texts: dict[int, str]) -> dict[int, dict]:
    """John Players Jeans: each design slide is "<Category> Range Plan : N/N"."""
    out: dict[int, dict] = {}
    for sn, text in slide_texts.items():
        m = _RANGE_PLAN_RE.match(text)
        if m:
            out[sn] = {"category": _normalize_category(m.group(1))}
    return out


def _make_section_header_carry_strategy(known_sections: set[str]):
    """KG Frendz / similar: short slides like "T-shirts" / "Leggings" set the
    category for subsequent design slides until the next section header.
    """
    known_lower = {s.lower() for s in known_sections}

    def strat(slide_texts: dict[int, str]) -> dict[int, dict]:
        out: dict[int, dict] = {}
        current_category: str | None = None
        for sn in sorted(slide_texts):
            text = (slide_texts[sn] or "").strip()
            tl = text.lower()
            # Detect a section-header slide: short text equal (or starting with)
            # one of the known categories.
            is_header = False
            if 1 <= len(text) <= 40:
                for sect in known_lower:
                    if tl == sect or tl.startswith(sect + " "):
                        current_category = sect
                        is_header = True
                        break
            if is_header:
                continue
            # Treat as a design slide if it mentions Silhouette / Style Detail
            # and we have an active section.
            if current_category and ("silhouette" in tl or "style detail" in tl):
                out[sn] = {"category": current_category}
        return out

    return strat


def _strategy_ajio(slide_texts: dict[int, str]) -> dict[int, dict]:
    """Ajio Licensed Only: per-slide T-shirt category with mid-deck gender shift.

    Slides 1..N are womenswear, then a divider mentioning "Menswear" flips
    subsequent slides to mens. Each design slide ("Style Detail ...") is a
    T-shirt; we don't try to subdivide oversized vs. regular fit.
    """
    out: dict[int, dict] = {}
    current_gender: str | None = None
    for sn in sorted(slide_texts):
        text = slide_texts[sn] or ""
        tl = text.lower()
        # Section dividers are short slides whose text mentions menswear/womenswear.
        # Check womenswear first — "menswear" is a substring of "womenswear".
        if len(text) < 200:
            if "womenswear" in tl and "overview" not in tl:
                current_gender = "womens"
            elif "menswear" in tl and "overview" not in tl:
                current_gender = "mens"
        # Design slides start with "Style Detail" and contain "T-Shirt".
        if "style detail" in tl and "t-shirt" in tl:
            meta = {"category": "T-Shirt"}
            if current_gender:
                meta["gender"] = current_gender
            out[sn] = meta
    return out


def _strategy_rio_sweatshirt(slide_texts: dict[int, str]) -> dict[int, dict]:
    """Rio AW26: every design slide is a "* Crew Sweatshirt"."""
    out: dict[int, dict] = {}
    current_theme: str | None = None
    for sn in sorted(slide_texts):
        text = slide_texts[sn] or ""
        tl = text.lower()
        # Short divider slides (e.g. "AOP", "EMBELLISHED", "L icensed") set theme.
        if 1 <= len(text.strip()) <= 30 and "sweatshirt" not in tl:
            current_theme = re.sub(r"\s+", " ", text).strip()
            continue
        if "sweatshirt" in tl and ("silhouette description" in tl or "style detail" in tl):
            meta: dict = {"category": "Sweatshirt"}
            if current_theme:
                meta["theme"] = current_theme
            out[sn] = meta
    return out


def _strategy_superdry_url(slide_texts: dict[int, str]) -> dict[int, dict]:
    """Superdry: design slides contain a product URL whose slug ends in the category."""
    out: dict[int, dict] = {}
    for sn, text in slide_texts.items():
        tl = (text or "").lower()
        # Try most specific to least specific.
        cat: str | None = None
        if "ajio.com/superdry-" not in tl:
            continue
        if re.search(r"shacket", tl):
            cat = "Shacket"
        elif re.search(r"resort-collar-shirt|fit-shirt(?:[/?]|$)", tl):
            cat = "Shirt"
        elif re.search(r"\bt-shirt\b", tl):
            cat = "T-Shirt"
        elif re.search(r"\bpolo\b", tl):
            cat = "Polo"
        if cat:
            out[sn] = {"category": cat}
    return out


def _strategy_lee_cooper(slide_texts: dict[int, str]) -> dict[int, dict]:
    """Lee Cooper Kids: range-plan slides bundle T-SHIRT/POLO/HENLEY TEE/CO-ORD SETS
    in a single slide, so per-image category isn't recoverable from text. We tag
    the *theme* (Sun Drenched Escape, etc.) instead and leave category null.
    """
    out: dict[int, dict] = {}
    current_theme: str | None = None
    concept_re = re.compile(r"CONCEPT\s+\d+\s*[-–]\s*(.+)", re.IGNORECASE)
    for sn in sorted(slide_texts):
        text = slide_texts[sn] or ""
        m = concept_re.match(text.strip())
        if m:
            current_theme = m.group(1).strip()
            continue
        if current_theme and "range plan" in text.lower():
            out[sn] = {"theme": current_theme}
    return out


# Section vocabulary used by the section-header-carry strategy for KG Frendz.
KG_FRENDZ_SECTIONS = {"T-shirts", "Leggings", "Co-ord Sets", "Tops", "Shirts"}


CATEGORY_STRATEGIES = {
    "numbered_design": _strategy_numbered_design,
    "jpj_range_plan": _strategy_jpj_range_plan,
    "ajio": _strategy_ajio,
    "rio_sweatshirt": _strategy_rio_sweatshirt,
    "superdry_url": _strategy_superdry_url,
    "lee_cooper": _strategy_lee_cooper,
    "kg_frendz": _make_section_header_carry_strategy(KG_FRENDZ_SECTIONS),
    "none": lambda _texts: {},
}


# Backward compat for the older single-text helper used in tests/probes.
def parse_numbered_design_category(slide_text: str) -> str | None:
    res = _strategy_numbered_design({1: slide_text})
    return res.get(1, {}).get("category")


def extract_linesheet(
    pptx_path: Path,
    brand: str,
    linesheet: str,
    output_root: Path,
    linesheet_slug: str | None = None,
    gender: str | None = None,
    category_strategy: str = "none",
) -> LinesheetResult:
    linesheet_slug = linesheet_slug or slugify(linesheet)
    strategy_fn = CATEGORY_STRATEGIES.get(category_strategy, CATEGORY_STRATEGIES["none"])
    result = LinesheetResult(
        brand=brand,
        linesheet=linesheet,
        linesheet_slug=linesheet_slug,
        source_file=pptx_path.name,
        slide_count=0,
    )

    with zipfile.ZipFile(pptx_path) as z:
        slide_names = sorted(
            (n for n in z.namelist() if n.startswith("ppt/slides/slide") and n.endswith(".xml")),
            key=_slide_sort_key,
        )
        result.slide_count = len(slide_names)
        log.info("Extracting %s: %d slides", pptx_path.name, len(slide_names))

        # First pass: read every slide's text so the strategy can use cross-slide context.
        slide_roots: dict[int, ET.Element] = {}
        for slide_name in slide_names:
            sn = _slide_sort_key(slide_name)
            root = ET.fromstring(z.read(slide_name))
            slide_roots[sn] = root
            result.slide_texts[sn] = _extract_text(root)

        # Run the per-deck strategy across all slides at once.
        slide_meta = strategy_fn(result.slide_texts)

        for slide_name in slide_names:
            slide_num = _slide_sort_key(slide_name)
            slide_root = slide_roots[slide_num]
            slide_text = result.slide_texts[slide_num]
            slide_title = slide_text[:80] if slide_text else ""
            meta = slide_meta.get(slide_num, {})
            slide_category = meta.get("category")
            slide_category_slug = category_slug(slide_category) if slide_category else None
            slide_gender = meta.get("gender") or gender
            slide_theme = meta.get("theme")
            slide_theme_slug = slugify(slide_theme) if slide_theme else None

            rels = _parse_rels(z, slide_name)
            pictures = _find_pictures_in_order(slide_root)
            if not pictures:
                continue

            slide_dir_rel = f"{brand}/{linesheet_slug}/slide-{slide_num:03d}"
            slide_dir = output_root / slide_dir_rel
            slide_dir.mkdir(parents=True, exist_ok=True)

            seq = 0
            for r_id, position in pictures:
                media_path = rels.get(r_id)
                if not media_path:
                    continue
                try:
                    data = z.read(media_path)
                except KeyError:
                    log.warning("Slide %d references missing media %s", slide_num, media_path)
                    continue

                ext = Path(media_path).suffix.lower() or ".bin"
                # Some pptx files store WMF/EMF; skip vector blobs that aren't images.
                if ext in {".wmf", ".emf"}:
                    log.debug("Skipping vector blob %s", media_path)
                    continue

                seq += 1
                filename = f"{seq:02d}{ext}"
                dest = slide_dir / filename
                dest.write_bytes(data)
                width, height = _image_dimensions(data)
                sha256 = hashlib.sha256(data).hexdigest()
                mime = {
                    ".jpg": "image/jpeg",
                    ".jpeg": "image/jpeg",
                    ".png": "image/png",
                    ".gif": "image/gif",
                    ".webp": "image/webp",
                    ".bmp": "image/bmp",
                    ".tiff": "image/tiff",
                    ".tif": "image/tiff",
                    ".svg": "image/svg+xml",
                }.get(ext, "application/octet-stream")

                result.images.append(
                    ImageRecord(
                        brand=brand,
                        linesheet=linesheet,
                        linesheet_slug=linesheet_slug,
                        source_file=pptx_path.name,
                        slide_number=slide_num,
                        slide_title=slide_title,
                        seq_in_slide=seq,
                        path=f"{slide_dir_rel}/{filename}",
                        original_media=Path(media_path).name,
                        mime_type=mime,
                        bytes=len(data),
                        width=width,
                        height=height,
                        sha256=sha256,
                        slide_position_emu=position,
                        gender=slide_gender,
                        category=slide_category,
                        category_slug=slide_category_slug,
                        theme=slide_theme,
                        theme_slug=slide_theme_slug,
                    )
                )

    log.info(
        "Extracted %d images from %s across %d slides",
        len(result.images),
        pptx_path.name,
        result.slide_count,
    )
    return result
