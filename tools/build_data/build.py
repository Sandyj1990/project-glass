#!/usr/bin/env python3
"""Build · regenerate every `data/ips/<slug>/` folder from spec.py.

Run from repo root:
    python3 tools/build_data/build.py
"""

import json
import sys
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools" / "build_data"))

from spec import IPS  # type: ignore

DATA_DIR = ROOT / "data"
IPS_DIR = DATA_DIR / "ips"

GENERATED_BANNER = "# This file is generated from tools/build_data/spec.py · do not hand-edit\n# Re-run `python3 tools/build_data/build.py` after spec changes\n"


def yaml_dump(data, indent=0):
    """Tiny YAML emitter · keeps dependencies zero. Handles dicts, lists, scalars."""
    pad = "  " * indent
    lines = []
    if isinstance(data, dict):
        if not data:
            return "{}\n"
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                lines.append(f"{pad}{key}:")
                lines.append(yaml_dump(value, indent + 1))
            else:
                lines.append(f"{pad}{key}: {scalar(value)}")
        return "\n".join(lines) + ("\n" if not lines[-1].endswith("\n") else "")
    if isinstance(data, list):
        if not data:
            return f"{pad}[]\n"
        out = []
        for item in data:
            if isinstance(item, dict):
                first = True
                for key, value in item.items():
                    prefix = f"{pad}- " if first else f"{pad}  "
                    if isinstance(value, (dict, list)):
                        out.append(f"{prefix}{key}:")
                        out.append(yaml_dump(value, indent + 2))
                    else:
                        out.append(f"{prefix}{key}: {scalar(value)}")
                    first = False
            else:
                out.append(f"{pad}- {scalar(item)}")
        return "\n".join(out) + "\n"
    return scalar(data) + "\n"


def scalar(value):
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    s = str(value)
    if "\n" in s or ":" in s and not s.startswith("[") and not s.startswith("{"):
        return f'"{s.replace(chr(34), chr(92) + chr(34))}"'
    if s == "" or s.startswith(("- ", "* ", "& ", "@", "%", "`")):
        return f'"{s}"'
    return s


