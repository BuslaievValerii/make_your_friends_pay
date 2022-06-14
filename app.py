# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QCheckBox, QTableWidgetItem
from PyQt5 import QtGui
from main_window_design import Ui_MainWindow
from add_person_design import Ui_Dialog_Add_Person
from transaction_design import Ui_Dialog_Transaction
from solver import DebtProblemSolver, SolverException

import sys
import numpy as np


def _message_box(msg_text, title='Помилка'):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setWindowTitle(title)
    msg.setText(msg_text)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec()


class Data():
    __OWED = 'OWED'
    __DEBT = 'DEBT'

    def __init__(self):
        self._people = {}

    @property
    def people(self):
        return list(self._people.keys())

    @property
    def needs(self):
        return list(map(lambda x: self._people[x][Data.__OWED], self.people))

    @property
    def debts(self):
        return list(map(lambda x: self._people[x][Data.__DEBT], self.people))

    def add_person(self, new_person):
        self._people[new_person] = {
            Data.__OWED: 0,
            Data.__DEBT: 0
        }

    def add_transaction(self, person, amount, destination):
        if destination == "OWED":
            self._people[person][Data.__OWED] += amount
        elif destination == "DEBT":
            self._people[person][Data.__DEBT] += amount
        else:
            return False
        return True

    def clear_data(self):
        self._people = {}
    

class AddPersonDialog(QDialog, Ui_Dialog_Add_Person):
    def __init__(self, data:Data):
        super(AddPersonDialog, self).__init__()
        self.setupUi(self)
        self.__data = data

    def accept(self):
        if self.new_person.text() in self.__data.people:
            _message_box("Такий учасник уже існує")
        elif self.new_person.text() == '':
            _message_box("Ім'я учасника не введено")
        else:
            super().accept()


class TransactionDialog(QDialog, Ui_Dialog_Transaction):
    def __init__(self, data:Data):
        super(TransactionDialog, self).__init__()
        self.setupUi(self)
        self.__data = data

    def accept(self):
        try:
            self.total_amount = float(self.amount.text())
        except:
            _message_box('Введіть чисельні дані')
            return
        
        self.people_count = len(self.who_in_debt.selectedItems())
        if self.people_count < 1:
            _message_box('Виберіть хоча б одного учасника зі списку')
            return
        
        self.part_amount = float(self.total_amount / self.people_count)
        super().accept()


class MainWindow(QMainWindow, Ui_MainWindow):               
    def __init__(self, data:Data):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self._data = data
        self._matrix = []

        def on_add_person_click():
            dlg = AddPersonDialog(self._data)
            np.expand_dims
            button = dlg.exec()
            if button == QDialog.Accepted:
                self._data.add_person(dlg.new_person.text())
                self.solve_problem()
                self.rebuild_table()
                    

        self.add_person.clicked.connect(on_add_person_click)

        def on_transaction_click():
            dlg = TransactionDialog(self._data)
            dlg.who_paid.addItems(self._data.people)
            dlg.who_in_debt.addItems(self._data.people)
            button = dlg.exec()
            if button == QDialog.Accepted:
                if not self._data.add_transaction(dlg.who_paid.currentText(), dlg.total_amount, "OWED"):
                    _message_box("Сталася помилка під час внесення даних")
                    return
                for person in dlg.who_in_debt.selectedItems():
                    if not self._data.add_transaction(person.text(), dlg.part_amount, "DEBT"):
                        _message_box("Сталася помилка під час внесення даних")
                        return

                self.solve_problem()
                self.rebuild_table()

        
        self.add_transaction.clicked.connect(on_transaction_click)

        def on_clear_click():
            self.information.setRowCount(0)
            self.information.setColumnCount(0)
            self._data.clear_data()

        self.clear.clicked.connect(on_clear_click)


    def solve_problem(self):
        solver = DebtProblemSolver(self._data.needs, self._data.debts)
        try:
            self._matrix = solver.solve()
        except SolverException as e:
            print(e)
            _message_box("Помилка під час розрахунку результатів")


    def rebuild_table(self):
        self.information.clear()
        self.information.setRowCount(len(self._data.people) + 2)
        self.information.setColumnCount(len(self._data.people) + 2)

        self.information.setItem(0,0,QTableWidgetItem('Учасники'))
        self.information.item(0,0).setBackground(QtGui.QColor(184, 184, 184))

        self.information.setItem(0,len(self._data.people)+1,QTableWidgetItem("Борги"))
        self.information.item(0,len(self._data.people)+1).setBackground(QtGui.QColor(138, 188, 235))

        self.information.setItem(len(self._data.people)+1,0,QTableWidgetItem("Потреби"))
        self.information.item(len(self._data.people)+1,0).setBackground(QtGui.QColor(223, 232, 144))

        # filling vectors of debts and needs
        for i in range(len(self._data.people)):
            self.information.setItem(i+1,0,QTableWidgetItem(self._data.people[i]))
            self.information.item(i+1,0).setBackground(QtGui.QColor(184, 184, 184))
            self.information.setItem(0,i+1,QTableWidgetItem(self._data.people[i]))
            self.information.item(0,i+1).setBackground(QtGui.QColor(184, 184, 184))

            self.information.setItem(i+1,len(self._data.people)+1,QTableWidgetItem(str(self._data.debts[i])))
            self.information.item(i+1,len(self._data.people)+1).setBackground(QtGui.QColor(138, 188, 235))
            self.information.setItem(len(self._data.people)+1,i+1,QTableWidgetItem(str(self._data.needs[i])))
            self.information.item(len(self._data.people)+1,i+1).setBackground(QtGui.QColor(223, 232, 144))

        # fill inside boxes
        for i in range(len(self._data.people)):
            for j in range(len(self._data.people)):
                self.information.setItem(i+1,j+1,QTableWidgetItem(str(self._matrix[i][j])))
                if i != j and self._matrix[i][j] != 0:
                    self.information.item(i+1, j+1).setBackground(QtGui.QColor(124, 235, 170))


def main():
    data = Data()

    app = QApplication(sys.argv)

    window = MainWindow(data)
    window.show()
    
    app.exec()


if __name__ == "__main__":
    main()
    