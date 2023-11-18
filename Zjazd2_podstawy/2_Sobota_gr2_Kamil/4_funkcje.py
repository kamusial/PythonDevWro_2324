import random
def podatek(zarobki, liczba_dzieci):
    podatek_do_zaplaty = zarobki * 0.2 - 100 * liczba_dzieci
    # print(f'twoj podatek wynosi {podatek_do_zaplaty}')
    return podatek_do_zaplaty


x = podatek(4000, 3)
print(x)

# funcka przyjmuje wiek, wagę, samopoczucie i zwraca współczynnik zdrowia
# jeśli wpsółczynnik zdrowia > 5, można przystąpić do ubezpieczenia

def wspolczynnik_zdrowia(wiek, waga, samopoczucie):
    wspolczynnik = 0
    wspolczynnik += 3 - wiek // 20
    if 70 > waga > 50:
        wspolczynnik += 3
    wspolczynnik += samopoczucie
    return wspolczynnik

wiek = int(input('Wprowadź wiek: '))
lista_wag = [60, 45, 76, 43]
wspolczynnik = wspolczynnik_zdrowia(wiek, lista_wag[2], random.randint(2, 6))
if wspolczynnik > 5:
    print('ok')

if wspolczynnik_zdrowia(32, 80, 4) > 5:
    print('Super')








