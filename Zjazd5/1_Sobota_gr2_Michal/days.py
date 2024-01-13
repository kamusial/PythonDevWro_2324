"""
Wyprintuj datę która była 10000 dni temu.
"""
from datetime import datetime, timedelta


now = datetime.today()
long_time_ago = now - timedelta(days=10000)

"""
Liczba numerologiczna:
1992-02-15:
1+9+9+2 + 0+2 + 1+5   =  29
29:
2+9 = 11
11:
1+1 = 2

Oblicz cyfrę numerologiczną dla osoby urodzonej 10000 dni temu.
"""
number = str(long_time_ago.date()).replace("-", "")
print(long_time_ago.strftime("%Y%m%d"))


while len(str(number)) > 1:
    number = sum(map(int, list(str(number))))


def get_digit_sum(number: int) -> int:
    if number <= 9:
        return number
    else:
        digit_sum = sum(map(int, list(str(number))))
        return get_digit_sum(digit_sum)


print(get_digit_sum(19920215))
