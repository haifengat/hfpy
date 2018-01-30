#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2017/10/30'
"""

from enum import Enum


class DirectType(Enum):
    """买卖"""
    '''买'''
    Buy = 0
    '''买'''
    '''卖'''
    Sell = 1
    '''卖'''

    def __int__(self):
        return self.value


class OffsetType(Enum):
    """开平(今)"""
    '''开仓'''
    Open = 0
    '''开仓'''
    '''平仓'''
    Close = 1
    '''平仓'''
    '''平今
    上期所独有'''
    CloseToday = 2
    '''平今
    上期所独有'''

    # ----------------------------------------------------------------------
    def __int__(self):
        return self.value


class OrderType(Enum):
    """委托类型"""
    '''限价单'''
    Limit = 0
    '''限价单'''
    '''市价单'''
    Market = 1
    '''市价单'''
    '''部成立撤'''
    FAK = 2
    '''部成立撤'''
    '''全成立撤'''
    FOK = 3
    '''全成立撤'''

    def __int__(self):
        return self.value


class OrderStatus(Enum):
    """委托状态"""
    '''正常'''
    Normal = 0
    '''正常'''
    '''部分成交'''
    Partial = 1
    '''部分成交'''
    '''全部成交'''
    Filled = 2
    '''全部成交'''
    '''撤单'''
    Canceled = 3
    '''撤单'''
    '''错单'''
    Error = 4
    '''错单'''

    def __int__(self):
        return self.value


class IntervalType(Enum):
    """时间类型:秒,分,时,日,周,月,年"""
    '''秒'''
    Second = 0
    '''秒'''
    '''分'''
    Minute = 1
    '''分'''
    '''时'''
    Hour = 2
    '''时'''
    '''日'''
    Day = 3
    '''日'''
    '''周'''
    Week = 4
    '''周'''
    '''月'''
    Month = 5
    '''月'''
    '''年'''
    Year = 6
    '''年'''

    def __int__(self):
        """return int value"""
        return self.value


class BarType(Enum):
    """请求数据的类型"""
    '''分钟'''
    Min = 0
    '''分钟'''
    '''实时'''
    Real = 2
    '''实时'''
    '''交易时间'''
    Time = 3
    '''交易时间'''
    '''品种信息'''
    Product = 4
    '''品种信息'''
    '''交易日历'''
    TradeDate = 5
    '''交易日历'''

    def __int__(self):
        """return int value"""
        return self.value
