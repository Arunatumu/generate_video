import requests

def send_video_request(api_url, text, avatar_id, voice_id):
    """
    Sends a request to the FastAPI server to generate a video.

    Parameters:
    - api_url (str): The URL of the FastAPI endpoint.
    - text (str): The text the avatar should speak.
    - avatar_id (str): The ID of the avatar to use.
    - voice_id (str): The ID of the voice to use.
    """
    payload = {
        "text": text,
        "avatar_id": avatar_id,
        "voice_id": voice_id
    }

    try:
        # Send a POST request to the API
        response = requests.post(api_url, json=payload)

        # Handle the response
        if response.status_code == 200:
            response_data = response.json()
            print(f"Video ID: {response_data.get('video_id')}")
        else:
            print(f"Error: {response.status_code}, {response.text}")
    except requests.RequestException as e:
        print(f"Request failed: {str(e)}")

# Example client usage
if __name__ == "__main__":
    # FastAPI endpoint URL
    API_URL = "http://127.0.0.1:8000/generate_video"

    # Details for video creation
    TEXT = "Welcome to HDFC Bank! How can we assist you today?"
    AVATAR_ID = "avatar_1"  # Replace with actual avatar ID
    VOICE_ID = "voice_1"    # Replace with actual voice ID

    # Sending  the request
    send_video_request(API_URL, TEXT, AVATAR_ID, VOICE_ID)
