## Detection

Suspicious activity was identified through Sysmon Event ID 1 (Process Creation Events), which logs process execution along with command-line arguments and parent-child relationships.

The following types of activity were analyzed:

- Command-line execution (cmd.exe)
- System enumeration commands (whoami, ipconfig, hostname)
- PowerShell activity
