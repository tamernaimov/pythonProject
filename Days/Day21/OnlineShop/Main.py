from Days.Day21.OnlineShop.CreditCardPayment import CreditCardPayment
from Days.Day21.OnlineShop.Order import Order
from Days.Day21.OnlineShop.Product import Product
from Days.Day21.OnlineShop.ShoppingCart import ShoppingCart

product1 = Product("Laptop",1000,5)
product2 = Product("phone",22222,3)

cart = ShoppingCart()
cart.add(product1)
cart.add(product2)

cart.view()

payment_method = CreditCardPayment()
order = Order()
order.orderStuff(cart,payment_method,30000)

cart.view()