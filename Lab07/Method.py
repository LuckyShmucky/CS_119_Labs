#!/user/bin/env python3

# Cuyamaca College CS-119
# Christian Luciano
# Lab 6 exercise 1 Methods

def get_float_val(prompt):
    is_num = False
    str_val = input(prompt)
    while is_num == False:
        try:
            # if the user enters a value that is not a 
            # an int python will throw an error, therefore the except/catch code will execute instead of the try code
            
            value = float(str_val)
            is_num = True
        except: 
            print(str_val + ' is not a float')
            str_val = input(prompt)
    return value


def get_int_val(prompt):
    is_int = False 
    user_input = input(prompt)
    while is_int == False:
        try:
            value = int(user_input)
            is_int = True
        except:
            print(f'{user_input} is not an integer')
            user_input = input(prompt)
    return value


def find_string(list, find_char):
    idx = -1
    for i in list:
        if i.upper() == find_char.upper():
            idx = list.index(i)
            break
    return idx

def find_int(list, find_int):
    idx = -1
    for num in list:
        if int(num) == int(find_int):
            idx = list.index(num)
            break
    return idx

