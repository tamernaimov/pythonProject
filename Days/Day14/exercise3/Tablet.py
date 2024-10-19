from Days.Day14.try3.Electronics import Electronics
from Days.Day14.try3.Electronicsabs import Electronicstab

class Tablet(Electronicstab,Electronics):
    def __init__(self,year,model):
        super().__init__(year,model)

    def turn_on(self):
        print("ITS TURNED ON")

    def turn_off(self):
        print("ITS TURNED OFF")