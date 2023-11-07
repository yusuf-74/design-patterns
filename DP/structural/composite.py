"""
Composite Pattern Implementation

Description:
Welcome to the "Composite Pattern Implementation" module. 
This module explores and demonstrates the Composite design pattern, a structural pattern in software design. 
The Composite pattern is used to compose objects into tree structures to represent part-whole hierarchies. 
It allows clients to treat individual objects and compositions of objects uniformly.

Module Overview:
- Problem Description: 
    We will start by presenting a scenario where you have a complex system consisting of various elements, some of which may be composed of other elements. 
    Managing this hierarchy and applying operations to individual elements and compositions can become complex and inconsistent.

- Solving with Composite Pattern: 
    Next, we will implement the Composite pattern to address the issues outlined in the problem description. 
    The pattern introduces a common interface for both individual elements and compositions, 
    making it easier for clients to work with the hierarchy in a consistent manner.

By the end of this module, you will have a clear understanding of how to use the Composite pattern 
to represent part-whole hierarchies and simplify operations on complex systems.
"""

# Composite Pattern Example: Shipping System

# Problem Description:
#   - In a shipping system, we have a complex hierarchy of boxes and products. Each box can contain other boxes or individual products. 
#     Managing this hierarchy and calculating the total weight of a shipment can become complex and inconsistent. 
#     We need a solution that simplifies the handling of this hierarchy and allows clients to work with it uniformly.

# Solving with Composite Pattern:

#   - We will implement the Composite pattern to address the issues outlined in the problem description. 
#     The Composite Pattern introduces a common interface for both individual products and composite boxes, 
#     making it easier for clients to work with the hierarchy in a consistent manner.

from abc import ABC, abstractmethod
from typing import List
# Abstract Component
class Component(ABC):
    @abstractmethod
    def get_weight(self):
        pass

# Leaf: Individual Product
class Product(Component):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def get_weight(self):
        return self.weight

# Composite: Shipping Box
class Box(Component):
    def __init__(self, name):
        self.name = name
        self.contents : List[Component] = []

    def add(self, component):
        self.contents.append(component)

    def remove(self, component):
        self.contents.remove(component)

    def get_weight(self):
        total_weight = 0
        for item in self.contents:
            total_weight += item.get_weight()
        return total_weight

# Client Code
if __name__ == "__main__":
    product1 = Product("Laptop", 5)  # Laptop weighs 5 kg
    product2 = Product("Headphones", 0.5)  # Headphones weigh 0.5 kg

    box1 = Box("Small Box")
    box1.add(product1)
    box1.add(product2)

    product3 = Product("Tablet", 1.5)  # Tablet weighs 1.5 kg

    box2 = Box("Large Box")
    box2.add(product3)
    box2.add(box1)

    total_weight = box2.get_weight()
    print(f"Total Weight of Shipment: {total_weight} kg")
