def welcome(imie, wiek, plec):
    if wiek <= 20:
        print(f'cześć {imie}')
    else:
        print(f'Dzień dobry {imie}')


username = input('podaj imie: ')
age = int(input('podaj wiek: '))

welcome(username, age)


welcome('Kamil', 23)

# import random
# lista_imion = ['Kamil', 'Olena', 'Gosia']
# welcome(lista_imion[1], random.randint(12, 30))
