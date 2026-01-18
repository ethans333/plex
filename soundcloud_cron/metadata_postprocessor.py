from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from yt_dlp.postprocessor.common import PostProcessor


class MetaDataPostProcessor(PostProcessor):
    def run(self, info):
        audio = MP3(info["filepath"], ID3=EasyID3)

        title = audio.get("title", [None])[0]
        album = audio.get("album", [None])[0]

        artist = audio.get("artist", [None])[0]
        album_artist = audio.get("albumartist", [None])[0]

        changed = False

        # album title
        if (not album) and title:
            audio["album"] = [title]
            changed = True

        # album artist
        if (not album_artist) and artist:
            audio["albumartist"] = [artist]
            changed = True

        if changed:
            audio.save()

        return [], info
