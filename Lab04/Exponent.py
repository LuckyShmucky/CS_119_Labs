#!/user/bin/env python3

# Christian Luciano
# Cuyamaca College CS-119-0799
# Lab 4, Exponent

# declare methods, variables and constants

result = 1
ZEROTH_POWER = 0
number = 0
exponent = 0

# input 
number = int(input("Enter a number:"))
exponent = int(input("Raise you number the power of:"))

# process

while exponent > ZEROTH_POWER:
    result = result * number
    exponent -= 1

# output 
print(f'The result is {result}')
