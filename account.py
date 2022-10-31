# We import random to generate a random account number ever time a new account is created.
import random
# We import regular expressions so we can replace the first 4 characters of the account when we display it to the user.
import re


class Account:
    def __init__(self, first_name, last_name, password, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.balance = balance
        self.number = ''

    def get_balance(self):
        return self.balance

    # This function is currently not necessary.
    # def set_account_name(self, first_name, last_name):
    #     self.first_name = first_name
    #     self.last_name = last_name

    def get_account_name(self):
        """
        We grab the account first and last name, and retrun it as an account's "full name" as a string.
        We use this frequently to verify login and display information to the user.
        """
        return f"{self.first_name} {self.last_name}"

    def set_account_number(self):
        """
        Here we are passing through the empty account number string and convert it into a random 8 digit int number.
        """
        number = []
        if self.number != '':
            return print("Account number is already set.")
        while len(number) < 8:
            number.append(random.randint(1, 9))
        number = int(''.join(map(str,number)))
        self.number = number

    def get_account_number(self):
        """
        We pass through the account number and convert the first 4 characters to display with "*". 
        We use a regular expression to find the numbers and replace them.
        Then returning the string to the user.
        """
        number = re.sub("(\d)", "*", str(self.number), 4)
        return number

    def get_account_number_raw(self):
        """
        Passthrough the account number.
        Here we needed a way for the logic on account confirmation identity to be able to read the actual account number without hidden digits.
        We return the account number, but it's only seen by the program looping for the correct account identity.
        """
        return self.number

    # This function is not currently being used.
    # def set_account_password():
    #     pass

    def get_account_password(self):
        """
        We passthrough the account password
        Returning the password, this is only to confirm we matched passwords during the login() function.
        """
        return self.password

    def set_deposit(self, amount):
        """
        Passthough the class account balance, and the money that is being deposited.
        There should be more validation here on the user input ammount.
        We update the account balance total, and return a string to the user diplaying the deposited amount and account balance total.
        """
        self.balance += round(float(amount), 2)
        print(f"You deposited {amount}$. Your balance is {self.balance}$")

    def set_withdraw(self, amount):
        """
        Passthrough the account balance and withdraw amount from the user.
        We check to see if the user has the available funds to withdraw.
        Return an NSF fee if the user doesn't have enough funds
        Return the debited amount and display the new updated balance to the user.
        """
        if self.balance < float(amount):
            self.balance -= 10
            amount = 0
            print(f"Ho ho ho ho, you didn't check your balance first. Thanks bucko, CHA CHING!\nCharged an NSF fee of 10$.\nNew balance: {self.balance}$")
            return amount
        else:
            tax = round(float(amount) * 1.5, 2)
            self.balance -= round(float(amount), 2) + tax
            print(f"You withdrew {amount}$. Your balance is {self.balance}$")
            return amount
    