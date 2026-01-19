import os
from soundcloud_downloader import SoundCloudDownloader


def main():
    SoundCloudDownloader(
        os.getenv("MEDIA_URL"),
        os.getenv("MEDIA_DIR")).download()


if __name__ == "__main__":
    main()
