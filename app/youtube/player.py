import re
import urllib.parse
import urllib.request
import json


def get_vid(query):
    """
    Search YouTube and return the first video ID.
    """

    try:
        query = query.strip()

        if not query:
            return None

        encoded = urllib.parse.quote_plus(query)

        url = f"https://www.youtube.com/results?search_query={encoded}"

        request = urllib.request.Request(
            url,
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 "
                    "(KHTML, like Gecko) "
                    "Chrome/140.0.0.0 Safari/537.36"
                ),
                "Accept-Language": "en-US,en;q=0.9",
            },
        )

        with urllib.request.urlopen(request, timeout=10) as response:
            data = response.read().decode(
                "utf-8",
                errors="ignore"
            )

        # Method 1: normal YouTube videoId
        ids = re.findall(
            r'"videoId":"([A-Za-z0-9_-]{11})"',
            data
        )

        if ids:
            return ids[0]

        # Method 2: escaped JSON
        ids = re.findall(
            r'\\"videoId\\":\\"([A-Za-z0-9_-]{11})\\"',
            data
        )

        if ids:
            return ids[0]

        return None

    except Exception as e:
        print("YouTube search error:", repr(e))
        return None


def create_youtube_url(command):
    """
    Convert a voice command into a YouTube embed URL.
    """

    if not command:
        return None

    original_command = command.strip()
    text = original_command.lower()

    patterns = [
        r"play\s+song\s+(.+)",
        r"play\s+music\s+(.+)",
        r"play\s+youtube\s+(.+)",
        r"youtube\s+(.+)",
        r"play\s+(.+)",
    ]

    query = original_command

    for pattern in patterns:
        match = re.search(pattern, text)

        if match:
            query = original_command[match.start(1):].strip()
            break

    query = query.strip()

    if not query:
        return None

    video_id = get_vid(query)

    if not video_id:
        return None

    return (
        f"https://www.youtube.com/embed/{video_id}"
        "?autoplay=1"
        "&rel=0"
    )
