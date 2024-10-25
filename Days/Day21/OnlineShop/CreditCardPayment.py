from Days.Day21.OnlineShop.Payment import Payment
from Days.Day21.OnlineShop.ShoppingCart import ShoppingCart


class CreditCardPayment(Payment):
    def process_payment(self,amount,shoppingCart: ShoppingCart):
         if amount >= shoppingCart.cost:
            print("You've paid with Credit Card!")
         else:
            print("you cant pay that you dumb")