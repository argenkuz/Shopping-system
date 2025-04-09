from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import QTimer
from project.qt import Ui_MainWindow
from project.login import Ui_LoginWindow
from model import Model
from dao.user_dao import UserDAO


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main_window = None
        self.login_window = None
        self.ui_main = Ui_MainWindow()
        self.ui_login = Ui_LoginWindow()
        self.model = Model()
        self.dao = UserDAO("/Users/argenkulzhanov/Desktop/Final/shopping_system.sqlite")
        self.reset_code = None
        self.email = None


    def show_main_window(self):
        self.main_window = QMainWindow()
        self.ui_main.setupUi(self.main_window)
        #self.ui_main.tabWidget.tabBar().hide()
        self.init_main_window_buttons()
        self.ui_main.pushButton_2.clicked.connect(self.show_login_window)
        self.main_window.show()

    def show_login_window(self):
        self.login_window = QMainWindow()
        self.ui_login.setupUi(self.login_window)
        self.init_login_window_buttons()
        self.login_window.show()

    def init_main_window_buttons(self):
        self.ui_main.pushButton.clicked.connect(self.search_information)
        self.ui_main.pushButton_3.clicked.connect(self.switch_to_tab_1)
        self.ui_main.pushButton_4.clicked.connect(self.switch_to_tab_2)
        self.ui_main.pushButton_5.clicked.connect(self.switch_to_tab_3)
        self.ui_main.pushButton_6.clicked.connect(self.switch_to_tab_4)
        self.ui_main.pushButton_7.clicked.connect(self.switch_to_tab_5)
        self.ui_main.pushButton_8.clicked.connect(self.switch_to_tab_6)
        self.ui_main.pushButton_9.clicked.connect(self.switch_to_tab_7)
        self.ui_main.pushButton_10.clicked.connect(self.switch_to_tab_8)
        self.ui_main.pushButton_11.clicked.connect(self.switch_to_tab_9)

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
        search_text = self.ui_main.lineEdit.text().strip()

    def switch_to_tab_1(self):
        self.ui_main.tabWidget.setCurrentIndex(0)

    def switch_to_tab_2(self):
        self.ui_main.tabWidget.setCurrentIndex(1)

    def switch_to_tab_3(self):
        self.ui_main.tabWidget.setCurrentIndex(2)

    def switch_to_tab_4(self):
        self.ui_main.tabWidget.setCurrentIndex(3)

    def switch_to_tab_5(self):
        self.ui_main.tabWidget.setCurrentIndex(4)

    def switch_to_tab_6(self):
        self.ui_main.tabWidget.setCurrentIndex(5)

    def switch_to_tab_7(self):
        self.ui_main.tabWidget.setCurrentIndex(6)

    def switch_to_tab_8(self):
        self.ui_main.tabWidget.setCurrentIndex(7)

    def switch_to_tab_9(self):
        self.ui_main.tabWidget.setCurrentIndex(8)

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
        self.ui_login.label_19.setVisible(False)
        self.reset_code = self.model.send_reset_password(self.email)
        if self.email != self.dao.find_by_email(self.email).get_email():
            self.ui_login.label_20.setText("Email not found")
            self.ui_login.label_20.setVisible(True)

        else:
            self.ui_login.lineEdit_17.setEnabled(False)
            self.ui_login.label_19.setText("Code is sent to your email")
            self.ui_login.label_19.setVisible(True)
            self.ui_login.lineEdit_18.setVisible(True)


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


#





