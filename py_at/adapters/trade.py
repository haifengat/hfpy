#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/9/21'
"""

from py_at.structs import InfoField, OrderField, TradeField
from py_at.enums import DirectType, OffsetType, OrderType


class TradeAdapter:
    def __init__(self):
        """"""
        self.BrokerID = ''
        self.Investor = ''
        self.Password = ''

        self.FrontID = ''
        self.SessionID = ''
        self.TradingDay = ''

        self.DicInstrument = {}
        self.DicOrderField = {}
        self.DicTradeField = {}
        self.DicPositionField = {}
        self.DicInstrumentStatus = {}
        self.Account = None
        self.IsLogin = False

    def ReqConnect(self, pAddress=''):
        pass

    def ReqUserLogin(self, user='', pwd='', broker=''):
        pass

    def ReqOrderInsert(self,
                       pInstrument='',
                       pDirection=DirectType,
                       pOffset=OffsetType,
                       pPrice=0.0,
                       pVolume=1,
                       pType=OrderType,
                       pCustom=0):
        pass

    def ReqOrderAction(self, OrderID=''):
        pass

    def Release(self):
        pass

    def OnFrontConnected(self):
        """"""
        pass

    def OnFrontDisConnected(self, error=0):
        """"""
        pass

    def OnRspUserLogin(self, info=InfoField):
        """"""
        pass

    def OnRtnOrder(self, f=OrderField):
        """"""
        print(f.__dict__)

    def OnRtnTrade(self, f=TradeField):
        """"""
        pass

    def OnRtnCancel(self, f=OrderField):
        """"""
        pass

    def OnRtnErrOrder(self, f=OrderField, info=InfoField):
        """"""
        pass
