# 🧭 Fabulo Roadmap

This roadmap separates the current implementation from potential future work. A roadmap item is not a delivered feature. Prioritize improvements by user value, risk, complexity, and maintenance cost.

## 🧱 Current baseline
- [x] Static HTML landing page.
- [x] Tailwind CSS CLI build and watch commands.
- [x] Local JPEG and SVG assets.
- [x] Repository setup and contribution documentation.
- [x] Architecture and workflow documentation.

## 🧹 Quality and accessibility
- [ ] Add meaningful image alternatives and dimensions.
- [ ] Review semantic landmarks and heading order.
- [ ] Replace non-functional buttons with real destinations or non-interactive presentation.
- [ ] Audit contrast and visible keyboard focus.
- [ ] Verify responsive behavior on real browsers and devices.
- [ ] Optimize editorial imagery based on measured rendering needs.
- [ ] Decide whether to remove the Tailwind browser CDN in production.

## 🧪 Engineering quality
- [ ] Add HTML validation to CI.
- [ ] Add link and asset reference validation.
- [ ] Add browser smoke tests if automated behavior checks are needed.
- [ ] Add accessibility automation and manual assistive-technology review.
- [ ] Record a reproducible performance baseline.
- [ ] Review and minimize workflow permissions.

## 🎨 Product and design
- [ ] Capture genuine screenshots at documented viewport sizes.
- [ ] Document typography, color, spacing, and image treatment as reusable design tokens.
- [ ] Review mobile navigation semantics and usability.
- [ ] Add visual regression checks if visual changes become frequent.

## 🛍️ Potential product expansion, not currently committed

A real commerce experience would require a separate product and architecture decision. It may involve catalogue ownership, product data, inventory, cart, checkout, payment provider, shipping, taxes, returns, support, privacy, security, and operational monitoring.

Do not add payment or customer-data collection merely to make the repository appear more sophisticated. Establish business requirements and a threat model first.

## 📊 Prioritization rubric

| Priority | Meaning |
|---|---|
| P0 | Security, data loss, or release-blocking defect |
| P1 | Core usability, accessibility, or build reliability |
| P2 | Valuable quality improvement |
| P3 | Optional polish or experiment |

Each roadmap change should have an issue, clear acceptance criteria, owner, and evidence of completion.
