#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  Author:  HaiFeng --<galaxy>
  Purpose: 
  Created: 2016/8/4
"""
import _thread

from py_ctp.ctp_quote import *
from py_ctp.ctp_trade import *


########################################################################
class ctp_test:
	""""""

	#----------------------------------------------------------------------
	def __init__(self):
		"""Constructor"""
		
		self.q = ctp_quote()
		self.t = ctp_trade()
		self.price = 0.0    	

	#----------------------------------------------------------------------
	def OnFrontConnected(self):
		""""""
		print("t:connected by client")
		self.t.ReqUserLogin("008105", "1", "9999")
	
	#----------------------------------------------------------------------
	def relogin(self):
		""""""
		self.t.ReqRelease()
		print('sleep 60 seconds to wait try connect next time')
		sleep(60)
		front = 'tcp://180.168.146.187:10000'
		self.t.ReqConnect(front)
	
	#----------------------------------------------------------------------
	def OnRspUserLogin(self, info):
		""""""
		r = InfoField()
		r = info
		print('{0},{1}'.format(r.ErrorID, r.ErrorMsg))
		if r.ErrorID == 7:
			_thread.start_new_thread(self.relogin, ())
		elif r.ErrorID == 0:
			front = 'tcp://180.168.146.187:10010'
			self.q.ReqConnect(front)
	
	
	#----------------------------------------------------------------------
	def OnOrder(self, field):
		""""""
		f = OrderField()
		f = field
		print('Order:\t{0},{1}'.format(f.Status, f.StatusMsg))
	
	
	#----------------------------------------------------------------------
	def OnTrade(self, field):
		""""""
		f = OrderField()
		f = field
		print('Trade:\t{0},{1},{2}'.format(f.TradeID, f.InstrumentID, f.Price))
	
	
	#----------------------------------------------------------------------
	def OnCancel(self, field):
		""""""
		f = OrderField()
		f = field
		print('Cancel:\t{0},{1}'.format(f.Status, f.StatusMsg))
	
	
	#----------------------------------------------------------------------
	def OnErrorOrder(self, field, info):
		""""""
		f = OrderField()
		f = field
		i = InfoField()
		i = info
		print('Error:\t{0},{1},{2},{3}'.format(i.ErrorID, i.ErrorMsg, f.InstrumentID, f.LimitPrice))
	
	################# quote 
	#----------------------------------------------------------------------
	def q_OnFrontConnected(self):
		""""""
		print("q:connected by client")
		self.q.ReqUserLogin("008105", "1", "9999")
	
	#----------------------------------------------------------------------
	def q_OnRspUserLogin(self, info):
		""""""
		i = InfoField()
		i = info
		print('{0}, {1}'.format(i.ErrorID, i.ErrorMsg))
		self.q.ReqSubscribe("rb1610")
	
	#----------------------------------------------------------------------
	def q_Tick(self, field):
		""""""
		f = MarketData()
		f = field
		self.price = f.LastPrice
		
	######################################

	#----------------------------------------------------------------------
	def main(self):
		""""""
	
		self.q.OnFrontConnected = self.q_OnFrontConnected
		self.q.OnUserLogin = self.q_OnRspUserLogin
		self.q.OnRtnTick = self.q_Tick
	
		self.t.OnFrontConnected = self.OnFrontConnected
		self.t.OnUserLogin = self.OnRspUserLogin
		self.t.OnRtnOrder = self.OnOrder
		self.t.OnRtnTrade = self.OnTrade
		self.t.OnRtnCancel = self.OnCancel
		self.t.OnRtnErrOrder = self.OnErrorOrder
		
		front = 'tcp://180.168.146.187:10000'
		self.t.ReqConnect(front)
		get = input()
		while True:
			#LIMIT/FAK/FOK/MARKET测试完成
			if get == 'p':
				for pf in self.t.DicPositionField:
					print('{0},{1}'.format(pf, self.t.DicPositionField[pf]))
			elif get == 'order':
				self.t.ReqOrderInsert("rb1610",  DirectionType.Sell, OffsetFlagType.Open, self.price, 1, OrderType.Limit, 10)
				#self.t.ReqOrderInsert("rb1610",  DirectionType.Sell, OffsetFlagType.Open, 0, 1, OrderType.Market, 10)
			get = input()

if __name__ == '__main__':
	m = ctp_test()
	m.main()