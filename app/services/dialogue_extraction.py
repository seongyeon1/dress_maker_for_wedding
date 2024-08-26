# services/dialogue_extraction.py

from openai import OpenAI
import os
from dotenv import load_dotenv

from ..templates.template import system_prompt

load_dotenv()

UPSTAGE_API_KEY = os.getenv('UPSTAGE_API_KEY')

client = OpenAI(
    api_key=UPSTAGE_API_KEY,
    base_url="https://api.upstage.ai/v1/solar"
)


def extract_dress_info(dialogue):
    response = client.chat.completions.create(
        model="solar-1-mini-chat",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": dialogue},
        ],
        stream=False,
    )
    result = response.choices[0].message.content
    return result