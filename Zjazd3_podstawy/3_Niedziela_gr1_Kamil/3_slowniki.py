# napisz program, który przyjmuje numer i zwraca wszystkie dostępne informacje
# napisz program, który przyjmuje imie i zwraca stan konta

imiona = {
    4123: 'Asia',
    1234: 'Kamil',
    8777: 'Bartosz'
}

stan_konta = {
    4123: 2342,
    1234: 0,
    8777: 100000
}

for number in imiona.keys():
    print(imiona[number])

for value in imiona.values():
    print(value)

if 'Asia' in imiona.values():
    pass