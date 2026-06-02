# Incident timeline

## Objective

This section reconstructs the full attack sequence from reconnaissance through privilege escalation, correlating attacker activity with Windows Security event logs.

---

## Timeline of Events

| Time | Phase | Attacker Activity | Defender Evidence |
|------|-------|------------------|-------------------|
| 09:00 | Reconnaissance | Nmap scan of target host | No direct log visibility |
| 09:06 | Initial Access | Failed RDP login attempts | Event ID 4625 observed |
| 09:07 | Initial Access | Successful authentication | No direct log observed |
| 09:08 | Execution | System commands executed | Process activity observed |
| 09:11 | Persistence | Local account created | Event ID 4720 observed |
| 09:12 | Privilege Escalation | Added to Administrators group | Not observed / missing audit logs |

## Detailed Summary of Findings

This investigation simulated a full end-to-end intrusion scenario against a Windows Server 2019 environment using a Kali Linux attack system. The exercise followed a complete attack lifecycle, including reconnaissance, authentication attempts, successful access, persistence, and privilege escalation.

The attacker began by identifying exposed network services through port scanning, revealing potential entry points such as RDP and SMB. Following reconnaissance, multiple authentication attempts were made against the target system, resulting in both failed and successful logins. These activities were confirmed through Windows Security Event Logs, specifically Event ID 4625 (failed logon) and Event ID 4624 (successful logon).

After gaining access, a new local user account was created on the system to simulate persistence. This activity was confirmed through Event ID 4720, indicating account creation. The account was then added to the local Administrators group to simulate privilege escalation; however, corresponding group membership modification events were not observed, indicating a gap in audit logging configuration.

From a defensive perspective, Windows Event Viewer provided partial visibility into the attack chain. Authentication and account creation events were successfully captured, but visibility into privilege escalation activity was limited due to missing or disabled auditing policies for group membership changes.

Overall, this exercise demonstrated how attackers progress through a structured kill chain and how defenders can reconstruct those actions using available telemetry. It also highlighted the importance of comprehensive logging configuration to ensure full detection coverage across all stages of an intrusion.
