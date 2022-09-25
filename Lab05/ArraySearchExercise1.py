#!/user/bin/env python3

# Cuyamaca College CS-119
# Christian Luciano
# Lab 5 exercise 1 parallel array search

# create parallel lists of zip codes and the corresponding cities and states
zips = [53115, 53125, 53147, 53148]
cities = ["Delevan", "Fontana", "Lake Geneva", "Walworth"]
states = ["WI", "WI", "IL", "IL"]

# other variables
zip_code = 0
city = "Not Found"
state = ' '
found = False
iteration = 0
list_len = len(zips)
# input
zip_code = int(input("Enter the zip code: "))

# use a loop to find a matching array

while iteration < list_len and found == False:
    if zip_code == zips[iteration]:
        city = cities[iteration]
        state = states[iteration]
        found = True
    iteration = iteration + 1

# output
print(f"Zip: {zip_code} City: {city} State: {state}")
