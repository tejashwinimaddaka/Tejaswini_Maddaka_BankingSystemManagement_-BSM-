accounts = {
    "12345": 1500.50,
    "67890": 2500.00,
    "54321": 5000.75,
    "98765": 10000.00
}

def check_account_balance():
    while True:
        
        account_number = input("Enter your account number (or type 'exit' to quit): ")

        if account_number.lower() == 'exit':
            print("Thank you for using the bank system.")
            break

        if account_number in accounts:
            print(f"Account Number: {account_number}")
            print(f"Your balance is: {accounts[account_number]:.2f}\n")
        else:
            print("Invalid account number. Please try again.\n")

check_account_balance()
