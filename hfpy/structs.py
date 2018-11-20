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


class ReqPackage:
    """数据请求格式包"""

    def __init__(self):
        """Constructor"""
        '''请求类型'''
        self.Type: BarType = BarType.Min
        '''请求类型'''
        '''合约'''
        self.Instrument = ''
        '''合约'''
        '''开始时间'''
        self.Begin = ''
        '''开始时间'''
        '''结束时间'''
        self.End = ''
        '''结束时间'''

    def __setitem__(self, k, v):
        self.k = v

    def __dict__(self):
        return {'Type': int(self.Type), 'Instrument': self.Instrument, 'Begin': self.Begin, 'End': self.End}
