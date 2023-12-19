# from project.player import Player
from player import Player
from typing import List


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players: List[Player] = []

    def assign_player(self, player: Player) -> str:
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."

        elif player.guild != Player.guild:
            return f"Player {player.name} is in another guild."

        else:
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        for player_1 in self.players:
            if player_1.name == player_name:
                player_1.guild = Player.guild
                self.players.remove(player_1)
                return f"Player {player_name} has been removed from the guild."

        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        players = "\n".join(p.player_info() for p in self.players)
        return f"Guild: {self.name}\n" \
               f"{players}"
