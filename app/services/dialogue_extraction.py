# services/dialogue_extraction.py

from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

UPSTAGE_API_KEY = os.getenv('UPSTAGE_API_KEY')

client = OpenAI(
    api_key=UPSTAGE_API_KEY,
    base_url="https://api.upstage.ai/v1/solar"
)

from templates import system_prompt

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

def translate_dialogue(prompt):
    response = client.chat.completions.create(
        model="solar-1-mini-translate-koen",
        messages=[
            {"role": "user", "content": prompt}
        ],
        stream=False,
    )
    result = response.choices[0].message.content
    return result