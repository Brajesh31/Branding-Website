# ✨ Feature Inventory and Behavior Matrix

This page inventories what the current HTML presents. It does not describe proposed features as delivered capabilities.

## 🧩 Current page areas

### 🏷️ Brand header
The header establishes the Fabulo identity and includes three decorative SVG marks. The marks are intentionally hidden from assistive technology because they have no navigation or action behavior. A skip-to-content link is provided.

### 🌸 Spring/Summer editorial
A seasonal heading, supporting copy, and image establish the collection narrative. The image includes descriptive alternative text and lazy loading.

### 📼 Retro-inspired editorial
The section pairs collection copy with imagery. The former “Shop Now” button has been replaced by a non-interactive editorial label because no shopping destination exists.

### 🧢 Streetwear editorial
A streetwear heading, description, and image create a second editorial story. The former “Explore” button is now a non-interactive label rather than a misleading control.

### 💳 Promotional concept cards
The page includes rewards, flexible-payment, and payment-information concepts. Each card explicitly says it is illustrative only. No provider, terms engine, reward calculation, payment authorization, or checkout exists.

### 🔗 Footer
Footer groups contain plain labels and are not represented as active social or service links. The footer now has semantic sections and a copyright/scope note.

## 📊 Capability matrix

| Capability | Status | Evidence / next step |
|---|---|---|
| Static landing page | Implemented | index.html |
| Tailwind CLI build | Configured | package.json |
| Local image assets | Present | Images/ |
| Responsive layout | Responsive utility classes added | Verify actual browser widths |
| Skip-to-content link | Added | Verify keyboard focus behavior |
| Editorial image alternatives | Added | Review wording with actual imagery |
| Shopping CTA behavior | Not implemented | Editorial labels are non-interactive |
| Product catalogue | Not implemented | Requires product source and UI |
| Cart and checkout | Not implemented | Requires architecture and payment design |
| Account and authentication | Not implemented | No auth flow or backend |
| Payment processing | Not implemented | Concept copy only |
| Cashback/rewards | Not implemented | No reward engine |
| Contact form | Not implemented | No form submission path |
| Analytics | Not configured | No analytics integration identified |

## 🧭 Visitor flow

~~~mermaid
flowchart TD
    A[Open landing page] --> B[Read brand header]
    B --> C[Explore seasonal story]
    C --> D[Explore retro story]
    D --> E[Explore streetwear story]
    E --> F[Read illustrative concept cards]
    F --> G[Reach footer]
~~~

## Acceptance criteria for future functionality
A new feature must define user value, visible behavior, responsive states, accessible semantics, data dependencies, privacy/security impact, failure behavior, testing evidence, and documentation updates.
