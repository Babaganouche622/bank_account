import random
import itertools


class Account:
    def __init__(self, name, password, balance):
        self.name = name
        self.password = password
        self.balance = balance
        self.number = ''


    def set_account_number(self):
        number = []
        if self.number != '':
            return print("Account number is already set.")
        while len(number) < 8:
            number.append(random.randint(1, 9))

        number = int(''.join(map(str,number)))
        self.number = number


    def getBalance(self):
        return self.balance

    def getAccountName(self):
        return self.name

    def getAccountNumber(self):
        return self.number

    def getAccountPassword(self):
        return self.password


    def setAccountBalance():
        """
        Ask the user if they want to withdraw or Deposit before coming inside the class
        here we will check which the user input, then condition which Withdraw/Deposit will trigger
        Passthrough some number, validate that it is a number and rounded to the 0.00$ correct decimal.
        If the user is depositing the number should be positive.
        If the user is withdrawing the number should be nugative AND less than the total account balance
        If the withdraw amount is over the account total, kick out to main menu and charge a 10$NSF

        Else set the amount to be deposited/withdrawn in the account. 
        """
        pass
    
    
    def set_account_password():
        pass
    def set_account_name():
        pass


brian = Account('Brian', "Password", 0)
brian.set_account_number()
print(brian.number)
print(brian.__dict__)
brian.set_account_number()
