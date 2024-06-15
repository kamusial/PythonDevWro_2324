#iteracyjnie

def silnia_iter(n):
    s = 1
    for i in range(2, n+1):
        s *= i
    return s

def silnia_rekurencyjnie(n):
    if n > 1:
        return n*silnia_rekurencyjnie(n-1)
    return 1


def silnia_szybka(n): return n*silnia_szybka(n-1) if n > 1 else 1


print(silnia_iter(4))
