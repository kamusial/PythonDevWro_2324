user_dict = {
    'tf43ftf4344545fcf': ['Kamil', 'Musial', 26, 'mail@mail.com'],
    'Kamil': '124',
    'Kamil1': '234',
    'Kamil11': '765',
    'Kamil111': 'mama',
    'Kamil001': 'eee',
    'Rafcio': '876',
    'Betty': 'betty'
}

with open('C:\\Users\\vdi-student\\Desktop\\rozliczenie.csv', 'r') as plik1:
    content = plik1.read(5)  # przeczytaj 5 pierwszych bądź kolejnych znaków
    print(content)
    content = plik1.read(5)
    print(content)
    content = plik1.read(5)
    print(content)
    print(type(content))
