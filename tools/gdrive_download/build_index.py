"""Run pptx extraction over a fixed set of linesheets and emit an index.

Usage:
    python -m gdrive_download.build_index \
        --pptx-dir . \
        --output images \
        [--cdn-base https://cdn.example.com/]
"""

from __future__ import annotations

import argparse
import json
import logging
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

from .pptx_extract import LinesheetResult, category_slug, extract_linesheet, slugify

log = logging.getLogger("build_index")


# Per-deck plan. `gender` is set at deck level (slide 1 / filename evidence).
# `category_strategy` chooses how to extract per-slide category text:
#   - "numbered_design": parse "N. <Category> | Silhouette: ..." (cross-brand deck)
#   - "none": leave category null; rely on overrides.json for manual tagging.
LINESHEET_PLAN: list[dict] = [
    {
        "file": "Fynd Create x Ajio Linesheet Jan 15 2026 V3 (Licensed Only).pptx",
        "brand": "ajio",
        "linesheet": "Ajio Licensed Only Jan 15 2026 V3",
        "gender": "womens",  # default; mid-deck shifts to mens via strategy
        "category_strategy": "ajio",
    },
    {
        "file": "Fynd Create x John Players Jeans S_S 27 Apr 27 2026 V3 .pptx",
        "brand": "john-players-jeans",
        "linesheet": "John Players Jeans SS27 Apr 27 2026 V3",
        "gender": "mens",
        "category_strategy": "jpj_range_plan",
    },
    {
        "file": "Fynd Create X KG Frendz AW26.pptx",
        "brand": "kg-frendz",
        "linesheet": "KG Frendz AW26",
        "gender": "kids",
        "category_strategy": "kg_frendz",
    },
    {
        "file": "Fynd Create X Lee Cooper Kids SS'27 Linesheet V1.pptx",
        "brand": "lee-cooper-kids",
        "linesheet": "Lee Cooper Kids SS27 V1",
        "gender": "kids-boys",
        # Range-plan slides bundle multiple categories; we tag theme only.
        "category_strategy": "lee_cooper",
    },
    {
        "file": "Fynd Create x Rio AW26 (Womenswear) V2.pptx",
        "brand": "rio",
        "linesheet": "Rio AW26 Womenswear V2",
        "gender": "womens",
        "category_strategy": "rio_sweatshirt",
    },
    {
        "file": "Fynd Create x Superdry.pptx",
        "brand": "superdry",
        "linesheet": "Superdry",
        "gender": "mens",  # URLs reference men's items
        "category_strategy": "superdry_url",
    },
    {
        "file": "Designs for Rio, Fig & DNMX.pptx",
        "brand": None,  # multi-brand → currently lands in _unsorted
        "linesheet": "Designs for Rio, Fig & DNMX",
        "gender": "womens",  # slide 1: "Womens Western Wear"
        "category_strategy": "numbered_design",
    },
]

# Keywords used to classify slides in the multi-brand deck.
# Order matters: longer/more-specific keywords first.
MULTI_BRAND_KEYWORDS = [
    ("dnmx", "dnmx"),
    ("dnm-x", "dnmx"),
    ("rio", "rio"),
    ("fig", "fig"),
]


def classify_slide(text: str) -> str | None:
    """Return a brand slug for a slide based on its text, or None if ambiguous."""
    if not text:
        return None
    lower = text.lower()
    matched: list[str] = []
    for kw, brand in MULTI_BRAND_KEYWORDS:
        if re.search(rf"\b{re.escape(kw)}\b", lower) and brand not in matched:
            matched.append(brand)
    if len(matched) == 1:
        return matched[0]
    return None  # zero or multiple matches → leave for human triage


