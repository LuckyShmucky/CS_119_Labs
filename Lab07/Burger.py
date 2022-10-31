#!/user/bin/env python3

# Cuyamaca College CS-119
# Christian Luciano
# Lab 7 exercise 4 Burger

class Burger:
    types = {
        'veggie': 2,
        'bacon': 3,
        'double': 5
    }

    def __init__(self, customer_name, order_num, type, qty):
        self.__customer_name = customer_name
        self.__order_num = order_num
        self.__type = type
        self.__qty = qty

    def get_customer_name(self):
        return self.__customer_name

    def get_order_num(self):
        return self.__order_num

    def get_type(self):
        return self.__type

    def get_qty(self):
        return self.__qty

    def calc_price(self):
        if self.__type in self.types:
            return self.__qty * self.types[self.__type]
        else:
            return 'we do not serve that kind of burger'

    def set_customer_name(self, name):
        self.__customer_name = name

    def set_order_num(self, number):
        self.__order_num = number

    def set_type(self, type):
        self.__type = type

    def set_qty(self, qty):
        self.__qty = qty

    def to_string(self):
        return f'Order {self.__order_num} is for {self.__customer_name}. They ordered {self.__qty} {self.__type}(s).'
