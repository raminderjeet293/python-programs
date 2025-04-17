class BankAccount:
    def __init__(self, first_name, last_name, starting_balance=0.00):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = starting_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited. New Balance: ₹{self.balance:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Transaction declined. Insufficient balance.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn. New Balance: ₹{self.balance:.2f}")

    def display(self):
        print(f"\nAccount Holder: {self.first_name} {self.last_name}")
        print(f"Current Balance: ₹{self.balance:.2f}")

fname = input("Enter first name: ")
lname = input("Enter last name: ")
bank_account = BankAccount(fname, lname)

while True:
    print("\n==== BANK MENU ====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display Account Info")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        amt = float(input("Enter amount to deposit: ₹"))
        bank_account.deposit(amt)

    elif choice == "2":
        amt = float(input("Enter amount to withdraw: ₹"))
        bank_account.withdraw(amt)

    elif choice == "3":
        bank_account.display()

    elif choice == "4":
        print("Thank you for banking with us!")
        break

    else:
        print("Invalid choice. Please select from 1-4.")
