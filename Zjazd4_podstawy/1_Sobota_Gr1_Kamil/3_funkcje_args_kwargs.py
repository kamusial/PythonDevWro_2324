def my_function(a, b, c=1):
    if b > a:
        return b + c
    else:
        return a + c

print(my_function(3, 4))


def my_arg_function(*args):
    for arg in args:
        if arg > 0:
            print(f'{arg} * 2 to {arg * 2}')
        else:
            print(f' {arg} mniejsze od zera')

my_arg_function(3, 4, 5,-1, 2)
my_arg_function(1, 2)

def my_kwargs_funtion(**kwargs):
    if 'nazwisko' in kwargs and kwargs['nazwisko'] == 'Kowalski':
        print(f'Jesteś na liscie zablokowanych')

my_kwargs_funtion(imie='Kamil', status='wolny')

def draw_lines(x, y, *coordinates):
    start = [x, y]
    for i in range(0, len(coordinates), 2):
        print(f'Rysule linie z {start} do {coordinates[i]}, {coordinates[i+1]}')
        start = [coordinates[i], coordinates[i+1]]

def triangle(**data):
    if 'a' in data.keys() and 'b' in data.keys() and 'c' in data.keys():
        print(f'Liczę pole z 3 bokow')
    elif 'a' in data.keys() and 'b' in data.keys() and 'alpha' in data.keys():
        print(f'Liczę pole z 2 bokow i kata')
    elif 'a' in data.keys() and 'alpha' in data.keys() and 'beta' in data.keys():
        print(f'Liczę pole z boku i 2 katów')
    elif 'a' in data.keys() and 'h' in data.keys():
        print(f'Liczę pole z podstawy i wysokosci')
    else:
        print('no nie da sie')

triangle(a=5, alpha=43, beta=23)

#draw_lines(1, 1, 5, 6, 87, 3, 23, 1, 7, 6)


login_database = ['Kamilxxx', 'Marzenka78', 'Danio1', 'Dixi']

def check_logins(*logins):
    available_login_list = []
    for login in logins:
        if login not in login_database:
            print(f'Login {login} jest dostepny')
            available_login_list.append(login)
    return available_login_list

print(check_logins('Kamil', 'Kamilxxx', 'Daniel', 'Dixi', 'Kasia'))
triangle()

def final_function(b, a=1, c=0):
    return a + b + c

print(final_function(3, 4))

def final2(a, b, *rest, c=1, **kwargs):
    return True

final2(3, 4, 5, 6, 7, 8, c=1, imie='Kamil', nazwisko='Kowalski')