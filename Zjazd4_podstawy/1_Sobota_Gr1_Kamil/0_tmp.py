print('string split')
my_string = 'Mama.kupila.psa'
splitted_string = my_string.split('.')
print(f'string przed podzialem: {my_string}')
print(f'string po podziale (dzielimy po kopce): {splitted_string}')

print('\nusuwanie znaków')
my_string = 'Mama.kupila.psa'
my_string = my_string.replace('.','')
print(f'string po usunięciu kropki: {my_string}')

print('\nFunkcje')
def after_a(text):
    return text[text.index('a')+1]

my_string = 'Mama.kupila.psa'
print(after_a(my_string))

print('\nZbiory')
zbior1 = {'.', ',', '(', '\'', '\"'}
zbior2 = set('.,(\'\"')
print(f'zbior1: {zbior1}')
print(f'zbior2: {zbior2}')


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