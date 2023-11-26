with open('rozliczenie.csv', 'r') as file1:
    content = file1.readlines()
print(content)

for i in range(len(content)):
    content[i] = content[i].split(',')
print(content)
print(content[3])
print(content[3][2])

# oblicz średnią wypłatę
# oblicz liczbę kobiet na macierzynskim