# motion-system.md
## Project Glass · Open Design Revamp

---

## 1. Scroll Reveal System
All major section elements (paragraphs, cards, tiles) must use the `data-reveal` attribute for scroll-triggered entrance animations.

- **Initial State:** `opacity: 0`, `transform: translateY(16px)`
- **Revealed State:** `opacity: 1`, `transform: none`
- **Transition:** `opacity 0.5s ease, transform 0.5s ease`
- **Stagger:** When multiple items in a grid enter the viewport simultaneously, they should be staggered by `80ms` based on their index.

## 2. Hover Interactions
Hover states should be subtle, focusing on borders, backgrounds, and minor translations rather than heavy shadows or scaling.

- **Cards/Tiles:** `border-color: var(--ink)`, `transform: translateY(-2px)`
- **Transition Timing:** `0.15s` to `0.2s` depending on element size.
- **Buttons (Primary):** `opacity: 0.85`, `transform: translateY(-1px)`
- **Buttons (Secondary):** `border-color: var(--ink)`, `transform: translateY(-1px)`
- **Nav Links:** `background: var(--bg-soft)`, `color: var(--accent)`

## 3. Hero Ambient Animation
The hero background should feature slow, ambient, looping animations to provide a sense of life without distracting from the content.

- **Blob 1:** 12s ease-in-out infinite loop. Drifts 20px right, 10px up, scales to 1.02x, then drifts left/down. Opacity pulses between 0.3 and 0.6.
- **Blob 2:** 12s ease-in-out infinite loop. Drifts 15px right, 8px up, scales to 1.03x. Opacity pulses between 0.5 and 0.7.

## 4. Hero UI Panel Drift
The floating UI panels in the hero section should drift slowly to simulate depth and motion.

- **Panel 1 & 3 (Drift A):** 8s and 11s ease-in-out infinite loops. Drifts up 8px, right 4px.
- **Panel 2 (Drift B):** 14s ease-in-out infinite loop. Drifts down 6px, left 5px.

## 5. Reduced Motion Support
All animations and transitions MUST be disabled for users who prefer reduced motion.

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
  [data-reveal] { opacity: 1; transform: none; }
}
```
