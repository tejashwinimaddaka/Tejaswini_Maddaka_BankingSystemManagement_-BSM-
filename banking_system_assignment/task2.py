def atm_transaction():
    balance = float(input("Enter your current balance: "))
    print("\nATM Options:")
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")
    
    option = int(input("\nEnter the option number: "))
    
    if option == 1:
        print(f"\nYour current balance is: {balance}")
    
    elif option == 2:
        withdraw_amount = float(input("Enter the amount to withdraw: "))

        # Check if withdrawal amount is in multiples of 100 or 500
        if withdraw_amount % 100 != 0 and withdraw_amount % 500 != 0:
            print("Error: The withdrawal amount must be in multiples of 100 or 500.")
        # Check if the balance is sufficient for withdrawal
        elif withdraw_amount > balance:
            print("Error: Insufficient balance for this withdrawal.")
        else:
            balance -= withdraw_amount
            print(f"Success: You have withdrawn {withdraw_amount}. Your new balance is {balance}.")
    
    elif option == 3:
        deposit_amount = float(input("Enter the amount to deposit: "))
        balance += deposit_amount
        print(f"Success: You have deposited {deposit_amount}.\n Your new balance is {balance}.")
    
    else:
        print("Invalid option selected. Please try again.")

atm_transaction()
