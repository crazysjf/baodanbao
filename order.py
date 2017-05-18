# -*- coding: utf-8 -*-

# 订单中的单个宝贝（一行）
class Item:
    def __init__(self, skuCode, count):
        self.skuCode    = skuCode
        self.count      = count

# 一个订单。里面可能有多个宝贝
class Order:
    def __init__(self, expNum, customerID, items):
        self.expNum = expNum
        self.customerID = customerID
        self.customerID = customerID
        self.items = items
