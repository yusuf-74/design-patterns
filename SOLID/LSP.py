"""
Liskov Substitution Principle (LSP) Implementation

Description:
Welcome to the "Liskov Substitution Principle (LSP) Implementation" module.
This module is dedicated to exploring the LSP, one of the SOLID principles of object-oriented design. 
The LSP emphasizes that derived classes should be substitutable for their base classes without altering the correctness of the program.
In simpler terms, it promotes a strong relationship between base and derived classes, ensuring consistent behavior and maintainability.

Module Overview:

Problem Introduction:   We'll start by presenting a scenario involving a base class and derived classes.
                        This scenario will initially violate the LSP, illustrating the challenges associated with 
                        a lack of adherence to the principle.

Solving with LSP:   Next, we will refactor the code by adhering to the Liskov Substitution Principle. 
                    You'll see how to design base and derived classes to ensure that derived classes can seamlessly 
                    replace base class instances without introducing unexpected behavior.
"""

# Problematic Code

# Base class: Account
class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

# Derived class: SavingsAccount
class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance += self.balance * (self.interest_rate / 100)

# Derived class: CheckingAccount
class CheckingAccount(Account):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
        else:
            print("Insufficient funds")

# Usage
savings_account = SavingsAccount("S1001", 1000, 3.0)
checking_account = CheckingAccount("C2001", 2000, 500)

# Process account operations
savings_account.deposit(1000)
savings_account.add_interest()
savings_account.withdraw(500)

checking_account.deposit(1500)
checking_account.withdraw(2200)


# Issues with the Problematic Code:

# The CheckingAccount class overrides the withdraw method to handle overdrafts, which is a valid behavior. 
# However, this behavior is not consistent with the base class Account, which doesn't consider overdraft limits. 
# This violates the Liskov Substitution Principle (LSP).


# Refactored Code - Adhering to LSP
from abc import ABC, abstractmethod

# Base class: Account
class Account(ABC):
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    @abstractmethod
    def withdraw(self, amount):
        pass

# Derived class: SavingsAccount
class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def add_interest(self):
        self.balance += self.balance * (self.interest_rate / 100)

# Derived class: CheckingAccount
class CheckingAccount(Account):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
        else:
            print("Insufficient funds")

# Usage
savings_account = SavingsAccount("S1001", 1000, 3.0)
checking_account = CheckingAccount("C2001", 2000, 500)

# Process account operations
savings_account.deposit(1000)
savings_account.add_interest()
savings_account.withdraw(500)

checking_account.deposit(1500)
checking_account.withdraw(2200)
