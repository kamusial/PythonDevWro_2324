#funcja, która przyjmuje wiek auta, liczbe szkód, wiek kierowcy
#funkcja mówi ile będzie kosztować skłądka na ubezpieczenie

def wysokosc_skladki(wiek_auta, liczba_szkod, wiek_kierowcy):
    skladka = 0
    skladka += wiek_auta * 20
    skladka += liczba_szkod * 200
    if wiek_kierowcy < 25:
        skladka += 100
#    print(f'skladka wynosi {skladka}')
    return skladka


skladka = wysokosc_skladki(10, 2, 30)
czynsz = 500
jedzenie = 700
koszt_zycia = czynsz + jedzenie + skladka
print(f'koszty zycia to: {koszt_zycia}, a tym skladka to: {skladka}')
print('...................')

imie = 'Oliwia'
if len(imie) > 5:
    print(f'{imie} - masz dlugie imie')
else:
    print('Masz krotkie imie')

if wysokosc_skladki(10, 2, 55) > 1000:
    print('Nie stac Cie')
else:
    print('skladka akceptowalna')

wiek_auta = int(input('Ile twoja fura ma lat? '))
liczba_szkod = int(input('ile razy rozwaliles auto? '))
wiek = int(input('Ile lat ma kierowca?: '))
if wysokosc_skladki(wiek_auta, liczba_szkod, wiek) > 1000:
    print('Nie stac Cie')
else:
    print('skladka akceptowalna')