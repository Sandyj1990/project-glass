"""Scrape Play Store screenshots/icons for non-RBL JCP channels.

Reads tools/scratch/non_rbl_channels.json (a hand-curated list with `slug`,
`name`, `play_search_query` and optional `play_package_id` overrides), then:

  1. Searches play.google.com/store/search and picks the first/preferred package.
  2. Fetches the detail page and extracts the app icon + first N screenshots.
  3. Downloads icon + screenshots into images/jcp-channels/<slug>/.
  4. Writes tools/scratch/non_rbl_play.json with the resolved metadata.

Channels with no obvious app are skipped and logged with reason "no-match".
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.parse import quote_plus

ROOT = Path(__file__).resolve().parent.parent
IMG_DIR = ROOT / "images" / "jcp-channels"
SCRATCH = ROOT / "tools" / "scratch"
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
)


def http_get(url: str, *, retries: int = 2) -> str:
    last = None
    for i in range(retries + 1):
        try:
            req = Request(url, headers={"User-Agent": USER_AGENT, "Accept-Language": "en-US,en"})
            with urlopen(req, timeout=20) as r:
                return r.read().decode("utf-8", errors="replace")
        except Exception as e:  # noqa: BLE001
            last = e
            time.sleep(1.5 * (i + 1))
    raise RuntimeError(f"GET failed: {url} ({last})")


def http_download(url: str, out_path: Path) -> None:
    req = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(req, timeout=30) as r, open(out_path, "wb") as f:
        f.write(r.read())


def search_apps(query: str) -> list[str]:
    url = f"https://play.google.com/store/search?q={quote_plus(query)}&c=apps&hl=en"
    html = http_get(url)
    pkgs = re.findall(r'href="/store/apps/details\?id=([A-Za-z0-9_.]+)"', html)
    # Stable order, deduped
    seen, out = set(), []
    for p in pkgs:
        if p not in seen:
            seen.add(p)
            out.append(p)
    return out


def fetch_detail(package: str) -> dict | None:
    url = f"https://play.google.com/store/apps/details?id={package}&hl=en"
    try:
        html = http_get(url)
    except Exception as e:  # noqa: BLE001
        return {"error": str(e), "url": url}
    # Title sits in <title>App Name - Apps on Google Play</title>
    title = ""
    m = re.search(r"<title>([^<]+?)\s*-\s*Apps on Google Play</title>", html)
    if m:
        title = m.group(1).strip()
    # Icon: og:image meta is the most reliable source.
    icon = None
    m_og = re.search(r'<meta[^>]+property="og:image"[^>]+content="([^"]+)"', html)
    if m_og:
        icon = m_og.group(1).split("=")[0]  # strip variant suffix
    # Screenshots: only take URLs that carry a landscape/portrait variant suffix
    # — these are the actual phone shots Google emits in the gallery rail.
    # Common variants: =w526-h296-rw (landscape) or =w296-h526-rw (portrait).
    sized = re.findall(
        r"https://play-lh\.googleusercontent\.com/([A-Za-z0-9_-]+)=w(\d+)-h(\d+)-rw",
        html,
    )
    seen, screens = set(), []
    portrait, landscape = [], []
    for token, w, h in sized:
        w, h = int(w), int(h)
        # Skip near-square (badges, icons) and tiny logos.
        if min(w, h) < 200:
            continue
        ratio = max(w, h) / min(w, h)
        if ratio < 1.4:
            continue  # too square — likely a promo card or badge
        shot_url = f"https://play-lh.googleusercontent.com/{token}"
        if icon and shot_url == icon:
            continue
        if shot_url in seen:
            continue
        seen.add(shot_url)
        # Portrait (h > w) is an actual phone-UI screenshot. Landscape is
        # almost always a marketing/feature graphic — keep them as fallback only.
        (portrait if h > w else landscape).append(shot_url)
    # Prefer portrait phone shots; fall back to landscape if the app has none.
    screens = portrait + landscape
    return {
        "package": package,
        "url": url,
        "title": title,
        "icon": icon,
        "screenshots": screens,
        "shotCounts": {"portrait": len(portrait), "landscape": len(landscape)},
    }


def pick_package(channel: dict, candidates: list[str]) -> str | None:
    if channel.get("play_package_id"):
        return channel["play_package_id"]
    if not candidates:
        return None
    # Prefer obvious Reliance / channel matches.
    name_low = channel["name"].lower().replace(" ", "")
    prefer = channel.get("preferred_package_substrings", [])
    for sub in prefer:
        for p in candidates:
            if sub in p.lower():
                return p
    # Heuristic: look for the channel name as a substring of package id.
    for p in candidates:
        if name_low and name_low[:6] in p.lower().replace(".", "").replace("_", ""):
            return p
    # Fall back to first.
    return candidates[0]


def process_channel(ch: dict, force: bool = False) -> dict:
    slug = ch["slug"]
    out_dir = IMG_DIR / slug
    out_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = out_dir / "manifest.json"
    if manifest_path.exists() and not force:
        return json.loads(manifest_path.read_text())

    if ch.get("skip"):
        manifest = {**ch, "status": "skipped", "reason": ch.get("skip_reason", "no-app")}
        manifest_path.write_text(json.dumps(manifest, indent=2))
        return manifest

    candidates = search_apps(ch.get("play_search_query") or ch["name"])
    package = pick_package(ch, candidates)
    if not package:
        manifest = {**ch, "status": "no-match", "candidates": candidates[:5]}
        manifest_path.write_text(json.dumps(manifest, indent=2))
        return manifest

    detail = fetch_detail(package)
    if not detail or detail.get("error"):
        manifest = {**ch, "status": "fetch-error", "package": package, "detail": detail}
        manifest_path.write_text(json.dumps(manifest, indent=2))
        return manifest

    # Download icon + up to 4 screenshots at 720w.
    saved = []
    if detail["icon"]:
        try:
            http_download(detail["icon"] + "=s256", out_dir / "icon.png")
            saved.append("icon.png")
        except Exception as e:  # noqa: BLE001
            saved.append(f"icon-error:{e}")
    for i, u in enumerate(detail["screenshots"][:8], start=1):
        try:
            http_download(u + "=w720", out_dir / f"shot-{i}.png")
            saved.append(f"shot-{i}.png")
        except Exception as e:  # noqa: BLE001
            saved.append(f"shot-{i}-error:{e}")

    manifest = {
        **ch,
        "status": "ok",
        "play_package_id": package,
        "play_url": detail["url"],
        "play_title": detail["title"],
        "saved_files": saved,
        # Channel-curated index of which shot-N.png to feature in the gallery.
        # Defaults to 1 if the input doesn't override it.
        "primary_shot": ch.get("primary_shot", 1),
    }
    manifest_path.write_text(json.dumps(manifest, indent=2))
    return manifest


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--input", default=str(SCRATCH / "non_rbl_channels.json"))
    p.add_argument("--output", default=str(SCRATCH / "non_rbl_play.json"))
    p.add_argument("--force", action="store_true", help="ignore per-channel manifest cache")
    p.add_argument("--only", default="", help="comma-separated slugs to limit to")
    args = p.parse_args()

    channels = json.loads(Path(args.input).read_text())
    if args.only:
        wanted = set(s.strip() for s in args.only.split(","))
        channels = [c for c in channels if c["slug"] in wanted]
    results = []
    for ch in channels:
        print(f"  · {ch['slug']:24s} ", end="", flush=True)
        try:
            r = process_channel(ch, force=args.force)
            print(r.get("status", "?"))
        except Exception as e:  # noqa: BLE001
            r = {**ch, "status": "exception", "error": str(e)}
            print(f"EXC {e}")
        results.append(r)

    Path(args.output).write_text(json.dumps(results, indent=2))
    by_status: dict[str, int] = {}
    for r in results:
        by_status[r.get("status", "?")] = by_status.get(r.get("status", "?"), 0) + 1
    print(f"\nWrote {args.output}")
    print(f"Counts: {by_status}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
