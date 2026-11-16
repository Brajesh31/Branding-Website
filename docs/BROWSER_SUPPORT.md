# 🌐 Browser Support and Compatibility

## 1. Support policy
The project targets modern evergreen browsers that support current HTML, CSS, flexbox, and the Tailwind CSS output used by the page. No formal browser certification or compatibility test matrix is currently recorded.

## 2. Suggested browser coverage

| Browser family | Suggested verification |
|---|---|
| Chrome / Chromium | Latest stable desktop and mobile |
| Microsoft Edge | Latest stable |
| Firefox | Latest stable |
| Safari | Current macOS and iOS versions available for testing |

These are recommendations for testing, not claims that every browser has already been verified.

## 3. Test scenarios
- Page loads without a fatal error.
- Local CSS and image resources resolve.
- Fonts and image crops remain intentional.
- Layout wraps without horizontal overflow.
- Buttons and links behave consistently.
- Keyboard focus remains visible.
- Zoom and responsive reflow remain usable.

## 4. Compatibility constraints
Avoid relying on experimental CSS without a fallback. Test external script dependencies separately from locally generated CSS. Verify case-sensitive asset paths on a Linux-like host.

## 5. Reporting
Record browser name/version, operating system, viewport, commit SHA, reproduction steps, expected result, actual result, and screenshot or console evidence.
