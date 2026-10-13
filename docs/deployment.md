# Deployment

## Deployment model

This repository is a static website. A static hosting service can serve its files; no application server, database, runtime secrets, or API deployment is required. No host-specific deployment configuration is currently committed, so configure the selected provider to serve the repository root.

## Prepare a deployment

From a clean checkout:

1. Install the locked development dependency graph using **npm ci**.
2. Run **npm run build** to generate **css/style.css**.
3. Confirm the deployment includes **index.html**, **Images/**, and the generated **css/style.css**.
4. Configure the static host's published directory as the repository root, because the HTML and asset folders live there.
5. Use HTTPS and verify the deployed page at desktop and mobile widths.

The build script does not define a separate **dist/** output directory; Tailwind writes its CSS into the repository's **css/** subdirectory. The generated CSS file is ignored by Git, so a host that serves a Git checkout directly must run the build command during deployment or receive the generated file through another deliberate process.

## External styling dependency

**index.html** also loads Tailwind from **https://cdn.tailwindcss.com**. This means the published page makes a request to an external service and its CDN styling behavior depends on network access and the availability of that script. Review that dependency and the current compiled stylesheet together when choosing a production policy. The project does not currently provide a Content Security Policy, integrity pin, or self-hosted-only configuration.

## Hosting checks

- Preserve directory and filename case, particularly **Images/** and its nested **SVG/** folder.
- Confirm every image URL and the **css/style.css** URL returns successfully.
- Ensure the host serves **index.html** at the site root.
- Check browser developer tools for failed requests and unexpected external requests.
- Do not publish **node_modules/** or local environment files.
- Remember that the page is a design/demo: its visible shopping buttons and social/footer labels are not connected to live services.

## Rollback

Each repository change is committed independently. To roll back a documentation or metadata change, revert its commit. For a deployment issue, redeploy the last known-good revision and preserve build logs for diagnosis.
