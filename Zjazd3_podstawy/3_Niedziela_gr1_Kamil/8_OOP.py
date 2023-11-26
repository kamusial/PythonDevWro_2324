class Auto:
    def __init__(self, kolor, b, wiek):
        self.kolor = kolor
        self.ilosc_paliwa = 10
        self.kondycja = b * 2
        self.tryb_ekonomiczny = False
        self.spalanie_na_100 = 14
        self.rocznik = 2023 - wiek

    def zasieg(self):
        zasieg = self.ilosc_paliwa / self.spalanie_na_100 * 100 * 0.9
        return round(zasieg)

auto1 = Auto('red', 2, 2)
auto2 = Auto('white', 4, 4)
auto_sasiada = Auto('black', 1, 12)
print(auto1.kolor)
auto1.kolor = 'blue'
print(auto1.kolor)
if auto2.ilosc_paliwa > 5:
    auto_sasiada.kondycja += 1

print(auto_sasiada.zasieg())