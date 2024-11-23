""" This module contains a simple ATM class that allows a user to:
     insert card,
     make them insert pin,
     check their balance, 
     deposit money, 
     withdraw money. """
# TODO: add documnetation to the methods


# This BankApi class is a dummy class that simulates a bank API that allows a simple atm to be tested
class BankAPI:
    """ This class is a mockup of a bank API that allows a simple atm to be tested"""
    def __init__(self):
        self.user_data_1 = CurrentUserData()
        self.user_data_1.user_name = 'Alp'
        self.user_data_1.accounts[0].account_id = 1234
        self.user_data_1.accounts[0].account_currency = 'USD'
        self.user_data_1.accounts[0].account_balance = 1000

    
    def check_pin(self, card_id, pin):
        """ This method checks if the pin is correct for the given card_id"""
        if card_id == self.user_data_1.accounts[0].account_id and pin == 1234:
            return True
        return False
    
    def get_user_data(self, card_id, pin):
        """ This method returns the user data for the given card_id and pin"""
        if self.check_pin(card_id, pin):
            return self.user_data_1
        
    def update_user_balance(self, user_data, account_id, amount):
        """ This method updates the user data"""
        user_data.accounts[account_id].account_balance += amount
        pass

# Following code is a simple ATM class that allows a user to:
class BankAccount:
    """ This class represents a bank account"""
    def __init__(self):
        self.account_id = None
        self.account_currency = None
        self.account_balance = None

class CurrentUserData:
    """ This class represents the current user data"""
    def __init__(self):
        self.user_name = None
        self.accounts = [BankAccount()]

class SimpleATM:
    """ This class represents a simple ATM"""
    def __init__(self):
        self.bank_api = BankAPI()
        self.cash_bin = 999
        self.current_card_id = None
        self.current_pin = None

        self.user_data = CurrentUserData()

    def check_pin(self):
        """ This method checks the pin"""
        check_pin_status = ""
        if self.current_card_id == None or self.current_pin == None:
            check_pin_status = "Card id and pin should be inserted first"
            return check_pin_status
        check_pin_status = self.bank_api.check_pin(self.current_card_id, self.current_pin)

        if check_pin_status:
            self.user_data = self.bank_api.get_user_data(self.current_card_id, self.current_pin)
            print("Pin Correct and User Data Retrieved for: ", self.user_data.user_name)

        return check_pin_status
    
    def insert_card(self, card_id : int):
        """ This method for inserting the card id, the id is read by the card reader and passed to the atm"""
        insert_card_status = ""
        if card_id < 1000 or card_id > 9999:
            insert_card_status = "Invalid card id, expected 4 digit card id"
        self.current_card_id = card_id
        
    def insert_pin(self, pin : int):
        """ This method for inserting the pin received from the user"""
        pin_status = ""
        if pin < 1000 or pin > 9999:
            pin_status = "Invalid pin, input should be 4 digit pin" 
        else: 
            self.current_pin = pin
            pin_status = "Pin inserted"

        return pin_status
    def select_account(self, account_number : int):
        """ This method for selecting the account"""
        account = self.user_data.accounts[account_number]

        print("Account ID: ", account.account_id)
        print("Balance: ", account.account_balance)
        print("Currency: ", account.account_currency)

    def see_balance(self, account_number : int):
        """ This method for checking the balance"""
        account = self.user_data.accounts[account_number]
        print("Balance: ", account.account_balance)
        return account.account_balance
    
    def deposit(self, account_number : int, amount : int):
        """ This method for depositing the money"""
        
        deposit_status = self.bank_api.update_user_balance(self.user_data, account_number, amount)
        
        if deposit_status:
            self.cash_bin += amount
            self.user_data.accounts[account_number].account_balance += amount

        return deposit_status

    def withdraw(self, account_number : int, amount : int):
        """ This method for withdrawing the money"""

        withdraw_status = ""  
        if self.cash_bin >= amount: # Check if there is enough money in the ATM
            if self.user_data.accounts[account_number].account_balance >= amount: # Check if there is enough money in the account
        
                withdraw_status = self.bank_api.update_user_balance(self.user_data, account_number, -amount)
                if withdraw_status:
                    self.cash_bin -= amount
                    self.user_data.accounts[account_number].account_balance -= amount
                    withdraw_status = "Money withdrawn"
            else: 
                withdraw_status = "Not enough money in the account"
        else:
            withdraw_status  = "Not enough money in the ATM"

        return withdraw_status

if __name__ == '__main__':
    """ This is the main function that tests the SimpleATM class"""
    # Test the SimpleATM class

    # Test case 1: initialize the ATM
    print("*****************************")
    print("Test case 1: initialize the ATM")
    atm = SimpleATM()
    del atm

    # Test case 2: insert card, insert pin, check pin
    print("*****************************")
    print("Test case 2: insert card, insert pin, check pin")
    atm = SimpleATM()

    # test 2.0: no input
    print("Test 2.0: no input inserted")
    check_pin_status = atm.check_pin()
    print("Check pin for no input inserted: ", check_pin_status)
    
    # test 2.1: wrong pin
    print("Test 2.1: wrong pin inserted")
    atm.insert_card(1234)
    atm.insert_pin(0000)
    check_pin_status = atm.check_pin()
    print("Check pin status wrong pin: ", check_pin_status)
    
    # test 2.2: wrong id
    print("Test 2.2: wrong id inserted")
    atm.insert_card(0000)
    atm.insert_pin(1234)
    check_pin_status = atm.check_pin()
    print("Check pin status wrong card id: ", check_pin_status)
    
    # test 2.3: correct configuration
    print("Test 2.3: correct configuration inserted")
    atm.insert_card(1234)
    atm.insert_pin(1234)
    check_pin_status = atm.check_pin()
    print("Check pin status correct configuration: ", check_pin_status)
    
    del atm

    # Test case 3: select account, see balance, deposit, withdraw
    print("*****************************")
    print("Test case 3: select account, see balance, deposit, withdraw")
    atm = SimpleATM()
    atm.insert_card(1234)
    atm.insert_pin(1234)
    check_pin_status = atm.check_pin()
    print("Check pin status wrong card id: ", check_pin_status)
    
    select_account = atm.select_account(0)
    see_balance = atm.see_balance(0)
    atm.deposit(0, 100)
    see_balance = atm.see_balance(0)

    atm.withdraw(0, 200)
    see_balance = atm.see_balance(0)




