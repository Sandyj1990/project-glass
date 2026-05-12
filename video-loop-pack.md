# Video Loop Pack — glass.jiocommerce.io v0.8.4

**Author:** Manus AI
**Purpose:** Motion and video loop direction for all 10 sections.
**Constraints:** CSS-driven where possible, seamless loops (5-12s), no JavaScript dependencies, exact brand colours.

---

## General Motion Principles
*   **Seamless:** All loops must return to their exact starting frame to allow infinite playback without stutter.
*   **Subtle:** Motion should support reading, not distract from it. Use slow eases (`ease-in-out`) and avoid sudden flashes.
*   **Brand Aligned:** Use only `var(--accent)`, `var(--bg)`, and `var(--ink)` for motion graphics. No random gradients.
*   **Accessible:** All video/motion must respect `prefers-reduced-motion: reduce`.

## 01. Impact
**Loop Duration:** 12 seconds.
**Concept:** Isometric Data Flow.
**Execution:** A pre-rendered WebM video showing an abstract isometric grid. Data nodes pulse softly along the grid lines. The camera slowly tracks forward over the grid. The loop seamlessly resets by matching the grid pattern geometry.
**Export:** 1920x1080 WebM (VP9) at 60fps.

## 02. Impetus
**Loop Duration:** 8 seconds.
**Concept:** Sketch to Render.
**Execution:** A split-screen wipe effect. A 3D garment wireframe slowly rotates on the Y-axis. A vertical wipe transitions the wireframe into a fully rendered, photorealistic garment (using real PixelBin assets), then wipes back to the wireframe.
**Export:** 1920x1080 WebM (VP9) at 60fps.

## 03. Jio Commerce Platform (JCP)
**Loop Duration:** 10 seconds.
**Concept:** App Cascade Parallax.
**Execution:** CSS-driven motion is preferred here. Real mobile app screens (AJIO, JioMart, etc.) are layered in the DOM. A slow, continuous `transform: translateY()` moves the background apps upward slower than the foreground apps, creating parallax depth.
**Export:** Can be implemented natively via CSS. If video is required, 1920x1080 WebM (VP9) at 60fps.

## 04. UCP & Marketing OS
**Loop Duration:** 6 seconds.
**Concept:** Identity Resolution.
**Execution:** Abstract data particles (small geometric shapes) flow from the edges of the frame toward a central, glowing `var(--accent)` node. The node slowly pulses in size (scale 1.0 to 1.05).
**Export:** 1920x1080 WebM (VP9) at 60fps.

## 05. Granary
**Loop Duration:** 10 seconds.
**Concept:** Forecasting Grid.
**Execution:** A macro view of a data grid UI. The grid slowly scrolls horizontally. Individual data cells briefly flash with a `var(--accent)` background to simulate real-time updates.
**Export:** 1920x1080 WebM (VP9) at 60fps.

## 06. Special Projects
**Loop Duration:** 12 seconds.
**Concept:** Interface Pan.
**Execution:** A slow, smooth camera pan across a multi-screen UI setup, briefly highlighting the interfaces of ALP, RetailVista, and HireFirst. The pan loops back to the start seamlessly.
**Export:** 1920x1080 WebM (VP9) at 60fps.

## 07. AI-Native Platforms
**Loop Duration:** 8 seconds.
**Concept:** Workflow Pulses.
**Execution:** A node-based diagram representing Boltic. Glowing `var(--accent)` pulses travel along the SVG connector lines between the nodes in a continuous, rhythmic flow.
**Export:** Can be implemented natively via CSS/SVG. If video is required, 1920x1080 WebM (VP9) at 60fps.

## 08. Recent Innovations
**Loop Duration:** 5 seconds.
**Concept:** AutRi Scanning.
**Execution:** A smooth, stabilizing tracking shot of the AutRi robot moving down a supermarket aisle. The camera tracks alongside the robot's sensor array. The loop relies on a crossfade or matching aisle geometry to reset.
**Export:** 1920x1080 WebM (VP9) at 60fps.

## 09. Organisation
**Loop Duration:** 15 seconds.
**Concept:** Engineering Scale.
**Execution:** A slow, smooth drone shot moving forward through the open-plan Fynd office. People are seen collaborating at their desks. The motion is extremely slow to avoid distraction.
**Export:** 1920x1080 WebM (VP9) at 60fps.

## 10. Every Platform
**Loop Duration:** N/A.
**Concept:** Interactive Grid.
**Execution:** This section relies on user interaction (filter chips and hover states). No continuous background video loop is recommended here to maintain performance and focus on the UI cards.
**Export:** N/A.
