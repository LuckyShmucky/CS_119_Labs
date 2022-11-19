#!/user/bin/env python3

# Cuyamaca College CS-119
# Christian Luciano 
# Lab 8 exercise 2 Automobile class (Race care Extension)

from Automobile import Automobile

class RaceCar(Automobile):
    def __init__(self, vin, make, model, color, horse_power):
        super().__init__(vin, make, model, color)
        self._horse_power = horse_power
        
    def get_horse_power(self):
        return self._horse_power
    def set_horse_power(self, horse_power):
        self._horse_power = horse_power
    
    def to_string(self):
        return super().to_string() \
            + '\nIs top up? ' + self.get_horse_power()
    


vin2 = input('What is the vin? ')
make2 = input('What is the make? ')
model2 = input('What is the model? ')
year2 = input('What is the year? ')
color2 = input('what is the color?')
horse_power = input('How many horses? ')
race_car = RaceCar(vin2, make2, model2, color2, horse_power)
print(race_car.to_string())
