#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/8/16'
"""
import talib
from hfpy.data import Data
from hfpy.bar import Bar
from hfpy.strategy import Strategy
import numpy as np


class SMACross(Strategy):

    def __init__(self, jsonfile):
        super().__init__(jsonfile)
        self.p_ma1 = self.Params['MA1']
        self.p_ma2 = self.Params['MA2']
        self.p_lots = self.Params['Lots']

    def OnBarUpdate(self, data=Data, bar=Bar):
        if len(self.C) < self.p_ma2:
            return

        # print('{0}-{1}'.format(self.D[-1], self.C[-1]))
        ma1 = talib.SMA(np.array(self.C, dtype=float), self.p_ma1)
        ma2 = talib.SMA(np.array(self.C, dtype=float), self.p_ma2)

        self.IndexDict['ma5'] = ma1
        self.IndexDict['ma10'] = ma2

        if self.PositionLong == 0:
            if ma1[-1] >= ma2[-1] and ma1[-2] < ma2[-2]:
                if self.PositionShort > 0:
                    self.BuyToCover(self.O[-1], self.p_lots, '买平')
                self.Buy(self.O[-1], self.p_lots, '买开')
        elif self.PositionShort == 0:
            if ma1[-1] <= ma2[-1] and ma1[-2] > ma2[-2]:
                if self.PositionLong > 0:
                    self.Sell(self.O[-1], self.p_lots, '卖平')
                self.SellShort(self.O[-1], self.p_lots, '卖开')
