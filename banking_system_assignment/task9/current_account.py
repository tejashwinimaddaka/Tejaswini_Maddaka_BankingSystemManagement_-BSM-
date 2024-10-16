from bankaccount import BankAccount

class CurrentAccount(BankAccount):
    OVERDRAFT_LIMIT = 1000  #  a constant overdraft limit

    def __init__(self, account_number, customer_name, balance):
        super().__init__(account_number, customer_name, balance)

    def deposit(self, amount):
        if amount > 0:
            new_balance = self.get_balance() + amount
            self.set_balance(new_balance)
            print(f"Deposited: {amount}, New Balance: {self.get_balance()}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        # Check if the withdrawal amount exceeds the total available balance (including overdraft limit)
        if amount > self.get_balance() + self.OVERDRAFT_LIMIT:
            print("Exceeds overdraft limit. Insufficient balance.")
        else:
            # Deduct the amount from the balance
            new_balance = self.get_balance() - amount
            self.set_balance(new_balance)  # Update the balance
            print(f"Withdrew: {amount}, New Balance: {self.get_balance()}")

    def calculate_interest(self):
        print("Current Account does not earn interest.")
