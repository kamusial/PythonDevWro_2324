import json


class Pokemon:
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height


def load_pikachu():
    pika_file = open("pika.json")
    pikachu_dict = json.load(pika_file)
    return Pokemon(pikachu_dict["name"],
                   pikachu_dict["weight"],
                   pikachu_dict["height"])


pikachu = load_pikachu()

# Stworzenie klasy Pokemon ułatwia nam czytanie danych z
# załadowanego jsona:
print(pikachu.name)

