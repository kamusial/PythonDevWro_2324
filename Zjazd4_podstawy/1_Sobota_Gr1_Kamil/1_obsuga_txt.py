# program sprawdza, ile jest słów, ile różnych słów i ile razy słowa się powtarzają

from functions import *

content = read_file('u2.txt')
content = clear_text(content)
print(f'Liczba slow: {no_of_words(content)}')
print(f'liczba roznych slow: {no_of_unique_words(content)}')
