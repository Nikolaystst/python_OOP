# from project.pokemon import Pokemon
from pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"
        return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str):
        try:
            poke = next(filter(lambda x: x.name == pokemon_name, self.pokemons))
        except StopIteration:
            return "Pokemon is not caught"

        self.pokemons.remove(poke)
        return f"You have released {pokemon_name}"
        # for name_1 in self.pokemons:
        #     if name_1.name == pokemon_name:
        #         self.pokemons.remove(name_1)
        #         return f"You have released {pokemon_name}"
        #
        # return "Pokemon is not caught"

    def trainer_data(self):
        final = "\n".join(f"- {p.pokemon_details()}" for p in self.pokemons)

        return f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n{final}"


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
third_pokemon = Pokemon("hi", 231231)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(third_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
