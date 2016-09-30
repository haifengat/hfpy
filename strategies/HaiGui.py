#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '海龟交易法则'
__author__ = 'HaiFeng'
__mtime__ = '2016/8/25'
"""

from py_at.Data import Data
from py_at.EnumDefine import *
import talib


class HaiGui(Data):
	""""""

	def __init__(self):
		super().__init__()

		self.Instrument = 'rb1610'
		self.Interval = 15
		self.IntervalType = IntervalType.Minute
		self.BeginDate = '20160101'

		self.Params['Lots'] = 1

		self.SingleOrderOneBar = True

		self.Params['RiskRatio'] = 1  # % Risk Per N ( 0 - 100)
		self.Params['ATRLength'] = 20  # 平均波动周期 ATR Length
		self.Params['boLength'] = 20  # 短周期 BreakOut Length
		self.Params['fsLength'] = 55  # 长周期 FailSafe Length
		self.Params['teLength'] = 10  # 离市周期 Trailing Exit Lengt

	def BarUpdate(self):
		""""""
		if self.CurrentBar < self.Params['fsLength']:
			return
		atr = talib.ATR(self.H, self.L, self.C, 14)

		lots = self.Params['Lots']

		DonchianHi = talib.MAX(self.H, self.Params['boLength'])[-2]
		DonchianLo = talib.MIN(self.L, self.Params['boLength'])[-2]

		fsDonchianHi = talib.MAX(self.H, self.Params['fsLength'])[-2]
		fsDonchianLo = talib.MIN(self.L, self.Params['fsLength'])[-2]

		ExitHighestPrice = talib.MAX(self.H, self.Params['teLength'])[-2]
		ExitLowestPrice = talib.MIN(self.L, self.Params['teLength'])[-2]

		if len(atr) < 2:
			return

		N = atr[-2]

		if self.Position == 0:
			if self.H[-1] > DonchianHi:
				price = max(min(self.H[-1], DonchianHi), self.O[-1])
				self.Buy(price, lots, '上轨')
			elif self.L[-1] < DonchianLo:
				price = min(max(self.L[-1], DonchianLo), self.O[-1])
				self.SellShort(price, lots, '下轨')
			#长期突破
			elif self.H[-1] > fsDonchianHi:
				price = max(min(self.H[-1], fsDonchianHi), self.O[-1])
				self.Buy(price, lots, '上轨-fs')
			elif self.L[-1] < fsDonchianLo:
				price = min(max(self.L[-1], fsDonchianLo), self.O[-1])
				self.SellShort(price, lots, '下轨-fs')

		elif self.Position > 0:
			if self.L[-1] < ExitLowestPrice:
				price = min(self.O[-1], max(self.L[-1], ExitLowestPrice))
				self.Sell(price, self.PositionLong, 'exit-价格需优化')
			else:
				if self.H[-1] >= self.LastEntryPriceLong + 0.5 * N:
					price = max(self.O[-1], self.LastEntryPriceLong + 0.5 * N)
					self.Buy(price, lots, '{0},{1}'.format(N, '加仓-多'))
		elif self.Position < 0:
			if self.H[-1] > ExitHighestPrice:
				price = max(self.O[-1], min(self.H[-1], ExitHighestPrice))
				self.BuyToCover(price, self.PositionShort, 'exit')
			else:
				if self.L[-1] <= self.LastEntryPriceShort - 0.5 * N:
					price = min(self.O[-1], self.LastEntryPriceShort - 0.5 * N)
					self.SellShort(price, lots, '{0},{1}'.format(N, '加仓-空'))

	def FixPrice(self, dire, price):
		"""修正发单价格"""
		if dire == Direction.Buy:
			return max(self.O[-1], price)
		else:
			return min(self.O[-1], price)
