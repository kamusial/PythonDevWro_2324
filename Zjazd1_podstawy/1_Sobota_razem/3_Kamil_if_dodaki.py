# pomidory kosztują 3zł sztuka. Ale w 3-paku, 3 pomidory razem kosztują 80% ceny
# program pyta ile pomidorów chcemy kupić i zwraca najniższą cenę

# print(11 // 3)
# print(11 % 3)

#podejscie 1
print('Ie pomidorów chcesz kupić? ')
no_of_tomatos = input()
print('Chcesz kupić')
print(no_of_tomatos)
print('pomidorow')

# każdy 3-pak = 3zł/szt * 80%
# osobne pomidory = 3zł

no_of_3packs = int(no_of_tomatos) // 3   #część całkowita z dzielenia

print('liczba 3-pakow')
print(no_of_3packs)

no_of_tomatos_apart = int(no_of_tomatos) - no_of_3packs * 3
print('liczba pomidorow osobno')
print(no_of_tomatos_apart)

money_to_pay = (no_of_3packs * (3 * 3 * 0.8) + no_of_tomatos_apart * 3)

print('zaplacisz')
print(round(money_to_pay, 2))

# podejście2

no_of_tomatos = int(input('Ile pomidorów chcesz kupić? '))

print(round((no_of_tomatos // 3) * 3 * 3 * 0.8 + no_of_tomatos % 3 * 3, 2))


