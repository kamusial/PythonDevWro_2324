from pathlib import Path
import asyncio
import httpx


async def get_pokemon(client: httpx.AsyncClient, pokemon_id: int):
    response = await client.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
    pokemon_data = response.json()
    return pokemon_data


async def download_png(client: httpx.AsyncClient, url: str, filename: str):
    repsonse = await client.get(url)
    png_file = open(Path(__file__).parent / "pngs" / filename, "wb")
    png_file.write(repsonse.content)


async def download_pokemon_png(client: httpx.AsyncClient, pokemon_id: int):
    print(f"Getting dictionary of {pokemon_id=}")
    data = await get_pokemon(client, pokemon_id)
    name = data["name"]
    url = data["sprites"]["other"]["official-artwork"]["front_default"]
    print(f"Downloading png of {name} ({pokemon_id=})")
    await download_png(client, url, name + ".png")
    print(f"{name}.png downloaded")


"""
Ściągnij .png 10 pokemonów :)
"""


async def download_pngs_of_10_pokemon():
    async with httpx.AsyncClient() as client:
        await asyncio.gather(*(download_pokemon_png(client, pokemon_id) for pokemon_id in range(1, 11)))


asyncio.run(download_pngs_of_10_pokemon())
