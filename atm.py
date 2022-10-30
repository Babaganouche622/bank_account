from bank import Bank
from account import Account
import time
import copy
import getpass
import sys, os


def enable_print():
    sys.stdout = sys.__stdout__

def block_print():
    sys.stdout = open(os.devnull, 'w')

# Run user switches in here to trigger the different atm functions
def login():
    is_banking = True
    while is_banking == True:
        choice = input("Welcome to the criminal bank of Money. Would you like to give us money today?\n1: Yes\n2: No\nSelection: ")
        match choice:
            case "1":
                print("Excellent!")
                time.sleep(1)
                account_choice = input("Do you have an account with us already?\n1: Yes\n2: No\nEnter selection: ")
                time.sleep(1)
                match account_choice:
                    case "1":
                        login_name = input("Enter your full name here: ")
                        login_password = input("Enter you password here: ")
                        time.sleep(1)
                        for login in bank_of_hell.accounts:
                            if login_name == login.get_account_name() and login_password == login.get_account_password():
                                is_banking = False
                                login_info = copy.copy(login)
                                return login_info
                        print("You have an account")
                    case "2":
                        print("You don't have an account, let's make you one! HAHAHAHAHA\n")
                        time.sleep(1)
                        first_name = input("Give me your first name: ")
                        time.sleep(1)
                        last_name = input("Give me your last name: ")
                        time.sleep(1)
                        password = getpass.getpass(prompt = "Give me your password: ")
                        time.sleep(1)
                        balance = 0
                        bank_of_hell.set_new_account(first_name, last_name, password, balance)
                        for name in bank_of_hell.accounts:
                            if f"{first_name} {last_name}" == name.get_account_name():
                                name.set_account_number()
                                print(f"This is your account number: {name.get_account_number_raw()}\nYou will only ever see this once.")
                        print("Let's log in.")
                        time.sleep(1)
                    case _:
                        print("Input unrecognised.")
            case "2":
                print("Too bad, we'll take your money another time!")
                exit()
            case _:
                print(f"{choice} not compatible, enter correct choice.")
                time.sleep(1)
def banking(your_account):
    is_banking = True
    while is_banking == True:
        choice = input("What would you like to do?\n1: Deposit\n2: Withdraw\n3: Transfer\n4: Display Status\n5: Exit app\nSelection: ")
        match choice:
            case "1":
                amount = input("How much will you deposit? ")
                for account in bank_of_hell.accounts:
                    if your_account.get_account_number_raw() == account.get_account_number_raw():
                        account.set_deposit(amount)
            case "2":
                amount = input("How much will you withdraw? ")
                for account in bank_of_hell.accounts:
                    if your_account.get_account_number_raw() == account.get_account_number_raw():
                        account.set_withdraw(amount)
            case "3":
                name_of_receiver = input("Who are we sending money to today? Enter full name: ")
                send_amount = input("How much are you sending? ")
                for account in bank_of_hell.accounts:
                    if your_account.get_account_number_raw() == account.get_account_number_raw():
                        block_print()
                        real_amount = bank_of_hell.transfer(your_account.get_account_name(), name_of_receiver, send_amount)
                        enable_print()
                        if real_amount != send_amount:
                            print("Oops, looks like you didn't check your balance first, thanks for paying us again.")
                        else:
                            print(f"Nice transfer, you withdrew {send_amount}, your new balance is: {your_account.get_balance()}")
            case "4":
                bank_of_hell.statement(your_account.get_account_number_raw())
            case "5":
                print("Thanks for all your money!")
                exit()
            case "Steal":
                print("You found the secret option! Welcome to my world")
                name_of_receiver = input("Who are we stealing money from today? Enter full name: ")
                send_amount = input("How much are you stealing? ")
                for account in bank_of_hell.accounts:
                    if your_account.get_account_number_raw() == account.get_account_number_raw():
                        block_print()
                        real_amount = bank_of_hell.transfer(name_of_receiver, your_account.get_account_name(), send_amount)
                        enable_print()
                        if real_amount != send_amount:
                            print("Oops, looks like they don't have enough to steal.")
                        else:
                            print(f"Killer steal, you stole {send_amount}, your new balance is: {your_account.get_balance()}")
            case _:
                print("Unrecognised input.")

bank_of_hell = Bank()
bank_of_hell.add_account_numbers()
your_account = login()
banking(your_account)

for account in bank_of_hell.accounts:
    print(account.__dict__)
print(your_account.get_account_name())
