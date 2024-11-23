""" 
This module contains a simple ATM class that allows a user to:
    insert card,
    make them insert pin,
    check their balance, 
    deposit money, 
    withdraw money. 

Typing: https://docs.python.org/3/library/typing.html
Documentation: https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html

"""

# This BankApi class is a dummy class that simulates a bank API that allows a simple atm to be tested
class BankAPI:
    """ This class is a mockup of a bank API that allows a simple atm to be tested"""
    def __init__(self):
        self.user_data_1 = CurrentUserData()
        self.user_data_1.user_name = 'Alp'
        self.user_data_1.accounts[0].account_id = 1234
        self.user_data_1.accounts[0].account_currency = 'USD'
        self.user_data_1.accounts[0].account_balance = 1000

    
    def check_pin(self, card_id : int, pin : int) -> bool:
        """ This method checks if the pin is correct for the given card_id
            Args:
                card_id: The card id
                pin: The pin
            Returns: 
                bool true if the pin is correct
        """
        if card_id == self.user_data_1.accounts[0].account_id and pin == 1234:
            return True
        return False
    
    def get_user_data(self, card_id, pin):
        """ This method returns the user data for the given card_id and pin
            Args:
                card_id: The card id
                pin: The pin
            Returns:
                CurrentUserData: The user data
        """
        if self.check_pin(card_id, pin):
            return self.user_data_1
        
    def update_user_balance(self, user_data, account_id, amount):
        """ This method updates the user data
            Args:
                user_data: The user data
                account_id: The account id
                amount: The amount to be updated
            Returns:
                bool: True if the update is successful
        """
        if user_data.user_name != self.user_data_1.user_name:
            return False
        self.user_data_1.accounts[account_id].account_balance += amount
        return True

# Following code is a simple ATM class that allows a user to:
class BankAccount:
    """ This class represents a bank account"""
    def __init__(self):
        self.account_id = None
        self.account_currency = None
        self.account_balance = None
    def __str__(self):
        return f"Account ID: {self.account_id}, Account Currency: {self.account_currency}, Account Balance: {self.account_balance}"

class CurrentUserData:
    """ This class represents the current user data"""
    def __init__(self):
        self.user_name = None
        self.accounts = [BankAccount()]
    def custom_deepcopy(self):
        """ This method deep copies the user data without the library"""
        user_data = CurrentUserData()
        user_data.user_name = self.user_name
        user_data.accounts = [BankAccount()]
        # iterate over the all the accounts and copy them
        for i in range(len(self.accounts)):
            user_data.accounts[i].account_id = self.accounts[i].account_id
            user_data.accounts[i].account_currency = self.accounts[i].account_currency
            user_data.accounts[i].account_balance = self.accounts[i].account_balance
        return user_data
    
class SimpleATM:
    """ This class represents a simple ATM"""
    def __init__(self):
        self.bank_api = BankAPI()
        self.cash_bin = 99999
        self.current_card_id = None
        self.current_pin = None

        self.user_data = CurrentUserData()

    def check_pin(self):
        """ This method checks the pin
            Returns: true for correct pin, false for incorrect pin
        """
        check_pin_status = ""
        if self.current_card_id == None or self.current_pin == None:
            check_pin_status = "Card id and pin should be inserted first"
            return check_pin_status
        check_pin_status = self.bank_api.check_pin(self.current_card_id, self.current_pin)

        if check_pin_status:
            from_api = (self.bank_api.get_user_data(self.current_card_id, self.current_pin))
            self.user_data = from_api.custom_deepcopy()
            check_pin_status = "Pin Correct and User Data Retrieved for " + self.user_data.user_name

        return check_pin_status
    
    def insert_card(self, card_id : int) -> str:
        """ This method for inserting the card id, the id is read by the card reader and passed to the atm
            Args:
                card_id: The card id
            Returns:
                str: The status of the card insertion
        """
        insert_card_status = ""
        if card_id < 1000 or card_id > 9999:
            insert_card_status = "Invalid card id, expected 4 digit card id"
        self.current_card_id = card_id
        return insert_card_status
    def insert_pin(self, pin : int) -> bool:
        """ This method for inserting the pin received from the user
            Args:
                pin: The pin
        """
        pin_status = ""
        if pin < 1000 or pin > 9999:
            pin_status = "Invalid pin, input should be 4 digit pin" 
        else: 
            self.current_pin = pin
            pin_status = "Pin inserted"

        return pin_status
    def select_account(self, account_number : int) -> BankAccount:
        """ This method for selecting the account
            Args:
                account_number: The account number
        """
        account = self.user_data.accounts[account_number]
        return account

    def see_balance(self, account_number : int) -> int:
        """ This method for checking the balance
            Args:
                account_number: The account number
            Returns:
                int: The account balance
        """
        account = self.user_data.accounts[account_number]
        return account.account_balance
    
    def deposit(self, account_number : int, amount : int) -> str:
        """ This method for depositing the money
            Args:
                account_number: The account number
                amount: The amount to be deposited
            Returns:
                str: status of deposit 
        """
        deposit_status = self.bank_api.update_user_balance(self.user_data, account_number, amount)
        
        if deposit_status:
            self.cash_bin += amount
            self.user_data.accounts[account_number].account_balance += amount
            
        return deposit_status

    def withdraw(self, account_number : int, amount : int)-> str:
        """ This method for withdrawing the money
            Args:
                account_number: The account number
                amount: The amount to be withdrawn
            Returns:
                str: status of withdraw
        """
        withdraw_status = ""  
        if self.cash_bin >= amount: # Check if there is enough money in the ATM
            if self.user_data.accounts[account_number].account_balance >= amount: # Check if there is enough money in the account
        
                withdraw_status = self.bank_api.update_user_balance(self.user_data, account_number, -amount)
                if withdraw_status:
                    self.cash_bin -= amount
                    self.user_data.accounts[account_number].account_balance -= amount
                    withdraw_status = "Money withdrawn"
                else: 
                    withdraw_status = "API error"
            else: 
                withdraw_status = "Not enough money in the account"
        else:
            withdraw_status  = "Not enough money in the ATM"

        return withdraw_status
