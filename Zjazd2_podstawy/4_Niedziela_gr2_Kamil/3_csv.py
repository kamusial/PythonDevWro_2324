with open('C:\\Users\\vdi-student\\Desktop\\rozliczenie.csv', 'r') as plik1:
    content = plik1.readlines()
print(content)

# przygotowanie danych
for i in range(len(content)):
    content[i] = content[i].split(',')
print(content)
print(content[3])
print(content[3][2])

# obliczanie średniej wypłaty
total = 0
for line in content[1:]:
    total += int(line[1])
print(f'srednia {round(total/(len(content)-1),2)}')

# Obliczenie liczby kobiet na macierzynskim
count = 0
for line in content[1:]:

    if line[3].lower() == 'k' and line[4][0].lower() == 't':
        count += 1
print(f'Liczba: {count}')

with open('newfile.txt', 'a') as plik1:   #w - nadpisz   a - dopisz
    plik1.write('Text')