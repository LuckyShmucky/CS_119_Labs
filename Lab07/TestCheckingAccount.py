#!/user/bin/env python3

# Cuyamaca College CS-119
# Christian Luciano
# Lab 7 exercise 3 Test Checking Account

from CheckingAccount import CheckingAccount

account_num = int(input('What is the account number: '))
client_name = input('Enter client name: ')
client_address = input('Enter client address: ')
initial_balance = int(input('Enter the initial balance: '))
transaction = input('Is this transaction a credit or debit? ')
my_account = CheckingAccount(
    account_num, client_name, client_address, initial_balance)
print(my_account.to_string())
if transaction == 'credit':
    print(my_account.credit())
elif transaction == 'debit':
    print(my_account.debit())
else:
    print('not a valid payment type')
