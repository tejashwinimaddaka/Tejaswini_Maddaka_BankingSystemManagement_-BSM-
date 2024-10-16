from savings_account import SavingsAccount
from current_account import CurrentAccount
class Bank:
    def main(self):
        print("Welcome to the Banking System!")
        account_type = input("Choose account type (Savings/Current): ").strip().lower()
        
        if account_type == 'savings':
            account_number = input("Enter account number: ")
            balance = float(input("Enter initial balance: "))
            account = SavingsAccount(account_number, balance)
        elif account_type == 'current':
            account_number = input("Enter account number: ")
            balance = float(input("Enter initial balance: "))
            account = CurrentAccount(account_number, balance)
        else:
            print("Invalid account type.")
            return

        while True:
            print("\nMenu:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Calculate Interest (for Savings Account only)")
            print("4. Show Account Info")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            elif choice == '2':
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            elif choice == '3':
                if isinstance(account, SavingsAccount):
                    account.calculate_interest()
                else:
                    print("Interest calculation is only available for Savings accounts.")
            elif choice == '4':
                account.print_account_info()
            elif choice == '5':
                print("Exiting the Banking System. ")
                break
            else:
                print("Invalid choice. Please try again.")


# Main execution
if __name__ == "__main__":
    bank = Bank()
    bank.main()
