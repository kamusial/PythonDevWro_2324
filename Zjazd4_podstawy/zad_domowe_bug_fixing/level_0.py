"""
Funkcja get_even powinna zwrócić listę z samymi parzystymi liczbami z podanej listy.
Niestety coś poszło nie tak XD
Bonus pkt za zastąpienie 'is_even' lambdą.
"""


def is_even(x: int) -> bool:
    return x % 2 == True


def get_even(numbers: list[int]) -> list[int]:
    return list(filter(is_even, numbers))


if __name__ == '__main__':
    even_numbers = get_even([52, 5243, 23, -5, 6, 7, 3254])
    assert even_numbers == [52, 6, 3254], f"{even_numbers=} are not expected even numbers from the list :("
