#!/user/bin/env python3

# Cuyamaca College CS-119
# Christian Luciano 
# Lab 8 exercise 3 Person Class Implementation

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    def to_string(self):
        return f'Name: {self._name} Age: {self._age}'