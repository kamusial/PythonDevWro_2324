print("")


def collatz_step(number):
    if number % 2 == 0:
        number = number // 2
    else:
        number = number * 3 + 1
    return number


x = collatz_step(3)
print(x)
y = collatz_step(x)
print(y)
