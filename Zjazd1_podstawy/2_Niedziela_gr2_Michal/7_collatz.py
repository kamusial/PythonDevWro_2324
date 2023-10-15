# jeżeli liczba jest parzysta:  podziel ją na 2
# jeżeli liczba jest nieparzysta: pomnóż ją razy 3 i dodaj 1
# wykonuj te operacje w kółko, aż dostaniesz 1
# przykład:
# 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

# zadanie: uruchom ten algorytm dla liczb 2-100
# wyprintuj, której z liczb 2-100 zajęło najwięcej kroków by dotrzeć do 1

def collatz_step(n):
    if n % 2 == 0:
        n = n // 2
    else:
        n = n * 3 + 1
    return n


def collatz_convergence(n):
    collatz_path = [n]
    while n != 1:
        n = collatz_step(n)
        collatz_path.append(n)
    return collatz_path


longest_path = 0
winning_numbers = [1]
for number in range(2, 101):
    collatz_path = collatz_convergence(number)
    collatz_steps_count = len(collatz_path) - 1
    if collatz_steps_count > longest_path:
        longest_path = collatz_steps_count
        winning_numbers = [collatz_path[0]]
    elif collatz_steps_count == longest_path:
        winning_numbers.append(collatz_path[0])

print(f"The highest amount of steps was: {longest_path} for numbers {winning_numbers}")
