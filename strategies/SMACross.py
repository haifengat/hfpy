#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/8/16'
"""
import talib

from py_at.EnumDefine import *
from py_at.Data import Data

class SMACross(Data):
	def __init__(self):
		super().__init__()
		self.p_ma1 = self.Params['MA1'] = 10
		self.p_ma2 = self.Params['MA2'] = 60
		self.p_lots = self.Params['Lots'] = 1

		self.Instrument = 'rb1701'
		self.Interval = 15
		self.IntervalType = IntervalType.Minute
		self.BeginDate = '20160701'
		#self.EndDate= ''

	def UpdateParams(self):
		self.p_ma1 = self.Params['MA1']
		self.p_ma2 = self.Params['MA2']
		self.p_lots = self.Params['Lots']

	def BarUpdate(self):
		if len(self.C) == 1:
			self.UpdateParams()
		if len(self.C) < self.p_ma2:
			return

		ma1 = talib.SMA(self.C, self.p_ma1)
		ma2 = talib.SMA(self.C, self.p_ma2)

		self.IndexDict['ma5'] = ma1
		self.IndexDict['ma10'] = ma2

		if self.PositionLong == 0:
			if ma1[-1] >= ma2[-1] and ma1[-2] < ma2[-2]:
				if self.PositionShort > 0:
					self.BuyToCover(self.O[-1], self.p_lots, '买平')
				self.Buy(self.O[-1], self.p_lots, '买开')
		elif self.PositionShort == 0:
			if ma1[-1] <= ma2[-1] and ma1[-2] > ma2[-2]:
				if self.PositionLong > 0:
					self.Sell(self.O[-1], self.p_lots, '卖平')
				self.SellShort(self.O[-1], self.p_lots, '卖开')

