#!/usr/bin/env python
#coding:utf-8
"""
  Author:  HaiFeng --<galaxy>
  Purpose: trade api of ctp
  Created: 2016/7/26
"""


from time import *
import os
from ctypes import *

from ctp_data_type import *
from ctp_struct import *
from ctp_enum import *
from enum_req_trade import *
from enum_dele_trade import *
from common_field import *
from enum import *
from switch import *

import _thread
import itertools
	
	
	
########################################################################
class ctp_trade(object):
	"""交易类"""

	#----------------------------------------------------------------------
	def __init__(self):
		"""initialize"""

		self.__dic_orderid_sysid = {}
		self.DicOrderField = {}
		self.DicTradeField = {}
		self.DicPositionField = {}
		self.DicInstrument = {}
		self.IsLogin = False
		self.Account = None
		self.__posi = []

		self._req = 0		#req add param
		cur_path = os.getcwd()
		#change work directory
		os.chdir(os.path.join(os.getcwd(), "dll"))
		#make log dir for api log
		if not os.path.exists("log"):
			os.mkdir("log")

		self.h = CDLL("ctp_trade.dll")


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

		self.__RegDelegate()	#注册事件

		#restore work directory
		os.chdir(cur_path)

		#front = 'tcp://192.168.105.72:53213'
		#front = 'tcp://180.168.146.187:10010'
		#self.ReqConnect(front)
		#os.system("pause")	#必须的,否则会报异常.可能是由此导致某些变量被回收 ##改用Self...注册即可 ^_^
	


	#----------------------------------------------------------------------
	def __ReqCmd(self, cmd_type, cmd_params):
		if type(cmd_params) == str:
			self.h.ReqCommand(self.api, cmd_type, cmd_params.encode("ascii"))   #导致invalidport的原因:cast(cmd_params.encode("ascii"), c_void_p))
			return

		return self.h.ReqCommand(self.api, int(cmd_type), cmd_params)


	#----------------------------------------------------------------------
	def __RegDele(self, dele_type, dele_ptr):
		self.h.RegDelegate(self.spi, dele_type, dele_ptr)	


	#----------------------------------------------------------------------
	def ReqConnect(self, front_addr):
		"""connect to server """
		self.__ReqCmd(EnumReq.RegisterFront, front_addr)
		return self.__ReqCmd(EnumReq.Init, None)


	#----------------------------------------------------------------------
	def ReqRelease(self):
		""""""
		self.__ReqCmd(EnumReq.Release, None)

	#----------------------------------------------------------------------
	def ReqUserLogin(self, user, pwd, broker):
		"""login"""
		f = CThostFtdcReqUserLoginField()

		f.UserID = bytes(user, 'ascii')
		f.Password = bytes(pwd, 'ascii')
		f.BrokerID = bytes(broker, 'ascii')
		return self.__ReqCmd(EnumReq.ReqUserLogin, byref(f))
	

	#----------------------------------------------------------------------
	def ReqOrderInsert(self, pInstrument, pDirection, pOffset, pPrice, pVolume, pType, pCustom = 0):
		""""""
		f = CThostFtdcInputOrderField()
		f.InstrumentID = bytes(pInstrument, 'ascii')
		f.Direction = pDirection.__char__()
		f.CombOffsetFlag = bytes(pOffset.__char__())
		f.VolumeTotalOriginal = pVolume
		self._req += 1
		f.OrderRef = bytes("%06d%06d" % (self._req, pCustom % 1000000), 'ascii')
		f.InvestorID = self.Investor
		f.BrokerID = self.BrokerID
		f.IsAutoSuspend = 0
		f.CombHedgeFlag = bytes(HedgeFlagType.Speculation.__char__())
		f.ForceCloseReason = ForceCloseReasonType.NotForceClose.__char__()
		f.ContingentCondition = ContingentConditionType.Immediately.__char__()
		f.VolumeCondition = VolumeConditionType.AV.__char__()
		f.LimitPrice = pPrice
		f.IsSwapOrder = 0
		f.MinVolume = 1
		f.UserForceClose = 0
		for case in switch(pType):
			if case(OrderType.Market): #市价
				f.OrderPriceType = OrderPriceTypeType.AnyPrice.__char__()
				f.TimeCondition = TimeConditionType.IOC.__char__()
				#max = instField.MaxMarketOrderVolume;
				f.LimitPrice = 0;
				break;
			if case(OrderType.Limit): #限价
				f.OrderPriceType = OrderPriceTypeType.LimitPrice.__char__();
				f.TimeCondition = TimeConditionType.GFD.__char__();
				break;
			if case(OrderType.FAK): #FAK
				f.OrderPriceType = OrderPriceTypeType.LimitPrice.__char__();
				f.TimeCondition = TimeConditionType.IOC.__char__();
				break;
			if case(OrderType.FOK): #FOK
				f.OrderPriceType = OrderPriceTypeType.LimitPrice.__char__();
				f.TimeCondition = TimeConditionType.IOC.__char__();
				f.VolumeCondition = VolumeConditionType.CV.__char__(); #全部数量
				break;			
		return self.__ReqCmd(EnumReq.ReqOrderInsert, byref(f))
	

	#----------------------------------------------------------------------
	def ReqOrderAction(self, OrderID):
		""""""
		of = self.DicOrderField[OrderID]
		
		if not of:
			return -1
		else:
			f = CThostFtdcInputOrderActionField()
			f.ActionFlag = TThostFtdcActionFlagType.THOST_FTDC_AF_Delete
			f.BrokerID = self.BrokerID
			f.InstrumentID = of.InstrumentID
			f.InvestorID = of.InvestorID
			f.SessionID = int.Parse(pOrderId.Split('|')[0])
			f.FrontID = int.Parse(pOrderId.Split('|')[1])
			f.OrderRef = pOrderId.Split('|')[2]
			return self.__ReqCmd(EnumReq.ReqOrderAction, byref(f))


	#----------------------------------------------------------------------
	def __qry(self):
		f = CThostFtdcQryInstrumentField()		
		self.__ReqCmd(EnumReq.ReqQryInstrument, byref(f))
		while not self.Account or self.IsLogin:
				
			"""查询持仓与权益"""	
			sleep(1.1)
			q = CThostFtdcQryInvestorPositionField()
			q.BrokerID = bytes(self.BrokerID)
			q.InvestorID = bytes(self.Investor)
			self.__ReqCmd(EnumReq.ReqQryInvestorPosition, byref(q))
			
			sleep(1.1)
			q = CThostFtdcQryTradingAccountField()
			q.BrokerID = self.BrokerID
			q.InvestorID = self.Investor
			self.__ReqCmd(EnumReq.ReqQryTradingAccount, byref(q))


	#----------------------------------------------------------------------
	def OnFrontConnected(self):
		""""""
		pass


	#----------------------------------------------------------------------
	def OnFrontDisConnected(self, error):
		""""""
		pass

	#----------------------------------------------------------------------
	def OnUserLogin(self, info):
		""""""
		pass


	#----------------------------------------------------------------------
	def OnRtnOrder(self, f):
		""""""
		pass
	

	#----------------------------------------------------------------------
	def OnRtnTrade(self, f):
		""""""
		pass
		

	#----------------------------------------------------------------------
	def OnRtnCancel(self, f):
		""""""
		pass
	

	#----------------------------------------------------------------------
	def OnRtnErrOrder(self, f, info):
		""""""
		pass
		

	#----------------------------------------------------------------------
	def __OnFrontConnected(self):
		""""""
		self.OnFrontConnected()

	#----------------------------------------------------------------------
	def __OnFrontDisConnected(self, error):
		""""""
		self.IsLogin = False
		print('disconnected')
		self.OnFrontDisConnected(error)
		

	#----------------------------------------------------------------------
	def __OnRspUserLogin(self, rsp, info, req, last):
		r = CThostFtdcRspUserLoginField()
		r = POINTER(CThostFtdcRspUserLoginField).from_param(rsp).contents
		c = CThostFtdcRspInfoField()
		c = POINTER(CThostFtdcRspInfoField).from_param(info).contents
		self.Investor = r.UserID
		self.BrokerID = r.BrokerID
		
		self.SessionID = r.getSessionID()
		self.TradingDay = r.getTradingDay()

		if c.getErrorID() != 0:
			self.OnUserLogin(r, c);
		else:
			f = CThostFtdcSettlementInfoConfirmField()
			f.BrokerID = self.BrokerID
			f.InvestorID = self.Investor
			self.__ReqCmd(EnumReq.ReqSettlementInfoConfirm, byref(f))
			sleep(0.5)
			"""查询持仓与权益"""	
			_thread.start_new_thread(self.__qry, ())	#开启查询
			#未确认结算,会导致没有查询响应.....
	

	#----------------------------------------------------------------------
	def __OnRtnOrder(self, field:CThostFtdcOrderField):
		""""""
		f = CThostFtdcOrderField()
		f = POINTER(CThostFtdcOrderField).from_param(field).contents
		
		id = '{0}|{1}|{2}'.format(f.getSessionID(), f.getFrontID(), f.getOrderRef())
		
		#of = OrderField()
		of = self.DicOrderField.get(id)
		if not of:
			#if type(f.getOrderRef()) is types.
			of = OrderField()
			l = int(f.getOrderRef())
			of.Custom = l % 1000000
			of.InstrumentID = f.getInstrumentID()
			of.InsertTime = f.getInsertTime()
			of.Direction = f.getDirection()
			of.Offset = f.getCombOffsetFlag()[0]
			of.Status = OrderStatus.Normal
			of.StatusMsg = f.getStatusMsg()
			of.IsLocal = f.getSessionID() == self.SessionID
			of.LimitPrice = f.getLimitPrice()
			of.OrderID = id
			of.Volume = f.getVolumeTotalOriginal()
			of.VolumeLeft = of.Volume
			self.DicOrderField[id] = of
			self.OnRtnOrder(of);	#call client OnRtnOrder event
		elif f.getOrderStatus() == OrderStatusType.Canceled:
			of.Status = OrderStatus.Canceled
			of.StatusMsg = f.getStatusMsg()
		
			if of.StatusMsg.find('被拒绝') >= 0:
				info = InfoField()
				info.ErrorID = -1
				info.ErrorMsg = of.StatusMsg
				self.OnRtnErrOrder(of, info)
			else:
				self.OnRtnCancel(of)
		elif f.getOrderSysID():
			self.__dic_orderid_sysid[f.getOrderSysID()] = id #记录sysid与orderid关联,方便Trade时查找处理
			


	#----------------------------------------------------------------------
	def __OnRtnTrade(self, field):
		""""""
		f = CThostFtdcTradeField()
		f = POINTER(CThostFtdcTradeField).from_param(field).contents
		tf = TradeField()
		tf.Direction = f.getDirection()
		tf.ExchangeID = f.getExchangeID()
		tf.InstrumentID = f.getInstrumentID()
		tf.Offset = OffsetType.Open if f.getOffsetFlag() == OffsetFlagType.Open else OffsetType.Close if f.getOffsetFlag() == OffsetFlagType.Close else OffsetType.CloseToday
		tf.Price = f.getPrice()
		tf.SysID = f.getOrderSysID()
		tf.TradeID = f.getTradeID()
		tf.TradeTime = f.getTradeTime()
		tf.TradingDay = f.getTradingDay()
		tf.Volume = f.getVolume()
		
		self.DicTradeField[tf.TradeID] = tf

		id = self.__dic_orderid_sysid[tf.SysID]
		of = OrderField()
		of = self.DicOrderField[id]
		tf.OrderID = id		#tradeid 与 orderid 关联
		of.TradeTime = tf.TradeTime
		#of.AvgPrice = (of.AvgPrice * (of.Volume - of.VolumeLeft) + pTrade.Price * pTrade.Volume) / (of.Volume - of.VolumeLeft + pTrade.Volume);
		of.AvgPrice = (of.AvgPrice * (of.Volume - of.VolumeLeft) + tf.Price * tf.Volume) / (of.Volume - of.VolumeLeft + tf.Volume)
		of.TradeVolume = tf.Volume
		of.VolumeLeft -= tf.Volume
		if of.VolumeLeft == 0:
			of.Status = OrderStatus.Filled
			of.StatusMsg = '全部成交'
		else:
			of.Status = OrderStatus.Partial
			of.StatusMsg = '部分成交'
		#更新持仓 *****
		pf = PositionField()
		if tf.Offset == OffsetType.Open:
			key = '{0}_{1}'.format(tf.InstrumentID, int( tf.Direction))
			pf = self.DicPositionField.get(key)
			if not pf:
				pf = PositionField()
				self.DicPositionField[key] = pf
			pf.InstrumentID = tf.InstrumentID
			pf.Direction = tf.Direction
			pf.Price = (pf.Price * pf.Position + tf.Price * tf.Volume) / (pf.Position + tf.Volume)
			pf.TdPosition += tf.Volume
			pf.Position += tf.Volume
		else:
			key = '{0}_{1}'.format(tf.InstrumentID, int(DirectionType.Sell if tf.Direction == DirectionType.Buy else DirectionType.Buy))
			pf = self.DicPositionField.get(key)
			if pf: #有可能出现无持仓的情况
				if tf.Offset == OffsetType.CloseToday:
					pf.TdPosition -= tf.Volume
				else:
					tdclose = min(pf.TdPosition, tf.Volume)
					if pf.TdPosition > 0:
						pf.TdPosition -= tdclose
					pf.YdPosition -= max(0, tf.Volume - tdclose)
				pf.Position -= tf.Volume
		
		self.OnRtnOrder(of)		
		self.OnRtnTrade(tf)
	

	#----------------------------------------------------------------------
	def __OnRspOrder(self, rsp, info, req, last):
		""""""
		f = CThostFtdcInputOrderField()
		f = POINTER(CThostFtdcInputOrderField).from_param(rsp).contents
		c = CThostFtdcRspInfoField()
		c = POINTER(CThostFtdcRspInfoField).from_param(info).contents
		
		info = InfoField()
		info.ErrorID = c.getErrorID()
		info.ErrorMsg = c.getErrorMsg()
		
		id = '{0}|{1}|{2}'.format(self.SessionID, '0', f.getOrderRef())
		of = OrderField()
		of = self.DicOrderField.get(id)
		if not of:
			of = OrderField()
			l = int(f.getOrderRef())
			of.Custom = l % 1000000
			of.InstrumentID = f.getInstrumentID()
			of.InsertTime = time()
			of.Direction = f.getDirection()
			of.Offset = f.getCombOffsetFlag()[0]
			#of.Status = OrderStatus.Normal
			#of.StatusMsg = f.getStatusMsg()
			of.IsLocal = True
			of.LimitPrice = f.getLimitPrice()
			of.OrderID = id
			of.Volume = f.getVolumeTotalOriginal()
			of.VolumeLeft = of.Volume
			self.DicOrderField[id] = of
			
		of.Status = OrderStatus.Error
		of.StatusMsg = '{0}:{1}'.format(info.ErrorID, info.ErrorMsg)
		self.OnRtnErrOrder(of, info)


	#----------------------------------------------------------------------
	def __OnErrRtnOrderInsert(self, rsp, info):
		""""""
		r = CThostFtdcInputOrderField()
		r = POINTER(CThostFtdcInputOrderField).from_param(rsp).contents
		c = CThostFtdcRspInfoField()
		c = POINTER(CThostFtdcRspInfoField).from_param(info).contents
		
		id = '{0}|{1}|{2}'.format(self.SessionID, '0', r.getOrderRef())
		of = OrderField()
		of = self.DicOrderField.get(id)
		
		info = InfoField()
		info.ErrorID = c.getErrorID()
		info.ErrorMsg = c.getErrorMsg()
		
		if of and of.IsLocal:
			of.Status = OrderStatus.Error
			of.StatusMsg = c.getErrorID() + ':' + c.getErrorMsg()
			self.OnRtnErrOrder(of, info)	


	#----------------------------------------------------------------------
	def __onRspInst(self, rsp, info, req, last):
		"""查合约响应"""
		f = CThostFtdcInstrumentField()
		f = POINTER(CThostFtdcInstrumentField).from_param(rsp).contents
		c = CThostFtdcRspInfoField()
		c = POINTER(CThostFtdcRspInfoField).from_param(info).contents
		inst = InstrumentField()
		inst.InstrumentID = f.getInstrumentID()
		inst.ProductID = f.getProductID()
		inst.ExchangeID = f.getExchangeID()
		inst.VolumeMultiple = f.getVolumeMultiple()
		inst.PriceTick = f.getPriceTick()
		inst.MaxOrderVolume = f.getMaxLimitOrderVolume()
		self.DicInstrument[inst.InstrumentID] = inst	

	def __onQryAccount(self, rsp, info, req, last):
		""""""
		f = CThostFtdcTradingAccountField()
		f = POINTER(CThostFtdcTradingAccountField).from_param(rsp).contents
		c = CThostFtdcRspInfoField()
		c = POINTER(CThostFtdcRspInfoField).from_param(info).contents
		
		if not self.Account:
			self.Account = TradingAccount()
		self.Account.Available = f.getAvailable()
		self.Account.CloseProfit = f.getCloseProfit()
		self.Account.Commission = f.getCommission()
		self.Account.CurrMargin = f.getCurrMargin()
		self.Account.FrozenCash = f.getFrozenCash()
		self.Account.PositionProfit = f.getPositionProfit()
		self.Account.PreBalance = f.getPreBalance() + f.getDeposit() + f.getWithdraw()
		self.Account.Fund = self.Account.PreBalance  + f.getCloseProfit() + f.getPositionProfit() - f.getCommission()
		self.Account.Risk = self.Account.CurrMargin / self.Account.Fund
		if not self.IsLogin:
			self.IsLogin = True
			info = InfoField()
			info.ErrorID = 0
			info.ErrorMsg = '正确'
			self.OnUserLogin(info)
	

	#----------------------------------------------------------------------
	def __onQryPosition(self, rsp, info, req, last):
		"""持仓查询响应"""
		r = CThostFtdcInvestorPositionField()
		r = POINTER(CThostFtdcInvestorPositionField).from_param(rsp).contents

		if not self.__posi:
			self.__posi = []
		if r.getInstrumentID() != '':  # 偶尔出现NULL的数据导致数据转换错误
			self.__posi.append(r)
		
		if last:
			#direction需从posidiction转换为dictiontype
			for key, group in itertools.groupby(self.__posi, lambda c: '{0}_{1}'.format(c.getInstrumentID(), int(DirectionType.Buy if c.getPosiDirection() == PosiDirectionType.Long else DirectionType.Sell))):
				pf = self.DicPositionField.get(key)
				if not pf:
					pf = PositionField()
					self.DicPositionField[key] = pf
				pf.Position = 0
				pf.TdPosition = 0
				pf.YdPosition = 0
				pf.CloseProfit = 0
				pf.PositionProfit = 0
				pf.Commission = 0
				pf.Margin = 0
				pf.Price = 0
				cost = 0.0
				for g in group:
					if not pf.InstrumentID:
						pf.InstrumentID = g.InstrumentID
						pf.Direction = g.getPosiDirection() == DirectionType.Buy if PosiDirectionType.Long else DirectionType.Sell
					pf.Position += g.getPosition()
					pf.TdPosition += g.getTodayPosition()					
					pf.YdPosition = pf.Position - pf.TdPosition
					pf.CloseProfit += g.getCloseProfit()
					pf.PositionProfit += g.getPositionProfit()
					pf.Commission += g.getCommission()
					pf.Margin += g.getUseMargin()
					cost += g.getOpenCost()
				#pf.Position <= 0 ? 0 : (g.Sum(n => n.PositionCost) / DicInstrumentField[pf.InstrumentID].VolumeMultiple / pf.Position);
				vm = self.DicInstrument[bytes.decode(pf.InstrumentID, 'ascii')].VolumeMultiple
				pf.Price = 0 if pf.Position <=0 else cost / vm / pf.Position				
				
			self.__posi.clear()


	#----------------------------------------------------------------------
	def __RegDelegate(self):
		"""regist all delegate"""
		
		ev = CFUNCTYPE(c_void_p)
		self.evConn = ev(self.__OnFrontConnected)
		self.__RegDele(EnumDelegate.OnFrontConnected, self.evConn)
		
		evdis = CFUNCTYPE(c_void_p, c_int)
		self.evDis = ev(self.__OnFrontDisConnected)
		self.__RegDele(EnumDelegate.OnFrontDisconnected, self.evDis)

		log = CFUNCTYPE(c_void_p, POINTER(CThostFtdcRspUserLoginField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)
		self.evLog = log(self.__OnRspUserLogin)
		self.__RegDele(EnumDelegate.OnRspUserLogin, self.evLog)

		order = CFUNCTYPE(c_void_p, POINTER(CThostFtdcOrderField))
		self.evOrder = order(self.__OnRtnOrder)
		self.__RegDele(EnumDelegate.OnRtnOrder, self.evOrder)
		
		trade = CFUNCTYPE(c_void_p, POINTER(CThostFtdcTradeField))
		self.evTrade = trade(self.__OnRtnTrade)
		self.__RegDele(EnumDelegate.OnRtnTrade, self.evTrade)
		
		onRspOrder = CFUNCTYPE(c_void_p, POINTER(CThostFtdcInputOrderField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)
		self.evOnRspOrder = onRspOrder(self.__OnRspOrder)
		self.__RegDele(EnumDelegate.OnRspOrderInsert, self.evOnRspOrder)
		
		onErrOrder = CFUNCTYPE(c_void_p, POINTER(CThostFtdcInputOrderField), POINTER(CThostFtdcRspInfoField))
		self.evOnErrOrder = onErrOrder(self.__OnErrRtnOrderInsert)
		self.__RegDele(EnumDelegate.OnErrRtnOrderInsert, self.evOnErrOrder)
		
		onRspInst = CFUNCTYPE(c_void_p, POINTER(CThostFtdcInstrumentField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)
		self.evOnRspInst = onRspInst(self.__onRspInst)
		self.__RegDele(EnumDelegate.OnRspQryInstrument, self.evOnRspInst)		

		onRspAccount = CFUNCTYPE(c_void_p, POINTER(CThostFtdcTradingAccountField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)
		self.evOnRspAccount = onRspAccount(self.__onQryAccount)
		self.__RegDele(EnumDelegate.OnRspQryTradingAccount, self.evOnRspAccount)
		
		OnRspPosition = CFUNCTYPE(c_void_p, POINTER(CThostFtdcInvestorPositionField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)
		self.evOnRspPosition = OnRspPosition(self.__onQryPosition)
		self.__RegDele(EnumDelegate.OnRspQryInvestorPosition, self.evOnRspPosition)
		


	