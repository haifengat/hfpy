#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/8/16'

Purpose: 定义enum类型,在at平台层使用,注意与底层(如CTP)之间的类型转换
"""


from enum import Enum

########################################################################
class Direction(Enum):
	"""买卖方向"""
   
	Buy = 0
	Sell = 1

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

########################################################################
class Offset(Enum):
	"""开平"""
    
	Open = 0
	Close = 1

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value	


########################################################################
class IntervalType(Enum):
	"""时间类型:秒,分,时,日,周,月,年"""
    
	Second = 0
	Minute = 1
	Hour = 2
	Day = 3
	Week = 4
	Month = 5
	Year = 6

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

########################################################################
class BarType(Enum):
	""""""
	Min = 0
	Day = 1
	Real = 2
	Time = 3
	Product = 4
	TradeDate = 5

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value
	
########################################################################
class ReqPackage:
	"""数据请求格式包"""

	#----------------------------------------------------------------------
	def __init__(self):
		"""Constructor"""

		self.Type = 0
		self.Instrument = ''
		self.Begin = ''
		self.End = ''	
		