# ♿ Accessibility Requirements and Review

## 1. Intent
Use WCAG 2.2 AA as a practical design and evaluation target. This document is guidance, not a certification or assertion that the current site conforms.

## 2. Current issues to review
- Existing image elements need meaningful alternatives or empty alternatives when decorative.
- Image-only header visuals need a clear purpose and accessible name if interactive.
- Visible call-to-action buttons need working behavior or should not use button semantics.
- Heading order and semantic landmarks should be reviewed.
- Color contrast must be measured from rendered colors.
- Keyboard focus should be visible.

## 3. Semantic structure
Use one clear main content area and appropriate landmarks. Headings should describe the section hierarchy rather than being selected for visual size. Use links for navigation and buttons for actions.

## 4. Images
For each image, decide whether it communicates information:
- Informative image: provide concise alternative text that conveys relevant meaning.
- Decorative image: use an empty alt attribute.
- Complex image: provide an equivalent text explanation nearby.
- Avoid filenames or generic descriptions such as “image” as alternatives.

## 5. Keyboard and focus
Every interactive element must be reachable by keyboard, have a visible focus state, and activate with expected keyboard input. Do not create custom controls unless native HTML elements are insufficient.

## 6. Contrast and responsive use
Measure text and UI contrast against actual backgrounds. Do not rely on color alone. Confirm content remains usable at 200% zoom and narrow viewport widths.

## 7. Motion
If animation is added, avoid unnecessary motion, provide reduced-motion behavior, and ensure motion does not hide content or prevent interaction.

## 8. Manual review checklist
- [ ] Logical landmarks and heading order.
- [ ] Informative images have useful alt text.
- [ ] Decorative images are ignored by assistive technology.
- [ ] Links and buttons have accessible names.
- [ ] All interactions work with keyboard.
- [ ] Focus indicator is visible.
- [ ] Text and UI contrast is measured.
- [ ] 200% zoom and reflow are usable.
- [ ] Screen-reader reading order is understandable.
- [ ] No content relies only on color or hover.

Automated tools are useful for finding common issues, but manual testing remains necessary.
