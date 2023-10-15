# jeżeli liczba jest parzysta:  podziel ją na 2
# jeżeli liczba jest nieparzysta: pomnóż ją razy 3 i dodaj 1
# wykonuj te operacje w kółko, aż dostaniesz 1
# przykład:
# 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

# zadanie: uruchom ten algorytm dla liczb 2-100
# wyprintuj, której z liczb 2-100 zajęło najwięcej kroków by dotrzeć do 1


number = 3
if number % 2 == 0:
    number = number // 2
else:
    number = number * 3 + 1
print(number)
