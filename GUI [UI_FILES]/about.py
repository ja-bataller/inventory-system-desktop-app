# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\PROGRAMMING\DESKTOP-APP\Inventory_System_via_QRcode [TUP-C_UITC]\GUI [UI_FILES]\about.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_aboutWindow(object):
    def setupUi(self, aboutWindow):
        aboutWindow.setObjectName("aboutWindow")
        aboutWindow.resize(631, 863)
        aboutWindow.setMinimumSize(QtCore.QSize(631, 863))
        aboutWindow.setMaximumSize(QtCore.QSize(631, 863))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("E:\\PROGRAMMING\\DESKTOP-APP\\Inventory_System_via_QRcode [TUP-C_UITC]\\GUI [UI_FILES]\\icons/INVENTORY.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        aboutWindow.setWindowIcon(icon)
        aboutWindow.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.centralwidget = QtWidgets.QWidget(aboutWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.AboutBackPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.AboutBackPushButton.setGeometry(QtCore.QRect(10, 10, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.AboutBackPushButton.setFont(font)
        self.AboutBackPushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.AboutBackPushButton.setStyleSheet("background-color: rgb(195, 29, 57);\n"
"color: rgb(255, 255, 255);")
        self.AboutBackPushButton.setObjectName("AboutBackPushButton")
        self.AboutMainCard = QtWidgets.QLabel(self.centralwidget)
        self.AboutMainCard.setGeometry(QtCore.QRect(10, 50, 611, 801))
        self.AboutMainCard.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"border-radius: 10px;")
        self.AboutMainCard.setText("")
        self.AboutMainCard.setObjectName("AboutMainCard")
        self.AboutOnlineCVPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.AboutOnlineCVPushButton.setGeometry(QtCore.QRect(80, 630, 181, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AboutOnlineCVPushButton.sizePolicy().hasHeightForWidth())
        self.AboutOnlineCVPushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.AboutOnlineCVPushButton.setFont(font)
        self.AboutOnlineCVPushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.AboutOnlineCVPushButton.setStyleSheet("background-color: rgb(195, 29, 57);\n"
"color: rgb(255, 255, 255);")
        self.AboutOnlineCVPushButton.setObjectName("AboutOnlineCVPushButton")
        self.AboutJABBPic = QtWidgets.QLabel(self.centralwidget)
        self.AboutJABBPic.setGeometry(QtCore.QRect(60, 310, 221, 231))
        self.AboutJABBPic.setStyleSheet("image: url(:/icons/icons/Bataller.jpg);")
        self.AboutJABBPic.setText("")
        self.AboutJABBPic.setObjectName("AboutJABBPic")
        self.AboutCard1 = QtWidgets.QLabel(self.centralwidget)
        self.AboutCard1.setGeometry(QtCore.QRect(40, 290, 261, 451))
        self.AboutCard1.setStyleSheet("background-color: rgb(65, 65, 65);\n"
"border-radius: 10px;")
        self.AboutCard1.setText("")
        self.AboutCard1.setObjectName("AboutCard1")
        self.AboutJABBName = QtWidgets.QLabel(self.centralwidget)
        self.AboutJABBName.setGeometry(QtCore.QRect(70, 550, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.AboutJABBName.setFont(font)
        self.AboutJABBName.setStyleSheet("background-color: rgb(65, 65, 65);\n"
"color: rgb(255, 255, 255);")
        self.AboutJABBName.setObjectName("AboutJABBName")
        self.AboutCourseLbl1 = QtWidgets.QLabel(self.centralwidget)
        self.AboutCourseLbl1.setGeometry(QtCore.QRect(110, 580, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.AboutCourseLbl1.setFont(font)
        self.AboutCourseLbl1.setStyleSheet("background-color: rgb(65, 65, 65);\n"
"color: rgb(255, 255, 255);")
        self.AboutCourseLbl1.setObjectName("AboutCourseLbl1")
        self.AboutGithubPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.AboutGithubPushButton.setGeometry(QtCore.QRect(80, 680, 181, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AboutGithubPushButton.sizePolicy().hasHeightForWidth())
        self.AboutGithubPushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.AboutGithubPushButton.setFont(font)
        self.AboutGithubPushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.AboutGithubPushButton.setStyleSheet("background-color: rgb(109, 109, 109);\n"
"color: rgb(255, 255, 255);")
        self.AboutGithubPushButton.setObjectName("AboutGithubPushButton")
        self.AboutCourseLbl2 = QtWidgets.QLabel(self.centralwidget)
        self.AboutCourseLbl2.setGeometry(QtCore.QRect(400, 580, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.AboutCourseLbl2.setFont(font)
        self.AboutCourseLbl2.setStyleSheet("background-color: rgb(65, 65, 65);\n"
"color: rgb(255, 255, 255);")
        self.AboutCourseLbl2.setObjectName("AboutCourseLbl2")
        self.AboutCard2 = QtWidgets.QLabel(self.centralwidget)
        self.AboutCard2.setGeometry(QtCore.QRect(330, 290, 261, 451))
        self.AboutCard2.setStyleSheet("background-color: rgb(65, 65, 65);\n"
"border-radius: 10px;")
        self.AboutCard2.setText("")
        self.AboutCard2.setObjectName("AboutCard2")
        self.AboutNJSName = QtWidgets.QLabel(self.centralwidget)
        self.AboutNJSName.setGeometry(QtCore.QRect(350, 550, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.AboutNJSName.setFont(font)
        self.AboutNJSName.setStyleSheet("background-color: rgb(65, 65, 65);\n"
"color: rgb(255, 255, 255);")
        self.AboutNJSName.setObjectName("AboutNJSName")
        self.AboutProgrammersDevelopersLbl = QtWidgets.QLabel(self.centralwidget)
        self.AboutProgrammersDevelopersLbl.setGeometry(QtCore.QRect(40, 210, 551, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.AboutProgrammersDevelopersLbl.setFont(font)
        self.AboutProgrammersDevelopersLbl.setStyleSheet("background-color: rgb(65, 65, 65);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.AboutProgrammersDevelopersLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.AboutProgrammersDevelopersLbl.setObjectName("AboutProgrammersDevelopersLbl")
        self.AccountSettingsBGLbl_5 = QtWidgets.QLabel(self.centralwidget)
        self.AccountSettingsBGLbl_5.setGeometry(QtCore.QRect(200, 70, 391, 121))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.AccountSettingsBGLbl_5.setFont(font)
        self.AccountSettingsBGLbl_5.setStyleSheet("background-color: rgb(65, 65, 65);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.AccountSettingsBGLbl_5.setText("")
        self.AccountSettingsBGLbl_5.setAlignment(QtCore.Qt.AlignCenter)
        self.AccountSettingsBGLbl_5.setObjectName("AccountSettingsBGLbl_5")
        self.AboutDescriptionLbl = QtWidgets.QLabel(self.centralwidget)
        self.AboutDescriptionLbl.setGeometry(QtCore.QRect(200, 120, 391, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.AboutDescriptionLbl.setFont(font)
        self.AboutDescriptionLbl.setStyleSheet("background-color: rgb(65, 65, 65);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.AboutDescriptionLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.AboutDescriptionLbl.setObjectName("AboutDescriptionLbl")
        self.AccountSettingsBGLbl_7 = QtWidgets.QLabel(self.centralwidget)
        self.AccountSettingsBGLbl_7.setGeometry(QtCore.QRect(200, 80, 331, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.AccountSettingsBGLbl_7.setFont(font)
        self.AccountSettingsBGLbl_7.setStyleSheet("background-color: rgb(65, 65, 65);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.AccountSettingsBGLbl_7.setAlignment(QtCore.Qt.AlignCenter)
        self.AccountSettingsBGLbl_7.setObjectName("AccountSettingsBGLbl_7")
        self.AboutSystemIconLbl = QtWidgets.QLabel(self.centralwidget)
        self.AboutSystemIconLbl.setGeometry(QtCore.QRect(40, 70, 141, 121))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.AboutSystemIconLbl.setFont(font)
        self.AboutSystemIconLbl.setStyleSheet("background-color: rgb(65, 65, 65);\n"
"image: url(:/icons/icons/INVENTORY.png);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.AboutSystemIconLbl.setText("")
        self.AboutSystemIconLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.AboutSystemIconLbl.setObjectName("AboutSystemIconLbl")
        self.AboutPycharmLogo = QtWidgets.QLabel(self.centralwidget)
        self.AboutPycharmLogo.setGeometry(QtCore.QRect(260, 770, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.AboutPycharmLogo.setFont(font)
        self.AboutPycharmLogo.setStyleSheet("background-color: rgb(65, 65, 65);\n"
"image: url(:/icons/icons/pycharm.png);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.AboutPycharmLogo.setText("")
        self.AboutPycharmLogo.setAlignment(QtCore.Qt.AlignCenter)
        self.AboutPycharmLogo.setObjectName("AboutPycharmLogo")
        self.AboutQtLogo = QtWidgets.QLabel(self.centralwidget)
        self.AboutQtLogo.setGeometry(QtCore.QRect(320, 770, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.AboutQtLogo.setFont(font)
        self.AboutQtLogo.setStyleSheet("background-color: rgb(65, 65, 65);\n"
"image: url(:/icons/icons/qt.png);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.AboutQtLogo.setText("")
        self.AboutQtLogo.setAlignment(QtCore.Qt.AlignCenter)
        self.AboutQtLogo.setObjectName("AboutQtLogo")
        self.AboutPythonLogo = QtWidgets.QLabel(self.centralwidget)
        self.AboutPythonLogo.setGeometry(QtCore.QRect(380, 770, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.AboutPythonLogo.setFont(font)
        self.AboutPythonLogo.setStyleSheet("background-color: rgb(65, 65, 65);\n"
"image: url(:/icons/icons/python.png);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.AboutPythonLogo.setText("")
        self.AboutPythonLogo.setAlignment(QtCore.Qt.AlignCenter)
        self.AboutPythonLogo.setObjectName("AboutPythonLogo")
        self.AboutMySQLLogo = QtWidgets.QLabel(self.centralwidget)
        self.AboutMySQLLogo.setGeometry(QtCore.QRect(440, 770, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.AboutMySQLLogo.setFont(font)
        self.AboutMySQLLogo.setStyleSheet("background-color: rgb(65, 65, 65);\n"
"image: url(:/icons/icons/mysql.png);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.AboutMySQLLogo.setText("")
        self.AboutMySQLLogo.setAlignment(QtCore.Qt.AlignCenter)
        self.AboutMySQLLogo.setObjectName("AboutMySQLLogo")
        self.AboutToolsTechLbl = QtWidgets.QLabel(self.centralwidget)
        self.AboutToolsTechLbl.setGeometry(QtCore.QRect(110, 780, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.AboutToolsTechLbl.setFont(font)
        self.AboutToolsTechLbl.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.AboutToolsTechLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.AboutToolsTechLbl.setObjectName("AboutToolsTechLbl")
        self.AboutNJMSPic = QtWidgets.QLabel(self.centralwidget)
        self.AboutNJMSPic.setGeometry(QtCore.QRect(350, 310, 221, 231))
        self.AboutNJMSPic.setStyleSheet("image: url(:/icons/icons/Salvador.jpg);\n"
"background-color: rgb(255, 255, 255);")
        self.AboutNJMSPic.setText("")
        self.AboutNJMSPic.setObjectName("AboutNJMSPic")
        self.AboutMainCard.raise_()
        self.AboutCard2.raise_()
        self.AboutBackPushButton.raise_()
        self.AboutCard1.raise_()
        self.AboutJABBPic.raise_()
        self.AboutCourseLbl1.raise_()
        self.AboutJABBName.raise_()
        self.AboutOnlineCVPushButton.raise_()
        self.AboutGithubPushButton.raise_()
        self.AboutCourseLbl2.raise_()
        self.AboutNJSName.raise_()
        self.AboutProgrammersDevelopersLbl.raise_()
        self.AccountSettingsBGLbl_5.raise_()
        self.AccountSettingsBGLbl_7.raise_()
        self.AboutDescriptionLbl.raise_()
        self.AboutSystemIconLbl.raise_()
        self.AboutPycharmLogo.raise_()
        self.AboutQtLogo.raise_()
        self.AboutPythonLogo.raise_()
        self.AboutMySQLLogo.raise_()
        self.AboutToolsTechLbl.raise_()
        self.AboutNJMSPic.raise_()
        aboutWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(aboutWindow)
        QtCore.QMetaObject.connectSlotsByName(aboutWindow)

    def retranslateUi(self, aboutWindow):
        _translate = QtCore.QCoreApplication.translate
        aboutWindow.setWindowTitle(_translate("aboutWindow", "TUP-C UITC INVENTORY SYSTEM"))
        self.AboutBackPushButton.setText(_translate("aboutWindow", "BACK"))
        self.AboutOnlineCVPushButton.setText(_translate("aboutWindow", "ONLINE CV"))
        self.AboutJABBName.setText(_translate("aboutWindow", "Bataller, John Anthony B."))
        self.AboutCourseLbl1.setText(_translate("aboutWindow", "BET-COET STUDENT"))
        self.AboutGithubPushButton.setText(_translate("aboutWindow", "GITHUB"))
        self.AboutCourseLbl2.setText(_translate("aboutWindow", "BET-COET STUDENT"))
        self.AboutNJSName.setText(_translate("aboutWindow", "Salvador, Nigelle Jarred M."))
        self.AboutProgrammersDevelopersLbl.setText(_translate("aboutWindow", "PROGRAMMERS & DEVELOPERS"))
        self.AboutDescriptionLbl.setText(_translate("aboutWindow", "which can help track the equipments of the UITC."))
        self.AccountSettingsBGLbl_7.setText(_translate("aboutWindow", "This Inventory System is for TUP-C UITC,"))
        self.AboutToolsTechLbl.setText(_translate("aboutWindow", "Tools & Technology used:"))
import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    aboutWindow = QtWidgets.QMainWindow()
    ui = Ui_aboutWindow()
    ui.setupUi(aboutWindow)
    aboutWindow.show()
    sys.exit(app.exec_())
