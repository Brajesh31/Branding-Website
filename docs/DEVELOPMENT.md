# 🧑‍💻 Development Guide

## 1. Requirements
- Git.
- Node.js and npm.
- Python 3 for optional local serving and validation.
- A modern browser.

Use the Node.js version supported by the repository's Tailwind dependency. Check the package manifest and lockfile before upgrading toolchain versions.

## 2. Setup

~~~bash
git clone https://github.com/Brajesh31/Branding-Website.git
cd Branding-Website
npm ci
npm run build
~~~

## 3. Local preview

~~~bash
python -m http.server 8000
~~~

Open http://localhost:8000. Use Ctrl + C to stop the server.

## 4. Watch mode

~~~bash
npm run watch
~~~

The watcher regenerates CSS as configured source files change. Confirm the content glob includes any new HTML files.

## 5. Source map

| File | Responsibility |
|---|---|
| index.html | Landing page content |
| input.css | Tailwind directives and custom CSS input |
| tailwind.config.js | Tailwind content scanning and theme |
| package.json | Scripts and dependencies |
| package-lock.json | Reproducible dependency graph |
| Images/ | Existing editorial and SVG assets |
| docs/ | Engineering and product documentation |
| .github/ | Issue forms, PR guidance, CI |

## 6. Development workflow

~~~mermaid
flowchart TD
    A[Update local main] --> B[Create focused branch]
    B --> C[Implement one coherent change]
    C --> D[Run npm build]
    D --> E[Run repository validator]
    E --> F[Inspect in browser]
    F --> G[Update docs and screenshots]
    G --> H[Open pull request]
    H --> I[Review and CI]
    I --> J[Merge after approval]
~~~

## 7. Code conventions
- Prefer semantic HTML and accessible controls.
- Keep utility classes readable.
- Preserve exact asset path casing.
- Do not commit generated dependencies or secrets.
- Avoid unneeded packages.
- Document architecture changes and new dependencies.
- Do not claim inactive UI controls are functional.

## 8. Validation commands

~~~bash
npm ci
npm run build
python3 scripts/validate-repository.py
git status --short
~~~

The repository validator checks selected files and relative documentation links. It does not replace browser, accessibility, or security review.

## 9. Troubleshooting
See FAQ.md. When reporting a failure, include the command, complete relevant error, runtime versions, and reproduction steps. Remove secrets before sharing logs.
