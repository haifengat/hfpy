#!/usr/bin/env python
#coding:utf-8
"""
  Author:  HaiFeng --<galaxy>
  Purpose: enum of delegate
  Created: 2016/7/4
"""

from enum import Enum

class EnumDelegate(Enum):

	OnFrontConnected = 0
	OnFrontDisconnected = 1
	OnHeartBeatWarning = 2
	OnRspUserLogin = 3
	OnRspUserLogout = 4
	OnRspError = 5
	OnRspSubMarketData = 6
	OnRspUnSubMarketData = 7
	OnRtnDepthMarketData = 8

	#----------------------------------------------------------------------	
	def __int__(self):
		return self.value
