x = input('Podaj 2 liczby do dzielenia:   ').split()

try:
    result = int(x[0]) / int(x[1])
except IndexError:
    result = int(x[0])
except ZeroDivisionError:
    result = 1
except ValueError:
    result = 0

print(result)