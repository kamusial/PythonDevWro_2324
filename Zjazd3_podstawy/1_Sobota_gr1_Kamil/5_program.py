# dany jest spis uzytkowników i ich haseł
# program pozwala dodać użytkownika do bazy
# program sprawdza, czy nazwa uzytkownika jes wolna
# jeśli nazwa zajęta, program proponuje własną nazwę

def add_user(username):
    while True:
        passwd1 = input('Podaj haslo: ')
        passwd2 = input('Powtorz haslo haslo: ')
        if passwd1 == passwd2:
            users_database[username] = passwd1
            break
        else:
            print('Hasła nie pasują, jeszcze raz')



users_database = {
    'Kamil': '123',
    'Oliwia': 'Oliwia123',
    'Patixxd': 'Pati1'
}




new_user = input('Podaj nazwe uzytkownika: ')
if new_user not in users_database:

    while True:
        passwd1 = input('Podaj haslo: ')
        passwd2 = input('Powtorz haslo haslo: ')
        if passwd1 == passwd2:
            users_database[new_user] = passwd1
            break
        else:
            print('Hasła nie pasują, jeszcze raz')

else:
    print('Nazwa zajeta')

print(users_database)