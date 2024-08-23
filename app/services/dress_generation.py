# services/dress_generation.py

import fal_client
import os
from dotenv import load_dotenv

load_dotenv()

os.environ['FAL_KEY'] = os.getenv('FAL_KEY')

def generate_dress(prompt):
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