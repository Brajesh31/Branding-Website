# Troubleshooting

## Styles appear missing or incomplete

- Confirm the browser can access the Tailwind CDN script referenced from **index.html**.
- If relying on the compiled stylesheet, run **npm ci** and **npm run build**. The build writes **css/style.css**, which is ignored by Git and must be regenerated after a fresh checkout.
- Confirm the generated file is reachable at **/css/style.css** from the static server.
- Tailwind scans only root-level HTML files in the current configuration. If markup was added in a nested directory, update **tailwind.config.js** and rebuild.
- Clear the browser cache and reload after changing CSS.

## Images do not load

Serve the project from its root directory and inspect the failed request URL in browser developer tools. Preserve exact directory and filename case: the asset directory is **Images/**, and the SVGs are under **Images/SVG/**. Case-sensitive hosting may reject a differently cased path that worked on a case-insensitive local filesystem.

## npm installation or CLI fails

- Confirm you are in the directory containing **package.json** and **package-lock.json**.
- Use a maintained Node.js and npm installation compatible with the locked Tailwind CSS dependency.
- Remove only the project's local **node_modules/** directory and rerun **npm ci** if the dependency install is incomplete.
- Read the first error from npm output; network and registry proxy problems can prevent package installation.

## The page looks blank when opening the file

Start a local static server from the repository root, for example with **python -m http.server 8000**, and visit **http://localhost:8000**. A static server gives the browser consistent relative paths for images and CSS.

## Buttons and footer items do nothing

This is the current repository behavior. The visible buttons and footer/social labels are presentation text without destinations, event handlers, or server integration. They do not implement shopping, payment, rewards, account, social, or support services.

## A CDN request is blocked

The page includes **https://cdn.tailwindcss.com**. A network filter, offline browser, or CDN outage can affect styling. The repository also has a local Tailwind CLI build, but changing to a self-hosted-only production approach requires checking the generated stylesheet and updating the HTML and deployment configuration accordingly.

## Where should I report another issue?

Use the project's [Support guide](../SUPPORT.md). For a security concern, follow the private reporting instructions in [SECURITY.md](../SECURITY.md).
