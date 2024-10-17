from Days.Day13.Vehicle import Vehicle


class Motorcycle(Vehicle):
    def __init__(self,make,model,year,has_sidecar):
        super().__init__(make,model,year)
        self.has_sidecar = has_sidecar

    def start_engine(self):
        super().start_engine()
        print("Motorcycle engine Started!")

    def test_method(self):
        print(self.make)