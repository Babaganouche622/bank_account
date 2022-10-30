from account import Account
import time


class Bank:
    def __init__(self):
        self.accounts = [
            Account("Brian", "Cahill", "Big-Daddy69", 47000042),
            Account("Josh", "Faigan", "Charmander4Life", 55555555),
            Account("Andrew", "Alsing", "Vu/n3r@b/3-S3cur1\y", 69696969),
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
        return amount

    
    def add_account_numbers(self):
        for name in self.accounts:
            name.set_account_number()

    def statement(self, account_number):
        for name in self.accounts:
            if account_number == name.get_account_number_raw():
                print(f"""
|----------------------------------------------------|
 Your name:             |{name.get_account_name()}
 Your account number:   |{name.get_account_number()}
 Your balance:          |{name.get_balance()}$
|----------------------------------------------------|
                """)


