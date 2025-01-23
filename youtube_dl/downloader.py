import os
import yt_dlp
from typing import Optional

class DownloadError(Exception):
    pass

def download_video(
    url: str,
    save_path: str = "downloads",
    media_type: str = "video",
    quality: Optional[str] = None
) -> None:
    try:
        os.makedirs(save_path, exist_ok=True)

        ydl_opts = {
            'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
            'ffmpeg_location': 'C:/ffmpeg/bin/ffmpeg.exe',  # Укажите свой путь!
            'merge_output_format': 'mp4',
            'geo_bypass': True,
            'progress_hooks': [progress_hook],
            'verbose': False
        }

        if media_type == "audio":
            ydl_opts.update({
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192'
                }]
            })
        elif media_type == "video":
            if quality:
                ydl_opts['format'] = f'bestvideo[height<={quality[:-1]}]+bestaudio'
            else:
                ydl_opts['format'] = 'bestvideo+bestaudio/best'
        else:
            raise DownloadError("Invalid media type")

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            print(f"\nDownloading: {info_dict['title']}")
            if media_type == "video":
                print(f"Quality: {quality if quality else 'max'}")
            ydl.download([url])

        print(f"\nSaved to: {os.path.abspath(save_path)}")

    except yt_dlp.utils.DownloadError as e:
        raise DownloadError(str(e)) from e

def progress_hook(d: dict):
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', 'N/A')
        speed = d.get('_speed_str', 'N/A')
        print(f"\rProgress: {percent} | Speed: {speed}", end="", flush=True)