# -*- coding: utf-8 -*-
from multi_selection import Ui_Dialog
from PyQt5.Qt import *
from PyQt5.QtWidgets import  QApplication, QDialog, QTableWidgetItem

class MultiSelectionDialog(QDialog, Ui_Dialog):
    def __init__(self, items):
        super(MultiSelectionDialog, self).__init__()
        self.setupUi(self)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)

        self.items = items
        self.nrows = len(items)
        self.tableWidget.setRowCount(self.nrows)
        for i in range(0, self.nrows):
            item = items[i]
            cb = QTableWidgetItem()
            cb.setCheckState(Qt.Unchecked)
            self.tableWidget.setItem(i,0,cb)
            self.tableWidget.setItem(i, 1, QTableWidgetItem(item.skuCode))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(item.count))

    def accept(self):
        self.selectedItems = []
        for i in range(0, self.nrows):
            cb = self.tableWidget.item(i, 0)
            if cb.checkState() == Qt.Checked:
                self.selectedItems.append(self.items[i])
        super(MultiSelectionDialog,self).accept()
