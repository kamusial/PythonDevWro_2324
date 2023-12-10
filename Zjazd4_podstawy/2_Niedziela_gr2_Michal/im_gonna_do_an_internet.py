import random
from pathlib import Path
import requests
import httpx


def get_pokemon(pokemon_id: int):
    response = httpx.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
    pokemon_data = response.json()
    return pokemon_data


def download_png(url: str, filename: str):
    repsonse = httpx.get(url)
    png_file = open(Path(__file__).parent / "pngs" / filename, "wb")
    png_file.write(repsonse.content)


def download_pokemon_png(pokemon_id: int):
    data = get_pokemon(pokemon_id)
    name = data["name"]
    url = data["sprites"]["other"]["official-artwork"]["front_default"]
    download_png(url, name + ".png")

"""
Ściągnij .png losowego pokemona :)
"""


def download_png_of_random_pokemon():
    pokemon_id = random.randint(1, 151)
    download_pokemon_png(pokemon_id)


"""
Ściągnij .png wszystkich 151 pokemonów :)
"""


def download_pngs_of_151_pokemon():
    for pokemon_id in range(1, 152):
        download_pokemon_png(pokemon_id)


download_pngs_of_151_pokemon()
