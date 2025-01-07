import yt_dlp


def download_video(url):

    video_url = url

    # Define the download options to get the lowest quality
    ydl_opts = {
        "format": "best",  # Download the worst (lowest quality) video format
        "outtmpl": "video.mp4",  # Output filename
    }

    # Download the video
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

    print("Download completed!")


if __name__ == "__main__":
    download_video("https://youtu.be/BOCM7hh_KOY?si=k665HNl6r9PZ0Jzu")
