from moviepy.editor import VideoFileClip
from downloader import download_video
import os


def convert_audio(url, audio_name):

    try:
        # Download the video
        download_video(url)

        # Use a context manager to ensure the video file is closed properly
        with VideoFileClip("video.mp4") as video:
            # Extract the audio and write it to an MP3 file
            audio_filename = f"{audio_name}.mp3"
            output_path = f"C:\\Users\\hp\\Music\\{audio_filename}"
            video.audio.write_audiofile(f"{output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Clean up the downloaded video file
        try:
            os.remove("video.mp4")
        except Exception as e:
            print(f"Failed to remove file: {e}")


if __name__ == "__main__":
    url = input("Enter YouTube URL: ")
    audio_name = input("Audio name (without type): ")
    convert_audio(url=url, audio_name=audio_name)
