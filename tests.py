from SimpleATM import SimpleATM

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
print("Select account: ", select_account)

see_balance = atm.see_balance(0)
print("See balance: ", see_balance)

atm.deposit(0, 100)
print("Deposit 100")

see_balance = atm.see_balance(0)
print("See balance: ", see_balance)

withdraw_status = atm.withdraw(0, 200)
print("Withdraw 200", withdraw_status)

see_balance = atm.see_balance(0)
print("See balance: ", see_balance)

# Test case 4: select account, see balance, withdraw too much, deposit enough, withdraw enough
print("*****************************")
print("Test case 4: select account, see balance, withdraw too much, deposit enough, withdraw enough")
del atm
atm = SimpleATM()
atm.insert_card(1234)
atm.insert_pin(1234)
check_pin_status = atm.check_pin()
print("Check pin status wrong card id: ", check_pin_status)

see_balance = atm.see_balance(0)
print("See balance: ", see_balance)

select_account = atm.select_account(0)
print("Select account: ", select_account)

withdraw_status = atm.withdraw(0, 2000)
print("Withdraw 2000: ", withdraw_status)

see_balance = atm.see_balance(0)
print("See balance: ", see_balance)

atm.deposit(0, 5000)
print("Deposit 5000")

see_balance = atm.see_balance(0)
print("See balance: ", see_balance)

withdraw_status = atm.withdraw(0, 2000)
print("Withdraw 2000: ", withdraw_status)

see_balance = atm.see_balance(0)
print("See balance: ", see_balance)

del atm
