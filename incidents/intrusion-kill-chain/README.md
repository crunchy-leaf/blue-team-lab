# End-to-End Intrusion Investigation

## Objective

This project simulates a multi-stage attack against a Windows Server 2019 system and documents the investigation from a blue team perspective.

## Attack Flow

- [Reconnaissance](01-reconnaissance.md)
- [Initial Access](02-initial-access.md)
- [Execution](03-execution.md)
- [Persistence](04-persistence.md)
- [Privilege Escalation](05-privilege-escalation.md)
- [Incident Timeline](06-incident-timeline.md)

## MITRE ATT&CK Techniques

The following MITRE ATT&CK techniques were observed or simulated during this investigation:

- **Reconnaissance (T1595 - Active Scanning)**  
  The attacker performed network scanning to identify open ports and services on the target system using Nmap.

- **Valid Accounts (T1078)**  
  Successful authentication was achieved using valid credentials after multiple failed login attempts.

- **Brute Force (T1110)**  
  Multiple failed authentication attempts were generated against a target user account prior to successful access.

- **Create Account (T1136.001 - Local Account)**  
  A new local user account was created on the system to simulate persistence.

- **Account Manipulation (T1098)**  
  The newly created account was added to the local Administrators group to simulate privilege escalation.

## Notes

Some advanced persistence and privilege escalation techniques were not fully observable due to limited auditing configuration within the lab environment.
