# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\PROGRAMMING\DESKTOP-APP\Inventory_System_via_QRcode [TUP-C_UITC]\GUI [UI_FILES]\login.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_loginWIndow(object):
    def setupUi(self, loginWIndow):
        loginWIndow.setObjectName("loginWIndow")
        loginWIndow.setWindowModality(QtCore.Qt.NonModal)
        loginWIndow.setEnabled(True)
        loginWIndow.resize(630, 561)
        loginWIndow.setMinimumSize(QtCore.QSize(630, 561))
        loginWIndow.setMaximumSize(QtCore.QSize(630, 561))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("E:\\PROGRAMMING\\DESKTOP-APP\\Inventory_System_via_QRcode [TUP-C_UITC]\\GUI [UI_FILES]\\icons/INVENTORY.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        loginWIndow.setWindowIcon(icon)
        loginWIndow.setStyleSheet("background-color: rgb(223, 223, 223);")
        loginWIndow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(loginWIndow)
        self.centralwidget.setObjectName("centralwidget")
        self.loginCard = QtWidgets.QLabel(self.centralwidget)
        self.loginCard.setEnabled(True)
        self.loginCard.setGeometry(QtCore.QRect(15, 20, 600, 520))
        self.loginCard.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"border-radius: 14px;")
        self.loginCard.setText("")
        self.loginCard.setObjectName("loginCard")
        self.loginTitle = QtWidgets.QLabel(self.centralwidget)
        self.loginTitle.setGeometry(QtCore.QRect(160, 150, 321, 81))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(28)
        self.loginTitle.setFont(font)
        self.loginTitle.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(48, 48, 48);")
        self.loginTitle.setObjectName("loginTitle")
        self.pushButtonLogin = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonLogin.setGeometry(QtCore.QRect(220, 420, 190, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(20)
        self.pushButtonLogin.setFont(font)
        self.pushButtonLogin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonLogin.setStyleSheet("background-color: rgb(195, 29, 57);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButtonLogin.setAutoDefault(True)
        self.pushButtonLogin.setDefault(True)
        self.pushButtonLogin.setObjectName("pushButtonLogin")
        self.lineEditLoginUsername = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditLoginUsername.setGeometry(QtCore.QRect(100, 240, 431, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.lineEditLoginUsername.setFont(font)
        self.lineEditLoginUsername.setStyleSheet("border-radius: 14px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(65, 65, 65);")
        self.lineEditLoginUsername.setMaxLength(45)
        self.lineEditLoginUsername.setPlaceholderText("")
        self.lineEditLoginUsername.setObjectName("lineEditLoginUsername")
        self.labelLoginUsername = QtWidgets.QLabel(self.centralwidget)
        self.labelLoginUsername.setGeometry(QtCore.QRect(110, 210, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.labelLoginUsername.setFont(font)
        self.labelLoginUsername.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(48, 48, 48);")
        self.labelLoginUsername.setObjectName("labelLoginUsername")
        self.labelLoginPassword = QtWidgets.QLabel(self.centralwidget)
        self.labelLoginPassword.setGeometry(QtCore.QRect(110, 310, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.labelLoginPassword.setFont(font)
        self.labelLoginPassword.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(48, 48, 48);")
        self.labelLoginPassword.setObjectName("labelLoginPassword")
        self.lineEditLoginPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditLoginPassword.setGeometry(QtCore.QRect(100, 340, 431, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.lineEditLoginPassword.setFont(font)
        self.lineEditLoginPassword.setStyleSheet("border-radius: 14px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(65, 65, 65);")
        self.lineEditLoginPassword.setMaxLength(45)
        self.lineEditLoginPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditLoginPassword.setPlaceholderText("")
        self.lineEditLoginPassword.setObjectName("lineEditLoginPassword")
        self.labelLoginNoacc = QtWidgets.QLabel(self.centralwidget)
        self.labelLoginNoacc.setGeometry(QtCore.QRect(210, 500, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.labelLoginNoacc.setFont(font)
        self.labelLoginNoacc.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(48, 48, 48);")
        self.labelLoginNoacc.setObjectName("labelLoginNoacc")
        self.pushButtonLoginSignup = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonLoginSignup.setGeometry(QtCore.QRect(330, 500, 80, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        self.pushButtonLoginSignup.setFont(font)
        self.pushButtonLoginSignup.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonLoginSignup.setStyleSheet("background-color: rgb(195, 29, 57);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButtonLoginSignup.setObjectName("pushButtonLoginSignup")
        self.loginLogo = QtWidgets.QLabel(self.centralwidget)
        self.loginLogo.setGeometry(QtCore.QRect(270, 50, 100, 100))
        self.loginLogo.setStyleSheet("image: url(:/icons/icons/user.png);\n"
"background-color: rgb(48, 48, 48);")
        self.loginLogo.setText("")
        self.loginLogo.setObjectName("loginLogo")
        loginWIndow.setCentralWidget(self.centralwidget)

        self.retranslateUi(loginWIndow)
        QtCore.QMetaObject.connectSlotsByName(loginWIndow)
        loginWIndow.setTabOrder(self.lineEditLoginUsername, self.lineEditLoginPassword)
        loginWIndow.setTabOrder(self.lineEditLoginPassword, self.pushButtonLogin)
        loginWIndow.setTabOrder(self.pushButtonLogin, self.pushButtonLoginSignup)

    def retranslateUi(self, loginWIndow):
        _translate = QtCore.QCoreApplication.translate
        loginWIndow.setWindowTitle(_translate("loginWIndow", "TUP-C UITC INVENTORY SYSTEM"))
        self.loginTitle.setText(_translate("loginWIndow", "<html><head/><body><p align=\"center\">LOG IN</p></body></html>"))
        self.pushButtonLogin.setText(_translate("loginWIndow", "LOG IN"))
        self.labelLoginUsername.setText(_translate("loginWIndow", "<html><head/><body><p><span style=\" font-size:10pt;\">Username</span></p></body></html>"))
        self.labelLoginPassword.setText(_translate("loginWIndow", "<html><head/><body><p>Password</p></body></html>"))
        self.labelLoginNoacc.setText(_translate("loginWIndow", "<html><head/><body><p>No account yet?</p></body></html>"))
        self.pushButtonLoginSignup.setText(_translate("loginWIndow", "SIGN UP"))
import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loginWIndow = QtWidgets.QMainWindow()
    ui = Ui_loginWIndow()
    ui.setupUi(loginWIndow)
    loginWIndow.show()
    sys.exit(app.exec_())
