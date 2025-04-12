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


