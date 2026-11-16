# 🧪 Testing Strategy

## 1. Current automated checks

The repository includes a dependency-free Python test suite for static HTML and local repository integrity, plus a documentation/link validator. These checks are intentionally lightweight. They do not replace browser automation or human accessibility review.

## 2. Run the complete local check sequence

~~~bash
npm ci
npm run build
npm test
python3 scripts/validate-repository.py
~~~

The stylesheet must be built before running the test suite because the HTML references the generated `css/style.css` asset.

## 3. Automated test coverage

The suite in `tests/test_repository.py` currently checks:

| Test | What it verifies |
|---|---|
| Document metadata | HTML language and non-empty page title |
| Heading structure | Exactly one primary h1 |
| Image alternatives | Every image has an alt attribute, including empty alt for decorative images |
| Local assets | Referenced local images, scripts, and stylesheets exist after build |
| In-page navigation | Fragment links resolve to an element ID |
| Support files | Essential site and repository policy files exist |

The suite uses Python's standard library. It does not require pytest or an external test framework.

## 4. Build smoke test

~~~bash
npm ci
npm run build
~~~

Expected evidence:
- npm install exits successfully.
- Tailwind CLI exits successfully.
- The configured stylesheet output exists and is non-empty.
- No build errors are hidden by shell piping.

## 5. Repository documentation validation

~~~bash
python3 scripts/validate-repository.py
~~~

This validates selected repository-authored files and relative Markdown links. It does not execute the site in a browser or validate external URLs.

## 6. Manual browser scenarios

| ID | Scenario | Expected result |
|---|---|---|
| WEB-01 | Open root page | Page loads without fatal error |
| WEB-02 | Load editorial images | All referenced assets resolve |
| WEB-03 | Load stylesheet | Generated CSS request succeeds |
| WEB-04 | Narrow viewport | No unintended horizontal overflow |
| WEB-05 | Keyboard navigation | Focus is visible and order is logical |
| WEB-06 | Image semantics | Alternatives reflect image purpose |
| WEB-07 | Footer | Labels are not misleading inactive links |
| WEB-08 | 404 route | Host serves the custom not-found page |
| WEB-09 | Manifest and favicon | Browser metadata assets load |
| WEB-10 | Browser console | No new uncaught errors or failed critical requests |

## 7. Responsive matrix

| Class | Viewport |
|---|---:|
| Small phone | 320 × 568 |
| Phone | 390 × 844 |
| Tablet | 768 × 1024 |
| Laptop | 1366 × 768 |
| Desktop | 1920 × 1080 |

These are test targets, not a statement that all devices have been tested.

## 8. Accessibility review

Use keyboard-only navigation, browser zoom, semantic inspection, contrast measurement, and assistive technology where available. Record tool versions and findings. Do not claim WCAG conformance from static checks alone.

## 9. Future test opportunities

Consider adding Playwright browser tests, screenshot-based visual regression, automated accessibility scans, and HTML validation when the project has a maintained browser test environment. Add tooling only with clear value, documented ownership, and CI runtime budget.

## 10. Test evidence

A useful report includes commit SHA, date, operating system, browser/version, viewport, commands, pass/fail result, logs, screenshots, known limitations, and issue references.

Never fabricate test output, coverage numbers, Lighthouse scores, or compliance results.
