class Car:

   def __init__(self,make,model,year):
       self.make = make
       self.model = model
       self.year = year



   def printStats(self):
       print(self.make,self.model,self.year)

   def update_year(self, newYear):
       self.year = newYear