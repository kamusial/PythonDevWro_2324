"""
Napisz funkcję, która zwróci ilość powtarzających się już elementów.
W poniższej liście są 3 powtórki - 2, 2 i 15, więc:
output = 3
"""
a = [2, 4, 2, 2, 15, 16, 5, 15]


def czy_roznica(lista):
    return len(lista) - len(set(lista))


print(czy_roznica(a))
