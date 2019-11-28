#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/8/16 '
"""

import time
import copy
from .structs import IntervalType
from .order import OrderItem
from .bar import Bar
from py_ctp.enums import DirectType, OffsetType
from py_ctp.structs import InstrumentField, Tick


class Data(object):
    '''数据类, 策略继承此类'''

    def __init__(self, stra_barupdate=None, stra_onorder=None):
        '''初始所有变量'''
        self.stra_uppdate = stra_barupdate
        self.stra_onorder = stra_onorder
        '''每bar只执行一次交易'''
        self.SingleOrderOneBar = False
        '''每bar只执行一 次交易'''
        '''K线序列'''
        self.Bars = []
        '''K线序列'''
        '''合约'''
        self.Instrument = ''
        '''合约'''
        '''合约信息'''
        self.InstrumentInfo = InstrumentField()
        '''合约信息'''
        '''周期'''
        self.Interval = 1
        '''周期'''
        '''周期类型'''
        self.IntervalType = IntervalType.Minute
        '''周期类型'''
        '''分笔数据
        Tick.Instrument用来判断是否有实盘数据'''
        self.Tick = Tick()
        '''分笔数据
        Tick.Instrument用来判断是否有实盘数据'''
        '''买卖信号'''
        self.Orders = []
        '''买卖信号'''
        '''指标字典
        策略使用的指标保存在此字典中
        以便管理程序显示和处理'''
        self.IndexDict = {}
        '''指标字典
        策略使用的指标保存在此字典中
        以便管理程序显示和处理'''
        '''时间'''
        self.D = []
        '''时间'''
        '''最高价'''
        self.H = []
        '''最高价'''
        '''最低价'''
        self.L = []
        '''最低价'''
        '''开盘价'''
        self.O = []
        '''开盘价'''
        '''收盘价'''
        self.C = []
        '''收盘价'''
        '''交易量'''
        self.V = []
        '''交易量'''
        '''持仓量'''
        self.I = []
        '''持仓量'''

        self._lastOrder = OrderItem()

    @property
    def AvgEntryPriceShort(self):
        '''开仓均价-空'''
        return self._lastOrder.AvgEntryPriceShort

    @property
    def AvgEntryPriceLong(self):
        '''开仓均价-多'''
        return self._lastOrder.AvgEntryPriceLong

    @property
    def PositionLong(self):
        '''持仓-多'''
        return self._lastOrder.PositionLong

    @property
    def PositionShort(self):
        '''持仓-空'''
        return self._lastOrder.PositionShort

    @property
    def EntryDateLong(self):
        '''开仓时间-多'''
        return self._lastOrder.EntryDateLong

    @property
    def EntryPriceLong(self):
        '''开仓价格-多'''
        return self._lastOrder.EntryPriceLong

    @property
    def ExitDateShort(self):
        '''平仓时间-空'''
        return self._lastOrder.ExitDateShort

    @property
    def ExitPriceShort(self):
        '''平仓价-空'''
        return self._lastOrder.ExitPriceShort

    @property
    def EntryDateShort(self):
        '''开仓时间-空'''
        return self._lastOrder.EntryDateShort

    @property
    def EntryPriceShort(self):
        '''开仓价-空'''
        return self._lastOrder.EntryPriceShort

    @property
    def ExitDateLong(self):
        '''平仓时间-多'''
        return self._lastOrder.ExitDateLong

    @property
    def ExitPriceLong(self):
        '''平仓价-多'''
        return self._lastOrder.ExitPriceLong

    @property
    def LastEntryDateShort(self):
        '''最后开仓时间-空'''
        return self._lastOrder.LastEntryDateShort

    @property
    def LastEntryPriceShort(self):
        '''最后开仓价-空'''
        return self._lastOrder.LastEntryPriceShort

    @property
    def LastEntryDateLong(self):
        '''最后开仓时间-多'''
        return self._lastOrder.LastEntryDateLong

    @property
    def LastEntryPriceLong(self):
        '''最后开仓价-多'''
        return self._lastOrder.LastEntryPriceLong

    @property
    def IndexEntryLong(self):
        '''开仓到当前K线数量-多'''
        return self._lastOrder.IndexEntryLong

    @property
    def IndexEntryShort(self):
        '''开仓到当前K线数量-空'''
        return self._lastOrder.IndexEntryShort

    @property
    def IndexLastEntryLong(self):
        '''最后开仓到当前K线的数量-多'''
        return self._lastOrder.IndexLastEntryLong

    @property
    def IndexLastEntryShort(self):
        '''最后开仓到当前K线的数量-空'''
        return self._lastOrder.IndexLastEntryShort

    @property
    def IndexExitLong(self):
        '''平仓到当前K线数量-多'''
        return self._lastOrder.IndexExitLong

    @property
    def IndexExitShort(self):
        '''平仓到当前K线数量-空'''
        return self._lastOrder.IndexExitShort

    @property
    def Position(self):
        '''持仓净头寸'''
        return self.PositionLong - self.PositionShort

    @property
    def CurrentBar(self):
        '''当前K线序号(0开始)'''
        return max(len(self.Bars) - 1, 0)

    def on_tick(self, tick: Tick, tradingday: str):
        '''分笔数据处理'''
        # 避免相同tick重复调用
        if self.Tick.UpdateTime == tick.UpdateTime and self.Tick.Volume == tick.Volume:
            return
        self.Tick = copy.copy(tick)
        # 取此tick对应的分钟时间
        # bar_time = time.strptime(time.strftime("%Y-%m-%d %H:%M", tick.UpdateTime), "%Y-%m-%d %H:%M")
        bar_time = self.Tick.UpdateTime[:-2] + '00'  # time.strftime("%Y%m%d %H:%M:00", time.strptime(tick.UpdateTime, "%Y%m%d %H:%M:%S"))
        if len(self.Bars) == 0 or self.Bars[-1].D != bar_time:  # 新数据
            # bar_time, ins, h, l, o, c, v, i, a)
            bar = Bar(bar_time, self.Tick.Instrument, self.Tick.LastPrice, self.Tick.LastPrice, self.Tick.LastPrice, self.Tick.LastPrice, self.Tick.Volume, self.Tick.OpenInterest, tradingday)
            if len(self.Bars) > 0:
                if self.Bars[-1]._pre_volume == 0:  # 实时行情首K即为新的分钟
                    bar.V = 0
                else:
                    bar.V = self.Tick.Volume - self.Bars[-1]._pre_volume - self.Bars[-1].V
            bar._pre_volume = self.Tick.Volume

            self.__new_min_bar__(bar)  # 新K线数据插入
        else:
            bar = self.Bars[-1]
            bar.H = max(bar.H, self.Tick.LastPrice)
            bar.L = min(bar.L, self.Tick.LastPrice)
            bar.C = self.Tick.LastPrice
            # 当时从服务器取到的数据,与ctp实时数据处于同一分钟,需做衔接处理.
            if bar._pre_volume == 0:
                bar._pre_volume = self.Tick.Volume - bar.V  # 此tick产生的成交量忽略
            else:
                bar.V = self.Tick.Volume - bar._pre_volume
            # bar._pre_volume = tick.Volume
            bar.I = self.Tick.OpenInterest
            bar.A = self.Tick.AveragePrice

            self.__update_bar__(bar)

    def __new_min_bar__(self, bar2):
        """有新min_bar添加"""
        bar = copy.copy(bar2)
        bar_time = time.strptime(bar.D, "%Y-%m-%d %H:%M:%S")
        year = bar_time.tm_year
        mon = bar_time.tm_mon
        day = bar_time.tm_mday
        hour = bar_time.tm_hour
        mins = bar_time.tm_min
        if self.IntervalType == IntervalType.Minute:
            mins = bar_time.tm_min // self.Interval * self.Interval
        elif self.IntervalType == IntervalType.Hour:
            hour = hour // self.Interval
            mins = 0
        elif self.IntervalType == IntervalType.Day:
            hour = 0
            mins = 0
        elif self.IntervalType == IntervalType.Month:
            hour = 0
            mins = 0
            day = 1
        elif self.IntervalType == IntervalType.Year:
            hour = 0
            mins = 0
            day = 1
            mon = 1
        elif self.IntervalType == IntervalType.Week:
            hour = 0
            mins = 0
            # 用周号替换日期
            day = time.strftime('%W', bar_time)

        # time -> str
        bar_time = '{0}{1:02d}{2:02d} {3:02d}:{4:02d}:00'.format(
            year, mon, day, hour, mins)
        if len(self.Bars) == 0 or self.Bars[-1].D != bar_time:
            bar.D = bar_time
            self.Bars.append(bar)

            self.D.append(bar.D)
            self.H.append(bar.H)
            self.L.append(bar.L)
            self.O.append(bar.O)
            self.C.append(bar.C)
            self.V.append(bar.V)
            self.I.append(bar.I)
        else:
            old_bar = self.Bars[-1]
            self.H[-1] = old_bar.H = max(bar.H, old_bar.H)
            self.L[-1] = old_bar.L = min(bar.L, old_bar.L)
            self.C[-1] = old_bar.C = bar.C
            old_bar.V += bar.V
            self.V[-1] = old_bar.V
            self.I[-1] = old_bar.I = bar.I
            # bar.A = tick.AveragePrice

        self.stra_uppdate(self, bar)

    def __update_bar__(self, bar):
        """更新当前数据序列"""

        self.D[-1] = bar.D
        self.H[-1] = bar.H
        self.L[-1] = bar.L
        self.O[-1] = bar.O
        self.C[-1] = bar.C
        self.V[-1] = bar.V
        self.I[-1] = bar.I
        self.stra_uppdate(self, bar)

    def __order__(self, direction, offset, price, volume, remark):
        """策略执行信号"""
        if self.SingleOrderOneBar:
            # 平仓后允许开仓
            if self.ExitDateShort == self.D[-1] and (not (direction == DirectType.Buy and offset == OffsetType.Open)):
                return
            if self.ExitDateLong == self.D[-1] and (not (direction == DirectType.Sell and offset == OffsetType.Open)):
                return
            if self.LastEntryDateLong == self.D[-1] or self.LastEntryDateShort == self.D[-1]:
                return
        # if self.SingleOrderOneBar and (self.LastEntryDateLong == self.D[-1]
        #                                or self.LastEntryDateShort == self.D[-1]
        #                                or self.ExitDateLong == self.D[-1]
        #                                or self.ExitDateShort == self.D[-1]):
        #     return
        order = OrderItem()
        order.Instrument = self.Instrument
        order.DateTime = self.D[-1]
        order.Direction = direction
        order.Offset = offset
        order.Price = price
        order.Volume = volume
        order.Remark = remark

        self.Orders.append(order)

        # 处理策略相关属性
        order.IndexEntryLong = self._lastOrder.IndexEntryLong
        order.IndexExitLong = self._lastOrder.IndexExitLong
        order.IndexEntryShort = self._lastOrder.IndexEntryShort
        order.IndexExitShort = self._lastOrder.IndexExitShort
        order.IndexLastEntryLong = self._lastOrder.IndexLastEntryLong
        order.IndexLastEntryShort = self._lastOrder.IndexLastEntryShort
        order.AvgEntryPriceLong = self._lastOrder.AvgEntryPriceLong
        order.AvgEntryPriceShort = self._lastOrder.AvgEntryPriceShort
        order.PositionLong = self._lastOrder.PositionLong
        order.PositionShort = self._lastOrder.PositionShort
        order.EntryDateLong = self._lastOrder.EntryDateLong
        order.EntryDateShort = self._lastOrder.EntryDateShort
        order.EntryPriceLong = self._lastOrder.EntryPriceLong
        order.EntryPriceShort = self._lastOrder.EntryPriceShort
        order.ExitDateLong = self._lastOrder.ExitDateLong
        order.ExitDateShort = self._lastOrder.ExitDateShort
        order.ExitPriceLong = self._lastOrder.ExitPriceLong
        order.ExitPriceShort = self._lastOrder.ExitPriceShort
        order.LastEntryDateLong = self._lastOrder.LastEntryDateLong
        order.LastEntryDateShort = self._lastOrder.LastEntryDateShort
        order.LastEntryPriceLong = self._lastOrder.LastEntryPriceLong
        order.LastEntryPriceShort = self._lastOrder.LastEntryPriceShort

        diroff = '{0}-{1}'.format(order.Direction.name, order.Offset.name)
        if diroff == 'Buy-Open':
            if self._lastOrder.PositionLong == 0:
                order.IndexEntryLong = len(self.Bars) - 1
                order.EntryDateLong = self.D[-1]  # str '20160630 21:25:00'
                order.EntryPriceLong = order.Price
                order.PositionLong = order.Volume
                order.AvgEntryPriceLong = order.Price
            else:
                order.PositionLong += order.Volume
                order.AvgEntryPriceLong = (self._lastOrder.PositionLong * self._lastOrder.AvgEntryPriceLong + order.Volume * order.Price) / (self._lastOrder.PositionLong + order.Volume)
            order.IndexLastEntryLong = len(self.Bars) - 1
            order.LastEntryPriceLong = order.Price
            order.LastEntryDateLong = self.D[-1]
        elif diroff == 'Buy-Close':
            c_lots = min(self._lastOrder.PositionShort, order.Volume)  # 能够平掉的数量
            if c_lots > 0:  # 避免无仓可平
                order.PositionShort -= c_lots

                order.IndexExitShort = len(self.Bars) - 1
                order.ExitDateShort = self.D[-1]
                order.ExitPriceShort = order.Price
                # if order.PositionShort == 0:
                # order.AvgEntryPriceShort = 0  # 20180906注销方便后期计算盈利
        elif diroff == 'Sell-Open':
            if self._lastOrder.PositionShort == 0:
                order.IndexEntryShort = len(self.Bars) - 1
                order.EntryDateShort = self.D[-1]  # time or double or str ???
                order.EntryPriceShort = order.Price
                order.AvgEntryPriceShort = order.Price
                order.PositionShort = order.Volume
            else:
                order.PositionShort += order.Volume
                order.AvgEntryPriceShort = (self._lastOrder.PositionShort * self._lastOrder.AvgEntryPriceShort + order.Volume * order.Price) / (self._lastOrder.PositionShort + order.Volume)
            order.IndexLastEntryShort = len(self.Bars) - 1
            order.LastEntryPriceShort = order.Price
            order.LastEntryDateShort = self.D[-1]
        elif diroff == 'Sell-Close':
            c_lots = min(self._lastOrder.PositionLong, order.Volume)  # 能够平掉的数量
            if c_lots > 0:  # 避免无仓可平
                order.PositionLong -= c_lots

                order.IndexExitLong = len(self.Bars) - 1
                order.ExitDateLong = self.D[-1]
                order.ExitPriceLong = order.Price
                # if order.PositionLong == 0:
                # order.AvgEntryPriceLong = 0  # 20180906注销方便后期计算盈利

        self._lastOrder = order
        self.stra_onorder(self, order)

    def Buy(self, price: float, volume: int, remark: str = ''):
        """买开"""
        self.__order__(DirectType.Buy, OffsetType.Open, price, volume, remark)

    def Sell(self, price, volume, remark: str = ''):
        """买平"""
        self.__order__(DirectType.Sell, OffsetType.Close, price, volume,
                       remark)

    def SellShort(self, price, volume, remark: str = ''):
        """卖开"""
        self.__order__(DirectType.Sell, OffsetType.Open, price, volume, remark)

    def BuyToCover(self, price, volume, remark: str = ''):
        """买平"""
        self.__order__(DirectType.Buy, OffsetType.Close, price, volume, remark)
