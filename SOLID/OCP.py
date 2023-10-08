"""
Open/Closed Principle (OCP) Implementation

Description:
This module is dedicated to the Open/Closed Principle (OCP)  one of the five SOLID principles of object-oriented design.
The OCP emphasizes that software entities (e.g., classes, modules, functions) should be open for extension but closed for modification.
In simpler terms, it promotes the idea that you should be able to extend the behavior of a module without altering its source code.

Module Overview:

Problem Introduction: We'll start by presenting a class that violates the OCP, 
showcasing the challenges associated with modifying existing code to accommodate new functionality.

Solving with OCP: Next, we'll explore how to refactor the code by introducing new classes or modules to extend functionality 
without changing the existing codebase.
This approach aligns with the OCP's principle of open for extension and closed for modification.

By the end of this module, you'll grasp the significance of the Open/Closed Principle and have a practical understanding 
of how to design software systems that are resilient to change and easy to extend, a crucial skill in software development.
"""

# Problematic Code: Violating OCP

class Shape:
    def __init__(self, type):
        self.type = type

class Circle(Shape):
    def __init__(self, radius):
        super().__init__('Circle')
        self.radius = radius

class Square(Shape):
    def __init__(self, side_length):
        super().__init__('Square')
        self.side_length = side_length

# each time we add a new shape, we need to modify the calculate_area function

def calculate_area(shape):
    if shape.type == 'Circle':
        return 3.14 * shape.radius ** 2
    elif shape.type == 'Square':
        return shape.side_length ** 2

# Refactored Code: Adhering to OCP

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

def calculate_area(shape):
    return shape.area()

# Usage
circle = Circle(5)
square = Square(4)

print(calculate_area(circle))  # Output: 78.5
print(calculate_area(square))  # Output: 16

# ANOTHER EXAMPLE

# Problematic Code

# Credit Card payment method
class CreditCardPayment:
    def process_credit_card_payment(self, amount):
        # Logic for processing credit card payment
        print(f"Processed credit card payment of ${amount}")

# PayPal payment method
class PayPalPayment:
    def process_paypal_payment(self, amount):
        # Logic for processing PayPal payment
        print(f"Processed PayPal payment of ${amount}")

# Payment processing system
class PaymentProcessor:
    def process_payment(self, method, amount):
        if method == "credit_card":
            credit_card_payment = CreditCardPayment()
            credit_card_payment.process_credit_card_payment(amount)
        elif method == "paypal":
            paypal_payment = PayPalPayment()
            paypal_payment.process_paypal_payment(amount)
        else:
            print(f"Unsupported payment method: {method}")

# Usage
payment_processor = PaymentProcessor()
payment_processor.process_payment("credit_card", 100)
payment_processor.process_payment("paypal", 50)

# NOTE that if we want to add a new payment method, we need to modify the process_payment method in the PaymentProcessor class

# Refactored Code - Adhering to OCP

from abc import ABC, abstractmethod

# Abstract class representing a payment method
class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

# Credit Card payment method
class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount):
        # Logic for processing credit card payment
        print(f"Processed credit card payment of ${amount}")

# PayPal payment method
class PayPalPayment(PaymentMethod):
    def process_payment(self, amount):
        # Logic for processing PayPal payment
        print(f"Processed PayPal payment of ${amount}")

# New payment method: Cryptocurrency
class CryptoPayment(PaymentMethod):
    def process_payment(self, amount):
        # Logic for processing cryptocurrency payment
        print(f"Processed cryptocurrency payment of ${amount}")

# Payment processing system
class PaymentProcessor:
    def __init__(self):
        self.payment_methods = {}

    def register_payment_method(self, method_name, payment_method):
        self.payment_methods[method_name] = payment_method

    def process_payment(self, method_name, amount):
        if method_name in self.payment_methods:
            payment_method = self.payment_methods[method_name]
            payment_method.process_payment(amount)
        else:
            print(f"Unsupported payment method: {method_name}")

# Usage
payment_processor = PaymentProcessor()
payment_processor.register_payment_method("credit_card", CreditCardPayment())
payment_processor.register_payment_method("paypal", PayPalPayment())
payment_processor.register_payment_method("crypto", CryptoPayment())  # Adding a new payment method

payment_processor.process_payment("credit_card", 100)
payment_processor.process_payment("paypal", 50)
payment_processor.process_payment("crypto", 200)

