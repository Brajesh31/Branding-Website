# 🧪 Testing Strategy

## 1. Current state
The project currently defines Tailwind build and watch commands. A build check is available. No dedicated unit, integration, browser E2E, visual regression, or accessibility test framework is assumed by this guide.

## 2. Build smoke test

~~~bash
npm ci
npm run build
~~~

Expected evidence:
- npm install exits successfully.
- Tailwind CLI exits successfully.
- The configured stylesheet output exists.
- No build errors are hidden by shell piping.

## 3. Repository structure validation

~~~bash
python3 scripts/validate-repository.py
~~~

This validates selected repository files and relative Markdown links. It does not execute the site in a browser.

## 4. Manual browser scenarios

| ID | Scenario | Expected result |
|---|---|---|
| WEB-01 | Open root page | Page loads without fatal error |
| WEB-02 | Load editorial images | All referenced assets resolve |
| WEB-03 | Load stylesheet | Generated CSS request succeeds |
| WEB-04 | Narrow viewport | No unintended horizontal overflow |
| WEB-05 | Keyboard navigation | Focus is visible and order is logical |
| WEB-06 | Image semantics | Alternatives reflect image purpose |
| WEB-07 | Footer | Labels are not misleading inactive links |
| WEB-08 | CTA controls | Controls work or are not interactive |

## 5. Responsive matrix

| Class | Viewport |
|---|---:|
| Small phone | 320 × 568 |
| Phone | 390 × 844 |
| Tablet | 768 × 1024 |
| Laptop | 1366 × 768 |
| Desktop | 1920 × 1080 |

These are test targets, not a statement that all devices have been tested.

## 6. Accessibility review
Use keyboard-only navigation, browser zoom, semantic inspection, contrast measurement, and assistive technology where available. Record tool versions and findings.

## 7. Test evidence
A useful report includes commit SHA, date, operating system, browser/version, viewport, commands, pass/fail result, logs, screenshots, known limitations, and issue references.

Never fabricate test output, coverage numbers, Lighthouse scores, or compliance results.
