# -*- coding: utf-8 -*-
from multi_selection import Ui_Dialog
from PyQt5.QtWidgets import QApplication, QDialog

class MultiSelectionDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super(MultiSelectionDialog, self).__init__()
        self.setupUi(self)

