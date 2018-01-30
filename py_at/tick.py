#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/9/21'
"""


class Tick:
    """分笔数据"""

    def __init__(self):
        """初始化"""
        '''合约'''
        self.Instrument = ''
        '''最新价'''
        self.LastPrice = 0.0
        '''挂卖价'''
        self.AskPrice = 0.0
        '''挂买价'''
        self.BidPrice = 0.0
        '''挂卖量'''
        self.AskVolume = 1
        '''挂买量'''
        self.BidVolume = 1
        '''时间'''
        self.UpdateTime = ''
        '''成交量'''
        self.Volume = 1
        '''持仓量'''
        self.OpenInterest = 1.0
        '''均价'''
        self.AveragePrice = 0.0

    def __str__(self):
        """"""
        return '{self.Instrument}, {self.LastPrice}, {self.AskPrice}, {self.AskVolume}, {self.BidPrice}, {self.BidVolume}, {self.UpdateTime}, {self.Volume}, {self.OpenInterest}, {self.AveragePrice}'.format(
            self=self)

    @property
    def __dict__(self):
        return {
            'Instrument': self.Instrument,
            'LastPrice': self.LastPrice,
            'AskPrice': self.AskPrice,
            'AskVolume': self.AskVolume,
            'BidPrice': self.BidPrice,
            'BidVolume': self.BidVolume,
            'UpdateTime': self.UpdateTime,
            'Volume': self.Volume,
            'OpenInterest': self.OpenInterest,
            'AveragePrice': self.AveragePrice
        }
