#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/8/16 '
"""

import time
from py_ctp.enums import DirectType, OffsetType


class OrderItem(object):
    """策略信号"""

    def __init__(self):
        """Constructor"""
        '''合约'''
        self.Instrument = ''
        '''合约'''
        '''时间 yyyyMMdd HH:mm:ss'''
        self.DateTime = time.strftime('%Y%m%d %H:%Mm:%S', time.localtime(time.time()))
        '''时间 yyyyMMdd HH:mm:ss'''
        '''买卖'''
        self.Direction = DirectType.Buy
        '''买卖'''
        '''开平'''
        self.Offset = OffsetType.Open
        '''开平'''
        '''价格'''
        self.Price = 0.0
        '''价格'''
        '''数量'''
        self.Volume = 0
        '''数量'''
        '''备注'''
        self.Remark = ''
        '''备注'''
        '''关联的开仓指令'''
        self.RelationOpenOrders = []
        '''关联的开仓指令'''
        '''开仓均价-空'''
        self.AvgEntryPriceShort = 0.0
        '''开仓均价-空'''
        '''开仓均价-多'''
        self.AvgEntryPriceLong = 0.0
        '''开仓均价-多'''
        '''持仓-多'''
        self.PositionLong = 0
        '''持仓-多'''
        '''持仓-空'''
        self.PositionShort = 0
        '''持仓-空'''
        '''开仓时间-多'''
        self.EntryDateLong = ''
        '''开仓时间-多'''
        '''开仓时间-空'''
        self.EntryDateShort = ''
        '''开仓时间-空'''
        '''开仓价格-多'''
        self.EntryPriceLong = 0.0
        '''开仓价格-多'''
        '''开仓价格-空'''
        self.EntryPriceShort = 0.0
        '''开仓价格-空'''
        '''平仓时间-多'''
        self.ExitDateLong = ''
        '''平仓时间-多'''
        '''平仓时间-空'''
        self.ExitDateShort = ''
        '''平仓时间-空'''
        '''平仓价格-多'''
        self.ExitPriceLong = 0.0
        '''平仓价格-多'''
        '''平仓价格-空'''
        self.ExitPriceShort = 0.0
        '''平仓价格-空'''
        '''最后一次开仓时间-多'''
        self.LastEntryDateLong = ''
        '''最后一次开仓时间-多'''
        '''最后一次开仓时间-空'''
        self.LastEntryDateShort = ''
        '''最后一次开仓时间-空'''
        '''最后一次开仓价格-多'''
        self.LastEntryPriceLong = 0.0
        '''最后一次开仓价格-多'''
        '''最后一次开仓价格-空'''
        self.LastEntryPriceShort = 0.0
        '''最后一次开仓价格-空'''
        '''开仓到当前K线的数量(0开始)-多'''
        self.IndexEntryLong = 0.0
        '''开仓到当前K线的数量(0开始)-多'''
        '''开仓到当前K线的数量(0开始)-空'''
        self.IndexEntryShort = 0.0
        '''开仓到当前K线的数量(0开始)-空'''
        '''最后开仓到当前K线的数量(0开始)-多'''
        self.IndexLastEntryLong = -1
        '''最后开仓到当前K线的数量(0开始)-多'''
        '''最后开仓到当前K线的数量(0开始)-空'''
        self.IndexLastEntryShort = -1
        '''最后开仓到当前K线的数量(0开始)-空'''
        '''平仓到当前K线的数量(0开始)-多'''
        self.IndexExitLong = -1
        '''平仓到当前K线的数量(0开始)-多'''
        '''平仓到当前K线的数量(0开始)-空'''
        self.IndexExitShort = -1
        '''平仓到当前K线的数量(0开始)-空'''

    def __str__(self):
        """"""
        return '{self.Instrument}, {self.DateTime}, {self.Direction}, {self.Offset}, {self.Price}, {self.Volume}, {self.Remark}'.format(
            self=self)
