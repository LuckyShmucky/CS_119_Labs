#!/user/bin/env python3

# Christian Luciano
# Cuyamaca College CS-119-0799
# Lab 3, exercise 3, Coyote Inn

# declare variables and constants
num_of_nights = int(input('How many nights will you be staying?'))
month = int(input('What month are you planning your trip to be? '))
cost_per_night = 0
total_cost = 0
# process
if month >= 1 and month <= 3:
    cost_per_night = 80
elif month >= 4 and month <= 6:
    cost_per_night = 90
elif month >= 7 and month <= 9:
    cost_per_night = 120
elif month >= 10 and month <= 12:
    cost_per_night = 100
else:
    print('that is not a month')

total_cost = num_of_nights * cost_per_night
print(str(total_cost))
