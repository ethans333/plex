import os
import json
from yt_dlp import YoutubeDL
from metadata_postprocessor import MetaDataPostProcessor


class SoundCloudDownloader:
    def __init__(
        self,
        media_url: str | list[str],
        media_dir: str,
        ytdl_options_path: str = "./data/yt_dlp_options.json",
    ):
        with open(ytdl_options_path, 'r') as file:
            self.options = json.load(file)

        self.options["download_archive"] = os.path.join(
            media_dir,
            "archive.txt"
        )
        self.options["outtmpl"] = os.path.join(
            media_dir,
            "%(uploader)s/%(title)s.%(ext)s"
        )

        self.media_url = media_url
        self.media_dir = media_dir

    def download(self):
        with YoutubeDL(self.options) as ydl:
            # download songs
            ydl.add_post_processor(
                MetaDataPostProcessor(), when="post_process")
            ydl.download(self.media_url)
