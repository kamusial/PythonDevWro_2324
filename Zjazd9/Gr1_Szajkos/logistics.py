"""
Biedny rybak nie wie gdzie mieszkać :(
data/cities.txt to mapa terenu.
Literki to nazwy miast.
Musimy obliczyć, które 4 miasta rybak może najszybciej objechać,
żeby zużyć jak najmniej paliwa/czasu.

1. Parsowanie pliku. Utwórz obiekty klasy City, w których zawszesz jego współrzędne.
2. Klasa "Map". Metoda "distance" obliczy odległość między dwoma zadanymi miastami.
3. Używając city_map.distance(city_a, city_b) znajdź najkrótszą 'pętlę' 4 miast
"""
from logistics_utils.loader import load_cities, City


class Map:
    def distance(self, city_a: City, city_b: City):
        print(city_a.x)


if __name__ == '__main__':
    cities = load_cities("data/cities.txt")
    Map().distance(cities[0], cities[1])
