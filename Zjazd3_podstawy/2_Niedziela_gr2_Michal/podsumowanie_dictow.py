dictionary = {
    "key": "value",
    "key2": "value2",
    "key3": "value"
}

# porównanie do seta:
a_set = {"value", "value2", "value3"}

# inicjalizacjia:
empty_dict = {}
empty_set = set()

# znamy 'key' i chcemy value:
print(dictionary["key"])

# znamy 'value' i chcemy key:
list_of_matching_keys = []
for key in dictionary:
    if dictionary[key] == "value":
        list_of_matching_keys.append(key)
print(list_of_matching_keys)

# znamy 'value' i chcemy key part 2:
list_of_matching_keys = []
for key, value in dictionary.items():
    if value == "value":
        list_of_matching_keys.append(key)
print(list_of_matching_keys)

# porównanie z listą
for key, value in dictionary.items():
    print(key, value)

for index, value in enumerate(["a", "bedzie", "json?"]):
    print(index, value)
