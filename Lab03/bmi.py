#!/user/bin/env python3

# Christian Luciano
# Cuyamaca College CS-119-0799
# Lab 3, exercise 2, BMI Calculator

# declare variables and constants
bmi = 0
meters = 0
kilograms = 0
INCHES_TO_METERS = 39.36
LBS_TO_KILOS = 2.2
# input
pounds = float(input("How many pounds do you weigh? "))
height_in_inches = float(input("how tall are you in inches? "))

# process
meters = height_in_inches / INCHES_TO_METERS
kilograms = pounds / LBS_TO_KILOS
bmi = kilograms / (meters * meters)

if bmi < 18.5:
    print('You are under weight')
elif bmi >= 18.5 and bmi < 25:
    print("You are at a normal weight")
elif bmi >= 25 and bmi < 30:
    print("You are over weight")
elif bmi >= 30 and bmi < 40:
    print("You are obese")
else:
    print("You are morbidly obese")
