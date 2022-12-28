import requests

# Set the base URL for the Instagram Private API
BASE_URL = "https://i.instagram.com/api/v1/"

# Set the access token for your Instagram account
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"

# Set the path to the video file to be uploaded
video_path = "/path/to/video.mp4"

# Set the caption for the video
caption = "This is a caption for my video."

# Set the date and time for the video to be published
publish_time = "2022-12-19T00:00:00Z"

# Set the media type to "video"
media_type = "video"

# Define the payload for the request
payload = {
    "caption": caption,
    "published_at": publish_time,
    "media_type": media_type,
}

# Set the headers for the request
headers = {
    "User-Agent": "Instagram 10.26.0 Android (18/4.3; 320dpi; 720x1280; Xiaomi; HM 1SW; armani; qcom; en_US)",
    "Connection": "close",
    "Accept-Language": "en-US",
    "Accept-Encoding": "gzip",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie2": "$Version=1",
    "X-IG-Capabilities": "3w==",
    "X-IG-Connection-Type": "WIFI",
    "X-IG-App-ID": "567067343352427",
    "X-IG-WWW-Claim": "hmac.AR22cB7f0Nz_hY7NwKjdZO_xT-LQJ3mZf9Tm3zpZD1aZg==",
    "Authorization": f"Bearer {ACCESS_TOKEN}",
}

# Set the file to be uploaded
files = {"video": open(video_path, "rb")}

# Make a POST request to the Instagram Private API to upload the video
response = requests.post(
    f"{BASE_URL}upload/video/", data=payload, headers=headers, files=files
)

# Print the response from the request
print(response.text)
