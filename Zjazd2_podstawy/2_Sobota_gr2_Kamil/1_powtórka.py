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
else:
    print('No nic nie pasuje')
