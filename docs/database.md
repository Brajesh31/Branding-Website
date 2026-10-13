# Database and persistence

## Current data model

This project has no database and defines no server-side data model. The rendered page content is written directly in **index.html**. Images and vector assets are files in **Images/**. Tailwind configuration and package metadata are local project configuration, not visitor records.

## Persistence

The site does not implement accounts, cookies, browser storage, user preferences, cart state, orders, messages, or a content-management workflow. The visible promotional copy about cashback and payment options is static presentation content; it does not record activity or process payments.

## Data flow

A visitor's browser requests the static page and its local assets from the configured host. It also requests the Tailwind browser script from the external CDN referenced in the HTML. The checked-in source does not contain an application submission or data-writing request.

## Future changes

If a feature starts collecting or persisting data, document:

- The data fields, purpose, and data owner.
- Where data is stored, how long it is retained, and how deletion is handled.
- Authentication, authorization, encryption, backup, and access controls.
- Any third-party processor, network request, or privacy notice required.
- Local development and deployment setup without committing credentials.

Update this document, [API behavior](api.md), [Security](../SECURITY.md), and [Deployment](deployment.md) before shipping a feature that changes these boundaries.
