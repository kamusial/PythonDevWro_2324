zbior1 = {1, 4, 5, 4, 2, 7}
zbior2 = {2, 7, 8, 0, 9}

print(zbior1)
print(zbior2)

# suma zbiorów         ->  |
# część wspólna        ->  &
# różnica              ->  -
# różnica symetryczna  ->  ^

print(f'suma zbiorów: {zbior1 | zbior2}')
print(f'część wspólna zbiorów: {zbior1 & zbior2}')
print(f'różnica zbiorów: {zbior1 - zbior2}')
print(f'różnica symetryczna zbiorów: {zbior1 ^ zbior2}')

lista = [1, 2, 5, 5, 4, 34, 2, 4, 7, 9]

lista = list(set(lista))
print(lista)

imiona = {'Kamil', 'Aleksandra', 'Oliwia', 'Agnieszka', 'Arkadusz'}
#stworzyć osobne zbiory na imiona męskie i damskie

meskie = set()
zenskie = set()

for imie in imiona:
    if imie[-1] == 'a':
        zenskie.add(imie)
meskie = imiona - zenskie







