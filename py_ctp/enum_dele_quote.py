#!/usr/bin/env python
#coding:utf-8
"""
  Author:  HaiFeng --<galaxy>
  Purpose: enum of delegate
  Created: 2016/7/4
"""

from enum import *

class EnumDelegate(Enum):

	OnFrontConnected = 1-1
	OnFrontDisconnected = 2-1
	OnHeartBeatWarning = 3-1
	OnRspUserLogin = 4-1
	OnRspUserLogout = 5-1
	OnRspError = 6-1
	OnRspSubMarketData = 7-1
	OnRspUnSubMarketData = 8-1
	OnRtnDepthMarketData = 9-1

	#----------------------------------------------------------------------	
	def __int__(self):
		return self.value
