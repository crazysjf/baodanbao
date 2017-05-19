# -*- coding: utf-8 -*-

import xlwt;
import xlrd;
import sys;
#import xlutils;
from xlutils.copy import copy;
from datetime import date,datetime;

from order import *
import os
import os.path

# 各字段列号（Number of Column）
NC_SKU_CODE     = 8  # 编码
NC_COUNT        = 14 # 数量
NC_EXP_NUM      = 21 # 快递单号
NC_EXP_RECEIVER = 26 # 收件人
NC_CUSTOMER_ID  = 25 # 旺旺ID

# 销量数据类，从excel表读取数据


class OrderData:
    # 从指定路径加载数据。读取路径下的所有报表，载入data数组中
    def load(self,dir):
        # 保存所有数据的数据表
        self.data = []
        #print code.encode('utf-8')
        list = os.listdir(dir)  # 列出文件夹下所有的目录与文件
        for i in range(0, len(list)):
            path = os.path.join(dir, list[i])
            if os.path.isfile(path) and os.path.splitext(path)[1] == '.xls':
                orderDataFileRb = xlrd.open_workbook(path)
                self.sheet = orderDataFileRb.sheet_by_index(0)
                for i in range(1, self.sheet.nrows):
                    self.data.append(self.sheet.row_values(i))
                print "Loaded:", path

    # 根据快递单号找订单
    def findOrderByExpNum(self, expNum):
        for i in range(1, len(self.data)):
            row = self.data[i]
            n = row[NC_EXP_NUM] # 快递单号
            if expNum == n:
                items = []
                item = Item(row[NC_SKU_CODE], row[NC_COUNT])
                items.append(item)

                # 如果后续的行中快递单号为空，且收件人为空，则表明后续的行仍然属于该订单
                i = i + 1
                while i < len(self.data):
                    row = self.data[i]
                    n = row[NC_EXP_NUM]         # 快递单号
                    r = row[NC_EXP_RECEIVER]    # 收件人
                    if n == "" and r == "":
                        items.append(Item(row[NC_SKU_CODE], row[NC_COUNT]))
                    else:
                        break
                    i = i+1

                return Order(expNum, row[NC_CUSTOMER_ID], items)

            #print n.encode('utf-8')