def write_text(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


def build_ip(ip):
    slug = ip["slug"]
    folder = IPS_DIR / slug
    folder.mkdir(parents=True, exist_ok=True)

    # ---- meta.json
    meta = {
        "slug": slug,
        "name": ip["name"],
        "tagline": ip.get("tagline", ""),
        "track": ip.get("track", slug),
        "track_role": ip.get("track_role", "sub-ip"),
        "status": ip.get("status", "Build"),
        "since": ip.get("since"),
        "last_release": ip.get("last_release"),
        "verticals": ip.get("verticals", []),
        "value_chain": ip.get("value_chain", []),
        "ownership": ip.get("ownership", "reliance"),
        "web_anchor": ip.get("web_anchor", f"/{slug}"),
        "external_url": ip.get("external_url"),
        "stake_inr_cr": ip.get("stake_inr_cr"),
        "tags": ip.get("tags", []),
    }
    write_text(folder / "meta.json", json.dumps(meta, indent=2) + "\n")

    # ---- narrative.md
    narrative = [f"# {ip['name']}"]
    if ip.get("tagline"):
        narrative.append(f"\n> {ip['tagline']}\n")
    narrative.append("")
    if ip.get("narrative"):
        narrative.append("## What it does\n")
        narrative.append(ip["narrative"].strip())
        narrative.append("")
    if ip.get("why_this_matters"):
        narrative.append("## Why this matters for Reliance\n")
        narrative.append(ip["why_this_matters"].strip())
        narrative.append("")
    if ip.get("external_validation"):
        narrative.append("## External validation\n")
        for item in ip["external_validation"]:
            narrative.append(f"- {item}")
        narrative.append("")
    if ip.get("case_study"):
        cs = ip["case_study"]
        narrative.append(f"## Case study · {cs.get('name', '')}\n")
        if cs.get("window"):
            narrative.append(f"**Window** · {cs['window']}\n")
        narrative.append("Headline metrics:")
        for k, v in cs.get("headline_metrics", {}).items():
            narrative.append(f"- {k.replace('_', ' ').title()}: {v}")
        if cs.get("transactor_segment_lift"):
            narrative.append("\nTransactor segment lift:")
            for k, v in cs["transactor_segment_lift"].items():
                narrative.append(f"- {k.replace('_', ' ').title()}: {v}")
        if cs.get("category_mix"):
            narrative.append("\nCategory mix:")
            for k, v in cs["category_mix"].items():
                narrative.append(f"- {k.replace('_', ' ').title()}: ₹{v} Cr")
        narrative.append("")
    write_text(folder / "narrative.md", "\n".join(narrative))

    # ---- metrics.yaml
    metrics_data = {"metrics": []}
    for m in ip.get("metrics", []):
        # Each metric is a tuple: (id, label, value, definition, source, confidence)
        id_, label, value, definition, source, confidence = m
        metrics_data["metrics"].append({
            "id": id_,
            "label": label,
            "value": value,
            "definition": definition,
            "source": source,
            "confidence": confidence,
        })
    write_text(folder / "metrics.yaml", GENERATED_BANNER + yaml_dump(metrics_data))

    # ---- team.yaml
    team = ip.get("team", {})
    write_text(folder / "team.yaml", GENERATED_BANNER + yaml_dump(team) if team else GENERATED_BANNER + "# no team data yet\n")

    # ---- releases.yaml
    releases = ip.get("releases", [])
    if releases:
        rel_data = {"releases": []}
        for r in releases:
            # Each release is a tuple: (date, title, summary, next)
            date, title, summary, next_step = r
            entry = {"date": date, "title": title, "summary": summary}
            if next_step:
                entry["next"] = next_step
            rel_data["releases"].append(entry)
        write_text(folder / "releases.yaml", GENERATED_BANNER + yaml_dump(rel_data))
    else:
        write_text(folder / "releases.yaml", GENERATED_BANNER + "releases: []\n")

    # ---- links.yaml
    links = ip.get("links", {})
    if links or ip.get("external_url"):
        clean_links = {}
        for key, value in links.items():
            if isinstance(value, list) and value:
                clean_links[key] = []
                for item in value:
                    if isinstance(item, tuple) and len(item) == 2:
                        clean_links[key].append({"url": item[0], "label": item[1]})
                    else:
                        clean_links[key].append({"url": str(item)})
        if ip.get("external_url") and "production_urls" not in clean_links:
            clean_links["production_urls"] = [{"url": ip["external_url"], "label": ip["name"]}]
        write_text(folder / "links.yaml", GENERATED_BANNER + yaml_dump(clean_links))
    else:
        write_text(folder / "links.yaml", GENERATED_BANNER + "# no external links\n")


def build_index():
    """Master index of every IP for cross-page navigation."""
    index = {
        "generated_at": datetime.now().strftime("%Y-%m-%d"),
        "total_ips": len(IPS),
        "by_status": {},
        "by_track": {},
        "ips": [],
    }
    for ip in IPS:
        status = ip.get("status", "Build")
        index["by_status"][status] = index["by_status"].get(status, 0) + 1
        track = ip.get("track", "uncategorized")
        index["by_track"].setdefault(track, []).append(ip["slug"])
        index["ips"].append({
            "slug": ip["slug"],
            "name": ip["name"],
            "track": track,
            "track_role": ip.get("track_role", "sub-ip"),
            "status": status,
            "web_anchor": ip.get("web_anchor"),
        })
    write_text(DATA_DIR / "index.json", json.dumps(index, indent=2) + "\n")


def main():
    print(f"Building data from spec · {len(IPS)} IPs")
    IPS_DIR.mkdir(parents=True, exist_ok=True)

    for ip in IPS:
        build_ip(ip)
        print(f"  ✓ {ip['slug']}")

    build_index()
    print(f"\n✓ data/index.json regenerated")
    print(f"✓ {len(IPS)} IP folders under data/ips/")


if __name__ == "__main__":
    main()
