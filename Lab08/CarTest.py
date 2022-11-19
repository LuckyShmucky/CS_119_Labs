#!/user/bin/env python3

# Cuyamaca College CS-119
# Christian Luciano
# Lab 8 exercise 1 Automobile class implementation

from Convertible import Convertible

vin = input('What is the vin? ')
make = input('What is the make? ')
model = input('What is the model? ')
year = input('What is the year? ')
color = input('what is the color?')
is_top_up = input('Is the top up? ')


if is_top_up.upper() == "YES":
    is_top_up = True
else:
    is_top_up = False

my_car = Convertible(vin, make, model, color, is_top_up)

