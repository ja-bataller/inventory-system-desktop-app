from GUI.index import *
from GUI.login import *
from GUI.signup import *
from GUI.main import *
from GUI.account_settings import *
from GUI.initem import *
from GUI.outitem import *
from GUI.addremoveitem import *
from GUI.qrcodegenerator import *
from GUI.about import *
from GUI.icons import *

from PyQt5.QtWidgets import *
import webbrowser
from PIL import Image
import qrcode
import os.path

import sys
import re

# CREATE DATABASE AND TABLE FUNCTION
from database import *

# VALIDATION FUNCTIONS
from validation import *

from datetime import datetime

# Textual month, day and year
today = datetime.today()
date_today = today.strftime("%B %d, %Y") + " " + datetime.today().strftime("%I:%M %p")
print("Date Today =", date_today)

# MYSQL DATABASE CONFIGURATION
DB_configuration = {"host": "localhost", "user": "root", "password": "admin", "database": "inventory_system_tupc_uitc"}

# CREATE ARRAY - DATA COMES FROM MYSQL DB
main_equipments = []
main_records = []

accounts = []
usernames = []
currentUser = []

equipments = []
items = []
pickedQty = []

existing_borrowers_name = []
existing_borrowers_id = []
existing_borrowers_info = []

check_borrower_info = []
check_item_info = []
check_item_qty = []

out_items = []


# INDEX WINDOW - CHECKED & DONE
class IndexWindow(Ui_indexWindow, QMainWindow):

    def __init__(self):

        super(IndexWindow, self).__init__()
        self.setupUi(self)

        # WHEN BUTTON IS CLICKED THIS WILL TRIGGER THE FUNCTION
        self.pushButtonIndexLogin.clicked.connect(self.login)
        self.pushButtonIndexSignup.clicked.connect(self.signup)

    # OPENS THE LOGIN WINDOW
    def login(self):

        # LOGIN RESET INPUT FIELDS
        validation.loginReset(login)

        # MYSQL QUERY - GET ADMINS ACCOUNT DETAILS
        self.mydb = mysql.connector.connect(**DB_configuration)
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT username,password, account_type FROM accounts;")

        # ADD DATA TO ACCOUNT LIST
        for account in mycursor:
            accounts.append(account)
        print("Username , Password, first_name, last_name, account_type")
        print(accounts)

        # OPEN LOGIN WINDOW AND CLOSE INDEX WINDOW
        login.show()
        index.close()

    # OPENS THE SIGNUP WINDOW
    def signup(self):

        # SIGN UP RESET INPUT FIELDS
        validation.signupReset(signup)

        # MYSQL QUERY - GET EXISTING USERNAME
        self.mydb = mysql.connector.connect(**DB_configuration)
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT username FROM accounts;")

        # ADD DATA TO USERNAMES LIST
        for username in mycursor:
            usernames.append(username)
        print("Existing Usernames")
        print(usernames)

        # OPEN SIGNUP WINDOW AND CLOSE INDEX WINDOW
        signup.show()
        index.close()


# LOGIN WINDOW - CHECKED & DONE
class LoginWindow(Ui_loginWindow, QMainWindow):
    def __init__(self):

        super(LoginWindow, self).__init__()
        self.setupUi(self)

        # WHEN BUTTON IS CLICKED THIS WILL TRIGGER THE FUNCTION
        self.pushButtonLogin.clicked.connect(self.login_account)
        self.pushButtonLoginSignup.clicked.connect(self.signup)

    # LOGIN ACCOUNT PROCESS
    def login_account(self):

        login_username = self.lineEditLoginUsername.text()
        login_password = self.lineEditLoginPassword.text()

        #  IF THE LOG-IN FIELD ARE EMPTY
        if login_username == "" or login_password == "":
            QMessageBox.warning(self, "Error", "Please complete all fields.")
            return

        for x in range(len(accounts)):
            # LOG IN FOR ADMINISTRATOR ACCOUNT
            if accounts[x][0] == login_username and accounts[x][1] == login_password and accounts[x][
                2] == "administrator":

                # QMessageBox.information(self, "Success","WELCOME.")
                self.lineEditLoginUsername.clear()
                self.lineEditLoginPassword.clear()

                # MYSQL QUERY - GET ADMINS ACCOUNT DETAILS
                self.mydb = mysql.connector.connect(**DB_configuration)
                mycursor = self.mydb.cursor()
                sql = "SELECT first_name ,last_name, username, password FROM accounts WHERE username = %s"
                val = (login_username,)
                mycursor.execute(sql, val)

                # ADD DATA TO CURRENT USER LIST
                for users in mycursor:
                    currentUser.append(users)
                    print("First Name, Last Name, username, Password")
                    print(currentUser)

                for x in range(len(currentUser)):
                    first_name = currentUser[x][0]
                    last_name = currentUser[x][1]
                    full_name = first_name + " " + last_name

                    main.MainSystemUserLbl.setText(full_name)
                    main.MainSystemUserAccountLbl.setText("Administrator")

                # -----------------------------------------------------------------------------------------------------

                main_equipments.clear()

                # MYSQL QUERY - APPEND TO EQUIPMENTS LIST
                self.mydb = mysql.connector.connect(**DB_configuration)
                mycursor = self.mydb.cursor()
                mycursor.execute("SELECT equipment, quantity FROM items;")

                for item in mycursor:
                    main_equipments.append(item)

                print(main_equipments)

                # ADD EQUIPMENT TO TABLE
                main.tableWidget.setRowCount(0)
                row = 0
                main.tableWidget.setRowCount(len(main_equipments))
                for item in main_equipments:
                    main.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(item[0])))
                    main.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(item[1])))

                    row = row + 1

                # -----------------------------------------------------------------------------------------------------

                main_records.clear()

                # MYSQL QUERY - APPEND TO RECORDS LIST
                self.mydb = mysql.connector.connect(**DB_configuration)
                mycursor = self.mydb.cursor()
                mycursor.execute("SELECT name, borrowers_num, item, date_out, date_in  FROM borrowers;")

                for record in mycursor:
                    main_records.append(record)

                print(main_records)

                # ADD EQUIPMENT TO TABLE
                main.tableWidget_2.setRowCount(0)
                row = 0
                main.tableWidget_2.setRowCount(len(main_records))
                for b_record in main_records:
                    main.tableWidget_2.setItem(row, 0, QtWidgets.QTableWidgetItem(str(b_record[0])))
                    main.tableWidget_2.setItem(row, 1, QtWidgets.QTableWidgetItem(str(b_record[1])))
                    main.tableWidget_2.setItem(row, 2, QtWidgets.QTableWidgetItem(str(b_record[2])))
                    main.tableWidget_2.setItem(row, 3, QtWidgets.QTableWidgetItem(str(b_record[3])))
                    main.tableWidget_2.setItem(row, 4, QtWidgets.QTableWidgetItem(str(b_record[4])))

                    row = row + 1

                # -----------------------------------------------------------------------------------------------------

                existing_borrowers_id.clear()
                main.comboBoxMainRecords.clear()
                main.comboBoxMainRecords.addItem("---ALL BORROWERS---")

                # MYSQL QUERY - APPEND TO existing_borrowers_id LIST
                self.mydb = mysql.connector.connect(**DB_configuration)
                mycursor = self.mydb.cursor()
                mycursor.execute("SELECT borrowers_num FROM borrowers;")

                for borrower_id in mycursor:
                    existing_borrowers_id.append(borrower_id)

                ids = list(dict.fromkeys(existing_borrowers_id))
                for b_id in ids:
                    main.comboBoxMainRecords.addItems(b_id)

                print("EXISTING BORROWERS ID")
                print(existing_borrowers_id)

                # -----------------------------------------------------------------------------------------------------

                login.close()
                main.show()
                return

            # LOG IN FOR OPERATOR ACCOUNT
            if accounts[x][0] == login_username and accounts[x][1] == login_password and accounts[x][2] == "operator":
                # QMessageBox.information(self, "Success","WELCOME.")
                self.lineEditLoginUsername.clear()
                self.lineEditLoginPassword.clear()

                # MYSQL QUERY - GET OPERATORS ACCOUNT DETAILS
                self.mydb = mysql.connector.connect(**DB_configuration)
                mycursor = self.mydb.cursor()
                sql = "SELECT first_name ,last_name  FROM accounts WHERE username = %s"
                val = (login_username,)
                mycursor.execute(sql, val)

                for users in mycursor:
                    currentUser.append(users)
                    print("First Name, Last Name, username, Password")
                    print(currentUser)

                for x in range(len(currentUser)):
                    first_name = currentUser[x][0]
                    last_name = currentUser[x][1]
                    full_name = first_name + " " + last_name

                main.MainSystemUserLbl.setText(full_name)
                main.MainSystemUserAccountLbl.setText("Operator")

                # -----------------------------------------------------------------------------------------------------

                main_equipments.clear()

                # MYSQL QUERY - APPEND TO EQUIPMENTS LIST
                self.mydb = mysql.connector.connect(**DB_configuration)
                mycursor = self.mydb.cursor()
                mycursor.execute("SELECT equipment, quantity FROM items;")

                for item in mycursor:
                    main_equipments.append(item)

                print(main_equipments)

                # ADD EQUIPMENT TO TABLE
                main.tableWidget.setRowCount(0)
                row = 0
                main.tableWidget.setRowCount(len(main_equipments))
                for item in main_equipments:
                    main.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(item[0])))
                    main.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(item[1])))

                    row = row + 1

                # -----------------------------------------------------------------------------------------------------

                main_records.clear()

                # MYSQL QUERY - APPEND TO RECORDS LIST
                self.mydb = mysql.connector.connect(**DB_configuration)
                mycursor = self.mydb.cursor()
                mycursor.execute("SELECT name, borrowers_num, item, date_out, date_in  FROM borrowers;")

                for record in mycursor:
                    main_records.append(record)

                print(main_records)

                # ADD EQUIPMENT TO TABLE
                main.tableWidget_2.setRowCount(0)
                row = 0
                main.tableWidget_2.setRowCount(len(main_records))
                for b_record in main_records:
                    main.tableWidget_2.setItem(row, 0, QtWidgets.QTableWidgetItem(str(b_record[0])))
                    main.tableWidget_2.setItem(row, 1, QtWidgets.QTableWidgetItem(str(b_record[1])))
                    main.tableWidget_2.setItem(row, 2, QtWidgets.QTableWidgetItem(str(b_record[2])))
                    main.tableWidget_2.setItem(row, 3, QtWidgets.QTableWidgetItem(str(b_record[3])))
                    main.tableWidget_2.setItem(row, 4, QtWidgets.QTableWidgetItem(str(b_record[4])))

                    row = row + 1

                # -----------------------------------------------------------------------------------------------------

                existing_borrowers_id.clear()
                main.comboBoxMainRecords.clear()
                main.comboBoxMainRecords.addItem("---ALL BORROWERS---")

                # MYSQL QUERY - APPEND TO existing_borrowers_id LIST
                self.mydb = mysql.connector.connect(**DB_configuration)
                mycursor = self.mydb.cursor()
                mycursor.execute("SELECT borrowers_num FROM borrowers;")

                for borrower_id in mycursor:
                    existing_borrowers_id.append(borrower_id)

                ids = list(dict.fromkeys(existing_borrowers_id))
                for b_id in ids:
                    main.comboBoxMainRecords.addItems(b_id)

                print("EXISTING BORROWERS ID")
                print(existing_borrowers_id)

                # -----------------------------------------------------------------------------------------------------

                login.close()
                main.show()
                return

        QMessageBox.warning(self, "Error", "This User is not registered.")
        self.lineEditLoginUsername.clear()
        self.lineEditLoginPassword.clear()
        return

    # OPENS THE  SIGNUP WINDOW
    def signup(self):

        usernames.clear()

        validation.signupReset(signup)

        # MYSQL QUERY - GET ACCOUNTS
        self.mydb = mysql.connector.connect(**DB_configuration)
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT username FROM accounts;")

        for username in mycursor:
            usernames.append(username)
        print("EXISTING USERNAMES")
        print(usernames)

        signup.show()
        login.close()


