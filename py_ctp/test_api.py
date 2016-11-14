#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/9/13'
"""

from py_ctp.ctp_struct import *
from py_ctp.trade import Trade
from py_ctp.quote import Quote
import _thread
from time import sleep

class Test:

	def __init__(self):
		self.Session = ''
		self.q = Quote()
		self.t = Trade()
		self.req = 0
		self.ordered = False

	def q_OnFrontConnected(self):
		print('connected')
		self.q.ReqUserLogin(BrokerID='9999', UserID='xxx', Password='***')

	def q_OnRspUserLogin(self, rsp, info, req, last):
		print('quote')
		print(info)

		#insts = create_string_buffer(b'cu', 5)
		self.q.SubscribeMarketData('rb1701')

	def q_OnTick(self, tick):
		f = CThostFtdcMarketDataField()
		f = tick
		print(tick)

		if not self.ordered:
			_thread.start_new_thread(self.Order, (f,))
			self.ordered = True

	def Order(self, f):
		self.req += 1
		self.t.ReqOrderInsert(
			BrokerID='9999',
			InvestorID='008105',
			InstrumentID=f.getInstrumentID(),
			OrderRef= '{0:>12}'.format(self.req),
			UserID= '008105',
			OrderPriceType=OrderPriceTypeType.LimitPrice,
			Direction=DirectionType.Buy,
			CombOffsetFlag= OffsetFlagType.Open.__char__(),
			CombHedgeFlag=HedgeFlagType.Speculation.__char__(),
			LimitPrice=f.getLastPrice() - 50,
			VolumeTotalOriginal=1,
			TimeCondition=TimeConditionType.GFD,
			#GTDDate=''
			VolumeCondition=VolumeConditionType.AV,
			MinVolume=1,
			ContingentCondition=ContingentConditionType.Immediately,
			StopPrice= 0,
			ForceCloseReason=ForceCloseReasonType.NotForceClose,
			IsAutoSuspend=0,
			IsSwapOrder=0,
			UserForceClose=0)

	def OnFrontConnected(self):
		print('connected')
		self.t.ReqUserLogin(BrokerID='9999', UserID='008105', Password='1')

	def OnRspUserLogin(self, rsp, info, req, last):
		i = CThostFtdcRspInfoField()
		i = info
		print(i.getErrorMsg())

		if i.getErrorID() == 0:
			self.Session = rsp.getSessionID()
			self.t.ReqSettlementInfoConfirm(BrokerID='9999', InvestorID='008105')

	def StartQuote(self):
		api = self.q.CreateApi()
		spi = self.q.CreateSpi()
		self.q.RegisterSpi(spi)

		self.q.OnFrontConnected = self.q_OnFrontConnected
		self.q.OnRspUserLogin = self.q_OnRspUserLogin
		self.q.OnRtnDepthMarketData = self.q_OnTick

		self.q.RegCB()

		self.q.RegisterFront('tcp://180.168.146.187:10010')
		self.q.Init()
		self.q.Join()

	def OnRspOrderInsert(self, pInputOrder = CThostFtdcInputOrderField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
		f = CThostFtdcRspInfoField()
		f = pRspInfo
		print(pRspInfo)
		print(pInputOrder)
		print(f.getErrorMsg())

	def OnRtnOrder(self, pOrder = CThostFtdcOrderField):
		print(pOrder)
		if pOrder.getSessionID() == self.Session and pOrder.getOrderStatus() == OrderStatusType.NoTradeQueueing:
			self.t.ReqOrderAction(
				'9999', '008105',
				InstrumentID=pOrder.getInstrumentID(),
				OrderRef=pOrder.getOrderRef(),
				FrontID=pOrder.getFrontID(),
				SessionID=pOrder.getSessionID(),
				ActionFlag=ActionFlagType.Delete)

	def OnRspSettlementInfoConfirm(self, pSettlementInfoConfirm = CThostFtdcSettlementInfoConfirmField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
		#print(pSettlementInfoConfirm)
		_thread.start_new_thread(self.StartQuote, ())

	def Qry(self):
		sleep(1.1)
		self.t.ReqQryInstrument()
		while True:
			sleep(1.1)
			self.t.ReqQryTradingAccount('9999', '008105')
			sleep(1.1)
			self.t.ReqQryInvestorPosition('9999', '008105')
			return

	def OnRtnInstrumentStatus(self, pInstrumentStatus = CThostFtdcInstrumentStatusField):
		pass

	def Run(self):
		#CreateApi时会用到log目录,需要在程序目录下创建**而非dll下**
		api = self.t.CreateApi()
		spi = self.t.CreateSpi()
		self.t.RegisterSpi(spi)

		self.t.OnFrontConnected = self.OnFrontConnected
		self.t.OnRspUserLogin = self.OnRspUserLogin
		self.t.OnRspSettlementInfoConfirm = self.OnRspSettlementInfoConfirm
		self.t.OnRtnInstrumentStatus = self.OnRtnInstrumentStatus
		self.t.OnRspOrderInsert = self.OnRspOrderInsert
		self.t.OnRtnOrder = self.OnRtnOrder
		#_thread.start_new_thread(self.Qry, ())

		self.t.RegCB()

		self.t.RegisterFront('tcp://180.168.146.187:10000')
		self.t.Init()
		self.t.Join()


if __name__ == '__main__':
	t = Test()
	t.Run()
	input()
