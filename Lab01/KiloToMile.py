#!/user/bin/env python3

# Christian Luciano
# Cuyamaca College CS-119-0799
# Lab 1, exercise 2, convert Kilometers to Miles


def kiloToMile():
    # declare variables
    kilometers = 0
    multiplierNum = 0.62137

    # input
    kilometers = float(input("Enter Kilometers: "))

    # process
    product = kilometers * multiplierNum

    # output
    return product


print(kiloToMile())
