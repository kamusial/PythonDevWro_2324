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


