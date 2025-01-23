import os
import yt_dlp
from typing import Optional


class DownloadError(Exception):
    """Базовый класс для ошибок загрузки"""


def download_video(
        url: str,
        save_path: str = "downloads",
        media_type: str = "video",
        quality: Optional[str] = None
) -> None:
    """
    Скачивает видео/аудио с YouTube с использованием yt-dlp

    Аргументы:
        url: Ссылка на YouTube видео
        save_path: Путь для сохранения файлов
        media_type: 'video' или 'audio'
        quality: Желаемое разрешение видео (например, '720p')
    """
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
                # Формат: best видео с высотой <= указанной + best аудио
                ydl_opts['format'] = f'bestvideo[height<={quality[:-1]}]+bestaudio'
            else:
                ydl_opts['format'] = 'bestvideo+bestaudio/best'
        else:
            raise DownloadError("Недопустимый тип медиа. Используйте 'video' или 'audio'")

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            print(f"\nСкачивание: {info_dict['title']}")
            if media_type == "video":
                print(f"Разрешение: {quality if quality else 'максимальное'}")
            ydl.download([url])

        print(f"\n✅ Успешно сохранено в: {os.path.abspath(save_path)}")

    except yt_dlp.utils.DownloadError as e:
        raise DownloadError(f"Ошибка загрузки: {str(e)}") from e


def progress_hook(d: dict):
    """Отображает прогресс загрузки"""
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', 'N/A')
        speed = d.get('_speed_str', 'N/A')
        print(f"\rПрогресс: {percent} | Скорость: {speed}", end="", flush=True)