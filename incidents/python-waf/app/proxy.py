from flask import Flask, request
import requests
from logger import log_event
from rules import rules
from datetime import datetime
import re

timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

app = Flask(__name__)

Target = 'http://127.0.0.1:5000'

def is_malicious(text):
    waf_rules = rules

    for rule in waf_rules:
        for pattern in rule['patterns']:
            if re.search(pattern, text, re.IGNORECASE):
                return rule
    
    return None
        

@app.route('/', defaults = {'path': ''})
@app.route('/<path:path>')

def proxy(path):
    query_text = ' '.join(request.args.values())
    path_text = path
    host_text = request.headers.get('Host', '')
    user_agent_text = request.headers.get('User-Agent', '')
    body_text = request.get_data(as_text=True)

    inspection_text = ' '.join([
        query_text,path_text,
        host_text, 
        user_agent_text,
        body_text
    ])

    
    matched_rule = is_malicious(inspection_text)

    if matched_rule:
        log_event(timestamp, request.remote_addr,
                  request.method, path,
                  inspection_text, matched_rule)
        return 'Blocked by WAF', 403
    
    url = f'{Target}/{path}'

    print('=== New Request ===')
    print(f'Method: {request.method}')
    print(f'Path: /{path}')
    print(f'URL: {url}')
    print(f'Parameters: {request.args}')
    
    args = request.args

    for key, value in args.items():
        print(f'{key} = {value}')


    resp = requests.get(url)

    return resp.content, resp.status_code


       

if __name__ == '__main__':
    app.run(port = 8080, debug = True)