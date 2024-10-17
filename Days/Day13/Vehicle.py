class Vehicle():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print("Engine Started!")

    def parent_method(self):
        print("This was called from Vehicle")

    def parent_method_with_vars(self):
        print("make: " + self.make)