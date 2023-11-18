user_dict = {
    'majki': '123',
    'Kamil': '124',
    'Kamil1': '234',
    'Kamil11': '765',
    'Kamil111': 'mama',
    'Kamil001': 'eee',
    'Rafcio': '876',
    'Betty': 'betty'
}
def is_user_available(user):
    if user not in user_dict.keys():
        print(f'Nazwa {user} dozwolna')
        return True
    else:
        print(f'Nazwa {user} NIEdozwolona')
        return False

def add_user(user):
    while True:
        passwd1 = input('Podaj haslo: ')
        passwd2 = input('Potwierdź haslo: ')
        if passwd1 == passwd2 and passwd_has_CAP_small_letter(passwd1):
            user_dict[user] = passwd1
            break
        else:
            print('Zle, jeszcze raz')


def suggest_username(user):
    return user + '1'


def passwd_has_CAP_small_letter(passwd):
    if passwd != passwd.lower() and passwd != passwd.upper():
        print('Haslo posiada duza i mala litera')
        return True
    print('Haslo NIE posiada duzej lub malej litery')
    return False
