from Days.Day13.Vehicle import Vehicle


class Car(Vehicle):
    def __init__(self,make,model,year,number_of_doors):
        super().__init__(make,model,year)
        self.number_of_doors = number_of_doors

    def start_engine(self):
        print("CAR engine started!")

    def test(self):
        print("test")