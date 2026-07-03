# Project Report: Python WAF

## Summary

This project implements a lightweight Web Application Firewall (WAF) using Python and Flask. The system acts as a reverse proxy that inspects HTTP requests and blocks common web attack patterns using regex-based detection rules.

---

## Objectives

- Understand how WAFs process HTTP traffic
- Build a rule-based detection engine
- Log and analyze malicious requests
- Simulate real-world web attack detection

---

## Implementation

The system processes incoming HTTP requests by extracting key components:
- Path
- Query parameters
- Headers
- Request body

These components are merged into a single inspection string and evaluated against a set of regex-based security rules.

If a match is found, the request is blocked and logged.

---

## Tools & Technologies

- Python
- Flask
- Requests library
- Regex (re module)

---

## Key Features

- Reverse proxy architecture
- Rule-based detection engine
- Multi-vector request inspection
- Attack logging system
- Support for multiple attack types

---

## Security Concepts Demonstrated

- Input validation
- Pattern-based intrusion detection
- HTTP request analysis
- Basic intrusion prevention system design

---

## Future Improvements

- JSON-based rule configuration
- Dashboard for attack monitoring
- Rate limiting and IP blocking
- Advanced encoding detection
- Integration with SIEM tools
- Cookie inspection
