# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from ui import Ui_Form
from orderData import OrderData
from order import Order

import xlwt;
import xlrd;
import sys;
#import xlutils;
from xlutils.copy import copy;
from datetime import date,datetime;

# 缺货的数据，以 款号：数量 的方式保存
lackDict = {}

orderData = OrderData()

class mywindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)

    # 导入订单数据
    def importOrderDataButtonPushed(self):
        orderDateFile = QFileDialog.getOpenFileName(self)
        print orderDateFile
        orderData.load(orderDateFile[0]) # orderDataFile为tupple，只取第一个元素


    # 导入宝贝销量数据
    def importGoodSalesDataButtonPushed(self):
        print "ffff"

    def barCodeLineEditReturnPressed(self):
        expNum =  self.barCodeLineEdit.text()
        self.barCodeLineEdit.clear()
        order = orderData.findOrderByExpNum(expNum)
        print order.skuCode
        print order.count

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())