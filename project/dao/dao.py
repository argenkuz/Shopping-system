import sqlite3

class Dao:
    def __init__(self, db_path):
        self.__connection = sqlite3.connect(db_path)
        self.__cursor = self.__connection.cursor()

    def execute_query(self, query, params=None):
        self.__cursor.execute(query, params or [])
        self.__connection.commit()
        return self.__cursor
    
    def fetch_all(self, query, params=None):
        self.__cursor.execute(query, params or [])
        return self.__cursor.fetchall()
    
    def fetch_one(self, query, params=None):
        self.__cursor.execute(query, params or [])
        return self.__cursor.fetchone()