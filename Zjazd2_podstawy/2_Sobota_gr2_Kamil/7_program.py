# dana jest baza użytkowników z hasłami
# program pozwala na dodanie uzytkownika oraz zmianę hasła
# program sprawdza, czy nazwa uzytkownika dostępna
# program wymaga dwukrotnego wprowadzenia hasła przy dodawaniu nowego uzytkownika
# program pyta, czy zakończyć, czy kontynuować dodawanie uzytkowników

# w przypadku niedostepnej nazwy uzytkownika, program proponuje nazwę
# program sprawdza poziom skomplikowania hasła

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
        if passwd1 == passwd2:
            user_dict[user] = passwd1
            break
        else:
            print('hasla nie pasuja, jeszcze raz')


def suggest_username(user):
    return user + '1'


username = input('Podaj uzytkownika: ')
if is_user_available(username):
    add_user(username)
else:
    print(f'Sugeruje nazwę {suggest_username(username)}')
    decision = input('Chcesz wprowadzić inną nazwę (N), czy skorzystać z zaproponowanej nazwy (P)? ')


