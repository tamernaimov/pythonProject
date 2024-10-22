from abc import ABC,abstractmethod
class Worker:
    def eat(self):
        print("EATING!")
    @abstractmethod
    def work(self):
        print("WORK!")
