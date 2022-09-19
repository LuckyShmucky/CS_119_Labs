#!/user/bin/env python3

# Christian Luciano
# Cuyamaca College CS-119-0799
# Lab 4, exercise 1, Factorial

# declare methods, variables and constants

factorial = 0
result = 1
factorial = int(input("Enter a number:"))
# process

for num in range(factorial, 0, -1):
    result = result * num


# output
print(f'the result is{result}')
