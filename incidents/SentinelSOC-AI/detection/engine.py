from detection.rules import detect_sqli, detect_command_injection
import uuid

def analyze_logs(events):
    alerts = []

    for event in events:

        endpoint = event['endpoint']

        if detect_sqli(endpoint):

            alerts.append({
                'id': str(uuid.uuid4()),
                'type': 'SQL Injection',
                'severity': 'High',
                'source_ip': event['ip'],
                'endpoint': endpoint,
                'timestamp': event['timestamp'],
                'event': event
            })

        if detect_command_injection(endpoint):
            alerts.append({
                'id': str(uuid.uuid4()),
                'type': 'Command Injection',
                'severity': 'High',
                'source_ip': event['ip'],
                'endpoint': endpoint,
                'timestamp': event['timestamp'],
                'event': event
            })

    return alerts