# Clone the repository

git clone https://github.com/Alprecep/bear.git
cd bear

# Run tests
python3 tests.py

## Cases are tested in the following order:

## Test case 1: Initialize the class 

## Test case 2:
```
Test case 2: insert card, insert pin, check pin
Test 2.0: no input inserted
Check pin for no input inserted:  Card id and pin should be inserted first
Test 2.1: wrong pin inserted
Check pin status wrong pin:  Card id and pin should be inserted first
Test 2.2: wrong id inserted
Check pin status wrong card id:  False
Test 2.3: correct configuration inserted
Check pin status correct configuration:  Pin Correct and User Data Retrieved for Alp
```
## Test case 3: Insert correct card and pin, select account, see balance, deposit, withdraw
```
Test case 3: select account, see balance, deposit, withdraw
Check pin status wrong card id:  Pin Correct and User Data Retrieved for Alp
Select account:  Account ID: 1234, Account Currency: USD, Account Balance: 1000
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
