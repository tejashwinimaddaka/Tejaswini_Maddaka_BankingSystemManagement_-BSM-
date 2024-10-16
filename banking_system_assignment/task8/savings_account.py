from account import Account
class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate=0.045):
        super().__init__(account_number, 'Savings', balance)
        self.__interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.get_balance() * self.__interest_rate
        self.set_balance(self.get_balance() + interest)
        print(f"Interest of {interest} added, new balance: {self.get_balance()}")





