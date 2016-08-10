#!/usr/bin/env python
#coding:utf-8
"""
  Author:  HaiFeng --<galaxy>
  Purpose: order fields type of all api of trade
  Created: 2016/7/28
"""
from enum import *
from ctp_struct import *
from ctp_enum import *

########################################################################
class OffsetType(Enum):
	""""""
	Open = 0
	Close = 1
	CloseToday = 2

	#----------------------------------------------------------------------	
	def __int__(self):
		return self.value
    
	

########################################################################
class OrderType(Enum):
	""""""
	Limit = 0,
	Market = 1,
	FAK = 2,
	FOK = 3


	#----------------------------------------------------------------------	
	def __int__(self):
		return self.value
	
########################################################################
class OrderStatus(Enum):
	""""""
	Normal = 0
	Partial = 1
	Filled = 2
	Canceled = 3	
	Error = 4
		
	#----------------------------------------------------------------------	
	def __int__(self):
		return self.value
	
########################################################################
class InfoField:
	""""""

	
	#----------------------------------------------------------------------
	def __init__(self):
		"""Constructor"""
		self.ErrorID = 0
		self.ErrorMsg = '正确'
		
		
    
	

########################################################################
class OrderField:
	"""报单响应"""
	
	#----------------------------------------------------------------------
	def __init__(self):
		"""initionalize"""
		
		self.OrderID = ""
		self.InstrumentID = ""
		self.Direction = DirectionType.Buy
		self.Offset = OffsetFlagType.Open
		self.LimitPrice = 0.0
		self.AvgPrice = 0.0
		self.InsertTime = ""
		self.TradeTime = ""
		self.TradeVolume = 0
		self.Volume = 0
		self.VolumeLeft = 0
		self.Status = OrderStatus.Normal
		self.StatusMsg = ""
		self.IsLocal = False
		self.Custom = 0
		self.SysID = ""
	
	#----------------------------------------------------------------------
	def __str__(self):
		""""""
		return '''self.OrderID, self.InstrumentID, self.Direction, self.Offset, self.LimitPrice, self.AvgPrice, 
		    self.InsertTime, self.TradeTime, self.TradeVolume, self.Volume, self.VolumeLeft, self.Status,
		    self.StatusMsg, self.IsLocal, self.Custom, self.SysID'''.format(self = self)

########################################################################
class TradeField:
	"""成交响应"""
	
	
	#----------------------------------------------------------------------
	def __init__(self):
		"""Constructor"""
		self.TradeID = ''
		self.InstrumentID = ''
		self.ExchangeID = ''
		self.Direction = DirectionType.Buy
		self.Offset = OffsetFlagType.Open
		self.Price = 0.0
		self.Volume = 0
		self.TradeTime = ''
		self.TradingDay = ''
		self.OrderID = ''
		self.SysID = ''
    
	#----------------------------------------------------------------------
	def __str__(self):
		""""""
		return '''self.TradeID, self.InstrumentID, self.ExchangeID, self.Direction, self.Offset, self.Price, self.Volume, 
			self.TradeTime, self.TradingDay, self.OrderID, self.SysID'''.format(self = self)

########################################################################
class InstrumentField:
	"""合约"""

	#----------------------------------------------------------------------
	def __init__(self):
		"""Constructor"""
		
		self.InstrumentID = ''
		self.ProductID = ''
		self.ExchangeID = ''
		self.VolumeMultiple = ''
		self.PriceTick = 0.0
		self.MaxOrderVolume = 9999
	#----------------------------------------------------------------------
	def __str__(self):
		""""""
		return 'self.InstrumentID, self.ProductID, self.ExchangeID, self.VolumeMultiple, self.PriceTick, self.MaxOrderVolume'.format(self = self)
	

########################################################################
class TradingAccount:
	"""交易帐户"""

	#----------------------------------------------------------------------
	def __init__(self):
		"""Constructor"""
		
		self.PreBalance = 0.0
		self.PositionProfit = 0.0
		self.CloseProfit = 0.0
		self.Commission = 0.0
		self.CurrMargin = 0.0
		self.FrozenCash = 0.0
		self.Available = 0.0
		self.Fund = 0.0
		self.Risk = 0.0
	#----------------------------------------------------------------------
	def __str__(self):
		""""""
		return 'self.PreBalance, self.PositionProfit, self.CloseProfit, self.Commission, self.CurrMargin, self.FrozenCash, self.Available, self.Fund, self.Risk'.format(self = self)
    
########################################################################
class PositionField:
	"""持仓"""

	#----------------------------------------------------------------------
	def __init__(self):
		"""Constructor"""
		
		self.InstrumentID = ''
		self.Direction = DirectionType.Buy
		self.Price = 0.0
		self.Position = 1
		self.YdPosition = 0
		self.TdPosition = 0
		self.CloseProfit = 0.0
		self.PositionProfit = 0.0
		self.Commission = 0.0
		self.Margin = 0.0
	
	#----------------------------------------------------------------------
	def __str__(self):
		""""""
		return '''{self.InstrumentID}, {self.Direction}, {self.Price}, {self.Position}, {self.TdPosition}, {self.YdPosition}, {
			self.CloseProfit}, {self.PositionProfit}, {self.Commission}, {self.Margin}'''.format(self=self)
	

########################################################################
class MarketData:
	"""行情"""

	#----------------------------------------------------------------------
	def __init__(self):
		"""Constructor"""
		
		self.InstrumentID = ''
		self.LastPrice = 0.0
		self.BidPrice = 0.0
		self.BidVolume = 1
		self.AskPrice = 0.0
		self.AskVolume = 1
		self.AveragePrice = 0.0
		self.Volume = 1
		self.OpenInterest = 0.0
		self.UpdateTime = ''
		self.UpdateMillisec = 0
		self.UpperLimitPrice = 0.0
		self.LowerLimitPrice = 0.0
	#----------------------------------------------------------------------
	def __str__(self):
		""""""
		return '''self.InstrumentID, self.LastPrice, self.BidPrice, self.BidVolume, self.AskPrice, self.AskVolume, self.AveragePrice, 
		self.Volume, self.OpenInterest, self.UpdateTime, self.UpdateMillisec, self.UpperLimitPrice, self.LowerLimitPrice'''.format(self = self)

