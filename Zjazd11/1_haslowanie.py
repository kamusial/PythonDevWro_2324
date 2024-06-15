import keyring


with open('dane.csv', 'r') as plik1:
    content = plik1.readlines()
print(content)

for i in range(len(content)):
    content[i] = content[i].replace('\n','')
    content[i] = content[i].split(';')
print(content[1][1])
print(content)

# zapis hasła, usunięcie i odzyskanie
for i in range(len(content)):
    keyring.set_password(content[i][0], content[i][1], content[i][2])
    del content[i][2]
print('Dane bez hasel\n', content)

for i in range(len(content)):
    content[i].append(keyring.get_password(content[i][0], content[i][1]))
print(content)
