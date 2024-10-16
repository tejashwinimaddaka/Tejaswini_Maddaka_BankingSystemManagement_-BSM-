def bank_transactions():
    transactions = []  
    balance = 0  

    while True:
        print("\nSelect a transaction type:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Exit and show transaction history")
        
        choice = input("Enter your choice : ")
        
        if choice == "1":
           
            deposit_amount = float(input("Enter deposit amount: "))
            transactions.append(f"Deposited: {deposit_amount}")
            balance += deposit_amount
            print(f"Successfully deposited {deposit_amount}. New balance: {balance}")
        
        elif choice == "2":
           
            withdraw_amount = float(input("Enter withdrawal amount: "))
            
            if withdraw_amount > balance:
                print("Error: Insufficient balance for this withdrawal.")
            else:
                transactions.append(f"Withdrew: {withdraw_amount}")
                balance -= withdraw_amount
                print(f"Successfully withdrew {withdraw_amount}. New balance: {balance}")
        
        elif choice == "3":
           
            print("\nTransaction History:")
            for transaction in transactions:
                print(transaction)
            print(f"Final Balance: {balance}")
            break
        
        else:
            print("Invalid option. Please try again.")

bank_transactions()
