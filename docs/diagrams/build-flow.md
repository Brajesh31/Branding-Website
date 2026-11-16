# 🏗️ Build and Publish Flow

~~~mermaid
flowchart TD
    A[Checkout source] --> B[npm ci]
    B --> C[Tailwind CLI build]
    C --> D{Build successful?}
    D -->|No| E[Inspect logs and fix]
    D -->|Yes| F[Verify css/style.css]
    F --> G[Publish static root]
    G --> H[Open deployed page]
    H --> I[Check images, styles, console, responsive layout]
    I --> J{Verified?}
    J -->|No| K[Rollback or fix]
    J -->|Yes| L[Record release]
~~~