# SIGNUP WINDOW - CHECKED & DONE
class SignupWindow(Ui_signupWindow, QMainWindow):

    def __init__(self):
        super(SignupWindow, self).__init__()
        self.setupUi(self)

        self.pushButtonSignup.clicked.connect(self.signup_account)
        self.pushButtonSignupLogin.clicked.connect(self.login)

    # OPENS THE LOGIN WINDOW
    def login(self):

        accounts.clear()

        # LOG IN RESET INPUT FIELDS
        validation.loginReset(login)

        # OPEN LOGIN WINDOW AND CLOSE SIGNUP WINDOW
        self.mydb = mysql.connector.connect(**DB_configuration)
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT username,password, account_type FROM accounts;")

        for account in mycursor:
            accounts.append(account)
        print("Username , Password, first_name, last_name, account_type")
        print(accounts)

        login.show()
        signup.close()

    # SIGN UP ACCOUNT AND SAVE TO MYSQL PROCESS
    def signup_account(self):

        first_name = self.lineEditSignupFirstname.text()
        last_name = self.lineEditSignupLastname.text()
        username = self.lineEditSignupUsername.text()
        password = self.lineEditSignupPassword.text()
        confirm_pass = self.lineEditSignupRetypePassword.text()
        account_admin = self.radioButtonSignupAdministrator.isChecked()
        account_operator = self.radioButtonSignupOperator.isChecked()
        signup_code = self.lineEditSignupCode.text()
        code = "tupc"

        # IF INPUT FIELD IS NOT COMPLETE
        if first_name == "" or last_name == "" or username == "" or password == "" or confirm_pass == "" or signup_code == "":
            QMessageBox.warning(self, "Error", "Please complete all fields.")
            return

        if account_admin == False and account_operator == False:
            QMessageBox.warning(self, "Error", "Please complete all fields.")
            return

        # IF USERNAME IS NOT AVAILABLE (USERNAME MUST BE UNIQUE)
        for x in range(len(usernames)):
            if usernames[x][0] == username:
                QMessageBox.warning(self, "Error", "This Username is not available.")

                self.lineEditSignupUsername.clear()
                self.lineEditSignupPassword.clear()
                self.lineEditSignupRetypePassword.clear()
                self.lineEditSignupCode.clear()
                return

        # IF PASSWORD AND CONFIRM PASSWORD DOES NOT MATCH
        if password != confirm_pass:
            QMessageBox.warning(self, "Error",
                                "This Password and Confirm password doesn't match.")

            self.lineEditSignupPassword.clear()
            self.lineEditSignupRetypePassword.clear()
            return

        # IF SIGNUP CODE IS CORRECT, THEN SAVE TO MYSQL DB
        if signup_code == code:
            # IF ACCOUNT IS ADMIN
            if account_admin:
                print("pass")
                self.mydb = mysql.connector.connect(**DB_configuration)
                mycursor = self.mydb.cursor()
                print("pass")
                sql = "INSERT INTO accounts (first_name, last_name, username, password, account_type) VALUES (%s,%s,%s,%s,%s);"
                val = (first_name, last_name, username, password, "administrator")
                mycursor.execute(sql, val)
                self.mydb.commit()

                print("pass")

                # UPDATE THE ACCOUNTS ARRAY
                self.mydb = mysql.connector.connect(**DB_configuration)
                mycursor = self.mydb.cursor()
                mycursor.execute("SELECT username,password, account_type FROM accounts;")
                for account in mycursor:
                    accounts.append(account)
                print("Username , Password, first_name, last_name, account_type")
                print(accounts)
                # END

                QMessageBox.information(self, "Success",
                                        "Administrator account signed-up successfully.")

                signup.close()
                login.show()
                return

            # IF ACCOUNT IS OPERATOR
            if account_operator:
                self.mydb = mysql.connector.connect(**DB_configuration)
                mycursor = self.mydb.cursor()
                sql = "INSERT INTO accounts (first_name,last_name,username, password, account_type ) VALUES (%s,%s,%s,%s,%s);"
                val = (first_name, last_name, username, password, "operator")
                mycursor.execute(sql, val)
                self.mydb.commit()

                # UPDATE THE ACCOUNTS ARRAY
                self.mydb = mysql.connector.connect(**DB_configuration)
                mycursor = self.mydb.cursor()
                mycursor.execute("SELECT username,password, account_type FROM accounts;")
                for account in mycursor:
                    accounts.append(account)
                print("Username , Password, first_name, last_name, account_type")
                print(accounts)
                #  END

                QMessageBox.information(self, "Success",
                                        "Operator account signed-up successfully.")

                signup.close()
                login.show()
                return
            else:
                QMessageBox.warning(self, "Error", "MYSQL ERROR.")


