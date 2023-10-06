# SOLID Principles & Design Patterns Explained!

Welcome to the "SOLID Principles and Design Patterns Explained" repository! Dive into the world of software engineering excellence with comprehensive explanations and practical code examples that demystify the SOLID principles and illuminate the power of design patterns.

## Table of Contents
1. [SOLID Principles](#solid-principles)
    1. [Single Responsibility Principle](#single-responsibility-principle)

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
 