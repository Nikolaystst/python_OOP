# from project.song import Song
from typing import List
from song import Song


class Album:
    def __init__(self, name: str, *args: Song, published: bool = False):
        self.name = name
        self.published = published
        self.songs: List[Song] = [*args]

    def add_song(self, song: Song) -> str:
        if song in self.songs:
            return "Song is already in the album."

        elif self.published:
            return "Cannot add songs. Album is published."

        elif song.single:
            return f"Cannot add {song.name}. It's a single"

        else:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str) -> str:
        if self.published:
            return "Cannot remove songs. Album is published."

        for song_1 in self.songs:
            if song_1.name == song_name:
                self.songs.remove(song_1)
                return f"Removed song {song_name} from album {self.name}."

        return "Song is not in the album."

    def publish(self) -> str:
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True
        return f"Album {self.name} has been published."

    def details(self) -> str:
        songs = "\n".join(f"== {p.get_info()}" for p in self.songs)
        return f"Album {self.name}\n{songs}"
