#!/user/bin/env python3

# Cuyamaca College CS-119
# Christian Luciano 
# Lab 8 exercise 2 Player Class Implementation

from BaseballPlayer import BaseballPlayer
name = input('Enter Name: ')
number = int(input('Enter number: '))
position = input('Enter position: ')
batting_avg = float(input('Enter batting average: '))

my_player = BaseballPlayer(name, number,  position, batting_avg)

print(my_player.to_string())