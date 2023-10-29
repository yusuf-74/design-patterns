"""
Abstract Factory Method Pattern Implementation

Description:
Welcome to the "Abstract Factory Method Pattern Implementation" module. 
This module is dedicated to exploring and implementing the Abstract Factory design pattern, a creational pattern in software development. 
The Abstract Factory pattern provides an interface for creating families of related or dependent objects 
without specifying their concrete classes. It promotes the creation of objects with a consistent, compatible set of products.

Module Overview:
- Problem Introduction: 
    We'll start by presenting a scenario where creating objects that belong to a specific family is challenging, 
    especially when those objects need to be consistent and compatible. This scenario will highlight the need for the Abstract Factory pattern.

- Solving with Abstract Factory Method Pattern: 
    Next, we will implement the Abstract Factory pattern, demonstrating how to define abstract factories for creating families of related objects. 
    Concrete factories will provide specific implementations for these families, ensuring consistent and compatible object creation.

By the end of this module, you'll have a practical understanding of how to apply the Abstract Factory pattern in your code, 
allowing you to create families of objects with a cohesive and unified set of products.
"""

from abc import ABC, abstractmethod

# Abstract Product: Chair
class Chair(ABC):
    @abstractmethod
    def sit_on(self):
        pass

# Concrete Products: ModernChair and VictorianChair
class ModernChair(Chair):
    def sit_on(self):
        return "Sitting on a modern chair."

class VictorianChair(Chair):
    def sit_on(self):
        return "Sitting on a Victorian chair."

# Abstract Product: Table
class Table(ABC):
    @abstractmethod
    def put_item(self):
        pass

# Concrete Products: ModernTable and VictorianTable
class ModernTable(Table):
    def put_item(self):
        return "Putting an item on a modern table."

class VictorianTable(Table):
    def put_item(self):
        return "Putting an item on a Victorian table."

# Abstract Factory: FurnitureFactory
class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_table(self) -> Table:
        pass

# Concrete Factories: ModernFurnitureFactory and VictorianFurnitureFactory
class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ModernChair()

    def create_table(self) -> Table:
        return ModernTable()

class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return VictorianChair()

    def create_table(self) -> Table:
        return VictorianTable()

# Client
def build_furniture(factory: FurnitureFactory):
    chair = factory.create_chair()
    table = factory.create_table()
    return chair, table

# Usage
modern_factory = ModernFurnitureFactory()
victorian_factory = VictorianFurnitureFactory()

modern_chair, modern_table = build_furniture(modern_factory)
victorian_chair, victorian_table = build_furniture(victorian_factory)

print(modern_chair.sit_on())
print(modern_table.put_item())

print(victorian_chair.sit_on())
print(victorian_table.put_item())

# In this code, the creation of chairs and tables is done by separate factories, 
# leading to inconsistencies and lack of cohesion in the product families.

from abc import ABC, abstractmethod

# Abstract Product: Chair
class Chair(ABC):
    @abstractmethod
    def sit_on(self):
        pass

# Concrete Products: ModernChair and VictorianChair
class ModernChair(Chair):
    def sit_on(self):
        return "Sitting on a modern chair."

class VictorianChair(Chair):
    def sit_on(self):
        return "Sitting on a Victorian chair."

# Abstract Product: Table
class Table(ABC):
    @abstractmethod
    def put_item(self):
        pass

# Concrete Products: ModernTable and VictorianTable
class ModernTable(Table):
    def put_item(self):
        return "Putting an item on a modern table."

class VictorianTable(Table):
    def put_item(self):
        return "Putting an item on a Victorian table."

# Abstract Factory: FurnitureFactory
class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_table(self) -> Table:
        pass

# Concrete Factories: ModernFurnitureFactory and VictorianFurnitureFactory
class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ModernChair()

    def create_table(self) -> Table:
        return ModernTable()

class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return VictorianChair()

    def create_table(self) -> Table:
        return VictorianTable()

# Client
def build_furniture(factory: FurnitureFactory):
    chair = factory.create_chair()
    table = factory.create_table()
    return chair, table

# Usage
modern_factory = ModernFurnitureFactory()
victorian_factory = VictorianFurnitureFactory()

modern_chair, modern_table = build_furniture(modern_factory)
victorian_chair, victorian_table = build_furniture(victorian_factory)

print(modern_chair.sit_on())
print(modern_table.put_item())

print(victorian_chair.sit_on())
print(victorian_table.put_item())