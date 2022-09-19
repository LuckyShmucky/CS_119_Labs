#!/user/bin/env python3

# Christian Luciano
# Cuyamaca College CS-119-0799
# Lab 2, exercise 1, Text Message Cost Calculator


# declare variables
messages = 0
costPerMessage = 0.25
# cost per message is 25 cents
tax = 0.09
# tax is nine percent

# input
messages = float(input("Enter Total Messages: "))
# process
costPreTax = messages * costPerMessage
taxedAmount = costPreTax * tax
costPostTax = costPreTax + taxedAmount
# output
print(f'Your total is {costPostTax}')



