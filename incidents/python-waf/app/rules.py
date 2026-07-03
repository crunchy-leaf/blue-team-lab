rules = [
    {
        "id": "sqli_001",
        "name": "SQL Injection",
        "severity": "high",
        "patterns": [
            r"select\b",
            r"drop\b",
            r"--",
            r"or\s+['\"]?\s*\w+\s*['\"]?\s*=\s*['\"]?\s*\w+",
            r"union\s+select"
        ],
        "action": "BLOCK"
    },

    {
        "id": "xss_001",
        "name": "Cross Site Scripting",
        "severity": "medium",
        "patterns": [
            r"<\s*script\s*>",
            r"javascript\s*:",
            r"onerror\s*=",
            r"onload\s*="
        ],
        "action": "BLOCK"
    },

    {
        "id": "cmd_001",
        "name": "Command Injection",
        "severity": "high",
        "patterns": [
            r";\s*ls\b",
            r"\|\s*whoami\b",
            r"`",
            r"&&\s*\w+",
            r"\|\s*\w+",
            r";\s*\w+",
            r"(&&|\|\|)\s*\w+",
            r"[;&|]\s*\w+"
        ],
        "action": "BLOCK"
    },

    {
        "id": "path_001",
        "name": "Path Traversal",
        "severity": "high",
        "patterns": [
            r"\.\./",
            r"\.\.\\",
            r"/etc/passwd",
            r"c:\\windows"
        ],
        "action": "BLOCK"
    }
]