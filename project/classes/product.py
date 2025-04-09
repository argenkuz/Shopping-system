class Products:
    def __init__(self,product_name, description, price, stock_quantity, category):
        self.__product_name = product_name
        self.__description = description
        self.__price = price
        self.__stock_quantity = stock_quantity
        self.__category = category

    def get_product_name(self):
        return self.__product_name
    def set_product_name(self, product_name):
        self.__product_name = product_name

    def get_description(self):
        return self.__description
    def set_description(self, description):
        self.__description = description

    def get_price(self):
        return self.__price
    def set_price(self, price):
        self.__price = price

    def get_stock_quantity(self):
        return self.__stock_quantity
    def set_stock_quantity(self, stock_quantity):
        self.__stock_quantity = stock_quantity

    def get_category(self):
        return self.__category
    def set_category(self, category):
        self.__category = category

    def __str__(self):
        return f"Product Name: {self.__product_name}, Description: {self.__description}, Price: {self.__price}, Stock Quantity: {self.__stock_quantity}, Category: {self.__category}"

    def is_available(self,amount):
        return self.__stock_quantity >= amount

    def update_stock(self, quantity):
        if quantity <= self.__stock_quantity:
            self.__stock_quantity -= quantity
            return True
        else:
            return False
