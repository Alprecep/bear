# General 
Implemented based on Implementation_Instructions.md file give by Bear.
Typing: https://docs.python.org/3/library/typing.html
Documentation: https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html

# Clone the repository

git clone https://github.com/Alprecep/bear.git
cd bear

# Run tests
python3 tests.py

## Cases are tested in the following order:

## Test case 1: Initialize the class 
```
ATM initialized
```
## Test case 2:  insert card, insert pin, check pin
```
Test 2.0: no input inserted but check pin called
Check pin for no input inserted:  Card id and pin should be inserted first
Test 2.1: wrong pin inserted and check pin called
Check pin status wrong pin:  Card id and pin should be inserted first
Test 2.2: wrong id inserted and check pin called
Check pin status wrong card id:  False
Test 2.3: correct configuration inserted
Check pin status correct configuration:  Pin Correct and User Data Retrieved for Alp
```
## Test case 3: Insert correct card and pin, select account, see balance
```
Check pin status wrong card id:  Pin Correct and User Data Retrieved for Alp
Select account:  Account ID: 1234, Account Currency: USD, Account Balance: 1000
See balance:  1000
Deposit 100
See balance:  1100
Withdraw 200 Money withdrawn
See balance:  900
```
## Test case 4: 
```
Test case 4: select account, see balance, withdraw too much, deposit enough, withdraw enough
Check pin status wrong card id:  Pin Correct and User Data Retrieved for Alp
See balance:  1000
Select account:  Account ID: 1234, Account Currency: USD, Account Balance: 1000
Withdraw 2000:  Not enough money in the account
See balance:  1000
Deposit 5000
See balance:  6000
Withdraw 2000:  Money withdrawn
See balance:  4000
```
