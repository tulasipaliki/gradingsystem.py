balance = 1000

while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print(f"Your current balance is: ₹{balance}")

    elif choice == "2":
        amount = float(input("Enter deposit amount: ₹"))
        if amount > 0:
            balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid amount.")

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: ₹"))
        if amount <= 0:
            print("Invalid amount.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    elif choice == "4":
        print("Thank you for using the ATM!")
        break

    else:
        print("Invalid choice. Please try again.")