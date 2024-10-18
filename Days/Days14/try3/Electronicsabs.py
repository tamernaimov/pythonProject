from abc import ABC, abstractmethod

class Electronicstab(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    def turn_off(self):
        pass