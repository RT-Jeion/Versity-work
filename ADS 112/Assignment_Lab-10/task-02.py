# Write a 'BankAccount' class with deposit and withdraw methods.Print the current balance after every transaction.

class Bank:
    def __init__(self, name: str, balance: int = 00):
        self.name = name
        self.balance = balance
        print(f"Account Has been Created.")
        print("Name:", self.name)
        print("Starting Balance:", self.balance)
        print()

    def deposit(self, amount: int):
        self.balance += amount
        print("Account Holder Name:", self.name)
        print(f"${amount} has been deposit.")
        print("Current Balance:", self.balance)
        print()

    def withdraw(self, amount: int):
        if self.balance < amount:
            print("Not Enough Money")
            return

        self.balance -= amount
        print("Account Holder Name:", self.name)
        print(f"${amount} has been withdraw.")
        print("Current Balance:", self.balance)
        print()


rt = Bank("RT Jeion")

rt.deposit(5000)
rt.withdraw(1000)

rejuwan = Bank("Rejuwan", 20000)
