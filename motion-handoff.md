# Hero Motion Frame — Handoff & Export Guide

**Project:** `glass.jiocommerce.io` (v0.8.4)  
**Deliverable:** 12-second seamless CSS-only looping hero animation  
**Author:** Manus AI  

## 1. Composition Overview

The hero motion frame has been constructed as a self-contained HTML/CSS composition tailored for HyperFrames or direct video export. It strictly adheres to the approved `index.html` content and the v0.8.4 Open Design brand system.

| Element | Motion Behaviour | CSS Implementation |
|---|---|---|
| **Ambient Blobs** | Slow orbital drift with opacity breathing and scaling. | `transform: scale() translate()`, `opacity` |
| **Grid Overlay** | Static structural lines with slow opacity fade. | `opacity` fade on repeating linear gradient |
| **Headline Accent** | Slow breathing opacity on the "World's First..." span. | `opacity: 0.9` to `1.0` |
| **UI Panels (Right)** | Staggered, continuous orbital drift simulating floating dashboard widgets. | `transform: translate()` with offset delays |
| **Metric Pulses** | Sequenced outline pulses highlighting key row metrics (Orders, Pieces, Platforms). | Staggered `opacity` and `scale` on pseudo-rings |
| **Floating Chips** | Vertical floating drift for abstract UI depth. | `transform: translateY()` |
| **Connector Lines** | Marching dashed lines linking the panels. | SVG `stroke-dashoffset` animation |

## 2. Keyframe Sequence (12s Loop)

The animation uses a 12-second master cycle. All individual `@keyframes` animations are mathematically synced to divide evenly into 12 seconds, ensuring a perfect seamless loop.

*   **0s:** All panels at rest. Headline visible. Blobs at origin. Metric chips at base position. Panel rows fully opaque.
*   **3s:** Panel-1 (JCP) drifts +6px Y, -3px X. Panel-2 (Impetus) drifts -4px Y, +5px X. First pulse ring on "Orders / day" row fires (50% opacity).
*   **6s:** All panels reach mid-orbit. Blob-1 at peak scale (1.12). Metric chips at peak float (+8px Y). Second pulse ring on "Platforms live" fires. Headline accent span at full opacity (1.0).
*   **9s:** Panels begin returning to origin. Blob-2 at peak scale (1.08). Chip-3 (1 K+ AI agents) at peak float. Third pulse ring on "Pieces shipped" fires (80% opacity).
*   **12s:** Identical to 0s. Loop restarts seamlessly.

## 3. Brand Compliance

*   **Colours:** No new hex codes were introduced. The composition strictly uses `var(--ink)`, `var(--bg)`, `var(--accent)`, `var(--accent-soft)`, `var(--green)`, `var(--border)`, and `var(--caption)` exactly as defined in `style.css`.
*   **Typography:** Uses `Inter` for primary UI and `JetBrains Mono` for data metrics and labels, matching the approved site.
*   **Content:** Every word and metric is sourced verbatim from the approved `index.html`. No mock data or fake text was invented.
*   **Accessibility:** The composition includes a `@media (prefers-reduced-motion: reduce)` block that instantly disables all animations, freezing the panels and blobs in their fully visible, opaque rest states.

## 4. Export Notes (MP4 / WebM)

To convert this HTML motion frame into a video file for HyperFrames or social sharing, use headless Chrome (Puppeteer/Playwright) or a tool like Remotion.

### Recommended Remotion / Puppeteer Settings

1.  **Viewport:** `1920x1080` (16:9)
2.  **Frame Rate:** `60 FPS` (essential for smooth CSS transform rendering)
3.  **Duration:** Exactly `12.0 seconds` (720 frames at 60fps)
4.  **Wait for Load:** Ensure web fonts (`Inter`, `JetBrains Mono`) are fully loaded before capturing the first frame.
5.  **Format:**
    *   `WebM (VP9)`: Recommended for web embedding (preserves alpha if background is removed, though this composition uses a solid background).
    *   `MP4 (H.264)`: Recommended for Slack/social sharing. High bitrate (e.g., 10-15 Mbps) is required to prevent banding in the subtle gradient background blobs.

### FFmpeg Encoding (Post-Capture)

If capturing raw frames to PNG, encode the final loop using FFmpeg with high-quality settings to preserve the subtle gradients:

```bash
ffmpeg -framerate 60 -i frame_%04d.png -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p hero_loop.mp4
```
