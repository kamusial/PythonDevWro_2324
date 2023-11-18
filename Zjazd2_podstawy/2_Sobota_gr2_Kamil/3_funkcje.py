def przywitanie1():
    print('Siema')
    print('format dysku D')

def przywianie2(imie):
    print(f'siema {imie[::-1]}')

def przywitanie3(imie, wiek):
    if wiek < 18:
        print('Siema')
    else:
        print(f'dzien dobry {imie}')

a = 2
zmienna = 'Diana'
if a > 3:
    przywitanie1()
else:
    przywianie2(zmienna)

przywitanie3('Kamil', 122)