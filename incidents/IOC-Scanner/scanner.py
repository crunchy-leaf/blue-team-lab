def read_ioc():
    with open('iocs.txt', 'r') as ioc_file:
        ioc_list = []
        
        for ip in ioc_file:
            ip = ip.strip()
            ioc_list.append(ip)
    
    return ioc_list

def read_log():
    with open('logs.txt', 'r') as log_file:
        log_list = []

        for log in log_file:
            log = log.strip()
            log_list.append(log)
        
    return log_list

def find_matches(iocs, logs):
    matches =[]

    for ip in logs:
        if ip in iocs:
            matches.append(ip)
    
    return matches

iocs = read_ioc()
logs = read_log()

matches = find_matches(iocs, logs)

print('=== IOC Matches ===')

for ip in matches:
    print(f'Alert: {ip}')

print(f'Total Matches Found: {len(matches)}')
