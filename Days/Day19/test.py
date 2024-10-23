from abc import ABC, abstractmethod

class Vehicle(ABC):

    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def stop(self):
        print("dk!")



vehicle1 = Car()
vehicle1.go()