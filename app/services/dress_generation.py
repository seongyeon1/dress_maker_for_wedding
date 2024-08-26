# services/dress_generation.py
from langchain import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

import fal_client
import os
from dotenv import load_dotenv

from ..templates.template import image_prompt as img_maker_prompt

load_dotenv()

os.environ['FAL_KEY'] = os.getenv('FAL_KEY')

def make_prompt(dialogue):
    template = img_maker_prompt
    prompt_template = PromptTemplate(input_variables=["dialogue"], template=template)
    chain = LLMChain(prompt=prompt_template, llm=OpenAI(model="solar-1-mini-chat"))
    response = chain.run(dialogue=dialogue)
    return response

# def generate_dress(prompt):
#     handler = fal_client.submit(
#         "fal-ai/flux/dev",
#         arguments={
#             "prompt": prompt,
#             "image_size": "landscape_4_3",
#             "num_inference_steps": 28,
#             "guidance_scale": 3.5,
#             "num_images": 1,
#             "enable_safety_checker": True,
#         },
#     )
#     result = handler.get()
#     return result

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