# MAIN WINDOW - NEED TO FIX - PAUSE
class MainWindow(Ui_MainSystemWindow, QMainWindow):

    def __init__(self):

        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.pushButtonMainShowRecords.clicked.connect(self.show_records)
        self.MainSystemLogOutPushBUtton.clicked.connect(self.logout)
        self.MainSystemAccountSettingsPushButton.clicked.connect(self.changePassword)
        self.MainSystemAddItemPushButton.clicked.connect(self.addremoveItem)
        self.MainSystemItemInPushButton.clicked.connect(self.inItem)
        self.MainSystemItemOutPushButton.clicked.connect(self.outItem)
        self.MainSystemQrCodeGeneratorPushButton.clicked.connect(self.qr_code_generator)
        self.MainSystemAboutPushButton.clicked.connect(self.about)

    def show_records(self):
        picked_id = self.comboBoxMainRecords.currentText()

        if self.comboBoxMainRecords.currentIndex() == 0:
            # -----------------------------------------------------------------------------------------------------

            main_records.clear()

            # MYSQL QUERY - APPEND TO RECORDS LIST
            self.mydb = mysql.connector.connect(**DB_configuration)
            mycursor = self.mydb.cursor()
            mycursor.execute("SELECT name, borrowers_num, item, date_out, date_in  FROM borrowers;")

            for record in mycursor:
                main_records.append(record)

            print(main_records)

            # ADD EQUIPMENT TO TABLE
            self.tableWidget_2.setRowCount(0)
            row = 0
            self.tableWidget_2.setRowCount(len(main_records))
            for b_record in main_records:
                self.tableWidget_2.setItem(row, 0, QtWidgets.QTableWidgetItem(str(b_record[0])))
                self.tableWidget_2.setItem(row, 1, QtWidgets.QTableWidgetItem(str(b_record[1])))
                self.tableWidget_2.setItem(row, 2, QtWidgets.QTableWidgetItem(str(b_record[2])))
                self.tableWidget_2.setItem(row, 3, QtWidgets.QTableWidgetItem(str(b_record[3])))
                self.tableWidget_2.setItem(row, 4, QtWidgets.QTableWidgetItem(str(b_record[4])))

                row = row + 1
            return
            # -----------------------------------------------------------------------------------------------------

        main_records.clear()

        self.mydb = mysql.connector.connect(**DB_configuration)
        mycursor = self.mydb.cursor()
        sql = "SELECT name, borrowers_num, item, date_out, date_in FROM borrowers WHERE borrowers_num = %s;"
        val = (picked_id,)
        mycursor.execute(sql, val)

        for record in mycursor:
            main_records.append(record)

        print(main_records)

        # ADD EQUIPMENT TO TABLE
        self.tableWidget_2.setRowCount(0)
        row = 0
        self.tableWidget_2.setRowCount(len(main_records))
        for b_record in main_records:
            self.tableWidget_2.setItem(row, 0, QtWidgets.QTableWidgetItem(str(b_record[0])))
            self.tableWidget_2.setItem(row, 1, QtWidgets.QTableWidgetItem(str(b_record[1])))
            self.tableWidget_2.setItem(row, 2, QtWidgets.QTableWidgetItem(str(b_record[2])))
            self.tableWidget_2.setItem(row, 3, QtWidgets.QTableWidgetItem(str(b_record[3])))
            self.tableWidget_2.setItem(row, 4, QtWidgets.QTableWidgetItem(str(b_record[4])))

            row = row + 1
        return


    # LOGOUT PROCESS
    def logout(self):

        answer = QMessageBox.question(self, "Logout", "Are you sure you want to logout?",
                                      QMessageBox.Yes | QMessageBox.No)
        if answer == QMessageBox.Yes:
            self.tableWidget.setRowCount(0)

            equipments.clear()

            accounts.clear()
            usernames.clear()

            print("CLEARED")

            main.close()
            index.show()

    # OPEN ACCOUNT SETTINGS
    def changePassword(self):

        validation.accountSettingsReset(account_settings)

        main.close()
        account_settings.show()

    # OPEN ADD & REMOVE ITEMS
    def addremoveItem(self):

        if self.MainSystemUserAccountLbl.text() != "Administrator":
            QMessageBox.warning(self, "Unauthorized Access",
                                "Only Admins can access this Window.")
            return
        else:

            addremove_item.radioButtonUpdateInventoryAdditem.setAutoExclusive(False)
            addremove_item.radioButtonUpdateInventoryAdditem.setChecked(False)
            addremove_item.radioButtonUpdateInventoryAdditem.setAutoExclusive(True)

            addremove_item.radioButtonUpdateInventoryUpdateItem.setAutoExclusive(False)
            addremove_item.radioButtonUpdateInventoryUpdateItem.setChecked(False)
            addremove_item.radioButtonUpdateInventoryUpdateItem.setAutoExclusive(True)

            addremove_item.radioButtonUpdateInventoryDeleteItem.setAutoExclusive(False)
            addremove_item.radioButtonUpdateInventoryDeleteItem.setChecked(False)
            addremove_item.radioButtonUpdateInventoryDeleteItem.setAutoExclusive(True)

            addremove_item.comboBoxUpdateInventoryEquipment.clear()
            addremove_item.spinBoxUpdateInventoryQty.setValue(0)

            addremove_item.comboBoxUpdateInventoryEquipment.setEnabled(False)
            addremove_item.comboBoxUpdateInventoryEquipment.setEditable(False)
            addremove_item.spinBoxUpdateInventoryQty.setEnabled(False)
            addremove_item.pushButtonUpdateinventoryConfirm.setEnabled(False)

            main.close()
            addremove_item.show()

    # OPEN IN ITEM WINDOW
    def inItem(self):

        existing_borrowers_id.clear()
        in_item.comboInOutExistingborrowersinfo.clear()
        in_item.comboInOutExistingborrowersinfo.addItem("---Choose Borrowers ID Number---")
        in_item.lineEditInIteminfo.clear()

        # ------------------------------------------------------------

        # MYSQL QUERY - APPEND TO existing_borrowers_id LIST
        self.mydb = mysql.connector.connect(**DB_configuration)
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT borrowers_num FROM borrowers;")

        for borrower_id in mycursor:
            existing_borrowers_id.append(borrower_id)

        ids = list(dict.fromkeys(existing_borrowers_id))
        for b_id in ids:
            in_item.comboInOutExistingborrowersinfo.addItems(b_id)

        print("EXISTING BORROWERS ID")
        print(existing_borrowers_id)

        # ------------------------------------------------------------

        main.close()
        in_item.show()

    # OPEN OUT ITEM WINDOW
    def outItem(self):

        out_item.radioButtonOutExistingborrower.setAutoExclusive(False)
        out_item.radioButtonOutExistingborrower.setChecked(False)
        out_item.radioButtonOutExistingborrower.setAutoExclusive(True)

        out_item.radioButtonOutNewborrower.setAutoExclusive(False)
        out_item.radioButtonOutNewborrower.setChecked(False)
        out_item.radioButtonOutNewborrower.setAutoExclusive(True)

        out_item.spinBoxOutStudentNumber.setEnabled(False)
        out_item.comboBoxBorrowerName.setEnabled(False)
        out_item.comboBoxBorrowerName.setEditable(False)
        out_item.lineEditOutIteminfo.setEnabled(False)
        out_item.pushButtonOutSubmit.setEnabled(False)

        out_item.spinBoxOutStudentNumber.setValue(0)
        out_item.comboBoxBorrowerName.clear()
        out_item.lineEditOutIteminfo.clear()

        main.close()
        out_item.show()

    # OPEN QR CODE GENERATOR WINDOW
    def qr_code_generator(self):
        if self.MainSystemUserAccountLbl.text() != "Administrator":
            QMessageBox.warning(self, "Unauthorized Access",
                                "Only Admins can access this Window.")
        else:

            items.clear()

            qr_code_generator.comboBoxQrcodeItemCode.clear()
            qr_code_generator.comboBoxQrcodeItemCode.addItem("Click here to choose Equipment")

            qr_code_generator.spinBoxQrcodeStart.setMinimum(1)
            qr_code_generator.spinBoxQrcodeEnd.setMinimum(1)

            qr_code_generator.spinBoxQrcodeStart.setValue(1)
            qr_code_generator.spinBoxQrcodeEnd.setValue(1)

            # MYSQL QUERY - APPEND TO COMBO-BOX
            self.mydb = mysql.connector.connect(**DB_configuration)
            mycursor = self.mydb.cursor()
            mycursor.execute("SELECT equipment FROM items;")

            for itemDB in mycursor:
                items.append(itemDB)

            print("EQUIPMENTS IN items LIST AND COMBO-BOX")
            print(items)

            for item in items:
                qr_code_generator.comboBoxQrcodeItemCode.addItems(item)

            main.close()
            qr_code_generator.show()

    # OPEN ABOUT WINDOW
    def about(self):
        main.close()
        about.show()


# ACCOUNT SETTINGS WINDOW - CHECKED & DONE
class AccountSettingsWindow(Ui_AccountSettingsWindow, QMainWindow):

    def __init__(self):

        super(AccountSettingsWindow, self).__init__()
        self.setupUi(self)

        self.AccountSettingsBackPushButton.clicked.connect(self.main)
        self.AccountSettingsChangePasswordPushButton.clicked.connect(self.changePassword)

    # OPEN MAIN WINDOW
    def main(self):

        main_equipments.clear()

        # MYSQL QUERY - APPEND TO EQUIPMENTS LIST
        self.mydb = mysql.connector.connect(**DB_configuration)
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT equipment, quantity FROM items;")

        for item in mycursor:
            main_equipments.append(item)

        print(main_equipments)

        # ADD EQUIPMENT TO TABLE
        main.tableWidget.setRowCount(0)
        row = 0
        main.tableWidget.setRowCount(len(main_equipments))
        for item in main_equipments:
            main.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(item[0])))
            main.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(item[1])))
            row = row + 1

        # -----------------------------------------------------------------------------------------------------

        main_records.clear()

        # MYSQL QUERY - APPEND TO RECORDS LIST
        self.mydb = mysql.connector.connect(**DB_configuration)
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT name, borrowers_num, item, date_out, date_in  FROM borrowers;")

        for record in mycursor:
            main_records.append(record)

        print(main_records)

        # ADD EQUIPMENT TO TABLE
        main.tableWidget_2.setRowCount(0)
        row = 0
        main.tableWidget_2.setRowCount(len(main_records))
        for b_record in main_records:
            main.tableWidget_2.setItem(row, 0, QtWidgets.QTableWidgetItem(str(b_record[0])))
            main.tableWidget_2.setItem(row, 1, QtWidgets.QTableWidgetItem(str(b_record[1])))
            main.tableWidget_2.setItem(row, 2, QtWidgets.QTableWidgetItem(str(b_record[2])))
            main.tableWidget_2.setItem(row, 3, QtWidgets.QTableWidgetItem(str(b_record[3])))
            main.tableWidget_2.setItem(row, 4, QtWidgets.QTableWidgetItem(str(b_record[4])))

            row = row + 1

        # -----------------------------------------------------------------------------------------------------

        existing_borrowers_id.clear()
        main.comboBoxMainRecords.clear()
        main.comboBoxMainRecords.addItem("---ALL BORROWERS---")

        # MYSQL QUERY - APPEND TO existing_borrowers_id LIST
        self.mydb = mysql.connector.connect(**DB_configuration)
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT borrowers_num FROM borrowers;")

        for borrower_id in mycursor:
            existing_borrowers_id.append(borrower_id)

        ids = list(dict.fromkeys(existing_borrowers_id))
        for b_id in ids:
            main.comboBoxMainRecords.addItems(b_id)

        print("EXISTING BORROWERS ID")
        print(existing_borrowers_id)

        # -----------------------------------------------------------------------------------------------------

        account_settings.close()
        main.show()

    # CHANGE CURRENT ACCOUNT PASSWORD
    def changePassword(self):

        old = self.AccountSettingsOldPasswordLineEdit.text()
        new = self.AccountSettingsNewPasswordLineEdit.text()
        confirm = self.AccountSettingsConfirmNewPasswordLineEdit.text()

        if old == "" or new == "" or confirm == "":
            QMessageBox.warning(self, "Error", "Please complete all fields.")
            return

        if old != "" and new != "" and confirm != "":
            for x in range(len(currentUser)):
                username = currentUser[x][2]
                old_value = currentUser[x][3]

            if new != confirm:
                QMessageBox.warning(self, "Error",
                                    "Confirm New password doesn't match.")
                self.AccountSettingsOldPasswordLineEdit.clear()
                self.AccountSettingsNewPasswordLineEdit.clear()
                self.AccountSettingsConfirmNewPasswordLineEdit.clear()
                return

            if old == old_value:
                self.mydb = mysql.connector.connect(**DB_configuration)
                mycursor = self.mydb.cursor()
                sql = "UPDATE accounts SET password = %s WHERE username = %s;"
                val = (new, username)
                mycursor.execute(sql, val)
                self.mydb.commit()

                accounts.clear()

                self.mydb = mysql.connector.connect(**DB_configuration)
                mycursor = self.mydb.cursor()
                mycursor.execute("SELECT username,password, account_type FROM accounts;")
                for account in mycursor:
                    accounts.append(account)
                print("Username , Password, first_name, last_name, account_type")
                print(accounts)

                QMessageBox.information(self, "Success",
                                        "The password has been changed successfully. Please log in again.")
                account_settings.close()
                index.show()
                return

            else:
                self.AccountSettingsOldPasswordLineEdit.clear()
                self.AccountSettingsNewPasswordLineEdit.clear()
                self.AccountSettingsConfirmNewPasswordLineEdit.clear()
                QMessageBox.warning(self, "Error",
                                    "The old password you entered is incorrect.")
                return


