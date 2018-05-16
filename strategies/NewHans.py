#!/usr/bin/env python
# -*- coding: utf-8 -*-

import talib
import copy
import logging
import numpy as np
from py_at.strategy import Strategy
from py_at.enums import IntervalType
from py_at.data import Data
from py_at.tick import Tick
from py_at.bar import Bar
from py_at.structs import OrderField, TradeField, InfoField

class NewHans(Strategy):
    '''
    该版本的hans策略在hans123的基础上进行了修正，该策略认为波动具有延续性，从而添加了对日线波动的判断，当日线波动比较大时，
    正好适合日内hans123策略的实施;这里为了更好的利用波动，采用最高价与最低价的差来定义波动，用波动的N日平均值来作为
    '''
    def __init__(self, jsonfile=''):
        super().__init__(jsonfile)
       
        self.up = 0
        self.down = 1000000
        self.rate = 20
        
        self.openflag = False

        self.highD = self.Datas[1].H
        self.lowD = self.Datas[1].L

        self.token = 1

    def OnBar(self, data=Data, bar=Bar):
        if not self.openflag:
            if bar.D[-8:] > '21:00:00' and bar.D[-8:] < '21:30:00':
                self.up = max(self.up, bar.H)
                self.down = min(self.down, bar.L)
                
            elif bar.D[-8:] > '21:30:00' and bar.D[-8:] < '21:40:00':
                self.openflag = True
                diff = np.array(self.Datas[1].H) - np.array(self.Datas[1].L) 
                self.rate = np.std(diff)
                
        else:
            if self.rate > 20:
                
                if self.Position == 0 and self.token > 0: 
                    if  bar.C > self.up:
                        self.Buy(bar.C, self.Lots)
                        self.token = self.token - 1 
                    elif bar.C < self.down:
                        self.token = self.token - 1 
                        self.SellShort(bar.C, self.Lots)
                else:
                    if bar.D[-8:] > '14:55:00' and bar.D[-8:] < '15:00:00':
                        if self.PositionLong > 0:
                            self.Sell(bar.C, self.PositionLong)
                        elif self.PositionShort > 0:
                            self.BuyToCover(bar.C, self.PositionShort)
                            
        
          
                
                               
                

        

        




