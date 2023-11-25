"""
Utwórz klasę:
Player / Hero / Monster / NPC / Attackable
- self.hp
- self.damage
- def attack


Zasymuluj walkę 2 obiektów
kiedy self.hp <= 0 oznacz obiekt jako martwy
Ogłoś zwycięzcę pojedynku :D
"""


class Character:
    def __init__(self, hp, damage):
        self.hp = hp
        self.damage = damage

    def attack(self, target):
        target.hp -= self.damage


godzilla = Character(110, 15)
hedora = Character(150, 10)

while godzilla.hp > 0 and hedora.hp > 0:
    godzilla.attack(hedora)
    hedora.attack(godzilla)
    print(f"Godzilla ma {godzilla.hp} HP a Hedora {hedora.hp}")
if godzilla.hp > 0:
    print("Pojedynek wygrała godzilla!")
else:
    print("Pojedynek wygrała hedora!")