# ADD / REMOVE ITEM WINDOW - DONE - NEED TO CHECK
class AddRemoveItemWindow(Ui_addremoveitemWindow, QMainWindow):

    def __init__(self):
        super(AddRemoveItemWindow, self).__init__()
        self.setupUi(self)

        self.radioButtonUpdateInventoryAdditem.clicked.connect(self.setup_add)
        self.radioButtonUpdateInventoryUpdateItem.clicked.connect(self.setup_update)
        self.radioButtonUpdateInventoryDeleteItem.clicked.connect(self.setup_delete)

        self.pushButtonUpdateinventoryConfirm.clicked.connect(self.equipment_db)
        self.pusButtonUpdateInventoryBack.clicked.connect(self.main)

    # BACK TO MAIN WINDOW
    def main(self):

        main.tableWidget.setRowCount(0)

        main_equipments.clear()

        # MYSQL QUERY - APPEND TO EQUIPMENTS LIST
        self.mydb = mysql.connector.connect(**DB_configuration)
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT equipment, quantity FROM items;")

        for item in mycursor:
            main_equipments.append(item)

        print(main_equipments)

        # ADD EQUIPMENT TO TABLE
        main.tableWidget.setRowCount(0)
        row = 0
        main.tableWidget.setRowCount(len(main_equipments))
        for item in main_equipments:
            main.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(item[0])))
            main.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(item[1])))
            row = row + 1

        # -----------------------------------------------------------------------------------------------------

        main_records.clear()

        # MYSQL QUERY - APPEND TO RECORDS LIST
        self.mydb = mysql.connector.connect(**DB_configuration)
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT name, borrowers_num, item, date_out, date_in  FROM borrowers;")

        for record in mycursor:
            main_records.append(record)

        print(main_records)

        # ADD EQUIPMENT TO TABLE
        main.tableWidget_2.setRowCount(0)
        row = 0
        main.tableWidget_2.setRowCount(len(main_records))
        for b_record in main_records:
            main.tableWidget_2.setItem(row, 0, QtWidgets.QTableWidgetItem(str(b_record[0])))
            main.tableWidget_2.setItem(row, 1, QtWidgets.QTableWidgetItem(str(b_record[1])))
            main.tableWidget_2.setItem(row, 2, QtWidgets.QTableWidgetItem(str(b_record[2])))
            main.tableWidget_2.setItem(row, 3, QtWidgets.QTableWidgetItem(str(b_record[3])))
            main.tableWidget_2.setItem(row, 4, QtWidgets.QTableWidgetItem(str(b_record[4])))

            row = row + 1

        # -----------------------------------------------------------------------------------------------------

        existing_borrowers_id.clear()
        main.comboBoxMainRecords.clear()
        main.comboBoxMainRecords.addItem("---ALL BORROWERS---")

        # MYSQL QUERY - APPEND TO existing_borrowers_id LIST
        self.mydb = mysql.connector.connect(**DB_configuration)
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT borrowers_num FROM borrowers;")

        for borrower_id in mycursor:
            existing_borrowers_id.append(borrower_id)

        ids = list(dict.fromkeys(existing_borrowers_id))
        for b_id in ids:
            main.comboBoxMainRecords.addItems(b_id)

        print("EXISTING BORROWERS ID")
        print(existing_borrowers_id)

        # -----------------------------------------------------------------------------------------------------

        addremove_item.close()
        main.show()

    def setup_add(self):

        equipments.clear()
        items.clear()
        pickedQty.clear()

        self.comboBoxUpdateInventoryEquipment.clear()
        self.comboBoxUpdateInventoryEquipment.addItem(
            "--- type here equipment / existing item is already listed below ---")
        self.comboBoxUpdateInventoryEquipment.setEnabled(True)
        self.comboBoxUpdateInventoryEquipment.setEditable(False)
        self.comboBoxUpdateInventoryEquipment.setEditable(True)
        self.spinBoxUpdateInventoryQty.setValue(0)
        self.spinBoxUpdateInventoryQty.setEnabled(True)
        self.pushButtonUpdateinventoryConfirm.setEnabled(True)

        # MYSQL QUERY - APPEND TO EQUIPMENTS LIST
        self.mydb = mysql.connector.connect(**DB_configuration)
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT equipment, quantity FROM items;")

        for equipment in mycursor:
            equipments.append(equipment)

        print("EQUIPMENTS IN equipments LIST")
        print(equipments)

        # MYSQL QUERY - APPEND TO COMBO-BOX
        self.mydb = mysql.connector.connect(**DB_configuration)
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT equipment FROM items;")

        for itemDB in mycursor:
            items.append(itemDB)

        print("EQUIPMENTS IN items LIST AND COMBO-BOX")
        print(items)

        for item in items:
            self.comboBoxUpdateInventoryEquipment.addItems(item)

    def setup_update(self):

        equipments.clear()
        items.clear()
        pickedQty.clear()

        self.comboBoxUpdateInventoryEquipment.clear()
        self.comboBoxUpdateInventoryEquipment.addItem("--- choose equipment ---")
        self.comboBoxUpdateInventoryEquipment.setEnabled(True)
        self.comboBoxUpdateInventoryEquipment.setEditable(False)
        self.spinBoxUpdateInventoryQty.setValue(0)
        self.spinBoxUpdateInventoryQty.setEnabled(True)
        self.pushButtonUpdateinventoryConfirm.setEnabled(True)

        # MYSQL QUERY - APPEND TO EQUIPMENTS LIST
        self.mydb = mysql.connector.connect(**DB_configuration)
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT equipment, quantity FROM items;")

        for equipment in mycursor:
            equipments.append(equipment)

        print("equipment , quantity")
        print(equipments)

        # MYSQL QUERY - APPEND TO COMBO-BOX
        self.mydb = mysql.connector.connect(**DB_configuration)
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT equipment FROM items;")

        for itemDB in mycursor:
            items.append(itemDB)

        print("EQUIPMENTS IN items LIST AND COMBO-BOX")
        print(items)

        for item in items:
            self.comboBoxUpdateInventoryEquipment.addItems(item)

    def setup_delete(self):

        equipments.clear()
        items.clear()
        pickedQty.clear()

        self.comboBoxUpdateInventoryEquipment.clear()
        self.comboBoxUpdateInventoryEquipment.addItem("--- choose equipment ---")
        self.comboBoxUpdateInventoryEquipment.setEnabled(True)
        self.comboBoxUpdateInventoryEquipment.setEditable(False)
        self.spinBoxUpdateInventoryQty.setValue(0)
        self.spinBoxUpdateInventoryQty.setEnabled(True)
        self.pushButtonUpdateinventoryConfirm.setEnabled(True)

        # MYSQL QUERY - APPEND TO EQUIPMENTS LIST
        self.mydb = mysql.connector.connect(**DB_configuration)
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT equipment, quantity FROM items;")

        for equipment in mycursor:
            equipments.append(equipment)

        print("equipment , quantity")
        print(equipments)

        # MYSQL QUERY - APPEND TO COMBO-BOX
        self.mydb = mysql.connector.connect(**DB_configuration)
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT equipment FROM items;")

        for itemDB in mycursor:
            items.append(itemDB)

        print("EQUIPMENTS IN items LIST AND COMBO-BOX")
        print(items)

        for item in items:
            self.comboBoxUpdateInventoryEquipment.addItems(item)

    def equipment_db(self):

        equipment = self.comboBoxUpdateInventoryEquipment.currentText()
        equipment_quantity = self.spinBoxUpdateInventoryQty.value()

        if self.radioButtonUpdateInventoryAdditem.isChecked() == True:
            if self.comboBoxUpdateInventoryEquipment.currentIndex() == 0:
                QMessageBox.warning(self, "Error", "Please enter equipment you want to add to the Inventory.")
                return

            # IF EQUIPMENT IS ALREADY IN DATABASE
            for x in range(len(equipments)):
                if equipments[x][0] == equipment:
                    QMessageBox.warning(self, "Error", "This Equipment is already in Inventory, choose Update if you "
                                                       "wish to update the quantity.")
                    return

            self.mydb = mysql.connector.connect(**DB_configuration)
            mycursor = self.mydb.cursor()

            sql = "INSERT INTO items (equipment, quantity) VALUES (%s,%s);"
            val = (equipment, equipment_quantity,)
            mycursor.execute(sql, val)
            self.mydb.commit()

            equipments.clear()
            items.clear()

            addremove_item.radioButtonUpdateInventoryAdditem.setAutoExclusive(False)
            addremove_item.radioButtonUpdateInventoryAdditem.setChecked(False)
            addremove_item.radioButtonUpdateInventoryAdditem.setAutoExclusive(True)

            addremove_item.radioButtonUpdateInventoryUpdateItem.setAutoExclusive(False)
            addremove_item.radioButtonUpdateInventoryUpdateItem.setChecked(False)
            addremove_item.radioButtonUpdateInventoryUpdateItem.setAutoExclusive(True)

            addremove_item.radioButtonUpdateInventoryDeleteItem.setAutoExclusive(False)
            addremove_item.radioButtonUpdateInventoryDeleteItem.setChecked(False)
            addremove_item.radioButtonUpdateInventoryDeleteItem.setAutoExclusive(True)

            addremove_item.comboBoxUpdateInventoryEquipment.clear()
            addremove_item.spinBoxUpdateInventoryQty.setValue(0)

            addremove_item.comboBoxUpdateInventoryEquipment.setEnabled(False)
            addremove_item.comboBoxUpdateInventoryEquipment.setEditable(False)
            addremove_item.spinBoxUpdateInventoryQty.setEnabled(False)
            addremove_item.pushButtonUpdateinventoryConfirm.setEnabled(False)

            QMessageBox.information(self, "Added", "Item has been added to Inventory.")

        elif self.radioButtonUpdateInventoryUpdateItem.isChecked() == True:
            if self.comboBoxUpdateInventoryEquipment.currentIndex() == 0:
                QMessageBox.warning(self, "Error", "Please choose equipment you want to update in the Inventory.")
                return

            # MYSQL QUERY - APPEND TO PICKED QTY LIST
            self.mydb = mysql.connector.connect(**DB_configuration)
            mycursor = self.mydb.cursor()
            sql = "SELECT quantity FROM items WHERE equipment = %s;"
            val = (equipment,)
            mycursor.execute(sql, val)
            for pQty in mycursor:
                pickedQty.append(pQty)

            oldQty = pickedQty[0][0]
            newQty = oldQty + equipment_quantity

            self.mydb = mysql.connector.connect(**DB_configuration)
            mycursor = self.mydb.cursor()
            sql = "UPDATE items SET quantity = %s WHERE equipment = %s;"
            val = (newQty, equipment)
            mycursor.execute(sql, val)
            self.mydb.commit()

            equipments.clear()
            items.clear()

            addremove_item.radioButtonUpdateInventoryAdditem.setAutoExclusive(False)
            addremove_item.radioButtonUpdateInventoryAdditem.setChecked(False)
            addremove_item.radioButtonUpdateInventoryAdditem.setAutoExclusive(True)

            addremove_item.radioButtonUpdateInventoryUpdateItem.setAutoExclusive(False)
            addremove_item.radioButtonUpdateInventoryUpdateItem.setChecked(False)
            addremove_item.radioButtonUpdateInventoryUpdateItem.setAutoExclusive(True)

            addremove_item.radioButtonUpdateInventoryDeleteItem.setAutoExclusive(False)
            addremove_item.radioButtonUpdateInventoryDeleteItem.setChecked(False)
            addremove_item.radioButtonUpdateInventoryDeleteItem.setAutoExclusive(True)

            addremove_item.comboBoxUpdateInventoryEquipment.clear()
            addremove_item.spinBoxUpdateInventoryQty.setValue(0)

            addremove_item.comboBoxUpdateInventoryEquipment.setEnabled(False)
            addremove_item.comboBoxUpdateInventoryEquipment.setEditable(False)
            addremove_item.spinBoxUpdateInventoryQty.setEnabled(False)
            addremove_item.pushButtonUpdateinventoryConfirm.setEnabled(False)

            QMessageBox.information(self, "Update", "Item Quantity has been increased.")

        elif self.radioButtonUpdateInventoryDeleteItem.isChecked() == True:
            if self.comboBoxUpdateInventoryEquipment.currentIndex() == 0:
                QMessageBox.warning(self, "Error", "Please choose equipment you want to delete in the Inventory.")
                return

            # MYSQL QUERY - APPEND TO PICKED QTY LIST
            self.mydb = mysql.connector.connect(**DB_configuration)
            mycursor = self.mydb.cursor()
            sql = "SELECT quantity FROM items WHERE equipment = %s;"
            val = (equipment,)
            mycursor.execute(sql, val)

            for pQty in mycursor:
                pickedQty.append(pQty)

            print("pickedqty")
            print(pickedQty[0][0])

            print("spinbox qty")
            print(equipment_quantity)

            oldQty = pickedQty[0][0]
            spinQty = equipment_quantity
            newQty = oldQty - spinQty

            if oldQty < spinQty:
                QMessageBox.warning(self, "Alert", f"The Quantity you entered exceeds. Please enter less than or "
                                                   f"equal to {oldQty}")
                pickedQty.clear()
                return

            if oldQty == spinQty:
                self.mydb = mysql.connector.connect(**DB_configuration)
                mycursor = self.mydb.cursor()
                sql = "DELETE FROM items WHERE equipment = %s;"
                val = (equipment,)
                mycursor.execute(sql, val)
                self.mydb.commit()

                equipments.clear()
                items.clear()
                pickedQty.clear()

                addremove_item.radioButtonUpdateInventoryAdditem.setAutoExclusive(False)
                addremove_item.radioButtonUpdateInventoryAdditem.setChecked(False)
                addremove_item.radioButtonUpdateInventoryAdditem.setAutoExclusive(True)

                addremove_item.radioButtonUpdateInventoryUpdateItem.setAutoExclusive(False)
                addremove_item.radioButtonUpdateInventoryUpdateItem.setChecked(False)
                addremove_item.radioButtonUpdateInventoryUpdateItem.setAutoExclusive(True)

                addremove_item.radioButtonUpdateInventoryDeleteItem.setAutoExclusive(False)
                addremove_item.radioButtonUpdateInventoryDeleteItem.setChecked(False)
                addremove_item.radioButtonUpdateInventoryDeleteItem.setAutoExclusive(True)

                addremove_item.comboBoxUpdateInventoryEquipment.clear()
                addremove_item.spinBoxUpdateInventoryQty.setValue(0)

                addremove_item.comboBoxUpdateInventoryEquipment.setEnabled(False)
                addremove_item.comboBoxUpdateInventoryEquipment.setEditable(False)
                addremove_item.spinBoxUpdateInventoryQty.setEnabled(False)
                addremove_item.pushButtonUpdateinventoryConfirm.setEnabled(False)

                QMessageBox.information(self, "Deleted",
                                        "The Equipment has been deleted.")
                return

            self.mydb = mysql.connector.connect(**DB_configuration)
            mycursor = self.mydb.cursor()
            sql = "UPDATE items SET quantity = %s WHERE equipment = %s;"
            val = (newQty, equipment)
            mycursor.execute(sql, val)
            self.mydb.commit()

            equipments.clear()
            items.clear()
            pickedQty.clear()

            addremove_item.radioButtonUpdateInventoryAdditem.setAutoExclusive(False)
            addremove_item.radioButtonUpdateInventoryAdditem.setChecked(False)
            addremove_item.radioButtonUpdateInventoryAdditem.setAutoExclusive(True)

            addremove_item.radioButtonUpdateInventoryUpdateItem.setAutoExclusive(False)
            addremove_item.radioButtonUpdateInventoryUpdateItem.setChecked(False)
            addremove_item.radioButtonUpdateInventoryUpdateItem.setAutoExclusive(True)

            addremove_item.radioButtonUpdateInventoryDeleteItem.setAutoExclusive(False)
            addremove_item.radioButtonUpdateInventoryDeleteItem.setChecked(False)
            addremove_item.radioButtonUpdateInventoryDeleteItem.setAutoExclusive(True)

            addremove_item.comboBoxUpdateInventoryEquipment.clear()
            addremove_item.spinBoxUpdateInventoryQty.setValue(0)

            addremove_item.comboBoxUpdateInventoryEquipment.setEnabled(False)
            addremove_item.comboBoxUpdateInventoryEquipment.setEditable(False)
            addremove_item.spinBoxUpdateInventoryQty.setEnabled(False)
            addremove_item.pushButtonUpdateinventoryConfirm.setEnabled(False)

            QMessageBox.information(self, "Updated", "The Item Quantity has been reduced.")


