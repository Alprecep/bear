
"""
This BankApi class is a dummy class that simulates a bank API that allows a simple atm to be tested

"""
from UserData import UserData

class BankAPI:
    """ This class is a mockup of a bank API that allows a simple atm to be tested"""
    def __init__(self):
        self.user_data_1 = UserData()
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
