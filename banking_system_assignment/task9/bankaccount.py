
from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, account_number=None, customer_name=None, balance=0.0):
        self.__account_number = account_number
        self.__customer_name = customer_name
        self.__balance = balance

    # Getters
    def get_account_number(self):
        return self.__account_number

    def get_customer_name(self):
        return self.__customer_name

    def get_balance(self):
        return self.__balance

    # Setters
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid balance value.")

    def print_account_info(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Customer Name: {self.__customer_name}")
        print(f"Balance: {self.__balance}")

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def calculate_interest(self):
        pass
