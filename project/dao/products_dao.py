from dao.BaseDao import Dao
import sys

sys.path.append("/Users/argenkulzhanov/Desktop/Final/project/classes")
from product import Products

class ProductsDAO(Dao):
    def __init__(self, db_path):
        super().__init__(db_path)

    def insert(self, product: Products):
        query = "INSERT INTO Products (product_name, description, price, stock_quantity, category) VALUES (?, ?, ?, ?, ?)"
        self.execute_query(query, (product.get_product_name(), product.get_description(), product.get_price(), product.get_stock_quantity(), product.get_category()))

        self._connection.commit()
        return self._cursor.lastrowid

    def find_by_product_name(self, product_name: str):
        query = "SELECT * FROM Products WHERE product_name = ?"
        row = self.fetch_one(query, (product_name,))
        if row:
            return Products(row[1], row[2], row[3], row[4], row[5])
        else:
            return None

    def get_all_products(self):
        query = "SELECT * FROM Products"
        return self.fetch_all(query)

    def update_stock(self, product_name: str, quantity: int):
        query = "UPDATE Products SET stock_quantity = stock_quantity - ? WHERE product_name = ?"
        self.execute_query(query, (quantity, product_name))

        self._connection.commit()
        return self._cursor.rowcount

    def delete(self, product_name: str):
        query = "DELETE FROM Products WHERE product_name = ?"
        self.execute_query(query, (product_name,))

        self._connection.commit()
        return self._cursor.rowcount

