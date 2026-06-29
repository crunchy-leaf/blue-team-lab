# Overview
The goal of this project is to create a Web Application Firewall (WAF) using Python that sits between the client and the web server. Every incoming HTTP request is intercepted and analyzed before it reaches the application. The firewall inspects request components such as the URL, headers, body, cookies, and query parameters, then evaluates the request against a collection of security rules. Based on the results, the request is either allowed or blocked, and all activity is logged for analysis and auditing.

## High level workflow diagram:

```mermaid
flowchart TD
    A[HTTP Request] --> B[Parse Incoming Request]
    B --> C[Extract Request Components]

    C --> D[URL]
    C --> E[Headers]
    C --> F[Body]
    C --> G[Cookies]
    C --> H[Parameters]

    D --> I[Rule Evaluation Engine]
    E --> I
    F --> I
    G --> I
    H --> I

    I --> J[Record Rule Matches]
    J --> K{Decision}

    K -->|Allow| L[Forward to Web Server]
    K -->|Block| M[Return Error Response]

    L --> N[Log Request]
    M --> N
```
 
