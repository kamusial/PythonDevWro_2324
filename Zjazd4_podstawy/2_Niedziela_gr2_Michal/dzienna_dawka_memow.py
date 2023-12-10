import httpx
from bs4 import BeautifulSoup, Tag


response = httpx.get("https://kwejk.pl/")
response.raise_for_status()
html = BeautifulSoup(response.text, features="html.parser")
images = html.find_all("img", attrs={"class": "full-image"})
# for section in sections_with_memes:
for image in images:
    image: Tag
    print(image.attrs["src"])

"""
Pobierz obrazki do folderu jpgs
Dodatkowe 'punkty' za użycie async.gather :)
"""