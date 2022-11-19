#!/user/bin/env python3

# Cuyamaca College CS-119
# Christian Luciano 
# Lab 8 exercise 1 Automobile class implementation

from Automobile import Automobile

class Convertible(Automobile):
    def __init__(self, vin, make, model, color, is_top_up, messy_hair):
        super().__init__(vin, make, model, color)
        self._is_top_up = is_top_up
        if self._is_top_up == True:
            set_messy_hair(messy_hair)            
            
    def set_messy_hair(self, hair):
        self._messy_hair = hair
    def get_is_top_up(self):
        return self._is_top_up
    def set_is_top_up(self, is_top_up):
        self._is_top_up = is_top_up
    
    def fmt_top_status(self):
        status = 'No'
        if self._is_top_up == True:
            status = 'Yes'
        return status
    
    def to_string(self):
        return super().to_string() \
            + '\nIs top up? ' + self.fmt_top_status()
