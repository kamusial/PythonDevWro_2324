"""
5!
1*2*3*4*5
3!
1*2*3
-1!  XXX
0!
1
"""
import pytest


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


@pytest.mark.parametrize("factorial_input, expected_output",
                         [
                             (3, 6),
                             (5, 120),
                             (0, 1),
                             (1, 1),
                             (10, 3628800)
                         ]
                         )
def test_factorial(factorial_input: int, expected_output: int):
    result = factorial(factorial_input)
    assert result == expected_output


def test_factorial_negative():
    with pytest.raises(OutOfRangeError):
        factorial(-1)

    # Ekwiwalent wbudowanymi funkcjonalnościami pythona:
    # try:
    #     factorial(-1)
    # except OutOfRangeError:
    #     pass
    # else:
    #     raise AssertionError("Passing negative number to factorial did not raise an exception")
