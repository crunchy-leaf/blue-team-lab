import re

SQLI_PATTERNS = [
    r'union',
    r'select',
    r'or\s+1=1',
    r'--',
    r'drop',
    r'insert',
    r'delete'
]

CMD_PATTERNS = [
    r';',
    r'\|\|',
    r'&&',
    r'wget',
    r'curl',
    r'powershell',
    r'cmd\.exe'
]


def detect_sqli(endpoint):

    endpoint = endpoint.lower()

    for pattern in SQLI_PATTERNS:
        if re.search(pattern, endpoint):
            return True

    return False

def detect_command_injection(endpoint):

    endpoint = endpoint.lower()

    for pattern in CMD_PATTERNS:
        if re.search(pattern, endpoint):
            return True

    return False
