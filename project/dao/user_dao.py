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

        self._connection.commit()
        return self._cursor.lastrowid
    
    def find_by_username(self, username: str):
        query = "SELECT * FROM Users WHERE username = ?"
        row = self.fetch_one(query, (username,))
        if row:
            return User(row[4], row[1], row[3], row[5], row[2], row[6])
        else:
            return None
        
    def find_by_email(self, email: str):
        query = "SELECT * FROM Users WHERE email = ?"
        row = self.fetch_one(query, (email,))
        if row:
            return User(row[4], row[1], row[3], row[5], row[2], row[6])
        else:
            return None
        
    def get_all_users(self):
        query = "SELECT * FROM Users"
        return self.fetch_all(query)
    
    def update_password(self, email: str, new_password: str):
        query = "UPDATE Users SET password = ? WHERE email = ?"
        self.execute_query(query, (new_password, email))
        
        self._connection.commit()
        return self._cursor.rowcount