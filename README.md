# 👗 Fabulo | Fashion Brand Landing Page

<p align="center">
  <img src="https://img.shields.io/badge/Project-Fabulo-AF7452?style=for-the-badge" alt="Fabulo">
  <img src="https://img.shields.io/badge/HTML5-Static%20Website-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5">
  <img src="https://img.shields.io/badge/Tailwind_CSS-3.x-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white" alt="Tailwind CSS">
  <img src="https://img.shields.io/badge/License-MIT-2E8B57?style=for-the-badge" alt="MIT">
</p>

<p align="center"><strong>A minimal editorial fashion-brand landing page concept built with HTML and Tailwind CSS.</strong></p>

---

## ✨ Overview

**Fabulo** is a fashion-brand website concept focused on editorial presentation, seasonal collection storytelling, streetwear imagery, promotional messaging, and a clean footer. Its visual direction uses warm neutral surfaces, dark typography, brown accents, and fashion photography.

> ⚠️ **Scope clarification:** This repository currently contains a static frontend concept. It is not a functioning e-commerce platform. Shopping, cashback, financing, and payment-related copy is presentation content only. There is no cart, checkout, inventory, account system, payment processor, reward engine, or order backend.

### 🎯 Project goals
- 🧵 Present a coherent fashion identity through a single landing page.
- 🖼️ Use local editorial imagery and vector assets.
- 🎨 Maintain a consistent visual hierarchy and warm palette.
- 📱 Keep the layout usable across mobile and desktop viewports.
- 🛠️ Provide a reproducible Tailwind CSS build.
- 📚 Make the repository maintainable through detailed documentation.

## 🪄 Page experience

| Area | Visitor experience | Current behavior |
|---|---|---|
| 🏷️ Brand header | Fabulo identity and visual navigation assets | Static presentation |
| 🌸 Seasonal story | Spring/Summer editorial heading, copy, and imagery | Static content |
| 📼 Retro story | Retro-inspired collection narrative | Static content; CTA is not wired |
| 🧢 Streetwear story | Streetwear feature and imagery | Static content; CTA is not wired |
| 💳 Promotional strip | Cashback, financing, and payment-themed messages | Illustrative copy only |
| 🔗 Footer | Social, service, activity, and other labels | Plain text, not live links |

Screenshots should be captured from the actual running page and stored in docs/assets/. Do not use fabricated screenshots as proof of implementation.

## 🧰 Technology stack

| Technology | Purpose |
|---|---|
| HTML5 | Page structure and content |
| Tailwind CSS 3 | Utility-first styling |
| Node.js + npm | Build tooling and dependency management |
| Tailwind CLI | Generates the local stylesheet |
| SVG | Vector assets |
| JPEG | Editorial photography |
| Static hosting | Deployment model |

Node.js is a build requirement, not an application server. No framework, API server, database, authentication service, payment SDK, or analytics platform is part of the current implementation.

## 🗂️ Repository structure

~~~text
Branding-Website/
├── .github/
│   ├── ISSUE_TEMPLATE/       # Structured issue forms
│   ├── workflows/            # CI and security automation
│   └── PULL_REQUEST_TEMPLATE.md
├── Images/                   # Existing editorial images and SVG assets
├── css/                      # Tailwind build output (generated)
├── docs/
│   ├── assets/               # Genuine screenshots and visual assets
│   ├── diagrams/             # Mermaid architecture and flow diagrams
│   ├── templates/            # Reusable engineering templates
│   ├── ACCESSIBILITY.md
│   ├── ARCHITECTURE.md
│   ├── DEPLOYMENT.md
│   ├── DEVELOPMENT.md
│   ├── FAQ.md
│   ├── FEATURES.md
│   ├── PERFORMANCE.md
│   ├── PROJECT_OVERVIEW.md
│   ├── QA.md
│   ├── SECURITY_MODEL.md
│   └── TESTING.md
├── scripts/
│   └── validate-repository.py
├── index.html
├── input.css
├── package.json
├── package-lock.json
├── tailwind.config.js
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── ROADMAP.md
├── SECURITY.md
└── SUPPORT.md
~~~

