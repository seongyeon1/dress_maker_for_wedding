# services/dialogue_extraction.py
from langchain import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

UPSTAGE_API_KEY = os.getenv('UPSTAGE_API_KEY')

client = OpenAI(
    api_key=UPSTAGE_API_KEY,
    base_url="https://api.upstage.ai/v1/solar"
)

from templates import *

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


def make_prompt(dialogue):
    template = make_img_prompt
    prompt_template = PromptTemplate(input_variables=["dialogue"], template=template)
    chain = LLMChain(prompt=prompt_template, llm=OpenAI(model="solar-1-mini-chat"))
    response = chain.run(dialogue=dialogue)
    return response