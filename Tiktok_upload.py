import requests
import json
from datetime import datetime, timedelta

# Set the API endpoint URL
endpoint_url = "https://open.tiktok.com/api/v2/video/upload"

# Set the API key and access token
api_key = "your_api_key"
access_token = "your_access_token"


def uploadToTikTok(
    video_path,
    scheduled_publish_time,
    title='', 
    description='', 
    tags=[]
):
    # Set the API headers
    headers = {
        "api_key": api_key,
        "access_token": access_token,
    }

    # Set the API data
    data = {
        "video": open(video_path, "rb"),
        "title": title,
        "description": description,
        "tags": ",".join(tags),
        "scheduled_publish_time": scheduled_publish_time,
    }

    # Send the API request
    response = requests.post(endpoint_url, headers=headers, data=data)

    # Print the API response
    print(response.text)    


if __name__ == "__main__":
    video_path = "Videos\\1_Compiled_Videos\\CHAP_1_VERSE_[1, 2, 3, 4, 5, 6, 7].mp4"
    post_schedule = datetime.now() + timedelta(minutes=5)
    uploadToTikTok(video_path, post_schedule)