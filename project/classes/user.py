class User:
    def __init__(self, name, username, password, address, email, phone_number):
        self.__name = name
        self.__username = username
        self.__password = password
        self.__address = address
        self.__email = email
        self.__phone_number = phone_number

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_username(self):
        return self.__username

    def set_username(self, username):
        self.__username = username

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number