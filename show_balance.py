def show_balance0():
    print(f"Yout balance is ${balance:.2f}")
def deposit():
    amount = float(input("Enter an amount to be deposited: "))

    if amount < 0:
        print("That is not an valid amount")
        return 0
    else:
        return amount

def withdraw():
    amount = float(input("Enter amount to be withdraw: "))

    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount

balance = 0
is_runing = True

while is_runing:
    print("Banking Program")
    print("1.Show balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        show_balance0()
    elif choice == "2":
        balance += deposit()
    elif choice == "3":
        balance -= withdraw()
    elif choice == "4":
        is_runing = False
    else:
        print("That is not a walid choice")

print("Thank you! Have a nice day!")