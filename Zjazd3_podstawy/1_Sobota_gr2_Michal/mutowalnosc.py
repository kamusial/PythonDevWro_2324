"""
Lista - wór elementów - można je zmieniać w trakcie istnienia listy
Tupla - wór elementów - nie można jej zmieniać po utworzeniu
Dict - wór par elementów - można je zmieniać w trakcie istnienia listy
"""

def modifier(x):
    x[1] = 3


a = [1, 2]
modifier(a)
print(a)
