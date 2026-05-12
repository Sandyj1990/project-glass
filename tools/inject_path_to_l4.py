"""Single source of truth: data/agents-x-platforms.yaml. This sweep:
  - injects the §03 Path to L4 section into each platform page that has at least
    one agent in the registry, between <!-- PATH-TO-L4-START --> markers
  - injects the "Deployed in" block into each agent page, between
    <!-- DEPLOYED-IN-START --> markers
  - --check exits non-zero if either side drifts from the registry, OR if any
    page that should carry the markers is missing them

Mirrors tools/inject_chrome.py and tools/inject_meta_robots.py patterns.

Per docs/path-to-l4-spec.md §6.2.

Usage:
  python tools/inject_path_to_l4.py          # rewrite both sides
  python tools/inject_path_to_l4.py --dry    # report what would change
  python tools/inject_path_to_l4.py --check  # exit non-zero on drift (CI)
  python tools/inject_path_to_l4.py --only impetus jcp   # restrict to specific platforms

Section pattern choice (resolved Round 2 · per-page):
  - .grid-table when 2+ agents on a platform (Impetus has 3)
  - .platform-card grid when 1 agent (JCP, UCP, Granary)
  - retail-vista is the special case · grid-table with rows = tracks (the
    deployment carries a structured 3-track string the renderer parses)
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Lightweight YAML reader — avoids adding pyyaml as a dependency. The registry
# format is intentionally narrow (no anchors, no flow-style); a couple of state
# checks parse it deterministically.
def _strip_inline_comment(s: str) -> str:
    """Strip a YAML-style inline `# comment` from the end of a value. Quoted
    strings are preserved as-is (a `#` inside quotes isn't a comment)."""
    if s.startswith('"') and s.endswith('"'):
        return s
    return re.sub(r"\s+#.*$", "", s).strip()


def parse_registry(path: Path) -> dict:
    text = path.read_text()
    agents: dict[str, dict] = {}
    rungs: dict[str, str] = {}
    section_nums: dict[str, str] = {}
    pattern_overrides: dict[str, str] = {}
    cur_section = None      # "agents" | "platform_current_rungs" | "platform_section_nums" | "platform_pattern_overrides" | None
    cur_agent: str | None = None
    cur_deploy: dict | None = None
    in_deploys = False
    for raw in text.splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        # top-level keys
        m = re.match(r"^(\w+):\s*$", raw)
        if m and not raw.startswith(" "):
            cur_section = m.group(1)
            cur_agent = None
            cur_deploy = None
            in_deploys = False
            continue
        if cur_section == "agents":
            # Agent slug at 2-space indent
            m = re.match(r"^  ([a-z][a-z0-9-]*):\s*$", raw)
            if m:
                cur_agent = m.group(1)
                agents[cur_agent] = {"deployments": []}
                cur_deploy = None
                in_deploys = False
                continue
            # Agent field at 4-space indent · capture rest of line, then strip
            # quotes + inline-comment in helper
            m = re.match(r"^    (\w+):\s*(.*)$", raw)
            if m and cur_agent:
                key = m.group(1)
                val = _strip_inline_comment(m.group(2).strip())
                # Strip surrounding quotes if present
                if val.startswith('"') and val.endswith('"'):
                    val = val[1:-1]
                if key == "deployments":
                    in_deploys = True
                else:
                    agents[cur_agent][key] = val
                continue
            # Deployment list entry — starts with `- platform:`
            m = re.match(r"^      - platform:\s*(.*)$", raw)
            if m and cur_agent and in_deploys:
                plat = _strip_inline_comment(m.group(1).strip())
                cur_deploy = {"platform": plat}
                agents[cur_agent]["deployments"].append(cur_deploy)
                continue
            # Deployment field — `unlocks: "..."` OR `tracks:` (list start)
            m = re.match(r"^        (\w+):\s*(.*)$", raw)
            if m and cur_deploy is not None:
                key = m.group(1)
                rest = m.group(2).strip()
                if key == "tracks" and not rest:
                    cur_deploy["tracks"] = []
                    continue
                val = _strip_inline_comment(rest)
                if val.startswith('"') and val.endswith('"'):
                    val = val[1:-1]
                cur_deploy[key] = val
                continue
            # Track list entry — `- name: "..."`
            m = re.match(r"^          - name:\s*(.*)$", raw)
            if m and cur_deploy is not None and "tracks" in cur_deploy:
                val = _strip_inline_comment(m.group(1).strip())
                if val.startswith('"') and val.endswith('"'):
                    val = val[1:-1]
                cur_deploy["tracks"].append({"name": val})
                continue
            # Track field — `state: Live` or `unlocks: "..."`
            m = re.match(r"^            (\w+):\s*(.*)$", raw)
            if m and cur_deploy is not None and cur_deploy.get("tracks"):
                key = m.group(1)
                val = _strip_inline_comment(m.group(2).strip())
                if val.startswith('"') and val.endswith('"'):
                    val = val[1:-1]
                cur_deploy["tracks"][-1][key] = val
                continue
        elif cur_section == "platform_current_rungs":
            m = re.match(r"^  ([a-z][a-z0-9-]*):\s*(.*)$", raw)
            if m:
                val = _strip_inline_comment(m.group(2).strip())
                if re.match(r"^L[0-5]$", val):
                    rungs[m.group(1)] = val
                continue
        elif cur_section == "platform_section_nums":
            m = re.match(r"^  ([a-z][a-z0-9-]*):\s*(.*)$", raw)
            if m:
                val = _strip_inline_comment(m.group(2).strip())
                if val.startswith('"') and val.endswith('"'):
                    val = val[1:-1]
                section_nums[m.group(1)] = val
                continue
        elif cur_section == "platform_pattern_overrides":
            m = re.match(r"^  ([a-z][a-z0-9-]*):\s*(.*)$", raw)
            if m:
                val = _strip_inline_comment(m.group(2).strip())
                if val.startswith('"') and val.endswith('"'):
                    val = val[1:-1]
                pattern_overrides[m.group(1)] = val
                continue
    return {
        "agents": agents,
        "platform_current_rungs": rungs,
        "platform_section_nums": section_nums,
        "platform_pattern_overrides": pattern_overrides,
    }


# --- rendering ---------------------------------------------------------------

# Map agent state to existing pill class (design.md §2.2 · no new variants).
PILL_CLASS = {
    "Live":     "pill-live",
    "Building": "pill-build",
    "Roadmap":  "pill-phase2",
    "Pilot":    "pill-pilot",
}


def _agents_for_platform(registry: dict, platform: str) -> list[dict]:
    """Reverse-index: list every agent whose deployments include this platform.
    Each entry carries the per-deployment `unlocks` and (optional)
    `next_milestone` strings · plus an optional `link_override:` on the
    agent block (used when an agent has no /agents/<slug>/ detail page
    and should link out to a platform page instead — e.g., ZIP/JIIA on
    /kaily/)."""
    out = []
    for slug, agent in registry["agents"].items():
        for d in agent.get("deployments", []):
            if d.get("platform") == platform:
                out.append({
                    "slug": slug,
                    "name": agent.get("name", slug),
                    "state": agent.get("state", "Building"),
                    "target_rung": agent.get("target_rung", "L4"),
                    "unlocks": d.get("unlocks", ""),
                    "next_milestone": d.get("next_milestone", "—"),
                    "link": agent.get("link_override") or f"/agents/{slug}/",
                })
    return out


def render_platform_section(registry: dict, platform: str, section_num: str | None = None) -> str:
    """Override the default `03` via registry's `platform_section_nums` map.
    Caller can also pass explicit `section_num` (kwarg) to override the
    registry value."""
    if section_num is None:
        section_num = registry.get("platform_section_nums", {}).get(platform, "03")
    """Render the §03 Path to L4 section for a platform. Picks pattern based on
    agent count (per spec §5)."""
    agents = _agents_for_platform(registry, platform)
    if not agents:
        return ""  # platform not in registry — sweep skips it

    rung = registry["platform_current_rungs"].get(platform, "L?")
    n_agents = len(agents)
    # Force grid-table on platforms with track-based deployments (currently
    # just retail-vista) so the rows-per-track rendering kicks in.
    has_tracks = any(
        d.get("tracks")
        for agent in registry["agents"].values()
        for d in agent.get("deployments", [])
        if d.get("platform") == platform
    )
    # Per-platform override · lets a platform force "platform-card" even with
    # 2+ agents (e.g. JCP wants the card grid for visual continuity).
    override = registry.get("platform_pattern_overrides", {}).get(platform)
    if override in ("grid-table", "platform-card"):
        pattern = override
    else:
        pattern = "grid-table" if (n_agents >= 2 or has_tracks) else "platform-card"

    plat_label = platform.upper().replace("-", " ")
    if has_tracks:
        # Track-based deployments (currently retail-vista) — the "agents close
        # the gap" framing is misleading; the page is the agent and the rows
        # are tracks toward L4.
        n_tracks = sum(
            len(d.get("tracks", []))
            for agent in registry["agents"].values()
            for d in agent.get("deployments", [])
            if d.get("platform") == platform
        )
        pcap = (
            f"Currently at <strong>{rung}</strong>. "
            f"{n_tracks} parallel tracks close the gap to L4."
        )
    else:
        verb = "closes" if n_agents == 1 else "close"
        # Drop the "/agents/ directory" framing when any agent on this
        # platform has a link_override (lives outside /agents/, e.g.,
        # ZIP/JIIA on /kaily/). Otherwise the link is misleading.
        any_override = any(a.get("link", "").split("/")[1] != "agents" for a in agents if a.get("link"))
        if any_override:
            pcap = (
                f"Currently at <strong>{rung}</strong>. "
                f"{n_agents} named agent{'s' if n_agents > 1 else ''} {verb} the gap to L4."
            )
        else:
            pcap = (
                f"Currently at <strong>{rung}</strong>. "
                f"{n_agents} named agent{'s' if n_agents > 1 else ''} from the "
                f'<a href="/agents/" style="color: var(--accent); text-decoration: underline;">/agents/</a> '
                f"directory {verb} the gap to L4."
            )
        # Impetus carries an inline 3-week build plan (§04) — link out to it
        # from the §03 paragraph. Other platforms have no such section.
        if platform == "impetus":
            pcap += (
                ' &nbsp;<a href="#path-to-l4-buildplan" '
                'style="color: var(--accent); text-decoration: underline; '
                "font-family: 'JetBrains Mono', monospace; font-size: 13px;\">"
                'See the 3-week build plan ↓</a>'
            )

    if pattern == "grid-table":
        # Special case: a deployment with `tracks:` (currently just retail-vista)
        # renders as rows = tracks rather than rows = agents.
        tracks_deployment = None
        for slug, agent in registry["agents"].items():
            for d in agent.get("deployments", []):
                if d.get("platform") == platform and d.get("tracks"):
                    tracks_deployment = (slug, agent, d)
                    break
        if tracks_deployment:
            slug, agent, dep = tracks_deployment
            rows = []
            for t in dep["tracks"]:
                pill = PILL_CLASS.get(t.get("state", "Building"), "pill-build")
                rows.append(
                    f'      <tr>\n'
                    f'        <td>{t.get("name", "")}</td>\n'
                    f'        <td><span class="pill {pill}">{t.get("state", "Building")}</span></td>\n'
                    f'        <td><span class="cap-num">{agent.get("target_rung", "L4")}</span></td>\n'
                    f'        <td>{t.get("unlocks", "")}</td>\n'
                    f'      </tr>'
                )
            rows_html = "\n".join(rows)
            body = (
                '<div class="overflow-x-auto">\n'
                '  <table class="grid-table">\n'
                '    <thead>\n'
                f'      <tr><th>Track</th><th>State</th><th>Target rung</th><th>What this track unlocks</th></tr>\n'
                '    </thead>\n'
                '    <tbody>\n'
                f'{rows_html}\n'
                '    </tbody>\n'
                '  </table>\n'
                '</div>'
            )
        else:
            rows = []
            for a in agents:
                pill = PILL_CLASS.get(a["state"], "pill-build")
                rows.append(
                    f'      <tr>\n'
                    f'        <td><a href="{a["link"]}" '
                    f'style="color: var(--accent); text-decoration: underline;">{a["name"]}</a></td>\n'
                    f'        <td><span class="pill {pill}">{a["state"]}</span></td>\n'
                    f'        <td><span class="cap-num">{a["target_rung"]}</span></td>\n'
                    f'        <td><span class="cap-num">{a["next_milestone"]}</span></td>\n'
                    f'        <td>{a["unlocks"]}</td>\n'
                    f'      </tr>'
                )
            rows_html = "\n".join(rows)
            body = (
                '<div class="overflow-x-auto">\n'
                '  <table class="grid-table">\n'
                '    <thead>\n'
                '      <tr><th>Agent</th><th>State</th><th>Target rung</th><th>Next milestone</th><th>What it delivers for this platform</th></tr>\n'
                '    </thead>\n'
                '    <tbody>\n'
                f'{rows_html}\n'
                '    </tbody>\n'
                '  </table>\n'
                '</div>'
            )
    else:
        cards = []
        for a in agents:
            pill = PILL_CLASS.get(a["state"], "pill-build")
            cards.append(
                f'  <a href="{a["link"]}" class="platform-card">\n'
                f'    <div class="platform-card-head">\n'
                f'      <div class="platform-card-name">{a["name"]}</div>\n'
                f'      <span class="pill {pill}">{a["state"].upper()}</span>\n'
                f'    </div>\n'
                f'    <div class="platform-card-desc">{a["unlocks"]}</div>\n'
                f'    <div class="platform-card-foot">'
                f'<span class="platform-card-tag">Target {a["target_rung"]}</span>'
                f'</div>\n'
                f'  </a>'
            )
        cards_html = "\n".join(cards)
        body = (
            '<div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-3 max-w-5xl">\n'
            f'{cards_html}\n'
            '</div>'
        )

    return (
        f'<!-- PATH-TO-L4-START · auto-generated by tools/inject_path_to_l4.py · do not edit -->\n'
        f'<section id="path-to-l4" class="py-16 border-b" style="border-color: var(--border);">\n'
        f'<div class="max-w-7xl mx-auto px-6">\n'
        f'<div class="section-label mb-3">{section_num} · PATH TO L4</div>\n'
        f'<h2 class="display-2 text-3xl md:text-4xl mb-4" style="color: var(--ink);">'
        f'How {plat_label} becomes <span style="color: var(--accent);">L4 agentic.</span></h2>\n'
        f'<p class="text-base max-w-3xl mb-8" style="color: var(--ink);">{pcap}</p>\n'
        f'{body}\n'
        f'</div>\n'
        f'</section>\n'
        f'<!-- PATH-TO-L4-END -->'
    )


PLATFORM_DISPLAY = {
    "impetus": "Impetus",
    "jcp": "JCP",
    "ucp": "UCP",
    "granary": "Granary",
    "retail-vista": "Retail Vista",
}


def render_agent_deployed_in(registry: dict, agent_slug: str) -> str:
    """Render the 'Deployed in' block for an agent page · table of platforms +
    per-deployment unlocks string. Self-deployment (agent-as-platform, e.g.
    retail-vista) is filtered out — would just point the page at itself.
    When no non-self deployments remain, the markers are still emitted (with
    no visible body) so the sweep is idempotent."""
    EMPTY = (
        "<!-- DEPLOYED-IN-START · auto-generated by tools/inject_path_to_l4.py · do not edit -->\n"
        "<!-- (no non-self deployments — agent IS its own deployment surface) -->\n"
        "<!-- DEPLOYED-IN-END -->"
    )
    agent = registry["agents"].get(agent_slug)
    if not agent:
        return EMPTY
    deploys = [d for d in agent.get("deployments", []) if d.get("platform") != agent_slug]
    if not deploys:
        return EMPTY
    rows = "\n".join(
        f'      <tr>\n'
        f'        <td><a href="/{d["platform"]}" '
        f'style="color: var(--accent); text-decoration: underline;">'
        f'{PLATFORM_DISPLAY.get(d["platform"], d["platform"].title())}</a></td>\n'
        f'        <td>{d.get("unlocks", "")}</td>\n'
        f'      </tr>'
        for d in deploys
    )
    return (
        f'<!-- DEPLOYED-IN-START · auto-generated by tools/inject_path_to_l4.py · do not edit -->\n'
        f'<section class="py-10 border-t" style="border-color: var(--border);">\n'
        f'<div class="container mx-auto px-6 max-w-6xl">\n'
        f'<div class="text-xs mb-3" style="color: var(--accent); font-family: \'JetBrains Mono\', monospace; text-transform: uppercase; letter-spacing: 0.06em;">Deployed in</div>\n'
        f'<div class="overflow-x-auto">\n'
        f'  <table class="grid-table">\n'
        f'    <thead><tr><th>Platform</th><th>What this agent delivers for that platform</th></tr></thead>\n'
        f'    <tbody>\n'
        f'{rows}\n'
        f'    </tbody>\n'
        f'  </table>\n'
        f'</div>\n'
        f'</div>\n'
        f'</section>\n'
        f'<!-- DEPLOYED-IN-END -->'
    )


# --- patching ----------------------------------------------------------------

PLATFORM_RE = re.compile(
    r"<!-- PATH-TO-L4-START.*?-->.*?<!-- PATH-TO-L4-END -->",
    re.DOTALL,
)
AGENT_RE = re.compile(
    r"<!-- DEPLOYED-IN-START.*?-->.*?<!-- DEPLOYED-IN-END -->",
    re.DOTALL,
)


def patch_file(path: Path, marker_re: re.Pattern, new_block: str, dry: bool) -> str:
    if not path.exists():
        return "missing"
    text = path.read_text()
    if not marker_re.search(text):
        return "no-markers"
    new_text = marker_re.sub(new_block, text, count=1)
    if new_text == text:
        return "unchanged"
    if not dry:
        path.write_text(new_text)
    return "patched"


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--dry", action="store_true", help="report only; no writes")
    p.add_argument("--check", action="store_true", help="report drift and exit non-zero")
    p.add_argument("--only", nargs="*", help="restrict to specific platform/agent slugs")
    args = p.parse_args()
    if args.check:
        args.dry = True

    registry = parse_registry(ROOT / "data" / "agents-x-platforms.yaml")
    only = set(args.only) if args.only else None

    counts = {"patched": 0, "unchanged": 0, "no-markers": 0, "missing": 0}

    # Platform side — derive set from the deployments
    platforms = set()
    for agent in registry["agents"].values():
        for d in agent.get("deployments", []):
            platforms.add(d["platform"])

    print("=== platform side ===")
    for slug in sorted(platforms):
        if only and slug not in only:
            continue
        page = ROOT / slug / "index.html"
        block = render_platform_section(registry, slug)
        result = patch_file(page, PLATFORM_RE, block, args.dry)
        counts[result] = counts.get(result, 0) + 1
        print(f"  {result:11s} {slug}/index.html")

    print("\n=== agent side ===")
    for slug in sorted(registry["agents"].keys()):
        if only and slug not in only:
            continue
        # Agents with link_override don't have a /agents/<slug>/ detail page
        # by design (e.g., ZIP/JIIA documented on /kaily/). Skip them on the
        # agent-side sweep so the gate doesn't report them as "missing".
        if registry["agents"][slug].get("link_override"):
            print(f"  skipped     agents/{slug}/index.html (link_override → {registry['agents'][slug]['link_override']})")
            continue
        page = ROOT / "agents" / slug / "index.html"
        block = render_agent_deployed_in(registry, slug)
        result = patch_file(page, AGENT_RE, block, args.dry)
        counts[result] = counts.get(result, 0) + 1
        print(f"  {result:11s} agents/{slug}/index.html")

    print()
    for k, v in counts.items():
        if v:
            print(f"  {k}: {v}")
    if args.dry:
        print("\n(dry run — no files written)")
    if args.check and (counts.get("patched", 0) > 0 or counts.get("no-markers", 0) > 0 or counts.get("missing", 0) > 0):
        print("\nDRIFT DETECTED · run `python tools/inject_path_to_l4.py` to sync.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
