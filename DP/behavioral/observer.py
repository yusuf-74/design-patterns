"""
Observer Pattern Implementation

Description:
Welcome to the "Observer Pattern Implementation" module.
This module explores and demonstrates the Observer design pattern, a behavioral pattern in software design. The Observer pattern defines a one-to-many dependency between objects, 
where one object (the subject) maintains a list of its dependents (observers) that are notified of any state changes, typically by calling one of their methods.

Module Overview:
- Problem Description:
    Consider a scenario where there is a subject (publisher) that produces some data or events, and multiple observers (subscribers) interested in being notified 
    whenever the data or events change. The challenge is to establish a flexible and decoupled mechanism for notifying and updating the observers when the subject's state changes.

- Solving with Observer Pattern:
    The Observer pattern addresses the problem by defining a subject interface with methods for registering, unregistering, and notifying observers. 
    Concrete subjects maintain a list of observers and notify them when a state change occurs. Observers implement an interface with an update method to receive and handle the notifications.

by the end of this module, you will be able to:
- Understand the role of the Observer Pattern in establishing a communication channel between subjects and observers.
- Implement a flexible and decoupled system where observers can dynamically subscribe and unsubscribe from subjects.
- Use the Observer Pattern to design systems where multiple components need to react to changes in another component.
"""

# Observer Pattern Implementation
from abc import ABC, abstractmethod
from typing import List
# Observer Interface: Observer
class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass

# Subject Interface: Subject


class ISubject(ABC):
    @abstractmethod
    def add_observer(self, observer):
        pass
    
    @abstractmethod
    def remove_observer(self, observer):
        pass
    
    @abstractmethod
    def notify_observers(self, message):
        pass


class Subject(ISubject):
    def __init__(self):
        self.observers :List[Observer] = []

    def add_observer(self, observer):
        print(f"Adding observer: {observer}")
        self.observers.append(observer)

    def remove_observer(self, observer):
        print(f"Removing observer: {observer}")
        self.observers.remove(observer)

    def notify_observers(self, message):
        print(f"Notifying observers: {message}")
        for observer in self.observers:
            observer.update(message)

# Concrete Observer: ConcreteObserver
class ConcreteObserver(Observer):
    def __init__(self, name, subject=None):
        self.name = name
        self.subject : ISubject = subject

    def update(self, message):
        print(f"{self.name} received message: {message}")

# Concrete Subject: ConcreteSubject
class ConcreteSubject(Subject):
    def set_state(self, state):
        print(f"Setting state to: {state}")
        self.notify_observers(state)

# Client Code
if __name__ == "__main__":
    observer1 = ConcreteObserver("Observer 1")
    observer2 = ConcreteObserver("Observer 2")

    subject = ConcreteSubject()

    subject.add_observer(observer1)
    subject.add_observer(observer2)

    subject.set_state("State 1")
    subject.set_state("State 2")
