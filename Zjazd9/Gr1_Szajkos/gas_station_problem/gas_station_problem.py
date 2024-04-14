"""
Kończy nam sie paliwo :(
Starczy nam go na przejechanie obok następnych 100 stacji.
Obieramy strategię, by zatrzymać się przy najlepszej z tych 100.
1. Przejeżdżamy przez N stacji, i zapamiętujemy najładniejszą/najlepszą.
2. Przez pozostałe 100-N stacji przejeżdżamy i zatrzymujemy się przy pierwszej lepszej niż N stacji z pkt 1.
3. Jakie jest najoptymalniejsze N, żeby zmaksymalizować szansę na zatrzymanie się przy najlepszej stacji?

Implementacja:
1. funkcja gas_stations(n) produkuje listę n stacji z losową oceną od 0 do 10000.
2. funkcja set_standards(stations, n) zwraca ocenę najlepszej z pierwszych n stacji.
3. funkcja stop_at_best_station(stations, start, min_rank) zwraca stację przy której się zatrzymujemy
Jeśli przejechaliśmy przez wszystkie stacje, funkcja zwróci None.
"""
import random
from dataclasses import dataclass
from typing import Optional
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter


@dataclass
class GasStation:
    rank: int
    id: int

    def __repr__(self):
        return f"Station *{self.rank}*"


def generate_gas_stations(n: int) -> list[GasStation]:
    stations = []
    for i in range(n):
        rank = random.randint(0, 10000)
        station = GasStation(rank, i)
        stations.append(station)
    return stations


def set_standards(stations: list[GasStation], n: int) -> int:
    if n == 0:
        return 0
    first_n_stations = stations[:n]
    best_station = max(first_n_stations, key=lambda station: station.rank)
    return best_station.rank


def stop_at_best_station(stations: list[GasStation], start: int, min_rank: int) -> Optional[GasStation]:
    for station in stations[start:]:
        if station.rank > min_rank:
            return station
    return None


def get_best_station(stations: list[GasStation]) -> GasStation:
    return max(stations, key=lambda station: station.rank)


def found_best_gas_station_simulation(n_stations: int, n: int) -> bool:
    stations = generate_gas_stations(n_stations)
    my_standard = set_standards(stations, n)
    stopped_at = stop_at_best_station(stations, n, my_standard)
    best = get_best_station(stations)
    return stopped_at == best


def get_success_chance(n_stations: int, n: int) -> float:
    successes = 0
    for _ in range(10000):
        best_station_found = found_best_gas_station_simulation(n_stations, n)
        successes += best_station_found
    return successes / 10000


def main():
    x = range(101)
    y = []
    for i in x:
        success_chance = get_success_chance(100, i)
        y.append(success_chance)
        print(i, success_chance*100)
    _, ax = plt.subplots()
    ax.plot(x, y)
    ax.yaxis.set_major_formatter(PercentFormatter())
    ax.grid()
    plt.show()


if __name__ == '__main__':
    main()
