# DESIGN.md

## 1. Core Principles
- **Data Density:** High information density. Show the numbers, show the scale.
- **Clarity over Decoration:** Minimal shadows, flat cards, clear borders.
- **Systematic Structure:** Predictable section layouts, consistent typography hierarchy.
- **Frontier Tech Aesthetic:** Use monospace fonts for metadata, status pills, and section labels to evoke an engineering/technical feel.

## 2. Typography
- **Headlines (`.display`, `.display-2`):** Inter Bold (700), tight tracking (-0.04em, -0.03em), tight line-height (1.0 - 1.05).
- **Body (`.prose`):** Inter Regular, line-height 1.55, max-width 70ch for readability.
- **Metadata (`.mono`, `.section-label`, `.pill`, `.cap-num`):** JetBrains Mono, uppercase, tracked out (0.04em - 0.05em).

## 3. Color System
- **Backgrounds:** Pure white (`#FFFFFF`) alternating with soft gray (`#FAFAFA`) per section.
- **Text:** High contrast ink (`#0A0A0A`) for primary, muted (`#6B7280`) for secondary.
- **Accent:** Purple (`#6B5BD6`) used sparingly for CTAs, active states, and key highlights.
- **Status:** Green (`#16A34A`) for LIVE, Amber (`#D97706`) for BUILD/PILOT.

## 4. Components
- **Cards (`.card`):** 12px border-radius, 1px solid border (`#D4D4D4`), white background. Hover state: darker border, very subtle shadow (0 1px 3px rgba(0,0,0,0.05)).
- **Buttons (`.btn-primary`, `.btn-secondary`):** Pill-shaped (999px radius), 15px font size, 500 weight. Primary is filled (`--ink`), Secondary is outlined.
- **Pills (`.pill`):** Small status indicators. Monospace, 11px, 4px border-radius. Color-coded by status.
- **Navigation (`.topnav`):** Sticky, glassmorphism (backdrop-filter blur), clear active states with bottom border indicator. Mega-menu dropdowns for deep navigation.

## 5. Layout & Spacing
- **Container:** Max-width 7xl, centered, 6px horizontal padding.
- **Section Padding:** Generous vertical padding (`py-32`) to separate distinct thematic areas.
- **Grid:** CSS Grid for platform cards (1 column mobile, 2 columns tablet, 3-4 columns desktop). Gap 3 (12px).

## 6. Anti-Patterns
- NO excessive drop shadows.
- NO complex gradients (except subtle hero background if needed).
- NO rounded corners larger than 12px on content cards.
- NO centered text for long paragraphs (keep it left-aligned).
