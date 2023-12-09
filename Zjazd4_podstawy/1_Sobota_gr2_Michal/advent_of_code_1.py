"""1. Znajdź pierwszą cyfrę od lewej i od prawej zadanego napisu
2. Połącz tak znalezione 2 cyfry w liczbę 2-cyfrową."""
from more_itertools import first
from pathlib import Path


def get_2_digit_number(string: str) -> int:
    digits = []
    for char in string:
        if char.isdigit():
            digits.append(char)
    return int(digits[0] + digits[-1])


def get_2_digit_number_2(string: str) -> int:
    digit_1 = first(char for char in string if char.isdigit())
    digit_2 = first(char for char in reversed(string) if char.isdigit())
    return int(digit_1 + digit_2)


advent_txt = Path(__file__).parent / "advent_1.txt"
lines = open(advent_txt).readlines()
result = sum(map(get_2_digit_number, lines))
print(result)
