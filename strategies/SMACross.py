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
import numpy as np
from scipy.optimize import leastsq
import pandas as pd


class SMACross(Strategy):

    def __init__(self, jsonfile):
        super().__init__(jsonfile)
        self.p_ma1 = self.Params['MA1'] 
        self.p_ma2 = self.Params['MA2'] 
        self.p_lots = self.Params['Lots'] = 1
        self.maRatio = []
        self.longmaRatio = []
        self.shortmaRatio = []
        
        self.volRatio = []
        self.longvolRatio = []
        self.shortvolRatio = []

        self.winnlist = []
        self.longwinnlist= []
        self.shortwinnlist = []
        self.inprice = 0
        self.tempMaRatio = 0
        self.tempVolRatio = 0
        self.f_list = []
        self.longf_list= []
        self.shortf_list = []
        self.tempF = 0
        self.longk = 0
        self.longb = 0
        self.shortk = 0
        self.shortb = 0
        self.corrlist = []
        self.longcorrlist = []
        self.shortcorrlist = []
    def func(self,p,x1):
        k,b=p
        return k*x1+b

    def error(self,p,x1,y):
        #print(s)
        return self.func(p,x1) - y

    def OnBarUpdate(self, data=Data, bar=Bar):
        if len(self.C) < self.p_ma2:
            return

        # print('{0}-{1}'.format(self.D[-1], self.C[-1]))
        ma1 = talib.SMA(self.C, self.p_ma1)
        ma2 = talib.SMA(self.C, self.p_ma2)

        vol1 = talib.SMA(self.V,5)
        vol2 = talib.SMA(self.V,15)

        ll = vol1[-2] - vol2[-2]
        mm = ma1[-2] - ma2[-2]
        self.IndexDict['ma5'] = ma1
        self.IndexDict['ma10'] = ma2

        #
        if len(self.longwinnlist) > 30:
            g = np.array(self.longwinnlist)
            f1 = np.array(self.longmaRatio)

            # 求拟合因子参数
            p0 = np.array([1.0,1.0])
            para = leastsq(self.error,p0,args=(f1,g))
            self.longk,self.longb = para[0]


        if len(self.longwinnlist) > 30:
            g = np.array(self.shortwinnlist)
            f1 = np.array(self.shortmaRatio)

            # 求拟合因子参数
            p0 = np.array([1.0,1.0])
            para = leastsq(self.error,p0,args=(f1,g))
            self.shortk,self.shortb = para[0]
            #print("求解的拟合直线：")
            #print('y=' + str(round(self.k,4)) + 'x1' + str(round(self.b,4)))

        if self.PositionLong == 0:
            if ma1[-2] >= ma2[-2] and ma1[-3] < ma2[-3]:
                if self.PositionShort > 0:
                    self.BuyToCover(self.O[-1], data.PositionShort, '买平')
                    self.maRatio.append(self.tempMaRatio)
                    self.shortmaRatio.append(self.tempMaRatio)
                    self.volRatio.append(self.tempVolRatio)
                    self.shortvolRatio.append(self.tempVolRatio)
                    self.f_list.append(self.tempF)
                    self.shortf_list.append(self.tempF)
                    self.winnlist.append(self.inprice - self.O[-1])
                    self.shortwinnlist.append(self.inprice - self.O[-1])
                    if len(self.f_list)>1:
                        print('f = ',self.f_list[-1],'g = ',self.winnlist[-1])
                    if len(self.winnlist) > 30:
                        s1 = pd.Series(self.shortf_list[-30:])
                        yy = pd.Series(self.shortwinnlist[-30:])
                        self.shortcorrlist.append(s1.corr(yy))
                if len(self.longwinnlist) > 32:
                    if self.longcorrlist[-1] < -0.2 and self.longk*mm + self.longb < -2.5:
                        lots = self.p_lots*2
                        self.Buy(self.O[-1], lots, '买开')
                    elif self.longcorrlist[-1] < -0.2 and self.longk*mm + self.longb > 2.5:
                        pass
                    else:
                        self.Buy(self.O[-1], self.p_lots, '买开')
                else:
                    self.Buy(self.O[-1], self.p_lots, '买开')
                self.inprice = self.O[-1]
                self.tempMaRatio = mm
                self.tempVolRatio = ll
                self.tempF =  self.longk*mm + self.longb
                
        elif self.PositionShort == 0:
            if ma1[-2] <= ma2[-2] and ma1[-3] > ma2[-3]:
                if self.PositionLong > 0:
                    self.Sell(self.O[-1], data.PositionLong, '卖平')
                    self.maRatio.append(self.tempMaRatio)
                    self.longmaRatio.append(self.tempMaRatio)
                    self.volRatio.append(self.tempVolRatio)
                    self.longvolRatio.append(self.tempVolRatio)
                    self.f_list.append(self.tempF)
                    self.longf_list.append(self.tempF)
                    self.winnlist.append(self.O[-1] - self.inprice)
                    self.longwinnlist.append(self.inprice - self.O[-1])

                    if len(self.f_list)>1:
                        print('f = ',self.f_list[-1],'g = ',self.winnlist[-1])

                    if len(self.winnlist) > 30:
                        s1 = pd.Series(self.longf_list[-30:])
                        yy = pd.Series(self.longwinnlist[-30:])
                        self.longcorrlist.append(s1.corr(yy))

                if len(self.shortwinnlist) > 32:
                    
                    if self.shortcorrlist[-1] < -0.1 and self.shortk*mm + self.shortb <-4:
                        lots = self.p_lots*2
                        self.SellShort(self.O[-1], lots, 'mai开')
                    elif self.shortcorrlist[-1] < -0.1 and self.shortk*mm + self.shortb > 4:
                        pass
                    else:
                        self.SellShort(self.O[-1], self.p_lots, 'mai开')

                else:
                    self.SellShort(self.O[-1], self.p_lots, '卖开')

                self.inprice = self.O[-1]
                self.tempMaRatio = mm
                self.tempVolRatio = ll
                self.tempF =  self.shortk*mm + self.shortb


                
