# Simple GUI Shopping System

This repository contains the simple shopping system built on Python. This project has Graphical User Interface(GUI) and implementation of databases.

## Our Team
- [Argen Kulzhanov](https://github.com/argenkuz) (argenkuz): Design and GUI.
- [Kirill Donetskov](https://github.com/kd0nwww) (kd0nwww): Code and logic.
- [Magomed Mukhamedov](): Databases and documentation.

## Structure
- [user.py](/project/classes/user.py) : Contains the class that creates `User` instances.
- [product.py](/project/classes/product.py) : Contains the class that creates `Product` instances.
- [shoppingcart.py](/project/classes/shoppingcart.py) : Class that creates `ShoppingCart` instances.
- [base_dao.py](/project/dao/base_dao.py) : Contains the base DAO class (`Dao`) that is responsible to make CRUD operations with the database.
- [user_dao.py](/project/dao/user_dao.py) : Contains DAO class that inherits from `Dao` that is in base_dao.py
- [parser](/project/parser) : Simple Amazon web scraper.
- [controller.py](/project/controller.py) : This file makes the connection between logic and design.
- [login.py](/project/login.py) : File with the design of login page.
- [main.py](/project/main.py) : File that launches the whole program.
- [model.py](/project/model.py) : File that contains the logic of program.
- [qt.py](/project/qt.py) : File that contains the design of starting page.

## User class
### Attributes
- `name`: User's name.
- `username`
- `password`
- `address`
- `email`
- `phone_number`

## Dao class
This class represents a blueprint for managing user-related database operations.

### Attributes
- `db_path`:  path do database.

### Methods
- `execute_query(query: str, params=None)`: Executes the SQL query that is given in `query` attribute with some parameters which are `None` by default.
- `fetch_all(query: str, params=None)`: Return all records contained in cursor.
- `fetch_one(query: str, params=None)`: Return one record contained in cursor.

## UserDAO class
This class provides functionality to interact with the Users table in the database. 
The class includes methods to insert new users, retrieve user details by username or email, fetch all users, and update user passwords. Inherits from `base_dao.py`.

### Attributes
- `db_path`: path do database.

### Methods
- `insert(user: User)`: Inserts new `User` object into Users table.
- `find_by_username(username: str)`: Finds the record in database with the given `username`.
- `find_by_email(email: str)`: Finds the record in database with the given `email`.
- `get_all_users()`: Return all `User` objects contained in database.
- `update_password(email: str, new_password: str)`: Updates the `User` objects password with the given `email`.

## Model class
This class contains the logic of whole program.
