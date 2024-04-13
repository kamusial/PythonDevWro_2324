"""
3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
Znajdź liczbę w przedziale 1-100, której 'zajmie' najwięcej kroków by dotrzeć do 1.
"""


def collatz_iteration(n: int) -> int:
    """If n is even -> divide by 2.
    If n is odd -> multiply by 3 and add 1"""
    if n % 2 == 0:
        return n // 2
    return n * 3 + 1


def collatz_conjecture(n: int) -> list[int]:
    steps = [n]
    while n != 1:
        n = collatz_iteration(n)
        steps.append(n)
    return steps


def collatz_conjecture_steps(n: int):
    return len(collatz_conjecture(n))


def max_collatz_steps_in_range_1_to_100() -> tuple[int, int]:
    """Calculate amount of collatz conjecture steps for n from 1 to 100
    Return n which took the most steps to reach 1
    """
    collatz_dict = {}
    for n in range(1, 101):
        collatz_dict[n] = collatz_conjecture_steps(n)
    return max(collatz_dict.items(), key=lambda item: item[1])


if __name__ == '__main__':
    result = max_collatz_steps_in_range_1_to_100()
    print(result)
