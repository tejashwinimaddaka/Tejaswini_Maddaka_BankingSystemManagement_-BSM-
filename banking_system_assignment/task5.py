def validate_password():
  
    password = input("Create a password for your bank account: ")

    if len(password) < 8:
        print("Error: Password must be at least 8 characters long.")
        return
    if not any(char.isupper() for char in password):
        print("Error: Password must contain at least one uppercase letter.")
        return
    if not any(char.isdigit() for char in password):
        print("Error: Password must contain at least one digit.")
        return
    print("Password is valid!")

validate_password()
