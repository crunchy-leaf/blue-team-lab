from google import genai
from dotenv import load_dotenv
import json
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv('Gemini_API_KEY')
)


def analyze_request(alert):
    prompt = f'''
You are an AI Web Application Firewall analyzing a suspicious request.

Review this alert:

{alert}

Determine if this request is malicious.

Respond ONLY with valid JSON:

{{
    "decision": "BLOCK or ALLOW",
    "risk": "LOW, MEDIUM, or HIGH",
    "reason": "Explain why"
}}
'''

    response = client.models.generate_content(
        model='models/gemini-3.1-flash-lite',
        contents=prompt
    )

    try:
        return json.loads(response.text)
    except json.JSONDecodeError:
        return {
        'decision': 'BLOCK',
        'risk': 'HIGH',
        'reason': 'Gemini returned an invalid response.'
    }