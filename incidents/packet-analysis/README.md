# Objective:
This project demonstrates a network and endpoint investigation using Wireshark, Sysmon, and Splunk to analyze suspicious network activity and reconstruct a unified timeline of events across multiple data sources. The objective is to simulate a real-world SOC investigation where raw network traffic is correlated with endpoint telemetry to determine whether observed behavior is benign or indicative of reconnaissance or compromise.

## Environment:
- Windows 11 (Endpoint under investigation)
- Kali Linux (Attack / scanning simulation host)
- Splunk (Log aggregation and analysis)
- Sysmon (Endpoint telemetry collection)
- Wireshark (Packet capture and network analysis)

## Scenario:
During routine network monitoring, unusual TCP connection attempts were identified in Wireshark originating from an internal host. The traffic consisted of rapid, repeated connection attempts targeting multiple ports on a Windows workstation within a short time window.

This behavior deviated from normal baseline activity and is consistent with potential reconnaissance activity such as port scanning.

An investigation was initiated to determine the source of the traffic, identify targeted services, and assess whether any additional malicious activity occurred on the endpoint.

---

**This investigation aims to answer the following questions:**

- What system generated the suspicious traffic?
- What was the purpose of the observed activity?
- Is there evidence of compromise beyond the initial network activity?
- What response actions, if any, are required?