def reclassify_multi_brand(
    pptx_path: Path,
    plan: dict,
    output_root: Path,
) -> list[LinesheetResult]:
    """Extract a multi-brand deck once, then re-organize images per detected brand.

    Each slide's images move to <brand>/<linesheet_slug>/slide-NNN/. Slides that
    can't be classified land in `_unsorted/<linesheet_slug>/slide-NNN/`.
    """
    base_label = plan["linesheet"]
    base_slug = slugify(base_label)
    # First extract everything under a temp brand folder.
    staging_brand = "_staging"
    staging = extract_linesheet(
        pptx_path=pptx_path,
        brand=staging_brand,
        linesheet=base_label,
        output_root=output_root,
        linesheet_slug=base_slug,
        gender=plan.get("gender"),
        category_strategy=plan.get("category_strategy", "none"),
    )

    # Bucket images per detected brand. We rewrite paths and move files.
    grouped: dict[str, list] = defaultdict(list)
    for img in staging.images:
        slide_text = staging.slide_texts.get(img.slide_number, "")
        detected = classify_slide(slide_text) or "_unsorted"
        # Rewrite path.
        new_path_rel = (
            f"{detected}/{base_slug}/slide-{img.slide_number:03d}/"
            f"{img.seq_in_slide:02d}{Path(img.path).suffix}"
        )
        old_abs = output_root / img.path
        new_abs = output_root / new_path_rel
        new_abs.parent.mkdir(parents=True, exist_ok=True)
        old_abs.replace(new_abs)
        img.brand = detected
        img.path = new_path_rel
        grouped[detected].append(img)

    # Remove the now-empty staging tree.
    staging_root = output_root / staging_brand
    if staging_root.exists():
        for p in sorted(staging_root.rglob("*"), reverse=True):
            if p.is_dir():
                try:
                    p.rmdir()
                except OSError:
                    pass
        try:
            staging_root.rmdir()
        except OSError:
            pass

    # Build one LinesheetResult per detected brand for indexing.
    results: list[LinesheetResult] = []
    for brand, imgs in grouped.items():
        r = LinesheetResult(
            brand=brand,
            linesheet=base_label,
            linesheet_slug=base_slug,
            source_file=pptx_path.name,
            slide_count=staging.slide_count,
        )
        r.images = imgs
        # Carry slide texts only for slides that ended up in this brand.
        slides_in_brand = {img.slide_number for img in imgs}
        r.slide_texts = {
            n: t for n, t in staging.slide_texts.items() if n in slides_in_brand
        }
        results.append(r)
    return results


def _load_overrides(path: Path) -> dict:
    """Load optional per-image / per-prefix overrides for gender and category.

    Schema:
        {
          "byPath": {
            "<exact image path>": {"gender": "...", "category": "...", "brand": "..."}
          },
          "byPrefix": {
            "<path prefix>": {"gender": "...", "category": "...", "brand": "..."}
          }
        }
    """
    if not path.exists():
        return {"byPath": {}, "byPrefix": {}}
    raw = json.loads(path.read_text())
    return {"byPath": raw.get("byPath", {}), "byPrefix": raw.get("byPrefix", {})}


