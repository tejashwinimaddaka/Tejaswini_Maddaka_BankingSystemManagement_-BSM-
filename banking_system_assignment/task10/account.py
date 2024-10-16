class Account:
    def __init__(self, account_number, account_type, balance, customer):
        self.__account_number = account_number
        self.__account_type = account_type
        self.__balance = balance
        self.__customer = customer  # Has-a relationship with Customer

    # Getters and Setters
    def get_account_number(self):
        return self.__account_number

    def get_account_type(self):
        return self.__account_type

    def get_balance(self):
        return self.__balance

    def get_customer(self):
        return self.__customer

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited: {amount}. New Balance: {self.__balance}")
        return self.__balance

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}. New Balance: {self.__balance}")
            return self.__balance
        else:
            print("Insufficient balance.")
            return self.__balance

    def print_account_info(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Account Type: {self.__account_type}")
        print(f"Balance: {self.__balance}")
        self.__customer.print_info()  # Print customer info
