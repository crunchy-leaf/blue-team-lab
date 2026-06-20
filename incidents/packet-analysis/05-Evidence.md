# Evidence

## Evidence 1 - Wireshark Packet Capture

Packet capture analysis confirmed that the source host initiated TCP connection attempts across a large number of destination ports on the Windows workstation. The communication pattern consisted of repeated TCP connection attempts occurring within a short period of time, consistent with automated reconnaissance activity.

**Evidence:**



Display filter:

tcp.flags.syn == 1 && tcp.flags.ack == 0
Highlight:
Source IP
Destination IP
Destination ports
TCP SYN packets
