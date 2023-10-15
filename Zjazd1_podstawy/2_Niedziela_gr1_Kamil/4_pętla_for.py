my_list = ['kotek', 'piesek', 'szynka', 'sąsiad', 'biurko', 'I jeszcze coś']

print('Pętla1')
for i in range(5):    #pętla 5 razy, i = 0-4
    print(f'interacja nr {i+1}, i ma wartość {i}')
    print(my_list[i]+my_list[i])

print('\npętla2')
for i in range(3, 17, 2):      #od, do, krok
    print(f'interacja nr {i + 1}, i ma wartość {i}')

print('\nPętla3')
print('dlugość listy:', len(my_list))
for i in range(len(my_list)):
    print(my_list[i])
    if len(my_list[i]) > 5:
        print('długie słowo\n...................................')

print('\nPętla4')
for i in my_list:
    print(i)
    if len(i) > 5:
        print('długie słowo\n...................................')

print('\nPętla5 - czy dane slowo jest w liście?')
word = 'mazurek'
for i in my_list:
    print(i)
    if len(i) > 5:
        print('długie słowo\n...................................')
