from typing import List

from project.player import Player
from project.supply.drink import Drink
from project.supply.food import Food
from project.supply.supply import Supply


class Controller:
    VALID_TYPES = [
        "Food",
        "Drink"
    ]

    def __init__(self):
        self.players: List[Player] = []
        self.supplies: List[Supply] = []

    def add_player(self, *args) -> str or None:
        players_added = []
        for player in args:
            if player not in self.players:
                self.players.append(player)
                players_added.append(player.name)

        return f"Successfully added: {', '.join(players_added)}"

    def add_supply(self, *args) -> None:
        for arg in args:
            self.supplies.append(arg)

    def sustain(self, player_name: str, sustenance_type: str):
        if sustenance_type not in Controller.VALID_TYPES:
            return

        for pl in self.players:
            if pl.name == player_name:
                break
        else:
            return

        if not pl.need_sustenance:
            return f"{player_name} have enough stamina."

        for i in range(len(self.supplies)-1, -1, -1):
            food = self.supplies[i]
            if food.__class__.__name__ == sustenance_type:
                self.supplies.pop(i)
                break
        else:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        pl.stamina = min(pl.stamina + food.energy, 100)
        return f"{player_name} sustained successfully with {food.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        zero_stamina = []
        players = [p for p in self.players if p.name == first_player_name or p.name == second_player_name]
        players = sorted(players, key=lambda x: x.stamina)
        p1 = players[0]
        p2 = players[1]
        if p1.stamina <= 0:
            zero_stamina.append(f"Player {p1.name} does not have enough stamina.")
        if p2.stamina <= 0:
            zero_stamina.append(f"Player {p2.name} does not have enough stamina.")
        if zero_stamina:
            return "\n".join(zero_stamina)

        p2.stamina = max(p2.stamina - (p1.stamina / 2), 0)

        p1.stamina = max(p1.stamina - (p2.stamina / 2), 0)

        players = [p1, p2]
        players = sorted(players, key=lambda x: x.stamina)
        winner = players[1]
        return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            player.stamina = max(player.stamina - (player.age * 2), 0)

            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = []
        for p in self.players:
            result.append(p.__str__())
        for f in self.supplies:
            result.append(f.details())
        return "\n".join(result)
