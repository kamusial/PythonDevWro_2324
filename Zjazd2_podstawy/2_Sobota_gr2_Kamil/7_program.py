# dana jest baza użytkowników z hasłami
# program pozwala na dodanie uzytkownika oraz zmianę hasła
# program sprawdza, czy nazwa uzytkownika dostępna
# program wymaga dwukrotnego wprowadzenia hasła przy dodawaniu nowego uzytkownika
# program pyta, czy zakończyć, czy kontynuować dodawanie uzytkowników

# w przypadku niedostepnej nazwy uzytkownika, program proponuje nazwę
# program sprawdza poziom skomplikowania hasła

from funkcje_do_programu import *
username = input('Podaj uzytkownika: ')
while True:
    if is_user_available(username):
        add_user(username)
        break
    else:
        print(f'Sugeruje nazwę {suggest_username(username)}')
        decision = input('Chcesz wprowadzić inną nazwę (N), czy skorzystać z zaproponowanej nazwy (P)? ')
        if decision == 'P':
            username = suggest_username(username)
        else:
            username = input('Podaj nowa nazwe uzytkownika')
print(user_dict)


