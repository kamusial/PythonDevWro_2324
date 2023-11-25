import random

print(random.randint(4, 10))
print(len('mama') * 3)
print('....................')

slownik_zakupow = {
    'marchew': 4.5,
    'serek': 2.99,
    'margaryna': 7,
    'serek': 7,
    'maslo': 7
}

print(slownik_zakupow['marchew'])
print(3 * slownik_zakupow['marchew'] + 5 * slownik_zakupow['serek'])
slownik_zakupow['marchew'] = 3.99

lista_robocza = ['mama', 'tata', 'pies', 'mysz']
if 'pies' in lista_robocza:
    print('Tak')
else:
    print('nie')

x = int(input('x'))