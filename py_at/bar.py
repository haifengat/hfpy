#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/8/16'
"""


class Bar(object):
    """K线数据"""

    def __init__(self, datetime='', ins='', h=0.0, l=0.0, o=0.0, c=0.0, v=0, i=0.0):
        """初始化"""
        """时间
        yyyyMMdd HH:mm:ss"""
        self.D = datetime
        """时间
        yyyyMMdd HH:mm:ss"""
        """合约"""
        self.Instrument = ins
        """合约"""
        """最高价"""
        self.H = h
        """最高价"""
        """最低价"""
        self.L = l
        """最低价"""
        """开仓价"""
        self.O = o
        """开仓价"""
        """收盘价"""
        self.C = c
        """收盘价"""
        """成交量"""
        self.V = v
        """成交量"""
        """持仓价"""
        self.I = i
        """持仓价"""
        self._pre_volume = 0

    def __str__(self):
        """"""
        return '{self.D}, {self.H}, {self.L}, {self.O}, {self.C}, {self.V}, {self.I}'.format(
            self=self)
