#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/8/16'
"""

import time
from py_at.EnumDefine import *

########################################################################
class OrderItem(object):
	"""策略信号"""

	#----------------------------------------------------------------------
	def __init__(self):
		"""Constructor"""
		
		self.Instrument = ''
		self.DateTime = time.strftime('%Y%m%d %H:%Mm:%S', time.localtime(time.time()))
		self.Direction = Direction.Buy
		self.Offset = Offset.Open
		self.Price = 0.0
		self.Volume = 0
		self.Remark = ''
		self.RelationOpenOrders = []
		#策略相关
		self.AvgEntryPriceShort = 0.0
		self.AvgEntryPriceLong = 0.0
		self.PositionLong = 0
		self.PositionShort = 0
		self.EntryDateLong = ''
		self.EntryPriceLong = 0.0
		self.ExitDateShort = ''
		self.ExitPriceShort = 0.0
		self.EntryDateShort = ''
		self.EntryPriceShort = 0.0
		self.ExitDateLong = ''
		self.ExitPriceLong = 0.0
		self.LastEntryDateShort = ''
		self.LastEntryPriceShort = 0.0
		self.LastEntryDateLong = ''
		self.LastEntryPriceLong = 0.0

		self.IndexEntryLong = -1
		self.IndexEntryShort = -1
		self.IndexLastEntryLong = -1
		self.IndexLastEntryShort = -1

		self.IndexExitLong = -1
		self.IndexExitShort = -1

	#----------------------------------------------------------------------
	def __str__(self):
		""""""
		return '{self.Instrument}, {self.DateTime}, {self.Direction}, {self.Offset}, {self.Price}, {self.Volume}, {self.Remark}'.format(self = self)