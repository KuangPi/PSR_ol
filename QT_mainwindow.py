# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PYQT_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(233, 260)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.labelInstruction = QtWidgets.QLabel(self.centralwidget)
        self.labelInstruction.setObjectName("labelInstruction")
        self.verticalLayout.addWidget(self.labelInstruction)
        self.buttonRank = QtWidgets.QPushButton(self.centralwidget)
        self.buttonRank.setObjectName("buttonRank")
        self.verticalLayout.addWidget(self.buttonRank)
        self.buttonFight = QtWidgets.QPushButton(self.centralwidget)
        self.buttonFight.setObjectName("buttonFight")
        self.verticalLayout.addWidget(self.buttonFight)
        self.buttonQuit = QtWidgets.QPushButton(self.centralwidget)
        self.buttonQuit.setObjectName("buttonQuit")
        self.verticalLayout.addWidget(self.buttonQuit)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.buttonRank.clicked.connect(MainWindow.transfer_Rank)
        self.buttonQuit.clicked.connect(MainWindow.exit)
        self.buttonFight.clicked.connect(MainWindow.transfer_Fight)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PSR_ol"))
        self.label.setText(_translate("MainWindow", "Error! "))
        self.labelInstruction.setText(_translate("MainWindow", "What do you want to do? "))
        self.buttonRank.setText(_translate("MainWindow", "See Rank|1|2|3|"))
        self.buttonFight.setText(_translate("MainWindow", "Fight!!!!"))
        self.buttonQuit.setText(_translate("MainWindow", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())