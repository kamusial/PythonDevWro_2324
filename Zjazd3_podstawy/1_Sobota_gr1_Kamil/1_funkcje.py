def przywitaj():
    print('.................')
    print('Witamy na spotkaniu')
    print('plik z logami uaktualniony')


def przywitaj_spersonalizowane1(x):
    print('Siema ',x)
    print(f'Siema {x}')

while True:
    decision = input('Czy przywitać? T/N ')
    if decision.lower() == 't':
        przywitaj()
    else:
        print('Brak przywitania')
        break

imie = input('Podaj imie: ')
przywitaj_spersonalizowane1(imie)
print('................')
przywitaj_spersonalizowane1('Erwina')

