#!/usr/bin/env python
#coding:utf-8
"""
  Author:  HaiFeng --<>
  Purpose: ctp quote package
  Created: 2016/7/4
"""

import os

from py_ctp.common_field import *
from py_ctp.ctp_struct import *
from py_ctp.enum_dele_quote import EnumDelegate
from py_ctp.enum_req_quote import EnumReq

class ctp_quote:
	#RegDele(IntPtr classPtr, int cbType, IntPtr cbPtr);
	def __RegDele(self, dele_type, dele_ptr):
		self.h.RegDelegate(self.spi, int(dele_type), dele_ptr)
	
	#ReqCmd(IntPtr pApi, int pCmd, IntPtr pPtr)
	def __ReqCmd(self, cmd_type, cmd_params):
		if type(cmd_params) == str:
			self.h.ReqCommand(self.api, int(cmd_type), cmd_params.encode("ascii"))
			return
		
		self.h.ReqCommand(self.api, int(cmd_type), cmd_params)
	
	
	
	#----------------------------------------------------------------------
	def ReqConnect(self, front_addr):
		"""connect to server """
		self.__ReqCmd(EnumReq.RegisterFront, front_addr)
		return self.__ReqCmd(EnumReq.Init, None)

	#----------------------------------------------------------------------
	def ReqSubscribe(self, instrument:str):
		""""""
		self.__ReqCmd(EnumReq.SubscribeMarketData, instrument)
	
	#----------------------------------------------------------------------
	def ReqUserLogin(self, user, pwd, broker):
		"""login"""
		f = CThostFtdcReqUserLoginField()
		
		f.UserID = bytes(user, 'ascii')
		f.Password = bytes(pwd, 'ascii')
		f.BrokerID = bytes(broker, 'ascii')
		return self.__ReqCmd(EnumReq.ReqUserLogin, byref(f))
	
	def OnFrontConnected(self):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def OnUserLogin(self, info):
		""""""
		pass

	#----------------------------------------------------------------------
	def OnRtnTick(self, field):
		""""""
		pass
	
	#----------------------------------------------------------------------
	def __OnFrontConnected(self):
		""""""
		self.OnFrontConnected()
	
	#响应中断点无效
	def __OnRspUserLogin(self, rsp, info, id, last):
		f = CThostFtdcRspInfoField()
		c = POINTER(CThostFtdcRspInfoField).from_param(info).contents
		f = c
		i = InfoField()
		i.ErrorID = f.getErrorID()
		i.ErrorMsg = f.getErrorMsg()
		self.OnUserLogin(i)
			
	
	#----------------------------------------------------------------------
	def __OnTick(self, tick):
		"""response of tick"""
		f = CThostFtdcDepthMarketDataField()
		r = POINTER(CThostFtdcDepthMarketDataField).from_param(tick).contents
		f = r

		tick = MarketData()
		tick.AskPrice = f.getAskPrice1()
		tick.AskVolume = f.getAskVolume1()
		tick.AveragePrice = f.getAveragePrice()
		tick.BidPrice = f.getBidPrice1()
		tick.BidVolume = f.getBidVolume1()
		tick.InstrumentID = f.getInstrumentID()
		tick.LastPrice = f.getLastPrice()
		tick.LowerLimitPrice = f.getLowerLimitPrice()
		tick.OpenInterest = f.getOpenInterest()
		tick.UpdateMillisec = f.getUpdateMillisec()
		tick.UpdateTime = f.getUpdateTime()
		tick.UpperLimitPrice = f.getUpperLimitPrice()
		tick.Volume = f.getVolume()
		
		self.DicTick[f.getInstrumentID()] = tick
		self.OnRtnTick(tick)
		
	#----------------------------------------------------------------------
	def __RegDelegate(self):
		"""regist all delegate"""
		ev = CFUNCTYPE(c_voidp)
		self.evh = ev(self.__OnFrontConnected)
		self.__RegDele(EnumDelegate.OnFrontConnected, self.evh)
	
		#DefOnRspUserLogin(ref CThostFtdcRspUserLoginField pRspUserLogin, ref CThostFtdcRspInfoField pRspInfo, int nRequestID, bool bIsLast);
		log = CFUNCTYPE(c_void_p, POINTER(CThostFtdcRspUserLoginField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)
		self.evLog = log(self.__OnRspUserLogin)
		self.__RegDele(EnumDelegate.OnRspUserLogin, self.evLog)
	
		tick = CFUNCTYPE(c_void_p, POINTER(CThostFtdcDepthMarketDataField))
		self.evTick = tick(self.__OnTick)
		self.__RegDele(EnumDelegate.OnRtnDepthMarketData, self.evTick)			
		
	
	#----------------------------------------------------------------------
	def __init__(self):
		"""main function"""
		self.DicTick = {}
	
		cur_path = os.getcwd()
		#change work directory
		os.chdir(os.path.join(os.getcwd(), "dll"))
		#make log dir for api log
		if not os.path.exists("log"):
			os.mkdir("log")
		
		self.h = CDLL("ctp_quote.dll")
		
		
		#define command types
		self.h.ReqCommand.argtypes = [c_void_p, c_int, c_void_p]
		self.h.ReqCommand.restype = c_void_p
		
		self.h.RegDelegate.argtypes = [c_void_p, c_int, c_void_p]
		self.h.RegDelegate.restype = c_void_p
		
		self.h.CreateApi.argtypes = []
		self.h.CreateApi.restype = c_void_p
		
		self.h.CreateSpi.argtypes = [c_void_p]
		self.h.CreateSpi.restype = c_void_p
		
		self.api = self.h.CreateApi()
		self.spi = self.h.CreateSpi(self.api)
		
		#self.Reg()	#注册事件
		self.__RegDelegate()
		
		#restore work directory
		os.chdir(cur_path)
		
		#os.system("pause")	#必须的,否则会报异常.可能是由此导致某些变量被回收 ##改用Self...注册即可 ^_^

	