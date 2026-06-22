# IOC Scanner (Python)

## Overview
This project is a simple IOC (Indicator of Compromise) scanner built in Python.  
It compares known malicious IP addresses against network log data to identify potential threats.

## Scenario

A Security Operations Center (SOC) receives a threat intelligence feed containing known malicious IP addresses associated with recent malicious activity. At the same time, network monitoring tools generate logs of IP addresses that have communicated with systems on the organization's network.

The objective of this project is to automate the initial triage process by comparing observed network activity against the threat intelligence feed. If a match is found, the script reports the malicious IP address as a potential Indicator of Compromise (IOC) that requires further investigation.

**This project demonstrates a foundational detection workflow commonly performed by SOC analysts:**

- Ingest threat intelligence (IOCs)
- Parse network log data
- Correlate observed activity against known malicious indicators
- Generate alerts for matching IP addresses
- Provide a summary of detection results


## How it works
- Reads a list of known malicious IPs from `iocs.txt`
- Reads simulated network logs from `logs.txt`
- Compares both datasets
- Prints matching IPs and total number of detections

## Features
- File-based IOC ingestion
- Log parsing
- Simple correlation engine
- Clean CLI output

## Example Output
=== IOC Scanner Report ===

IOC Match Found: 8.8.8.8  
IOC Match Found: 45.33.32.156  

Total Matches: 2

## Purpose
Built as a beginner cybersecurity project to practice Python scripting, log analysis, and IOC correlation techniques used in SOC environments.
