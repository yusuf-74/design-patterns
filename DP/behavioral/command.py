# Command Pattern Implementation

"""
Module: Command Pattern Implementation

Description:
Welcome to the "Command Pattern Implementation" module.
This module explores and demonstrates the Command design pattern, a behavioral pattern in software design. The Command pattern turns a request into a stand-alone object, 
allowing for parameterization of clients with different requests, queuing of requests, and logging of the parameters.

Module Overview:
- Problem Description:
    In many applications, you might encounter scenarios where you need to decouple the sender of a request from the object that processes the request. 
    Additionally, you may want to parameterize objects with operations, queue requests, or support undoable operations. 
    The challenge is to design a flexible and extensible solution for handling such requests.

- Solving with Command Pattern:
    The Command pattern addresses the problem by encapsulating a request as an object, parameterizing clients with different requests, 
    and allowing for the queuing and execution of requests. The pattern involves defining command interfaces, 
    implementing concrete command classes, and providing invoker classes to trigger the commands.

by the end of this module, you will be able to:
- Understand the role of the Command Pattern in decoupling senders and receivers of requests.
- Implement a flexible and extensible system where commands can be parameterized, queued, and executed on demand.
- Use the Command Pattern to design applications that require undoable operations or complex workflows.
"""

# Command Pattern Implementation
from abc import ABC, abstractmethod

# Command Interface: Command
class ICommand(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def unexecute(self):
        pass

# Concrete Commands: TurnOnCommand, TurnOffCommand, BrightenCommand, DimCommand
class TurnOnCommand(ICommand):
    def __init__(self, light):
        self.light : Light = light

    def execute(self):
        self.light.turn_on()

    def unexecute(self):
        self.light.turn_off()

class TurnOffCommand(ICommand):
    def __init__(self, light):
        self.light : Light = light

    def execute(self):
        self.light.turn_off()

    def unexecute(self):
        self.light.turn_on()

class BrightenCommand(ICommand):
    def __init__(self, light):
        self.light : Light = light
        self.previous_state = None

    def execute(self):
        self.previous_state = self.light.get_state()
        self.light.brighten()

    def unexecute(self):
        if self.previous_state == "ON":
            self.light.turn_on()
        elif self.previous_state == "OFF":
            self.light.turn_off()

class DimCommand(ICommand):
    def __init__(self, light):
        self.light :Light = light
        self.previous_state = None

    def execute(self):
        self.previous_state = self.light.get_state()
        self.light.dim()

    def unexecute(self):
        print("undoing")
        if self.previous_state == "ON":
            self.light.turn_on()
        elif self.previous_state == "OFF":
            self.light.turn_off()

# Receiver: Light
class Light:
    def __init__(self):
        self.state = "OFF"

    def turn_on(self):
        print("Light is ON")
        self.state = "ON"

    def turn_off(self):
        print("Light is OFF")
        self.state = "OFF"

    def brighten(self):
        print("Light is Brightened")

    def dim(self):
        print("Light is Dimmed")

    def get_state(self):
        return self.state

class IInvoker(ABC):
    def __init__(self):
        self.command = None
    
    @abstractmethod
    def set_command(self, command):
        pass
    
    @abstractmethod
    def press_button(self):
        pass
    
    @abstractmethod
    def press_undo_button(self):
        pass

# Invoker: RemoteControl
class RemoteControl(IInvoker):
    def __init__(self):
        self.command: ICommand = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        self.command.execute()

    def press_undo_button(self):
        self.command.unexecute()

# Client Code
if __name__ == "__main__":
    smart_light = Light()

    turn_on = TurnOnCommand(smart_light)
    turn_off = TurnOffCommand(smart_light)
    brighten = BrightenCommand(smart_light)
    dim = DimCommand(smart_light)

    remote = RemoteControl()

    remote.set_command(turn_on)
    remote.press_button()

    remote.set_command(brighten)
    remote.press_button()

    remote.set_command(dim)
    remote.press_button()

    remote.press_undo_button()
    remote.press_undo_button()
    remote.press_undo_button()
