# AI-Enhanced Web Application Firewall (WAF)

## Overview

This project is a Python-based Web Application Firewall (WAF) built as a reverse proxy to inspect HTTP requests before they reach a protected web application. The firewall uses traditional rule-based detection to identify common web attacks and integrates Google's Gemini API to provide contextual AI analysis of suspicious requests.

Unlike AI-only security tools, this implementation uses a layered approach:

* Local detection rules quickly identify potentially malicious traffic.
* Only suspicious requests are sent to Gemini for additional analysis.
* Gemini evaluates the request and returns a structured security assessment.
* Malicious requests are blocked while legitimate traffic is forwarded to the protected application.

This approach minimizes unnecessary AI requests while demonstrating how traditional security controls and AI can work together.

---

## Features

* Reverse proxy Web Application Firewall built with Flask
* Rule-based detection engine
* SQL Injection detection
* Cross-Site Scripting (XSS) detection
* Command Injection detection
* Path Traversal detection
* AI-assisted request analysis using Google Gemini
* Structured AI decisions (BLOCK / ALLOW)
* Detailed security event logging
* Protected backend web application simulation

---

## Architecture

```
                    Incoming HTTP Request
                             │
                             ▼
                   Reverse Proxy (Flask WAF)
                             │
                             ▼
                  Rule-Based Detection Engine
                             │
               ┌─────────────┴─────────────┐
               │                           │
         No Match                     Rule Match
               │                           │
               ▼                           ▼
     Forward to Application      Send Alert to Gemini
               │                           │
               ▼                           ▼
     Protected Flask App         AI Security Analysis
                                             │
                                             ▼
                                  BLOCK or ALLOW Decision
                                             │
                         ┌───────────────────┴───────────────────┐
                         │                                       │
                      BLOCK                                 Forward
                         │                                       │
                         ▼                                       ▼
                   Log Security Event                Protected Application
```

---

## Technologies Used

* Python
* Flask
* Requests
* Regular Expressions (Regex)
* Google Gemini API
* python-dotenv

---

## Project Structure

```
python-waf/
│
├── app/
│   ├── main.py
│   ├── proxy.py
│   ├── rules.py
│   ├── logger.py
│   └── ai_engine.py
│
├── logs/
│
├── requirements.txt
│
└── README.md
```

---

## Detection Workflow

1. An incoming HTTP request is received by the reverse proxy.
2. The request is inspected using locally defined security rules.
3. If no rule matches, the request is immediately forwarded to the protected application.
4. If a rule matches, only that suspicious request is sent to Gemini.
5. Gemini analyzes the request using the matched rule, request metadata, and payload.
6. Gemini returns a structured JSON response containing:

   * Decision (BLOCK or ALLOW)
   * Risk level
   * Explanation
7. Malicious requests are blocked and logged.

---

## Example AI Response

```json
{
    "decision": "BLOCK",
    "risk": "HIGH",
    "reason": "The request contains SQL injection syntax intended to bypass authentication."
}
```

---

## Example Attack

```
http://127.0.0.1:8080/?username=' OR 1=1 --
```

Detection Flow:

```
SQL Injection Rule
        │
        ▼
Gemini Analysis
        │
        ▼
Decision: BLOCK
        │
        ▼
403 Forbidden
```

---

## Logging

Blocked requests are recorded with:

* Timestamp
* Source IP
* HTTP Method
* Request Path
* Request Data
* Detection Rule
* Severity
* AI Analysis
* AI Decision

---

## Environment Variables

Create a `.env` file inside the project directory.

```
GEMINI_API_KEY=your_api_key_here
```

The project uses `python-dotenv` to securely load the API key at runtime.

---

## Installation

Clone the repository.

```
git clone https://github.com/crunchy-leaf/ai-python-waf.git
```

Navigate into the project.

```
cd ai-python-waf
```

Install dependencies.

```
pip install -r requirements.txt
```

Create a `.env` file containing your Gemini API key.

Start the protected web application.

```
python app/main.py
```

In another terminal, start the WAF.

```
python app/proxy.py
```

Open your browser and navigate to:

```
http://127.0.0.1:8080
```

---

## Future Improvements

* Support all HTTP methods
* Machine learning-assisted anomaly detection
* IP reputation integration
* Rate limiting
* Configurable rule management
* Threat intelligence feeds
* Detection confidence scoring
* Administrative dashboard

---

## Lessons Learned

Building this project reinforced several important cybersecurity concepts:

* Reverse proxy architecture
* HTTP request inspection
* Regex-based detection engineering
* Balancing detection accuracy with false positives
* Integrating AI into traditional security workflows
* Secure API key management using environment variables
* Logging and documenting security events

One of the biggest challenges was reducing false positives. During testing, overly broad command injection rules incorrectly flagged legitimate browser requests. Refining the detection logic improved accuracy while maintaining effective coverage, demonstrating the importance of tuning defensive security tools.

---

## Disclaimer

This project was built for educational purposes to demonstrate defensive security concepts, reverse proxy design, and AI-assisted threat analysis. It is not intended to replace production-grade Web Application Firewalls.

