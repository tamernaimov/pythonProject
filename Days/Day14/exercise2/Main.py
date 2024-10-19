from Days.Day14.try2.Refrigerator import Refrigerator
from Days.Day14.try2.WashingMachine import WashingMachine

washing_machine = WashingMachine(2001)
refrigerator = Refrigerator(2005)

washing_machine.turn_on()
washing_machine.turn_off()

print(refrigerator.get_year())
print(washing_machine.get_year())