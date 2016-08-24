#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/8/16'
"""

import time

########################################################################
class Tick:
	"""Tick数据"""

	#----------------------------------------------------------------------
	def __init__(self):
		"""Constructor"""		
		
		self.Instrument = ''
		self.LastPrice = 0.0
		self.AskPrice = 0.0
		self.BidPrice = 0.0
		self.AskVolume = 1
		self.BidVolume = 1
		self.UpdateTime = time.localtime()
		self.Volume = 1
		self.OpenInterest = 1.0
		self.AveragePrice = 0.0
		
	#----------------------------------------------------------------------
	def __str__(self):
		""""""
		return '{self.Instrument}, {self.LastPrice}, {self.BidPrice}, {self.BidVolume}, {self.UpdateTime}, {self.Volume}, {self.OpenInterest}, {self.AveragePrice}'.format(self = self)