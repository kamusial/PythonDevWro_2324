import json


def load_pikachu() -> dict:
    pika_file = open("pika.json")
    pikachu_dict = json.load(pika_file)
    return pikachu_dict


pikachu = load_pikachu()

"""Utworz listę nazw wszystkich movesetów pikachu"""
moves = []
for move in pikachu["moves"]:
    moves.append(move["move"]["name"])
# for move in moves:
#     print(move)

"""Utwórz listę nieukrytych umiejętności pikachu
czyli pikachu["abilities"] które mają is_hidden = false
oczekiwany print / output:
abilities_list = ["static"]
"""
abilities = []
for ability in pikachu["abilities"]:
    if ability["is_hidden"] is False:
        abilities.append(ability["ability"]["name"])
print(abilities)
