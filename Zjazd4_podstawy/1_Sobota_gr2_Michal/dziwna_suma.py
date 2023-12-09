"""
1. Przemnóż wszystkie liczby z listy
2. Oblicz sumę cyfr z wyniku pkt 1
"""
from functools import reduce


a = [4, 2, 5, 7, 2, 3]

"""Rozwiązanie podstawowymi funkcjonalnościami pythona"""

result = 1
for number in a:
    result = result * number
print(result)

final_sum = 0
for digit in str(result):
    digit_as_int = int(digit)
    final_sum += digit_as_int
print(final_sum)


"""Rozwiązanie 'fancy'"""


def multiply(x, y):
    return x*y


result = reduce(multiply, a)

# ekwiwalent funkcji multiply:
result = reduce(lambda x, y: x*y, a)
print(result)


"""
result = multiply(a[0], a[1])
result = multiply(result, a[2])
result = multiply(result, a[3])
result = multiply(result, a[4])
...
"""

final_result = reduce(lambda x, y: x+y, [int(digit) for digit in str(result)])
print(final_result)
"""Ekwiwalent jako sum"""
final_result = sum([int(digit) for digit in str(result)])
print(final_result)

"""Ekwiwalent z mapą"""
final_result = sum(map(int, str(result)))
print(final_result)

"""GIGACHAD solution"""
print(sum(map(int, str(reduce(lambda x, y: x*y, a)))))
