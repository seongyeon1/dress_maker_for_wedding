# services/dress_generation.py
from openai import OpenAI
import os
from dotenv import load_dotenv

import fal_client
import os
from dotenv import load_dotenv

load_dotenv()

from .templates.template import image_prompt

os.environ['FAL_KEY'] = os.getenv('FAL_KEY')
UPSTAGE_API_KEY = os.getenv('UPSTAGE_API_KEY')

client = OpenAI(
    api_key=UPSTAGE_API_KEY,
    base_url="https://api.upstage.ai/v1/solar"
)

def make_prompt(dialogue):
    response = client.chat.completions.create(
        model="solar-1-mini-chat",
        messages=[
            {"role": "system", "content": image_prompt},
            {"role": "user", "content": dialogue},
        ],
        stream=False,
    )
    result = response.choices[0].message.content
    return result

def generate_dress(dialogue):
    prompt = make_prompt(dialogue)
    handler = fal_client.submit(
        "fal-ai/flux/dev",
        arguments={
            "prompt": prompt,
            "image_size": "landscape_4_3",
            "num_inference_steps": 28,
            "guidance_scale": 3.5,
            "num_images": 1,
            "enable_safety_checker": True,
        },
    )
    result = handler.get()
    return result