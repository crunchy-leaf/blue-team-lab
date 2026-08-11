# Blue Team Lab & Detection Projects

This repository documents my cybersecurity projects focused on **security monitoring, detection engineering, incident response, web application security, and defensive automation**.

The goal of this portfolio is to simulate real-world security operations by generating attacks in controlled environments, analyzing security telemetry, developing detection logic, and documenting investigations using industry-standard security concepts and tools.

---

# Projects

## [AI SOC Analyst Platform](./incidents/SentinelSOC-AI)

A security operations automation project that analyzes logs, detects suspicious activity, and uses AI-assisted analysis to generate SOC-style investigation summaries.

The platform simulates a SOC analyst workflow by:

- Ingesting security logs
- Parsing events and extracting indicators
- Applying detection rules
- Generating alerts
- Providing AI-assisted investigation summaries

### Features

- Flask-based web application
- Automated log analysis
- Detection rule engine
- Alert generation
- AI-assisted incident analysis
- MITRE ATT&CK technique mapping
- SOC investigation workflow simulation

### AI Analysis Output

The AI analysis provides:

- Executive Summary
- Technical Explanation
- Threat Classification
- MITRE ATT&CK Mapping
- Risk Assessment
- Recommended Response Actions

---

## [AI-Enhanced Web Application Firewall (WAF)](./incidents/ai-python-waf)

An enhanced version of my custom Python Web Application Firewall that adds AI-assisted security analysis to improve threat classification and investigation.

The original WAF was developed as a Flask-based reverse proxy that inspected incoming HTTP requests and blocked malicious traffic using custom detection rules. The project was expanded by integrating AI capabilities to provide additional context and analysis for detected attacks.

### Architecture

The WAF follows a layered detection approach:

1. Incoming HTTP request
2. Request normalization and inspection
3. Rule-based detection engine
4. Attack classification
5. AI-assisted security analysis
6. Logging and alert generation

### Detection Capabilities

The WAF inspects:

- URL paths
- Query parameters
- HTTP headers
- Request bodies

Detected attack categories include:

- SQL Injection
- Command Injection
- Cross-Site Scripting (XSS)
- Path Traversal

### AI Enhancement

The AI component assists with:

- Explaining detected attack behavior
- Providing security context
- Classifying severity
- Generating analyst-style recommendations
- Supporting investigation workflows

### Features

- Flask reverse proxy architecture
- Custom regex-based detection rules
- Multi-vector HTTP request inspection
- Automated malicious request blocking
- Structured security logging
- AI-assisted alert analysis

### Example Detections

The WAF has been tested against simulated attacks including:

- SQL injection payloads
- Command injection attempts
- XSS payloads
- Path traversal attempts

Screenshots and test cases are included demonstrating blocked requests and AI-generated analysis.

---

# Python IOC Detection Tool

A Python-based security automation script that identifies potentially malicious network activity by comparing connection logs against known Indicators of Compromise (IOCs).

### Features

- Network log parsing
- IOC matching
- Automated detection results
- Security-focused Python scripting

---

# SOC Investigation Project

A simulated blue team investigation analyzing Windows security events and network activity following attacker reconnaissance.

### Investigation Documentation Includes

- Executive Summary
- Environment Overview
- Detection Analysis
- Timeline of Events
- Evidence Collection
- MITRE ATT&CK Mapping
- Incident Impact Assessment
- Response Recommendations
- Lessons Learned

---

# Splunk Detection Lab

Configured Splunk Enterprise to ingest Windows telemetry and create security monitoring searches.

### Detection Use Cases

- Failed logons (Event ID 4625)
- Successful authentication events (Event ID 4624)
- Account lockouts
- Privilege changes
- Process creation monitoring
- Network reconnaissance activity

### Skills Practiced

- SIEM monitoring
- Log analysis
- Detection engineering
- Threat hunting
- Incident investigation

---

# Lab Environment

## Infrastructure

- Windows Server 2019 (Active Directory Domain Controller)
- Windows 10 Client
- Kali Linux Attack Machine

## Security Tools

- Splunk Enterprise
- Sysmon
- Windows Event Viewer
- Nmap
- Wireshark
- Python
- Advanced Windows Audit Policies

---

# Skills Demonstrated

- Active Directory security
- Windows Event Log analysis
- SIEM monitoring
- Detection engineering
- Threat hunting
- Incident response documentation
- Python security automation
- IOC detection
- Authentication monitoring
- Network traffic analysis
- MITRE ATT&CK mapping
- Web application security
- WAF rule development

---

# Evidence & Documentation

Each project includes supporting artifacts demonstrating implementation and analysis.

Examples include:

- Screenshots of detections
- Attack simulations
- Splunk queries
- Event logs
- Network captures
- Investigation reports
- Detection logic documentation
- Test cases

---

# Future Enhancements

Planned additions:

- Brute-force detection
- Pass-the-Hash investigations
- Kerberoasting detection
- PowerShell attack detection
- Lateral movement analysis
- Sigma rule development
- Custom Splunk dashboards
- Additional threat hunting scenarios
- Expanded AI-assisted SOC capabilities

---

# Disclaimer

All activities in this repository were performed in isolated lab environments created for educational purposes.

No testing was conducted against systems without authorization.
---

