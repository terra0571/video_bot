from pytube import YouTube
import os

def download_youtube_video(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()

        if stream is None:
            raise Exception("❌ Video oqim topilmadi (format mavjud emas).")

        if not os.path.exists("downloads"):
            os.makedirs("downloads")

        file_path = stream.download(output_path="downloads")
        return file_path, yt.title

    except Exception as e:
        raise Exception(f"❌ YouTube videoni yuklab bo‘lmadi:\n{str(e)}")
