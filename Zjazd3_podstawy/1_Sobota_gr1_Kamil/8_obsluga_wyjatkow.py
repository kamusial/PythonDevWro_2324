while True:
    try:
        wiek = int(input('Podaj wiek: '))
        x = 5 / 0
        break
    except ValueError:
        print('złe dane wprowadzone, jeszcze raz')
    except ZeroDivisionError:
        x = 0
        break

print(f'na emerytuję przejdziesz za {65 - wiek}')