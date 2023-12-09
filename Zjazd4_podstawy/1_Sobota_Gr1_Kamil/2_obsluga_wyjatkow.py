x = input('Podaj 2 liczby do dzielenia:   ').split()

try:
    result = int(x[0]) / int(x[1])
except IndexError:
    print('blad, zakladam, ze result to pierwsa liczba')
    result = int(x[0]) / 1
except ZeroDivisionError:
    print('blad, zakladam, ze result to 0')
    result = 1
    raise
except ValueError:
    print('blad, zakladam, ze result to 1')
    result = 0
else:
    print(f'Udalo sie - tworze plik z logami')
finally:
    print('finally - koniec')
    print(f'wynik to: {result}')