from product import Products
from user import User

class Reviews:
    def __init__(self, user, product, rating, comment):
        self.user_name = user.get_name()
        self.product_name = product.get_product_name()
        self.rating = rating
        self.comment = comment

    def __str__(self):
        return f"Review by {self.user_name} for {self.product_name} - Rating: {self.rating}, Comment: {self.comment}"

product1 = Products("Awesome Product", "dasd", 1000, 231, "phone")  # Создаем объект продукта
user1 = User("das","1323", "afasd","asfd","sdfasdf", "312312")  # Создаем объект пользователя
review1 = Reviews(user1, product1, 5, "Great product! Highly recommend.")  # Создаем отзыв

print(review1)