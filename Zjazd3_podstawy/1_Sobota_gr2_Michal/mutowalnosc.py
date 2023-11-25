"""
Lista - wór elementów - można je zmieniać w trakcie istnienia listy
Tupla - wór elementów - nie można jej zmieniać po utworzeniu
Dict - wór par elementów - można je zmieniać w trakcie istnienia listy
"""

# zmienne mutowalne są modyfikowalne wewnątrz funkcji:
def modifier(x):
    x[1] = 3


a = [1, 2]
modifier(a)
print(a)  # [1, 3]


# zmienne niemutowalne już nie
def no_modifier(x):
    x = x + 3


a = 5
no_modifier(a)
print(a)  # nadal 5!
