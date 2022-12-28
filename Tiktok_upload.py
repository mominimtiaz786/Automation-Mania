import requests
import json

# Set the API endpoint URL
endpoint_url = "https://open.tiktok.com/api/v2/video/upload"

# Set the API key and access token
api_key = "your_api_key"
access_token = "your_access_token"

# Set the video file path
video_file = "path/to/your/video/file.mp4"

# Set the video metadata
title = "My TikTok Video"
description = "This is my TikTok video"
tags = ["tiktok", "video"]

# Set the scheduled publish time (in UTC)
scheduled_publish_time = "2022-01-01T00:00:00Z"

# Set the API headers
headers = {
    "api_key": api_key,
    "access_token": access_token,
}

# Set the API data
data = {
    "video": open(video_file, "rb"),
    "title": title,
    "description": description,
    "tags": ",".join(tags),
    "scheduled_publish_time": scheduled_publish_time,
}

# Send the API request
response = requests.post(endpoint_url, headers=headers, data=data)

# Print the API response
print(response.text)
