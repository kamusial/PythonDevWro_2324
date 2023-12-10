import httpx

print("robie sobie rzeczy")
x = 46 / 3
print("dalej robie sobie rzeczy")
try:
    y = 63 / 0
except ZeroDivisionError:
    print("chopie, przez zero sie nie dzieli")
except httpx.TimeoutException:
    print("URL nie odpowiada, spróbuj później")
else:
    print("KOD W SEKCJI 'try' NIE WYRZUCIŁ ŻADNEGO WYJĄTKU :)")
finally:
    print("ZAWSZE SIĘ WYPRINTUJĘ NA KONIEC")

print("chyba tej rzeczy już nie robie")
z = 3 + 56
print("koniec 'programu' xD")
