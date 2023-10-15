#  Oblicz (eksperymentalnie) prawdopodobieństwo wyrzucenia min. 1 szóstki
#  rzutem 3 kostkami k6
import random

# print(list(range(1, 11)))

# rzuć kostką 3 razy i sprawdź czy jest conajmniej 1 szóstka!
total_rolls = 100000

# flexowe rozwiązanie any + list comprehension
success_count = 0

for i in range(total_rolls):
    success_count += any([random.randint(1, 6) == 6
                          for _ in range(3)])

prawdop = 100 * success_count / total_rolls
print(f'Prawdopodobienstwo wynosi {prawdop}%.')

# normalne, prawidłowe rozwiązanie:
count = 0
ileok = 0

for i in range(1000):
    for j in range(3):
        if random.randint(1, 6) == 6:
            count += 1
    if count != 0:
        ileok += 1
    count = 0
prawdop = 100 * ileok / 1000
print(f'Prawdopodobienstwo wynosi {prawdop}%.')
