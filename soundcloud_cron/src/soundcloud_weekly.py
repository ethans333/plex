import os
import time
from datetime import date
from plexapi.server import PlexServer
from plexapi.audio import Track
from plexapi.library import Library
from soundcloud_downloader import SoundCloudDownloader


def main():
    plex = PlexServer(os.getenv("PLEX_BASE_URL"), os.getenv("PLEX_TOKEN"))
    music_library: Library = plex.library.section('Music')

    weekly_name = f"SoundCloud Weekly 🔥 [{date.today().strftime("%m-%d-%Y")}]"
    weekly_path = os.path.join(os.getenv("MEDIA_DIR"), weekly_name)

    info = SoundCloudDownloader(
        os.getenv("MEDIA_URL"),
        weekly_path,
        archive_file_path=os.path.join(os.getenv("MEDIA_DIR"), "archive.txt")
    ).download()

    music_library.update(path=weekly_path)

    print("Waiting for library to update...")
    n_tracks = info.get("playlist_count", 0)
    while len(tracks_to_add := get_tracks_in_folder(music_library, weekly_name)) < n_tracks:
        time.sleep(3)
    print("✔ Library updated.")

    playlist = plex.createPlaylist(title=weekly_name, items=tracks_to_add)
    print(f"'{playlist.title}' added w/ {len(tracks_to_add)} tracks")


def get_tracks_in_folder(library: Library, folder_name: str) -> list[Track]:
    tracks = []

    for track in library.searchTracks():
        track: Track
        gp_dir = track.media[0].parts[0].file.split(os.sep)[-3]

        if gp_dir == folder_name:
            tracks.append(track)

    return tracks


if __name__ == "__main__":
    main()
