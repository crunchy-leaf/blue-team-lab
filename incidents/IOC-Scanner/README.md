# IOC Scanner (Python)

## Overview
This project is a simple IOC (Indicator of Compromise) scanner built in Python.  
It compares known malicious IP addresses against network log data to identify potential threats.

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
