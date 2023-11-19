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