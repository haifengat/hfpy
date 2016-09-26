#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/9/23'
"""
import _thread
import sys
import time

sys.path.append('..')

from py_at.adapters.QuoteAdapter import *
from py_ctp.quote import *
from py_at.at_struct import *

class CtpQuote(QuoteAdapter):
	""""""
	def __init__(self):
		super().__init__()
		self.q = Quote()

	def ReqConnect(self, pAddress=''):
		self.q.CreateApi()
		spi = self.q.CreateSpi()
		self.q.RegisterSpi(spi)

		self.q.OnFrontConnected = self.__OnFrontConnected
		self.q.OnRspUserLogin = self.__OnRspUserLogin
		self.q.OnRtnDepthMarketData = self.__OnRtnDepthMarketData

		self.q.RegCB()

		self.q.RegisterFront(pAddress)
		self.q.Init()

	def ReqUserLogin(self, user='', pwd='', broker=''):
		self.q.ReqUserLogin(
			BrokerID=broker,
			UserID=user,
			Password=pwd
		)

	def ReqSubscribeMarketData(self, pInstrument=''):
		self.q.SubscribeMarketData(pInstrument)

	def __OnFrontConnected(self):
		""""""
		_thread.start_new_thread(self.OnFrontConnected, ())

	def __OnRspUserLogin(self, pRspUserLogin = CThostFtdcRspUserLoginField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
		""""""
		info = InfoField()
		info.ErrorID = pRspInfo.getErrorID()
		info.ErrorMsg = pRspInfo.getErrorMsg()
		_thread.start_new_thread(self.OnRspUserLogin, (info,))

	def __OnRtnDepthMarketData(self, pDepthMarketData = CThostFtdcDepthMarketDataField):
		""""""
		tick = Tick()
		tick.AskPrice = pDepthMarketData.getAskPrice1()
		tick.AskVolume = pDepthMarketData.getAskVolume1()
		tick.AveragePrice = pDepthMarketData.getAveragePrice()
		tick.BidPrice = pDepthMarketData.getBidPrice1()
		tick.BidVolume = pDepthMarketData.getBidVolume1()
		tick.Instrument = pDepthMarketData.getInstrumentID()
		tick.LastPrice = pDepthMarketData.getLastPrice()
		tick.OpenInterest = pDepthMarketData.getOpenInterest()
		tick.Volume = pDepthMarketData.getVolume()

		day = pDepthMarketData.getTradingDay()
		str = day + ' ' + pDepthMarketData.getUpdateTime()
		if day == None or day == ' ':
			str = time.strftime('%Y%m%d %H:%M:%S', time.localtime())
		tick.UpdateTime = time.strptime(str, '%Y%m%d %H:%M:%S')
		self.DicTick[tick.Instrument] = tick
		_thread.start_new_thread(self.OnRtnTick, (tick,))


	def OnFrontDisConnected(self, error = 0):
		""""""
		pass


	def OnRspUserLogin(self, info = InfoField):
		""""""
		pass


	# ----------------------------------------------------------------------
	def OnRtnTick(self, field = Tick):
		""""""
		pass
