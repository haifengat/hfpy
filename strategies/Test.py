# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2017/11/16'
"""

from hfpy.strategy import Strategy
from hfpy.data import Data
from hfpy.bar import Bar


class Test(Strategy):
    ''''''

    def __init__(self, jsonfile=''):
        super().__init__(jsonfile)
        self.ordered = False
        self.closed = False
        self.oid = 0
    
    def OnBarUpdate(self, data=Data, bar=Bar):
        if self.Tick.Instrument == '':
            return
        # print(self.Datas[0].Tick.UpdateTime[-2:])
        if self.Tick.UpdateTime[-2:] == '00' or self.Tick.UpdateTime[-2:] == '30':
            if self.ordered:
                self.ordered = False
            else:
                self.ordered = True
                # self.ReqOrder(self.Instrument, DirectType.Buy, OffsetType.Open, self.Tick.AskPrice, 1)
                # self.ReqOrder(self.Tick.Instrument, DirectType.Buy, OffsetType.Open, self.Tick.BidPrice, 1)
                self.Sell(self.Tick.BidPrice, 1, 'close long')

                print('1 last order == ', self.GetLastOrder())
                print('1 order id == ', self.oid)
        '''
        if self.Tick.UpdateTime[-2:] == '05' or self.Tick.UpdateTime[-2:] == '35':
            if self.closed:
                self.closed = False
            else:
                self.closed = True
                self.Sell(self.O[0], 1, '')
                print(self.PositionLong)
                print('all:{0},last:{1},notfill:{2}'.format(len(self.GetOrders()), self.GetLastOrder(), len(self.GetNotFillOrders())))
        '''

    # def OnOrder(self, order=OrderField()):
    #     """委托响应"""
    #     print('委托反应')
    #     self.oid = self.GetLastOrder().OrderID

    #     print('last order == ', self.GetLastOrder())
    #     print('order id == ', self.oid)
    #     print('cancel orderid == ', order.OrderID)
    #     self.ReqCancel(self.oid)

    #     #print('strategy order')
    #     # print(order)

    # def OnTrade(self, trade=TradeField()):
    #     """成交响应"""
    #     print('成交反应')
    #     print('strategy trade')
    #     print(trade)

    # def OnCancel(self, order):
    #     """撤单响应"""
    #     print('扯淡反应')
    #     print('所撤单资料 ：', order)

    #     #print('strategy cancel')
    #     # print(order)

    # def OnErrOrder(self, order=OrderField(), info=InfoField()):
    #     """委托错误"""
    #     print('委托错误')
    #     print('strategy err order')
    #     print(order)

    # def OnErrCancel(self, order=OrderField(), info=InfoField()):
    #     """撤单错误"""
    #     print('撤单错误')
    #     print('strategy err cancel')
    #     print(order)
