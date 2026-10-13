# Installation

This guide prepares a local checkout of the Fabulo static landing page.

## Requirements

- Git, if cloning the repository.
- A supported Node.js installation with npm for the Tailwind CLI commands. The dependency graph is locked in **package-lock.json**; use the repository's npm lockfile rather than installing Tailwind globally.
- A modern browser.
- Python 3 or another simple static HTTP server for serving the page locally.

This project has no database, backend service, or environment-variable setup.

## Get the source

Clone the GitHub repository and enter its root directory:

    git clone https://github.com/Brajesh31/Branding-Website.git
    cd Branding-Website

If the source is already present locally, change to the directory containing **package.json** and **index.html**.

## Install dependencies

Install the exact dependency versions from the lockfile:

    npm ci

The project declares Tailwind CSS as a development dependency. Installation is not needed merely to view the page through its CDN script, but it is needed to run the local CSS build or watch command.

## Serve the page

Start a static server from the repository root. For example:

    python -m http.server 8000

Then visit **http://localhost:8000**. Keep the server process running while browsing. The page uses relative URLs for **Images/** and **css/style.css**, so serving the repository root preserves the expected paths.

If Python is unavailable, use any static HTTP server configured to serve the repository root. Opening the HTML file directly may work in some browsers, but a server is the reliable way to verify relative assets and generated CSS.

## Optional: compile Tailwind CSS

The package build script writes its output to **css/style.css**:

    npm run build

The generated stylesheet is ignored by Git. Run the build on a fresh checkout before testing or deploying the generated CSS. The HTML also loads Tailwind from **https://cdn.tailwindcss.com**, so the current page still requests that external resource.

To rebuild automatically while editing:

    npm run watch

Stop the watch process with Ctrl+C.
