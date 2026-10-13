# Contributing

Thank you for considering a contribution to Fabulo. Contributions should improve this static landing page while keeping its scope, presentation, and setup clear.

## Before making a change

- Read the [Code of Conduct](CODE_OF_CONDUCT.md), [Security Policy](SECURITY.md), and [License](LICENSE).
- Check open issues and pull requests so work does not duplicate an active change.
- For a larger change, open an issue first to discuss the design and expected behavior.
- Confirm that any new images, fonts, icons, or other assets may legally be used and redistributed. Record the source and required attribution.

## Development setup

Use a supported Node.js release and npm. Clone the repository, enter its root, and install the lockfile-defined dependencies with **npm ci**. A local static server can be started with **python -m http.server 8000** from the repository root. Open the printed local address in a browser.

The page is plain HTML and Tailwind CSS. Edit **index.html** for page structure and content, **input.css** for Tailwind layers or custom CSS, and **tailwind.config.js** for scanning and theme configuration. Assets belong under **Images/** unless there is a clear reason to change the layout.

## Making a contribution

1. Create a focused branch from the current default branch.
2. Make the smallest coherent change that addresses the issue.
3. Keep HTML semantic, use meaningful alternative text for informative images, and preserve the existing relative asset paths.
4. If adding utility classes to a new HTML file or directory, update the Tailwind content globs so those classes are included in the generated stylesheet.
5. Avoid adding secrets, analytics, trackers, external services, or dependencies without explaining the need and their privacy and maintenance impact.
6. Run **npm run build** when changing HTML classes, Tailwind configuration, or stylesheet input. Review the generated output locally; generated **css/style.css** is not committed.
7. Inspect the page in a browser at narrow and wide viewport sizes. Check the browser console and verify image loading and keyboard behavior.
8. Commit the source changes with a clear message. Do not commit credentials, editor state, or generated build artifacts unless a maintainer requests them.

## Pull requests

A pull request should include:

- A concise description of the user-facing or maintenance change and its motivation.
- The issue it addresses, when applicable.
- Screenshots for visible layout changes at desktop and mobile widths.
- The browser and viewport used for visual review.
- The commands and manual checks performed, including any checks not run.
- Asset provenance and attribution for every newly added visual asset.
- Notes on external requests, privacy implications, accessibility impact, and deployment steps if relevant.

Keep pull requests reviewable and avoid bundling unrelated formatting or redesign work. Maintainers may request changes or decline a contribution that is out of scope, unsafe, legally unclear, or inconsistent with the project's direction.
