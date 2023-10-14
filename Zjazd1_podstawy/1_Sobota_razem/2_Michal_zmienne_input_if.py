print("Powiedz czy jestes fajny (tak/nie)")
stan = input()


if stan == "tak":
    uzytkownik_jest_fajny = True
else:
    uzytkownik_jest_fajny = False


if uzytkownik_jest_fajny:
    print("Super że jesteś z nami")
else:
    print("A to idz sobie")
    print("Nie lubimy Cie")

#  = to jest operator przypisania
#    a = 5
#   nazwa worka  =  zawartość worka

#  ==  operator porównania     >   <   >=  <=  !=
#  operatory logiczne:  not, or, and
#  not a - odwrócenie - True -> False  i  False -> True
#  a or b - jeśli chociaż 1 ze stron to prawda, zwraca prawdę
#  a and b - zwraca prawdę TYLKO jeśli obie strony są prawdą
