import sys
class User:
    def __init__(self, user_id, pin_no):
        self.user_id = user_id
        self.pin = pin_no


class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return amount
        else:
            return "Your account has insufficient Balance"

    def get_balance(self):
        return self.balance


class TransactionHistory:
    def __init__(self):
        self.history = []

    def add_transaction(self, transaction):
        self.history.append(transaction)

    def display_history(self):
        for transaction in self.history:
            print(transaction)


class ATM:
    def __init__(self, users, transactions):
        self.users = users
        self.transactions = transactions

    def authenticate_user(self, user_id, pin_no):
        for user in self.users:
            if user.user_id == user_id and user.pin == pin_no:
                return True, user
        return False, "Invalid UserId or Pin"

    def select_account(self, user):
        return Account(user.user_id)

    def deposit(self, account, amount):
        account.deposit(amount)
        self.transactions.add_transaction(f"Deposit: +{amount}")

    def withdraw(self, account, amount):
        withdrawn = account.withdraw(amount)
        if isinstance(withdrawn, str):
            return withdrawn
        else:
            self.transactions.add_transaction(f"Withdrawal: -{amount}")
            return withdrawn

    def transfer(self, source_account, target_account, amount):
        withdrawn = source_account.withdraw(amount)
        if isinstance(withdrawn, str):
            return withdrawn
        else:
            target_account.deposit(amount)
            self.transactions.add_transaction(f"Transfer: -{amount} to {target_account.account_number}")
            return withdrawn

bal=0.00
class Main:
    @staticmethod
    def main():
        global bal
        # Sample users
        users = [User("112233", "1234"), User("445566", "5678")]

        atm = ATM(users, TransactionHistory())

        # Authentication
        user_id = input("Enter Your User ID: ")
        pin_no = input("Enter Your PIN: ")

        authenticated, user = atm.authenticate_user(user_id, pin_no)

        if authenticated:
            print("Authentication successful.")
            account = atm.select_account(user)
            while True:
                print("*"*30)
                print("\tWelcome To ATM")
                print("*"*30)
                print("\t1. Transaction History")
                print("\t2. Withdraw")
                print("\t3. Deposit")
                print("\t4. Transfer")
                print("\t5. Quit")
                choice = input("Enter your choice: ")
                if choice == "1":
                    atm.transactions.display_history()
                elif choice == "2":
                    amount = float(input("Enter amount to withdraw: "))
                    result = atm.withdraw(account, amount)
                    if isinstance(result, str):
                        print(result)
                    else:
                       bal=bal-amount
                       print("Your Account xxxxxxx123 Debited with INR:Rs.{}".format(result))
                       print("Now Your Account Balance is Rs.{}".format(bal))
                elif choice == "3":
                    amount = float(input("Enter amount to deposit: "))
                    atm.deposit(account, amount)
                    bal=bal+amount
                    print("Your Account xxxxxxx123 Credited with INR:Rs.{}".format(amount))
                    print("Now Your Account Balance is Rs.{}".format(bal))
                elif choice == "4":
                    target_account = input("Enter target account number: ")
                    amount = float(input("Enter amount to transfer: "))
                    target_user = next((u for u in users if u.user_id == target_account), None)
                    if target_user:
                        target_account = atm.select_account(target_user)
                        result = atm.transfer(account, target_account, amount)
                        if isinstance(result, str):
                            print(result)
                        else:
                            bal=bal-amount
                            print(f"Transfer of Rs.{amount} to {target_account.account_number} successful.")
                            print("Now Your Account Bal is Rs.{}".format(bal))
                    else:
                        print("Target account not found.")
                elif choice == "5":
                    print("Thank you for using the ATM.")
                    break
                else:
                    print("You Entered Invalid choice. Please try again.")
        else:
            print("Authentication failed.")



atm=Main.main()

