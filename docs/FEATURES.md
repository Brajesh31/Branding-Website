# ✨ Feature Inventory and Behavior Matrix

This page inventories what the current HTML presents. It does not describe proposed features as delivered capabilities.

## 🧩 Current page areas

### 🏷️ Brand header
The header establishes the Fabulo identity and includes SVG visual assets. Verify whether each visual is decorative or intended to be a control. If it is a control, provide a destination, accessible name, and keyboard behavior.

### 🌸 Spring/Summer editorial
A seasonal heading, supporting copy, and image establish the collection narrative. Keep copy concise and imagery responsive.

### 📼 Retro-inspired editorial
The section pairs collection copy with imagery. Its visible “Shop Now” call-to-action is not wired to a destination or commerce behavior in the current source.

### 🧢 Streetwear editorial
A streetwear heading, description, and image create a second editorial story. The “Explore” call-to-action is not currently functional.

### 💳 Promotional messages
The page includes cashback, financing, and payment-themed text. These are static messages. No provider, terms engine, reward calculation, payment authorization, or secure checkout exists.

### 🔗 Footer
Footer groups contain plain labels. They should not be represented as active social or service links until real destinations are added.

## 📊 Capability matrix

| Capability | Status | Evidence / next step |
|---|---|---|
| Static landing page | Implemented | index.html |
| Tailwind CLI build | Configured | package.json |
| Local image assets | Present | Images/ |
| Responsive layout | Utility classes present | Verify actual browser widths |
| Shopping CTA behavior | Not implemented | Define destinations or remove button semantics |
| Product catalogue | Not implemented | Requires product source and UI |
| Cart and checkout | Not implemented | Requires architecture and payment design |
| Account and authentication | Not implemented | No auth flow or backend |
| Payment processing | Not implemented | Static promotional copy only |
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
    E --> F[Read promotional messages]
    F --> G[Reach footer]
~~~

## Acceptance criteria for future functionality
A new feature must define user value, visible behavior, responsive states, accessible semantics, data dependencies, privacy/security impact, failure behavior, testing evidence, and documentation updates.
