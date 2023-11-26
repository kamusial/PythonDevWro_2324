# załóżmy, że pesel ma 4 cyfry
# stwórzmy zbiór NFZ – ludzie, w bazie pacjentów NFZ
# stwórzmy zbiór chorzy_rok – ludzie chorzy w ostatnim roku
# stwórzmy zbiór chorzy_miesiac – ludzie chorzy w ostatnim miesiącu
# stwórzmy zbiór centrum – wszystkich ludzi mieszkających na bemowie
# stwórzmy zbiór krzyki – wszystkich ludzi mieszkających na zoliborzu

NFZ = {1234, 3476, 4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243, 6435, 1298, 6732, 7688, 7648, 2345, 2356}
chorzy_rok = set([1234, 3476, 4544, 3423, 3254, 8769, 5436])
chorzy_miesiac = set([1234, 3476, 3098, 4544, 3423])
centrum = {4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243}
krzyki = {7648, 2345, 2356, 3987, 1234, 3476, 3254}
zbior_pusty = set()

# suma zbiorów ->              |
# cześć wspólna zbiorów   ->   &
# różnica zbiorów  ->          -
# różnica symetryczna  ->      ^


# sprawdźmy, ile osób chorowało w ostatnim roku w centrum
print(f'Chorzy w ostatnim roku w centrum to {chorzy_rok & centrum}')
print(f'Liczba: {len(chorzy_rok & centrum)}\n')

# Ile osób z centrum chorowło w ostatnim roku?
print(f'Chorzy z centrum w ostatnio roku to: {centrum & chorzy_rok}')
print(f'Liczba: {len(centrum & chorzy_rok)}\n')

#            Sprawdźmy poprawność danych
# każdy, kto chorował w ostatnim miesiącu, powinien jednocześnie chorować w ostatnim roku
print(f'Ludzie chorujący w ostatnim miesiącu i NIEchorujący w ostatnim roku: {chorzy_miesiac <= chorzy_rok}')
print(f'Liczba: {chorzy_miesiac - chorzy_rok}')
if len(chorzy_miesiac - chorzy_rok) == 0:
    print('ok')

# nikt nie powinien mieszkać jednoczeście w centrum i na krzykach
# jeśli są tacy, trzeba usunąć
print(f'Ludzie mieszkający jednocześnie w centrum i na krzykach: {centrum & krzyki}')
print(f'Liczba: {len(centrum & krzyki)}')
if len(centrum & krzyki) > 0:
    decision = input('skad usuwamy? K/C ')
    if decision.upper() == 'C':
        centrum = centrum - (centrum & krzyki)
    elif decision.upper() == 'K':
        krzyki -= centrum
    else:
        for pesel in centrum & krzyki:
            centrum.remove(pesel)

# każdy: chory, zdrowy, z centeum i z krzyków, powinien być w bazie NFZ. Jeśli nie ma, trzeba dopisać)