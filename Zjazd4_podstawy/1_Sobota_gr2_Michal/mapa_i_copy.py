a = ["4", "6", "2"]

result = list(map(int, a))

"""
a[0] = f(a[0])
a[1] = f(a[1])
a[2] = f(a[2])
"""
print(a)
print(result)

"""kopia listy a:"""
b = list(map(lambda x: x, a))
"""ale lepiej"""
from copy import copy
b = copy(a)
"""jeszcze lepiej"""
b = a.copy()
