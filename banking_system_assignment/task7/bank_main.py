from account import Account
class Bank:
    def main(self):
        account = Account("411456213256", "Savings", 500.0)    #parameterized constructor
        account.print_account_info()
        account.deposit(150.0)
        account.withdraw(1000.0)
        account.calculate_interest()
        account.print_account_info()


#Bank class main method
if __name__ == "__main__":
    bank = Bank()
    bank.main()
