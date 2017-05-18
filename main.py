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
        # 测试阶段自动载入报表
        file = u"D:/projects/报单宝/销量数据/5.18.xls"
        orderData.load(file)

    # 导入订单数据
    def importOrderDataButtonPushed(self):

        orderDateFile = QFileDialog.getOpenFileName(self)
        print orderDateFile[0].encode('utf-8')
        orderData.load(orderDateFile[0]) # orderDataFile为tupple，只取第一个元素


    # 导入宝贝销量数据
    def importGoodSalesDataButtonPushed(self):
        print "ffff"

    def barCodeLineEditReturnPressed(self):
        expNum =  self.barCodeLineEdit.text()
        self.barCodeLineEdit.clear()
        order = orderData.findOrderByExpNum(expNum)
        items = order.items
        for i in items:
            print i.skuCode, i.count
            c =  int(i.count)
            if lackDict.has_key(i.skuCode):
                lackDict[i.skuCode] = lackDict[i.skuCode] + c
            else:
                lackDict[i.skuCode] = c
        print lackDict
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())