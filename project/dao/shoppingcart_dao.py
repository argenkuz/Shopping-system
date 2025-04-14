from dao.BaseDao import Dao
import sys

sys.path.append("/Users/argenkulzhanov/Desktop/Final/project/classes")

class ShoppingCartDAO(Dao):
    def init(self, db_path):
        super().init(db_path)

    def insert(self, product_name, price, quantity):
        query = "INSERT INTO ShoppingCart (product_name, price, quantity) VALUES (?, ?, ?)"
        self.execute_query(query, (product_name, price, quantity))

        self._connection.commit()
        return self._cursor.lastrowid

    def find_by_product_name(self, product_name):
        query = "SELECT * FROM ShoppingCart WHERE product_name = ?"
        row = self.fetch_one(query, (product_name,))
        if row:
            return {
                "product_name": row[1],
                "price": row[2],
                "quantity": row[3]
            }
        else:
            return None

    def update_quantity(self, product_name, quantity):
        query = "UPDATE ShoppingCart SET quantity = ? WHERE product_name = ?"
        self.execute_query(query, (quantity, product_name))

        self._connection.commit()
        return self._cursor.rowcount

    def delete_all(self):
        query = "DELETE FROM ShoppingCart"
        self.execute_query(query)

        self._connection.commit()
        return self._cursor.rowcount

    def get_all_items(self):
        query = "SELECT * FROM ShoppingCart"
        return self.fetch_all(query)

    def get_headers(self):
        query = "PRAGMA table_info(ShoppingCart)"
        rows = self.fetch_all(query)
        headers = [row[1] for row in rows]
        return headers

    def get_all_items_without_id(self):
        query = "SELECT product_name, price, quantity,added_at FROM ShoppingCart"
        return self.fetch_all(query)


