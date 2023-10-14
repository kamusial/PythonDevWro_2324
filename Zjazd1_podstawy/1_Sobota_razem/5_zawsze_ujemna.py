#  input: liczba calkowita
#  output: printuje tą liczbę w postaci ujemnej

number = int(input("Type an integer: "))

#  rozwiazanie z if

if number > 0:
    output = -number
else:
    output = number

print(output)

#  rozwiazanie z abs

output = -abs(number)

print(output)
