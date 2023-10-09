# SOLID Principles & Design Patterns Explained!

Welcome to the "SOLID Principles and Design Patterns Explained" repository! Dive into the world of software engineering excellence with comprehensive explanations and practical code examples that demystify the SOLID principles and illuminate the power of design patterns.

## Table of Contents
1. [SOLID Principles](#solid-principles)
    1. [Single Responsibility Principle](#single-responsibility-principle)
    2. [Open-Closed Principle](#openclosed-principle)
    3. [Liskov Substitution Principle](#liskov-substitution-principle)
    4. [Interface Segregation Principle](#interface-segregation-principle)

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