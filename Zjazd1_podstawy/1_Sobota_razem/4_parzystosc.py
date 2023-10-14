try:
    number = int(input('Podaj liczbę: '))
    if number % 2 == 0:
        print('Parzysta')
    elif number % 2 != 0:
        print('Nieparzysta')
except ValueError:
    print('Będna wartość')


print('Program jest Ci niezbędny, serio?')
