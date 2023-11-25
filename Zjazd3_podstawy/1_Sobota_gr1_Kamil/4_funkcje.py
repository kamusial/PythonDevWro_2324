print(10 * 1.1)
print(10 * 1.1 * 10)
print(10 * 10 * 1.1)
print('.....................')
def mnozenie(x, y):
    result = round(x * y)
    return result

print(mnozenie(100, 1.1)  +   12)


def dzielenie(x, y):
    if y == 0:
        print(f'dzielenie przez 0, zwracam wartość 1')
        return 1
    else:
        return x / y

print(dzielenie(5, 0))