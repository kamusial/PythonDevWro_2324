import json

ACCOUNTS = {
    "asia": 10,
    "basia": 20,
    "pawel": 30
}

NICE_LIST = [10, 20, 30]


print(NICE_LIST[1])
print(ACCOUNTS["basia"])

# Print słownika - domyślny i "uładniony"
print(ACCOUNTS)
print(json.dumps(ACCOUNTS, indent=4))
