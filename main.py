# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from ui import Ui_Form
from multi_selection_dialog import MultiSelectionDialog
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
        file = u"D:/projects/报单宝/销量数据/"
        orderData.load(file)

        self.orderDetailLabel.setText("订单信息")
        self.orderDetailLabel.adjustSize()
        self.orderDetailLabel.setWordWrap(True)
        self.orderDetailLabel.setAlignment(Qt.AlignTop)

        # 列表列宽自适应
        self.lackDictTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.lackDictTableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)

    # 导入订单数据
    def importOrderDataButtonPushed(self):
        orderDateFile = QFileDialog.getOpenFileName(self)
        print orderDateFile[0].encode('utf-8')
        orderData.load(orderDateFile[0]) # orderDataFile为tupple，只取第一个元素


    # 导入宝贝销量数据
    def importGoodSalesDataButtonPushed(self):
        print "ffff"
        dialog = MultiSelectionDialog()
        dialog.exec_()

    def barCodeLineEditReturnPressed(self):
        expNum =  self.barCodeLineEdit.text()
        self.barCodeLineEdit.clear()
        order = orderData.findOrderByExpNum(expNum)

        if order != None:
            # 找到单号
            items = order.items

            # 如果有多件要弹框确认
            if len(items) > 1 :
                dialog = MultiSelectionDialog(items)
                if dialog.exec_():
                    items = dialog.selectedItems

            for i in items:
                print i.skuCode, i.count
                c =  int(i.count)
                if lackDict.has_key(i.skuCode):
                    lackDict[i.skuCode] = lackDict[i.skuCode] + c
                else:
                    lackDict[i.skuCode] = c
            self.orderDetailLabel.setText(self.order2Text(order))
            self.updateTableView()
        else:
            self.orderDetailLabel.setText(u"未找到单号：%s" % expNum)
        #print lackDict

    def order2Text(self, order):
        s = "%s %s\n\n" % (order.customerID, order.expNum)
        for i in order.items:
            s = s + "%s\t%s\n" % (i.skuCode, i.count)
        return s

    def updateTableView(self):
        self.lackDictTableWidget.clear()
        self.lackDictTableWidget.setRowCount(len(lackDict))
        i = 0
        for key in lackDict.keys():
            self.lackDictTableWidget.setItem(i, 0, QTableWidgetItem(key))
            self.lackDictTableWidget.setItem(i, 1, QTableWidgetItem("%s" % lackDict[key]))
            i = i+1

    def exportData(self):
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet(u'报单', cell_overwrite_ok=True)


        for i, key in enumerate(lackDict):
            sheet.write(i,0, key)
            sheet.write(i,1, lackDict[key])
        workbook.save('result.xls')  # 生成结果，保存到test3.xls中，如图2.

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())