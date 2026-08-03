# Each blocked request is logged with:

- Timestamp
- Source IP
- HTTP method
- Path
- Inspection data
- Triggered rule
- Severity
- Action taken

## Example log entry:

```
================LOG START=================
Timestamp: 2026-07-03 12:24:00
IP: 192.168.56.3
Method: GET
Path: 
Inspection Info: SELECT  127.0.0.1:8080  
Rule Name: SQL Injection
Severity: high
Action: BLOCK
==================LOG END=================
```
