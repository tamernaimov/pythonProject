from Days.Days14.try3.Electronics import Electronics
from Days.Days14.try3.Electronicsabs import Electronicstab

class Phone(Electronicstab,Electronics):
    def __init__(self,year,model):
        super().__init__(year,model)

    def turn_on(self):
        print("ITS TURNED ON")

    def turn_off(self):
        print("ITS TURNED OFF")