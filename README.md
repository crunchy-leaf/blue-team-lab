# Blue Team Lab & Detection Projects

This repository documents my cybersecurity home lab and blue team projects and web application security (WAF development) focused on threat detection, log analysis, incident response, and Active Directory security.

The purpose of this repository is to simulate realistic attacker activity, investigate security events, develop detection logic, and document investigations using industry-standard defensive tools.

---

# Lab Environment

## Infrastructure
- Windows Server 2019 (Active Directory Domain Controller)
- Windows 10 Client
- Kali Linux (Attack Machine)

## Security Tools
- Splunk Enterprise
- Sysmon
- Windows Event Viewer
- Nmap
- Wireshark
- Python
- Advanced Windows Audit Policies

---

## Skills Demonstrated

- Active Directory administration
- Windows Event Log analysis
- Splunk log ingestion and searching
- Detection engineering
- Threat hunting
- Incident response documentation
- Python scripting for security automation
- Log parsing and IOC detection
- Authentication monitoring
- Network traffic analysis
- MITRE ATT&CK mapping
- Security investigation workflow
- Web application security and WAF rule development

---

# Repository Projects

## Python Web Application Firewall (WAF)

A custom-built Web Application Firewall implemented in Python using Flask. This project functions as a reverse proxy that inspects incoming HTTP requests and blocks malicious traffic based on regex-based detection rules.

The WAF analyzes multiple components of each request including:
- URL path
- Query parameters
- HTTP headers
- Request body

All inputs are normalized into a single inspection string and evaluated against a customizable rule engine.

### Features
- Reverse proxy architecture
- Regex-based detection engine
- Multi-vector request inspection
- Blocking of common web attacks
- Structured logging of malicious requests

### Detected Attack Types
- SQL Injection
- Cross-Site Scripting (XSS)
- Command Injection
- Path Traversal

### Key Learning Outcomes
- HTTP request lifecycle understanding
- Web security fundamentals
- Pattern-based intrusion detection
- Defensive security engineering

## Python IOC Detection Tool

Developed a Python script to automate the detection of known malicious IP addresses by comparing network connection logs against a list of Indicators of Compromise (IOCs).

Features include:

- Parses network log files
- Compares IP addresses against known malicious IOCs
- Generates detection results
- Demonstrates basic security automation using Python

---

## SOC Investigation Project

Performed a simulated blue team investigation by analyzing Windows Security Logs and network activity after a reconnaissance attack.

Project includes:

- Executive Summary
- Environment Overview
- Detection Analysis
- Timeline of Events
- Evidence Collection
- MITRE ATT&CK Mapping
- Incident Impact Assessment
- Response Actions
- Lessons Learned

---

## Splunk Detection Lab

Configured Splunk Enterprise to ingest Windows Event Logs and build searches for security monitoring.

Detection examples include:

- Failed logons (Event ID 4625)
- Successful logons (4624)
- Account lockouts
- Privilege changes
- Process creation events
- Network reconnaissance

---

# Learning Objectives

- Improve SOC analyst skills
- Practice incident investigation
- Develop defensive detection logic
- Strengthen Active Directory knowledge
- Build a professional cybersecurity portfolio

---

# Evidence & Artifacts

Each project contains supporting documentation such as:

- Screenshots
- Splunk search queries
- Event logs
- Network captures
- Investigation reports
- Timelines
- Detection logic

---

# Future Enhancements

Planned additions include:

- Brute-force attack detection
- Pass-the-Hash detection
- Kerberoasting detection
- PowerShell attack detection
- Lateral movement investigations
- Sigma rule development
- Custom Splunk dashboards
- Additional threat hunting scenarios

---

# Disclaimer

All activities in this repository were performed in an isolated lab environment created for educational purposes. No testing was conducted against systems without authorization.
