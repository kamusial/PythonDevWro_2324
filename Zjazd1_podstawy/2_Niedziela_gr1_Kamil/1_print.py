#program, który wita uzytkownika.
#czesc albo dzien dobry, zaleznie od wieku
#Sznaowny Panie albo Szanowna Pani - w zależnosci od płci

print('Wprowadz imie')
first_name = input()
age = int(input('Wprowadz wiek:   '))
gender = bool(int(input('Czy jesteś kobietą? Jeśli tak, napisz "1", jeśli nie - wpisz "0"')))

if age <= 18:
    print('Czesc', first_name, '.\nMasz', age, 'lat. Pelnoletni za', 18-age)  #złożony print, z nową linią
else:
    if gender:
        print(f'Szanowna Pani {first_name}, ma Pani {age} lat.')
    else:
        print(f'Szanowny Panie {first_name}, ma Pan {age} lat.')

if first_name[-1] == 'a':    #czy ostatnia litera imienia to "a"
    print('Twoje imie kończy się na "a", Witam Panią')
else:
    print('Twoje imie nie kończy się na "a", Witam Pana')





