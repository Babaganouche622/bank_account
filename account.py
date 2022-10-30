import random
import re
import time


class Account:
    def __init__(self, first_name, last_name, password, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.balance = balance
        self.number = ''

    def get_balance(self):
        return self.balance

    def set_account_name(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_account_name(self):
        return f"{self.first_name} {self.last_name}"

    def set_account_number(self):
        number = []
        if self.number != '':
            return print("Account number is already set.")
        while len(number) < 8:
            number.append(random.randint(1, 9))
        number = int(''.join(map(str,number)))
        self.number = number

    def get_account_number(self):
        number = re.sub("(\d)", "*", str(self.number), 4)
        return number

    def get_account_number_raw(self):
        return self.number

    def set_account_password():
        pass

    def get_account_password(self):
        return self.password

    def set_deposit(self, amount):
        self.balance += round(float(amount), 2)
        print(f"You deposited {amount}$. Your balance is {self.balance}$")
        time.sleep(1)

    def set_withdraw(self, amount):
        if self.balance < float(amount):
            self.balance -= 10
            amount = 0
            print(f"Ho ho ho ho, you didn't check your balance first. Thanks bucko, CHA CHING!\nCharged an NSF fee of 10$.\nNew balance: {self.balance}$")
            time.sleep(1)
            return amount
        else:
            tax = round(float(amount) * 1.5, 2)
            self.balance -= round(float(amount), 2) + tax
            print(f"You withdrew {amount}$. Your balance is {self.balance}$")
            time.sleep(1)
            return amount
    