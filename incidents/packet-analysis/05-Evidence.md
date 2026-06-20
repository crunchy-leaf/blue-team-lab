# Evidence

## Evidence 1 - Wireshark Packet Capture

Packet capture analysis confirmed that the source host initiated TCP connection attempts across a large number of destination ports on the Windows workstation. The communication pattern consisted of repeated TCP connection attempts occurring within a short period of time, consistent with automated reconnaissance activity.

**Evidence:**

![Network scan evidence](../../images/packet-analysis/network-scan-evidence.png)

**Display filter:**
- tcp.flags.syn == 1 && tcp.flags.ack == 0

**Highlight:**
- Source IP
- Destination IP
- Destination ports
- TCP SYN packets

---

## Evidence 2 - TCP Conversation Analysis

Inspection of an individual TCP stream demonstrated the complete TCP three-way handshake associated with an Nmap TCP Connect scan. Successful connections completed the handshake before being immediately terminated by the scanning host, behavior characteristic of TCP Connect scanning.

**Evidence:**

![Network scan evidence](../../images/packet-analysis/full-tcp-conversation.png)

**Highlight:**
- SYN
- SYN/ACK
- ACK
- RST (or connection termination)

---

## Evidence 3 - Connection Statistics

Wireshark conversation statistics summarized the communication between the source and destination hosts, confirming that a single internal system generated a high volume of TCP connections during the investigation period.

**Evidence:**

![Network scan evidence](../../images/packet-analysis/statistics.png)

**Highlight:**
- Source host
- Destination host
- Packet counts
- Bytes transferred

---

## Key Findings
| Finding                | Result                        |
| ---------------------- | ----------------------------- |
| Attack Source          | Kali Linux                    |
| Target                 | Windows 11 Workstation        |
| Attack Type            | TCP Connect Scan (`nmap -sT`) |
| Primary Evidence       | Wireshark Packet Capture      |
| Endpoint Detection     | No Sysmon Event ID 3 logged   |
| Assessment             | Reconnaissance Activity       |
| Evidence of Compromise | None Observed                 |
