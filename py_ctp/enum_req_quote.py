#!/usr/bin/env python
#coding:utf-8
"""
  Author:  HaiFeng --<galaxy>
  Purpose: enum of command
  Created: 2016/7/4
"""

from enum import Enum

class EnumReq(Enum):
	"""enum for request command"""
	Release = 0
	Init = 1
	Join = 2
	GetTradingDay = 3
	RegisterFront = 4
	RegisterNameServer = 5
	RegisterSpi = 6
	SubscribeMarketData = 7
	UnSubscribeMarketData = 8
	ReqUserLogin = 9
	ReqUserLogout = 10
	
	#----------------------------------------------------------------------	
	def __int__(self):
		return self.value
	