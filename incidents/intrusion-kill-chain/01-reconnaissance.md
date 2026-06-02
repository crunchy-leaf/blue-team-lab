# Reconnaissance

## Objective

Identify exposed services on the target host.

## Attacker Activity

The attacker gained entry to the network and did a targeted port scan of a Windows server. 

![Nmap Scan](../../images/intrusion-kill-chain/nmap-service-scan.png)

Key Findings:

- Nmap service detection identified multiple services associated with Microsoft Active Directory. Open ports included DNS (53), Kerberos (88), LDAP (389), SMB (445), Global Catalog LDAP (3268), RDP (3389), and WinRM (5985).
- Service banners revealed the domain name lab.local, indicating that the target is functioning as a Windows Active Directory Domain Controller.
- The presence of SMB, LDAP, and Kerberos provides several opportunities for further enumeration of users, groups, shares, and authentication mechanisms.

## Defender Activity:

No direct evidence that the reconnaissance activity was observed in the default Windows security logs. This demonstrates a visibility gap that could addressed through enhanced logging solutions such as Sysmon.
