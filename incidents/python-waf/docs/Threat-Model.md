# Threat Model

## Threat Actors
- Script kiddies using basic payloads
- Automated scanners (sqlmap, curl scripts)
- Manual attackers testing injection flaws

---

## Attack Surface

- URL query parameters
- HTTP headers (User-Agent, Host)
- Request body
- URL path

---

## Threats and Mitigations

### 1. SQL Injection
- Example: `' OR 1=1 --`
- Mitigation: Regex-based pattern detection in request inspection engine

---

### 2. Cross-Site Scripting (XSS)
- Example: `<script>alert(1)</script>`
- Mitigation: Pattern matching for script tags and event handlers

---

### 3. Command Injection
- Example: `&& dir`, `; ls`
- Mitigation: Detection of shell operators in request payload

---

### 4. Path Traversal
- Example: `../../etc/passwd`
- Mitigation: Detection of directory traversal patterns

---

## Limitations

- Regex-based detection can be bypassed with obfuscation or encoding
- No behavioral analysis or anomaly detection
- No rate limiting or IP reputation system
