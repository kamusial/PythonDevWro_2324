"""
Funkcjonalność przelewów gdzieś nie działa.
Pls fix
"""

from abc import ABC, abstractmethod


class YouArePoorError(Exception):
    ...


def poorness_check(balance: int, money_to_pay: int):
    if balance < money_to_pay:
        raise YouArePoorError(f"You don't have enough money to pay: {money_to_pay=}, {balance=}")


class Account(ABC):
    @abstractmethod
    def transfer(self, account: 'Account', money: int):
        ...

    @abstractmethod
    def receive(self, money: int):
        ...


class CoolBankAccount(Account):
    def __init__(self):
        self.balance = 50

    def transfer(self, account: Account, money: int):
        poorness_check(self.balance, money)
        self.receive(money)
        self.balance -= money

    def receive(self, money: int):
        self.balance += money

    def new_month(self):
        self.balance = int(self.balance * 1.01)


class StupidBankAccount(Account):
    def __init__(self):
        self.balance = 0
        self.transfer_count = 0

    def transfer(self, account: Account, money: int):
        poorness_check(self.balance, money)
        self.balance -= money
        account.receive(money)
        self.transfer_count += 1
        if self.transfer_count >= 5:
            self.balance -= 3

    def receive(self, money: int):
        self.balance += money

    def new_month(self):
        self.transfer_count = 0


def main():
    account_1 = CoolBankAccount()
    account_2 = StupidBankAccount()
    bills = CoolBankAccount()
    employer = CoolBankAccount()
    accounts = [account_1, account_2]
    for _ in range(12):
        for account in accounts:
            employer.transfer(account, 1000)
            [account.transfer(bills, 10) for _ in range(10)]
            account.new_month()
        account_1.transfer(account_2, 40)
    print(account_1.balance)
    print(account_2.balance)
    assert account_1.balance == 11070, f"{account_1.balance=}"
    assert account_2.balance == 11064, f"{account_2.balance=}"


if __name__ == '__main__':
    main()
