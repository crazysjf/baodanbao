# -*- coding: utf-8 -*-

import xlwt;
import xlrd;
import sys;
#import xlutils;
from xlutils.copy import copy;
from datetime import date,datetime;

from order import Order

# 各字段列号（Number of Column）
NC_SKU_CODE = 8  # 编码
NC_COUNT    = 14 # 数量
NC_EXP_NUM  = 21 # 快递单号

# 销量数据类，从excel表读取数据
class OrderData:
    # 加载数据
    def load(self,file):
        orderDataFileRb = xlrd.open_workbook(file)
        self.sheet = orderDataFileRb.sheet_by_index(0)
        #print code.encode('utf-8')

    # 根据快递单号找订单
    def findOrderByExpNum(self, expNum):
        for i in range(1, self.sheet.nrows):
            n = self.sheet.cell(i, 21).value # 21列为快递单号
            if expNum == n:
                row = self.sheet.row_values(i)
                return Order(expNum, row[NC_SKU_CODE], row[NC_COUNT])
            #print n.encode('utf-8')