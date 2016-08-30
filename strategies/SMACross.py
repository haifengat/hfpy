#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/8/16'
"""
from py_at.EnumDefine import *
from strategies.SMA import SMA
from py_at.Data import Data

class SMACross:
	def __init__(self):
		super().__init__()
		self.p_ma1 = self.Params['MA1'] = 5
		self.p_ma2 = self.Params['MA2'] = 10
		self.p_lots = self.Params['Lots'] = 1

		self.Instrument = 'rb1610'
		self.Interval = 5
		self.IntervalType = IntervalType.Minute
		self.BeginDate = '20160701'
		#self.EndDate= ''

		self.sma1 = SMA(self.C, self.p_ma1)
		self.sma2 = SMA(self.C, self.p_ma2)

		self.flog = open('ma1', 'w')
	def BarUpdate(self, bar):

		self.sma1.Update()
		self.sma2.Update()
		if len(self.sma1.Result) < self.p_ma1 or len(self.sma2.Result) < self.p_ma2:
			return
		ma1 = self.sma1.Result
		ma2 = self.sma2.Result

		if self.PositionLong == 0:
			if ma1[1] >= ma2[1] and ma1[2] < ma2[2]:
				if self.PositionShort > 0:
					self.BuyToCover(self.O[0], self.p_lots, '买平')
				self.Buy(self.O[0], self.p_lots, '买开')
		elif self.PositionShort == 0:
			if ma1[1] <= ma2[1] and ma1[2] > ma2[2]:
				if self.PositionLong > 0:
					self.Sell(self.O[0], self.p_lots, '卖平')
				self.SellShort(self.O[0], self.p_lots, '卖开')

