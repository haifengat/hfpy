#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/8/16'
"""
import talib

from py_at.data import Data
from py_at.bar import Bar
from py_at.strategy import Strategy
from py_at.enums import IntervalType
from numpy import std, subtract, polyfit, sqrt, log
import numpy as np
import pandas as pd

class SMA_hurst(Strategy):

    def __init__(self, jsonfile):
        super().__init__(jsonfile)
        self.p_ma1 = self.Params['MA1'] 
        self.p_ma2 = self.Params['MA2'] 
        self.p_lots = self.Params['Lots'] = 1
        self.hurstlist = []
        self.mahurstlist = []
        self.vola = []
    #github版本 hurst 指数
    def churst(self,ts):
        """Returns the Hurst Exponent of the time series vector ts"""

        # create the range of lag values
        i = len(ts) // 2
        lags = range(2, i)
        # Calculate the array of the variances of the lagged differences
        tau = [sqrt(std(subtract(ts[lag:], ts[:-lag]))) for lag in lags]

        # use a linear fit to estimate the Hurst Exponent
        poly = polyfit(log(lags), log(tau), 1)

        # Return the Hurst Exponent from the polyfit output
        return poly[0] * 2.0

    # 自定义版本 hurst指数计算方法
    def calcHurst2(self, ts):
        '''
        if not isinstance(ts, Iterable):
            print('error')
            return
        '''
        n_min, n_max = 2, len(ts)//3
        RSlist = []
        for cut in range(n_min, n_max):
            children = len(ts) // cut
            children_list = [ts[i*children:(i+1)*children] for i in range(cut)]
            L = []
            for a_children in children_list:
                Ma = np.mean(a_children)
                Xta = pd.Series(map(lambda x: x-Ma, a_children)).cumsum()
                Ra = max(Xta) - min(Xta)
                Sa = np.std(a_children)
                rs = Ra / Sa
                L.append(rs)
            RS = np.mean(L)
            RSlist.append(RS)
        return np.polyfit(np.log(range(2+len(RSlist),2,-1)), np.log(RSlist), 1)[0]

    def OnBarUpdate(self, data=Data, bar=Bar):
        if len(self.C) > 2:
            volability = np.log(self.C[-1]) - np.log(self.C[-2])
            if self.D[-1] != self.D[-2]:
                self.vola.append(volability)

        if len(self.C) < self.p_ma2:
            return

        if len(self.C) < 50:
            return

        # print('{0}-{1}'.format(self.D[-1], self.C[-1]))
        ma1 = talib.SMA(self.C, self.p_ma1)
        ma2 = talib.SMA(self.C, self.p_ma2)

        # 实盘需要考虑tick的连续添加
        #self.hurstlist.append(np.array(self.churst(self.vola[-30:-1])))   
        
        self.hurstlist.append(np.array(self.calcHurst2(self.vola[-30:-1])))   


        if len(self.hurstlist) > 5:
            mahurst = np.mean(self.hurstlist[-6:-2]) 
            self.mahurstlist.append(mahurst)
            #talib.SMA(self.hurst,5)
            print('hurst = ',mahurst)
            print('date = ',self.D[-1])
            #print('***********************************')

            self.IndexDict['ma5'] = ma1
            self.IndexDict['ma10'] = ma2

            if self.PositionLong == 0:
                if ma1[-1] >= ma2[-1] and ma1[-2] < ma2[-2]:
                    if self.PositionShort > 0:
                        self.BuyToCover(self.O[-1], self.p_lots, '买平')
                    if mahurst > 1 and mahurst < 1.25:
                        self.Buy(self.O[-1], self.p_lots, '买开')
            elif self.PositionShort == 0:
                if ma1[-1] <= ma2[-1] and ma1[-2] > ma2[-2]:
                    if self.PositionLong > 0:
                        self.Sell(self.O[-1], self.p_lots, '卖平')
                    if mahurst > 1 and mahurst < 1.25:
                        self.SellShort(self.O[-1], self.p_lots, '卖开')

            if ((mahurst < 0.5 and mahurst > 0.3) or mahurst > 1.25 )and self.PositionLong >0:
                self.Sell(self.O[-1], self.p_lots, '卖平')
            
            if ((mahurst < 0.5 and mahurst > 0.3) or mahurst > 1.25) and self.PositionShort >0:
                self.BuyToCover(self.O[-1], self.p_lots, '买平')
            
