#!/user/bin/env python3

# Cuyamaca College CS-119
# Christian Luciano 
# Lab 8 exercise 2 Player Class Implementation

from Person import Person

class Student(Person):
    def __init__(self, name, age, major, units):
        super().__init__(name, age)
        self._major = major
        self._units = units
    
    def to_string(self):
        return super().to_string() + f'Major: {self._major} Units: {self._units}'