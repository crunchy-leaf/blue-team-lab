## MITRE ATT&CK Mapping

The observed activity is consistent with the reconnaissance phase of the MITRE ATT&CK framework. The packet capture demonstrated an automated TCP Connect scan performed against a Windows 11 workstation to identify accessible network services. No evidence was found indicating that the activity progressed beyond reconnaissance.

| Tactic         | Technique                 | ID    | Justification                                                                                                                          |
| -------------- | ------------------------- | ----- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Reconnaissance | Active Scanning           | T1595 | The scanning host actively probed the target system to identify reachable network services and gather information about exposed ports. |
| Discovery      | Network Service Discovery | T1046 | The TCP Connect scan enumerated services listening on the target host by attempting connections across multiple TCP ports.             |

Although the investigation confirmed reconnaissance activity, no evidence was identified indicating follow-on techniques such as exploitation, credential access, persistence, privilege escalation, or lateral movement. The activity was limited to service enumeration and information gathering.
