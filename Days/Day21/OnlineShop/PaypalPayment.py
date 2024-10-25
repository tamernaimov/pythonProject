from Days.Day21.OnlineShop.Payment import Payment
from Days.Day21.OnlineShop.ShoppingCart import ShoppingCart


class PaypalPayment(Payment):
    def process_payment(self,amount,shoppingCart: ShoppingCart):
        if amount >= shoppingCart.cost:
            print("You've paid with Paypal!")
        else:
            print("you cant pay that you dumb")

