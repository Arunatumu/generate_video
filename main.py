from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

# Replace this with your actual HeyGen API key
HEYGEN_API_KEY = "NDUyNWI4ZmUxYTVhNDJiNDliMGNlNzE2OTgwOWRjM2UtMTczNzY5NTA0MA=="
HEYGEN_API_URL = "https://api.heygen.com/v2/video/generate"

# Request schema for the API
class VideoRequest(BaseModel):
    text: str
    avatar_id: str
    voice_id: str

@app.post("/generate_video")
async def generate_video(request: VideoRequest):
    """
    Endpoint to generate a video using HeyGen API.
    """
    payload = {
        "api_key": HEYGEN_API_KEY,
        "text": request.text,
        "avatar_id": request.avatar_id,
        "voice_id": request.voice_id,
        "style": "normal"  # Optional: specify style if required
    }
    try:
        # Send POST request to HeyGen API
        response = requests.post(HEYGEN_API_URL, json=payload)
        response_data = response.json()

        # Check response and return video_id if successful
        if response.status_code == 200 and "video_id" in response_data:
            return {"video_id": response_data["video_id"]}
        else:
            # Raise error with response message
            raise HTTPException(status_code=400, detail=response_data.get("message", "Error creating video"))

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
