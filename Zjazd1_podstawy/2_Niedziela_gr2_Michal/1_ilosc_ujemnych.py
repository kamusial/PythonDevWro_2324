numbers = [24, 12, 67, 3, -1, 67, -23, -78]

# policz liczby ujemne z listy powyżej. Wyprintuj ich ilość.
# w pycharmie: ctrl+alt+l - auto poprawa estetyki składni

# list comprehension
negative_numbers = [number
                    for number in numbers
                    if number < 0]
print(len(negative_numbers))

# normalna pętla for
negative_numbers = []
for number in numbers:
    if number < 0:
        negative_numbers.append(abs(number))
print(len(negative_numbers))
