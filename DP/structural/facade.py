"""
Facade Pattern Implementation

Description:
Welcome to the "Facade Pattern Implementation" module. 
This module explores and demonstrates the Facade design pattern, a structural pattern in software design. 
The Facade pattern provides a unified interface to a set of interfaces in a subsystem. 
It simplifies a complex system by providing a higher-level interface that makes it easier to use.

Module Overview:
- Problem Description: 
    We will start by presenting a scenario where you have a complex system with numerous components and interfaces. 
    Interacting with the system can be cumbersome due to its complexity. You need a way to simplify the interactions and provide a single, 
    user-friendly interface to the system.

- Solving with Facade Pattern: 
    Next, we will implement the Facade pattern to address the issues outlined in the problem description. 
    The Facade acts as a simplified interface that abstracts and encapsulates the complex system, making it easier for clients to use.

By the end of this module, you will have a clear understanding of how to use the Facade pattern to provide 
a simplified and user-friendly interface to a complex system, reducing its complexity and making it more accessible to clients.
"""

# Problemtic Scenario:
# when you have a complex system with numerous components and interfaces.
# like a online shopping system, which has a lot of components and interfaces.
# Interacting with the system can be cumbersome due to its complexity.

class Item:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item: Item):
        self.items.append(item)

    def remove_item(self, item: Item):
        self.items.remove(item)

    def calculate_total(self):
        return sum([item.price for item in self.items])

class PaymentGateway:
    def charge(self, amount):
        print(f"Charging {amount} using Payment Gateway")

class Order:
    def __init__(self, cart: Cart, payment_gateway: PaymentGateway):
        self.cart = cart
        self.payment_gateway = payment_gateway

    def checkout(self):
        total = self.cart.calculate_total()
        self.payment_gateway.charge(total)

class Invoice:
    def __init__(self, order: Order):
        self.order = order

    def print(self):
        total = self.order.cart.calculate_total()
        print(f"Receipt: {total}")

# Solution with Facade Pattern:


class PaymentProcessor:
    def process_payment(self, amount):
        print(f"Processing payment of ${amount:.2f}")
        print("Payment processed successfully!")

class ShippingService:
    def ship_items(self):
        print("Shipping items to your address...")
        print("Items shipped successfully!")




class ShoppingCartFacade:
    def __init__(self):
        self.cart = Cart()
        self.payment_processor = PaymentProcessor()
        self.shipping_service = ShippingService()

    def add_item_to_cart(self, item, quantity):
        self.cart.add_item(item, quantity)

    def remove_item_from_cart(self, item, quantity):
        self.cart.remove_item(item, quantity)

    def checkout(self):
        total = self.cart.calculate_total()
        self.payment_processor.process_payment(total)
        self.shipping_service.ship_items()

#Client Code
if __name__ == "__main__":
    # without facade pattern
    cart = Cart()
    cart.add_item(Item("Guitar", 1000))
    cart.add_item(Item("Pick box", 5))

    payment_gateway = PaymentGateway()
    order = Order(cart, payment_gateway)
    order.checkout()

    invoice = Invoice(order)
    invoice.print()
    
    # with Facade pattern
    facade = ShoppingCartFacade()
    facade.add_item_to_cart(Item("Guitar", 1000), 1)
    facade.add_item_to_cart(Item("Pick box", 5), 1)
    facade.checkout()

