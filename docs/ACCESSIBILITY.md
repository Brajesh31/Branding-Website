# ♿ Accessibility Requirements and Review

## 1. Intent
Use WCAG 2.2 AA as a practical design and evaluation target. This document is guidance, not a certification or assertion that the current site conforms.

## 2. Current implementation notes
- Editorial images now include descriptive alt text.
- Header SVG marks are treated as decorative and hidden from assistive technology.
- The page has a skip link, a labeled navigation landmark, a main landmark, section headings, and footer sections.
- The previous non-functional buttons have been replaced with non-interactive editorial labels.
- Contrast and reading order still require review in actual browsers and assistive technology.

## 3. Semantic structure
Use one clear main content area and appropriate landmarks. Headings should describe the section hierarchy rather than being selected for visual size. Use links for navigation and buttons for actions.

## 4. Images
For each image, decide whether it communicates information:
- Informative image: provide concise alternative text that conveys relevant meaning.
- Decorative image: use an empty alt attribute.
- Complex image: provide an equivalent text explanation nearby.
- Avoid filenames or generic descriptions such as “image” as alternatives.

## 5. Keyboard and focus
Every interactive element must be reachable by keyboard, have a visible focus state, and activate with expected keyboard input. The page includes a skip link. Verify its focus behavior and all other controls in a browser.

## 6. Contrast and responsive use
Measure text and UI contrast against actual backgrounds. Do not rely on color alone. Confirm content remains usable at 200% zoom and narrow viewport widths.

## 7. Motion
If animation is added, avoid unnecessary motion, provide reduced-motion behavior, and ensure motion does not hide content or prevent interaction.

## 8. Manual review checklist
- [ ] Logical landmarks and heading order.
- [x] Editorial images have descriptive alternatives in the current HTML.
- [x] Decorative header SVGs are ignored by assistive technology.
- [x] Non-functional calls to action are not exposed as active buttons.
- [ ] Skip link and keyboard focus verified in browser.
- [ ] Text and UI contrast measured.
- [ ] 200% zoom and reflow are usable.
- [ ] Screen-reader reading order is understandable.
- [ ] No content relies only on color or hover.

The checked items describe source-level changes, not completed assistive-technology verification. Automated tools are useful for finding common issues, but manual testing remains necessary.
