""" This module contains a simple ATM class that allows a user to:
     insert card,
     make them insert pin,
     check their balance, 
     deposit money, 
     withdraw money. """


class BankAPI:
    """ This class is a mockup of a bank API that allows a simple atm to be tested"""
    def __init__(self):
        self.user_data_1 = CurrentUserData()
        self.user_data_1.user_name = 'Alp'
        self.user_data_1.accounts[0].account_id = 1234
        self.user_data_1.accounts[0].account_currency = 'USD'
        self.user_data_1.accounts[0].account_balance = 1000

    
    def check_pin(self, card_id, pin):
        if card_id == self.user_data_1.accounts[0].account_id and pin == 1234:
            return True
        return False
    
    def get_user_data(self, card_id, pin):
        if self.check_pin(card_id, pin):
            return self.user_data_1


# Following code is a simple ATM class that allows a user to:
class BankAccount:
    def __init__(self):
        self.account_id = None
        self.account_currency = None
        self.account_balance = None

class CurrentUserData:
    def __init__(self):
        self.user_name = None
        self.accounts = [BankAccount()]

class SimpleATM:
    def __init__(self):
        self.bank_api = BankAPI()
        self.cash_bin = 999
        self.current_card_id = None
        self.current_pin = None
        self.current_account_id = None

        self.user_data = CurrentUserData()

    def check_pin(self):
        print("Checking pin...")
        result = self.bank_api.check_pin(self.current_card_id, self.current_pin)
        print("Checking pin Result: ", result)

        if result:
            self.user_data = self.bank_api.get_user_data(self.current_card_id, self.current_pin)
            print("User Data: ", self.user_data.user_name)

        return result
    
    def insert_card(self, card_id : int):
        print("Inserting card...")
        self.current_card_id = card_id
        print("Card inserted")
        
    def insert_pin(self, pin : int):
        print("Inserting pin...")
        self.current_pin = pin
        print("Pin inserted")

    def select_account(self, account_number : int):
        print("Selecting account...")
        account = self.user_data.accounts[account_number]

        print("Account ID: ", account.account_id)
        print("Balance: ", account.account_balance)
        print("Currency: ", account.account_currency)
        print("Account selected")

if __name__ == '__main__':
    atm = SimpleATM()
    
    atm.insert_card(1234)
    atm.insert_pin(1234)
    check_pin_status = atm.check_pin()
    select_account = atm.select_account(0)
