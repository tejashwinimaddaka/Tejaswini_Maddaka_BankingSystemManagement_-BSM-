class Account:
    def __init__(self, account_number=None, account_type=None, balance=0.0):
        self.__account_number = account_number
        self.__account_type = account_type
        self.__balance = balance

     # Getters
    def get_account_number(self):
        return self.__account_number

    def get_account_type(self):
        return self.__account_type

    def get_balance(self):
        return self.__balance

    # Setters
    def set_account_number(self, account_number):
        self.__account_number = account_number

    def set_account_type(self, account_type):
        self.__account_type = account_type

    def set_balance(self, balance):
        self.__balance = balance
    
    def print_account_info(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Account Type: {self.__account_type}")
        print(f"Balance: {self.__balance}")

    # Overloaded deposit methods
    def deposit(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            self.__balance += amount
            print(f"Deposited amount: {amount}, new balance: {self.__balance}")
        else:
            print("Invalid deposit amount.")

    # Overloaded withdraw methods
    def withdraw(self, amount):
        if isinstance(amount, (int, float)):
            if amount > self.__balance:
                print("Insufficient balance.")
            elif amount <= 0:
                print("Invalid withdrawal amount.")
            else:
                self.__balance -= amount
                print(f"Withdrew: {amount}, new balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount.")

    def calculate_interest(self):
        if self.__account_type == 'Savings':
            interest = self.__balance * 0.045
            self.__balance += interest
            print(f"Interest of {interest} added, new balance: {self.__balance}")
        else:
            print("Interest calculation is only available for Savings accounts.")


