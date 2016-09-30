#!/usr/bin/env python
#coding:utf-8

import time
from py_at.Data import Data

from py_at.EnumDefine import *


class Strategy(Data):
	"""继承数据完成策略"""
	
	def __init__(self):
		print("srategy runing...")
		super().__init__()
		self.Params["a"] = 5
		self.Params["d"] = time.localtime(time.time())
		self.order = False	#控制只发一次
		self.Instrument = 'cu1610'
		self.BeginDate = '20160501'
		self.EndDate = '20160811'
		self.Interval = 5
		self.IntervalType = BarType.Min
    
	#----------------------------------------------------------------------
	def BarUpdate(self):
		"""strategy on_bar"""
		bar = self.Bars[0]
		#print(bar)
		
		#测试交易
		if self.Tick.Instrument:
			if not self.order or self.Tick.UpdateTime.tm_sec == 0:
				self.order = True
				self.Buy(self.C[-1], 1, "test")#平今与平昨处理
		
		