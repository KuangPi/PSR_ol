# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PYQT_login.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialogLogin(object):
    def setupUi(self, dialogLogin):
        dialogLogin.setObjectName("dialogLogin")
        dialogLogin.setEnabled(True)
        dialogLogin.resize(237, 252)
        self.verticalLayout = QtWidgets.QVBoxLayout(dialogLogin)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_Username = QtWidgets.QLabel(dialogLogin)
        self.label_Username.setObjectName("label_Username")
        self.verticalLayout.addWidget(self.label_Username)
        self.inputUsername = QtWidgets.QLineEdit(dialogLogin)
        self.inputUsername.setObjectName("inputUsername")
        self.verticalLayout.addWidget(self.inputUsername)
        self.labelPasswrod = QtWidgets.QLabel(dialogLogin)
        self.labelPasswrod.setObjectName("labelPasswrod")
        self.verticalLayout.addWidget(self.labelPasswrod)
        self.inputPassword = QtWidgets.QLineEdit(dialogLogin)
        self.inputPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inputPassword.setObjectName("inputPassword")
        self.verticalLayout.addWidget(self.inputPassword)
        self.input_AlertLabel = QtWidgets.QLabel(dialogLogin)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(252, 0, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 0, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.input_AlertLabel.setPalette(palette)
        self.input_AlertLabel.setText("")
        self.input_AlertLabel.setObjectName("input_AlertLabel")
        self.verticalLayout.addWidget(self.input_AlertLabel)
        self.buttonLogin = QtWidgets.QPushButton(dialogLogin)
        self.buttonLogin.setDefault(False)
        self.buttonLogin.setFlat(False)
        self.buttonLogin.setObjectName("buttonLogin")
        self.verticalLayout.addWidget(self.buttonLogin)
        self.buttonRegister = QtWidgets.QPushButton(dialogLogin)
        self.buttonRegister.setObjectName("buttonRegister")
        self.verticalLayout.addWidget(self.buttonRegister)
        self.buttonCancel = QtWidgets.QPushButton(dialogLogin)
        self.buttonCancel.setObjectName("buttonCancel")
        self.verticalLayout.addWidget(self.buttonCancel)

        self.retranslateUi(dialogLogin)
        self.buttonLogin.clicked.connect(dialogLogin.loginMain)
        self.buttonRegister.clicked.connect(dialogLogin.userRegister)
        self.buttonCancel.clicked.connect(dialogLogin.exit)
        QtCore.QMetaObject.connectSlotsByName(dialogLogin)

    def retranslateUi(self, dialogLogin):
        _translate = QtCore.QCoreApplication.translate
        dialogLogin.setWindowTitle(_translate("dialogLogin", "PSR_ol"))
        self.label_Username.setText(_translate("dialogLogin", "User name: "))
        self.labelPasswrod.setText(_translate("dialogLogin", "Password: "))
        self.buttonLogin.setText(_translate("dialogLogin", "Click me to Login >3<"))
        self.buttonRegister.setText(_translate("dialogLogin", "New? Register here! "))
        self.buttonCancel.setText(_translate("dialogLogin", "Cancel 555"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialogLogin = QtWidgets.QDialog()
    ui = Ui_dialogLogin()
    ui.setupUi(dialogLogin)
    dialogLogin.show()
    sys.exit(app.exec_())
