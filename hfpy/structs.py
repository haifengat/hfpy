#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/9/21'
"""

from enum import Enum


class IntervalType(Enum):
    """时间类型:秒,分,时,日,周,月,年"""

    Second = 0
    '''秒'''

    Minute = 1
    '''分'''

    Hour = 2
    '''时'''

    Day = 3
    '''日'''

    Week = 4
    '''周'''

    Month = 5
    '''月'''

    Year = 6
    '''年'''

    def __int__(self):
        """return int value"""
        return self.value


class BarType(Enum):
    """请求数据的类型"""

    Min = 0
    '''分钟'''

    Real = 2
    '''实时'''

    Time = 3
    '''交易时间'''

    Product = 4
    '''品种信息'''

    TradeDate = 5
    '''交易日历'''

    InstrumentInfo = 6
    '''合约与品种对应信息'''

    def __int__(self):
        """return int value"""
        return self.value


class ReqPackage:
    """数据请求格式包"""

    def __init__(self):
        """Constructor"""

        self.Type: BarType = BarType.Min
        '''请求类型'''

        self.Instrument = ''
        '''合约'''

        self.Begin = ''
        '''开始时间'''

        self.End = ''
        '''结束时间'''

    def __setitem__(self, k, v):
        self.k = v

    def __dict__(self):
        return {'Type': int(self.Type), 'Instrument': self.Instrument, 'Begin': self.Begin, 'End': self.End}
