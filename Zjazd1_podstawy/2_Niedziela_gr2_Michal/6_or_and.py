maturity_in_cookies = True
birth_date_given = False
user_logged_in = False
pesel_given = False

conditions = [
    maturity_in_cookies,
    birth_date_given,
    user_logged_in,
    pesel_given
]

if any(conditions) is True:
    pass

maturity_given_manually = birth_date_given or pesel_given
maturity_read_automatically = maturity_in_cookies or user_logged_in


if maturity_read_automatically or maturity_given_manually:
    pass

# math
a = 5 in list(range(1000000))
b = -5 in list(range(1000000))
c = 2 in list(range(1000000))

if a or b and not c:
    pass
