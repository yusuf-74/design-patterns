# SOLID Principles & Design Patterns Explained!

Welcome to the "SOLID Principles and Design Patterns Explained" repository! Dive into the world of software engineering excellence with comprehensive explanations and practical code examples that demystify the SOLID principles and illuminate the power of design patterns.

## Table of Contents
1. [SOLID Principles](#solid-principles)
    1. [Single Responsibility Principle](#single-responsibility-principle)
    2. [Open-Closed Principle](#openclosed-principle)
    3. [Liskov Substitution Principle](#liskov-substitution-principle)
    4. [Interface Segregation Principle](#interface-segregation-principle)
2. [Design Patterns](#design-patterns)
    1. [Creational Patterns](#creational-patterns)
       1. [Singleton](#singleton)

## SOLID Principles

  - ### Single Responsibility Principle
    
    A class should have one and only one reason to change, meaning that a class should have only one job.
    
    - Why S.R.P.?
        - It makes the code easier to understand and maintain.
        - It makes the code easier to test.
        - It reduces the coupling between classes.
        - It increases the cohesion between classes.
    - Real-World Example
        - A class that is responsible for sending a request to a server and also responsible for parsing the response is violating the S.R.P. 
        - A class that is responsible for sending a request to a server and also responsible for saving the response to a database is violating the S.R.P.
    - Coding Time ;)
      - Go to [S.R.P.](./SOLID/SRP.py) to see the code example.
  
  - ### Open/Closed Principle

      Software entities (e.g., classes, modules, functions) should be open for extension but closed for modification. This principle encourages extending the behavior of a module without altering its source code.

      - Why O.C.P.?
          - It promotes code stability, reducing the risk of introducing bugs when modifying existing code.
          - It allows for the addition of new features or functionality without changing existing code.
          - It enhances code reusability and maintainability.
          - It encourages the use of polymorphism and abstraction.

      - Real-World Example
          - In a drawing application, you have various shapes (circles, squares, triangles). You want to add new shapes without modifying the existing drawing code.
          - In a payment processing system, you need to support multiple payment methods (credit card, PayPal, cryptocurrency) without altering the core payment processing logic.

      - Coding Time ;)
        - Check out the code example demonstrating the Open/Closed Principle in action [here](./SOLID/OCP.py).


  - ### Liskov Substitution Principle

    Subtypes must be substitutable for their base types without altering the correctness of the program. In other words, if a program is using a base class, it should be able to use its derived class without causing issues.

    - Why L.S.P.?
        - It ensures that derived classes maintain the expected behavior of their base classes, enhancing code reliability.
        - It allows for polymorphism and flexibility in software design.
        - It promotes code reuse and extensibility.

    - Real-World Example
        - In a geometric shapes hierarchy, you have a base class `Shape` and derived classes like `Circle` and `Rectangle`. The LSP ensures that any code expecting a `Shape` can work seamlessly with `Circle` or `Rectangle` instances.
        - In a banking system, you have a base class `Account` and derived classes like `SavingsAccount` and `CheckingAccount`. The LSP ensures that operations on an `Account` can be performed on its derived types without errors.

    - Coding Time ;)
      - Check out the code example demonstrating the Liskov Substitution Principle in action [here](./SOLID/LSP.py).

  - ### Interface Segregation Principle

    Clients should not be forced to depend on interfaces they do not use. In other words, interfaces should be specific to the needs of the clients that use them.

    - Why ISP?
        - It promotes more modular and maintainable code.
        - It avoids the problem of clients being burdened with unnecessary methods.
        - It encourages a clear and focused design for interfaces.
        - It minimizes the impact of changes in one part of the system on unrelated parts.

    - Real-World Example
        - In a software system, there are various types of workers, including humans and robots. The original design provides a single `Worker` interface with both `work` and `eat` methods. This forces robot classes to implement irrelevant `eat` methods, violating the ISP.
        - After adhering to ISP, the design splits the `Worker` interface into `Workable` and `Eatable` interfaces, allowing classes like robots to implement only the `Workable` interface, and humans to implement both `Workable` and `Eatable` interfaces, promoting a more focused and modular interface design.

    - Coding Time ;)
      - Go to [ISP Example](./SOLID/ISP.py) to see the code example demonstrating the Interface Segregation Principle in action.

  - ### Dependency Inversion Principle

    High-level modules should not depend on low-level modules. Both should depend on abstractions. Abstractions should not depend on details. Details should depend on abstractions.

    - Why DIP?
        - It promotes decoupling between modules and components.
        - It enhances flexibility and scalability in the codebase.
        - It allows for easier unit testing and maintenance.
        - It encourages a clear separation of concerns.

    - Real-World Example
        - In a large software project, the high-level business logic components depend on low-level data access components directly. This tight coupling can make it difficult to replace or upgrade the data access layer without affecting the entire system. Adhering to DIP, you can introduce an abstraction (e.g., an interface) that both high-level and low-level components depend on, reducing the coupling and allowing for more flexibility in changing the data access layer.

        > "You can solve every problem with another level of indirection, except for the problem of too many levels of indirection"
        > - Butler Lampson

    - Coding Time ;)
      - Go to [DIP Example](./SOLID/DIP.py) to see the code example demonstrating the Dependency Inversion Principle in action.

## Design Patterns

 - ### Creational Patterns

    - #### Singleton

        The Singleton pattern ensures that only one instance of a class is created and provides a global point of access to that instance.

        - Why Singleton?
            - It provides a global point of access to a single instance, reducing the need for global variables.
            - It allows for lazy initialization of the singleton instance, reducing the memory footprint of the program.
            - It allows for easy access to the singleton instance during unit testing.
            - It allows for the extension of singleton behavior by subclassing the singleton class.

        - Real-World Example
            - In a game, there is only one game manager that manages the game state and player scores.
            - In a GUI application, there is only one application window that handles user input and displays the application state.

        - Coding Time ;)
          - Go to [Singleton Example](./DP/singleton.py) to see the code example demonstrating the Singleton pattern in action.