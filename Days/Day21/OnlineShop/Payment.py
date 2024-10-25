from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self,amount: int, shoppingCart):
        pass