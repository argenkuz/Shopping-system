import sys
import requests
from io import BytesIO
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QTimer
from project.qt import Ui_MainWindow
from project.login import Ui_LoginWindow
from project.cart import Ui_CartWindow
from model import Model
from dao.user_dao import UserDAO
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QLabel
from dao.shoppingcart_dao import ShoppingCartDAO
from PyQt6.QtGui import QTextDocument
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.QtWidgets import QHeaderView



class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main_window = None
        self.login_window = None
        self.cart_window = None
        self.ui_main = Ui_MainWindow()
        self.ui_login = Ui_LoginWindow()
        self.ui_cart = Ui_CartWindow()
        self.model = Model()
        self.cartDao = ShoppingCartDAO("/Users/argenkulzhanov/Desktop/Final/shopping_system.sqlite")
        self.dao = UserDAO("/Users/argenkulzhanov/Desktop/Final/shopping_system.sqlite")
        self.reset_code = None
        self.email = None
        self.labels = self.centralwidget.findChildren(QtWidgets.QLabel)
        self.cartDao.delete_all()

    """        
    def load_images(self):
        self.load_image_from_url(self.ui_main.label_45, "https://m.media-amazon.com/images/I/61n0lmxP5-L._AC_UY218_.jpg")  # Replace with your image URL
        self.load_image_from_url(self.ui_main.label_53, "https://m.media-amazon.com/images/I/61fh21u3DJL._AC_UY218_.jpg")  # Replace with your image URL
        self.load_image_from_url(self.ui_main.label_33, "https://m.media-amazon.com/images/I/71VV0kyOKCL._AC_UY218_.jpg")  # Replace with your image URL
        self.load_image_from_url(self.ui_main.label_61, "https://m.media-amazon.com/images/I/61xk4XNRktL._AC_UY218_.jpg")  # Replace with your image URL
        self.load_image_from_url(self.ui_main.label_41, "https://m.media-amazon.com/images/I/71JN6auKgKL._AC_UY218_.jpg")  # Replace with your image URL
        self.load_image_from_url(self.ui_main.label_73, "https://m.media-amazon.com/images/I/71FSzZAkyjL._AC_UY218_.jpg")  # Replace with your image URL
        #TVs
        self.load_image_from_url(self.ui_main.label_81, "https://m.media-amazon.com/images/I/61i1nyxiqjL._AC_UY436_FMwebp_QL65_.jpg")  # Replace with your image URL
        self.load_image_from_url(self.ui_main.label_161, "https://m.media-amazon.com/images/I/61ClNi6f90L._AC_UY436_FMwebp_QL65_.jpg")  # Replace with your image URL
        self.load_image_from_url(self.ui_main.label_105, "https://m.media-amazon.com/images/I/51ZFeo4yrLL._AC_UY436_FMwebp_QL65_.jpg")  # Replace with your image URL
        self.load_image_from_url(self.ui_main.label_137, "https://m.media-amazon.com/images/I/71lUqyqGKKL._AC_UY436_FMwebp_QL65_.jpg")  # Replace with your image URL
        self.load_image_from_url(self.ui_main.label_153, "https://m.media-amazon.com/images/I/71YXjVYWdyL._AC_UY436_FMwebp_QL65_.jpg")
        self.load_image_from_url(self.ui_main.label_169, "https://m.media-amazon.com/images/I/6128QeCWeLL._AC_UY436_FMwebp_QL65_.jpg")
        # Laptops
        self.load_image_from_url(self.ui_main.label_97, "https://m.media-amazon.com/images/I/71Ej6sIsNaL._AC_UY436_FMwebp_QL65_.jpg")
        self.load_image_from_url(self.ui_main.label_113,"https://m.media-amazon.com/images/I/61-oTP1X4rL._AC_UY436_FMwebp_QL65_.jpg")
        self.load_image_from_url(self.ui_main.label_89,"https://m.media-amazon.com/images/I/61PS8u04WwL._AC_UY436_QL65_.jpg")
        self.load_image_from_url(self.ui_main.label_121,"https://m.media-amazon.com/images/I/71r9BNO+8gL._AC_UY436_FMwebp_QL65_.jpg")
        self.load_image_from_url(self.ui_main.label_177,"https://m.media-amazon.com/images/I/81VNCWPxsVL._AC_UY436_FMwebp_QL65_.jpg")
        self.load_image_from_url(self.ui_main.label_185,"https://m.media-amazon.com/images/I/81lWUzhyBlL._AC_UY436_FMwebp_QL65_.jpg")
        #Tablets
        self.load_image_from_url(self.ui_main.label_201,"https://m.media-amazon.com/images/I/51rZDWRDWAL._AC_UY436_QL65_.jpg")
        self.load_image_from_url(self.ui_main.label_217,"https://m.media-amazon.com/images/I/71Ooq-c-nZL._AC_UY436_FMwebp_QL65_.jpg")
        self.load_image_from_url(self.ui_main.label_233,"https://m.media-amazon.com/images/I/617mLPA83fL._AC_UY436_QL65_.jpg")
        self.load_image_from_url(self.ui_main.label_209,"https://m.media-amazon.com/images/I/61JgQqAl00L._AC_UY436_QL65_.jpg")
        self.load_image_from_url(self.ui_main.label_225,"https://m.media-amazon.com/images/I/81w8usV6vxL._AC_UY436_FMwebp_QL65_.jpg")
        self.load_image_from_url(self.ui_main.label_241,"https://m.media-amazon.com/images/I/719U7raGViL._AC_UY436_FMwebp_QL65_.jpg")
        # Headphones
        self.load_image_from_url(self.ui_main.label_273,"https://m.media-amazon.com/images/I/71dwcdKD4+L._AC_UY436_FMwebp_QL65_.jpg")
        self.load_image_from_url(self.ui_main.label_281, "https://m.media-amazon.com/images/I/81mUqiW8YiL._AC_UY436_QL65_.jpg")
        self.load_image_from_url(self.ui_main.label_289,"https://m.media-amazon.com/images/I/61g7yQD0S2L._AC_UY436_QL65_.jpg")
        self.load_image_from_url(self.ui_main.label_297, "https://m.media-amazon.com/images/I/71T1OmRuZBL._AC_UY436_QL65_.jpg")
        self.load_image_from_url(self.ui_main.label_305,"https://m.media-amazon.com/images/I/71t-NRjVRtL._AC_UY436_QL65_.jpg")
        self.load_image_from_url(self.ui_main.label_313, "https://m.media-amazon.com/images/I/71V-8Mkx-vL._AC_UY436_QL65_.jpg")
    """

    def show_main_window(self):
        self.main_window = QMainWindow()
        self.ui_main.setupUi(self.main_window)
        self.init_main_window_buttons()
        self.ui_main.pushButton_2.clicked.connect(self.show_login_window)
        self.ui_main.pushButton_6.clicked.connect(self.show_cart_window)
        self.main_window.show()
        self.ui_main.tabWidget.setCurrentIndex(7)
        #self.load_images()

    def show_login_window(self):
        self.login_window = QMainWindow()
        self.ui_login.setupUi(self.login_window)
        self.init_login_window_buttons()
        self.login_window.show()

    def show_cart_window(self):
        self.cart_window = QMainWindow()
        self.ui_cart.setupUi(self.cart_window)
        self.load_cart_table()
        self.cart_window.show()
        self.load_cart_table()


    def init_main_window_buttons(self):
        self.ui_main.pushButton.clicked.connect(self.search_information)
        self.ui_main.pushButton_3.clicked.connect(self.switch_to_tab_1)
        self.ui_main.pushButton_4.clicked.connect(self.switch_to_tab_2)
        self.ui_main.pushButton_5.clicked.connect(self.switch_to_tab_3)
        self.ui_main.pushButton_7.clicked.connect(self.switch_to_tab_5)
        self.ui_main.pushButton_10.clicked.connect(self.switch_to_tab_8)
        self.ui_main.tabWidget.tabBar().hide()
        self.ui_main.tabWidget.setCurrentIndex(5)
        self.ui_main.pushButton_18.clicked.connect(
            lambda: self.add_to_cart(self.ui_main.label_52, self.ui_main.label_51)
        )

        self.ui_main.pushButton_16.clicked.connect(
            lambda: self.add_to_cart(self.ui_main.label_40, self.ui_main.label_39)
        )
        self.ui_main.pushButton_22.clicked.connect(
            lambda: self.add_to_cart(self.ui_main.label_72, self.ui_main.label_71)
        )
        self.ui_main.pushButton_20.clicked.connect(
            lambda: self.add_to_cart(self.ui_main.label_60, self.ui_main.label_59)
        )
        self.ui_main.pushButton_24.clicked.connect(
            lambda: self.add_to_cart(self.ui_main.label_68, self.ui_main.label_67)
        )
        self.ui_main.pushButton_26.clicked.connect(
            lambda: self.add_to_cart(self.ui_main.label_80, self.ui_main.label_79)
        )

        #laptops
        self.ui_main.pushButton_32.clicked.connect(
            lambda: self.add_to_cart(self.ui_main.label_104, self.ui_main.label_103)
        )
        self.ui_main.pushButton_30.clicked.connect(
            lambda: self.add_to_cart(self.ui_main.label_96, self.ui_main.label_95)
        )
        self.ui_main.pushButton_52.clicked.connect(
            lambda: self.add_to_cart(self.ui_main.label_184, self.ui_main.label_183)
        )
        self.ui_main.pushButton_36.clicked.connect(
            lambda: self.add_to_cart(self.ui_main.label_120, self.ui_main.label_119)
        )
        self.ui_main.pushButton_38.clicked.connect(
            lambda: self.add_to_cart(self.ui_main.label_128, self.ui_main.label_127)
        )
        self.ui_main.pushButton_54.clicked.connect(
            lambda: self.add_to_cart(self.ui_main.label_192, self.ui_main.label_191)
        )

        #TVs
        self.ui_main.pushButton_28.clicked.connect(
            lambda: self.add_to_cart(self.ui_main.label_88, self.ui_main.label_87)
        )
        self.ui_main.pushButton_42.clicked.connect(
            lambda: self.add_to_cart(self.ui_main.label_144, self.ui_main.label_143)
        )
        self.ui_main.pushButton_48.clicked.connect(
            lambda: self.add_to_cart(self.ui_main.label_168, self.ui_main.label_167)
        )
        self.ui_main.pushButton_46.clicked.connect(
            lambda: self.add_to_cart(self.ui_main.label_160, self.ui_main.label_159)
        )
        self.ui_main.pushButton_34.clicked.connect(
            lambda: self.add_to_cart(self.ui_main.label_112, self.ui_main.label_111)
        )
        self.ui_main.pushButton_50.clicked.connect(
            lambda: self.add_to_cart(self.ui_main.label_176, self.ui_main.label_175)
        )
        #tablets
        self.ui_main.pushButton_58.clicked.connect(
            lambda: self.add_to_cart(self.ui_main.label_208, self.ui_main.label_207)
        )
        self.ui_main.pushButton_62.clicked.connect(
            lambda: self.add_to_cart(self.ui_main.label_224, self.ui_main.label_223)
        )
        self.ui_main.pushButton_66.clicked.connect(
            lambda: self.add_to_cart(self.ui_main.label_240, self.ui_main.label_239)
        )
        self.ui_main.pushButton_60.clicked.connect(
            lambda: self.add_to_cart(self.ui_main.label_216, self.ui_main.label_215)
        )
        self.ui_main.pushButton_64.clicked.connect(
            lambda: self.add_to_cart(self.ui_main.label_232, self.ui_main.label_231)
        )
        self.ui_main.pushButton_68.clicked.connect(
            lambda: self.add_to_cart(self.ui_main.label_248, self.ui_main.label_247)
        )
        #headphones
        self.ui_main.pushButton_76.clicked.connect(
            lambda: self.add_to_cart(self.ui_main.label_280, self.ui_main.label_279)
        )
        self.ui_main.pushButton_80.clicked.connect(
            lambda: self.add_to_cart(self.ui_main.label_296, self.ui_main.label_295)
        )
        self.ui_main.pushButton_84.clicked.connect(
            lambda: self.add_to_cart(self.ui_main.label_312, self.ui_main.label_311)
        )
        self.ui_main.pushButton_78.clicked.connect(
            lambda: self.add_to_cart(self.ui_main.label_288, self.ui_main.label_287)
        )
        self.ui_main.pushButton_82.clicked.connect(
            lambda: self.add_to_cart(self.ui_main.label_304, self.ui_main.label_303)
        )
        self.ui_main.pushButton_86.clicked.connect(
            lambda: self.add_to_cart(self.ui_main.label_320, self.ui_main.label_319)
        )

    def init_login_window_buttons(self):
        self.ui_login.pushButton_3.clicked.connect(self.switch_to_tab_login)
        self.ui_login.pushButton_4.clicked.connect(self.switch_to_tab_create_account)
        self.ui_login.pushButton_6.clicked.connect(self.create_account)
        self.ui_login.pushButton_8.clicked.connect(self.on_cancel_create_account_clicked)
        self.ui_login.pushButton_9.clicked.connect(self.on_cancel_create_account_clicked)
        self.ui_login.pushButton_10.clicked.connect(self.login_account)
        self.ui_login.pushButton_11.clicked.connect(self.on_forgot_password_clicked)
        self.ui_login.pushButton_12.clicked.connect(self.on_cancel_clicked)
        self.ui_login.pushButton_13.clicked.connect(self.on_cancel_create_account_clicked)
        self.ui_login.pushButton_14.clicked.connect(self.switch_to_tab_condition_of_use)
        self.ui_login.pushButton_15.clicked.connect(self.switch_to_tab_usage_policy)
        self.ui_login.pushButton_16.clicked.connect(self.on_cancel_create_account_clicked)
        self.ui_login.pushButton_17.clicked.connect(self.on_send_code_clicked)
        self.ui_login.pushButton_18.clicked.connect(self.on_cancel_create_account_clicked)
        self.ui_login.pushButton_31.clicked.connect(self.change_password)
        self.ui_login.pushButton_32.clicked.connect(self.on_check_code_clicked)
        self.set_visible()
        self.ui_login.tabWidget.tabBar().hide()
        self.ui_login.tabWidget.setCurrentIndex(0)

    def get_plain_text(self,html_text):
        doc = QTextDocument()
        doc.setHtml(html_text)
        return doc.toPlainText()

    def add_to_cart(self, new_label, price_label):
        name_html = new_label.text()
        price_html = price_label.text()

        name = self.get_plain_text(name_html)
        price = self.get_plain_text(price_html).split(" ")[1]
        price = int(price[:-1])

        if self.cartDao.find_by_product_name(name) is None:
            self.cartDao.insert(name, price, 1)
        else:
            product = self.cartDao.find_by_product_name(name)
            quantity = product["quantity"] + 1
            self.cartDao.update_quantity(name, quantity)



    def set_visible(self):
        self.ui_login.label_10.setVisible(False)
        self.ui_login.label_13.setVisible(False)
        self.ui_login.label_14.setVisible(False)
        self.ui_login.label_15.setVisible(False)
        self.ui_login.label_16.setVisible(False)
        self.ui_login.label_17.setVisible(False)
        self.ui_login.label_12.setVisible(False)
        self.ui_login.label_11.setVisible(False)
        self.ui_login.label_19.setVisible(False)
        self.ui_login.label_20.setVisible(False)
        self.ui_login.label_21.setVisible(False)

    def switch_to_tab_login(self):
        self.ui_login.tabWidget.setCurrentIndex(1)

    def switch_to_tab_create_account(self):
        self.ui_login.tabWidget.setCurrentIndex(2)

    def on_cancel_create_account_clicked(self):
        self.ui_login.tabWidget.setCurrentIndex(0)
        self.set_visible()

    def switch_to_tab_condition_of_use(self):
        self.ui_login.tabWidget.setCurrentIndex(3)

    def switch_to_tab_usage_policy(self):
        self.ui_login.tabWidget.setCurrentIndex(4)

    def search_information(self):
        self.highlight_labels()

    def switch_to_tab_1(self):
        self.ui_main.tabWidget.setCurrentIndex(0)

    def switch_to_tab_2(self):
        self.ui_main.tabWidget.setCurrentIndex(1)

    def switch_to_tab_3(self):
        self.ui_main.tabWidget.setCurrentIndex(2)

    def switch_to_tab_5(self):
        self.ui_main.tabWidget.setCurrentIndex(4)

    def switch_to_tab_8(self):
        self.ui_main.tabWidget.setCurrentIndex(3)

    def login_account(self):
        username = self.ui_login.lineEdit_15.text()
        password = self.ui_login.lineEdit_16.text()
        self.set_visible()

        if self.dao.find_by_username(username) == None:
            self.ui_login.label_10.setText("Wrong username")
            self.ui_login.label_10.setVisible(True)

        else:
            my_password = self.dao.find_by_username(username).get_password()

            if password != my_password:
                self.ui_login.label_10.setText("Wrong password")
                self.ui_login.label_10.setVisible(True)

            else:
                self.ui_login.label_10.setVisible(False)
                self.ui_login.label_11.setText("Successfully login")
                self.ui_login.label_11.setVisible(True)
                QTimer.singleShot(2000, self.login_window.close)
                username = self.model.len_of_username(username)
                self.ui_main.pushButton_2.setText(username)

    def on_forgot_password_clicked(self):
        self.ui_login.tabWidget.setCurrentIndex(5)

    def on_cancel_clicked(self):
        self.login_window.close()

    def create_account(self):
        self.set_visible()
        name = self.ui_login.lineEdit_11.text()
        username = self.ui_login.lineEdit_13.text()
        password = self.ui_login.lineEdit_9.text()
        address = self.ui_login.lineEdit_12.text()
        email = self.ui_login.lineEdit_14.text()
        phone_number = self.ui_login.lineEdit_10.text()

        result = self.model.create_account(name, username, password, address, email, phone_number)

        if result["success"]:
            self.dao.insert(self.model.users[username])
            self.ui_login.tabWidget.setCurrentIndex(1)

        else:
            for error_message, label_name in result["errors"]:
                label = getattr(self.ui_login, label_name)
                label.setText(error_message)
                label.setVisible(True)

    def on_send_code_clicked(self):
        self.set_visible()
        self.email = self.ui_login.lineEdit_17.text()
        if self.email != "":
            result = self.dao.find_by_email(self.email)
            if result is not None:
                self.reset_code = self.model.send_reset_password(self.email)
                self.ui_login.lineEdit_17.setEnabled(False)
                self.ui_login.label_19.setText("Code is sent to your email")
                self.ui_login.label_19.setVisible(True)
                self.ui_login.lineEdit_18.setVisible(True)


            else:
                self.ui_login.label_20.setText("Email not found")
                self.ui_login.label_20.setVisible(True)
        else:
            self.ui_login.label_20.setText("Input something")
            self.ui_login.label_20.setVisible(True)

    def on_check_code_clicked(self):
        if int(self.ui_login.lineEdit_18.text()) == self.reset_code:
            self.ui_login.tabWidget.setCurrentIndex(6)
            self.ui_login.lineEdit_17.setEnabled(True)

    def change_password(self):
        self.set_visible()
        password = self.ui_login.lineEdit_30.text()
        confirm_password = self.ui_login.lineEdit_29.text()
        if password == confirm_password:
            if self.model.is_strong_password(password):
                self.dao.update_password(self.email, password)
                self.switch_to_tab_login()
            else:
                self.ui_login.label_21.setText("Passwords is weak")
                self.ui_login.label_21.setVisible(True)
        else:
            self.ui_login.label_21.setText("Passwords do not match")
            self.ui_login.label_21.setVisible(True)

    def load_image_from_url(self, label, url):
        response = requests.get(url)
        if response.status_code == 200:
            image_data = BytesIO(response.content)
            pixmap = QPixmap()
            pixmap.loadFromData(image_data.read())
            label.setPixmap(pixmap)
            label.setScaledContents(True)
        else:
            label.setText("Ошибка загрузки")

    def highlight_labels(self):
        query = self.ui_main.lineEdit.text()

        for query in self.findChildren(QLabel):
            self.ui_main.lineEdit.setText("")

    def load_cart_table(self):
        rows = self.cartDao.get_all_items_without_id()
        self.ui_cart.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.ui_cart.tableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )


        self.ui_cart.tableWidget.setRowCount(len(rows))
        self.ui_cart.tableWidget.setColumnCount(5)
        self.ui_cart.tableWidget.setHorizontalHeaderLabels(["Item", "Quantity", "Price","Added at", "Total Price"])

        total_sum = 0
        for row_idx, (item, qty, price,added_at) in enumerate(rows):
            total_price = int(qty * price)
            total_sum += total_price

            self.ui_cart.tableWidget.setItem(row_idx, 0, QTableWidgetItem(str(item)))
            self.ui_cart.tableWidget.setItem(row_idx, 1, QTableWidgetItem(str(price)))
            self.ui_cart.tableWidget.setItem(row_idx, 2, QTableWidgetItem(f"{str(qty)}$"))
            self.ui_cart.tableWidget.setItem(row_idx, 3, QTableWidgetItem(str(added_at)))
            self.ui_cart.tableWidget.setItem(row_idx, 4, QTableWidgetItem(f"{str(total_price)}$"))

        last_row = self.ui_cart.tableWidget.rowCount()
        self.ui_cart.tableWidget.insertRow(last_row)
        self.ui_cart.tableWidget.setItem(last_row, 3, QTableWidgetItem("Total:"))
        self.ui_cart.tableWidget.setItem(last_row, 4, QTableWidgetItem(f"{total_sum}$"))