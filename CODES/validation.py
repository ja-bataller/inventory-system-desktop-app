class validation():

    def loginReset(self):
        self.lineEditLoginUsername.clear()
        self.lineEditLoginPassword.clear()

    def signupReset(self):
        self.lineEditSignupFirstname.clear()
        self.lineEditSignupLastname.clear()
        self.lineEditSignupUsername.clear()
        self.lineEditSignupPassword.clear()
        self.lineEditSignupRetypePassword.clear()
        self.radioButtonSignupAdministrator.setAutoExclusive(False);
        self.radioButtonSignupAdministrator.setChecked(False)
        self.radioButtonSignupAdministrator.setAutoExclusive(True)
        self.radioButtonSignupOperator.setAutoExclusive(False);
        self.radioButtonSignupOperator.setChecked(False)
        self.radioButtonSignupOperator.setAutoExclusive(True)
        self.lineEditSignupCode.clear()

    def accountSettingsReset(self):
        self.AccountSettingsOldPasswordLineEdit.clear()
        self.AccountSettingsNewPasswordLineEdit.clear()
        self.AccountSettingsConfirmNewPasswordLineEdit.clear()

    def addremoveItemReset(self):
        self.radioButtonAddremoveAdditem.setAutoExclusive(False);
        self.radioButtonAddremoveAdditem.setChecked(False);
        self.radioButtonAddremoveAdditem.setAutoExclusive(True);

        self.radioButtonAddremoveRemoveitem.setAutoExclusive(False);
        self.radioButtonAddremoveRemoveitem.setChecked(False);
        self.radioButtonAddremoveRemoveitem.setAutoExclusive(True);

        self.comboBoxAddremoveEquipment.setCurrentIndex(0)
        self.comboBoxAddremoveBrand.setCurrentIndex(0)
        self.comboBoxAddremoveModel.setCurrentIndex(0)

        self.radioButtonAdditemNoserial.setAutoExclusive(False);
        self.radioButtonAdditemNoserial.setChecked(False);
        self.radioButtonAdditemNoserial.setAutoExclusive(True);

        self.radioButtonAdditemSerial.setAutoExclusive(False);
        self.radioButtonAdditemSerial.setChecked(False);
        self.radioButtonAdditemSerial.setAutoExclusive(True);

        self.lineEditAddremoveSerial.clear()
        self.lineEditAddremoveSerial.setDisabled(True)
        self.spinBoxAddremoveQty.setValue(1)