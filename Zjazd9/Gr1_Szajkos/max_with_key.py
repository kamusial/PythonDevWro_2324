
result = max([3, 457, 23, 567, 6, 34])   # 567


def negative(n):
    return -n


result = max([3, 457, 23, 567, 6, 34], key=negative)
print(result)

"""
3 -> negative(3) -> -3
457 -> negative(457) -> -457

max([-3, -457, -23, -567, -6, -34]) -> -3

-> 3
"""

result = max(["słowa", "myśli", "i", "by", "znowu", "budować"], key=len)
print(result)

"""
len("slowa")
len("mysli")
len("budować") = 7
"""