from account import Account
class CurrentAccount(Account):
    OVERDRAFT_LIMIT = 100 # Set a constant overdraft limit

    def __init__(self, account_number, balance):
        super().__init__(account_number, 'Current', balance)

    def withdraw(self, amount):
   
        if amount > self.get_balance() + self.OVERDRAFT_LIMIT:
            print("Exceeds overdraft limit. Insufficient balance.")
        else:
            new_balance = self.get_balance() - amount
            self.set_balance(new_balance)  
            print(f"Withdrew: {amount}, New Balance: {self.get_balance()}")

