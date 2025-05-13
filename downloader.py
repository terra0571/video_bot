from pytube import YouTube
import os

def download_youtube_video(url):
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()
    
    if not os.path.exists("downloads"):
        os.makedirs("downloads")
    
    file_path = stream.download(output_path="downloads")
    return file_path, yt.title