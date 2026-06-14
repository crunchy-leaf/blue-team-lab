# Objective:
The goal of this project is to use the packet catpure program Wireshark to analyze traffic on a network for suspicious activity, and then correlating that data with what I can find in Sysmon/Splunk to try and piece together a full comprehensive timeline of events.

## Environment:
- Windows 11
- Kali Linux 
- Splunk
- Sysmon
- Wireshark

## Scenario:
While performing routine network monitoring, unusual TCP connection activity was observed in Wireshark originating from a host on the internal network. The traffic consisted of repeated connection attempts to multiple ports on a Windows workstation over a short period of time.

Because this pattern differed from normal user activity and could indicate reconnaissance or unauthorized network scanning, an investigation was initiated to determine the nature of the traffic, identify the source host, and assess the potential impact to the environment.

The investigation leveraged packet captures from Wireshark, endpoint telemetry collected by Sysmon, and centralized logs in Splunk. Evidence from these sources was analyzed to establish a timeline of events, identify affected systems, and determine whether the activity represented malicious behavior or legitimate network operations.

---

**This investigation aims to answer the following questions:**

- What system generated the suspicious traffic?
- What services or ports were targeted?
- What was the purpose of the observed activity?
- Is there evidence of compromise beyond the initial network activity?
- What response actions, if any, are required?
