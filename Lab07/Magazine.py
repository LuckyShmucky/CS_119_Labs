#!/user/bin/env python3

# Cuyamaca College CS-119
# Christian Luciano
# Lab 7 exercise 1 Magazine class implementation


class Magazine():
    def __init__(self, subscriber_name, magazine_title, months_remaining):
        self.__subscriber_name = subscriber_name
        self.__magazine_title = magazine_title
        self.__months_remaining = months_remaining
    # getters

    def get_subscriber_name(self):
        return self.__subscriber_name

    def get_magazine_title(self):
        return self.__magazine_title

    def get_months_remaining(self):
        return self.__months_remaining
    # setters

    def set_subsriber_name(self, newName):
        self.__subscriber_name = newName

    def set_magazine_title(self, newName):
        self.__magazine_title = newName

    def set_months_remaining(self, months):
        self.__months_remaining = months

    def to_string(self):
        return f'Subscriber name: {self.__subscriber_name} Magazine Title: {self.__magazine_title} Months Remaining: {self.__months_remaining}'