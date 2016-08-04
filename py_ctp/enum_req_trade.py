#!/usr/bin/env python
#coding:utf-8
"""
  Author:  HaiFeng --<galaxy>
  Purpose: 
  Created: 2016/7/26
"""
from enum import *
########################################################################
class EnumReq(Enum):
	""""""
	Release = 0
	Init = 1
	Join = 2
	GetTradingDay = 3
	RegisterFront = 4
	RegisterNameServer = 5
	RegisterSpi = 6
	SubscribePrivateTopic = 7
	SubscribePublicTopic = 8
	ReqAuthenticate = 9
	ReqUserLogin = 10
	ReqUserLogout = 11
	ReqUserPasswordUpdate = 12
	ReqTradingAccountPasswordUpdate = 13
	ReqOrderInsert = 14
	ReqParkedOrderInsert = 15
	ReqParkedOrderAction = 16
	ReqOrderAction = 17
	ReqQueryMaxOrderVolume = 18
	ReqSettlementInfoConfirm = 19
	ReqRemoveParkedOrder = 20
	ReqRemoveParkedOrderAction = 21
	ReqExecOrderInsert = 22
	ReqExecOrderAction = 23
	ReqQryOrder = 24
	ReqQryTrade = 25
	ReqQryInvestorPosition = 26
	ReqQryTradingAccount = 27
	ReqQryInvestor = 28
	ReqQryTradingCode = 29
	ReqQryInstrumentMarginRate = 30
	ReqQryInstrumentCommissionRate = 31
	ReqQryExchange = 32
	ReqQryInstrument = 33
	ReqQryDepthMarketData = 34
	ReqQrySettlementInfo = 35
	ReqQryTransferBank = 36
	ReqQryInvestorPositionDetail = 37
	ReqQryNotice = 38
	ReqQrySettlementInfoConfirm = 39
	ReqQryInvestorPositionCombineDetail = 40
	ReqQryCFMMCTradingAccountKey = 41
	ReqQryEWarrantOffset = 42
	ReqQryOptionInstrTradeCost = 43
	ReqQryOptionInstrCommRate = 44
	ReqQryExecOrder = 45
	ReqQryTransferSerial = 46
	ReqQryAccountregister = 47
	ReqQryContractBank = 48
	ReqQryParkedOrder = 49
	ReqQryParkedOrderAction = 50
	ReqQryTradingNotice = 51
	ReqQryBrokerTradingParams = 52
	ReqQryBrokerTradingAlgos = 53
	ReqFromBankToFutureByFuture = 54
	ReqFromFutureToBankByFuture = 55
	ReqQueryBankAccountMoneyByFuture = 56


	#----------------------------------------------------------------------	
	def __int__(self):
		return self.value
		