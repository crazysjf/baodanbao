# -*- coding: utf-8 -*-

import xlwt;
import xlrd;
import sys;
#import xlutils;
from xlutils.copy import copy;
from datetime import date,datetime;

from order import *

# 各字段列号（Number of Column）
NC_SKU_CODE     = 8  # 编码
NC_COUNT        = 14 # 数量
NC_EXP_NUM      = 21 # 快递单号
NC_EXP_RECEIVER = 26 # 收件人
NC_CUSTOMER_ID  = 25 # 旺旺ID

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
            row = self.sheet.row_values(i)
            n = row[NC_EXP_NUM] # 快递单号
            if expNum == n:
                items = []
                item = Item(row[NC_SKU_CODE], row[NC_COUNT])
                items.append(item)

                # 如果后续的行中快递单号为空，且收件人为空，则表明后续的行仍然属于该订单
                i = i + 1
                while i < self.sheet.nrows:
                    row = self.sheet.row_values(i)
                    n = row[NC_EXP_NUM]         # 快递单号
                    r = row[NC_EXP_RECEIVER]    # 收件人
                    if n == "" and r == "":
                        items.append(Item(row[NC_SKU_CODE], row[NC_COUNT]))
                    else:
                        break
                    i = i+1

                return Order(expNum, row[NC_CUSTOMER_ID], items)

            #print n.encode('utf-8')