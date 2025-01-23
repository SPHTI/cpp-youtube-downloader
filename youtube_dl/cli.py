import argparse
import sys
from .downloader import download_video, DownloadError


def display_banner():
    print("""
    YouTube Downloader
    ------------------
    """)


def interactive_mode():
    display_banner()
    while True:
        try:
            url = input("\nEnter YouTube URL (q to quit): ").strip()
            if url.lower() in ('q', 'quit', 'exit'):
                break

            media_type = input("Media type [video/audio]: ").strip().lower() or "video"
            quality = None

            if media_type == "video":
                quality = input("Quality (e.g. 720p) [max]: ").strip() or None

            save_dir = input("Save directory [downloads]: ").strip() or "downloads"

            download_video(url, save_dir, media_type, quality)
            print("\nDownload completed!")

        except DownloadError as e:
            print(f"\nError: {str(e)}")
        except KeyboardInterrupt:
            print("\nOperation cancelled")
            break


def main():
    parser = argparse.ArgumentParser(description="YouTube Downloader")
    parser.add_argument("url", nargs="?", help="YouTube URL")
    parser.add_argument("-d", "--dir", help="Output directory")
    parser.add_argument("-t", "--type", choices=["video", "audio"], help="Media type")
    parser.add_argument("-q", "--quality", help="Video quality")

    args = parser.parse_args()

    if args.url:
        try:
            download_video(
                args.url,
                args.dir or "downloads",
                args.type or "video",
                args.quality
            )
        except DownloadError as e:
            print(f"Error: {str(e)}", file=sys.stderr)
            sys.exit(1)
    else:
        interactive_mode()


if __name__ == "__main__":
    main()