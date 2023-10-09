"""
Dependency Inversion Principle (DIP) Implementation

Description:
Welcome to the "Dependency Inversion Principle (DIP) Implementation" module. 
This module is dedicated to exploring and applying the Dependency Inversion Principle, 
one of the SOLID principles of object-oriented design. The DIP emphasizes that high-level modules 
should not depend on low-level modules; both should depend on abstractions. This principle promotes 
decoupling, flexibility, and maintainability in your codebase.

Module Overview:

Problem Introduction: 
    We'll begin by presenting a scenario where high-level modules directly depend on low-level modules, 
    resulting in tight coupling. This scenario will highlight the challenges associated with a lack of adherence to the DIP.

Solving with DIP: 
    Next, we will refactor the code to adhere to the Dependency Inversion Principle. 
    You'll see how to introduce abstractions (such as interfaces) that allow both high-level and low-level modules 
    to depend on them, reducing coupling and enhancing flexibility.

By the end of this module, you'll have a practical understanding of how to apply the Dependency Inversion Principle 
to create more modular, maintainable, and testable software systems.
"""

# Problematic Code

# Low-level module: DataAccess
class DataAccess:
    def get_data(self):
        # Simulate fetching data from a database
        return "Data from the database"
    
# High-level module: BusinessLogic
class BusinessLogic:
    def __init__(self):
        self.data_access = DataAccess()

    def do_business_logic(self):
        data = self.data_access.get_data()
        # Perform business logic using data
        print("Business logic executed with data:", data)

# Usage
data_access = DataAccess()
business_logic = BusinessLogic(data_access)
business_logic.do_business_logic()


"""
Issues with the Problematic Code:

The high-level module BusinessLogic directly depends on the low-level module DataAccess, resulting in tight coupling. 
Changes in the DataAccess module can directly impact the BusinessLogic module.
"""

# Refactored Code - Adhering to DIP

from abc import ABC, abstractmethod

# Abstraction: IDataAccess
class IDataAccess(ABC):
    @abstractmethod
    def get_data(self):
        pass

# High-level module: BusinessLogic
class BusinessLogic:
    def __init__(self, data_access: IDataAccess):
        self.data_access = data_access

    def do_business_logic(self):
        data = self.data_access.get_data()
        # Perform business logic using data
        print("Business logic executed with data:", data)

# Low-level module: DataAccess
class DataAccess(IDataAccess):
    def get_data(self):
        # Simulate fetching data from a database
        return "Data from the database"

# Usage
data_access = DataAccess()
business_logic = BusinessLogic(data_access)
business_logic.do_business_logic()

"""
so whenever we want to add new data source we just need to create a new class that implements IDataAccess interface
"""