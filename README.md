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
       2. [Prototype](#prototype)
       3. [Builder](#builder)
       4. [Factory Method](#factory-method)
       5. [Abstract Factory](#abstract-factory)
    2. [Structural Patterns](#structural-patterns)
       1. [Proxy](#proxy)

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
          - Go to [Singleton Example](./DP/creational/singleton.py) to see the code example demonstrating the Singleton pattern in action.

    - #### Prototype
            
        The Prototype pattern is a design concept that allows you to create new objects by duplicating an existing object, known as the prototype. This pattern is especially useful when you want to produce similar objects without explicitly specifying their class, and it becomes particularly beneficial when creating objects with heavy initialization, such as database connections or file I/O.

        - Why Prototype?
            - It simplifies the process of making new objects that share similar attributes and structures.
            - It efficiently handles the creation of objects with heavy initialization procedures.
            - It reduces code duplication by cloning prototypes.
            - It facilitates the customization of new objects based on existing ones.

        - Real-World Example
            - In a web application, you can use a prototype object for user accounts. These prototypes can be customized with user-specific data during runtime.
            - In a data processing system, you can clone a prototype processor that already holds complex and resource-intensive configurations.

        - Implementation
          - For a Python code example demonstrating the Prototype pattern with objects requiring heavy initialization, take a look at [Prototype Example](./DP/creational/prototype.py).


    - #### Builder

        The Builder pattern is a design pattern that allows for the step-by-step creation of complex objects using the correct sequence of actions. The construction is controlled by a director object that only needs to know the type of object it is to create.

        - Why Builder?
            - It allows for the step-by-step creation of complex objects.
            - It allows for the creation of different representations of the same object.
            - It allows for the creation of complex objects without exposing their internal structure.
            - It allows for the creation of complex objects without coupling the client code to their class.

        - Real-World Example
            - In a game, you can use a builder to create different types of characters (e.g., warriors, mages, archers) with different attributes (e.g., strength, intelligence, dexterity).
            - In a GUI application, you can use a builder to create different types of windows (e.g., main window, dialog window, popup window) with different components (e.g., title bar, menu bar, status bar).

        - Implementation
          - For a Python code example demonstrating the Builder pattern, take a look at [Builder Example](./DP/creational/builder.py).
    
    - #### Factory Method

        The Factory Method pattern is a design pattern that provides an interface for creating objects, but it allows subclasses to alter the type of objects that will be created. This pattern is particularly useful when you want to decouple the client code from the specific classes of objects it needs to instantiate.

        - Why Use Factory Method?

        - **Flexibility**: It allows for the creation of objects without specifying their concrete type, making it easy to switch between different implementations or variations of an object.

        - **Decoupling**: It decouples the client code from the details of object creation, ensuring that the client code doesn't depend on specific classes, making it more maintainable and extensible.

        - **Extensibility**: It allows for the extension of the factory method to create new types of objects, making it straightforward to add new object types without modifying existing code.

        - Real-World Examples

        - ##### ***Example 1: Document Generation*** 


            Consider a document generation system where you have various types of documents like reports, letters, and invoices. The Factory Method pattern can be used to create document objects:

          - **DocumentFactory**: The base factory class with a method for creating documents.
          - **ReportFactory**: A subclass that creates report documents.
          - **LetterFactory**: A subclass that creates letter documents.
          - **InvoiceFactory**: A subclass that creates invoice documents.

            This approach allows the client to create documents without worrying about the concrete classes involved.

        - ##### ***Example 2: Image Processing***

            In an image processing application, you can use the Factory Method pattern to create various filters for images:

            - **FilterFactory**: The base factory class with a method for creating image filters.
            - **BlurFilterFactory**: A subclass that creates blur filters.
            - **SepiaFilterFactory**: A subclass that creates sepia tone filters.
            - **GrayscaleFilterFactory**: A subclass that creates grayscale filters.

            This enables the application to apply different filters to images without hardcoding the filter types.

        - Implementation
          - For a Python code example demonstrating the Factory pattern, take a look at [Factory Example](./DP/creational/factory.py).



   - #### Abstract Factory

        The Abstract Factory pattern is a design pattern that provides an interface for creating families of related or dependent objects without specifying their concrete classes. This pattern is particularly useful when you want to ensure that the created objects are compatible and cohesive, maintaining a consistent interface among them.

       - Why Use Abstract Factory?

           - **Consistency and Compatibility**: It ensures that the created objects are part of a cohesive family and are compatible with each other, promoting consistency in their usage.

           - **Encapsulation**: It encapsulates the creation of related objects, abstracting the client code from the details of how objects are created.

           - **Scalability**: It makes it easy to add new product families (concrete factories) and their related products (concrete products) without affecting existing code.

       - Real-World Examples

           - ##### ***Example 1: Furniture Manufacturing*** 

               In a furniture manufacturing system, you have different styles of furniture, such as modern and Victorian. The Abstract Factory pattern can be used to create furniture objects:

               - **FurnitureFactory**: The abstract factory class with methods for creating chairs and tables.
               - **ModernFurnitureFactory**: A concrete factory that creates modern-style chairs and tables.
               - **VictorianFurnitureFactory**: A concrete factory that creates Victorian-style chairs and tables.

               This approach ensures that chairs and tables are created consistently within each style, allowing for cohesive furniture sets.

           - ##### ***Example 2: Operating System***

               In an operating system development project, you can use the Abstract Factory pattern to create families of related objects, such as widgets:

               - **WidgetFactory**: The abstract factory class with methods for creating buttons, menus, and windows.
               - **WindowsWidgetFactory**: A concrete factory for creating Windows-style widgets.
               - **LinuxWidgetFactory**: A concrete factory for creating Linux-style widgets.

               This ensures that widgets are created consistently to match the style of the operating system.

       - Implementation

           - For a Python code example demonstrating the Abstract Factory pattern, take a look at [Abstract Factory Example](./DP/creational/abstractFactory.py).

 - ### Structural Patterns
    - #### Proxy

        The Proxy pattern is a design pattern that provides a surrogate or placeholder for another object to control access to it. This pattern is particularly useful when you want to add functionality to an existing object without changing its code.

        - Why Use Proxy?

            - **Security**: It allows for the implementation of security restrictions on the original object.
            - **Simplicity**: It provides a simpler interface to the original object.

        - Real-World Examples

            - ##### ***Example 1: Ngnix Web Server***

                In a web server, you can use the Proxy pattern to implement a caching proxy:

                - **WebServer**: The original object that handles incoming requests.
                - **CachingProxy**: The proxy object that caches the results of requests.

                This approach allows the proxy to handle requests that can be served from the cache, reducing the load on the web server.
            
            - ##### ***Example 2: SMS Limiter***

                In a messaging application, you can use the Proxy pattern to implement a proxy that limits the number of SMS messages sent per day:

                - **MessageSender**: The original object that sends SMS messages.
                - **MessageSenderProxy**: The proxy object that limits the number of SMS messages sent per day.

                This approach allows the proxy to limit the number of SMS messages sent per day, preventing the original object from exceeding the daily limit.
        - Implementation
            - For a Python code example demonstrating the Proxy pattern, take a look at [Proxy Example](./DP/structural/proxy.py).
    
    - #### Decorator

        The Decorator pattern is a design pattern that allows behavior to be added to an individual object, dynamically, without affecting the behavior of other objects from the same class. This pattern is particularly useful when you want to add functionality to an existing object without changing its code.

        - Why Use Decorator?

            - **Extensibility**: It allows for the dynamic addition of new behavior to an object without affecting the behavior of other objects from the same class.
            - **Simplicity**: It provides a simpler interface to the original object.

        - Real-World Examples

            - ##### ***Example 1: Coffee Shop***

                In a coffee shop, you can use the Decorator pattern to implement a decorator that adds extra toppings to coffee:

                - **Coffee**: The original object that represents a coffee.
                - **CoffeeDecorator**: The decorator object that adds extra toppings to coffee.

                This approach allows the decorator to add extra toppings to coffee, without affecting the behavior of other coffee objects.

            - ##### ***Example 2: Text Editor***

                In a text editor, you can use the Decorator pattern to implement a decorator that adds spell checking to text:

                - **Text**: The original object that represents text.
                - **TextDecorator**: The decorator object that adds spell checking to text.

                This approach allows the decorator to add spell checking to text, without affecting the behavior of other text objects.

        - Implementation

            - For a Python code example demonstrating the Decorator patclook at [Decorator Example](./DP/structural/decorator.py).