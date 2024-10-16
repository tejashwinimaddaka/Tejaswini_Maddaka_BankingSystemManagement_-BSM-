import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dao.ICustomerServiceProvider import ICustomerServiceProvider
from exception.invalidAcctExcp import InvalidAccountException
from util.DBConnection import DBConnection

class CustomerServiceProviderImpl(ICustomerServiceProvider):
    connection=None
    def __init__(self):
        self.connection=DBConnection.getConnection()

    
    def get_account_balance(self, account_number: int):
        """
        Retrieve the balance of an account given its account number.
        """
        conn = DBConnection.getConnection()
        cursor = conn.cursor()

        cursor.execute('SELECT balance FROM Accounts WHERE account_id=?', (account_number,))
        account = cursor.fetchone()

        if account is None:
            conn.close()
            raise InvalidAccountException("Account not found")
        
        balance = account[0]
        conn.close()
        print(f"Account ID: {account_number}, Balance: {balance}")
        return balance

    def deposit(self, account_number: int, amount: float):
        """
        Deposit the specified amount into the account.
        """
        conn = DBConnection.getConnection()
        cursor = conn.cursor()

        # Check if the account exists
        cursor.execute('SELECT balance FROM Accounts WHERE account_id = ?', (account_number,))
        result = cursor.fetchone()

        if result is None:
            conn.close()
            raise Exception(f"Account with ID {account_number} does not exist.")

        # Perform the deposit
        cursor.execute('UPDATE Accounts SET balance = balance + ? WHERE account_id = ?', (amount, account_number))
        conn.commit()

        # Fetch the updated balance
        cursor.execute('SELECT balance FROM Accounts WHERE account_id = ?', (account_number,))
        new_balance = cursor.fetchone()[0]

        conn.close()
    
        # Print success message
        print(f"Deposited successfully. New balance: {new_balance}")
    
        return new_balance


    def withdraw(self, account_number: int, amount: float):
        """
        Withdraw the specified amount from the account.
        """
        conn = DBConnection.getConnection()
        cursor = conn.cursor()

        cursor.execute('SELECT balance FROM Accounts WHERE account_id=?', (account_number,))
        account = cursor.fetchone()

        if account is None:
            raise InvalidAccountException("Account not found")

        balance = account[0]
        if balance >= amount:
            cursor.execute('UPDATE Accounts SET balance = balance - ? WHERE account_id=?', (amount, account_number))
            conn.commit()

            cursor.execute('SELECT balance FROM Accounts WHERE account_id=?', (account_number,))
            new_balance = cursor.fetchone()[0]
            conn.close()
            print(f"Withdrawal successful. Updated balance: {new_balance}")
            return new_balance
        else:
            conn.close()
            raise Exception("Insufficient Balance")

    def transfer(self, from_account: int, to_account: int, amount: float):
        """
        Transfer money from one account to another.
        """
        self.withdraw(from_account, amount)
        self.deposit(to_account, amount)

    def get_account_details(self, account_number: int):
        """
        Retrieve account and customer details for the given account number.
        """
        conn = DBConnection.getConnection()
        cursor = conn.cursor()

        cursor.execute('''
            SELECT c.first_name, c.last_name, c.email, c.phone_number, a.account_type, a.balance
            FROM Customers c
            JOIN Accounts a ON c.customer_id = a.customer_id
            WHERE a.account_id=?
        ''', (account_number,))
        account_details = cursor.fetchone()

        if account_details is None:
            raise InvalidAccountException("Account not found")

        conn.close()
        print(f"Account Details:\n"
          f"First Name: {account_details[0]}\n"
          f"Last Name: {account_details[1]}\n"
          f"Email: {account_details[2]}\n"
          f"Phone Number: {account_details[3]}\n"
          f"Account Type: {account_details[4]}\n"
          f"Balance: {account_details[5]}")

        return account_details