def calculate_compound_interest():
   
    num_customers = int(input("Enter the number of customers: "))

    for i in range(1, num_customers + 1):
        print(f"\nCustomer {i}:")
        initial_balance = float(input("Enter the initial balance: "))
        annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
        years = int(input("Enter the number of years: "))

        future_balance = initial_balance * (1 + annual_interest_rate / 100) ** years

        print(f"Future balance for Customer {i}: {future_balance:.2f}")

calculate_compound_interest()
