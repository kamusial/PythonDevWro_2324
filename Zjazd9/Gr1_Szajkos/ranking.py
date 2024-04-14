"""
1. Załaduj data/ranking.json
2. Wyłoń zwycięzcę
3. Kto ma najdłuższe imię i nazwisko?
4. Wyłoń podium
"""
import json


def load_json(filepath):
    with open(filepath) as file:
        return json.load(file)


def find_winner(ranking):
    winner = max(ranking, key=lambda x: ranking[x])
    return winner


def longest_name(ranking):
    longest_name = max(ranking, key=len)
    return longest_name


def podium(ranking: dict):
    ranking_sorted = sorted(ranking, key=lambda x: ranking[x], reverse=True)
    return ranking_sorted[:3]


if __name__ == '__main__':
    ranking = load_json("data/ranking.json")
    print(find_winner(ranking))
    print(longest_name(ranking))
    print(podium(ranking))
