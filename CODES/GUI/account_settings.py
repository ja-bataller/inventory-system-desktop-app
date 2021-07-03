# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\PROGRAMMING\DESKTOP-APP\Inventory_System_via_QRcode [TUP-C_UITC]\GUI [UI_FILES]\account_settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AccountSettingsWindow(object):
    def setupUi(self, AccountSettingsWindow):
        AccountSettingsWindow.setObjectName("AccountSettingsWindow")
        AccountSettingsWindow.resize(605, 629)
        AccountSettingsWindow.setMinimumSize(QtCore.QSize(605, 629))
        AccountSettingsWindow.setMaximumSize(QtCore.QSize(605, 629))
        AccountSettingsWindow.setGeometry(680, 200, 605, 629)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("E:\\PROGRAMMING\\DESKTOP-APP\\Inventory_System_via_QRcode [TUP-C_UITC]\\GUI [UI_FILES]\\icons/INVENTORY.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AccountSettingsWindow.setWindowIcon(icon)
        AccountSettingsWindow.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.centralwidget = QtWidgets.QWidget(AccountSettingsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.AccountSettingsBGLbl = QtWidgets.QLabel(self.centralwidget)
        self.AccountSettingsBGLbl.setGeometry(QtCore.QRect(20, 50, 561, 551))
        self.AccountSettingsBGLbl.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"border-radius: 10px;")
        self.AccountSettingsBGLbl.setText("")
        self.AccountSettingsBGLbl.setObjectName("AccountSettingsBGLbl")
        self.AccountSettingsLbl = QtWidgets.QLabel(self.centralwidget)
        self.AccountSettingsLbl.setGeometry(QtCore.QRect(160, 200, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.AccountSettingsLbl.setFont(font)
        self.AccountSettingsLbl.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")
        self.AccountSettingsLbl.setObjectName("AccountSettingsLbl")
        self.AccountSettingsLogoLbl = QtWidgets.QLabel(self.centralwidget)
        self.AccountSettingsLogoLbl.setGeometry(QtCore.QRect(240, 70, 111, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AccountSettingsLogoLbl.sizePolicy().hasHeightForWidth())
        self.AccountSettingsLogoLbl.setSizePolicy(sizePolicy)
        self.AccountSettingsLogoLbl.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"image: url(:/icons/icons/ACCOUNT SETTINGS.png);\n"
"")
        self.AccountSettingsLogoLbl.setText("")
        self.AccountSettingsLogoLbl.setObjectName("AccountSettingsLogoLbl")
        self.AccountSettingsOldPasswordLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.AccountSettingsOldPasswordLineEdit.setGeometry(QtCore.QRect(160, 290, 291, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AccountSettingsOldPasswordLineEdit.sizePolicy().hasHeightForWidth())
        self.AccountSettingsOldPasswordLineEdit.setSizePolicy(sizePolicy)
        self.AccountSettingsOldPasswordLineEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"background-color: rgb(65, 65, 65);")
        self.AccountSettingsOldPasswordLineEdit.setMaxLength(64)
        self.AccountSettingsOldPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.AccountSettingsOldPasswordLineEdit.setObjectName("AccountSettingsOldPasswordLineEdit")
        self.AccountSettingsChangePasswordLbl = QtWidgets.QLabel(self.centralwidget)
        self.AccountSettingsChangePasswordLbl.setGeometry(QtCore.QRect(250, 230, 91, 16))
        self.AccountSettingsChangePasswordLbl.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")
        self.AccountSettingsChangePasswordLbl.setObjectName("AccountSettingsChangePasswordLbl")
        self.AccountSettingsNewPasswordLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.AccountSettingsNewPasswordLineEdit.setGeometry(QtCore.QRect(160, 360, 291, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AccountSettingsNewPasswordLineEdit.sizePolicy().hasHeightForWidth())
        self.AccountSettingsNewPasswordLineEdit.setSizePolicy(sizePolicy)
        self.AccountSettingsNewPasswordLineEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"background-color: rgb(65, 65, 65);")
        self.AccountSettingsNewPasswordLineEdit.setMaxLength(64)
        self.AccountSettingsNewPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.AccountSettingsNewPasswordLineEdit.setObjectName("AccountSettingsNewPasswordLineEdit")
        self.AccountSettingsOldPasswordLbl = QtWidgets.QLabel(self.centralwidget)
        self.AccountSettingsOldPasswordLbl.setGeometry(QtCore.QRect(160, 270, 91, 16))
        self.AccountSettingsOldPasswordLbl.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")
        self.AccountSettingsOldPasswordLbl.setObjectName("AccountSettingsOldPasswordLbl")
        self.AccountSettingsNewPasswordLbl = QtWidgets.QLabel(self.centralwidget)
        self.AccountSettingsNewPasswordLbl.setGeometry(QtCore.QRect(160, 340, 91, 16))
        self.AccountSettingsNewPasswordLbl.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")
        self.AccountSettingsNewPasswordLbl.setObjectName("AccountSettingsNewPasswordLbl")
        self.AccountSettingsConfirmNewPasswordLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.AccountSettingsConfirmNewPasswordLineEdit.setGeometry(QtCore.QRect(160, 430, 291, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AccountSettingsConfirmNewPasswordLineEdit.sizePolicy().hasHeightForWidth())
        self.AccountSettingsConfirmNewPasswordLineEdit.setSizePolicy(sizePolicy)
        self.AccountSettingsConfirmNewPasswordLineEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"background-color: rgb(65, 65, 65);")
        self.AccountSettingsConfirmNewPasswordLineEdit.setMaxLength(64)
        self.AccountSettingsConfirmNewPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.AccountSettingsConfirmNewPasswordLineEdit.setObjectName("AccountSettingsConfirmNewPasswordLineEdit")
        self.AccountSettingsConfirmNewPasswordLbl = QtWidgets.QLabel(self.centralwidget)
        self.AccountSettingsConfirmNewPasswordLbl.setGeometry(QtCore.QRect(160, 410, 121, 16))
        self.AccountSettingsConfirmNewPasswordLbl.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")
        self.AccountSettingsConfirmNewPasswordLbl.setObjectName("AccountSettingsConfirmNewPasswordLbl")
        self.AccountSettingsChangePasswordPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.AccountSettingsChangePasswordPushButton.setGeometry(QtCore.QRect(140, 490, 331, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AccountSettingsChangePasswordPushButton.sizePolicy().hasHeightForWidth())
        self.AccountSettingsChangePasswordPushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.AccountSettingsChangePasswordPushButton.setFont(font)
        self.AccountSettingsChangePasswordPushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.AccountSettingsChangePasswordPushButton.setStyleSheet("background-color: rgb(195, 29, 57);\n"
"color: rgb(255, 255, 255);")
        self.AccountSettingsChangePasswordPushButton.setObjectName("AccountSettingsChangePasswordPushButton")
        self.AccountSettingsBackPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.AccountSettingsBackPushButton.setGeometry(QtCore.QRect(20, 10, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.AccountSettingsBackPushButton.setFont(font)
        self.AccountSettingsBackPushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.AccountSettingsBackPushButton.setStyleSheet("background-color: rgb(195, 29, 57);\n"
"color: rgb(255, 255, 255);")
        self.AccountSettingsBackPushButton.setObjectName("AccountSettingsBackPushButton")
        AccountSettingsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AccountSettingsWindow)
        QtCore.QMetaObject.connectSlotsByName(AccountSettingsWindow)

    def retranslateUi(self, AccountSettingsWindow):
        _translate = QtCore.QCoreApplication.translate
        AccountSettingsWindow.setWindowTitle(_translate("AccountSettingsWindow", "TUP-C UITC INVENTORY SYSTEM"))
        self.AccountSettingsLbl.setText(_translate("AccountSettingsWindow", "ACCOUNT SETTINGS"))
        self.AccountSettingsOldPasswordLineEdit.setPlaceholderText(_translate("AccountSettingsWindow", "  Enter Old Password here"))
        self.AccountSettingsChangePasswordLbl.setText(_translate("AccountSettingsWindow", "Change Password"))
        self.AccountSettingsNewPasswordLineEdit.setPlaceholderText(_translate("AccountSettingsWindow", "  Enter New Password here"))
        self.AccountSettingsOldPasswordLbl.setText(_translate("AccountSettingsWindow", "Old Password"))
        self.AccountSettingsNewPasswordLbl.setText(_translate("AccountSettingsWindow", "New Password"))
        self.AccountSettingsConfirmNewPasswordLineEdit.setPlaceholderText(_translate("AccountSettingsWindow", "  Re-enter New Password here"))
        self.AccountSettingsConfirmNewPasswordLbl.setText(_translate("AccountSettingsWindow", "Confirm New Password"))
        self.AccountSettingsChangePasswordPushButton.setText(_translate("AccountSettingsWindow", "Change Password"))
        self.AccountSettingsBackPushButton.setText(_translate("AccountSettingsWindow", "BACK"))
import icons


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AccountSettingsWindow = QtWidgets.QMainWindow()
    ui = Ui_AccountSettingsWindow()
    ui.setupUi(AccountSettingsWindow)
    AccountSettingsWindow.show()
    sys.exit(app.exec_())