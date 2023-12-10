class Human:
    def __init__(self):
        print("human")

    def sleep(self):
        ...

    def eat(self):
        ...

    def drink(self):
        ...


class Bills:
    def calculate(self):
        ...

    def income(self):
        ...

    def expense(self):
        ...


class BobBuilder(Human):
    def __init__(self):
        super().__init__()
        self.bills = Bills()

    def build(self):
        ...

    def talk_to_cars(self):
        ...


class SuperDuperGlutton(Human):
    def __init__(self):
        super().__init__()
        print("dupa")

    def eat(self):
        super().eat()
        super().eat()
        super().eat()
        self.drink()


my_bob = BobBuilder()
"""Encapsulation over inheritance!!! <3"""
my_bob.bills.calculate()
my_bob.talk_to_cars()

alex = SuperDuperGlutton()
alex.eat()
