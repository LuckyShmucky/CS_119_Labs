#!/user/bin/env python3

# Cuyamaca College CS-119
# Christian Luciano 
# Lab 8 exercise 2 Player Class Implementation

from Employee import Employee
from Student import Student

name = input('Enter name: ')
age = int(input('Enter age:'))
major = input('Enter major: ')
units = input('Enter units: ')
years_worked = input("Enter years worked: ")
job_skills = input("Enter job skills: ")

student = Student(name, age, major, units)
employee = Employee(name, age, job_skills, years_worked )

print(student.to_string())
print(employee.to_string())