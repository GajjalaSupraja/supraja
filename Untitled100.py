#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class BankAccount:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid amount. Please enter a positive number.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def transfer(self, amount, target_account):
        if 0 < amount <= self.balance:
            self.balance -= amount
            target_account.balance += amount
            print(f"Transferred ${amount} to {target_account.name}. Your new balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def check_balance(self):
        print(f"Account Balance for {self.name}: ${self.balance}")


def main():
    print("Welcome to the Simple Banking System!")
    print("-------------------------------------")

    # Creating two bank accounts for testing
    account_number1 = input("Enter account number for Account 1: ")
    name1 = input("Enter name for Account 1: ")
    account1 = BankAccount(account_number1, name1)

    account_number2 = input("Enter account number for Account 2: ")
    name2 = input("Enter name for Account 2: ")
    account2 = BankAccount(account_number2, name2)

    while True:
        print("\nMENU:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Transfer")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            amount = float(input("Enter the amount to deposit: "))
            account1.deposit(amount)

        elif choice == '2':
            amount = float(input("Enter the amount to withdraw: "))
            account1.withdraw(amount)

        elif choice == '3':
            amount = float(input("Enter the amount to transfer: "))
            target_account_number = input("Enter the account number to transfer to: ")
            if target_account_number == account2.account_number:
                account1.transfer(amount, account2)
            else:
                print("Invalid account number.")

        elif choice == '4':
            account1.check_balance()

        elif choice == '5':
            print("Thank you for using the Simple Banking System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()


# In[ ]:




