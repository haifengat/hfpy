#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/8/16'
"""

import time

from py_at.OrderItem import OrderItem
from py_at.EnumDefine import *
from py_at.Bar import Bar
from py_at.Tick import Tick
from py_at.switch import switch


class Data(object):
	'''数据类, 策略继承此类'''

	def __init__(self):
		'''初始所有变量'''
		# 序列变量
		self.Bars = []
		self.D = []
		self.H = []
		self.L = []
		self.O = []
		self.C = []
		self.V = []
		self.I = []

		self.DateD = []
		self.OpenD = []
		self.HighD = []
		self.LowD = []
		self.CloseD = []

		self.Instrument = ''
		self.Interval = 1
		self.IntervalType = IntervalType.Minute
		self.BeginDate = '20160101'  # 注意日期格式
		self.EndDate = time.strftime("%Y%m%d", time.localtime())  # 默认值取当日

		self.Tick = Tick()
		self.Params = {}
		self.Orders = []

		self._lastOrder = OrderItem()

	# 当前策略相关
	@property
	def AvgEntryPriceShort(self):
		return self._lastOrder.AvgEntryPriceShort

	@property
	def AvgEntryPriceLong(self):
		return self._lastOrder.AvgEntryPriceLong

	@property
	def PositionLong(self):
		return self._lastOrder.PositionLong

	@property
	def PositionShort(self):
		return self._lastOrder.PositionShort

	@property
	def EntryDateLong(self):
		return self._lastOrder.EntryDateLong

	@property
	def EntryPriceLong(self):
		return self._lastOrder.EntryPriceLong

	@property
	def ExitDateShort(self):
		return self._lastOrder.ExitDateShort

	@property
	def ExitPriceShort(self):
		return self._lastOrder.ExitPriceShort

	@property
	def EntryDateShort(self):
		return self._lastOrder.EntryDateShort

	@property
	def EntryPriceShort(self):
		return self._lastOrder.EntryPriceShort

	@property
	def ExitDateLong(self):
		return self._lastOrder.ExitDateLong

	@property
	def ExitPriceLong(self):
		return self._lastOrder.ExitPriceLong

	@property
	def LastEntryDateShort(self):
		return self._lastOrder.LastEntryDateShort

	@property
	def LastEntryPriceShort(self):
		return self._lastOrder.LastEntryPriceShort

	@property
	def LastEntryDateLong(self):
		return self._lastOrder.LastEntryDateLong

	@property
	def LastEntryPriceLong(self):
		return self._lastOrder.LastEntryPriceLong

	@property
	def IndexEntryLong(self):
		return self._lastOrder.IndexEntryLong

	@property
	def IndexEntryShort(self):
		return self._lastOrder.IndexEntryShort

	@property
	def IndexLastEntryLong(self):
		return self._lastOrder.IndexLastEntryLong

	@property
	def IndexLastEntryShort(self):
		return self._lastOrder.IndexLastEntryShort

	@property
	def IndexExitLong(self):
		return self._lastOrder.IndexExitLong

	@property
	def IndexExitShort(self):
		return self._lastOrder.IndexExitShort

	@property
	def Position(self):
		return self.PositionLong - self.PositionShort

	@property
	def CurrentBar(self):
		return max(len(self.Bars) - 1, 0)

	def on_tick(self, tick):
		self.Tick = tick
		''' 取此tick对应的分钟时间'''
		#bar_time = time.strptime(time.strftime("%Y-%m-%d %H:%M", tick.UpdateTime), "%Y-%m-%d %H:%M")
		bar_time = time.strftime("%Y-%m-%d %H:%M:00", tick.UpdateTime)
		if len(self.Bars) == 0 or self.Bars[0].D != bar_time:  # 新数据
			# bar_time, h, l, o, c, v, i, a)
			bar = Bar(bar_time, tick.LastPrice, tick.LastPrice, tick.LastPrice, tick.LastPrice, tick.Volume, tick.OpenInterest)
			bar._pre_volume = tick.Volume

			self.__new_min_bar__(bar)  # 新K线数据插入
		else:
			bar = self.Bars[0]
			bar.H = max(bar.H, tick.LastPrice)
			bar.L = min(bar.L, tick.LastPrice)
			bar.C = tick.LastPrice
			bar.V = tick.Volume - bar._pre_volume
			bar._pre_volume = tick.Volume
			bar.I = tick.OpenInterest
			bar.A = tick.AveragePrice

			self.__update_bar__(bar)

	def __new_min_bar__(self, bar):
		"""有新min_bar添加"""

		bar_time = time.strptime(bar.D, "%Y%m%d %H:%M:%S")
		year = bar_time.tm_year
		mon = bar_time.tm_mon
		day = bar_time.tm_mday
		hour = bar_time.tm_hour
		mins = bar_time.tm_min
		for case in switch(self.IntervalType):
			if case(IntervalType.Minute):
				mins = bar_time.tm_min // self.Interval * self.Interval
				break
			if case(IntervalType.Hour):
				hour = hour // self.Interval
				mins = 0
				break
			if case(IntervalType.Day):
				hour = 0
				mins = 0
				break
			if case(IntervalType.Month):
				hour = 0
				mins = 0
				day = 1
				break
			if case(IntervalType.Year):
				hour = 0
				mins = 0
				day = 1
				mon = 1
				break
			if case(IntervalType.Week):
				hour = 0
				mins = 0
				# 用周号替换日期
				day = time.strftime('%W', bar_time)
				break

		bar_time = time.strptime('{0}-{1}-{2} {3}:{4}'.format(year, mon, day, hour, mins), '%Y-%m-%d %H:%M')
		#time -> str
		bar_time = time.strftime('%Y-%m-%d %H:%M:%S', bar_time)
		if len(self.Bars) == 0 or self.Bars[0].D != bar_time:
			bar.D = bar_time
			self.Bars.insert(0, bar)

			self.D.insert(0, bar.D)
			self.H.insert(0, bar.H)
			self.L.insert(0, bar.L)
			self.O.insert(0, bar.O)
			self.C.insert(0, bar.C)
			self.V.insert(0, bar.V)
			self.I.insert(0, bar.I)
		else:
			old_bar = self.Bars[0]
			bar.H = max(bar.H, old_bar.H)
			bar.L = min(bar.L, old_bar.L)
			bar.C = old_bar.C
			bar.V += old_bar.V
			#bar.I = .OpenInterest
			#bar.A = tick.AveragePrice
		#日线数据处理
		date = '{0}-{1}-{2}'.format(year, mon, day)
		if len(self.DateD) == 0 or self.DateD[0] != date:
			self.DateD.insert(0, date)
			self.OpenD.insert(0, bar.O)
			self.HighD.insert(0, bar.H)
			self.LowD.insert(0, bar.L)
			self.CloseD.insert(0, bar.C)
		else:
			self.HighD[0] = max(self.HighD[0], bar.H)
			self.LowD[0] = min(self.LowD[0], bar.L)
			self.CloseD[0] = bar.C

		self.BarUpdate(bar)

	def __update_bar__(self, bar):
		"""更新当前数据序列"""

		self.D[0] = bar.D
		self.H[0] = bar.H
		self.L[0] = bar.L
		self.O[0] = bar.O
		self.C[0] = bar.C
		self.V[0] = bar.V
		self.I[0] = bar.I

		self.HighD[0] = max(self.HighD[0], bar.H)
		self.LowD[0] = min(self.LowD[0], bar.L)
		self.CloseD[0] = bar.C

		self.BarUpdate(bar)

	def BarUpdate(self, bar):
		"""数据更新时调用此函数"""
		pass

	def OnOrder(self, stra, order):
		"""继承类中实现此函数,有策略信号产生时调用"""
		pass

	def __order__(self, direction, offset, price, volume, remark):
		"""策略执行信号"""

		order = OrderItem()
		order.Instrument = self.Instrument
		order.DateTime = self.D[0]
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
		for case in switch(diroff):
			if case('Buy-Open'):
				order.PositionLong += order.Volume
				order.AvgEntryPriceLong = (self._lastOrder.PositionLong * self._lastOrder.AvgEntryPriceLong + order.Volume * order.Price) / (self._lastOrder.Volume + order.Volume)
				if self._lastOrder.PositionLong == 0:
					order.IndexEntryLong = len(self.Bars) - 1
					order.EntryDateLong = self.D[0]  # str '20160630 21:25:00'
					order.EntryPriceLong = order.Price
				order.IndexLastEntryLong = len(self.Bars) - 1
				order.LastEntryPriceLong = order.Price
				order.LastEntryDateLong = self.D[0]
				break

			if case('Buy-Close'):
				c_lots = min(self._lastOrder.PositionShort, order.Volume)  # 能够平掉的数量
				if c_lots <= 0:  # 无仓可平
					print('平仓量>持仓量')
					break
				order.PositionShort -= c_lots

				order.IndexExitShort = len(self.Bars) - 1
				order.ExitDateShort = self.D[0]
				order.ExitPriceShort = order.Price
				break

			if case('Sell-Open'):
				order.PositionShort += order.Volume
				order.AvgEntryPriceShort = (self._lastOrder.PositionShort * self._lastOrder.AvgEntryPriceShort + order.Volume * order.Price) / (self._lastOrder.Volume + order.Volume)
				if self._lastOrder.PositionShort == 0:
					order.IndexEntryShort = len(self.Bars) - 1
					order.EntryDateShort = self.D[0]  # time or double or str ???
					order.EntryPriceShort = order.Price
				order.IndexLastEntryShort = len(self.Bars) - 1
				order.LastEntryPriceShort = order.Price
				order.LastEntryDateShort = self.D[0]
				break

			if case('Sell-Close'):
				c_lots = min(self._lastOrder.PositionLong, order.Volume)  # 能够平掉的数量
				if c_lots <= 0:  # 无仓可平
					print('平仓量>持仓量')
					break
				order.PositionLong -= c_lots

				order.IndexExitLong = len(self.Bars) - 1
				order.ExitDateLong = self.D[0]
				order.ExitPriceLong = order.Price
				break

		self._lastOrder = order

		self.OnOrder(self, order)

	def Buy(self, price, volume, remark):
		"""买开"""
		self.__order__(Direction.Buy, Offset.Open, price, volume, remark)

	def Sell(self, price, volume, remark):
		"""买开"""
		self.__order__(Direction.Sell, Offset.Close, price, volume, remark)

	def SellShort(self, price, volume, remark):
		"""买开"""
		self.__order__(Direction.Sell, Offset.Open, price, volume, remark)

	def BuyToCover(self, price, volume, remark):
		"""买开"""
		self.__order__(Direction.Buy, Offset.Close, price, volume, remark)
