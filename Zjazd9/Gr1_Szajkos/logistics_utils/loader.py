from dataclasses import dataclass


@dataclass
class City:
    name: str
    x: int
    y: int

    def __str__(self):
        return f"{self.name} ({self.x},{self.y})"

    def __repr__(self):
        return str(self)


def load_cities(map_filepath: str) -> list[City]:
    cities = []
    with open(map_filepath) as file:
        content = file.read()
    for y, line in enumerate(content.splitlines()):
        for x, character in enumerate(line):
            if character.isalpha():
                cities.append(City(character, x, y))
    return cities
