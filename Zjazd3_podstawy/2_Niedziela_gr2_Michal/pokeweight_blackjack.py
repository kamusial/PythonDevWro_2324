import random
from dataclasses import dataclass

import httpx


@dataclass
class Pokemon:
    name: str
    weight: int


def get_random_pokemon() -> Pokemon:
    pokemon_id = random.randint(1, 151)
    response = httpx.get(
        f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
    pokemon_data = response.json()
    return Pokemon(pokemon_data["name"], pokemon_data["weight"])


"""
Jesteśmy w pokoju z pokemonami, i mamy wielką walizkę, w której
możemy unieść 2000 wagi.
Program spyta nas, czy chcemy wziąć kolejnego pokemona do walizki.
Jeśli powiemy "tak", to poinformuje nas ile miejsca w walizce nam zostało.
Jeśli powiemy "tak" i skończy nam się miejsce w walizce - PRZEGRYWAMY.
Jeśli powiemy "nie", gra się kończy i printuje pokemony, które
zabieramy ze sobą do domu ^_^
"""


class PokeBlackJack:
    def __init__(self):
        self.capacity = 2000
        self.suitcase = []

    def get_pokemon(self):
        pokemon = get_random_pokemon()
        self.capacity -= pokemon.weight
        self.suitcase.append(pokemon.name)
        print(f"You found {pokemon.name}, it weighs {pokemon.weight}")
        self._print_capacity()

    def _print_capacity(self):
        if self.capacity >= 0:
            print(f"Remaining capacity: {self.capacity}")
        else:
            print("No capacity left")

    @property
    def is_lost(self):
        return self.capacity <= 0


game = PokeBlackJack()
game.get_pokemon()
while input("Do you want to take another Pokemon with you? (y/n) ") == "y":
    game.get_pokemon()
    if game.is_lost:
        print("You lost :<")
        break
else:
    print(f"Congrats, you took {game.suitcase} with you ;)")


"""
Sekcja else dla pętli 'while' i 'for' wydarzy się wtedy, gdy pętla zakończy się
bez instrukcji 'break' (czyli 'naturalnie')
"""
