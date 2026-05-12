# Asset Production Checklist — glass.jiocommerce.io v0.8.4

**Author:** Manus AI
**Purpose:** Master QA checklist for all image and video assets before deployment.

---

## 1. Brand & Colour Compliance
- [ ] **Strict Colour Palette:** Do all assets exclusively use the approved hex codes (`var(--accent)`, `var(--ink)`, `var(--bg)`, `var(--bg-soft)`, `var(--green)`)?
- [ ] **No Random Gradients:** Are all gradients purposeful and restricted to brand colours?
- [ ] **Typography Match:** Does any text within the assets use `Inter` or `JetBrains Mono`?
- [ ] **No Generic AI:** Have all generic AI artifacts (extra fingers, nonsensical text, cliché glowing brains/holograms) been removed or painted out?

## 2. Content & Factual Accuracy
- [ ] **No New Claims:** Do the assets avoid introducing any metrics or claims not present in the approved `index.html`?
- [ ] **Real UI:** Are all dashboard, app, and interface representations based on actual Reliance Retail / Fynd products (e.g., AJIO, JioMart, Cortex, Boltic)?
- [ ] **No Fake Data:** Is all visible data within UI representations either accurate or abstracted to illegibility? (No fake names, no invented charts).

## 3. Technical Specifications (Images)
- [ ] **Format:** Are all static images exported as WebP for optimal web performance?
- [ ] **Resolution:** Are hero/full-width images at least 2560px wide (2x retina)? Are standard section images at least 1600px wide?
- [ ] **Compression:** Are WebP files compressed to balance quality and file size (target < 200KB for section images, < 400KB for hero)?
- [ ] **Aspect Ratios:** Are multiple aspect ratios (16:9, 4:3, 1:1) provided or crop-safe for responsive design?
- [ ] **Alt-Text:** Is descriptive, SEO-friendly alt-text provided for every image?

## 4. Technical Specifications (Video/Motion)
- [ ] **Format:** Are all video loops exported as WebM (VP9) for web? (Provide MP4 H.264 fallbacks if required by specific browsers/devices).
- [ ] **Seamless Loop:** Does the final frame of the video match the first frame perfectly to ensure a stutter-free loop?
- [ ] **Framerate:** Are UI and abstract motion graphics exported at 60fps for smooth playback? (Live-action video can be 24fps/30fps).
- [ ] **File Size:** Are background video loops aggressively compressed? (Target < 2MB per loop).
- [ ] **No Audio:** Are all audio tracks completely stripped from the video files?
- [ ] **Accessibility:** Does the implementation respect `@media (prefers-reduced-motion: reduce)` by falling back to a static poster frame?

## 5. Section-Specific Sign-off
- [ ] **01. Impact:** Asset accurately conveys scale without cliché stock imagery.
- [ ] **02. Impetus:** Asset clearly shows the design-to-shelf transformation.
- [ ] **03. JCP:** Asset features real Reliance Retail mobile app interfaces.
- [ ] **04. UCP:** Asset visualizes data unification cleanly and abstractly.
- [ ] **05. Granary:** Asset focuses on the forecasting data grid UI.
- [ ] **06. Special Projects:** Asset cleanly represents the 6 diverse projects.
- [ ] **07. AI-Native:** Asset accurately reflects a Boltic/node-based workflow.
- [ ] **08. Recent Innovations:** Asset uses high-quality photography of AutRi or Dark Factory hardware.
- [ ] **09. Organisation:** Asset is a high-quality, authentic photo of the engineering team.
- [ ] **10. Every Platform:** Background pattern (if used) is extremely subtle and non-distracting.
