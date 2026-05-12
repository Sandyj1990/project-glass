# qa-checklist.md
## Project Glass · Open Design Revamp

---

## 1. Content Parity Check
- [ ] Every heading, paragraph, CTA label, statistic, product name, and microcopy from the original site is present.
- [ ] No text has been paraphrased, shortened, or "improved".
- [ ] No new claims, metrics, or features have been added.
- [ ] No placeholder text (Lorem Ipsum) exists.

## 2. Colour Parity Check
- [ ] Only existing brand colours from `style.css` (`--ink`, `--accent`, `--bg`, etc.) are used.
- [ ] No new hex codes or accent colours have been introduced.
- [ ] Gradients use only existing colour tokens.

## 3. Responsive Check
- [ ] Layout reflows gracefully across desktop, tablet, and mobile breakpoints.
- [ ] Mobile navigation is accessible and functional.
- [ ] Typography scales appropriately using clamp or media queries.

## 4. Accessibility Check
- [ ] Semantic HTML tags (`nav`, `section`, `main`, `footer`) are used correctly.
- [ ] All interactive elements are keyboard accessible (`tabindex`, focus states).
- [ ] ARIA attributes are used where necessary (e.g., `aria-expanded` on mobile menu).
- [ ] Contrast ratios meet WCAG AA standards.

## 5. Performance Check
- [ ] All CSS is inline in a `<style>` tag within `index.html`.
- [ ] Minimal or no external JS dependencies (using vanilla JS for interactions).
- [ ] Animations use GPU-accelerated properties (`transform`, `opacity`).

## 6. Motion Check
- [ ] Hero ambient animation and panel drift are smooth and seamless.
- [ ] Scroll reveal animations (`data-reveal`) stagger correctly.
- [ ] Hover states are subtle and performant.
- [ ] `prefers-reduced-motion` is respected (all animations disabled).

## 7. SEO & Structure Check
- [ ] Meta tags (title, description) are preserved.
- [ ] H1, H2, H3 hierarchy is logical and sequential.
- [ ] `data-od-id` attributes are present on major sections.

## 8. Brand Consistency & Enterprise Credibility
- [ ] The overall feel is premium, polished, and production-ready.
- [ ] Spacing follows Apple-level discipline and Stripe-level clarity.
- [ ] No "startup template" look or cheap parallax effects.
- [ ] Product-led visuals are prioritized over generic decorative art.