def _apply_overrides(record: dict, overrides: dict) -> dict:
    path = record["path"]
    out = dict(record)
    for prefix, fields in overrides["byPrefix"].items():
        if path.startswith(prefix):
            for k, v in fields.items():
                if v is not None:
                    out[k] = v
                    if k == "category":
                        out["category_slug"] = slugify(v)
    if path in overrides["byPath"]:
        for k, v in overrides["byPath"][path].items():
            if v is not None:
                out[k] = v
                if k == "category":
                    out["category_slug"] = category_slug(v)
    return out


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Extract images from linesheets and build a CDN-ready index.")
    p.add_argument("--pptx-dir", default=".", help="Directory containing .pptx files.")
    p.add_argument("--output", default="images", help="Output directory for extracted images.")
    p.add_argument(
        "--cdn-base",
        default="",
        help="Optional CDN URL base; included in index for client convenience.",
    )
    p.add_argument(
        "--overrides",
        default="overrides.json",
        help="Optional path to manual overrides JSON (gender/category/brand by path or prefix).",
    )
    p.add_argument("--log-level", default="INFO")
    args = p.parse_args(argv)

    logging.basicConfig(
        level=getattr(logging, args.log_level),
        format="%(asctime)s %(levelname)-5s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    pptx_dir = Path(args.pptx_dir).resolve()
    output_root = Path(args.output).resolve()
    output_root.mkdir(parents=True, exist_ok=True)

    all_results: list[LinesheetResult] = []
    missing: list[str] = []

    for plan in LINESHEET_PLAN:
        pptx_path = pptx_dir / plan["file"]
        if not pptx_path.exists():
            log.warning("Missing: %s", pptx_path.name)
            missing.append(plan["file"])
            continue
        log.info("Processing: %s", pptx_path.name)
        if plan["brand"] is None:
            results = reclassify_multi_brand(pptx_path, plan, output_root)
            all_results.extend(results)
        else:
            r = extract_linesheet(
                pptx_path=pptx_path,
                brand=plan["brand"],
                linesheet=plan["linesheet"],
                output_root=output_root,
                linesheet_slug=slugify(plan["linesheet"]),
                gender=plan.get("gender"),
                category_strategy=plan.get("category_strategy", "none"),
            )
            all_results.append(r)

    # Load optional overrides.
    overrides = _load_overrides(Path(args.overrides))

    # Flatten + apply overrides + capture aggregations.
    flat_images: list[dict] = []
    by_brand: dict[str, dict] = defaultdict(lambda: {"linesheets": defaultdict(list)})
    by_gender: dict[str, list[str]] = defaultdict(list)
    by_category: dict[str, list[str]] = defaultdict(list)
    by_gender_category: dict[str, list[str]] = defaultdict(list)
    by_gender_category_brand: dict[str, list[str]] = defaultdict(list)
    total_bytes = 0
    seen_hashes: set[str] = set()
    duplicates = 0

    for r in all_results:
        for img in r.images:
            d = img.to_dict()
            d = _apply_overrides(d, overrides)
            if args.cdn_base:
                d["url"] = args.cdn_base.rstrip("/") + "/" + d["path"]
            flat_images.append(d)
            by_brand[d["brand"]]["linesheets"][d["linesheet_slug"]].append(d)
            total_bytes += d["bytes"]
            if d["sha256"] in seen_hashes:
                duplicates += 1
            else:
                seen_hashes.add(d["sha256"])

            g = d.get("gender") or "_unknown"
            c = d.get("category_slug") or "_unknown"
            by_gender[g].append(d["path"])
            by_category[c].append(d["path"])
            by_gender_category[f"{g}/{c}"].append(d["path"])
            by_gender_category_brand[f"{g}/{c}/{d['brand']}"].append(d["path"])

    # Sorted, stable index shape.
    index = {
        "generatedAt": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "cdnBase": args.cdn_base or None,
        "overridesApplied": bool(overrides["byPath"] or overrides["byPrefix"]),
        "totals": {
            "brands": len(by_brand),
            "images": len(flat_images),
            "uniqueImagesBySha256": len(seen_hashes),
            "duplicateImageInstances": duplicates,
            "bytes": total_bytes,
        },
        "missingFiles": missing,
        "brands": {},
        "byGender": {k: sorted(v) for k, v in sorted(by_gender.items())},
        "byCategory": {k: sorted(v) for k, v in sorted(by_category.items())},
        "byGenderCategory": {k: sorted(v) for k, v in sorted(by_gender_category.items())},
        "byGenderCategoryBrand": {
            k: sorted(v) for k, v in sorted(by_gender_category_brand.items())
        },
    }
    for brand in sorted(by_brand):
        sheets = by_brand[brand]["linesheets"]
        index["brands"][brand] = {
            "linesheets": {
                slug: sorted(
                    sheets[slug],
                    key=lambda x: (x["slide_number"], x["seq_in_slide"]),
                )
                for slug in sorted(sheets)
            },
            "imageCount": sum(len(v) for v in sheets.values()),
        }

    index_path = output_root / "index.json"
    index_path.write_text(json.dumps(index, indent=2))

    # Per-brand index for convenience.
    for brand, data in index["brands"].items():
        per_brand_path = output_root / brand / "index.json"
        per_brand_path.parent.mkdir(parents=True, exist_ok=True)
        per_brand_path.write_text(
            json.dumps(
                {
                    "brand": brand,
                    "generatedAt": index["generatedAt"],
                    "cdnBase": index["cdnBase"],
                    "imageCount": data["imageCount"],
                    "linesheets": data["linesheets"],
                },
                indent=2,
            )
        )

    log.info(
        "Done. %d brands, %d images (%d unique, %d duplicates), %.1f MB total. Index: %s",
        len(by_brand),
        len(flat_images),
        len(seen_hashes),
        duplicates,
        total_bytes / 1024 / 1024,
        index_path,
    )
    # Print pivot summary.
    log.info("Gender × category × brand groups (top 20 by count):")
    top = sorted(by_gender_category_brand.items(), key=lambda kv: -len(kv[1]))[:20]
    for key, paths in top:
        log.info("  %5d  %s", len(paths), key)
    if missing:
        log.warning("Missing files: %s", ", ".join(missing))
    return 0


if __name__ == "__main__":
    sys.exit(main())
