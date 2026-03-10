from youtube_transcript_api import YouTubeTranscriptApi

def get_video_id(url):

    if "watch?v=" in url:
        return url.split("watch?v=")[1]

    return url


def get_transcript(url):

    video_id = get_video_id(url)

    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    text = " ".join([entry["text"] for entry in transcript])

    return text
