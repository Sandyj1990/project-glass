# /culture rebuild · spec

**Status:** Draft, awaiting approval before content build.
**Author:** Kushan Shah
**Date opened:** 2026-05-02
**Source:**
- `docs/org-notes-compilation/Fynd - Unlocking Growth.pdf` — slides 17–23 (gitignored).
- `organisation/data.json` — for keka CDN photo URLs, joined by Employee Number.

**Decided up front (2026-05-02):**
1. Existing `/culture` page (operating principles, AI-native, day-in-the-life, anti-patterns) is **replaced entirely**. Nothing carried over.
2. People photos **reused from keka** at `https://socialassets.impetusz0.de/rrl-portfolio/assets/keka-photos/<id>.<ext>`. Initials fallback for misses.
3. Glassdoor + ProductHunt sections **stylised to match the site** (existing `card`, `pill`, mono patterns). Not faithful Glassdoor/ProductHunt clones.

---

## 1 · Page shape

Single long page, no tabs. Sections in this order, all left-aligned, MDA bar:

| # | Section | Source | Notes |
|---|---|---|---|
| Hero | "Culture." + one-line lead | — | One sentence. No stats, no KPIs. |
| 01 | **Core Values** | Slide 17 | 10-tile grid (5 × 2 desktop, 2 col mobile). Title only on each tile. Subtitle from slide 17 lead. |
| 02 | **10+ years building Fynd** | Slide 22 | 10 person cards, each with photo (keka), name, current title, "Started as … in 2015", quote. |
| 03 | **Our Leaders** | Slide 23 | 7 person cards: 2 founders top, 5 leaders below. Photo + name + role + scope. |
| 04 | **Life at Fynd** | Slide 18 | 3 program cards (State of the Firm, Fynd Stars, Annual Awards) + a 2×3 photo collage (Hactimus, Navratri, State of the Firm, Holi, Women's Day, Fynd Stars Winners). |
| 05 | **What our people say** | Slide 19 | 9 Glassdoor reviews. Hero-quote layout for the lead 5★ review, smaller 8 cards below. Glassdoor source pill in section header. |
| 06 | **Awards & Recognition** | Slide 20 | 6 award cards (NRF / HBS / Gartner / GPTW / Fast Company / RTIH 2026) + 2 small photo strips (Women Leader in Business, India DevOps Show). |
| 07 | **ProductHunt Awards** | Slide 21 | 6 product cards: Kaily, CoPilot Live, Fynix, Bharat Diffusion, PixelBin, Erase.bg. Each shows the launch awards as small mono pills with dates. |

---

## 2 · Person → keka mapping (sections 02 & 03)

Looked up by name against `organisation/data.json` rows. 14 of 17 mapped; the remainder fall back to initials.

| Section | Person | xlsx ID | Has photo |
|---|---|---|---|
| 10+ yrs | Kavish Vora | 1033 | yes |
| 10+ yrs | Kinjal Patel | 1014 | yes |
| 10+ yrs | Kingshuk Bhattacharya | 1013 | yes |
| 10+ yrs | Kapil Kapri | 1026 | yes |
| 10+ yrs | Jigar Dafda | 1022 | yes |
| 10+ yrs | Muralidhar Edam | 1027 | yes |
| 10+ yrs | Kushan Shah | 1010 | yes |
| 10+ yrs | Mayur Suresh Thanekar | 1024 | yes |
| 10+ yrs | Ronak Modi | 1028 | yes |
| 10+ yrs | Debajit Sardar | 1011 | yes |
| Leaders | Farooq Adam | 1001 | yes |
| Leaders | Sreeraman MG (SMG in xlsx) | 1003 | yes |
| Leaders | Jigar Dafda | 1022 | yes |
| Leaders | Kushan Shah | 1010 | yes |
| Leaders | Ragini Varma | 2233 | **no** → initials |
| Leaders | Ronak Modi | 1028 | yes |
| Leaders | Salman Saudagar | 1694 | yes |

This mapping lives **in the page HTML directly** (not in mappings.json) — small, static, deck-derived, doesn't need a config layer.

---

## 3 · Section data

### Section 01 · Core Values (slide 17)

Lead: *"Over a decade of building Fynd, we've learned that culture isn't what you say — it's what you do when no one's watching."*

10 values:

1. Consumer is the Boss
2. Do More with Less
3. No Politics, No Bullshit
4. Be Humble
5. Treat Others as You Would Like to Be Treated
6. Do It Once, Do It Right
7. Treat Work as Sports *(continuous self-improvement)*
8. Be Ethical and Accountable
9. Brutal Honesty
10. Disagree but Commit

### Section 02 · 10+ years (slide 22)

| Name | Current role | Started as | Quote |
|---|---|---|---|
| Kavish Vora | Staff Engineering Manager-1 | SDE-1 in 2015 | "Fynd helps me push my limits of what I can do" |
| Kinjal Patel | Software Development Engineer-3 | SDE-1 in 2015 | "Fynd made me the person I am today" |
| Kingshuk Bhattacharya | Engineering Manager-2 | SDE-1 in 2015 | "At Fynd I am always around so many knowledgeable people" |
| Kapil Kapri | Staff Engineering Manager-1 | SDE-1 in 2015 | "At Fynd I get to work on new age technologies" |
| Jigar Dafda | Chief Technology & Product Officer | Web Team lead in 2015 | "When I joined Fynd, I knew I was building something extraordinary" |
| Muralidhar Edam | Engineering Manager-2 | (not in slide, inferred 2015) | "Fynd gives me new challenges everyday." |
| Kushan Shah | Chief Technology & Product Officer | (not in slide, inferred 2015) | "At Fynd I can solve problems across various domains" |
| Mayur Thanekar | Technical Integration Manager-3 | Reliability Manager in 2015 | "At Fynd I can contribute to solving real world problems" |
| Ronak Modi | Chief Business Officer - Global | Associate PM in 2015 | "I am relearning and learning something new everyday" |
| Debajit Sardar | Design Lead | Junior UI Designer in 2015 | "Where Fynd can go excites me" |

### Section 03 · Our Leaders (slide 23)

| Name | Role | Scope |
|---|---|---|
| Farooq Adam | Founder | — |
| Sreeraman MG | Founder | — |
| Jigar Dafda | CTPO | Commerce, AI/ML, Emerging Platforms |
| Kushan Shah | CTPO | Supply Chain, Engineering Productivity |
| Ragini Varma | CBO India | India Business Growth |
| Ronak Modi | CBO Global | Global Business Growth |
| Salman Saudagar | COO | Jio Platforms |

### Section 04 · Life at Fynd (slide 18)

3 programs:
- **State of the Firm** — quarterly all-hands to learn and discuss progress.
- **Fynd Stars** — top performer awards across the org, three times a year.
- **Fynd Annual Awards** — top performer awards across the org, once a year.

6 photos in the deck (Hactimus Hackathon, Navratri Celebrations, State of the Firm, Holi Celebrations, Women's Day, Fynd Stars Winners). **Open question Q1** below — see § 5.

### Section 05 · Glassdoor (slide 19)

Hero review (5★, 19 Jun 2025): *"A rocketship for builders who thrive on ownership and velocity"* — Associate director, sales · Mumbai · Current employee, less than 1 year. ✓ Recommend ✓ CEO approval ✓ Business outlook.

8 supporting reviews (date, stars, summary, role, tenure, location):

| Date | Stars | Summary | Role | Tenure |
|---|---|---|---|---|
| 10 Jul 2025 | 5 | Perfect place to grow if you're very proactive and adaptable | Anonymous | Current |
| 19 Jun 2025 | 4 | Innovative culture, great exposure, but could use more structure | Anonymous | Current, > 3 yrs |
| 10 Jul 2025 | 5 | More than just a company | Business program manager | Former, > 1 yr · Mumbai |
| 26 May 2025 | 5 | A Supportive, Growth-Oriented Workplace That Truly Cares | Senior program manager | Current, > 5 yrs · Mumbai |
| 28 May 2025 | 5 | AI First Opportunities | Engineering manager | Current, > 1 yr · Mumbai |
| 14 Dec 2025 | 4 | I love the work there related to the AI | AI intern | Current, < 1 yr |
| 14 Dec 2025 | 5 | Love the project I was at | AI intern | Former, < 1 yr |
| 9 Nov 2025 | 5 | Great place to learn, grow and take ownership | Anonymous | Current, < 1 yr · Mumbai |

### Section 06 · Awards & Recognition (slide 20)

| Award | Year | Source |
|---|---|---|
| 2025 NRF APAC Innovators | 2025 | NRF / Forrester |
| HBS Case Study | — | Harvard Business School |
| Digital Commerce Tech Vendor 2024 | 2024 | Gartner |
| Great Place to Work | — | GPTW |
| World's Most Innovative Company - APAC 2022 | 2022 | Fast Company |
| AI in Retail Awards 2025 | 2025 / RTIH 2026 Finalist | RTIH |

Also two photo references (Women Leader in Business — Ragini Verma; The India DevOps Show Award).

### Section 07 · ProductHunt Awards (slide 21)

| Product | Awards |
|---|---|
| Kaily | Launch of the Day, 12 Dec 2025 |
| CoPilot Live | Launch of the Day, 12 Jun 2025 · Launch of the Week, 2 Nov 2023 · Launch of the Day, 2 Nov 2023 |
| Fynix | Launch of the Week, 6 Mar 2025 · Launch of the Day, 6 Mar 2025 |
| Bharat Diffusion | Launch of the Day, 18 Nov 2024 |
| PixelBin | Launch of the Day, 23 Mar 2023 · Launch of the Day, 1 Dec 2022 |
| Erase.bg | Launch of the Month, 21 Oct 2021 · Launch of the Week · Launch of the Day |

---

## 4 · Build approach

- **No build script.** Page is hand-written HTML — content is small, deck-derived, and doesn't change per data refresh.
- Person photos resolve at render time via `https://socialassets.impetusz0.de/rrl-portfolio/assets/keka-photos/<id>.<ext>` with `onerror` swap to initials avatar (same pattern as `/organisation`).
- No new CDN uploads (sub-feature of decision #2 above).

---

## 5 · Resolved decisions (2026-05-02)

1. **Life at Fynd photos** → 6 photos extracted from slide 18, uploaded to `gs://impetus-socialpilot/rrl-portfolio/assets/culture-deck/life-*.png`. Photo collage renders.
2. **Awards & Recognition logos** → user asked for logo extraction, but per-logo cropping from the PDF render proved unreliable (rounded card edges, thin logos, multi-line layouts). **Pragmatic deviation:** ship text-only award cards (title + source name in mono). Two larger photos from the right side of slide 20 (Women Leader in Business, India DevOps Show) DID extract cleanly and are uploaded to `assets/culture-deck/award-photo-*.png`. Logos can be added in a follow-up — either by hand-curating the SVG/PNG from each org's brand assets, or by re-cropping with tighter coordinates.
3. **ProductHunt links** → no links. Pure text + mono date pills.
4. **Section order** → kept my reorder: Core Values → 10+ yrs → Leaders → Life → Glassdoor → Awards → ProductHunt.

> Resolved with user 2026-05-02.

---

## 6 · Acceptance checklist

- [ ] `/culture` loads, replaces all existing content
- [ ] Core Values renders as 10-tile grid (5 × 2 desktop)
- [ ] All 10 tenure people render with keka photos (initials fallback works for misses)
- [ ] All 7 leaders render with keka photos (Ragini Varma falls back to initials)
- [ ] Glassdoor hero quote prominent; 8 supporting reviews readable
- [ ] No em-dashes, no "leverage", DD - MMM - YYYY dates throughout
- [ ] Mobile: tile grids stack to 2 cols, person cards stack to 1 col
