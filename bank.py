from account import Account
import time

class Bank:
    def __init__(self):
        self.accounts = [
            Account("Brian", "Cahill", "Big-Daddy69", 47000042),
            Account("Josh", "Faigan", "Charmander4Life", 55555555),
            Account("Andrew", "Aisling", "Vu/n3r@b/3-S3cur1\y", 69696969),
            Account("Alex", "Rocha", "PwningN00bs", 81680085)
        ]
        
    def set_new_account(self, first_name, last_name, password, balance):
        self.accounts.append(Account(first_name, last_name, password, balance))

    def transfer(self, account_number_from, account_number_to, amount):
        for account in self.accounts:
            if account.get_account_number() == account_number_from:
                account.set_withdraw(amount)
        for account in self.accounts:
            if account.get_account_number() == account_number_to:
                account.set_deposit(amount)

    def banking():
        is_banking = True
        while is_banking == True:
            choice = input("Welcome to the criminal bank of Money. Would you like to give us money today?\n1: Yes\n2: No\nSelection: ")
            match choice:
                case "1":
                    print("Excellent!")
                    time.sleep(1)
                    input("Do you have an account with us already?\n1: Yes\n2: No\nEnter selection: ")
                    
                case "2":
                    print("Too bad, we'll take your money another time!")
                case _:
                    print(f"{choice} not compatible, enter correct choice.")
                    time.sleep(1)


# 

# build Banking class here
# Arguments should be nothing? This class will just trigger all the function of the banking machine

# Constructor should hold the list of bank accounts
# Start with 4, Brian, Josh, Alex, Andrew.

# SetBank account list with a new one, ask the user questions like:
# Account name and password
# type of account creating (Chequing/Savings)
# How much money they want to deposit

def creat_account():
    pass

def transfer():
    pass

def statement():
    pass




