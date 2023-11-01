"""
Adapter Pattern Implementation

Description:
Welcome to the "Adapter Pattern Implementation" module. 
This module explores and demonstrates the Adapter design pattern, a structural pattern in software design. 
The Adapter pattern allows objects with incompatible interfaces to work together.

Module Overview:
- Problem Description: 
    We will start by presenting a scenario where two existing classes have incompatible interfaces, 
    and you need to make them work together without modifying their source code. 
    You need a way to create an adapter that enables communication between these classes.

- Solving with Adapter Pattern: 
    Next, we will implement the Adapter pattern to address the issues outlined in the problem description. 
    The Adapter acts as an intermediary that translates one interface into another, 
    making it possible for the objects to collaborate seamlessly.

By the end of this module, you will have a clear understanding of how to use the Adapter pattern to bridge the gap 
between objects with different interfaces, ensuring compatibility and smooth integration in your software systems.
"""

from abc import ABC, abstractmethod

# Adapter Interface


# Database Contract (Abstract Class)
class Database(ABC):
    @abstractmethod
    def connect(self, host, username, password, database_name):
        pass

    @abstractmethod
    def execute_query(self, query):
        pass



# PostgreSQL Database (Adheres to the Database Contract)
class PostgreSQLDatabase(Database):
    def connect(self, host, username, password, database_name):
        print(f"Connected to PostgreSQL database on {host} as {username}")

    def execute_query(self, query):
        print(f"Executing PostgreSQL Query: {query}")

# MySQL Adapter (Implements the Adapter Interface)
class MySQLAdapter(Database):
    def __init__(self, database:Database):
        self._database = database

    def connect(self, host, username, password, database_name):
        # Adapt MySQL connection details to PostgreSQL
        postgres_host = host
        postgres_username = username
        postgres_password = password
        postgres_db_name = database_name

        self._database.connect(postgres_host, postgres_username, postgres_password, postgres_db_name)

    def execute_query(self, query:str):
        # Adapt MySQL query to PostgreSQL syntax
        postgres_query = query.replace("LIMIT", "LIMIT ALL")
        self._database.execute_query(postgres_query)


class IView(ABC):
    @abstractmethod
    def render(self,data):
        pass

class View(IView):
    def render(self,data):
        print(f"handle only json data {data}")

class XMLAdapterView(IView):
    def __init__(self,view):
        self._view = view

    def render(self,data):
        print("convert xml data to json")
        self._view.render(data)
        
        


# Client
if __name__ == "__main__":
    print(" Start of Database Adapter Example")
    postgres_db = PostgreSQLDatabase()
    adapter = MySQLAdapter(postgres_db)

    host = "localhost"
    username = "user123"
    password = "password123"
    database_name = "mydb"

    adapter.connect(host, username, password, database_name)

    query = "SELECT * FROM customers LIMIT 10"
    adapter.execute_query(query)
    print("=====================================================")
    print(" Start of Data Parser Adapter Example")
    
    view = View()
    view.render("json data")
    xml_adapter_view = XMLAdapterView(view)
    xml_adapter_view.render("xml data")
