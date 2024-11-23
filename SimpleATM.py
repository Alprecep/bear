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
from BankAPI import BankAPI
from UserData import UserData, BankAccount

class SimpleATM:
    """ This class represents a simple ATM"""
    def __init__(self):
        self.bank_api = BankAPI()
        self.cash_bin = 99999
        self.current_card_id = None
        self.current_pin = None

        self.user_data = UserData()

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
