#!/user/bin/env python3

# Christian Luciano
# Cuyamaca College CS-119-0799
# Lab 3, exercise 1, Portriat Studio

# declare methods, variables and constants
SURCHARGE = 1.2


def get_last_name():
    return str(input("What is the family's last name? "))


def get_day_of_week():
    return str(input("What day of the week are you usually available? "))


def get_num_of_subjects():
    return int(input("How many people will be in the photo? "))


def calculate_cost(num_of_subjects, day_of_week):
    price = 0
    if num_of_subjects < 1:
        print('Someone has to be in the picture')
        return
    elif num_of_subjects == 1:
        price = 100
    elif num_of_subjects == 2:
        price = 130
    elif num_of_subjects == 3:
        price = 150
    elif num_of_subjects == 4:
        price = 165
    elif num_of_subjects == 5:
        price = 175
    elif num_of_subjects == 6:
        price = 180
    else:
        price = 185
    # add additional charge for weekends
    if day_of_week == "Saturday" or day_of_week == "Sunday":
        price = price * SURCHARGE
    return price


def main():

    # input
    last_name = get_last_name()
    day_of_week = get_day_of_week()
    num_of_subjects = get_num_of_subjects()
# process
    final_price = calculate_cost(num_of_subjects, day_of_week)
# output
    print(last_name, final_price)


if __name__ == "__main__":
    main()
