#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '海龟交易法则'
__author__ = 'HaiFeng'
__mtime__ = '2016/8/25'
"""
from strategies.TrueRange import TrueRange
from py_at.Data import Data
from py_at.EnumDefine import *
from strategies.SMA import SMA
import sys

class HaiGui(Data):
	""""""

	def __init__(self):
		super().__init__()

		self.Instrument = 'rb1610'
		self.Interval = 15
		self.IntervalType = IntervalType.Minute
		self.BeginDate = '20160101'

		self.Params['Lots'] = 1

		self.Params['RiskRatio'] = 1  # % Risk Per N ( 0 - 100)
		self.Params['ATRLength'] = 20  # 平均波动周期 ATR Length
		self.Params['boLength'] = 20  # 短周期 BreakOut Length
		self.Params['fsLength'] = 55  # 长周期 FailSafe Length
		self.Params['teLength'] = 10  # 离市周期 Trailing Exit Lengt

		self.TR = TrueRange(self.H, self.L, self.C)
		#self.TR = TrueRange(self.HighD, self.LowD, self.CloseD)
		self.ATR = None

	def BarUpdate(self, bar):
		""""""
		self.TR.Update()
		if not self.ATR:
			self.ATR = SMA(self.TR.Result, self.Params['ATRLength'])
		self.ATR.Update()
		if self.CurrentBar < self.Params['fsLength']:
			return

		lots = self.Params['Lots']

		DonchianHi = 0
		for i in range(1, self.Params['boLength'] + 1):
			DonchianHi = max(DonchianHi, self.H[i])
		DonchianLo = sys.float_info.max
		for i in range(1, self.Params['boLength'] + 1):
			DonchianLo = min(DonchianLo, self.L[i])

		fsDonchianHi = 0
		for i in range(1, self.Params['fsLength'] + 1):
			fsDonchianHi = max(fsDonchianHi, self.H[i])
		fsDonchianLo = sys.float_info.max
		for i in range(1, self.Params['fsLength'] + 1):
			fsDonchianLo = min(fsDonchianLo, self.L[i])

		ExitHighestPrice = 0
		for i in range(1, self.Params['teLength'] + 1):
			ExitHighestPrice = max(ExitHighestPrice, self.H[i])
		ExitLowestPrice = sys.float_info.max
		for i in range(1, self.Params['teLength'] + 1):
			ExitLowestPrice = min(ExitLowestPrice, self.L[i])

		##大周期的策略,会因为小周期数据而多次同bar调用
		if self.LastEntryDateLong == self.D[0] or self.LastEntryDateShort == self.D[0] or self.ExitDateLong == self.D[0] or self.ExitDateShort == self.D[0]:
			return

		if len(self.ATR.Result) < 2:
			return

		N = self.ATR.Result[1]

		if self.Position == 0:
			if self.H[0] > DonchianHi:
				price = max(min(self.H[0], DonchianHi), self.O[0])
				self.Buy(price, lots, '上轨')
			elif self.L[0] < DonchianLo:
				price = min(max(self.L[0], DonchianLo), self.O[0])
				self.SellShort(price, lots, '下轨')
			#长期突破
			elif self.H[0] > fsDonchianHi:
				price = max(min(self.H[0], fsDonchianHi), self.O[0])
				self.Buy(price, lots, '上轨-fs')
			elif self.L[0] < fsDonchianLo:
				price = min(max(self.L[0], fsDonchianLo), self.O[0])
				self.SellShort(price, lots, '下轨-fs')

		elif self.Position > 0:
			if self.L[0] < ExitLowestPrice:
				price = min(self.O[0], max(self.L[0], ExitLowestPrice))
				self.Sell(price, self.PositionLong, 'exit-价格需优化')
			else:
				if self.H[0] >= self.LastEntryPriceLong + 0.5 * N:
					self.Buy(self.LastEntryPriceLong + 0.5 * N, lots, '{0},{1}'.format(N, '加仓-多'))
		elif self.Position < 0:
			if self.H[0] > ExitHighestPrice:
				price = max(self.O[0], min(self.H[0], ExitHighestPrice))
				self.BuyToCover(price, self.PositionShort, 'exit')
			else:
				if self.L[0] <= self.LastEntryPriceShort - 0.5 * N:
					self.SellShort(self.LastEntryPriceShort - 0.5 * N, lots, '{0},{1}'.format(N, '加仓-空'))

	def FixPrice(self, dire, price):
		"""修正发单价格"""
		if dire == Direction.Buy:
			return max(self.O[0], price)
		else:
			return min(self.O[0], price)
