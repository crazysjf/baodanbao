# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets


# 从PyQt库导入QtWidget通用窗口类
# class mywindow(QtWidgets.QWidget):
#     # 自己建一个mywindows类，以class开头，mywindows是自己的类名，
#     # （QtWidgets.QWidget）是继承QtWidgets.QWidget类方法，
#     def __init__(self):
#         super(mywindow, self).__init__()
#
#
# import sys
#
# app = QtWidgets.QApplication(sys.argv)
# windows = mywindow()
# label = QtWidgets.QLabel(windows)  # 在窗口中绑定label
# label.setText("hello world")
#
# windows.show()
# sys.exit(app.exec_())

from PyQt5 import QtWidgets
from ui import Ui_Form


class mywindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.pushButton.setText("按钮")
    def buttonPushed(self):
        print "asdf"
    def barCodeLineEditReturnPressed(self):
        print self.barCodeLineEdit.text()
        self.barCodeLineEdit.clear()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())