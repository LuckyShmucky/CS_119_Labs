#!/user/bin/env python3

# Cuyamaca College CS-119
# Christian Luciano 
# Lab 8 exercise 2 Player Class Implementation

class Player:
    def __init__(self, name, number):
        self._name = name
        self.set_number(number)
    
    def get_name(self):
        return self._name 
    def set_name(self, name):
        self._name = name
    def get_number(self):
        return self.get_number
    def set_number(self, number):
        MIN_NUMBER = 1
        MAX_NUMBER = 9999
        if number >= MIN_NUMBER and number <= MAX_NUMBER:
            self._number = number
        else: 
            self._number = MIN_NUMBER
            
    def to_string(self):
        return f'Name: {self._name} Number: {str(self._number)}'