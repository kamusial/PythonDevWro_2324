#  znajdź parę liczb w zadanej liście, której suma wynosi 62
a = [253, 12, -2, 53, 9, 234, 123, -94, 29, 7]

n = 62

# 1 pętla for :)
for i in a:
    if n - i in a:
        print(f"{i} oraz {n-i} daja razem {n} :)")
        break

# prosto i zrozumiale:
for i in a:
    for j in a:
        if i + j == n:
            print(f"{i} oraz {j} daja razem {n} :)")
