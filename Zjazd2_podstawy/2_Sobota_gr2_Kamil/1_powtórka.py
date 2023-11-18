a = 5
b = 7.4
c = 'mama'
d_lista = [1, 2, 3, 5.5, 'mama', '54']

print(a * d_lista[5])
print(c[2])

if c == 'tata':
    print('Czesc tata')
elif c == 'mama' and d_lista[2] > 0:
    print(f'Nasze slowo to {c}')
    print('Nasze slowo to',c)
else:
    print('No nic nie pasuje')

for i in range(3, 25, 4):
    print(i)

for i in range(100, -1, -10):
    print(i)

while (a < 10):
    print(f'a wynosi {a}')
    a += 3

# while True:
#     wiek = int(input('Ile masz lat? '))
#     if wiek >= 18:
#         break
#     else:
#         print('zly wiek, sprobuj jeszcze raz')
#
# print('Dalsza czesac programu')

moj_string = 'to jest moj string'

print(moj_string[3:13:2])
print(moj_string[::-1])
moj_string = moj_string.replace(' ', '')

my_list = [1, 2, 3, 4]
print(len(my_list) * 5)