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

    def check_pin(self, card_id : int  , pin : int):
        print("Checking pin...")
        result = self.bank_api.check_pin(card_id, pin)
        print("Checking pin Result: ", result)
        return result



if __name__ == '__main__':
    atm = SimpleATM()
    
    check_pin_status = atm.check_pin(1234, 1234)
