# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\PROGRAMMING\DESKTOP-APP\Inventory_System_via_QRcode [TUP-C_UITC]\GUI [UI_FILES]\signup.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_signupWindow(object):
    def setupUi(self, signupWindow):
        signupWindow.setObjectName("signupWindow")
        signupWindow.resize(652, 1000)
        signupWindow.setMinimumSize(QtCore.QSize(652, 1000))
        signupWindow.setMaximumSize(QtCore.QSize(652, 1000))
        signupWindow.setGeometry(630, 50, 652, 1000)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("E:\\PROGRAMMING\\DESKTOP-APP\\Inventory_System_via_QRcode [TUP-C_UITC]\\GUI [UI_FILES]\\icons/INVENTORY.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        signupWindow.setWindowIcon(icon)
        signupWindow.setToolTip("")
        signupWindow.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.centralwidget = QtWidgets.QWidget(signupWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEditSignupPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSignupPassword.setGeometry(QtCore.QRect(110, 520, 430, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.lineEditSignupPassword.setFont(font)
        self.lineEditSignupPassword.setStyleSheet("border-radius: 14px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(65, 65, 65);")
        self.lineEditSignupPassword.setMaxLength(45)
        self.lineEditSignupPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditSignupPassword.setPlaceholderText("")
        self.lineEditSignupPassword.setObjectName("lineEditSignupPassword")
        self.pushButtonSignupLogin = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSignupLogin.setGeometry(QtCore.QRect(370, 930, 80, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        self.pushButtonSignupLogin.setFont(font)
        self.pushButtonSignupLogin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonSignupLogin.setStyleSheet("background-color: rgb(195, 29, 57);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButtonSignupLogin.setObjectName("pushButtonSignupLogin")
        self.labelSignupTitle = QtWidgets.QLabel(self.centralwidget)
        self.labelSignupTitle.setGeometry(QtCore.QRect(180, 120, 321, 81))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(24)
        self.labelSignupTitle.setFont(font)
        self.labelSignupTitle.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(48, 48, 48);")
        self.labelSignupTitle.setObjectName("labelSignupTitle")
        self.lineEditSignupFirstname = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSignupFirstname.setGeometry(QtCore.QRect(110, 220, 430, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.lineEditSignupFirstname.setFont(font)
        self.lineEditSignupFirstname.setStyleSheet("border-radius: 14px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(65, 65, 65);")
        self.lineEditSignupFirstname.setMaxLength(45)
        self.lineEditSignupFirstname.setPlaceholderText("")
        self.lineEditSignupFirstname.setObjectName("lineEditSignupFirstname")
        self.labelSignupLogo = QtWidgets.QLabel(self.centralwidget)
        self.labelSignupLogo.setGeometry(QtCore.QRect(300, 40, 80, 80))
        self.labelSignupLogo.setMouseTracking(False)
        self.labelSignupLogo.setToolTip("")
        self.labelSignupLogo.setToolTipDuration(-1)
        self.labelSignupLogo.setWhatsThis("")
        self.labelSignupLogo.setStyleSheet("image: url(:/icons/icons/newuser.png);\n"
"background-color: rgb(48, 48, 48);")
        self.labelSignupLogo.setText("")
        self.labelSignupLogo.setObjectName("labelSignupLogo")
        self.labelSignupPassword = QtWidgets.QLabel(self.centralwidget)
        self.labelSignupPassword.setGeometry(QtCore.QRect(120, 490, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.labelSignupPassword.setFont(font)
        self.labelSignupPassword.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(48, 48, 48);")
        self.labelSignupPassword.setObjectName("labelSignupPassword")
        self.labelSignupAlreadyacc = QtWidgets.QLabel(self.centralwidget)
        self.labelSignupAlreadyacc.setGeometry(QtCore.QRect(180, 930, 181, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.labelSignupAlreadyacc.setFont(font)
        self.labelSignupAlreadyacc.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(48, 48, 48);")
        self.labelSignupAlreadyacc.setObjectName("labelSignupAlreadyacc")
        self.labelLoginCard = QtWidgets.QLabel(self.centralwidget)
        self.labelLoginCard.setEnabled(True)
        self.labelLoginCard.setGeometry(QtCore.QRect(25, 20, 600, 950))
        self.labelLoginCard.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"border-radius: 14px;")
        self.labelLoginCard.setText("")
        self.labelLoginCard.setObjectName("labelLoginCard")
        self.pushButtonSignup = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSignup.setGeometry(QtCore.QRect(230, 860, 190, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(20)
        self.pushButtonSignup.setFont(font)
        self.pushButtonSignup.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonSignup.setStyleSheet("background-color: rgb(195, 29, 57);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButtonSignup.setObjectName("pushButtonSignup")
        self.labelSignupFirstname = QtWidgets.QLabel(self.centralwidget)
        self.labelSignupFirstname.setGeometry(QtCore.QRect(120, 190, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.labelSignupFirstname.setFont(font)
        self.labelSignupFirstname.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(48, 48, 48);")
        self.labelSignupFirstname.setObjectName("labelSignupFirstname")
        self.lineEditSignupLastname = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSignupLastname.setGeometry(QtCore.QRect(110, 320, 430, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.lineEditSignupLastname.setFont(font)
        self.lineEditSignupLastname.setStyleSheet("border-radius: 14px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(65, 65, 65);")
        self.lineEditSignupLastname.setMaxLength(45)
        self.lineEditSignupLastname.setPlaceholderText("")
        self.lineEditSignupLastname.setObjectName("lineEditSignupLastname")
        self.labelSignupLastname = QtWidgets.QLabel(self.centralwidget)
        self.labelSignupLastname.setGeometry(QtCore.QRect(120, 290, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.labelSignupLastname.setFont(font)
        self.labelSignupLastname.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(48, 48, 48);")
        self.labelSignupLastname.setObjectName("labelSignupLastname")
        self.labelSignupUsername = QtWidgets.QLabel(self.centralwidget)
        self.labelSignupUsername.setGeometry(QtCore.QRect(120, 390, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.labelSignupUsername.setFont(font)
        self.labelSignupUsername.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(48, 48, 48);")
        self.labelSignupUsername.setObjectName("labelSignupUsername")
        self.lineEditSignupUsername = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSignupUsername.setGeometry(QtCore.QRect(110, 420, 430, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.lineEditSignupUsername.setFont(font)
        self.lineEditSignupUsername.setStyleSheet("border-radius: 14px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(65, 65, 65);")
        self.lineEditSignupUsername.setMaxLength(45)
        self.lineEditSignupUsername.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEditSignupUsername.setPlaceholderText("")
        self.lineEditSignupUsername.setObjectName("lineEditSignupUsername")
        self.groupBoxSignupAccounttype = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxSignupAccounttype.setGeometry(QtCore.QRect(110, 690, 430, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.groupBoxSignupAccounttype.setFont(font)
        self.groupBoxSignupAccounttype.setToolTip("")
        self.groupBoxSignupAccounttype.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(65, 65, 65);")
        self.groupBoxSignupAccounttype.setObjectName("groupBoxSignupAccounttype")
        self.radioButtonSignupAdministrator = QtWidgets.QRadioButton(self.groupBoxSignupAccounttype)
        self.radioButtonSignupAdministrator.setGeometry(QtCore.QRect(80, 20, 111, 17))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.radioButtonSignupAdministrator.setFont(font)
        self.radioButtonSignupAdministrator.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButtonSignupAdministrator.setObjectName("radioButtonSignupAdministrator")
        self.radioButtonSignupOperator = QtWidgets.QRadioButton(self.groupBoxSignupAccounttype)
        self.radioButtonSignupOperator.setGeometry(QtCore.QRect(250, 20, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.radioButtonSignupOperator.setFont(font)
        self.radioButtonSignupOperator.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButtonSignupOperator.setObjectName("radioButtonSignupOperator")
        self.labelSignupRetypePassword = QtWidgets.QLabel(self.centralwidget)
        self.labelSignupRetypePassword.setGeometry(QtCore.QRect(120, 590, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.labelSignupRetypePassword.setFont(font)
        self.labelSignupRetypePassword.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(48, 48, 48);")
        self.labelSignupRetypePassword.setObjectName("labelSignupRetypePassword")
        self.lineEditSignupRetypePassword = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSignupRetypePassword.setGeometry(QtCore.QRect(110, 620, 430, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.lineEditSignupRetypePassword.setFont(font)
        self.lineEditSignupRetypePassword.setStyleSheet("border-radius: 14px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(65, 65, 65);")
        self.lineEditSignupRetypePassword.setMaxLength(45)
        self.lineEditSignupRetypePassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditSignupRetypePassword.setPlaceholderText("")
        self.lineEditSignupRetypePassword.setObjectName("lineEditSignupRetypePassword")
        self.labelSignupCode = QtWidgets.QLabel(self.centralwidget)
        self.labelSignupCode.setGeometry(QtCore.QRect(110, 760, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.labelSignupCode.setFont(font)
        self.labelSignupCode.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(48, 48, 48);")
        self.labelSignupCode.setObjectName("labelSignupCode")
        self.lineEditSignupCode = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSignupCode.setGeometry(QtCore.QRect(109, 790, 431, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.lineEditSignupCode.setFont(font)
        self.lineEditSignupCode.setWhatsThis("")
        self.lineEditSignupCode.setStyleSheet("border-radius: 14px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(65, 65, 65);")
        self.lineEditSignupCode.setMaxLength(6)
        self.lineEditSignupCode.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditSignupCode.setPlaceholderText("")
        self.lineEditSignupCode.setObjectName("lineEditSignupCode")
        self.labelLoginCard.raise_()
        self.labelSignupTitle.raise_()
        self.pushButtonSignupLogin.raise_()
        self.lineEditSignupFirstname.raise_()
        self.labelSignupLogo.raise_()
        self.labelSignupAlreadyacc.raise_()
        self.pushButtonSignup.raise_()
        self.labelSignupFirstname.raise_()
        self.lineEditSignupLastname.raise_()
        self.labelSignupLastname.raise_()
        self.labelSignupUsername.raise_()
        self.lineEditSignupUsername.raise_()
        self.groupBoxSignupAccounttype.raise_()
        self.labelSignupPassword.raise_()
        self.lineEditSignupPassword.raise_()
        self.labelSignupRetypePassword.raise_()
        self.lineEditSignupRetypePassword.raise_()
        self.labelSignupCode.raise_()
        self.lineEditSignupCode.raise_()
        signupWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(signupWindow)
        QtCore.QMetaObject.connectSlotsByName(signupWindow)
        signupWindow.setTabOrder(self.lineEditSignupFirstname, self.lineEditSignupLastname)
        signupWindow.setTabOrder(self.lineEditSignupLastname, self.lineEditSignupUsername)
        signupWindow.setTabOrder(self.lineEditSignupUsername, self.lineEditSignupPassword)
        signupWindow.setTabOrder(self.lineEditSignupPassword, self.lineEditSignupRetypePassword)
        signupWindow.setTabOrder(self.lineEditSignupRetypePassword, self.radioButtonSignupAdministrator)
        signupWindow.setTabOrder(self.radioButtonSignupAdministrator, self.radioButtonSignupOperator)
        signupWindow.setTabOrder(self.radioButtonSignupOperator, self.lineEditSignupCode)
        signupWindow.setTabOrder(self.lineEditSignupCode, self.pushButtonSignup)
        signupWindow.setTabOrder(self.pushButtonSignup, self.pushButtonSignupLogin)

    def retranslateUi(self, signupWindow):
        _translate = QtCore.QCoreApplication.translate
        signupWindow.setWindowTitle(_translate("signupWindow", "Sign Up - TUP-C UITC INVENTORY SYSTEM"))
        self.pushButtonSignupLogin.setText(_translate("signupWindow", "LOG IN"))
        self.labelSignupTitle.setText(_translate("signupWindow", "<html><head/><body><p align=\"center\">SIGN UP</p></body></html>"))
        self.labelSignupPassword.setText(_translate("signupWindow", "<html><head/><body><p>Password</p></body></html>"))
        self.labelSignupAlreadyacc.setText(_translate("signupWindow", "<html><head/><body><p>Already have an account?</p></body></html>"))
        self.pushButtonSignup.setText(_translate("signupWindow", "SIGN UP"))
        self.labelSignupFirstname.setText(_translate("signupWindow", "<html><head/><body><p>First Name</p></body></html>"))
        self.labelSignupLastname.setText(_translate("signupWindow", "<html><head/><body><p>Last Name</p></body></html>"))
        self.labelSignupUsername.setText(_translate("signupWindow", "<html><head/><body><p>Username</p></body></html>"))
        self.groupBoxSignupAccounttype.setTitle(_translate("signupWindow", "Account Type"))
        self.radioButtonSignupAdministrator.setText(_translate("signupWindow", "Administrator"))
        self.radioButtonSignupOperator.setText(_translate("signupWindow", "Operator"))
        self.labelSignupRetypePassword.setText(_translate("signupWindow", "<html><head/><body><p>Re-type Password</p></body></html>"))
        self.labelSignupCode.setText(_translate("signupWindow", "<html><head/><body><p align=\"center\">SIGN UP CODE</p></body></html>"))
        self.lineEditSignupCode.setToolTip(_translate("signupWindow", "Type here the Signup Code (ask Administrator)"))
import icons


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    signupWindow = QtWidgets.QMainWindow()
    ui = Ui_signupWindow()
    ui.setupUi(signupWindow)
    signupWindow.show()
    sys.exit(app.exec_())
