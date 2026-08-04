def build_prompt(alert):

    return f'''
You are an experienced SOC analyst.

Analyze the following security alert.

Attack Type:
{alert['type']}

Severity:
{alert['severity']}

Source IP:
{alert['source_ip']}

Endpoint:
{alert['endpoint']}

Timestamp:
{alert['timestamp']}

Parsed Event:
{alert['event']}

Provide:

1. Executive Summary
2. Technical Explanation
3. MITRE ATT&CK Technique (if applicable)
4. Risk Assessment
5. Recommended Response

Keep the explanation professional and concise.
'''