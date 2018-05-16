
from py_at.strategy import Strategy
from py_at.enums import IntervalType
from py_at.structs import OrderField, TradeField, InfoField
from py_at.data import Data
from py_at.tick import Tick
from py_at.bar import Bar
import talib as tl 

class StdBO(Strategy):
    ''''''
    def __init__(self, jsonfile=''):
        super().__init__(jsonfile)
        self.ordered = False
        self.closed = False

    def OnBarUpdate(self, data=Data, bar=Bar):
        
        if self.CurrentBar <= self.Params['length']:
            return

        ma1 = tl.SMA(self.C, self.Params['length'])
        std1 = tl.STDDEV(self.C, self.Params['length'])
        UpperBand = ma1[-2] + std1[-2]
        UnderBand = ma1[-2] - std1[-2]
        
        '''
        print('上轨==',UpperBand)
        print('下轨==',UnderBand)
        print('jiage==',self.C[-2])
        print('多单==',self.PositionLong)
        print('空单==',self.PositionShort)
        '''
        
        if data.PositionLong < 1 and data.C[-2] > UpperBand and data.C[-3] < UpperBand:
            print('进入做多')
            if data.PositionShort > 0:
                data.BuyToCover(data.O[-1], data.PositionShort, '')
            data.Buy(data.O[-1], 1, '')
        if data.PositionShort < 1 and data.C[-2] > UnderBand and data.C[-3] < UnderBand:
            if data.PositionLong > 0:
                data.Sell(data.O[-1], data.PositionLong, '')
            data.SellShort(data.O[-1], 1, '')
            print('进入做空')

    def OnOrder(self, order=OrderField()):
        """委托响应"""
        print('strategy order')
        print(order)

    def OnTrade(self, trade=TradeField()):
        """成交响应"""
        print('strategy trade')
        print(trade)

    def OnCancel(self, order):
        """撤单响应"""
        print('strategy cancel')
        # print(order)

    def OnErrOrder(self, order=OrderField(), info=InfoField()):
        """委托错误"""
        print('strategy err order')
        # print(order)

    def OnErrCancel(self, order=OrderField(), info=InfoField()):
        """撤单错误"""
        print('strategy err cancel')
        # print(order)
