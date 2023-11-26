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