import Car
import Motorcycle
import Vehicle


car = Car.Car("make", "Audi", 2006, 4)
car.start_engine()

motorcycle = Motorcycle.Motorcycle("make", "hunday", 2010, True)
motorcycle.start_engine()

def vehicle_sound(vehicle):
    vehicle.start_engine()

vehicle_sound(motorcycle)
motorcycle.parent_method()
motorcycle.test_method()
motorcycle.parent_method_with_vars()

