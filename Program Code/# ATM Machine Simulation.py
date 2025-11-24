# ATM Machine Simulation
# Uses: if-else, loops, functions, simple list

balance = [1000]   # using list to store balance (as required)
                   # so its value can be updated inside functions

def check_balance():
    print(f"\nYour current balance is: ₹{balance[0]}\n")

def deposit():
    amt = int(input("Enter amount to deposit: ₹"))
    balance[0] += amt
    print(f"₹{amt} deposited successfully!\n")

def withdraw():
    amt = int(input("Enter amount to withdraw: ₹"))
    
    if amt <= balance[0]:
        balance[0] -= amt
        print(f"₹{amt} withdrawn successfully!\n")
    else:
        print("Insufficient balance! Transaction failed.\n")

def atm_menu():
    while True:
        print("------ ATM MACHINE ------")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            check_balance()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            print("Thank you for using ATM. Goodbye!")
            break
        else:
            print("Invalid choice, try again!\n")

# Start the ATM Program
atm_menu()