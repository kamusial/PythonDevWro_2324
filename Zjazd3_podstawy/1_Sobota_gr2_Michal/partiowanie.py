"""
Weź poniższą listę i 'pociachaj' ją na 4-elementowe kawałki
UWAGA: Ostatni 'kawałek' będzIe miał 3 elementy:
output = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11]]
lub
output = [(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11)]
"""
from more_itertools import batched

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
output = []
for i in range(0, len(a), 4):
    output.append(a[i:i + 4])
print(output)

print(list(batched(a, 4)))
