from bankaccount import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, account_number, customer_name, balance, interest_rate=0.045):
        super().__init__(account_number, customer_name, balance)
        self.__interest_rate = interest_rate

    def deposit(self, amount):
        if amount > 0:
            new_balance = self.get_balance() + amount
            self.set_balance(new_balance)
            print(f"Deposited: {amount}, New Balance: {self.get_balance()}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > self.get_balance():
            print("Insufficient balance. Can not withdraw the  amount you entered.")
        else:
            new_balance = self.get_balance() - amount
            self.set_balance(new_balance)
            print(f"Withdrew: {amount}, New Balance: {self.get_balance()}")

    def calculate_interest(self):
        interest = self.get_balance() * self.__interest_rate
        self.set_balance(self.get_balance() + interest)
        print(f"Interest of {interest} added, New Balance: {self.get_balance()}")



