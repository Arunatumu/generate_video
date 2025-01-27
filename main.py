from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

#HeyGen details
HEYGEN_API_KEY = "NDUyNWI4ZmUxYTVhNDJiNDliMGNlNzE2OTgwOWRjM2UtMTczNzY5NTA0MA=="
HEYGEN_API_URL = "https://api.heygen.com/v2/video/generate"

# request model
class VideoRequest(BaseModel):
    text: str #the text avatar should speak
    avatar_id: str  # the ID of the avatar to use
    voice_id: str  # the ID of the voice to use

# Endpoint to create the avatar video
@app.post("/generate_video/")
async def generate_video(request: VideoRequest):
    
    payload = {
        "api_key": HEYGEN_API_KEY,
        "text": request.text,
        "avatar_id": request.avatar_id,
        "voice_id": request.voice_id,
        "style": "normal" 
    }

    try:
        # Sending a POST request to HeyGen
        response = requests.post(HEYGEN_API_URL, json=payload)
        response_data = response.json()

        # Check if the request is successful generate video_id
        if response.status_code == 200 and "video_id" in response_data:
            return {"video_id": response_data["video_id"]}
        else:
            raise HTTPException(
                status_code=400,
                detail=response_data.get("message", "Error creating video")
            )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
