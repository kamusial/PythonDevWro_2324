"""
Mamy 3 pary drzwi. Za 1 z nich jest nagroda.
Wybieramy 1 z nich
Program 'odkrywa' drzwi bez nagrody (*inne niż te drzwi które wybraliśmy)
Program daje nam wybór 1 z 2 - pozostań przy swoich drzwiach, albo zmień zdanie.

Jaka jest szansa na wygraną przy strategii "Zostanę przy swoim"
A jaka przy zmianie zdania?

"""
import random


def monty_hall_game(change_choice: bool):
    doors = ['goat', 'goat', 'car']
    random.shuffle(doors)

    chosen_door = random.randint(0, 2)

    revealable_doors = []
    for i in range(3):
        if i != chosen_door and doors[i] == 'goat':
            revealable_doors.append(i)
    revealed_door = random.choice(revealable_doors)

    if change_choice:
        for i in range(3):
            if i != chosen_door and i != revealed_door:
                chosen_door = i
                break

    return doors[chosen_door]




"""Odpal monty_hall_game z obiema strategiami po 10000 razy.
Wyprintuj ile % razy udało się wygrać jedną i drugą strategią.
"""
if __name__ == '__main__':
    print(monty_hall_game(False))
