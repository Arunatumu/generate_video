import requests
from typing import List

#backened API_URL
API_URL = "http://127.0.0.1:8000/generate_video"

#setting character limit
CHARACTER_LIMIT=100

#function to break text into chunks
def split_text(text, limit):
    if len(text) <= limit:
        return [text]
    
    chunks = []
    for i in range(0, len(text), limit):
        chunks.append(text[i:i + limit])
    return chunks

# Function to send  chunk to the backend and get a video ID
def video_id_for_chunk(chunk, avatar_id, voice_id):
    
    # Sends a chunk of text to the backend API and retrieves the video ID.

    data = {
        "text": chunk,
        "avatar_id": avatar_id,
        "voice_id": voice_id
    }
    
    try:
        response = requests.post(API_URL, json=data)
        if response.status_code == 200:
            response_data = response.json()
            return response_data.get("video_id")
        else:
            print(f"Failed to get video for chunk. Status: {response.status_code}, Response: {response.text}")
            return None
    except Exception as e:
        print(f"Error connecting to the backend: {e}")
        return None
    
# Main function to handle the whole process
def generate_videos(text, avatar_id, voice_id):
    """
    Splits the text into chunks if needed, sends each chunk to the backend, and collects video IDs.
    """
    if len(text) > CHARACTER_LIMIT:
        chunks = split_text(text, CHARACTER_LIMIT)
        print(f"Text has been split into {len(chunks)} chunks: {chunks}")
    else:
        chunks = [text]  # No need to split if text is within limit

    video_ids = []

    for i, chunk in enumerate(chunks):
        print(f"Processing chunk {i + 1}/{len(chunks)}: {chunk}")
        video_id = video_id_for_chunk(chunk, avatar_id, voice_id)
        
        if video_id:
            print(f"Video ID for chunk {i + 1}: {video_id}")
            video_ids.append(video_id)
        else:
            print(f"Failed to generate video for chunk {i + 1}")

    return video_ids

# Example usage
if __name__ == "__main__":
    text = "This is a sample text that exceeds the character limit set for generating avatar videos. " \
           "The purpose is to test how the system splits the text into chunks and handles them sequentially for video creation."
    avatar_id = "avatar_123"
    voice_id = "voice_abc"

    print("Starting video generation process...")
    video_ids = generate_videos(text, avatar_id, voice_id)

    if video_ids:
        print("\nVideo IDs generated:", video_ids)
    else:
        print("\nNo videos were generated.")