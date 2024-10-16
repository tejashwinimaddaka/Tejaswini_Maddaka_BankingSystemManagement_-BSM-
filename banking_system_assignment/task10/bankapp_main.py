from bank import Bank
from customer import Customer

class BankApp:
    def main(self):
        bank = Bank()
        while True:
            print("\nMenu:")
            print("1. Create Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Get Balance")
            print("5. Transfer")
            print("6. Get Account Details")
            print("7. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                customer_id = input("Enter Customer ID: ")
                first_name = input("Enter First Name: ")
                last_name = input("Enter Last Name: ")
                email = input("Enter Email Address: ")
                phone = input("Enter Phone Number: ")
                address = input("Enter Address: ")

                customer = Customer(customer_id, first_name, last_name, email, phone, address)

                acc_type = input("Enter Account Type (Savings/Current): ")
                balance = float(input("Enter Initial Balance: "))

                bank.create_account(customer, acc_type, balance)

            elif choice == '2':
                acc_no = int(input("Enter Account Number: "))
            # Check for account existence immediately before proceeding
                if acc_no not in bank._Bank__accounts:  # Accessing private member for checking
                    print("Account not found.")
                    continue
                amount = float(input("Enter Deposit Amount: "))
                bank.deposit(acc_no, amount)

            elif choice == '3':
                acc_no = int(input("Enter Account Number: "))
                    # Check for account existence immediately before proceeding
                if acc_no not in bank._Bank__accounts:  # Accessing private member for checking
                    print("Account not found.")
                    continue
                amount = float(input("Enter Withdrawal Amount: "))
                bank.withdraw(acc_no, amount)

            elif choice == '4':
                acc_no = int(input("Enter Account Number: "))
                balance = bank.get_account_balance(acc_no)
                if balance is not None:
                    print(f"Current Balance: {balance}")

            elif choice == '5':
                from_acc = int(input("Enter From Account Number: "))
            
                if from_acc not in bank._Bank__accounts:  # Accessing private member for checking
                    print("Sender account not found.")
                    continue
                to_acc = int(input("Enter To Account Number: "))
                # Check receiver account existence
                if to_acc not in bank._Bank__accounts:  # Accessing private member for checking
                    print("Receiver account not found.")
                    continue
                amount = float(input("Enter Transfer Amount: "))
                bank.transfer(from_acc, to_acc, amount)


            elif choice == '6':
                acc_no = int(input("Enter Account Number: "))
                bank.get_account_details(acc_no)

            elif choice == '7':
                print("Exiting the Banking System.")
                break

            else:
                print("Invalid choice. Please try again.")

# Main execution
if __name__ == "__main__":
    app = BankApp()
    app.main()
