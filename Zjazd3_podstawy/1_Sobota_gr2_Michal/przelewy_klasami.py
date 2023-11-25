class Account:
    def __init__(self, name, initial_balance, incoming_transfer_fee=0):
        self.name = name
        self.balance = initial_balance
        self.incoming_transfer_fee = incoming_transfer_fee

    def transfer(self, target_account, amount):
        self.balance -= amount
        target_account.balance += amount - target_account.incoming_transfer_fee
        print(f"{self.name} transfers {amount} PLN to {target_account.name}")


asia_account = Account("Asia", 100, incoming_transfer_fee=1)
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
