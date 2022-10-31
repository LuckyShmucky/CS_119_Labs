#!/user/bin/env python3

# Cuyamaca College CS-119
# Christian Luciano
# Lab 7 exercise 2 Test Pizza Class

from Pizza import Pizza

toppings = input('Enter toppings: ')
size = input('Enter size (small, meduim, large): ')
qty = input('Enter quantity: ')

my_pizza = Pizza(toppings, size, qty)

print(my_pizza.to_string())