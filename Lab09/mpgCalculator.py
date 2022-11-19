#!/user/bin/env python3

# Christian Luciano
# Cuyamaca College CS-119-0799
# Lab 2, exercise 1, Gas Mileage Calculator

from tkinter import *


def calc_mileage():
    # input
    miles = float(txtMiles.get())
    gallons = float(txtGallons.get())
    cost_per_gal = float(txtCostPerGal.get())

    # process
    mpg = miles / gallons
    total_fuel_cost = gallons * cost_per_gal
    cost_per_mile = total_fuel_cost / miles

    # output - note the string formatting
    str_mpg.set("{:.2f}".format(mpg))
    str_cpm.set("${:.2f}".format(cost_per_mile))
    str_tot_fuel_cost.set("${:.2f}".format(total_fuel_cost))


def exit_program():
    frm.destroy()


frm = Tk()
frm.title("Find Your MPG")
frm.geometry('450x200')  # form size

# add controls

lblMiles = Label(frm, text="Miles Driven", height=1, width=12)
lblMiles.grid(row=0, column=0)

txtMiles = Entry(frm, width=8)
txtMiles.grid(row=0, column=1)

lblGallons = Label(frm, text="Gallons Purchased", height=1, width=15)
lblGallons.grid(row=0, column=3)

txtGallons = Label(frm, text="Gallons purchased", height=1, width=8)
txtGallons.grid(row=0, column=1)

lblCostPerGal = Label(frm, text="Cost Per Gallon", height=1, width=12)
lblCostPerGal.grid(row=1, column=0)

txtCostPerGal = Entry(frm, width=8)
txtCostPerGal.grid(row=1, column=1)

lblTextMPG = Label(frm, text='Your MPG is: ', height=1, width=10)
lblTextMPG.grid(row=2, column=0)

str_mpg = StringVar()
lblMPG = Label(frm, text="", height=1, width=10, textvariable=str_mpg)
lblMPG.grid(row=2, column=1)

str_tot_fuel_cost = StringVar()
lblTextTotFuel = Label(frm, text="Total Fuel Cost:", height=1, width=12)
lblTextTotFuel.grid(row=3, column=0)

lblTotFuel = Label(frm, text='Total Fuel Cost:', height=1, width=12)
lblTotFuel.grid(row=3, column=1)

str_cpm = StringVar()
lblTextCPM = Label(frm, text='Cost per Mile', height=1, width=12)
lblTextCPM.grid(row=4, column=1)

lblCPM = Label(frm, text='Calculate', height=1, width=10, textvariable=str_cpm)
lblCPM.grid(row=4, column=1)

btnCalc = Button(frm, text="calculate",
                 command=calc_mileage, height=1, width=10)
btnCalc.grid(row=6, column=0)

btnExit = Button(frm, text="Exit", command=exit_program, height=1, width=10)
btnExit.grid(row=7, column=0)

frm.mainloop()


lblCPM = Label(frm, text="", height=1, width=10, textvariable=str_cpm)


# declare methods
# def get_miles_driven():
#     return float(input("How many miles did you drive? "))


# def get_number_of_gallons():
#     return float(input("How many gallons did you put in your tank? "))


# def get_price_per_gallon():
#     return float(input("How much is one gallon of gas? "))


# def calculate_total_cost(num_of_gal, price_per_gal):
#     return num_of_gal * price_per_gal


# def calculate_mpg(num_of_miles, num_of_gal):
#     return num_of_miles / num_of_gal


# def calculate_price_per_mile(total_cost, num_of_miles):
#     return total_cost / num_of_miles


# def main():
#     # input
#     miles_driven = get_miles_driven()
#     amount_of_gallons = get_number_of_gallons()
#     price_per_gallon = get_price_per_gallon()

#     # process
#     total_cost = calculate_total_cost(amount_of_gallons, price_per_gallon)
#     mpg = calculate_mpg(miles_driven, amount_of_gallons)
#     price_per_mile = calculate_price_per_mile(total_cost, miles_driven)

#     # output

#     print(
#         f'Your total cost is ${format(total_cost, ".2f")}. Your miles per gallon is {format(mpg, ".2f")}. Your price per mile is ${format(price_per_mile, ".2f")}')


# if __name__ == "__main__":
#     main()
