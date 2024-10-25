class Product():
    def __init__(self,name,price,stock):
        self.name = name
        self.price = price
        self.stock = stock

    def printDetails(self):
        print(f"name is {self.name} and price is {self.price} also the stock is {self.stock}")
