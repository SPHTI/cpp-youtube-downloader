import argparse
import sys
from .downloader import download_video, DownloadError

def parse_args():
    parser = argparse.ArgumentParser(
        prog="yt-downloader",
        description="YouTube Downloader 2.0 (с поддержкой FFmpeg)"
    )
    parser.add_argument("url", help="Ссылка на YouTube видео")
    parser.add_argument("-d", "--dir", default="downloads", help="Папка для сохранения")
    parser.add_argument("-t", "--type", choices=["video", "audio"], default="video", help="Тип контента")
    parser.add_argument("-q", "--quality", help="Разрешение видео (например, 720p)")
    return parser.parse_args()

def main():
    args = parse_args()
    try:
        download_video(args.url, args.dir, args.type, args.quality)
    except DownloadError as e:
        print(f"\n❌ ОШИБКА: {str(e)}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n⏹️ Загрузка отменена пользователем")
        sys.exit(130)

if __name__ == "__main__":
    main()