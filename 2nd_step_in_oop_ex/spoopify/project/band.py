# from project.album import Album
# from project.song import Song
from album import Album
from song import Song
from typing import List


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums: List[Album] = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str) -> str:
        for album_1 in self.albums:
            if album_1.name == album_name:
                if album_1.published:
                    return "Album has been published. It cannot be removed."

                self.albums.remove(album_1)
                return f"Album {album_name} has been removed."

        return f"Album {album_name} is not found."

    def details(self):
        albums = "\n".join(a.details() for a in self.albums)
        return f"Band {self.name}\n{albums}"

