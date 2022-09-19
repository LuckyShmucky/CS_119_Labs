#!/user/bin/env python3

# Christian Luciano
# Cuyamaca College CS-119-0799
# Lab 2, exercise 1, Gas Mileage Calculator

# declare methods
def get_miles_driven():
    return float(input("How many miles did you drive? "))


def get_number_of_gallons():
    return float(input("How many gallons did you put in your tank? "))


def get_price_per_gallon():
    return float(input("How much is one gallon of gas? "))


def calculate_total_cost(num_of_gal, price_per_gal):
    return num_of_gal * price_per_gal


def calculate_mpg(num_of_miles, num_of_gal):
    return num_of_miles / num_of_gal


def calculate_price_per_mile(total_cost, num_of_miles):
    return total_cost / num_of_miles


def main():
    # input
    miles_driven = get_miles_driven()
    amount_of_gallons = get_number_of_gallons()
    price_per_gallon = get_price_per_gallon()

    # process
    total_cost = calculate_total_cost(amount_of_gallons, price_per_gallon)
    mpg = calculate_mpg(miles_driven, amount_of_gallons)
    price_per_mile = calculate_price_per_mile(total_cost, miles_driven)

    # output

    print(
        f'Your total cost is ${format(total_cost, ".2f")}. Your miles per gallon is {format(mpg, ".2f")}. Your price per mile is ${format(price_per_mile, ".2f")}')


if __name__ == "__main__":
    main()
