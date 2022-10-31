from account import Account

class Bank:
    def __init__(self):
        self.accounts = [
            Account("Brian", "Cahill", "Big-Daddy69", 47000042),
            Account("Josh", "Faigan", "Charmander4Life", 55555555),
            Account("Andrew", "Alsing", "Vu/n3r@b/3-S3cur1\y", 69696969),
            Account("Alex", "Rocha", "PwningN00bs", 81680085)
        ]
        
    def set_new_account(self, first_name, last_name, password, balance):
        """
        Pass through a first name, last name, password, and balance amount.
        Using all these passed through variables we can then instanciate a new account class that gets appened to the Bank.accounts array.
        """
        self.accounts.append(Account(first_name, last_name, password, balance))

    def transfer(self, name_from, name_to, amount):
        """
        Pass through the full name of the account FROM, the full name of the account TO, and the amount being tranfered.
        We then loop through the bank acounts to find the coresponding accounts and deposit/withdraw the amount entered by the user.
        We hold onto the transfer amout incase the withdraw account has insufficient funds. We need a way to tell if it wasn't withdrawn, 
        and we need to make sure nothing gets deposited if the withdraw doesn't happen.
        Retrun the final amount to display correctly in the printed phrase for the user. 
        """
        for name in self.accounts:
            if name.get_account_name() == name_from:
                amount = name.set_withdraw(amount)
            if name.get_account_name() == name_to:
                name.set_deposit(amount)
        return amount

    def add_interest(self, account_number):
        """
        Pass through the Bank accounts list, and the account number we are generating interest for.
        Loop through and catch the correct account, apply the interest.
        Return that interest was applied with the amount to the user.
        """
        for account in self.accounts:
            if account.get_account_number_raw() == account_number:
                interest_amount = account.generate_interest()
                print(f"Collected {interest_amount}$ in transaction interest. Thanks!\n")
    
    def add_account_numbers(self):
        """
        Pass through the bank accounts array
        Using the account class method we update all the accounts that pre-exist whenever the bank class is run with new random account numbers.
        This was to have the account numbers be unique, and not instanciate inside the constructor, but rather only when we use the randomizer method.
        """
        for name in self.accounts:
            name.set_account_number()

    def statement(self, account_number):
        """
        Pass through the account number of the user and the Bank accounts array.
        Assemble a print message of the account details for the user's account. 
        This should show the user's full name, display the account number with the first 4 didgits hidden, and their balance total.
        Return the printed string to the user.
        """
        for name in self.accounts:
            if account_number == name.get_account_number_raw():
                print(f"""
|----------------------------------------------------|
 Your name:             |{name.get_account_name()}
 Your account number:   |{name.get_account_number()}
 Your balance:          |{round(name.get_balance(), 2)}$
|----------------------------------------------------|
                """)


