#!/usr/bin/env python
#coding:utf-8
"""
  Author:  HaiFeng --<galaxy>
  Purpose: enum of command
  Created: 2016/7/4
"""

from enum import *

class EnumReq(Enum):
	"""enum for request command"""
	Release = 1-1
	"""dis"""
	Init = 2-1
	"""initialize"""
	Join = 3-1
	GetTradingDay = 4-1
	RegisterFront = 5-1
	RegisterNameServer = 6-1
	RegisterSpi = 7-1
	SubscribeMarketData = 8-1
	UnSubscribeMarketData = 9-1
	ReqUserLogin = 10-1
	ReqUserLogout = 11-1
	
	#----------------------------------------------------------------------	
	def __int__(self):
		return self.value
	