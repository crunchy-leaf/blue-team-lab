# Response Actions

The following actions were recommended based on the investigation findings:

- Verified that the observed activity originated from the authorized Kali Linux testing system used during the investigation.
- Confirmed that the activity was limited to reconnaissance and that no indicators of compromise were identified beyond network scanning.
- Reviewed exposed services identified during the scan and evaluated whether each service was required for normal operations.
- Identified a monitoring visibility gap in endpoint telemetry for inbound reconnaissance activity.
= Recommended supplementing endpoint monitoring with network-based detection technologies such as firewall logging or a network intrusion detection system.
- Recommended forwarding additional network security logs into Splunk to improve visibility and enable correlation of reconnaissance activity with endpoint events.

# Lessons Learned

This investigation demonstrated the importance of correlating multiple sources of evidence during incident response. While Wireshark provided clear visibility into the network reconnaissance activity, endpoint telemetry alone did not capture the inbound scan. The investigation reinforced that no single monitoring solution provides complete visibility into an environment. Future improvements to the lab include expanding telemetry collection through additional logging sources, improving network visibility, and developing Splunk detections capable of identifying reconnaissance techniques such as rapid TCP connection attempts across multiple destination ports. These enhancements would provide broader detection coverage and improve the ability to identify suspicious activity during future investigations.
