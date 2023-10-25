"""
Builder Pattern Implementation

Description:
Welcome to the "Builder Pattern Implementation" module. 
This module is dedicated to exploring and implementing the Builder design pattern, a creational pattern in software development. 
The Builder pattern separates the construction of a complex object from its representation, allowing you to create objects 
with various configurations while maintaining a clear and readable code structure.

Module Overview:
- Problem Introduction: 
    We'll start by presenting a scenario where creating a complex object with numerous configuration options becomes unwieldy, 
    especially when those options are optional. This scenario will highlight the need for the Builder pattern.

- Solving with Builder Pattern: 
    Next, we will implement the Builder pattern, demonstrating how to design a builder class that constructs complex objects step by step. 
    This approach provides a more intuitive and flexible way to create objects with various configurations.

By the end of this module, you'll have a practical understanding of how to apply the Builder pattern in your code, 
improving the readability and maintainability of complex object creation.

"""

# Problematic Code

class Computer:
    def __init__(self, cpu, memory, storage, gpu=None, sound=None, wifi=None):
        self.cpu = cpu
        self.memory = memory
        self.storage = storage
        self.gpu = gpu
        self.sound = sound
        self.wifi = wifi

    def display_specs(self):
        print(f"CPU: {self.cpu}, Memory: {self.memory}, Storage: {self.storage}, GPU: {self.gpu}, Sound: {self.sound}, WiFi: {self.wifi}")

# Usage
computer_1 = Computer("Intel i7", "16GB", "512GB SSD")
computer_1.display_specs()

computer_2 = Computer("AMD Ryzen", "32GB", "1TB HDD", "NVIDIA RTX 3080")
computer_2.display_specs()

# In this code, creating a Computer instance with various optional configurations leads to long and complex constructor calls. 
# It's challenging to keep track of which parameter corresponds to each configuration option.

class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def set_memory(self, memory):
        self.computer.memory = memory
        return self

    def set_storage(self, storage):
        self.computer.storage = storage
        return self

    def set_gpu(self, gpu):
        self.computer.gpu = gpu
        return self

    def set_sound(self, sound):
        self.computer.sound = sound
        return self

    def set_wifi(self, wifi):
        self.computer.wifi = wifi
        return self

    def build(self):
        return self.computer

# Usage
builder = ComputerBuilder()
computer_1 = builder.set_cpu("Intel i7")\
                    .set_memory("16GB")\
                    .set_storage("512GB SSD")\
                    .build()
computer_1.display_specs()

builder = ComputerBuilder()
computer_2 = builder.set_cpu("AMD Ryzen")\
                    .set_memory("32GB")\
                    .set_storage("1TB HDD")\
                    .set_gpu("NVIDIA RTX 3080")\
                    .build()
computer_2.display_specs()
