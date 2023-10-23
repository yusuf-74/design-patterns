"""
Singleton Pattern Implementation

Description:
Welcome to the "Singleton Pattern Implementation" module. 
This module is dedicated to exploring and implementing the Singleton design pattern, a widely used creational pattern in software development. 
The Singleton pattern ensures that a class has only one instance and provides a global point of access to that instance. 
It's commonly used for situations where you want to limit the number of instances of a class to just one, 
such as managing a single point of control for resources, configurations, or connections.

Module Overview:
    - Problem Introduction: 
        We'll start by presenting a scenario where multiple instances of a class can cause problems or inefficiencies. 
        This scenario will highlight the need for a Singleton pattern to ensure a single, globally accessible instance of the class.

    - Solving with Singleton Pattern: 
        Next, we will implement the Singleton pattern, demonstrating how to design a class that enforces a single instance and provides 
        access to that instance throughout the application.

By the end of this module, you'll have a practical understanding of how to apply the Singleton pattern in your code, 
ensuring that there's only one instance of a class when it's needed.

"""

# Problematic Code

class Logger:
    def __init__(self, name):
        self.name = name

    def log(self, message):
        print(f"[{self.name}] {message}")

# Usage
logger_1 = Logger("Logger 1")
logger_1.log("This is a log message from Logger 1")

logger_2 = Logger("Logger 2")
logger_2.log("This is a log message from Logger 2")
print("====================== END OF PROBLEMATIC CODE =====================")
print("======================         Singleton       =====================")
# Singleton Pattern Implementation
class SingletonLogger:
    _instance = None

    def __new__(cls, name):
        if cls._instance is None:
            cls._instance = super(SingletonLogger, cls).__new__(cls)
            cls._instance.__init_data(name)
        return cls._instance

    def __init_data(self, name):
        self.name = name

    def log(self, message):
        print(f"[{self.name}] {message}")

# Usage
logger_1 = SingletonLogger("Logger 1")
logger_1.log("This is a log message from Logger 1")

logger_2 = SingletonLogger("Logger 2")
logger_2.log("This is a log message from Logger 2")
logger_1.log("This is a log message from Logger 3")

# Both instances refer to the same SingletonLogger instance
print(logger_1 is logger_2)  # Output: True