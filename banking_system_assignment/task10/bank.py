from account import Account
class Bank:
    account_counter = 1001  # Static variable for account number generation

    def __init__(self):
        self.__accounts = {}

    def create_account(self, customer, acc_type, balance):
        account_number = Bank.account_counter
        Bank.account_counter += 1  # Increment account number for the next account
        account = Account(account_number, acc_type, balance, customer)
        self.__accounts[account_number] = account
        print(f"Account created for {customer.get_first_name()} {customer.get_last_name()} with Account Number: {account_number}")

    def get_account_balance(self, account_number):
        if account_number in self.__accounts:
            return self.__accounts[account_number].get_balance()
        else:
            print("Account not found.")
            return None

    def deposit(self, account_number, amount):
        # Check for account existence immediately
        if account_number not in self.__accounts:
            print("Account not found.")
            return None

        # If account exists, proceed with deposit
        current_balance = self.__accounts[account_number].deposit(amount)
        return current_balance

    def withdraw(self, account_number, amount):
        # Check for account existence immediately
        if account_number not in self.__accounts:
            print("Account not found.")
            return None

        current_balance = self.__accounts[account_number].withdraw(amount)
        return current_balance

    def transfer(self, from_account_number, to_account_number, amount):
        if from_account_number not in self.__accounts:
            print("Sender account not found.")
            return
    
        if to_account_number not in self.__accounts:
            print("Receiver account not found.")
            return
    
        if self.__accounts[from_account_number].get_balance() < amount:
            print("Insufficient balance to transfer.")
            return
    
        # Proceed with withdrawal and deposit if checks pass
        print(f"Transferred {amount} from Account {from_account_number} to Account {to_account_number}.")
        self.__accounts[from_account_number].withdraw(amount)



    def get_account_details(self, account_number):
        if account_number in self.__accounts:
            account = self.__accounts[account_number]
            account.print_account_info()
        else:
            print("Account not found.")
