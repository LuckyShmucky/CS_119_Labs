#!/user/bin/env python3

# Cuyamaca College CS-119
# Christian Luciano
# Lab 7 exercise 2 Pizza class implementation

import Method as m 

class Pizza: 
    # parallel lists 
    __sizes = ['small', 'meduim', 'large']
    __prices = [8.00, 10.00, 12.00]
    
    def __init__(self, toppings, size, qty):
        self.__price = 0
        self.__toppings = toppings
        self.__qty = qty
        self.set_size(size)
    def get_toppings(self):
        return self.__toppings
    def set_toppings(self, toppings):
        self.__toppings = toppings
    def get_size(self):
        return self.__sizes
    def set_size(self, size):
        idx = m.find_string(self.__sizes, size)
        if idx >= 0:
            self.__price = self.__prices[idx]
            self.__size = size
        else:
            self.__size = self.__sizes[0]
            self.__price = self.__prices[0]
    def get_qty(self):
        return self.__qty
    def set_qty(self, qty):
        if qty < 0:
            qty = 0
        self.__qty = qty
    def get_price(self):
        return self.__price
    def calculate_price(self):
        return self.__price * float(self.__qty)
    def to_string(self):
        ext_price = self.calculate_price()
        return f'Toppings: {self.__toppings} Size: {self.__size} Qty: {self.__qty} Total Price: {ext_price}'


