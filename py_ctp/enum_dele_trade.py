#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  Author:  HaiFeng --<galaxy>
  Purpose: 
  Created: 2016/7/26
"""


from enum import Enum

class EnumDelegate(Enum):
	
	OnFrontConnected = 0
	OnFrontDisconnected = 1
	OnHeartBeatWarning = 2
	OnRspAuthenticate = 3
	OnRspUserLogin = 4
	OnRspUserLogout = 5
	OnRspUserPasswordUpdate = 6
	OnRspTradingAccountPasswordUpdate = 7
	OnRspOrderInsert = 8
	OnRspParkedOrderInsert = 9
	OnRspParkedOrderAction = 10
	OnRspOrderAction = 11
	OnRspQueryMaxOrderVolume = 12
	OnRspSettlementInfoConfirm = 13
	OnRspRemoveParkedOrder = 14
	OnRspRemoveParkedOrderAction = 15
	OnRspExecOrderInsert = 16
	OnRspExecOrderAction = 17
	OnRspQryOrder = 18
	OnRspQryTrade = 19
	OnRspQryInvestorPosition = 20
	OnRspQryTradingAccount = 21
	OnRspQryInvestor = 22
	OnRspQryTradingCode = 23
	OnRspQryInstrumentMarginRate = 24
	OnRspQryInstrumentCommissionRate = 25
	OnRspQryExchange = 26
	OnRspQryInstrument = 27
	OnRspQryDepthMarketData = 28
	OnRspQrySettlementInfo = 29
	OnRspQryTransferBank = 30
	OnRspQryInvestorPositionDetail = 31
	OnRspQryNotice = 32
	OnRspQrySettlementInfoConfirm = 33
	OnRspQryInvestorPositionCombineDetail = 34
	OnRspQryCFMMCTradingAccountKey = 35
	OnRspQryEWarrantOffset = 36
	OnRspQryOptionInstrTradeCost = 37
	OnRspQryOptionInstrCommRate = 38
	OnRspQryExecOrder = 39
	OnRspQryTransferSerial = 40
	OnRspQryAccountregister = 41
	OnRspError = 42
	OnRtnOrder = 43
	OnRtnTrade = 44
	OnErrRtnOrderInsert = 45
	OnErrRtnOrderAction = 46
	OnRtnInstrumentStatus = 47
	OnRtnTradingNotice = 48
	OnRtnErrorConditionalOrder = 49
	OnRtnExecOrder = 50
	OnErrRtnExecOrderInsert = 51
	OnErrRtnExecOrderAction = 52
	OnRspQryContractBank = 53
	OnRspQryParkedOrder = 54
	OnRspQryParkedOrderAction = 55
	OnRspQryTradingNotice = 56
	OnRspQryBrokerTradingParams = 57
	OnRspQryBrokerTradingAlgos = 58
	OnRtnFromBankToFutureByBank = 59
	OnRtnFromFutureToBankByBank = 60
	OnRtnRepealFromBankToFutureByBank = 61
	OnRtnRepealFromFutureToBankByBank = 62
	OnRtnFromBankToFutureByFuture = 63
	OnRtnFromFutureToBankByFuture = 64
	OnRtnRepealFromBankToFutureByFutureManual = 65
	OnRtnRepealFromFutureToBankByFutureManual = 66
	OnRtnQueryBankBalanceByFuture = 67
	OnErrRtnBankToFutureByFuture = 68
	OnErrRtnFutureToBankByFuture = 69
	OnErrRtnRepealBankToFutureByFutureManual = 70
	OnErrRtnRepealFutureToBankByFutureManual = 71
	OnErrRtnQueryBankBalanceByFuture = 72
	OnRtnRepealFromBankToFutureByFuture = 73
	OnRtnRepealFromFutureToBankByFuture = 74
	OnRspFromBankToFutureByFuture = 75
	OnRspFromFutureToBankByFuture = 76
	OnRspQueryBankAccountMoneyByFuture = 77
	OnRtnOpenAccountByBank = 78
	OnRtnCancelAccountByBank = 79
	OnRtnChangeAccountByBank = 80


	#----------------------------------------------------------------------	
	def __int__(self):
		return self.value