# IN ITEM WINDOW -
class InItemWindow(Ui_initemWindow, QMainWindow):

    def __init__(self):

        super(InItemWindow, self).__init__()
        self.setupUi(self)

        self.pushButtonInSubmit.clicked.connect(self.record_db)
        self.pushButtonInBack.clicked.connect(self.main)

    # BACK TO MAIN WINDOW
    def main(self):

        main.tableWidget.setRowCount(0)

        main_equipments.clear()

        # MYSQL QUERY - APPEND TO EQUIPMENTS LIST
        self.mydb = mysql.connector.connect(**DB_configuration)
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT equipment, quantity FROM items;")

        for item in mycursor:
            main_equipments.append(item)

        print(main_equipments)

        # ADD EQUIPMENT TO TABLE
        main.tableWidget.setRowCount(0)
        row = 0
        main.tableWidget.setRowCount(len(main_equipments))
        for item in main_equipments:
            main.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(item[0])))
            main.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(item[1])))
            row = row + 1

        # -----------------------------------------------------------------------------------------------------

        main_records.clear()

        # MYSQL QUERY - APPEND TO RECORDS LIST
        self.mydb = mysql.connector.connect(**DB_configuration)
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT name, borrowers_num, item, date_out, date_in  FROM borrowers;")

        for record in mycursor:
            main_records.append(record)

        print(main_records)

        # ADD EQUIPMENT TO TABLE
        main.tableWidget_2.setRowCount(0)
        row = 0
        main.tableWidget_2.setRowCount(len(main_records))
        for b_record in main_records:
            main.tableWidget_2.setItem(row, 0, QtWidgets.QTableWidgetItem(str(b_record[0])))
            main.tableWidget_2.setItem(row, 1, QtWidgets.QTableWidgetItem(str(b_record[1])))
            main.tableWidget_2.setItem(row, 2, QtWidgets.QTableWidgetItem(str(b_record[2])))
            main.tableWidget_2.setItem(row, 3, QtWidgets.QTableWidgetItem(str(b_record[3])))
            main.tableWidget_2.setItem(row, 4, QtWidgets.QTableWidgetItem(str(b_record[4])))

            row = row + 1

        # -----------------------------------------------------------------------------------------------------

        existing_borrowers_id.clear()
        main.comboBoxMainRecords.clear()
        main.comboBoxMainRecords.addItem("---ALL BORROWERS---")

        # MYSQL QUERY - APPEND TO existing_borrowers_id LIST
        self.mydb = mysql.connector.connect(**DB_configuration)
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT borrowers_num FROM borrowers;")

        for borrower_id in mycursor:
            existing_borrowers_id.append(borrower_id)

        ids = list(dict.fromkeys(existing_borrowers_id))
        for b_id in ids:
            main.comboBoxMainRecords.addItems(b_id)

        print("EXISTING BORROWERS ID")
        print(existing_borrowers_id)

        # -----------------------------------------------------------------------------------------------------

        in_item.close()
        main.show()

    def record_db(self):
        picked_id = self.comboInOutExistingborrowersinfo.currentText()
        entered_item = self.lineEditInIteminfo.text()

        if self.comboInOutExistingborrowersinfo.currentIndex() == 0:
            QMessageBox.warning(self, "Error", "Please choose Borrowers ID Number.")
            return

        # -----------------------------------------------------------------------------------------------------

        # MYSQL QUERY - APPEND TO PICKED QTY LIST
        self.mydb = mysql.connector.connect(**DB_configuration)
        mycursor = self.mydb.cursor()
        sql = "SELECT borrowers_num, date_out item FROM borrowers WHERE borrowers_num = %s AND item = %s AND date_in = %s;"
        val = (picked_id, entered_item, "item-out",)
        mycursor.execute(sql, val)

        for valid_item in mycursor:
            check_item_info.append(valid_item)

        print("Valid Item Info")
        print(check_item_info)

        # -----------------------------------------------------------------------------------------------------

        if check_item_info == []:

            self.lineEditInIteminfo.clear()

            check_item_info.clear()

            QMessageBox.warning(self, "Error", "The Borrower and Equipment doesn't match in any Records. Please re-check the info entered.")
            return

        try:
            equip_code = entered_item
            split_code = equip_code.split("/", 1)

            final_code = split_code[1]
            print(final_code)
        except:
            self.lineEditOutIteminfo.clear()

            check_borrower_info.clear()
            check_item_info.clear()
            check_item_qty.clear()

            QMessageBox.warning(self, "Error", "Invalid Item Code.")
            return

        # -------------------------------------------------------------------------------------------------------------
        check_item_qty.clear()

        # MYSQL QUERY - APPEND TO PICKED QTY LIST
        self.mydb = mysql.connector.connect(**DB_configuration)
        mycursor = self.mydb.cursor()
        sql = "SELECT quantity FROM items WHERE equipment = %s;"
        val = (final_code,)
        mycursor.execute(sql, val)

        for valid_qty in mycursor:
            check_item_qty.append(valid_qty[0])

        print("Check Item Qty")
        print(check_item_qty)

        # -----------------------------------------------------------------------------------------------------

        self.mydb = mysql.connector.connect(**DB_configuration)
        mycursor = self.mydb.cursor()
        sql = "UPDATE borrowers SET date_in = %s WHERE item = %s AND date_out = %s;"
        val = (date_today, entered_item, check_item_info[0][1])
        mycursor.execute(sql, val)

        self.mydb.commit()

        # -------------------------------------------------------------------------------------------------------------

        old_qty = check_item_qty[0]
        new_qty = old_qty + 1

        self.mydb = mysql.connector.connect(**DB_configuration)
        mycursor = self.mydb.cursor()
        sql = "UPDATE items SET quantity = %s WHERE equipment = %s;"
        val = (new_qty, final_code)
        mycursor.execute(sql, val)

        self.mydb.commit()

        check_item_info.clear()
        check_item_qty.clear()

        self.comboInOutExistingborrowersinfo.setCurrentIndex(0)
        self.lineEditInIteminfo.clear()

        QMessageBox.information(self, "Success", "The Borrowers record has been updated, and the Equipment has been returned.")


