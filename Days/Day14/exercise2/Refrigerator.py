from Days.Day14.try2.Appliance import Appliance
from Days.Day14.try2.Brand import  Brand

class Refrigerator(Appliance,Brand):
    def __init__(self,year):
        super().__init__(year)


    def turn_on(self):
        print("Refrigerator is now ON.")

    def turn_off(self):
        print("Refrigerator is now OFF.")