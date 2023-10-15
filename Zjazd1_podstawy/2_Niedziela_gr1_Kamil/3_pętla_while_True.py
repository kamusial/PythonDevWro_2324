standard_age = 18
user_age = int(input('Ile masz lat? '))

while True:
    if user_age >= standard_age:
        print('jestes pelnoletni')
        break
    elif user_age >= 13:
        print('dostarcz zgode rodzica')
        break
    elif user_age >= 8:
        print('dostarcz zgode psychologa')
        break
    else:
        print('Niestety, jesteś za mlody')
        user_age = int(input('Jeszcze raz, podaj wiek: '))
print('dalsza czesc programu')

# program, który przyjmuje cene w przedziale 1 - 1000zł
while True:
    cena = float(input('Podaj cenę (1-1000): '))
    if 1 <= cena <= 1000:
        break
    else:
        print('Zla cena, jeszcze raz.')

print('Cena zaakceptowana')