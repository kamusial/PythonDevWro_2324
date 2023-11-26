# dany jest spis uzytkowników i ich haseł
# program pozwala dodać użytkownika do bazy
# program sprawdza, czy nazwa uzytkownika jest wolna
# jeśli nazwa zajęta, program proponuje własną nazwę

from funkcje_5 import *

new_user = input('Podaj nazwe uzytkownika: ')
if not username_available(new_user):
    print('Użytkownik rozpoznany')
    if login_successful(new_user):
        print('dalsza czesc programu')
    else:
        exit()
else:
    add_user(new_user)
print(users_database)