"""
Napisz funkcję przyjmującą użytkownika (np. remigiusz) i zwracającą
stan konta.
"""

NAMES = {
    2356354: "eugeniusz",
    8936743: "tymoteusz",
    2389654: "remigiusz"
}

BALANCE = {
    2356354: 3200,
    8936743: 5100,
    2389654: 60
}


def get_username_balance(searched_username: str) -> int:
    for user_id, username in NAMES.items():
        if username == searched_username:
            return BALANCE[user_id]


balance = get_username_balance("tymoteusz")
nothing = None