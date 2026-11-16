# 🤝 Contribution Flow

~~~mermaid
flowchart TD
    A[Identify problem] --> B[Open or review issue]
    B --> C[Create focused branch]
    C --> D[Implement change]
    D --> E[Run build and validation]
    E --> F[Browser and accessibility review]
    F --> G[Update docs and evidence]
    G --> H[Open pull request]
    H --> I[CI and maintainer review]
    I --> J{Approved?}
    J -->|No| D
    J -->|Yes| K[Merge]
~~~