This is an orientation guide, not a command to remove existing files. Generated output and existing repository files may vary. Preserve existing assets and IDE files unless there is a deliberate, reviewed reason to change them.

## 🚀 Quick start

### Prerequisites
- Node.js compatible with the installed Tailwind toolchain.
- npm and Git.
- A modern browser.

### Installation and build

~~~bash
git clone https://github.com/Brajesh31/Branding-Website.git
cd Branding-Website
npm ci
npm run build
~~~

### Run locally

~~~bash
python -m http.server 8000
~~~

Open http://localhost:8000.

For automatic CSS rebuilding during development:

~~~bash
npm run watch
~~~

Stop the watcher or server with Ctrl + C.

### Available npm scripts

| Script | Purpose |
|---|---|
| npm run build | Compile Tailwind CSS into the configured output |
| npm run watch | Watch configured source files and rebuild CSS |

The package manifest is the source of truth for available scripts. Do not assume test, lint, start, or preview exists unless it is added and maintained.

## 🏗️ Architecture and request flow

The application is intentionally static. There is no application server or database in the current design.

~~~mermaid
flowchart TD
    A[Visitor opens Fabulo] --> B[Static hosting origin]
    B --> C[index.html]
    C --> D[Local Images assets]
    C --> E[Generated css/style.css]
    C --> F[Tailwind browser CDN script]
    D --> G[Browser renders page]
    E --> G
    F --> G
~~~

Build pipeline:

~~~mermaid
flowchart LR
    A[Clone repository] --> B[npm ci]
    B --> C[Tailwind CLI]
    C --> D[css/style.css]
    D --> E[Static host]
    E --> F[Visitor browser]
~~~

The HTML references both generated CSS and a Tailwind browser CDN script. Review this dual approach before production deployment. A predictable production setup should normally use the compiled local stylesheet and avoid unnecessary runtime dependencies.

## 🧪 Quality checks

Before submitting a change:
1. Run npm ci when dependencies have changed.
2. Run npm run build.
3. Confirm the generated stylesheet exists at the configured path.
4. Serve the site locally and inspect all sections.
5. Check browser console and network requests.
6. Review mobile and desktop layouts.
7. Verify keyboard focus and image alternatives.
8. Confirm buttons and links have real behavior or are not presented as interactive controls.
9. Update relevant documentation.

Run the repository structure validator:

~~~bash
python3 scripts/validate-repository.py
~~~

This script checks repository documentation and key source files. It is not a browser test, accessibility certification, security audit, or proof of production readiness.

## 📚 Documentation

See docs/ for the complete guides, including project overview, feature inventory, architecture, development, deployment, accessibility, testing, QA, performance, security model, FAQ, Mermaid diagrams, and reusable engineering templates.

## 🧭 Roadmap

See ROADMAP.md for proposed improvements. Roadmap items are proposals until implemented and verified.

## 🤝 Contributing

Contributions are welcome. Read CONTRIBUTING.md, follow CODE_OF_CONDUCT.md, and use the pull request template. For security-sensitive issues, follow SECURITY.md instead of opening a public issue.

## 🛡️ Security

This is a static frontend. Do not submit credentials, tokens, private user data, or payment details. Report vulnerabilities privately using SECURITY.md.

## 📄 License and asset rights

The project code is licensed under the MIT License. See LICENSE. Third-party photographs, icons, and other assets may have separate terms. Verify asset-specific rights and attribution before reuse; the repository's code license does not automatically grant rights to third-party imagery.

## 👤 Maintainer

Maintained by **Brajesh Kumar**.

<p align="center">Built with care for a clean, editorial fashion experience. 👗</p>

Last updated: 2026-11-16 21:44 UTC
