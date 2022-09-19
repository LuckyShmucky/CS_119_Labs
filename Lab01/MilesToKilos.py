#!/user/bin/env python3

# Christian Luciano
# Cuyamaca College CS-119-0799
# Lab 1, exercise 3, convert Miles to Kilometers

def MiletoKilo():
    # declare variables
    miles = 0
    multiplierNum = 1.60934

    # input
    miles = float(input("Enter Miles: "))

    # process
    product = miles * multiplierNum

    # output
    print(product)


MiletoKilo()
