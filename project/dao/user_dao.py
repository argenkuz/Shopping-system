from dao import Dao
import sys

sys.path.append("C:/Coding/Python/OOP/Shopping-system/project/classes")

from user import User

class UserDAO(Dao):
    def __init__(self, db_path):
        super().__init__(db_path)

    def insert(self, user: User):
        query = "INSERT INTO Users (username, email, password, full_name, address, phone_number) VALUES (?, ?, ?, ?, ?, ?)"
        self.execute_query(query, (user.get_username(), user.get_email(), user.get_password(), user.get_name(), user.get_address(), user.get_phone_number()))

        self.__connection.commit()
        return self.__cursor.lastrowid