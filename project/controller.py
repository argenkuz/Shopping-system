from PyQt6.QtWidgets import QMainWindow
from PyQt6 import QtWidgets
from project.qt import Ui_MainWindow
from project.login import Ui_LoginWindow


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main_window = None
        self.login_window = None
        self.ui_main = Ui_MainWindow()
        self.ui_login = Ui_LoginWindow()
        self.users = {}


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
        #self.ui_login.pushButton_6.clicked.connect(self.create_account)
        self.ui_login.pushButton_8.clicked.connect(self.on_cancel_create_account_clicked)
        self.ui_login.pushButton_9.clicked.connect(self.on_cancel_create_account_clicked)
        self.ui_login.pushButton_10.clicked.connect(self.login_account)
        self.ui_login.pushButton_12.clicked.connect(self.on_cancel_clicked)
        self.ui_login.pushButton_13.clicked.connect(self.on_cancel_create_account_clicked)
        self.ui_login.pushButton_14.clicked.connect(self.switch_to_tab_condition_of_use)
        self.ui_login.pushButton_15.clicked.connect(self.switch_to_tab_usage_policy)
        self.ui_login.pushButton_16.clicked.connect(self.on_cancel_create_account_clicked)
        #self.ui_login.pushButton_5.clicked.connect(self.forgot_password_clicked)
        self.ui_login.label_10.setVisible(False)
        self.ui_login.label_13.setVisible(False)
        self.ui_login.label_14.setVisible(False)
        self.ui_login.label_15.setVisible(False)
        self.ui_login.label_16.setVisible(False)
        self.ui_login.label_17.setVisible(False)
        self.ui_login.label_12.setVisible(False)
        self.ui_login.lineEdit_11.

    def switch_to_tab_login(self):
        self.ui_login.tabWidget.setCurrentIndex(1)

    def switch_to_tab_create_account(self):
        self.ui_login.tabWidget.setCurrentIndex(2)


    def on_cancel_create_account_clicked(self):
        self.ui_login.tabWidget.setCurrentIndex(0)

    def login_account(self):
        username = self.ui_login.lineEdit_15.text().strip()
        password = self.ui_login.lineEdit_16.text().strip()

        result = self.validate_login(username, password)

        if result["success"]:
            self.ui_login.label_10.setText("Login successful!")

        else:
            self.ui_login.label_10.setText(result["error"])


        self.ui_login.label_10.setVisible(True)

    def validate_login(self, username, password):
        user = self.users.get(username)
        if not user:
            return {"success": False, "error": "User does not exist"}
        if user["password"] != password:
            return {"success": False, "error": "Incorrect password"}
        return {"success": True, "message": "Login successful"}

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

    def on_login_clicked(self):
        self.model.on_login_clicked()

    def on_cancel_clicked(self):
        self.login_window.close()


