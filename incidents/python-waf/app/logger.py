from pathlib import Path

log_file = Path(__file__).parent.parent / 'logs' / 'waf.LOG'

def log_event(timestamp, ip, method, path, parameters, rule):
   
    with open(log_file, 'a') as logger:
        logger.write('================LOG START=================\n')
        logger.write(f'Timestamp: {timestamp}\n')
        logger.write(f'IP: {ip}\n')
        logger.write(f'Method: {method}\n')
        logger.write(f'Path: {path}\n')
        logger.write(f'Inspection Info: {parameters}\n')
        logger.write(f"Rule Name: {rule['name']}\n")
        logger.write(f"Severity: {rule['severity']}\n")
        logger.write(f"Action: {rule['action']}\n")
        logger.write('==================LOG END=================\n')