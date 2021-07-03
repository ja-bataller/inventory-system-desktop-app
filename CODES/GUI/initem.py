# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\PROGRAMMING\DESKTOP-APP\Inventory_System_via_QRcode [TUP-C_UITC]\GUI [UI_FILES]\initem.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_initemWindow(object):
    def setupUi(self, initemWindow):
        initemWindow.setObjectName("initemWindow")
        initemWindow.resize(439, 630)
        initemWindow.setMinimumSize(QtCore.QSize(439, 630))
        initemWindow.setMaximumSize(QtCore.QSize(439, 630))
        initemWindow.setGeometry(750, 200, 439, 439)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("E:\\PROGRAMMING\\DESKTOP-APP\\Inventory_System_via_QRcode [TUP-C_UITC]\\GUI [UI_FILES]\\icons/INVENTORY.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        initemWindow.setWindowIcon(icon)
        initemWindow.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.centralwidget = QtWidgets.QWidget(initemWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelInLogo = QtWidgets.QLabel(self.centralwidget)
        self.labelInLogo.setGeometry(QtCore.QRect(170, 90, 111, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelInLogo.sizePolicy().hasHeightForWidth())
        self.labelInLogo.setSizePolicy(sizePolicy)
        self.labelInLogo.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"image: url(:/icons/icons/in.png);")
        self.labelInLogo.setText("")
        self.labelInLogo.setObjectName("labelInLogo")
        self.pushButtonInSubmit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonInSubmit.setGeometry(QtCore.QRect(80, 480, 290, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonInSubmit.sizePolicy().hasHeightForWidth())
        self.pushButtonInSubmit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.pushButtonInSubmit.setFont(font)
        self.pushButtonInSubmit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonInSubmit.setStyleSheet("background-color: rgb(195, 29, 57);\n"
"color: rgb(255, 255, 255);")
        self.pushButtonInSubmit.setObjectName("pushButtonInSubmit")
        self.lineEditInIteminfo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditInIteminfo.setGeometry(QtCore.QRect(80, 410, 290, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditInIteminfo.sizePolicy().hasHeightForWidth())
        self.lineEditInIteminfo.setSizePolicy(sizePolicy)
        self.lineEditInIteminfo.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-radius: 14px;\n"
"background-color: rgb(65, 65, 65);")
        self.lineEditInIteminfo.setMaxLength(64)
        self.lineEditInIteminfo.setReadOnly(False)
        self.lineEditInIteminfo.setPlaceholderText("")
        self.lineEditInIteminfo.setObjectName("lineEditInIteminfo")
        self.labelInTitle = QtWidgets.QLabel(self.centralwidget)
        self.labelInTitle.setGeometry(QtCore.QRect(170, 220, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.labelInTitle.setFont(font)
        self.labelInTitle.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")
        self.labelInTitle.setObjectName("labelInTitle")
        self.labelInExistingborrowerinfo = QtWidgets.QLabel(self.centralwidget)
        self.labelInExistingborrowerinfo.setGeometry(QtCore.QRect(80, 290, 151, 16))
        self.labelInExistingborrowerinfo.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")
        self.labelInExistingborrowerinfo.setObjectName("labelInExistingborrowerinfo")
        self.pushButtonInBack = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonInBack.setGeometry(QtCore.QRect(30, 20, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonInBack.setFont(font)
        self.pushButtonInBack.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonInBack.setStyleSheet("background-color: rgb(195, 29, 57);\n"
"color: rgb(255, 255, 255);")
        self.pushButtonInBack.setObjectName("pushButtonInBack")
        self.labelInCard = QtWidgets.QLabel(self.centralwidget)
        self.labelInCard.setGeometry(QtCore.QRect(20, 60, 400, 550))
        self.labelInCard.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"border-radius: 14px;")
        self.labelInCard.setText("")
        self.labelInCard.setObjectName("labelInCard")
        self.comboInOutExistingborrowersinfo = QtWidgets.QComboBox(self.centralwidget)
        self.comboInOutExistingborrowersinfo.setEnabled(True)
        self.comboInOutExistingborrowersinfo.setGeometry(QtCore.QRect(80, 310, 290, 40))
        self.comboInOutExistingborrowersinfo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboInOutExistingborrowersinfo.setStyleSheet("border-radius: 14px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(65, 65, 65);")
        self.comboInOutExistingborrowersinfo.setEditable(False)
        self.comboInOutExistingborrowersinfo.setObjectName("comboInOutExistingborrowersinfo")
        self.comboInOutExistingborrowersinfo.addItem("")
        self.labelInIteminfo = QtWidgets.QLabel(self.centralwidget)
        self.labelInIteminfo.setGeometry(QtCore.QRect(80, 390, 81, 16))
        self.labelInIteminfo.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")
        self.labelInIteminfo.setObjectName("labelInIteminfo")
        self.labelInCard.raise_()
        self.labelInLogo.raise_()
        self.pushButtonInSubmit.raise_()
        self.lineEditInIteminfo.raise_()
        self.labelInTitle.raise_()
        self.labelInExistingborrowerinfo.raise_()
        self.pushButtonInBack.raise_()
        self.comboInOutExistingborrowersinfo.raise_()
        self.labelInIteminfo.raise_()
        initemWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(initemWindow)
        QtCore.QMetaObject.connectSlotsByName(initemWindow)

    def retranslateUi(self, initemWindow):
        _translate = QtCore.QCoreApplication.translate
        initemWindow.setWindowTitle(_translate("initemWindow", "TUP-C UITC INVENTORY SYSTEM"))
        self.pushButtonInSubmit.setText(_translate("initemWindow", "SUBMIT"))
        self.labelInTitle.setText(_translate("initemWindow", "IN ITEM"))
        self.labelInExistingborrowerinfo.setText(_translate("initemWindow", "Existing Borrowers Information"))
        self.pushButtonInBack.setText(_translate("initemWindow", "BACK"))
        self.comboInOutExistingborrowersinfo.setCurrentText(_translate("initemWindow", "Click here to show existing Borrowers Infromation"))
        self.comboInOutExistingborrowersinfo.setItemText(0, _translate("initemWindow", "Click here to show existing Borrowers Infromation"))
        self.labelInIteminfo.setText(_translate("initemWindow", "Item Information"))
import icons


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    initemWindow = QtWidgets.QMainWindow()
    ui = Ui_initemWindow()
    ui.setupUi(initemWindow)
    initemWindow.show()
    sys.exit(app.exec_())
