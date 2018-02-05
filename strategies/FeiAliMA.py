'''
开盘价加上开盘价乘以一个参数，作为入场条件
收盘离场
反手平仓
'''
from py_at.strategy import Strategy
from py_at.enums import IntervalType, DirectType, OffsetType, OrderType
from py_at.structs import OrderField, TradeField, InfoField
from py_at.data import Data
from py_at.tick import Tick
from py_at.bar import Bar
import time,datetime
import talib as tl
import datetime,time

class FeiAliMA():
    ''''''
    def __init__(self, jsonfile=''):
        super().__init__(jsonfile)
        self.openD = []

        self.highD = []
        self.lowD = []
        self.hh = 0
        self.ll = 0
        self.trading = True
    def OnBarUpdate(self, data=Data, bar=Bar):
    
        # 计算日内最高价和最低价  换日时候更新list
        if self.CurrentBar == 0 or (self.D[-1][9:13] > '18:00:00' and self.D[-2][9:13] <= '18:00:00'):
            self.openD.append(self.O[-1])
            self.highD.append(self.hh)
            self.lowD.append(self.ll)
            self.hh = self.H[-1]
            self.ll = self.L[-1]

        self.hh = max(self.H[-1],self.hh)
        self.ll = min(self.L[-1],self.ll)

        if data.CurrentBar < self.Params['vola']:
            return
        
        # 移动平均线，是个array
        ma1 = tl.SMA(data.C,self.Params['malength'])
        
        # 计算上下轨
        upband = self.openD[-1]*(1 + self.Params['vola']/1000)
        udband = self.openD[-1]*(1 - self.Params['vola']/1000)
        if self.D[-1][9:13] >'14:30:00' and self.D[-1][9:13] <'15:00:00':
            self.trading = False
        else:
            self.trading = True

        if upband < self.C[-2] and data.PositionShort >= 0:
            if data.PositionShort > 0:
                data.BuyToCover( data.O[-1] + 1,1,'')
                #print('平卖', data.D[-1])
                #print('upband1:',upband)

            if data.PositionLong == 0 and data.PositionShort == 0:
                data.Buy( data.O[-1] + 1,1,'')
                #print('买入', data.D[-1])
                #print('upband2:',upband)
 
        if udband > self.C[-2] and data.PositionLong >= 0:  
            if data.PositionLong > 0:
                data.Sell(data.O[-1] - 1,1,'')
                #print('平买', data.D[-1])
                #print('udband1:',udband)

            if data.PositionShort == 0 and data.PositionLong == 0:
                data.SellShort(data.O[-1] - 1,1,'')
                #print('卖出', data.D[-1])
                #print('udband2:',udband)
        
        if self.D[-1][9:13] >= '14:59:00' and self.D[-1][9:13] <= '15:01:00':
            if data.PositionLong > 0:
                data.Sell(data.O[-1] - 1,1,'')
            if data.PositionShort > 0:
                data.BuyToCover( data.O[-1] + 1,1,'')
         
            
        
