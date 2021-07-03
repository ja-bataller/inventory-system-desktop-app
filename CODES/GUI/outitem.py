# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\PROGRAMMING\DESKTOP-APP\Inventory_System_via_QRcode [TUP-C_UITC]\GUI [UI_FILES]\outitem.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_outitemWindow(object):
    def setupUi(self, outitemWindow):
        outitemWindow.setObjectName("outitemWindow")
        outitemWindow.resize(442, 710)
        outitemWindow.setMinimumSize(QtCore.QSize(442, 710))
        outitemWindow.setMaximumSize(QtCore.QSize(442, 710))
        outitemWindow.setGeometry(750, 120, 442, 841)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("E:\\PROGRAMMING\\DESKTOP-APP\\Inventory_System_via_QRcode [TUP-C_UITC]\\GUI [UI_FILES]\\icons/INVENTORY.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        outitemWindow.setWindowIcon(icon)
        outitemWindow.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.centralwidget = QtWidgets.QWidget(outitemWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelOutTitle = QtWidgets.QLabel(self.centralwidget)
        self.labelOutTitle.setGeometry(QtCore.QRect(160, 200, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.labelOutTitle.setFont(font)
        self.labelOutTitle.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")
        self.labelOutTitle.setObjectName("labelOutTitle")
        self.labelOutCard = QtWidgets.QLabel(self.centralwidget)
        self.labelOutCard.setGeometry(QtCore.QRect(20, 50, 400, 641))
        self.labelOutCard.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"border-radius: 14px;")
        self.labelOutCard.setText("")
        self.labelOutCard.setObjectName("labelOutCard")
        self.pushButtonOutBack = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonOutBack.setGeometry(QtCore.QRect(30, 10, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonOutBack.setFont(font)
        self.pushButtonOutBack.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonOutBack.setStyleSheet("background-color: rgb(195, 29, 57);\n"
"color: rgb(255, 255, 255);")
        self.pushButtonOutBack.setObjectName("pushButtonOutBack")
        self.pushButtonOutSubmit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonOutSubmit.setEnabled(False)
        self.pushButtonOutSubmit.setGeometry(QtCore.QRect(80, 580, 290, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonOutSubmit.sizePolicy().hasHeightForWidth())
        self.pushButtonOutSubmit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.pushButtonOutSubmit.setFont(font)
        self.pushButtonOutSubmit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonOutSubmit.setStyleSheet("background-color: rgb(195, 29, 57);\n"
"color: rgb(255, 255, 255);")
        self.pushButtonOutSubmit.setObjectName("pushButtonOutSubmit")
        self.labelOutLogo = QtWidgets.QLabel(self.centralwidget)
        self.labelOutLogo.setGeometry(QtCore.QRect(170, 70, 111, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelOutLogo.sizePolicy().hasHeightForWidth())
        self.labelOutLogo.setSizePolicy(sizePolicy)
        self.labelOutLogo.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"image: url(:/icons/icons/out.png);")
        self.labelOutLogo.setText("")
        self.labelOutLogo.setObjectName("labelOutLogo")
        self.comboBoxBorrowerName = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxBorrowerName.setEnabled(False)
        self.comboBoxBorrowerName.setGeometry(QtCore.QRect(80, 440, 290, 40))
        self.comboBoxBorrowerName.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBoxBorrowerName.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.comboBoxBorrowerName.setEditable(False)
        self.comboBoxBorrowerName.setCurrentText("")
        self.comboBoxBorrowerName.setObjectName("comboBoxBorrowerName")
        self.comboBoxBorrowerName.addItem("")
        self.comboBoxBorrowerName.setItemText(0, "")
        self.labelOutExistingborrowerinfo = QtWidgets.QLabel(self.centralwidget)
        self.labelOutExistingborrowerinfo.setGeometry(QtCore.QRect(80, 420, 151, 16))
        self.labelOutExistingborrowerinfo.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")
        self.labelOutExistingborrowerinfo.setObjectName("labelOutExistingborrowerinfo")
        self.lineEditOutIteminfo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditOutIteminfo.setEnabled(False)
        self.lineEditOutIteminfo.setGeometry(QtCore.QRect(80, 520, 290, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditOutIteminfo.sizePolicy().hasHeightForWidth())
        self.lineEditOutIteminfo.setSizePolicy(sizePolicy)
        self.lineEditOutIteminfo.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(65, 65, 65);")
        self.lineEditOutIteminfo.setMaxLength(64)
        self.lineEditOutIteminfo.setReadOnly(False)
        self.lineEditOutIteminfo.setPlaceholderText("")
        self.lineEditOutIteminfo.setObjectName("lineEditOutIteminfo")
        self.labelOutIteminfo = QtWidgets.QLabel(self.centralwidget)
        self.labelOutIteminfo.setGeometry(QtCore.QRect(80, 500, 81, 16))
        self.labelOutIteminfo.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")
        self.labelOutIteminfo.setObjectName("labelOutIteminfo")
        self.groupBoxOutBorrower = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxOutBorrower.setGeometry(QtCore.QRect(80, 270, 290, 50))
        self.groupBoxOutBorrower.setStyleSheet("background-color: rgb(65, 65, 65);\n"
"color: rgb(255, 255, 255);")
        self.groupBoxOutBorrower.setObjectName("groupBoxOutBorrower")
        self.radioButtonOutNewborrower = QtWidgets.QRadioButton(self.groupBoxOutBorrower)
        self.radioButtonOutNewborrower.setGeometry(QtCore.QRect(20, 20, 101, 17))
        self.radioButtonOutNewborrower.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButtonOutNewborrower.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButtonOutNewborrower.setObjectName("radioButtonOutNewborrower")
        self.radioButtonOutExistingborrower = QtWidgets.QRadioButton(self.groupBoxOutBorrower)
        self.radioButtonOutExistingborrower.setGeometry(QtCore.QRect(170, 20, 111, 17))
        self.radioButtonOutExistingborrower.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButtonOutExistingborrower.setObjectName("radioButtonOutExistingborrower")
        self.spinBoxOutStudentNumber = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBoxOutStudentNumber.setEnabled(False)
        self.spinBoxOutStudentNumber.setGeometry(QtCore.QRect(80, 360, 291, 41))
        self.spinBoxOutStudentNumber.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.spinBoxOutStudentNumber.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(65, 65, 65);")
        self.spinBoxOutStudentNumber.setMaximum(1000000000)
        self.spinBoxOutStudentNumber.setObjectName("spinBoxOutStudentNumber")
        self.labelIDNumber = QtWidgets.QLabel(self.centralwidget)
        self.labelIDNumber.setGeometry(QtCore.QRect(80, 340, 111, 16))
        self.labelIDNumber.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")
        self.labelIDNumber.setObjectName("labelIDNumber")
        self.labelOutCard.raise_()
        self.labelOutTitle.raise_()
        self.pushButtonOutBack.raise_()
        self.pushButtonOutSubmit.raise_()
        self.labelOutLogo.raise_()
        self.comboBoxBorrowerName.raise_()
        self.labelOutExistingborrowerinfo.raise_()
        self.lineEditOutIteminfo.raise_()
        self.labelOutIteminfo.raise_()
        self.groupBoxOutBorrower.raise_()
        self.spinBoxOutStudentNumber.raise_()
        self.labelIDNumber.raise_()
        outitemWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(outitemWindow)
        QtCore.QMetaObject.connectSlotsByName(outitemWindow)
        outitemWindow.setTabOrder(self.comboBoxBorrowerName, self.pushButtonOutSubmit)
        outitemWindow.setTabOrder(self.pushButtonOutSubmit, self.pushButtonOutBack)

    def retranslateUi(self, outitemWindow):
        _translate = QtCore.QCoreApplication.translate
        outitemWindow.setWindowTitle(_translate("outitemWindow", "QR CODE INVENTORY SYSTEM"))
        self.labelOutTitle.setText(_translate("outitemWindow", "OUT ITEM"))
        self.pushButtonOutBack.setText(_translate("outitemWindow", "BACK"))
        self.pushButtonOutSubmit.setText(_translate("outitemWindow", "CONFIRM"))
        self.labelOutExistingborrowerinfo.setText(_translate("outitemWindow", "Borrowers Full Name:"))
        self.labelOutIteminfo.setText(_translate("outitemWindow", "Item Information"))
        self.groupBoxOutBorrower.setTitle(_translate("outitemWindow", "Choose Borrower"))
        self.radioButtonOutNewborrower.setText(_translate("outitemWindow", "New Borrower"))
        self.radioButtonOutExistingborrower.setText(_translate("outitemWindow", "Existing Borrower"))
        self.labelIDNumber.setText(_translate("outitemWindow", "Borrowers ID Number"))
import icons


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    outitemWindow = QtWidgets.QMainWindow()
    ui = Ui_outitemWindow()
    ui.setupUi(outitemWindow)
    outitemWindow.show()
    sys.exit(app.exec_())