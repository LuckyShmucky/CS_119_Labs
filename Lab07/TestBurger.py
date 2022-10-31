#!/user/bin/env python3

# Cuyamaca College CS-119
# Christian Luciano
# Lab 7 exercise 4 Testing Burger

from Burger import Burger

name = input('Enter customer name: ')
order_num = int(input('Enter order num: '))
type = input('Enter burger type: ')
qty = int(input('Enter amount: '))

my_burger = Burger(name, order_num, type, qty)

print(my_burger.to_string())
print(my_burger.calc_price())
