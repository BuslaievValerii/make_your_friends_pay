# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Transaction(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(375, 294)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.amount_label = QtWidgets.QLabel(Dialog)
        self.amount_label.setObjectName("amount_label")
        self.gridLayout.addWidget(self.amount_label, 0, 1, 1, 1)
        self.who_in_debt = QtWidgets.QListWidget(Dialog)
        self.who_in_debt.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.who_in_debt.setObjectName("who_in_debt")
        self.gridLayout.addWidget(self.who_in_debt, 3, 0, 1, 2)
        self.who_paid = QtWidgets.QComboBox(Dialog)
        self.who_paid.setObjectName("who_paid")
        self.gridLayout.addWidget(self.who_paid, 1, 0, 1, 1)
        self.amount = QtWidgets.QLineEdit(Dialog)
        self.amount.setObjectName("amount")
        self.gridLayout.addWidget(self.amount, 1, 1, 1, 1)
        self.who_paid_label = QtWidgets.QLabel(Dialog)
        self.who_paid_label.setObjectName("who_paid_label")
        self.gridLayout.addWidget(self.who_paid_label, 0, 0, 1, 1)
        self.who_in_debt_label = QtWidgets.QLabel(Dialog)
        self.who_in_debt_label.setObjectName("who_in_debt_label")
        self.gridLayout.addWidget(self.who_in_debt_label, 2, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.amount_label.setText(_translate("Dialog", "Розмір оплати:"))
        self.who_paid_label.setText(_translate("Dialog", "Хто здійснював оплату:"))
        self.who_in_debt_label.setText(_translate("Dialog", "Хто входить в заборгованість:"))
