"""
Decorator Pattern Implementation

Description:
Welcome to the "Decorator Pattern Implementation" module. 
This module explores and demonstrates the Decorator design pattern, a structural pattern in software design. 
The Decorator pattern allows you to add new behaviors or responsibilities to objects dynamically, without altering their code.

Module Overview:
- Problem Description: 
    We will start by presenting a scenario where you need to add functionality to an object, 
    but you want to keep the object's class open for extension and closed for modification. 
    We need a way to achieve this without altering the existing code.

- Solving with Decorator Pattern: 
    Next, we will implement the Decorator pattern to address the issues outlined in the problem description. 
    The Decorator pattern allows us to attach additional responsibilities to objects through a chain of decorator objects. 
    These decorators add functionality in a flexible and reusable way.

By the end of this module, you will have a clear understanding of how to use the Decorator pattern to extend the behavior of objects 
in your software systems without modifying their code, making your code more maintainable and flexible.
"""

from abc import ABC, abstractmethod
# Example 1: Coffee Shop

class ICoffee(ABC):
    @abstractmethod
    def cost(self):
        pass

# Component: Coffee
class Coffee(ICoffee):
    def cost(self):
        return 5

# Decorator: CoffeeDecorator
class CoffeeDecorator(ICoffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

# Concrete Decorators: Milk, Sugar
class Milk(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)
        
    def cost(self):
        return self._coffee.cost() + 2

class Sugar(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)
        
    def cost(self):
        return self._coffee.cost() + 1


# Example 2: Text Editor

class IText(ABC):
    @abstractmethod
    def content(self):
        pass

# Component: Text
class Text(IText):
    def content(self):
        return "This is some text."

# Decorator: TextDecorator
class TextDecorator(IText):
    def __init__(self, text):
        self._text = text

    def content(self):
        return self._text.content()

# Concrete Decorators: SpellCheck
class SpellCheck(TextDecorator):
    def content(self):
        text = self._text.content()
        return text + " (Spell-checked)"



# Client
if __name__ == "__main__":
    
    print("Example 1: Coffee Shop")
    
    simple_coffee = Coffee()
    print(f"Cost of Simple Coffee: ${simple_coffee.cost()}")

    coffee_with_milk = Milk(simple_coffee)
    print(f"Cost of Coffee with Milk: ${coffee_with_milk.cost()}")

    coffee_with_milk_and_sugar = Sugar(coffee_with_milk)
    print(f"Cost of Coffee with Milk and Sugar: ${coffee_with_milk_and_sugar.cost()}")
    
    print("========================================")
    print("Example 2: Text Editor")
    
    simple_text = Text()
    print("Simple Text:")
    print(simple_text.content())

    text_with_spell_check = SpellCheck(simple_text)
    print("\nText with Spell Check:")
    print(text_with_spell_check.content())
