class Car:
    def __init__(self, make, model, year):
        self.make = make          # Public attribute
        self._model = model       # Protected attribute (convention, not truly private)
        self.__year = year        # Private attribute

    # Public method
    def get_make(self):
        return self.make

    # Protected method (conventionally used within class or subclass)
    def _get_model(self):
        return self._model

    # Private method
    def __get_year(self):
        return self.__year

    # Public method to access the private attribute
    def get_year(self):
        return self.__get_year()