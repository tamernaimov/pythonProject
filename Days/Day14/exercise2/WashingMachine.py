from Days.Day14.try2.Appliance import Appliance
from Days.Day14.try2.Brand import  Brand

class WashingMachine(Appliance,Brand):
    def turn_on(self):
        print("Washing Machine is now ON.")

    def turn_off(self):
        print("Washing Machine is now OFF.")

