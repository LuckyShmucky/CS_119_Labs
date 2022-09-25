#!/user/bin/env python3

# Cuyamaca College CS-119
# Christian Luciano
# Lab 5 dice game

import random

# variables and constants

MAX_ROLLS = 5
MAX_DICE_VAL = 6
pMax = 0
cMax = 0
pCounts = {}
cCounts = {}
# list for roll types

roll_types = {"Junk", "Pair", "3 of a kind", "4 of a kind", "5 of a kind"}

# declare lists for dice rolls and their tally
pdice = [0, 0, 0, 0, 0]
cdice = [0, 0, 0, 0, 0]


# process
# roll the dice using random
i = 0
while i < MAX_ROLLS:
    roll_val = random.randint(1, MAX_DICE_VAL)
    pdice[i] = roll_val
    roll_val = random.randint(1, MAX_DICE_VAL)
    cdice[i] = roll_val
    i += 1

# display rolls to user
for roll in pdice:
    print(f'Player rolled: {roll}')

for roll in cdice:
    print(f'Computer rolled: {roll}')


# for every element in the pdice array (all the rolls for the player) check to see if it exists in an empty object declared earlier
for roll_num in pdice:
    # if this key already exists in our object, add one to the value
    if roll_num in pCounts:
        pCounts[roll_num] += 1
    # if the key does not exist in the pCounts object, declare a new propert with the key being the value of the side of the die that was rolled
    # and the value of that same property being 1 (each time this key is seen in this loop after this had 1 added to it's total times it was rolled)
    else:
        pCounts[roll_num] = 1


for key in pCounts:
    # if a one of the properties in the pCounts object has a value larger than the current pMax, that property becomes the new pMax
    if pCounts[key] > pMax:
        pMax = pCounts[key]


for roll_num in cdice:
    if roll_num in cCounts:
        cCounts[roll_num] += 1
    else:
        cCounts[roll_num] = 1

for key in cCounts:
    if cCounts[key] > cMax:
        cMax = cCounts[key]

if pMax > cMax:
    print("Player wins!")
elif cMax > pMax:
    print("Computer wins!")
else:
    print("Tie!")
