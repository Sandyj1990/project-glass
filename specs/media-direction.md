# media-direction.md
## Project Glass · Open Design Revamp

---

## General Rules
- No stock photography.
- No generic AI gradients or fake 3D glass spheres.
- Use actual product screenshots, UI elements, and architecture diagrams from the `/assets/` directories.
- Maintain high fidelity and clarity.
- Use current interface screenshots/assets when available.
- If product screenshots are unavailable, create abstract UI panels without readable fake text or numbers.

## Hero Section
- **Visual Role:** Establish scale and enterprise credibility.
- **Composition:** A composite of 3 layered UI panels (JCP metrics, Impetus F&L, Platform Status) floating on a warm white background with subtle ambient gradient blobs.
- **Motion Opportunity:** 12-second seamless CSS loop. Panels drift 4-10px in alternating directions.
- **Negative Prompt:** No human faces, no stock imagery, no decorative elements, no fake numbers.

## Section Image Directions
- **§01 Impact:** 3×3 grid of stat tiles — no image needed, data is the visual.
- **§02 Impetus:** Product screenshots from `/assets/impetus/` as card thumbnails.
- **§03 JCP:** Architecture diagram from `/assets/jcp/fynd-for-retail.jpg`.
- **§04 UCP:** Brand Health dashboard screenshot from `/assets/ucp/`.
- **§05 Granary:** Command Centre screenshot from `/assets/granary/`.
- **§06 Special Projects:** ALP / RetailVista / Jarvis screenshots.
- **§07 AI-Native:** Boltic console + PixelBin + Kaily chat interface.
- **§08 Recent Innovations:** Fynd Horizon body-scan + AutRi shelf + Dark Factory.
- **§09 Organisation:** Team photo or abstract org chart.

## Product Visual Direction
- Use existing screenshots from `/assets/` directories.
- Display inside browser-frame or panel containers.
- Dark background (`#1c1a14`) behind light-bg screenshots for contrast.
- **CSS rules:** `object-fit: cover`, `aspect-ratio: 16/9`.

## Export Notes
- **MP4:** H.264, 1920×1080, 30fps, autoplay muted loop playsinline.
- **WebM:** VP9, same dimensions, for Chromium.
- **Poster:** First frame as static fallback image.
- **Responsive Crops:** 16:9 desktop, 4:3 tablet, 9:16 mobile hero.
