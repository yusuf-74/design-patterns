"""
Strategy Pattern Implementation

Description:
Welcome to the "Strategy Pattern Implementation" module. 
This module explores and demonstrates the Strategy design pattern, a behavioral pattern in software design. 
The Strategy pattern defines a family of algorithms, encapsulates each algorithm, and makes them interchangeable. 
It allows the client to choose an algorithm at runtime.

Module Overview:
- Problem Description: 
    We will start by presenting a scenario where you have a class that performs a specific task, but there are multiple ways (algorithms) to accomplish it. 
    The initial design may involve a fixed algorithm, making it challenging to adapt to changing requirements or incorporate new algorithms without modifying the existing code.
- Solving with Strategy Pattern: 
    Next, we will implement the Strategy pattern to address the limitations of the initial design. The pattern involves defining a family of algorithms, 
    encapsulating each algorithm in a separate class, and allowing the client to choose the appropriate algorithm dynamically.

by the end of this module, you will be able to:
- Understand the benefits of using the Strategy Pattern in designing flexible and adaptable systems.
- Implement interchangeable algorithms to perform specific tasks.
- Dynamically switch between different strategies without modifying client code.
"""


# Strategy Pattern Implementation
from abc import ABC, abstractmethod


class ISortingStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass

class ISortingContext(ABC):
    @abstractmethod
    def set_strategy(self, strategy):
        pass

    @abstractmethod
    def perform_sort(self, data):
        pass

# Context: SortingContext
class SortingContext(ISortingContext):
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def perform_sort(self, data):
        return self.strategy.sort(data)

# Concrete Strategies: BubbleSort, QuickSort
class BubbleSort(ISortingStrategy):
    def sort(self, data):
        print("Sorting using Bubble Sort")
        return sorted(data)

class QuickSort(ISortingStrategy):
    def sort(self, data):
        print("Sorting using Quick Sort")
        return sorted(data, key=lambda x: str(x))

# Client Code
if __name__ == "__main__":
    data = [4, 2, 7, 1, 9, 5]

    bubble_sort = BubbleSort()
    quick_sort = QuickSort()

    sorting_context = SortingContext(bubble_sort)
    sorted_data = sorting_context.perform_sort(data)
    print("Sorted Data:", sorted_data)

    sorting_context.set_strategy(quick_sort)
    sorted_data = sorting_context.perform_sort(data)
    print("Sorted Data:", sorted_data)
