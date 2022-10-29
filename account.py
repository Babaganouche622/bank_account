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

    def set_account_password():
        pass

    def get_account_password(self):
        return self.password

    def set_deposit(self, amount):
        self.balance += round(float(amount), 2)
        print(f"You deposited {amount}. Your balance is {self.balance}$")
        time.sleep(1)

    def set_withdraw(self, amount):
        if self.balance < amount:
            self.balance -= 10
            raise print("Ho ho ho ho, you didn't check your balance first. Thanks bucko, CHA CHING!")
        else:
            self.balance -= round(float(amount), 2)
            print(f"You withdrew {amount}. Your balance is {self.balance}$")
            time.sleep(1)    
    


brian = Account("Brian", "Cahill", "Password", 0)
brian.set_account_number()
print(brian.get_account_number())
print(brian.__dict__)
brian.set_account_number()
brian.set_deposit(50000)
