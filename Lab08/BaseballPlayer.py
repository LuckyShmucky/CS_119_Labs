#!/user/bin/env python3

# Cuyamaca College CS-119
# Christian Luciano 
# Lab 8 exercise 2 Player Class Implementation

from Player import Player

class BaseballPlayer(Player):
    def __init__(self, name, number, position, batting_avg):
        super().__init__(name, number)
        self._position = position
        self._batting_avg = batting_avg
    
    def get_position(self):
        return self._position
    def set_position(self, position):
        self._position = position
    def get_batting_avg(self):
        return self._batting_avg
    def set_batting_avg(self, batting_avg):
        self._batting_avg = batting_avg
    def to_string(self):
        return super().to_string() + f'Position {self._position} Batting Avg: {str(self._batting_avg)}'
