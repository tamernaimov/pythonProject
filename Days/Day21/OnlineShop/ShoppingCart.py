

class ShoppingCart():
    def __init__(self):
        self.products = []
        self.cost = 0
        self.quantity = 0

    def add(self,product):
        self.products.append(product)
        self.cost += product.price
        self.quantity += product.stock

    def remove(self,product):
        self.products.remove(product)
        self.cost -= product.price
        self.quantity -= product.stock

    def view(self):
        if not len(self.products):
            print("there are no products!")
            return

        for product in self.products:
            product.printDetails()

        print(f"COST: {self.cost}")


