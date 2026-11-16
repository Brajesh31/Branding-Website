# 🚀 Deployment Guide

## 1. Deployment model
Fabulo is a static frontend. It can be hosted by a static web host that serves HTML, CSS, and image files. The current repository does not establish a specific production provider or deployment target.

## 2. Required artifact
The published site needs index.html, Images/ and its referenced assets, generated css/style.css, and any other static resources referenced by the page.

The build script targets css/style.css. Generate it before publishing:

~~~bash
npm ci
npm run build
~~~

Confirm the file exists and that the published root contains it.

## 3. Deployment flow

~~~mermaid
flowchart TD
    A[Checkout intended commit] --> B[Install locked dependencies]
    B --> C[Run Tailwind build]
    C --> D{Build successful?}
    D -->|No| E[Stop and inspect logs]
    D -->|Yes| F[Verify generated CSS and assets]
    F --> G[Publish static root]
    G --> H[Open deployed URL]
    H --> I[Check page, assets, console, responsive layout]
    I --> J{Release verified?}
    J -->|No| K[Rollback to known-good artifact]
    J -->|Yes| L[Record release commit and URL]
~~~

## 4. Host configuration
For the selected provider, record repository and branch, build command, publish directory, Node.js version, custom domain and DNS ownership, HTTPS configuration, cache behavior, and rollback method.

Suggested build command: npm ci && npm run build. The publish directory is the repository root, provided the host runs the build in that root.

Do not add provider-specific files or claim successful deployment until the provider is confirmed and tested.

## 5. Production checks
- [ ] Build succeeds from a clean checkout.
- [ ] Generated CSS is in the published artifact.
- [ ] All image paths resolve with correct case.
- [ ] No source maps or local-only files are unintentionally published.
- [ ] HTTPS is active.
- [ ] Browser console and network panel reviewed.
- [ ] Mobile and desktop layout checked.
- [ ] External CDN dependency decision documented.
- [ ] Previous known-good release can be restored.

## 6. Rollback
Keep the last known-good commit or deployment artifact available. If a release breaks the page, restore the previous artifact or redeploy the known-good commit. Verify the rollback with the same page, asset, and browser checks.

## 7. Cache and stylesheet notes
If CSS changes do not appear, inspect the deployed artifact, network response, cache headers, and browser cache. Do not solve stale content by repeatedly changing unrelated source files.
