import os
import requests

YOUTUBE_KEY = os.getenv("YOUTUBE_API_KEY")


def get_video(recipe_name):

    if not YOUTUBE_KEY:

        return f"https://www.youtube.com/results?search_query={recipe_name}+recipe"

    url = "https://www.googleapis.com/youtube/v3/search"

    params = {
        "part": "snippet",
        "maxResults": 1,
        "q": recipe_name + " recipe",
        "type": "video",
        "key": YOUTUBE_KEY,
    }

    try:
        r = requests.get(url, params=params, timeout=10)
        data = r.json()

        items = data.get("items", [])

        if not items:
            return f"https://www.youtube.com/results?search_query={recipe_name}+recipe"

        video_id = items[0]["id"]["videoId"]

        return f"https://www.youtube.com/watch?v={video_id}"

    except Exception:
        return f"https://www.youtube.com/results?search_query={recipe_name}+recipe"