# 🌐 Static Page Request Flow

~~~mermaid
flowchart TD
    Visitor[Visitor browser] -->|GET /| Host[Static hosting origin]
    Host --> HTML[index.html]
    HTML --> CSS[css/style.css]
    HTML --> Images[Images directory]
    HTML --> CDN[Tailwind browser CDN script]
    CSS --> Page[Rendered landing page]
    Images --> Page
    CDN --> Page
~~~

No project-owned API, database, authentication provider, or payment service participates in the current request flow.
