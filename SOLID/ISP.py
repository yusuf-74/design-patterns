"""
Interface Segregation Principle (ISP) Implementation

Description:
Welcome to the "Interface Segregation Principle (ISP) Implementation" module. 
This module focuses on understanding and applying the ISP, one of the SOLID principles of object-oriented design. 
The ISP emphasizes that clients should not be forced to depend on interfaces they do not use. 
In simpler terms, it promotes the idea that classes should have specific, focused interfaces rather than large, monolithic ones.

Module Overview:

Problem Introduction:
    We'll begin by presenting a scenario involving an interface and a class that initially violate the ISP.
    This scenario will illustrate the challenges associated with interfaces that contain more methods than necessary.

Solving with ISP: 
    Next, we will refactor the code to adhere to the Interface Segregation Principle. 
    You'll see how to design smaller, more focused interfaces that cater to the specific needs of clients.

By the end of this module, you'll have a practical understanding of how to apply the Interface Segregation Principle to create 
more maintainable and flexible software systems, ensuring that interfaces are tailored to the requirements of clients.
"""

# Problematic Code

# Interface: Worker
class Worker:
    def work(self):
        pass

    def eat(self):
        pass

# Class: Robot
class Robot(Worker):
    def work(self):
        print("Robot is working")

    def eat(self):
        pass

# Class: Human
class Human(Worker):
    def work(self):
        print("Human is working")

    def eat(self):
        print("Human is eating")

# Function to make a worker work
def make_worker_work(worker):
    worker.work()

# Usage
robot = Robot()
human = Human()

make_worker_work(robot)
make_worker_work(human)

"""
Issues with the Problematic Code:

The Worker interface contains methods work and eat. While this is fine for humans, it doesn't make sense for robots. 
The Robot class is forced to provide an implementation for the eat method even though it's not relevant to robots. 
This violates the ISP because the interface contains methods that clients (in this case, the Robot class) don't need.

"""

# Refactored Code - Adhering to ISP

from abc import ABC, abstractmethod

# Interface: Workable
class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

# Interface: Eatable
class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

# Class: Robot
class Robot(Workable):
    def work(self):
        print("Robot is working")

# Class: Human
class Human(Workable, Eatable):
    def work(self):
        print("Human is working")

    def eat(self):
        print("Human is eating")

# Function to make a worker work
def make_worker_work(worker):
    worker.work()

# Usage
robot = Robot()
human = Human()

make_worker_work(robot)
make_worker_work(human)
