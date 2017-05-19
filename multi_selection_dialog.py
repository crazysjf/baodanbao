# -*- coding: utf-8 -*-
from multi_selection import Ui_Dialog
from PyQt5.Qt import *
from PyQt5.QtWidgets import  QApplication, QDialog, QTableWidgetItem

class MultiSelectionDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super(MultiSelectionDialog, self).__init__()
        self.setupUi(self)
        self.tableWidget.setRowCount(3)
        cb = QTableWidgetItem()
        cb.setCheckState(Qt.Checked)
        self.tableWidget.setItem(0,1,cb)

