dictionary = {
    "imie": "Michał",
    "nazwisko": "Szajn",
    "wiek": 32
}

print(dictionary)
print(list(dictionary.keys()))
print(list(dictionary.values()))
print(list(dictionary.items()))

for key, value in dictionary.items():
    print(f"Moje {key} to {value}")
