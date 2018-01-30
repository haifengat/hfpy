#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/9/21'
"""

from py_at.enums import DirectType, OffsetType, OrderStatus, BarType


class ReqPackage:
    """数据请求格式包"""

    def __init__(self):
        """Constructor"""
        '''请求类型'''
        self.Type = BarType.Min
        '''合约'''
        self.Instrument = ''
        '''开始时间'''
        self.Begin = ''
        '''结束时间'''
        self.End = ''


class InfoField:
    """返回信息"""

    def __init__(self):
        """Constructor"""
        '''错误号'''
        self.ErrorID = 0
        '''错误描述'''
        self.ErrorMsg = '正确'

    def __str__(self):
        # return 'ErrorID:{0}, ErrorMsg:{1}'.format(self.ErrorID, self.ErrorMsg)
        return '{{"ErrorID":{self.ErrorID}, "ErrorMsg":"{self.ErrorMsg}"}}'.format(
            self=self)

    @property
    def __dict__(self):
        return {'ErrorID': self.ErrorID, 'ErrorMsg': self.ErrorMsg}


class OrderField:
    """报单响应"""

    def __init__(self):
        """initionalize"""
        '''委托标识'''
        self.OrderID = ""
        '''合约'''
        self.InstrumentID = ""
        '''买卖'''
        self.Direction = DirectType.Buy
        '''开平'''
        self.Offset = OffsetType.Open
        '''限价单价格'''
        self.LimitPrice = 0.0
        '''报单均价'''
        self.AvgPrice = 0.0
        '''委托时间'''
        self.InsertTime = ""
        '''成交时间'''
        self.TradeTime = ""
        '''成交数量(本次)'''
        self.TradeVolume = 0
        '''委托数量'''
        self.Volume = 0
        '''未成交数量'''
        self.VolumeLeft = 0
        '''委托状态'''
        self.Status = OrderStatus.Normal
        '''状态描述'''
        self.StatusMsg = ""
        '''是否本地委托'''
        self.IsLocal = False
        '''委托自定义标识'''
        self.Custom = 0
        '''系统(交易所)ID'''
        self.SysID = ""

    def __str__(self):
        """"""
        return '{self.OrderID}, {self.InstrumentID}, {self.Direction}, {self.Offset}, {self.LimitPrice}, {self.AvgPrice}, {self.InsertTime}, {self.TradeTime}, {self.TradeVolume}, {self.Volume}, {self.VolumeLeft}, {self.Status}, {self.StatusMsg}, {self.IsLocal}, {self.Custom}, {self.SysID}'.format(
            self=self)

    @property
    def __dict__(self):  # 如何控制dict的字段次序?:交由客户端处理
        return {
            'OrderID': self.OrderID,
            'InstrumentID': self.InstrumentID,
            'Direction': self.Direction.name,
            'Offset': self.Offset.name,
            'LimitPrice': self.LimitPrice,
            'AvgPrice': self.AvgPrice,
            'InsertTime': self.InsertTime,
            'TradeTime': self.TradeTime,
            'TradeVolume': self.TradeVolume,
            'Volume': self.Volume,
            'VolumeLeft': self.VolumeLeft,
            'Status': self.Status.name,
            'StatusMsg': self.StatusMsg,
            'IsLocal': self.IsLocal,
            'Custom': self.Custom,
            'SysID': self.SysID
        }


class TradeField:
    """成交响应"""

    def __init__(self):
        """Constructor"""
        '''成交标识'''
        self.TradeID = ''
        '''合约'''
        self.InstrumentID = ''
        '''交易所'''
        self.ExchangeID = ''
        '''买卖'''
        self.Direction = DirectType.Buy
        '''开平'''
        self.Offset = OffsetType.Open
        '''成交价'''
        self.Price = 0.0
        '''成交数量'''
        self.Volume = 0
        '''成交时间'''
        self.TradeTime = ''
        '''交易日'''
        self.TradingDay = ''
        ''''对应的委托标识'''
        self.OrderID = ''
        '''对应的系统(交易所)ID'''
        self.SysID = ''

    def __str__(self):
        """"""
        return '{self.TradeID}, {self.InstrumentID}, {self.ExchangeID}, {self.Direction}, {self.Offset}, {self.Price}, {self.Volume}, {self.TradeTime}, {self.TradingDay}, {self.OrderID}, {self.SysID}'.format(
            self=self)

    @property
    def __dict__(self):
        return {
            'TradeID': self.TradeID,
            'InstrumentID': self.InstrumentID,
            'ExchangeID': self.ExchangeID,
            'Direction': self.Direction.name,
            'Offset': self.Offset.name,
            'Price': self.Price,
            'Volume': self.Volume,
            'TradeTime': self.TradeTime,
            'TradingDay': self.TradingDay,
            'OrderID': self.OrderID,
            'SysID': self.SysID
        }


class InstrumentField:
    """合约"""

    def __init__(self):
        """Constructor"""
        '''合约'''
        self.InstrumentID = ''
        '''品种'''
        self.ProductID = ''
        '''交易所'''
        self.ExchangeID = ''
        '''合约乘数'''
        self.VolumeMultiple = ''
        '''每跳价格变动'''
        self.PriceTick = 0.0
        '''最大单笔下单量'''
        self.MaxOrderVolume = 9999

    def __str__(self):
        """"""
        return '{self.InstrumentID}, {self.ProductID}, {self.ExchangeID}, {self.VolumeMultiple}, {self.PriceTick}, {self.MaxOrderVolume}'.format(
            self=self)

    @property
    def __dict__(self):
        return {
            'InstrumentID': self.InstrumentID,
            'ProductID': self.ProductID,
            'ExchangeID': self.ExchangeID,
            'VolumeMultiple': self.VolumeMultiple,
            'PriceTick': self.PriceTick,
            'MaxOrderVolume': self.MaxOrderVolume
        }


class TradingAccount:
    """交易帐户"""

    def __init__(self):
        """Constructor"""
        '''昨日结算'''
        self.PreBalance = 0.0
        '''持仓盈亏'''
        self.PositionProfit = 0.0
        '''平仓盈亏'''
        self.CloseProfit = 0.0
        '''手续费'''
        self.Commission = 0.0
        '''保证金'''
        self.CurrMargin = 0.0
        '''冻结'''
        self.FrozenCash = 0.0
        '''可用'''
        self.Available = 0.0
        '''动态权益'''
        self.Fund = 0.0
        '''风险度'''
        self.Risk = 0.0

    # ----------------------------------------------------------------------
    def __str__(self):
        """"""
        return '{self.PreBalance}, {self.PositionProfit}, {self.CloseProfit}, {self.Commission}, {self.CurrMargin}, {self.FrozenCash}, {self.Available}, {self.Fund}, {self.Risk}'.format(
            self=self)

    @property
    def __dict__(self):
        return {
            'PreBalance': self.PreBalance,
            'PositionProfit': self.PositionProfit,
            'CloseProfit': self.CloseProfit,
            'Commission': self.Commission,
            'CurrMargin': self.CurrMargin,
            'FrozenCash': self.FrozenCash,
            'Available': self.Available,
            'Fund': self.Fund,
            'Risk': self.Risk
        }


########################################################################
class PositionField:
    """持仓"""

    # ----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        '''合约'''
        self.InstrumentID = ''
        '''多空'''
        self.Direction = DirectType.Buy
        '''持仓价格'''
        self.Price = 0.0
        '''持仓量'''
        self.Position = 1
        '''昨持仓'''
        self.YdPosition = 0
        '''今持仓'''
        self.TdPosition = 0
        '''平仓盈亏'''
        self.CloseProfit = 0.0
        '''持仓盈亏'''
        self.PositionProfit = 0.0
        '''手续费'''
        self.Commission = 0.0
        '''保证金'''
        self.Margin = 0.0

    # ----------------------------------------------------------------------
    def __str__(self):
        """"""
        return (
            '{self.InstrumentID}, {self.Direction}, {self.Price}, {self.Position}, {self.TdPosition}, {self.YdPosition}, {self.CloseProfit}, {self.PositionProfit}, {self.Commission}, {self.Margin}'
        ).format(self=self)

    @property
    def __dict__(self):
        return {
            'InstrumentID': self.InstrumentID,
            'Direction': self.Direction.name,
            'Price': self.Price,
            'Position': self.Position,
            'TdPosition': self.TdPosition,
            'YdPosition': self.YdPosition,
            'CloseProfit': self.CloseProfit,
            'PositionProfit': self.PositionProfit,
            'Commission': self.Commission,
            'Margin': self.Margin
        }
