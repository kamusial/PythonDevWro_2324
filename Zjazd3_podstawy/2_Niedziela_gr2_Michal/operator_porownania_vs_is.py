"""
== to operator porównania wartości 2 zmiennych
is to operator porównania adresu w pamięci 2 zmiennych

is używamy do:
booli, None'a
ORAZ w przypadku kiedy FAKTYCZNIE zależy nam na sprawdzeniu,
że porównujemy TEN SAM obiekt
"""
a = "napis"
b = "napis"

print(a == b)
print(a is b)

c = [1, 2, 3]
d = [1, 2, 3]
print(c == d)
print(c is d)

t = 257
y = 257
print(id(t), id(y))
