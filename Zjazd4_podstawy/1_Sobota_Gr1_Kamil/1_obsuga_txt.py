# program sprawdza, ile jest słów, ile różnych słów i ile razy słowa się powtarzają

with open('u2.txt', 'r', encoding='utf8') as file1:
    content = file1.read()
print(type(content))
print(len(content))


