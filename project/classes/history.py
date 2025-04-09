from user import User
from product import Products

class History:
    def __init__(self, user, product, quantity, total_amount, ):
        self.__user = user.get_name()
        self.__product = product.get_product_name()
        self.__quantity = quantity
        self.__total_amount = total_amount

    def get_user(self):
        return self.__user

    def get_product(self):
        return self.__product

    def get_quantity(self):
        return self.__quantity

    def get_total_amount(self):
        return self.__total_amount

    def __str__(self):
        return f"User: {self.__user}, Product: {self.__product}, Quantity: {self.__quantity}, Total Amount: {self.__total_amount}"