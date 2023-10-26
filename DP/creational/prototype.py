"""
Prototype Pattern Implementation

Description:
Welcome to the "Prototype Pattern Implementation" module. 
This module is dedicated to exploring and implementing the Prototype design pattern, a creational pattern in software development.
The Prototype pattern allows you to create new objects by copying an existing object, known as a prototype. 
It's particularly useful when you need to create complex objects with similar structures but different data.

Module Overview:
- Problem Introduction: 
    We'll start by presenting a scenario where creating new objects with the same structure is challenging and may lead to code duplication. 
    This scenario will highlight the need for the Prototype pattern.

- Solving with Prototype Pattern: 
    Next, we will implement the Prototype pattern, demonstrating how to design a class that serves as a prototype for creating new instances with similar structures.

By the end of this module, you'll have a practical understanding of how to apply the Prototype pattern in your code, 
allowing you to efficiently create new objects by cloning existing ones.
"""

# Problematic Code

class Report:
    def __init__(self, filename):
        # heavy I/O call during initialization
        self.data = self.read_data_from_file(filename)

    def read_data_from_file(self, filename):
        # Simulate reading data from a file
        # Inefficient and slow operation
        data = f"Data from {filename}"
        return data

    def display_report(self):
        print(self.data)

# Usage
report_1 = Report("report1.txt")
report_1.display_report()

report_2 = Report("report2.txt")
report_2.display_report()


import copy
from abc import ABC, abstractmethod

class ReportPrototype(ABC):
    @abstractmethod
    def __copy__(self):
        pass

    @abstractmethod
    def __deepcopy__(self, memo):
        pass
    
    def read_data_from_file(self, filename):
        # Simulate reading data from a file
        # Inefficient and slow operation
        data = f"Data from {filename}"
        return data

class Report(ReportPrototype):
    def __init__(self, filename):
        # heavy I/O call during initialization
        self.data = self.read_data_from_file(filename)

    def __copy__(self):
        # Shallow copy implementation
        new_report = self.__class__(self.data)
        return new_report

    def __deepcopy__(self):
        # Deep copy implementation
        new_report = copy.copy(self)
        new_report.data = copy.deepcopy(self.data)
        return new_report

    def display_report(self):
        print(self.data)

# Create a prototype instance with data
prototype_report = Report("Data from report1.txt")

# Clone the prototype using custom copy and deep copy methods
report_1 = copy.copy(prototype_report)
report_1.data = "Data from report1.txt"
report_1.display_report()

report_2 = copy.deepcopy(prototype_report)
report_2.data = "Data from report2.txt"
report_2.display_report()