# OUT ITEM WINDOW -
class OutItemWindow(Ui_outitemWindow, QMainWindow):

    def __init__(self):

        super(OutItemWindow, self).__init__()
        self.setupUi(self)

        self.radioButtonOutNewborrower.clicked.connect(self.setup_new_borrower)
        self.radioButtonOutExistingborrower.clicked.connect(self.setup_exist_borrower)

        self.pushButtonOutSubmit.clicked.connect(self.record_db)
        self.pushButtonOutBack.clicked.connect(self.main)

    # BACK TO MAIN WINDOW
    def main(self):

        main.tableWidget.setRowCount(0)

        main_equipments.clear()

        # MYSQL QUERY - APPEND TO EQUIPMENTS LIST
        self.mydb = mysql.connector.connect(**DB_configuration)
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT equipment, quantity FROM items;")

        for item in mycursor:
            main_equipments.append(item)

        print(main_equipments)

        # ADD EQUIPMENT TO TABLE
        main.tableWidget.setRowCount(0)
        row = 0
        main.tableWidget.setRowCount(len(main_equipments))
        for item in main_equipments:
            main.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(item[0])))
            main.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(item[1])))
            row = row + 1

        # -----------------------------------------------------------------------------------------------------

        main_records.clear()

        # MYSQL QUERY - APPEND TO RECORDS LIST
        self.mydb = mysql.connector.connect(**DB_configuration)
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT name, borrowers_num, item, date_out, date_in  FROM borrowers;")

        for record in mycursor:
            main_records.append(record)

        print(main_records)

        # ADD EQUIPMENT TO TABLE
        main.tableWidget_2.setRowCount(0)
        row = 0
        main.tableWidget_2.setRowCount(len(main_records))
        for b_record in main_records:
            main.tableWidget_2.setItem(row, 0, QtWidgets.QTableWidgetItem(str(b_record[0])))
            main.tableWidget_2.setItem(row, 1, QtWidgets.QTableWidgetItem(str(b_record[1])))
            main.tableWidget_2.setItem(row, 2, QtWidgets.QTableWidgetItem(str(b_record[2])))
            main.tableWidget_2.setItem(row, 3, QtWidgets.QTableWidgetItem(str(b_record[3])))
            main.tableWidget_2.setItem(row, 4, QtWidgets.QTableWidgetItem(str(b_record[4])))

            row = row + 1

        # -----------------------------------------------------------------------------------------------------

        existing_borrowers_id.clear()
        main.comboBoxMainRecords.clear()
        main.comboBoxMainRecords.addItem("---ALL BORROWERS---")

        # MYSQL QUERY - APPEND TO existing_borrowers_id LIST
        self.mydb = mysql.connector.connect(**DB_configuration)
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT borrowers_num FROM borrowers;")

        for borrower_id in mycursor:
            existing_borrowers_id.append(borrower_id)

        ids = list(dict.fromkeys(existing_borrowers_id))
        for b_id in ids:
            main.comboBoxMainRecords.addItems(b_id)

        print("EXISTING BORROWERS ID")
        print(existing_borrowers_id)

        # -----------------------------------------------------------------------------------------------------

        out_item.close()
        main.show()

    def setup_new_borrower(self):

        self.spinBoxOutStudentNumber.setEnabled(True)
        self.comboBoxBorrowerName.setEnabled(True)
        self.comboBoxBorrowerName.setEditable(True)
        self.lineEditOutIteminfo.setEnabled(True)
        self.pushButtonOutSubmit.setEnabled(True)

        self.comboBoxBorrowerName.clear()
        self.lineEditOutIteminfo.clear()
        self.spinBoxOutStudentNumber.setValue(0)
        self.comboBoxBorrowerName.addItem("---Type borrowers Full Name---")

        existing_borrowers_name.clear()
        existing_borrowers_info.clear()
        existing_borrowers_id.clear()
        out_items.clear()

        check_borrower_info.clear()
        check_item_info.clear()
        check_item_qty.clear()

        # ------------------------------------------------------------

        # MYSQL QUERY - APPEND TO existing_borrowers_name LIST
        self.mydb = mysql.connector.connect(**DB_configuration)
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT name FROM borrowers;")

        for borrower in mycursor:
            existing_borrowers_name.append(borrower)

        names = list(dict.fromkeys(existing_borrowers_name))
        for name in names:
            self.comboBoxBorrowerName.addItems(name)

        print("EXISTING BORROWERS NAME")
        print(existing_borrowers_name)

        # ------------------------------------------------------------

        # MYSQL QUERY - APPEND TO existing_borrowers_info LIST
        self.mydb = mysql.connector.connect(**DB_configuration)
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT name, borrowers_num FROM borrowers;")

        for borrower in mycursor:
            existing_borrowers_info.append(borrower)

        print("EXISTING BORROWERS INFO")
        print(existing_borrowers_info)

        # ------------------------------------------------------------

        # MYSQL QUERY - APPEND TO existing_borrowers_id LIST
        self.mydb = mysql.connector.connect(**DB_configuration)
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT borrowers_num FROM borrowers;")

        for borrower_id in mycursor:
            existing_borrowers_id.append(borrower_id)

        print("EXISTING BORROWERS ID")
        print(existing_borrowers_id)

        # ------------------------------------------------------------

        # MYSQL QUERY - APPEND TO PICKED QTY LIST
        self.mydb = mysql.connector.connect(**DB_configuration)
        mycursor = self.mydb.cursor()
        sql = "SELECT item FROM borrowers WHERE date_in = %s;"
        val = ("item-out",)
        mycursor.execute(sql, val)

        for out_item in mycursor:
            out_items.append(out_item)

        print("OUT ITEMS")
        print(out_items)

    def setup_exist_borrower(self):

        self.spinBoxOutStudentNumber.setEnabled(True)
        self.comboBoxBorrowerName.setEnabled(True)
        self.comboBoxBorrowerName.setEditable(False)
        self.lineEditOutIteminfo.setEnabled(True)
        self.pushButtonOutSubmit.setEnabled(True)

        self.spinBoxOutStudentNumber.setValue(0)
        self.lineEditOutIteminfo.clear()
        self.comboBoxBorrowerName.clear()
        self.comboBoxBorrowerName.addItem("---Choose borrowers Name---")

        existing_borrowers_name.clear()
        existing_borrowers_info.clear()
        existing_borrowers_id.clear()
        out_items.clear()

        check_borrower_info.clear()
        check_item_info.clear()
        check_item_qty.clear()

        # ------------------------------------------------------------

        # MYSQL QUERY - APPEND TO existing_borrowers_name LIST
        self.mydb = mysql.connector.connect(**DB_configuration)
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT name FROM borrowers;")

        for borrower in mycursor:
            existing_borrowers_name.append(borrower)

        names = list(dict.fromkeys(existing_borrowers_name))
        for name in names:
            self.comboBoxBorrowerName.addItems(name)

        print("EXISTING BORROWERS NAME")
        print(existing_borrowers_name)

        # ------------------------------------------------------------

        # MYSQL QUERY - APPEND TO existing_borrowers_info LIST
        self.mydb = mysql.connector.connect(**DB_configuration)
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT name, borrowers_num FROM borrowers;")

        for borrower in mycursor:
            existing_borrowers_info.append(borrower)

        print("EXISTING BORROWERS INFO")
        print(existing_borrowers_info)

        # ------------------------------------------------------------

        # MYSQL QUERY - APPEND TO existing_borrowers_id LIST
        self.mydb = mysql.connector.connect(**DB_configuration)
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT borrowers_num FROM borrowers;")

        for borrower_id in mycursor:
            existing_borrowers_id.append(borrower_id[0])

        print("EXISTING BORROWERS ID")
        print(existing_borrowers_id)

        # ------------------------------------------------------------

        # MYSQL QUERY - APPEND TO PICKED QTY LIST
        self.mydb = mysql.connector.connect(**DB_configuration)
        mycursor = self.mydb.cursor()
        sql = "SELECT item FROM borrowers WHERE date_in = %s;"
        val = ("item-out",)
        mycursor.execute(sql, val)

        for out_item in mycursor:
            out_items.append(out_item)

        print("OUT ITEMS")
        print(out_items)

    def record_db(self):

        full_name = self.comboBoxBorrowerName.currentText()
        id_num = self.spinBoxOutStudentNumber.value()
        student_id = f"TUP-C {id_num}"
        item_code = self.lineEditOutIteminfo.text()
        date_out = date_today

        if self.radioButtonOutNewborrower.isChecked() == True:

            if self.comboBoxBorrowerName.currentIndex() == 0:
                QMessageBox.warning(self, "Error", "Please enter Borrowers name.")
                return

            if self.lineEditOutIteminfo.text() == "":
                QMessageBox.warning(self, "Error", "Please enter Item Code")
                return

            if self.spinBoxOutStudentNumber.value() == 0:
                QMessageBox.warning(self, "Error", "Please enter Borrowers ID Number")
                return

            for i in range(len(existing_borrowers_id)):
                if existing_borrowers_id[i][0] == student_id:
                    self.spinBoxOutStudentNumber.setValue(0)

                    QMessageBox.warning(self, "Error", "The Borrower's ID Number already exist in the Records.")
                    return

            for i in range(len(out_items)):
                if out_items[i][0] == item_code:
                    self.lineEditOutIteminfo.clear()

                    QMessageBox.warning(self, "Error",
                                        "The Equipment you entered is already out. Please enter another Item.")
                    return

            for i in range(len(existing_borrowers_info)):
                if existing_borrowers_info[i][0] == full_name and existing_borrowers_info[i][1] == student_id:
                    self.radioButtonOutExistingborrower.setAutoExclusive(False)
                    self.radioButtonOutExistingborrower.setChecked(False)
                    self.radioButtonOutExistingborrower.setAutoExclusive(True)

                    self.radioButtonOutNewborrower.setAutoExclusive(False)
                    self.radioButtonOutNewborrower.setChecked(False)
                    self.radioButtonOutNewborrower.setAutoExclusive(True)

                    self.spinBoxOutStudentNumber.setEnabled(False)
                    self.comboBoxBorrowerName.setEnabled(False)
                    self.comboBoxBorrowerName.setEditable(False)
                    self.lineEditOutIteminfo.setEnabled(False)
                    self.pushButtonOutSubmit.setEnabled(False)

                    self.spinBoxOutStudentNumber.setValue(0)
                    self.comboBoxBorrowerName.clear()
                    self.lineEditOutIteminfo.clear()

                    QMessageBox.warning(self, "Error",
                                        "The Borrower has already a record. Please choose exisiting borrower instead.")
                    return

            try:
                equip_code = item_code
                split_code = equip_code.split("/", 1)

                final_code = split_code[1]
                print(final_code)
            except:
                self.lineEditOutIteminfo.clear()

                check_borrower_info.clear()
                check_item_info.clear()
                check_item_qty.clear()

                QMessageBox.warning(self, "Error", "Invalid Item Code.")
                return

            # -----------------------------------------------------------------------------------------------------

            # MYSQL QUERY - APPEND TO PICKED QTY LIST
            self.mydb = mysql.connector.connect(**DB_configuration)
            mycursor = self.mydb.cursor()
            sql = "SELECT equipment FROM items WHERE equipment = %s;"
            val = (final_code,)
            mycursor.execute(sql, val)

            for valid_item in mycursor:
                check_item_info.append(valid_item[0])

            print("Valid Item Info")
            print(check_item_info)

            if check_item_info == []:
                self.lineEditOutIteminfo.clear()

                check_borrower_info.clear()
                check_item_info.clear()
                check_item_qty.clear()

                QMessageBox.warning(self, "Error", "Equipment not found in the Inventory.")
                return

            # -----------------------------------------------------------------------------------------------------

            # MYSQL QUERY - APPEND TO PICKED QTY LIST
            self.mydb = mysql.connector.connect(**DB_configuration)
            mycursor = self.mydb.cursor()
            sql = "SELECT quantity FROM items WHERE equipment = %s;"
            val = (final_code,)
            mycursor.execute(sql, val)

            for valid_qty in mycursor:
                check_item_qty.append(valid_qty[0])

            print("Valid Item Qty")
            print(check_item_qty)

            valid_item_qty = check_item_qty[0]

            if valid_item_qty == 0:
                self.lineEditOutIteminfo.clear()

                check_borrower_info.clear()
                check_item_info.clear()
                check_item_qty.clear()
                QMessageBox.warning(self, "Error", "The Equipments quantity is now 0.")
                return

            # -----------------------------------------------------------------------------------------------------

            self.mydb = mysql.connector.connect(**DB_configuration)
            mycursor = self.mydb.cursor()

            sql = "INSERT INTO borrowers (name, borrowers_num, item, date_out, date_in) VALUES (%s,%s,%s,%s,%s);"
            val = (full_name, student_id, item_code, date_out, "item-out")
            mycursor.execute(sql, val)

            self.mydb.commit()

            # -----------------------------------------------------------------------------------------------------
            new_valid_item_qty = valid_item_qty - 1
            print(f"New Equipment Qty = {new_valid_item_qty}")

            self.mydb = mysql.connector.connect(**DB_configuration)
            mycursor = self.mydb.cursor()
            sql = "UPDATE items SET quantity = %s WHERE equipment = %s;"
            val = (new_valid_item_qty, final_code)
            mycursor.execute(sql, val)

            self.mydb.commit()

            # -----------------------------------------------------------------------------------------------------

            check_borrower_info.clear()
            check_item_info.clear()
            check_item_qty.clear()

            self.radioButtonOutExistingborrower.setAutoExclusive(False)
            self.radioButtonOutExistingborrower.setChecked(False)
            self.radioButtonOutExistingborrower.setAutoExclusive(True)

            self.radioButtonOutNewborrower.setAutoExclusive(False)
            self.radioButtonOutNewborrower.setChecked(False)
            self.radioButtonOutNewborrower.setAutoExclusive(True)

            self.spinBoxOutStudentNumber.setEnabled(False)
            self.comboBoxBorrowerName.setEnabled(False)
            self.comboBoxBorrowerName.setEditable(False)
            self.lineEditOutIteminfo.setEnabled(False)
            self.pushButtonOutSubmit.setEnabled(False)

            self.spinBoxOutStudentNumber.setValue(0)
            self.comboBoxBorrowerName.clear()
            self.lineEditOutIteminfo.clear()

            QMessageBox.information(self, "Recorded",
                                    "The Borrowers info has been recorded, and the Equipment has been out.")
            return

        if self.radioButtonOutExistingborrower.isChecked() == True:
            if self.comboBoxBorrowerName.currentIndex() == 0:
                QMessageBox.warning(self, "Error", "Please choose Borrowers name.")
                return

            if self.lineEditOutIteminfo.text() == "":
                QMessageBox.warning(self, "Error", "Please enter Item Code")

                return

            if self.spinBoxOutStudentNumber.value() == 0:
                QMessageBox.warning(self, "Error", "Please enter Borrowers ID Number")
                return

            if f"TUP-C {id_num}" not in existing_borrowers_id:
                QMessageBox.warning(self, "Error",
                                    "The Borrower's ID doesn't exist in the Records. Please choose new borrower "
                                    "instead.")
                return

            check_borrower_info.clear()

            # MYSQL QUERY - APPEND TO PICKED QTY LIST
            self.mydb = mysql.connector.connect(**DB_configuration)
            mycursor = self.mydb.cursor()
            sql = "SELECT name, borrowers_num FROM borrowers WHERE name = %s AND borrowers_num = %s;"
            val = (full_name, f"TUP-C {id_num}",)
            mycursor.execute(sql, val)

            for valid_borrower in mycursor:
                check_borrower_info.append(valid_borrower)

            print("Valid Borrower")
            print(check_borrower_info)

            if check_borrower_info == []:
                QMessageBox.warning(self, "Error",
                                    "The Borrower's Info doesn't match in any Records. Please choose new borrower "
                                    "instead.")
                return

            for i in range(len(out_items)):
                if out_items[i][0] == item_code:
                    self.lineEditOutIteminfo.clear()

                    QMessageBox.warning(self, "Error",
                                        "The Equipment you entered is already out. Please enter another Item.")
                    return

            if check_borrower_info != []:
                try:
                    equip_code = item_code
                    split_code = equip_code.split("/", 1)

                    final_code = split_code[1]
                    print(final_code)
                except:
                    self.lineEditOutIteminfo.clear()

                    check_borrower_info.clear()
                    check_item_info.clear()
                    check_item_qty.clear()

                    QMessageBox.warning(self, "Error", "Invalid Item Code.")
                    return

                # -----------------------------------------------------------------------------------------------------

                # MYSQL QUERY - APPEND TO PICKED QTY LIST
                self.mydb = mysql.connector.connect(**DB_configuration)
                mycursor = self.mydb.cursor()
                sql = "SELECT equipment FROM items WHERE equipment = %s;"
                val = (final_code,)
                mycursor.execute(sql, val)

                for valid_item in mycursor:
                    check_item_info.append(valid_item[0])

                print("Valid Item Info")
                print(check_item_info)

                if check_item_info == []:
                    self.lineEditOutIteminfo.clear()

                    check_borrower_info.clear()
                    check_item_info.clear()
                    check_item_qty.clear()

                    QMessageBox.warning(self, "Error", "Equipment not found in the Inventory.")
                    return

                # -----------------------------------------------------------------------------------------------------

                # MYSQL QUERY - APPEND TO PICKED QTY LIST
                self.mydb = mysql.connector.connect(**DB_configuration)
                mycursor = self.mydb.cursor()
                sql = "SELECT quantity FROM items WHERE equipment = %s;"
                val = (final_code,)
                mycursor.execute(sql, val)

                for valid_qty in mycursor:
                    check_item_qty.append(valid_qty[0])

                print("Valid Item Qty")
                print(check_item_qty)

                valid_item_qty = check_item_qty[0]

                if valid_item_qty == 0:
                    self.lineEditOutIteminfo.clear()

                    check_borrower_info.clear()
                    check_item_info.clear()
                    check_item_qty.clear()
                    QMessageBox.warning(self, "Error", "The Equipments quantity is now 0.")
                    return

                # -----------------------------------------------------------------------------------------------------

                self.mydb = mysql.connector.connect(**DB_configuration)
                mycursor = self.mydb.cursor()

                sql = "INSERT INTO borrowers (name, borrowers_num, item, date_out, date_in) VALUES (%s,%s,%s,%s,%s);"
                val = (full_name, student_id, item_code, date_out, "item-out")
                mycursor.execute(sql, val)

                self.mydb.commit()

                # -----------------------------------------------------------------------------------------------------
                new_valid_item_qty = valid_item_qty - 1

                self.mydb = mysql.connector.connect(**DB_configuration)
                mycursor = self.mydb.cursor()
                sql = "UPDATE items SET quantity = %s WHERE equipment = %s;"
                val = (new_valid_item_qty, final_code)
                mycursor.execute(sql, val)

                self.mydb.commit()

                # -----------------------------------------------------------------------------------------------------

                check_borrower_info.clear()
                check_item_info.clear()
                check_item_qty.clear()

                self.radioButtonOutExistingborrower.setAutoExclusive(False)
                self.radioButtonOutExistingborrower.setChecked(False)
                self.radioButtonOutExistingborrower.setAutoExclusive(True)

                self.radioButtonOutNewborrower.setAutoExclusive(False)
                self.radioButtonOutNewborrower.setChecked(False)
                self.radioButtonOutNewborrower.setAutoExclusive(True)

                self.spinBoxOutStudentNumber.setEnabled(False)
                self.comboBoxBorrowerName.setEnabled(False)
                self.comboBoxBorrowerName.setEditable(False)
                self.lineEditOutIteminfo.setEnabled(False)
                self.pushButtonOutSubmit.setEnabled(False)

                self.spinBoxOutStudentNumber.setValue(0)
                self.comboBoxBorrowerName.clear()
                self.lineEditOutIteminfo.clear()

                QMessageBox.information(self, "Recorded",
                                        "The Borrowers info has been recorded, and the Equipment has been out.")
                return


