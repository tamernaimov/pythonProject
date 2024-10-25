from Days.Day21.OnlineShop.Payment import Payment
from Days.Day21.OnlineShop.ShoppingCart import ShoppingCart


class Order():
    def orderStuff(self, shoppingCart, payment,amount):
         for i in range(len(shoppingCart.products)):
            shoppingCart.products.clear()

         payment.process_payment(amount,shoppingCart)


