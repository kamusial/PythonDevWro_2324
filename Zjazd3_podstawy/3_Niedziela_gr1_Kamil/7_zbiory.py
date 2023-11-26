special_characters = set(',./;\'[]')
print(special_characters)

passwd = input('Podaj haslo: ')

if len(set(passwd) & special_characters) > 0:
    print('ok, uzyty znak specjalny')
else:
    print('no nie ma')