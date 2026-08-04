from google import genai 
from dotenv import load_dotenv
from pathlib import Path
import os

from ai.prompts import build_prompt


BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / '.env')


client = genai.Client(
    api_key=os.getenv('GEMINI_API_KEY')
)


def generative_analysis(alert):

    prompt = build_prompt(alert)

    try:
        response = client.models.generate_content(
            model='models/gemini-3.1-flash-lite',
            contents=prompt
        )

        return response.text

    except Exception:
        return f'''
AI analysis is temporarily unavailable.

The security detection engine successfully identified this alert.

Manual investigation steps:

• Review the source IP reputation
• Examine the request payload
• Check server logs
• Validate input filtering rules'''