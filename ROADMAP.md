# Roadmap

This is a lightweight set of possible directions, not a delivery schedule or commitment. Priorities may change as the project evolves.

## Current baseline

The repository contains one static Fabulo fashion landing page, local image and SVG assets, and a Tailwind CLI workflow. Buttons and footer labels are visual placeholders. There is no checkout, catalog service, content management, user data store, or backend.

## Potential next steps

### Accessibility and responsive behavior

- Add descriptive alternative text to informative photos and accessible names to SVG or icon imagery.
- Check heading hierarchy, keyboard focus visibility, color contrast, and controls at mobile and desktop sizes.
- Verify layout at common viewport widths and with zoom enabled.

### Styling and delivery

- Decide whether to rely on the Tailwind browser CDN, generated CSS, or a single documented strategy.
- Make a reproducible static build and deployment process, including the expected output files and host configuration.
- Add a responsive navigation pattern if navigation links are introduced.

### Functional interactions

- Define actual destinations and behavior for the current buttons and footer entries before presenting them as interactive controls.
- If commerce or forms are introduced, design the required trusted services, privacy disclosures, accessibility, validation, and abuse protection first.

### Asset records

- Record source URLs, author attribution, and license or permission information for each included image and vector asset.
- Replace any asset whose origin or permitted reuse cannot be verified.

## Prioritization

Open an issue to propose a roadmap item. Explain the user need, expected scope, dependencies, and any new external service or data collection.
