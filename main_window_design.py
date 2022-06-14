# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(321, 372)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.information = QtWidgets.QTableWidget(self.centralwidget)
        self.information.setObjectName("information")
        self.information.setColumnCount(0)
        self.information.setRowCount(0)
        self.verticalLayout.addWidget(self.information)
        self.add_person = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.add_person.setFont(font)
        self.add_person.setObjectName("add_person")
        self.verticalLayout.addWidget(self.add_person)
        self.add_transaction = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.add_transaction.setFont(font)
        self.add_transaction.setObjectName("add_transaction")
        self.verticalLayout.addWidget(self.add_transaction)
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.clear.setFont(font)
        self.clear.setObjectName("clear")
        self.verticalLayout.addWidget(self.clear)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Make Your Friends Pay"))
        self.add_person.setText(_translate("MainWindow", "Додати учасника"))
        self.add_transaction.setText(_translate("MainWindow", "Додати транзакцію"))
        self.clear.setText(_translate("MainWindow", "Очистити дані"))
