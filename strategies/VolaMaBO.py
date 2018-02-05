'''
//%进场只在每周的周一到周四进行，周五不进场开仓，但可以平仓。
//%寻找波动率放大突破点，同时满足close > average (close,N)均线过滤的有条件下，做多
//%寻找波动率放大突破点，同时满足close < average (close,N)均线过滤的有条件下，做空
//%出场使用3:1的合约价值止盈止损比
//%在沪深300股指期货与螺纹钢期货里面按照1:50的标准进行投资。
'''
from py_at.strategy import Strategy
from py_at.enums import IntervalType, DirectType, OffsetType, OrderType
from py_at.structs import OrderField, TradeField, InfoField
from py_at.data import Data
from py_at.tick import Tick
from py_at.bar import Bar
import time
import talib as tl
import datetime,time

class VolaMaBO():
    ''''''
    def __init__(self, jsonfile=''):
        super().__init__(jsonfile)

    def OnBarUpdate(self, data=Data, bar=Bar):
        if data.CurrentBar<50:
            return
        #移动平均线
        ma1 = tl.SMA(data.C,self.Params['malength'])
        #atr计算
        vola1 = tl.ATR(data.H, data.L, data.C, timeperiod=self.Params['volalength1'])
        vola2 = tl.ATR(data.H, data.L, data.C, timeperiod=self.Params['volalength2'])

        '''
        print('c==',data.D[-2])
        print('c==:',data.C[-2])
        print('ma1==:',ma1[-2])
        print('vola1 == ',vola1[-2])
        print('vola2==',vola2[-2])
        '''
        dd =5

        if data.C[-2]>ma1[-2] and vola1[-2] > vola2[-2] and data.PositionShort >= 0:
            if data.PositionShort > 0:
                data.BuyToCover( data.O[-1] + 1,1,'')
                print('平卖')
            if dd != self.Params['Noopen'] and data.PositionLong == 0:
                data.Buy( data.O[-1] + 1,1,'')
                print('买入')
 
        if data.C[-2]<ma1[-2] and vola1[-2] > vola2[-2] and data.PositionLong >= 0:  
            if data.PositionLong > 0:
                data.Sell(data.O[-1] - 1,1,'')
                print('平买')
            if dd != self.Params['Noopen'] and data.PositionShort == 0:
                data.SellShort(data.O[-1] - 1,1,'')
                print('卖出')
         
            
        

    

