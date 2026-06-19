# Environment 
The investigation was condcuted within a virtual environment including a Windows 11 workstation and a Kali Linux attack machine. The Windows system served as the victim while the Kali Linux machine simulated an internal threat actor performing reconnaissance against the network.


### Systems
| System  | Role |
| ------------- | ------------- |
| Windows 11 | Target system
| Kali Linux | Scanning/attacker system


### Tools
| Tool  | Purpose |
| ------------- | ------------- |
| Wireshark  | Captured and analyzed network traffic generated during the investigation.  |
| Nmap | Simulated reconnaissance activity through a TCP Connect (-sT) port scan.  |
| Sysmon | Collected endpoint telemetry from the Windows workstation. |
| Splunk | Aggregated and analyzed Sysmon logs for correlation with network activity. |


### Network Overview
- Source Host: Kali Linux
- Target Host: Windows 11
- Scan Type: TCP Connect Scan (nmap -sT)
- Primary Evidence Source: Wireshark packet capture
- Supporting Evidence: Sysmon endpoint logs and Splunk log searches


### Investigation Scope
The objective of the investigation was to identify the source of the suspicious network activity, determine which services were targeted, reconstruct the sequence of events using available telemetry, and assess whether the activity progressed beyond network reconnaissance.
