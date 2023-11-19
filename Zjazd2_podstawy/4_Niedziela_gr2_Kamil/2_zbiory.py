# załóżmy, że pesel ma 4 cyfry
# stwórzmy zbiór NFZ – ludzie, w bazie pacjentów NFZ
# stwórzmy zbiór chorzy_rok – ludzie chorzy w ostatnim roku
# stwórzmy zbiór chorzy_miesiac – ludzie chorzy w ostatnim miesiącu
# stwórzmy zbiór bemowo – wszystkich ludzi mieszkających na bemowie
# stwórzmy zbiór zoliborz – wszystkich ludzi mieszkających na zoliborzu

NFZ = {1234, 3476, 4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243, 6435, 1298, 6732, 7688, 7648, 2345, 2356}
chorzy_rok = set([1234, 3476, 4544, 3423, 3254, 8769, 5436])
chorzy_miesiac = set([1234, 3476, 3098, 4544, 3423])
bemowo = {4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243}
zoliborz = {7648, 2345, 2356, 3987, 1234, 3476, 3254}
zbior_pusty = set()

#suma zbiorów ->   |
# cześć wspólna zbiorów