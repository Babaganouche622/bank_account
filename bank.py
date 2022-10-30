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

    def transfer(self, name_from, name_to, amount):
        for name in self.accounts:
            if name.get_account_name() == name_from:
                amount = name.set_withdraw(amount)
            if name.get_account_name() == name_to:
                name.set_deposit(amount)

    
    def add_account_numbers(self):
        for name in self.accounts:
            name.set_account_number()

    def statement(self):
        for name in self.accounts:
            print(name.__dict__)


    # def banking():
    #     is_banking = True
    #     while is_banking == True:
    #         choice = input("Welcome to the criminal bank of Money. Would you like to give us money today?\n1: Yes\n2: No\nSelection: ")
    #         match choice:
    #             case "1":
    #                 print("Excellent!")
    #                 time.sleep(1)
    #                 account_choice = input("Do you have an account with us already?\n1: Yes\n2: No\nEnter selection: ")
    #                 time.sleep(1)
    #                 match choice:
    #                     case "1":
    #                         print("You have an account")
    #                     case "2":
    #                         print("You don't have an account, let's make you one! HAHAHAHAHA\n\n")
    #                         time.sleep(1)
    #                         first_name = input("Give me your first name: ")
    #                         time.sleep(1)
    #                         last_name = input("Give me your last name: ")
    #                         time.sleep(1)
    #                         password = input("Give me your password: ")
    #                         time.sleep(1)
    #                         balance = 0
    #                         set_new_account(first_name, last_name, password, balance)
    #                     case _:
    #                         print("Input unrecognised.")
    #             case "2":
    #                 print("Too bad, we'll take your money another time!")
    #             case _:
    #                 print(f"{choice} not compatible, enter correct choice.")
    #                 time.sleep(1)




