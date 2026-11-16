# 🎨 Fabulo Design System Notes

## 1. Purpose
This document records the visual language visible in the current page and provides consistency guidance for future edits. It is not a formal token library or a claim that all components already follow these rules.

## 2. Visual direction
Fabulo uses a warm editorial fashion direction: off-white surfaces, brown accents, dark text, serif branding, generous whitespace, and large fashion imagery.

## 3. Observed color references

| Token name | Value | Intended use |
|---|---|---|
| Canvas | #FBF7EE | Main page background |
| Brand accent | #AF7452 | Buttons, highlights, footer text |
| Primary text | Browser/default dark text | Main headings and copy |
| White | #FFFFFF | Contrast surfaces where required |

Before introducing additional colors, check whether an existing color can serve the same purpose. Verify contrast from rendered foreground/background pairs rather than relying on visual estimation.

## 4. Typography
- Use the existing serif treatment for the wordmark where appropriate.
- Keep editorial headings visually distinct from body copy.
- Use readable line lengths and sufficient line height.
- Avoid using heading tags solely to achieve a font size.

## 5. Spacing and layout
- Use consistent spacing between editorial blocks.
- Keep text and imagery aligned intentionally.
- Avoid fixed widths that cause overflow on narrow devices.
- Use responsive utilities deliberately and verify at real viewport widths.

## 6. Imagery
- Preserve the editorial tone.
- Use intentional crop and aspect ratio.
- Provide image dimensions and appropriate alternatives.
- Record image provenance and license information.

## 7. Interaction states
If controls are introduced or activated, define default, hover, focus-visible, active, and disabled states. Keyboard focus must be visible. Hover must not be the only way to discover or use a feature.

## 8. Design review checklist
- [ ] Brand colors are used consistently.
- [ ] Heading and body hierarchy is clear.
- [ ] Spacing is consistent across sections.
- [ ] Images have intentional crops.
- [ ] Layout works on mobile and desktop.
- [ ] Focus states are visible.
- [ ] Contrast is measured.
- [ ] Motion respects user preferences.