# QR CODE GENERATOR WINDOW - DONE - NEED TO CHECK
class QrCodeGeneratorWindow(Ui_qrcodegeneratorWindow, QMainWindow):

    def __init__(self):

        super(QrCodeGeneratorWindow, self).__init__()
        self.setupUi(self)

        self.pushButtonQrcodeBack.clicked.connect(self.main)
        self.pushButtonQrcodeGenerate.clicked.connect(self.generate_qr)

    # BACK TO MAIN WINDOW
    def main(self):

        main.tableWidget.setRowCount(0)

        main_equipments.clear()

        # MYSQL QUERY - APPEND TO EQUIPMENTS LIST
        self.mydb = mysql.connector.connect(**DB_configuration)
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT equipment, quantity FROM items;")

        for item in mycursor:
            main_equipments.append(item)

        print(main_equipments)

        # ADD EQUIPMENT TO TABLE
        main.tableWidget.setRowCount(0)
        row = 0
        main.tableWidget.setRowCount(len(main_equipments))
        for item in main_equipments:
            main.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(item[0])))
            main.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(item[1])))
            row = row + 1

        # -----------------------------------------------------------------------------------------------------

        main_records.clear()

        # MYSQL QUERY - APPEND TO RECORDS LIST
        self.mydb = mysql.connector.connect(**DB_configuration)
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT name, borrowers_num, item, date_out, date_in  FROM borrowers;")

        for record in mycursor:
            main_records.append(record)

        print(main_records)

        # ADD EQUIPMENT TO TABLE
        main.tableWidget_2.setRowCount(0)
        row = 0
        main.tableWidget_2.setRowCount(len(main_records))
        for b_record in main_records:
            main.tableWidget_2.setItem(row, 0, QtWidgets.QTableWidgetItem(str(b_record[0])))
            main.tableWidget_2.setItem(row, 1, QtWidgets.QTableWidgetItem(str(b_record[1])))
            main.tableWidget_2.setItem(row, 2, QtWidgets.QTableWidgetItem(str(b_record[2])))
            main.tableWidget_2.setItem(row, 3, QtWidgets.QTableWidgetItem(str(b_record[3])))
            main.tableWidget_2.setItem(row, 4, QtWidgets.QTableWidgetItem(str(b_record[4])))

            row = row + 1

        # -----------------------------------------------------------------------------------------------------

        existing_borrowers_id.clear()
        main.comboBoxMainRecords.clear()
        main.comboBoxMainRecords.addItem("---ALL BORROWERS---")

        # MYSQL QUERY - APPEND TO existing_borrowers_id LIST
        self.mydb = mysql.connector.connect(**DB_configuration)
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT borrowers_num FROM borrowers;")

        for borrower_id in mycursor:
            existing_borrowers_id.append(borrower_id)

        ids = list(dict.fromkeys(existing_borrowers_id))
        for b_id in ids:
            main.comboBoxMainRecords.addItems(b_id)

        print("EXISTING BORROWERS ID")
        print(existing_borrowers_id)

        # -----------------------------------------------------------------------------------------------------

        qr_code_generator.close()
        main.show()

    def generate_qr(self):
        item_code = self.comboBoxQrcodeItemCode.currentText()
        equipment_qty = self.spinBoxQrcodeEnd.value()
        number_start = self.spinBoxQrcodeStart.value()
        number_end = self.spinBoxQrcodeEnd.value() + 1

        if self.comboBoxQrcodeItemCode.currentIndex() == 0:
            QMessageBox.warning(self, "Error", "Please enter equipment you want to generate a qr code.")
            return

        # QR code save path / file directory
        home = os.path.expanduser('~')
        location = os.path.join(home, 'Pictures')

        pickedQty.clear()

        # MYSQL QUERY - APPEND TO PICKED QTY LIST
        self.mydb = mysql.connector.connect(**DB_configuration)
        mycursor = self.mydb.cursor()
        sql = "SELECT quantity FROM items WHERE equipment = %s;"
        val = (item_code,)
        mycursor.execute(sql, val)

        for pQty in mycursor:
            pickedQty.append(pQty)

        print("pickedqty")
        print(pickedQty[0][0])

        print("spinbox qty")
        print(equipment_qty)

        oldQty = pickedQty[0][0]
        spinQtyEnd = equipment_qty


        if oldQty < spinQtyEnd or oldQty < number_start:
            self.spinBoxQrcodeStart.setValue(1)
            self.spinBoxQrcodeEnd.setValue(oldQty)
            QMessageBox.warning(self, "Alert", f"The Quantity you entered exceeds. {item_code} has {oldQty} quantity. "
                                               f"Please enter less than or "
                                               f"equal to {oldQty}")
            pickedQty.clear()
            return

        if self.comboBoxQrcodeItemCode.currentIndex() != 0:
            check_main_location = os.path.join(location, f"TUP-C_UITC_QR_Code")
            if not os.path.exists(check_main_location):
                os.makedirs(check_main_location)

                check_sub_location = os.path.join(check_main_location, f"{item_code}")

                if not os.path.exists(check_sub_location):
                    os.makedirs(check_sub_location)

                    for Numbering in range(number_start, number_end):
                        qr = qrcode.make(f"{Numbering}/{item_code}")
                        qr.save(os.path.join(check_sub_location, f"Number {Numbering} {item_code}.png"))

                    self.comboBoxQrcodeItemCode.setCurrentIndex(0)
                    self.spinBoxQrcodeStart.setValue(1)
                    self.spinBoxQrcodeEnd.setValue(1)

                    QMessageBox.information(self, "Success", "QR Code has been Successfully Generated.")
                    return

                else:
                    exist_sub_loc = os.path.join(check_main_location, f"{item_code}")

                    for Numbering in range(number_start, number_end):
                        qr = qrcode.make(f"{Numbering}/{item_code}")
                        qr.save(os.path.join(exist_sub_loc, f"Number {Numbering} {item_code}.png"))

                    self.comboBoxQrcodeItemCode.setCurrentIndex(0)
                    self.spinBoxQrcodeStart.setValue(1)
                    self.spinBoxQrcodeEnd.setValue(1)

                    QMessageBox.information(self, "Success", "QR Code has been Successfully Generated.")
                    return

            else:
                check_sub_location = os.path.join(check_main_location, f"{item_code}")

                if not os.path.exists(check_sub_location):
                    os.makedirs(check_sub_location)

                    for Numbering in range(number_start, number_end):
                        qr = qrcode.make(f"{Numbering}/{item_code}")
                        qr.save(os.path.join(check_sub_location, f"Number {Numbering} {item_code}.png"))

                    self.comboBoxQrcodeItemCode.setCurrentIndex(0)
                    self.spinBoxQrcodeStart.setValue(1)
                    self.spinBoxQrcodeEnd.setValue(1)

                    QMessageBox.information(self, "Success", "QR Code has been Successfully Generated.")
                    return

                else:
                    exist_sub_loc = os.path.join(check_main_location, f"{item_code}")

                    for Numbering in range(number_start, number_end):
                        qr = qrcode.make(f"{Numbering}/{item_code}")
                        qr.save(os.path.join(exist_sub_loc, f"Number {Numbering} {item_code}.png"))

                    self.comboBoxQrcodeItemCode.setCurrentIndex(0)
                    self.spinBoxQrcodeStart.setValue(1)
                    self.spinBoxQrcodeEnd.setValue(1)

                    QMessageBox.information(self, "Success", "QR Code has been Successfully Generated.")
                    return


