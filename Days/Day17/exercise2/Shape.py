from abc import abstractmethod,ABC
class Shape(ABC):
    @abstractmethod
    def draw(self):
        print("drawing!")