# Overview:
This project was made to demonstrate how to build an endppoint monitoring dashboard using Splunk and Sysmon. The goal was to transform raw Windows event logs into meaningful security visibility.

## Environment:
- Windows 11 (Host machine)
- Sysmon (endpoint telemetry)
- Splunk Enterprise
- Local lab environment

## Data Sources:
**Sysmon**

Provides endpoint visibility including:
- Process creation
- Network connections
- File and registry activity

**Windows Security Logs**

Provides authenication visibility:
- Successful logins
- Failed logins

## Dashboard Design Philosophy:
The dashboard was desgined to reflect a SOC analyst workflow:
1. Authentication monitoring
2. Endpoint process visibility
3. Network activity tracking
4. Investigative drill-down

Each panel was made to represent a different layer of endpoint security.

## Dashboard Panels & Queries:
**Authentication Activity:**

index=endpoint (EventCode=4624 OR EventCode=4625)                                                                                                                   
| stats count by EventCode

**Why this?** It detects success/failure patterns and brute force attempts.

---

**Top Processes:**

index=endpoint EventCode=1                                                                                                                                              
| stats count by Image                                                                                                                                                  
| sort -count

**Why this?** It identifies executed processes and potential malicious binaries.

---

**Network Connections:**

index=endpoint EventCode=3                                                                                                                                                  
| stats count by DestinationIp                                                                                                                                            
| sort -count

**Why this?** It can show outboud connections and potential suspicious traffic.

---

**System Activity Timeline:**

index=endpoint                                                                                                                                                            
| timechart count

**Why this?** It highlights spikes in system behavior over time. 

---

**Event Detail View:**

index=endpoint                                                                                                                                                       
| table _time EventCode Image CommandLine User DestinationIp

**Why this?** This provides a raw investigative context for analysis.

---

## Screenshots:
To be added



