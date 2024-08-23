# app/main.py

from app.services.dialogue_extraction import extract_dress_info
from app.services.dress_generation import generate_dress
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class DialogueRequest(BaseModel):
    dialogue: str

@app.post("/generate-dress/")
async def generate_dress_from_dialogue(request: DialogueRequest):
    try:
        # Assuming extract_dress_info and generate_dress are defined somewhere in your service
        dress_prompt = extract_dress_info(request.dialogue)
        dress_image = generate_dress(dress_prompt)

        return dress_image # Returning the image URL or base64 encoded image data

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))