# coding: utf-8
# @Author:Sunqw

import sys
from PyQt6.QtWidgets import QWidget, QApplication
from ui.login import Ui_Form as LoginUiMimin


class LoginWindow(LoginUiMimin, QWidget):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)
        # super().__init__()  可简
        # self.ui = ui

    def login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        print(username, password)

    def open_register_page(self):
        pass


def run():
    app = QApplication(sys.argv)  # 创建程序对象
    login_window = LoginWindow()  # 创建窗口对象

    # login_window.setupUi(login_window)  # 传入form初始化

    login_window.show()  # 展示窗口
    sys.exit(app.exec())
