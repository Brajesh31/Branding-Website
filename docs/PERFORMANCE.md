# ⚡ Performance and Asset Optimization

## 1. Current profile
Fabulo is a static HTML page with local editorial images and a browser-side Tailwind script reference. No measured performance baseline is recorded here. Do not infer performance scores from the technology stack alone.

## 2. Image strategy
- Inspect actual rendered dimensions before resizing.
- Use appropriate compression and modern formats where supported.
- Preserve sufficient quality for editorial imagery.
- Add explicit width and height to reduce layout shifts.
- Lazy-load below-the-fold images where useful.
- Avoid shipping duplicate image variants that are never used.
- Keep meaningful alt text separate from image optimization.

## 3. CSS strategy
The project has a local Tailwind CLI build and a browser CDN reference. Evaluate whether production can rely on the generated stylesheet only. This can reduce runtime dependencies and avoid browser-side utility generation.

Confirm the Tailwind content configuration catches all used classes before removing the CDN script.

## 4. Third-party requests
Review external origins for necessity, privacy implications, availability, caching, and supply-chain risk. Avoid adding external scripts for purely decorative behavior.

## 5. Measurement process
Use browser DevTools or Lighthouse on a deployed build. Record exact deployed URL and commit, date and browser version, device and network profile, Core Web Vitals or audit output, largest image and resource timings, layout shift sources, and before/after comparison.

A score without a reproducible environment and trace is not a reliable performance claim.
