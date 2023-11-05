"""
Flyweight Pattern Implementation

Description:
    Welcome to the "Flyweight Pattern Implementation" module. 
    This module explores and demonstrates the Flyweight design pattern, a structural pattern in software design. 
    The Flyweight pattern is used to minimize memory usage or computational expenses by sharing as much as possible with related objects. 
    It's particularly useful when dealing with a large number of objects with shared characteristics.

Module Overview:
- Problem Description: 
    We will start by presenting a scenario where you have a system that manages a vast number of objects, 
    each of which has some intrinsic (shared) and extrinsic (unique) characteristics. 
    Managing and storing these objects can become memory-intensive and inefficient due to the redundancy of shared data.

- Solving with Flyweight Pattern: 
    Next, we will implement the Flyweight pattern to address the issues outlined in the problem description. 
    The pattern separates the intrinsic and extrinsic state of objects, allowing multiple objects to share common intrinsic data. 
    This significantly reduces memory usage and improves performance.

By the end of this module, you will have a clear understanding of how to use the Flyweight pattern 
to optimize memory usage and enhance the efficiency of managing a large number of similar objects.
"""

from abc import ABC, abstractmethod


class Discount(ABC):
    @abstractmethod
    def apply_discount(self, original_price, item_id=None):
        pass

# Concrete Flyweight: Day Discount


class DayDiscount(Discount):
    def apply_discount(self, original_price):
        discount_percent = 0.1  # fetch from database
        discount_amount = original_price * discount_percent 
        return original_price - discount_amount

# Concrete Flyweight: Specific Discount


class SpecificDiscount(Discount):
    def apply_discount(self, original_price, item_id):
        discount_percent = 0.5  # fetch from database
        discount_amount = original_price * discount_percent 
        return original_price - discount_amount


class DiscountFactory:
    _discounts = {}

    @staticmethod
    def get_discount(discount_type) -> Discount:
        key = f"{discount_type}"  # day or specific
        if key not in DiscountFactory._discounts:
            if discount_type == "day":
                DiscountFactory._discounts[key] = DayDiscount()
            elif discount_type == "specific":
                DiscountFactory._discounts[key] = SpecificDiscount()
        return DiscountFactory._discounts[key]


# Client Code
if __name__ == "__main__":
    items = [
        {
            "id": "1",  
            "name": "Laptop", 
            "price": 1000
        },
        {   
            "id": "2",
            "name": "Headphones", 
            "price": 200
        },
        {
            "id": "3",
            "name": "Tablet", 
            "price": 300
        },
    ]


    for item in items:
        discount = DiscountFactory.get_discount("day")
        discounted_price = discount.apply_discount(item["price"])
        print(f"Day offer: Item: {item['name']}, Discounted Price: ${discounted_price:.2f}")

    for item in items:
        discount = DiscountFactory.get_discount("specific")
        discounted_price = discount.apply_discount(item["price"], item["id"])
        print(f"Specific offer: Item: {item['name']}, Discounted Price: ${discounted_price:.2f}")
