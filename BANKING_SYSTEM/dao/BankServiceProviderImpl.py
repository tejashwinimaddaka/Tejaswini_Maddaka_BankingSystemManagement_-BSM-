import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from dao.ICustomerServiceProvider import ICustomerServiceProvider
from dao.IBankServiceProvider import IBankServiceProvider
from dao.CustomerServiceProviderImpl import CustomerServiceProviderImpl
from util.DBConnection import DBConnection
from exception.invalidAcctExcp import InvalidAccountException
from decimal import Decimal 
class BankServiceProviderImpl(CustomerServiceProviderImpl, IBankServiceProvider):
    connection=None
    def __init__(self, branch_name: str, branch_address: str):
        super().__init__()
        self.accountList = []  # To store the account objects
        self.branchName = branch_name
        self.branchAddress = branch_address
        self.connection=DBConnection.getConnection()

    def create_account(self, customer, account_number, account_type, balance):
        """
        Create a new bank account for the given customer and add it to accountList.
        """
        # We use the CustomerServiceProviderImpl to create the account in the database
        conn = DBConnection.getConnection()
        cursor = conn.cursor()

        # Insert Customer
        cursor.execute('''
            INSERT INTO dbo.Customers (first_name, last_name, DOB, email, phone_number, address)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (customer.first_name, customer.last_name, customer.dob, customer.email, customer.phone_number, customer.address))
        customer_id = self.get_customer_id(cursor,customer.first_name)
        account_id = f"{account_number}"

        # Insert Account
        cursor.execute('''
            INSERT INTO Accounts (account_id,customer_id, account_type, balance)
            VALUES (?,?, ?, ?)
        ''', (account_id,customer_id, account_type, balance))
        account_id = self.get_account_id(cursor,customer.customer_id)

        # Add account object to accountList
        self.accountList.append({
            "account_id": account_id,
            "account_type": account_type,
            "balance": balance
        })

        conn.commit()
        conn.close()
        print(f"Account {account_number} created for {customer.first_name} {customer.last_name}")

    def list_accounts(self, customer_id: int):
        """
        List all accounts for a specific customer in the bank.
        """
        conn = DBConnection.getConnection()
        cursor = conn.cursor()
        

        cursor.execute('''
            SELECT a.account_id, a.account_type, a.balance
            FROM Accounts a
            WHERE a.customer_id = ?
        ''', (customer_id,))
        accounts = cursor.fetchall()

        if not accounts:
            print("No accounts available for this customer.")
        else:
            print(f"Accounts for Customer ID {customer_id}:")
            for account in accounts:
                print(f"Account ID: {account[0]}, Type: {account[1]}, Balance: {account[2]}")

        conn.close()


    def calculate_interest(self, account_number: int):
        """
        Calculate the interest for a specific account (only for savings accounts).
        """
        conn = DBConnection.getConnection()
        cursor = conn.cursor()
        cursor.execute('SELECT account_type, balance FROM Accounts WHERE account_id = ?', (account_number,))
        account = cursor.fetchone()

        if account is None:
            raise InvalidAccountException("Account not found.")

        account_type, balance = account
        print(f"Account type: {account_type}, Balance: {balance}")

        if account_type == 'savings':
            interest_rate = Decimal('4.5')  # Assuming a fixed interest rate
            interest = Decimal(balance) * (interest_rate / Decimal('100'))
            print(f"Interest calculated for account {account_number}: {interest}")
            return interest
        else:
            raise Exception("Interest calculation is only applicable for savings accounts.")
        
    def get_customer_id(self,cursor, first_name):
   
        query = "SELECT customer_id FROM Customers WHERE first_name = ?"
        cursor.execute(query, (first_name,))

        customer_id = cursor.fetchone()
        if customer_id:
            return customer_id[0]
        else:
            return 1


    def get_account_id(self,cursor, customer_id):
    
        query = "SELECT account_id FROM Accounts WHERE customer_id = ?"
        cursor.execute(query, (customer_id,))

        account_id = cursor.fetchone()
        if account_id:
            return account_id[0]
        else:
            return 1

    

        

  
    