#!/user/bin/env python3

# Cuyamaca College CS-119
# Christian Luciano
# Lab 7 exercise 1 Magazine class test fixture

from Magazine import Magazine

subsrciber_name = input('Enter subscriber name: ')
magazine_title = input('Enter magazine title: ')
months_remaining = int(input('Enter months remaining : '))

# create an instance of a magazine
my_magazine = Magazine(subsrciber_name, magazine_title, months_remaining)

# invoke to_string() method and display everything
print(my_magazine.to_string())
