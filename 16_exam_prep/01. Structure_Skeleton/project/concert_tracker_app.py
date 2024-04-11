from typing import List

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_TYPES = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}

    # NEEDED_TYPES = {"Rock":
    #                     {"Drummer": ["play the drums with drumsticks"], "Singer": ["sing high pitch notes"],
    #                      "Guitarist": ["play rock"]},
    #                 "Metal":
    #                     {"Drummer": ["play the drums with drumsticks"], "Singer": ["sing low pitch notes"],
    #                      "Guitarist": ["play metal"]},
    #                 "Jazz":
    #                     {"Drummer": ["play the drums with drum brushes"],
    #                      "Singer": ["sing high pitch notes", "sing low pitch notes"],
    #                      "Guitarist": ["play jazz"]}}

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_TYPES.keys():
            raise ValueError("Invalid musician type!")

        for music in self.musicians:
            if music.name == name:
                raise Exception(f"{name} is already a musician!")

        self.musicians.append(self.VALID_TYPES[musician_type](name, age))
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        for band in self.bands:
            if band.name == name:
                raise Exception(f"{name} band is already created!")

        self.bands.append(Band(name))
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        for concert in self.concerts:
            if concert.place == place:
                raise Exception(f"{place} is already registered for {concert.genre} concert!")

        self.concerts.append(Concert(genre, audience, ticket_price, expenses, place))
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        a = self.get_musician(musician_name)
        b = self.get_band(band_name)
        b.members.append(a)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        b = self.get_band(band_name)
        for musician in b.members:
            if musician.name == musician_name:
                b.members.remove(musician)
                return f"{musician_name} was removed from {band_name}."
        raise Exception(f"{musician_name} isn't a member of {band_name}!")

    def start_concert(self, concert_place: str, band_name: str):

        band_1 = self.get_band(band_name)
        concert_1 = None
        for concert in self.concerts:
            if concert.place == concert_place:
                concert_1 = concert
                break

        for musician_type in ["Drummer", "Singer", "Guitarist"]:
            if not any(
                    filter(
                        lambda x: x.__class__.__name__ == musician_type,
                        band_1.members
                    )
            ):
                raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        if concert_1.genre == "Rock":
            for member in band_1.members:
                if member.__class__.__name__ == "Drummer" and "play the drums with drumsticks" not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif member.__class__.__name__ == "Singer" and "sing high pitch notes" not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif member.__class__.__name__ == "Guitarist" and "play rock" not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
        elif concert_1.genre == "Metal":
            for member in band_1.members:
                if member.__class__.__name__ == "Drummer" and "play the drums with drumsticks" not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif member.__class__.__name__ == "Singer" and "sing low pitch notes" not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif member.__class__.__name__ == "Guitarist" and "play metal" not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
        elif concert_1.genre == "Jazz":
            for member in band_1.members:
                if member.__class__.__name__ == "Drummer" and "play the drums with drum brushes" not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif member.__class__.__name__ == "Singer" and (
                        "sing low pitch notes" not in member.skills or "sing high pitch notes" not in member.skills):
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif member.__class__.__name__ == "Guitarist" and "play jazz" not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert_1.audience * concert_1.ticket_price) - concert_1.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert_1.genre} concert in {concert_place}."

    def get_band(self, band_name: str):
        for band_1 in self.bands:
            if band_1.name == band_name:
                return band_1

        raise Exception(f"{band_name} isn't a band!")

    def get_musician(self, musician_name: str):
        for musician in self.musicians:
            if musician.name == musician_name:
                return musician
        raise Exception(f"{musician_name} isn't a musician!")
