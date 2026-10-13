# Frequently asked questions

## What is Fabulo?

Fabulo is a static fashion-brand landing-page design/demo. It has one HTML page with collection descriptions, promotional copy, local imagery, and footer labels. It is not a working online store.

## What technology does it use?

The page is plain HTML with Tailwind utility classes. The npm package scripts call the Tailwind CSS CLI to build or watch **input.css**. The HTML also loads Tailwind from its browser CDN. No front-end framework, bundler, or application server is configured.

## How do I view it locally?

Install dependencies with **npm ci** if you need the Tailwind CLI, then serve the repository root with a static server such as **python -m http.server 8000**. Visit **http://localhost:8000**. See [Installation](installation.md).

## Do I need Node.js just to view the page?

The HTML can be served as static files without a Node.js runtime. Node.js and npm are needed for the repository's build and watch commands. The current HTML makes a network request to Tailwind's CDN.

## Where does the compiled CSS go?

The build script writes **css/style.css**. This generated file is ignored by Git, so run **npm run build** after cloning and as part of deployment when the published page needs the compiled file.

## Is the page responsive?

The source uses some Tailwind flex and wrapping classes, but the repository has no recorded responsive test coverage. Review the layout at narrow and wide widths before relying on it in production.

## Do the buttons place orders or send messages?

No. “Shop Now”, “Collect”, and “Explore” are visible button labels without handlers. The page does not have checkout, payment processing, rewards tracking, a contact form, user accounts, or social links.

## Does the page store visitor data?

No application database or browser-storage behavior is configured in the project source. The browser requests the page's static assets and the Tailwind CDN script.

## Can I reuse the photos and SVG files?

The MIT license covers the project's code and documentation, not necessarily the included images. The filenames identify some photo authors, but the repository does not provide source URLs or rights records. Confirm the terms for each asset and preserve any required attribution before reuse. See [README](../README.md).

## Where do I report problems or vulnerabilities?

For ordinary project questions and reproducible bugs, see [Support](../SUPPORT.md). For a suspected vulnerability, use the private reporting guidance in [Security](../SECURITY.md).
