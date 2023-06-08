class Bank:


    def __init__(self, initial_amount=0.00):#DUNDER METHOD
        self.balance = initial_amount 

    def transaction(self, transactions):
        with open("transaction.txt","a") as file:
            file.write(f"{transactions} \t\t\t Balance Amount:{self.balance}\n")

    def deposit(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount:
            self.balance = self.balance + amount
            self.transaction(f"deposited amount is:{amount}")

    def withdraw(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount:
            self.balance = self.balance - amount
            self.transaction(f"Withdrawal amount is:{amount}")

account = Bank(120000.00)
while True:
    num = input("enter the pin:\t")
    num = int(num)
    if num == 2436:
        print("YOU can enter the values")
    else:
        print("Wrong pin")
        break
    try:
        action = input("What kind of Process do want:\n\t")
    except KeyboardInterrupt:
        print("\n ATM machine repair")
        break
    if action in ["withdrawal","deposit",]:
        if action == "withdrawal":
            amount = input("Withdrawal amount :")
            account.withdraw(amount)
        else:
            amount = input("Deposited amount is:")
            account.deposit(amount)

        print("Your Bank Balance is",account.balance)

    else:
        print("YOU TYPED WRONG VALUE:")