# ABOUT WINDOW - DONE & CHECKED
class AboutWindow(Ui_aboutWindow, QMainWindow):

    def __init__(self):

        super(AboutWindow, self).__init__()
        self.setupUi(self)

        self.AboutBackPushButton.clicked.connect(self.main)
        self.AboutOnlineCVPushButton.clicked.connect(lambda: webbrowser.open('https://johnanthonybataller.netlify.app'))
        self.AboutGithubPushButton.clicked.connect(lambda: webbrowser.open('https://github.com/ja-bataller'))

    # BACK TO MAIN WINDOW
    def main(self):

        main.tableWidget.setRowCount(0)

        main_equipments.clear()

        # MYSQL QUERY - APPEND TO EQUIPMENTS LIST
        self.mydb = mysql.connector.connect(**DB_configuration)
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT equipment, quantity FROM items;")

        for item in mycursor:
            main_equipments.append(item)

        print(main_equipments)

        # ADD EQUIPMENT TO TABLE
        main.tableWidget.setRowCount(0)
        row = 0
        main.tableWidget.setRowCount(len(main_equipments))
        for item in main_equipments:
            main.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(item[0])))
            main.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(item[1])))
            row = row + 1

        # -----------------------------------------------------------------------------------------------------

        main_records.clear()

        # MYSQL QUERY - APPEND TO RECORDS LIST
        self.mydb = mysql.connector.connect(**DB_configuration)
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT name, borrowers_num, item, date_out, date_in  FROM borrowers;")

        for record in mycursor:
            main_records.append(record)

        print(main_records)

        # ADD EQUIPMENT TO TABLE
        main.tableWidget_2.setRowCount(0)
        row = 0
        main.tableWidget_2.setRowCount(len(main_records))
        for b_record in main_records:
            main.tableWidget_2.setItem(row, 0, QtWidgets.QTableWidgetItem(str(b_record[0])))
            main.tableWidget_2.setItem(row, 1, QtWidgets.QTableWidgetItem(str(b_record[1])))
            main.tableWidget_2.setItem(row, 2, QtWidgets.QTableWidgetItem(str(b_record[2])))
            main.tableWidget_2.setItem(row, 3, QtWidgets.QTableWidgetItem(str(b_record[3])))
            main.tableWidget_2.setItem(row, 4, QtWidgets.QTableWidgetItem(str(b_record[4])))

            row = row + 1

        # -----------------------------------------------------------------------------------------------------

        existing_borrowers_id.clear()
        main.comboBoxMainRecords.clear()
        main.comboBoxMainRecords.addItem("---ALL BORROWERS---")

        # MYSQL QUERY - APPEND TO existing_borrowers_id LIST
        self.mydb = mysql.connector.connect(**DB_configuration)
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT borrowers_num FROM borrowers;")

        for borrower_id in mycursor:
            existing_borrowers_id.append(borrower_id)

        ids = list(dict.fromkeys(existing_borrowers_id))
        for b_id in ids:
            main.comboBoxMainRecords.addItems(b_id)

        print("EXISTING BORROWERS ID")
        print(existing_borrowers_id)

        # -----------------------------------------------------------------------------------------------------

        about.close()
        main.show()


# PYQT5
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    index = IndexWindow()
    login = LoginWindow()
    signup = SignupWindow()
    main = MainWindow()
    account_settings = AccountSettingsWindow()
    addremove_item = AddRemoveItemWindow()
    in_item = InItemWindow()
    out_item = OutItemWindow()
    qr_code_generator = QrCodeGeneratorWindow()
    about = AboutWindow()

    index.show()
    login.close()
    signup.close()
    main.close()
    account_settings.close()
    addremove_item.close()

    sys.exit(app.exec())
