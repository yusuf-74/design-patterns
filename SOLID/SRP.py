"""
Single Responsibility Principle (SRP) Implementation

Description:
In this module, we will delve into the Single Responsibility Principle (SRP) and learn how to effectively apply it in software design.
SRP advocates that a class should have only one reason to change, promoting code organization and maintainability.

Module Overview:
-   Problem Introduction: We'll begin by introducing a class that violates the SRP, 
    demonstrating the challenges it poses in terms of code maintenance and scalability.

-   Solving with SRP: Next, we will explore how to refactor the code by separating responsibilities into distinct classes, 
    aligning with the SRP. You'll see how this approach enhances code readability and adaptability.

By the end of this module, you'll have a clear understanding of how to identify and rectify violations of the Single Responsibility Principle, 
contributing to the development of cleaner, more maintainable code.
"""

from typing_extensions import Self

# Problematic Code: Violating SRP

class Order:
    def __init__(self, order_id, customer, items):
        self.order_id = order_id
        self.customer = customer
        self.items = items

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total

    def generate_invoice(self):
        # Logic for generating an invoice
        pass

    def save_to_database(self):
        # Logic for saving the order to the database
        pass

# Refactored Code: Adhering to SRP

class Order:
    def __init__(self: Self, order_id: int, customer, items:list) -> None:
        self.order_id = order_id
        self.customer = customer
        self.items = items

    def calculate_total(self:Self) -> float: 
        total = 0
        for item in self.items:
            total += item.price
        return total

class InvoiceGenerator:
    def generate_invoice(self, order:Order) -> None:
        # Logic for generating an invoice
        pass

class DatabaseSaver:
    def save_to_database(self, order:Order) -> None:
        # Logic for saving the order to the database
        pass

"""
the biggest advantage of adhering to the SRP is that it makes code more maintainable. 
so whenever you need to make a change to the code, you know exactly where to look at. also it makes the code more readable and reusable.
"""