# Schema · per-IP folder

Each `data/ips/<slug>/` folder is a structured record of one IP. Six standard files plus optional sub-folders.

## `meta.json` · required

```json
{
  "slug": "ucp",
  "name": "Unified Customer Platform",
  "tagline": "One identity across every Reliance retail business.",
  "track": "jcp",                          // parent track slug
  "track_role": "headline",                // headline | sub-ip | feature
  "status": "Live",                        // Live | Pilot | Build
  "since": "2024-01-11",                   // ISO date · first production live
  "last_release": "2026-04-21",
  "verticals": ["fashion", "grocery", "electronics", "beauty", "pharma"],
  "value_chain": ["sell"],                 // plan | buy-make | move | sell · subset
  "ownership": "reliance",                 // reliance | fynd | shared
  "web_anchor": "/jcp#ucp",                // canonical link on the website
  "external_url": "https://...",           // production URL if customer-facing
  "stake_inr_cr": null,                    // if there's an INR ask attached
  "tags": ["customer-data", "identity", "ml"]
}
```

## `narrative.md` · required

Canonical Markdown narrative. What the IP does. Why it matters. Who built it. What's next.

Sections (in order, all optional except headline):

```markdown
# <IP name>
> <tagline>

## What it does
<1-3 paragraphs · plain English · no AI-slop>

## Why this matters for Reliance
<1-2 paragraphs · the business case>

## Built by
<short paragraph naming the team>

## How it integrates
<list of related IPs / tracks · how data flows>

## What's next
<list of upcoming releases or capability extensions>
```

## `metrics.yaml` · required

Numbers the website cites. Each metric needs definition + source + confidence.

```yaml
metrics:
  - id: identities_unified
    label: Identities unified
    value: "380M+"
    definition: "Customer profile records across RR online + offline"
    source: "UCP production · 29 - Apr - 2026"
    confidence: live          # audited | live | internal | estimate
  - id: rpos_daily_orders
    label: RPOS daily orders streaming
    value: "1.5M"
    definition: "In-store transactions captured by UCP daily"
    source: "UCP analytics"
    confidence: audited
```

## `team.yaml` · required

```yaml
dri:                            # primary owner · always one name
  - name: "Saumil Dalal"
    role: "EM"
product:
  - name: "Prem Nathwani"
  - name: "Amogh Dubey"
engineering:
  - name: "Vaibhav Kulkarni"
    role: "Lead engineer"
qa:
  - name: "Priyanjali Manore"
mentors:
  - name: "Farooq Adam"
  - name: "Advait Pandit"
  - name: "Kushan Shah"
ril_counterpart:
  - team: "Bond team · RIL HR Tech"
    contact: "Naren"
```

## `releases.yaml` · optional but expected for Live IPs

Chronological release history.

```yaml
releases:
  - date: "2026-04-21"
    title: "Campaign Coupon Codes"
    summary: "Shared and personalised coupons in Campaign Manager."
    proof:
      - "CSV/ZIP customer-to-coupon mapping at delivery time"
    next: "JCP Coupons + Central Promotion Engine integration"
  - date: "2026-04-03"
    title: "RPOS Real-Time · 15K+ stores"
    summary: "Every in-store transaction streams into UCP within minutes."
    metrics:
      - "1.5M orders/day · 75+ formats · 15K+ stores"
```

## `links.yaml` · required

External URLs grouped by purpose. **No Slack channel pills on the website**, but they're useful here for audit.

```yaml
production_urls:
  - url: "https://hiring.ril.com"
    label: "RIL HireFirst (Prod sign-off pending)"
sit_urls:
  - url: "https://ril.sit.fyndx1.de"
    label: "SIT environment"
demos:
  - url: "https://youtu.be/9KCFnV6kXEU"
    label: "AI Native UCP demo"
docs:
  - url: "https://docs.google.com/presentation/d/..."
    label: "UCP Release Notes Timeline · Amogh Dubey"
slack_channels:                         # for audit only · NOT rendered on website
  - "#ucp-squad"
```

## `slack-extracts/` · optional

If we have extracted Slack messages relevant to this IP, save them as JSON or Markdown:

```
slack-extracts/
  2026-04-21-coupon-codes.md
  2026-04-03-rpos-realtime.md
  2024-01-11-launch.md
```

Each file is a Markdown extract with a clear preamble:

```markdown
# UCP · Coupon Codes release
Source · Slack #general · 21 - Apr - 2026 · Amogh Dubey
Permalink · https://gofynd.slack.com/...

---

<verbatim message body>
```

## `assets/` · optional

Only put files here that are small (<5 MB) and frequently-referenced. Big files stay on Drive, linked from `links.yaml`.

```
assets/
  decks/      # PDFs we want versioned in repo
  docs/       # markdown copies of canonical docs
  images/     # screenshots, photos
  videos/     # short clips or .url shortcut files
```

## Status definitions (referenced from website /numbers page)

- **Live** · A paying or end customer is using this IP today. Excludes UAT, internal-only, pre-launch.
- **Pilot** · Single store, single channel, single brand, or UAT-only. Validation phase.
- **Build** · In active engineering. No customer is using it yet.

## Slug rules

- lowercase
- hyphens for spaces (`fynd-horizon`, not `fynd_horizon` or `FyndHorizon`)
- match the URL anchor on the website
- stable · never rename without a migration script
