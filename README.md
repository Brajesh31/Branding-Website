# Fabulo — fashion branding landing page

Fabulo is a small, static fashion-brand landing page built with HTML and Tailwind CSS. The page presents seasonal collection copy, promotional sections, imagery, and a footer. It is a front-end design/demo: the visible shopping, rewards, social, and footer labels are not connected to commerce, account, or navigation services.

## What is in this repository

- A single page in **index.html**, with the Fabulo brand and collection sections.
- Tailwind directives in **input.css** and a Tailwind 3 configuration in **tailwind.config.js**.
- npm scripts for compiling and watching the stylesheet.
- Local SVG and JPEG assets in **Images/**.

The project does not include a JavaScript application framework, server, API, database, user accounts, payment processing, contact form, or environment configuration. See [Architecture](docs/architecture.md) for the current boundaries and [API](docs/api.md) for the network surface.

## Run locally

Prerequisites: Node.js and npm, plus a browser. From the repository root:

1. Install the exact locked dependencies with **npm ci**.
2. Start a local static server from the repository root. For example, with Python installed, run **python -m http.server 8000**.
3. Open **http://localhost:8000** in a browser.

A local server keeps relative image and stylesheet paths consistent with static hosting. The page also loads Tailwind's browser CDN script from the network. Review [Installation](docs/installation.md) for alternatives and details.

## Build the stylesheet

Run **npm run build** to invoke the Tailwind CLI. The configured output path is **css/style.css**, which is referenced by the HTML page. The generated file is not tracked; regenerate it after checkout and before publishing a deployment that needs the compiled stylesheet. The page also includes the Tailwind CDN script, so deployments currently depend on that external script for its runtime styling behavior.

Use **npm run watch** while editing to regenerate the CSS when source content changes. Tailwind scans only root-level HTML files as configured in **tailwind.config.js**. If you add HTML elsewhere, update the content globs.

## Project documentation

- [Architecture](docs/architecture.md)
- [Installation](docs/installation.md)
- [Development](docs/development.md)
- [Deployment](docs/deployment.md)
- [API and external requests](docs/api.md)
- [Database and persistence](docs/database.md)
- [Troubleshooting](docs/troubleshooting.md)
- [Frequently asked questions](docs/faq.md)
- [Contributing](CONTRIBUTING.md)
- [Security policy](SECURITY.md)
- [Support](SUPPORT.md)
- [Roadmap](ROADMAP.md)

## Assets and licensing

The project source is licensed under the MIT License; see [LICENSE](LICENSE). That grant applies to the project code and does not claim ownership of third-party material. The JPEG filenames identify Unsplash photographers, but this repository does not record source-page URLs or asset-specific license metadata. The SVG files also have no provenance record in the repository. Verify the applicable rights and attribution requirements for each image before reusing or redistributing those assets.

## Browser and accessibility notes

The document uses semantic navigation, header, section, and footer elements, but this is a minimal design snapshot rather than a complete commerce experience. Images currently have no alternative text, the SVG images do not declare accessible labels, and the visible buttons are not wired to actions. Address these items before presenting the page as a finished accessible storefront.

## Maintainer

Brajesh Kumar — GitHub [@brajesh31](https://github.com/brajesh31).

Last updated: 2026-10-15 20:49 UTC
