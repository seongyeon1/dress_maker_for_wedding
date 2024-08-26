# app/main.py

from app.services.dialogue_extraction import extract_dress_info
from app.services.dress_generation import make_prompt, generate_dress
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class DialogueRequest(BaseModel):
    dialogue: str

@app.post("/extract-dress-feature/")
async def generate_dress_from_dialogue(request: DialogueRequest):
    try:
        dress_info = extract_dress_info(request.dialogue)
        return dress_info

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate-dress/")
async def generate_dress_from_dialogue(request: DialogueRequest):
    try:
        dress_prompt = make_prompt(request.dialogue)
        dress_image = generate_dress(dress_prompt)
        return dress_image # Returning the image URL or base64 encoded image data

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))