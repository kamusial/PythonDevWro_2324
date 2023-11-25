class Account:
    def __init__(self, currency):
        self.currency = currency

    def get_rate(self, other_currency):
        # internet.get(self.currency VS other_currency)
        pass


class PolishAccount:

    @staticmethod
    def get_rate():
        # internet.get(PLN VS other_currency)
        pass


class Crocodile:
    tail = True
    limbs = 4
    wiki_link = ""

    # dunder method (double underscore method)
    def __init__(self, name, place_of_habitat):
        self.name = name
        self.place = place_of_habitat

    def method(self):
        pass

    def eat(self):
        pass

    @staticmethod
    def get_population_count():
        # internet.get(...)
        return 99245



    @staticmethod
    def get_population_limbs_count():
        crocodile_count = Crocodile.get_population_count()
        return crocodile_count * Crocodile.limbs

    @classmethod
    def get_population_limbs_count_cls(cls):
        crocodile_count = cls.get_population_count()
        return crocodile_count * cls.limbs


def function():
    pass


integer_szczepan = int(99)
andrzej = Crocodile("Andrzej", "ZOO in Wroclaw")
blazej = Crocodile("Blazej", "Amazon forest")
print(Crocodile.get_population_count())
print(integer_szczepan)
andrzej.eat()
print(dir(Crocodile))
