def add_user(username):
    while True:
        passwd1 = input('Podaj haslo: ')
        passwd2 = input('Powtorz haslo haslo: ')
        if passwd1 == passwd2:
            users_database[username] = passwd1
            break
        else:
            print('Hasła nie pasują, jeszcze raz')


def login_successful(username):
    passwd = input('Podaj haslo: ')
    if passwd == users_database[username]:
        print('Haslo poprawne')
        return True
    else:
        print('Haslo niepoprawne')
        return False

def username_available(username):
    if username not in users_database:
        return True
    else:
        return False


users_database = {
    'Kamil': '123',
    'Oliwia': 'Oliwia123',
    'Patixxd': 'Pati1',
    'Gosia': 'dej_mi_haslo'
}