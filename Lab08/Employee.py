#!/user/bin/env python3

# Cuyamaca College CS-119
# Christian Luciano 
# Lab 8 exercise 2 Player Class Implementation
from Person import Person

class Employee(Person):
    def __init__(self, name, age, job_skills, years_worked):
        super().__init__(name, age)
        self._job_skills = job_skills
        self._years_worked = years_worked
    
    def to_string(self):
        return super().to_string() + f'Years worked: {self._years_worked} Job Skills: {self._job_skills}'
    