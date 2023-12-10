from os import PathLike
from pathlib import Path
import asyncio
import httpx
from bs4 import BeautifulSoup, Tag


def find_newest_page_number(xml_tag: Tag) -> int:
    tags_with_kwejk_href = xml_tag.find_all("a", attrs={"href": "https://kwejk.pl"})
    for tag in tags_with_kwejk_href:
        if tag.text.isnumeric():
            return int(tag.text)


async def download_image(client: httpx.AsyncClient, url: str, filepath: PathLike):
    repsonse = await client.get(url)
    png_file = open(filepath, "wb")
    png_file.write(repsonse.content)


async def download_newest_memes():
    response = httpx.get("https://kwejk.pl/")
    response.raise_for_status()
    html = BeautifulSoup(response.text, features="html.parser")
    images: list[Tag] = html.find_all("img", attrs={"class": "full-image"})
    # newest_page = find_newest_page_number(html)
    # print(newest_page)
    # for section in sections_with_memes:
    async with httpx.AsyncClient() as client:
        for image in images:
            url = image.attrs["src"]
            name = image.attrs["alt"] + ".jpg"
            print(f"Downloading {name}")
            filepath = Path(__file__).parent / "jpgs" / name
            await download_image(client, url, filepath)


asyncio.run(download_newest_memes())

"""
Używając html.find znajdź aktualnie najnowszą stronę memów: "57132"
"""