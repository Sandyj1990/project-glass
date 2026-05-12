# Visual Audit Checklist

The visual audit confirms the page actually loads, renders, and behaves the way the HTML says it should. Execution lives in Chrome DevTools MCP.

## Setup

1. Confirm the local dev server is reachable:
```bash
curl -s -o /dev/null -w "HTTP %{http_code}\n" http://localhost:8765/<route>/
```
If 0 or non-200, the audit cannot run the visual phase. Skip with a note in the report.

2. Open the page in Chrome DevTools MCP:
```
mcp__chrome-devtools__new_page url=http://localhost:8765/<route>
```

3. Bypass the auth gate (every page imports `/auth.js`):
```
mcp__chrome-devtools__evaluate_script function="() => { sessionStorage.setItem('fyndrrl_auth_v1','1'); location.reload(); return 'auth set'; }"
```

## Phase A — Network audit

```
mcp__chrome-devtools__list_network_requests resourceTypes=["image","document","stylesheet","script"]
```

Score each request:

| HTTP code | Verdict |
|---|---|
| 200 / 304 | OK |
| 404 | CRITICAL — broken asset visible to users |
| 403 / 401 | HIGH — usually a CDN auth issue |
| 5xx | HIGH — server-side problem |

Group by image vs PDF vs script. Every `<img src>` must have a 200/304. Every `<embed>` / `<iframe>` `src` must have a 200/304. CSS and Tailwind CDN loads should also be 200/304.

## Phase B — Console audit

```
mcp__chrome-devtools__list_console_messages types=["error","warn"]
```

Acceptable noise:
- `cdn.tailwindcss.com should not be used in production` — appears on every page, not actionable.

Anything else is a finding:
- Errors → HIGH
- Warnings other than the Tailwind dev message → MEDIUM
- Repeated warnings (same source firing 5+ times) → HIGH (often signals a render-loop or hydration issue)

## Phase C — Rendering audit

Take a hero screenshot (default desktop) and a mobile screenshot:

```
mcp__chrome-devtools__resize_page width=1280 height=900
mcp__chrome-devtools__take_screenshot filePath=tools/scratch/<page>-hero.jpg format=jpeg quality=75

mcp__chrome-devtools__resize_page width=375 height=812
mcp__chrome-devtools__evaluate_script function="() => { window.scrollTo({top: 0, behavior: 'instant'}); return 0; }"
mcp__chrome-devtools__take_screenshot filePath=tools/scratch/<page>-mobile-hero.jpg format=jpeg quality=75
```

Visual scan each:

| Check | Severity if failing |
|---|---|
| Hero H1 + status pills + first stat tile visible above the fold (1280×900) | HIGH |
| All status pills (Live/Building/Roadmap) render with correct colour | HIGH |
| Stat tiles align in a clean grid (no overflow, no truncated numbers) | MEDIUM |
| Mobile hero: H1 readable, pills wrap (don't overflow), stats stack to single column | HIGH |
| No text overlapping with pills, badges, or other text | HIGH |
| Images load with reasonable aspect ratio (no severe stretching) | MEDIUM |
| Tables fit the viewport (don't horizontally scroll on desktop) | MEDIUM |
| Embedded PDF / iframe loads (not a blank box) | HIGH |

## Phase D — Section navigation audit

For pages with subnav (Overview / Research / etc.), click each subnav link and confirm it navigates correctly. Failed click is HIGH.

For pages with anchor links (`#granary-cortex`, etc.), verify each anchor target exists in the DOM.

## Phase E — Section-label contiguity (visual)

Scroll to each numbered section. Take a screenshot at the section header. Confirm the visible label number matches the spec position:

```
grep -n 'section-label mb-3">[0-9]' <page>/index.html
```

Numbers must be a contiguous run. A skip (e.g., 01, 02, 04) is MEDIUM.

## Phase F — Cross-browser-ish smoke

Optional. The site uses no browser-specific APIs of note, but if the page heavily uses CSS grid / flexbox edge cases or PDF embedding (Chrome's PDF viewer specifically), note that Safari renders PDF embeds differently. Flag MEDIUM only if the page is critical-path for sharing.

## Per-finding output

Each visual finding records:

```
{
  "severity": "...",
  "section": "§NN" or "page chrome" or "mobile",
  "issue": "What's wrong (e.g., 'PDF embed shows blank box on mobile')",
  "fix": "What to do (e.g., 'replace <embed> with thumbnail + open-in-new-tab on viewports < 768px')",
  "screenshot": "tools/scratch/<page>-<issue>.jpg"
}
```

## Scoring

```
Visual Completeness score:

100 — All assets 200, console clean (Tailwind dev only), hero + mobile render clean, all
      embeds work, no overflow.
 95 — One LOW finding (e.g., minor spacing inconsistency).
 90 — One MEDIUM finding (e.g., embed renders differently on mobile but desktop is OK).
 80 — Two MEDIUM findings, OR one HIGH that's narrow in scope (e.g., one image broken
      but page still readable).
 70 — One CRITICAL or multiple HIGH findings.
<70 — Page has visible breakage that Apex would notice immediately.
```

A 404 on a hero stat image, a banned-construction word visible in the hero, or a console flooded with errors caps Visual at 70.
