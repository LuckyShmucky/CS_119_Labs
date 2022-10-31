#!/user/bin/env python3

# Cuyamaca College CS-119
# Christian Luciano
# Lab 7 exercise 3 Checking Account



class CheckingAccount: 
    
    def __init__(self, account_num, client_name, client_address, initial_balance):
        self.__account_num = account_num
        self.__client_name = client_name
        self.__client_address = client_address
        self.__initial_balance = initial_balance
    
    def get_account_num(self):
        return self.__account_num
    def get_client_name(self):
        return self.__client_name
    def get_client_address(self):
        return self.__client_address
    def get_initial_balance(self):
        return self.__initial_balance
    def set_account_num(self, account_num):
        self.__account_num = account_num
    def set_client_name(self, name):
        self.__client_name = name
    def set_client_address(self, address):
        self.__client_address = address
    def set_initial_balance(self, balance):
        self.__initial_balance = balance
    def credit(self):
        return 'this transaction is a credit'
    def debit(self):
        return 'this transaction is debit'
    def to_string(self):
        return f'Account number for {self.__client_name} is {self.__account_num}. Their address is {self.__client_address}. Their initial balance was {self.__initial_balance}.'
    
