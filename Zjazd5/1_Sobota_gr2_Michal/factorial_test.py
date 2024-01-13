"""
5!
1*2*3*4*5
3!
1*2*3
-1!  XXX
0!
1
"""


class OutOfRangeError(Exception):
    ...


def factorial(n: int):
    if n < 0:
        raise OutOfRangeError(f"{n=} cannot be negative!")
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


from functools import reduce
from operator import mul


def fancy_factorial(n: int):
    return reduce(mul, range(1, n+1))


"""PYTEST
pytest odpala wszystkie foldery/pliki/klasy/funkcje zaczynające się od "test"
"""


def test_factorial():
    result = factorial(5)
    assert result == 120


def test_factorial_2():
    result = factorial(0)
    assert result == 1


def test_factorial_3():
    result = factorial(1)
    assert result == 1


def test_factorial_4():
    result = factorial(-1)
    assert result == 1
