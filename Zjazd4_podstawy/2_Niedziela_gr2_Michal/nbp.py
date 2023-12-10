"""
Używając https://api.nbp.pl/en.html
pobierz i wyprintuj ostatni kurs wybranej waluty.
"""
import httpx

waluta = input("Jaka waluta Cię interesuje? (np. EUR, USD, JPY): ")
data = input("Z kiedy chcesz kurs? (yyyy-mm-dd): ")


response = httpx.get(f"https://api.nbp.pl/api/exchangerates/rates/a/{waluta}/{data}/")
rate_dict = response.json()["rates"][0]
print(f"Kurs: {rate_dict["mid"]} PLN")

"""
Zadanie domowe:
przy response.json() zrób sekcję try: except:
złap odpowiedni wyjątek, i spróbuj httpx.get ponownie z datą poprzedzającą.
PROBLEMY :(  :
1. datetime - obliczenie daty poprzedzającej
2. rekurencja
"""
