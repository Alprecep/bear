# Following code is a simple ATM class that allows a user to:
class BankAccount:
    """ This class represents a bank account"""
    def __init__(self):
        self.account_id = None
        self.account_currency = None
        self.account_balance = None
    def __str__(self):
        return f"Account ID: {self.account_id}, Account Currency: {self.account_currency}, Account Balance: {self.account_balance}"

class UserData:
    """ This class represents the current user data"""
    def __init__(self):
        self.user_name = None
        self.accounts = [BankAccount()]
    def custom_deepcopy(self):
        """ This method deep copies the user data without the library"""
        user_data = UserData()
        user_data.user_name = self.user_name
        user_data.accounts = [BankAccount()]
        # iterate over the all the accounts and copy them
        for i in range(len(self.accounts)):
            user_data.accounts[i].account_id = self.accounts[i].account_id
            user_data.accounts[i].account_currency = self.accounts[i].account_currency
            user_data.accounts[i].account_balance = self.accounts[i].account_balance
        return user_data
    