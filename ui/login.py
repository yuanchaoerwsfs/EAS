# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem2, 2, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 700 15pt \"Microsoft YaHei UI\";\n"
                                 "font: 60pt \"黑体\";\n"
                                 "color: rgb(0, 170, 127);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-radius:15px;\n"
                                    "padding:5px;")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("border-radius:15px;\n"
                                      "padding:5px;")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(100)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setAutoExclusive(True)
        self.checkBox.setTristate(False)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_2.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(Form)
        self.checkBox_2.setAutoExclusive(True)
        self.checkBox_2.setTristate(False)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_2.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(Form)
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setAutoExclusive(True)
        self.checkBox_3.setTristate(False)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout_2.addWidget(self.checkBox_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(100)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    background-color:rgb(0, 170, 127);\n"
                                      "    border-radius:15px;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "    background-color: rgb(0, 227, 166);\n"
                                      "}\n"
                                      "QPushButton:pressed{\n"
                                      "    \n"
                                      "    background-color: rgb(0, 130, 95);\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    background-color:rgb(206, 206, 206);\n"
                                        "    border-radius:15px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "    background-color: rgb(229, 229, 229);\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "    \n"
                                        "    background-color: rgb(127, 127, 127);\n"
                                        "}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 2, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.login)
        self.pushButton_2.clicked.connect(Form.open_register_page)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "教务管理系统"))
        self.label.setText(_translate("Form", "教务管理系统"))
        self.lineEdit.setPlaceholderText(_translate("Form", "账号"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "密码"))
        self.checkBox.setText(_translate("Form", "教师登陆"))
        self.checkBox_2.setText(_translate("Form", "学生登陆"))
        self.checkBox_3.setText(_translate("Form", "管理员登陆"))
        self.pushButton.setText(_translate("Form", "登陆"))
        self.pushButton_2.setText(_translate("Form", "注册"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)  # 创建程序对象
    ui = Ui_Form()  # 实例化
    Form = QtWidgets.QWidget(ui)  # 创建窗口对象

    ui.setupUi(Form)  # 传入form初始化

    Form.show()  # 展示窗口
    sys.exit(app.exec())
