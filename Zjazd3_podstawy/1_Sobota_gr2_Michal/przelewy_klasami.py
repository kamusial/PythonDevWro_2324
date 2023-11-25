class Account:
    def __init__(self, name, initial_balance):
        self.name = name
        self.balance = initial_balance

    def transfer(self, target_account, amount):
        self.balance -= amount
        target_account.balance += amount
        print(f"{self.name} transfers {amount} PLN to {target_account.name}")


asia_account = Account("Asia", 100)
basia_account = Account("Basia", 100)
pawel_account = Account("Paweł", 100)

# transfers("asia", "pawel", 20)
asia_account.transfer(pawel_account, 20)
basia_account.transfer(pawel_account, 50)
pawel_account.transfer(asia_account, 60)
basia_account.transfer(asia_account, 30)

print(f"{asia_account.name} has {asia_account.balance} PLN")
print(f"{basia_account.name} has {basia_account.balance} PLN")
print(f"{pawel_account.name} has {pawel_account.balance} PLN")
