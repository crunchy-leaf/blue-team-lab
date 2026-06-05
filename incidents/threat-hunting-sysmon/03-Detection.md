## Detection

Suspicious activity was identified through analysis of Sysmon telemetry, specifically:

- Event ID 1 (Process Creation): Execution of enumeration and system discovery commands
- Event ID 3 (Network Connection): Evidence of remote authentication sessions and outbound connections
- Repeated authentication failures followed by successful login

Initial indicators included:

- Multiple failed Remote Desktop authentication attempts
- Subsequent successful authentication from same source host
- Execution of system discovery commands immediately post-login
