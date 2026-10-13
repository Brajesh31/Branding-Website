# Development

## Project shape

Fabulo is intentionally small: the page is plain **index.html**, and Tailwind CSS supplies utility styling. The dependency scripts are defined in **package.json**. There is no framework dev server, bundler, application code transpilation, test suite, linter, or formatting script configured in the repository.

## Start a local editing session

1. Install dependencies with **npm ci**.
2. Start **python -m http.server 8000** from the repository root.
3. Open **http://localhost:8000** in a browser.
4. In a second terminal, run **npm run watch** when you want the Tailwind CLI to regenerate CSS as files change.
5. Stop running processes with Ctrl+C.

The CDN script in the HTML requires network access. Test both generated styles and the page's behavior in a browser; the CLI does not validate functionality or accessibility.

## Where changes belong

- Edit **index.html** for page structure, copy, image references, and utility classes.
- Edit **input.css** for Tailwind layers and future custom CSS.
- Edit **tailwind.config.js** for theme extensions, plugins, and content globs.
- Add local images under **Images/**, with verified usage rights and recorded attribution.

The configured Tailwind content source is **./*.html**. It includes the current root document but not future nested HTML. Update the glob if new pages or templates are added so their utility classes are found during compilation.

## Existing UI behavior

The displayed “Shop Now”, “Collect”, “Explore”, and other button labels are not connected to actions. Footer and social names are plain text. Do not describe these as working commerce or navigation features until their actual destinations and behavior have been implemented.

The current photos and SVGs do not provide alternative text or explicit accessible names. When changing markup, use semantic controls, descriptive alternative text for meaningful images, accessible names for non-text controls, visible keyboard focus, and a responsive layout.

## Build and generated output

- **npm run build** compiles the configured Tailwind input to **css/style.css**.
- **npm run watch** runs that compilation in watch mode.
- The generated CSS is ignored by Git. Regenerate it after checkout and before serving a deployment that depends on the compiled output.
- The current HTML separately includes Tailwind's browser CDN script. Treat changes to either styling path as a deployment change and review both network and local behavior.

## Review before proposing a change

Inspect the rendered page at narrow and wide viewport sizes, check image loading and browser console output, confirm any new classes appear in compiled CSS, and verify keyboard interaction. For a change involving assets, include provenance and license details in the contribution.
