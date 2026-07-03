# System Architecture

## Overview
This project is a Python-based Web Application Firewall (WAF) that operates as a reverse proxy. It intercepts HTTP requests, analyzes them for malicious patterns, and either blocks or forwards them to a backend server.

---

## Request Flow

1. Client sends HTTP request
2. Flask proxy receives request
3. Request components are extracted:
   - Path
   - Query parameters
   - Headers
   - Body
4. All components are combined into a single inspection string
5. Regex-based rule engine scans the request
6. Decision is made:
   - Match → Block + Log event
   - No match → Forward to backend server

---

## Components

- Proxy Layer (Flask)
- Rule Engine (Regex-based detection)
- Logging Module (file-based logs)
- Backend Target Server

---

## Design Philosophy

The system uses a unified inspection string approach, allowing all parts of the HTTP request to be analyzed consistently by a single rule engine.
