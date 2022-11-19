#!/user/bin/env python3

# Cuyamaca College CS-119
# Christian Luciano 
# Lab 8 exercise 2 Player Class Implementation

from Player import Player

class BasketballPlayer(Player):
    def __init__(self, name, number, position, free_throw_pct):
        super().__init__(name, number)
        self._position = position
        self._free_throw_pct = free_throw_pct
    
    def get_position(self):
        return self._position
    def set_position(self, position):
        self._position = position
    def get_batting_avg(self):
        return self._batting_avg
    def set_batting_avg(self, free_throw_pct):
        self._free_throw_pct = free_throw_pct
    def to_string(self):
        return super().to_string() + f'Position {self._position} Batting Avg: {str(self._free_throw_pct)}'
    
    
name = input('Enter Name: ')
number = int(input('Enter number: '))
position = input('Enter position: ')
free_throw_pct = float(input('free throw percentage: '))

my_player = BasketballPlayer(name, number,  position, free_throw_pct)
print(my_player.to_string())