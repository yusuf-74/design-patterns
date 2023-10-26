"""
Factory Method Pattern Implementation

Description:
Welcome to the "Factory Method Pattern Implementation" module. 
This module is dedicated to exploring and implementing the Factory Method design pattern, a creational pattern in software development. 
The Factory Method pattern provides an interface for creating objects, allowing subclasses to alter the type of objects that will be created. 
It promotes loose coupling between the creator and the product, making it easier to extend and maintain the code.

Module Overview:

Problem Introduction:  
    We'll start by presenting a scenario where creating objects of different types is hard-coded and inflexible. 
    This scenario will highlight the need for the Factory Method pattern.

Solving with Factory Method Pattern: 
    Next, we will implement the Factory Method pattern, demonstrating how to define a creator class with a factory method. 
    Subclasses can then override this method to create objects of specific types, allowing for more flexible and extensible object creation.

By the end of this module, you'll have a practical understanding of how to apply the Factory Method pattern in your code, 
promoting flexibility and maintainability when creating objects of various types.
"""

# Problematic Code

class Visa:
    def withdraw(self):
        print("Withdraw money from an ATM using Visa Card")

class MasterCard:
    def withdraw(self):
        print("Withdraw money from an ATM using MasterCard")

class UnionPay:
    def withdraw(self):
        print("Withdraw money from an ATM using UnionPay Card")

# Usage

card_number = "123456"

if card_number.startswith("4"):
    card = Visa()
elif card_number.startswith("5"):
    card = MasterCard()
elif card_number.startswith("6"):
    card = UnionPay()

card.withdraw()

# the code above is hard-coded and inflexible.
# we also force the client to know the exact type of object they want to create, which is not ideal.

# apply the Factory Method pattern to solve this problem.

from abc import ABC, abstractmethod

class Card(ABC):
    @abstractmethod
    def withdraw(self):
        pass

class Visa(Card):
    def withdraw(self):
        print("Withdraw money from an ATM using Visa Card")

class MasterCard(Card):
    def withdraw(self):
        print("Withdraw money from an ATM using MasterCard")

class UnionPay(Card):
    def withdraw(self):
        print("Withdraw money from an ATM using UnionPay Card")

class ICardFactory(ABC):
    @abstractmethod
    def create_card(self, card_number):
        pass

class CardFactory(ICardFactory):
    def create_card(self, card_number):
        if card_number.startswith("4"):
            return Visa()
        elif card_number.startswith("5"):
            return MasterCard()
        elif card_number.startswith("6"):
            return UnionPay()

# Usage
card_number = "123456"
card_factory = CardFactory()
card = card_factory.create_card(card_number)
card.withdraw()

# in this code, we've defined a creator class with a factory method that returns a Card object.
# we removed the hard-coded logic from the client code, allowing the client to create objects of various types without knowing the exact type of object they want to create.