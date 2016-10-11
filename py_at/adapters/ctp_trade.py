#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/9/22'
"""

import _thread
import sys

sys.path.append('..')
import time
from time import sleep
import itertools
from py_at.switch import *

from py_at.adapters.TradeAdapter import *
from py_ctp.trade import *
from py_ctp.ctp_enum import *


class CtpTrade(TradeAdapter):
	""""""
	def __init__(self):
		super().__init__()
		self._req = 0
		self.__dic_orderid_sysid = {}
		self.__posi = []
		self.t = Trade()

# ------------------
	def __qry(self):
		"""查询帐号相关信息"""
		self.t.ReqQryInstrument()
		sleep(1.1)
		while not self.Account or self.IsLogin:
			"""查询持仓与权益"""
			sleep(1.1)
			self.t.ReqQryInvestorPosition(self.BrokerID, self.Investor)
			sleep(1.1)
			self.t.ReqQryTradingAccount(self.BrokerID, self.Investor)

	def __OnFrontConnected(self):
		self.OnFrontConnected()

	def __OnFrontDisconnected(self, nReason):
		self.OnFrontDisConnected(nReason)

	def __OnRspUserLogin(self, pRspUserLogin = CThostFtdcRspUserLoginField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
		""""""
		self.Investor = pRspUserLogin.getUserID()
		self.BrokerID = pRspUserLogin.getBrokerID()

		self.SessionID = pRspUserLogin.getSessionID()
		self.TradingDay = pRspUserLogin.getTradingDay()

		if pRspInfo.getErrorID() != 0:
			info = InfoField()
			info.ErrorID = pRspInfo.getErrorID()
			info.ErrorMsg = pRspInfo.getErrorMsg()
			self.OnRspUserLogin(info)
		else:
			self.t.ReqSettlementInfoConfirm(self.BrokerID, self.Investor)
			time.sleep(0.5)
			"""查询持仓与权益"""
			_thread.start_new_thread(self.__qry, ())  # 开启查询

	def __OnRspQryInstrument(self, pInstrument = CThostFtdcInstrumentField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
		""""""
		inst = InstrumentField()
		inst.InstrumentID = pInstrument.getInstrumentID()
		inst.ProductID = pInstrument.getProductID()
		inst.ExchangeID = pInstrument.getExchangeID()
		inst.VolumeMultiple = pInstrument.getVolumeMultiple()
		inst.PriceTick = pInstrument.getPriceTick()
		inst.MaxOrderVolume = pInstrument.getMaxLimitOrderVolume()
		self.DicInstrument[inst.InstrumentID] = inst

	def __OnRspQryAccount(self, pTradingAccount = CThostFtdcTradingAccountField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
		""""""
		if not self.Account:
			self.Account = TradingAccount()
		self.Account.Available = pTradingAccount.getAvailable()
		self.Account.CloseProfit = pTradingAccount.getCloseProfit()
		self.Account.Commission = pTradingAccount.getCommission()
		self.Account.CurrMargin = pTradingAccount.getCurrMargin()
		self.Account.FrozenCash = pTradingAccount.getFrozenCash()
		self.Account.PositionProfit = pTradingAccount.getPositionProfit()
		self.Account.PreBalance = pTradingAccount.getPreBalance() + pTradingAccount.getDeposit() + pTradingAccount.getWithdraw()
		self.Account.Fund = self.Account.PreBalance + pTradingAccount.getCloseProfit() + pTradingAccount.getPositionProfit() - pTradingAccount.getCommission()
		self.Account.Risk = self.Account.CurrMargin / self.Account.Fund
		if not self.IsLogin:
			self.IsLogin = True
			info = InfoField()
			info.ErrorID = 0
			info.ErrorMsg = '正确'
			self.OnRspUserLogin(info)

	def __OnRspQryPosition(self, pInvestorPosition = CThostFtdcInvestorPositionField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
		""""""
		if not self.__posi:
			self.__posi = []
		if pInvestorPosition.getInstrumentID() != '':  # 偶尔出现NULL的数据导致数据转换错误
			self.__posi.append(pInvestorPosition)

		if bIsLast:
			# direction需从posidiction转换为dictiontype
			for key, group in itertools.groupby(self.__posi, lambda c: '{0}_{1}'.format(pInvestorPosition.getInstrumentID(), int(DirectionType.Buy if pInvestorPosition.getPosiDirection() == PosiDirectionType.Long else DirectionType.Sell))):
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
						pf.InstrumentID = g.getInstrumentID()
						pf.Direction = g.getPosiDirection() == DirectionType.Buy if PosiDirectionType.Long else DirectionType.Sell
					pf.Position += g.getPosition()
					pf.TdPosition += g.getTodayPosition()
					pf.YdPosition = pf.Position - pf.TdPosition
					pf.CloseProfit += g.getCloseProfit()
					pf.PositionProfit += g.getPositionProfit()
					pf.Commission += g.getCommission()
					pf.Margin += g.getUseMargin()
					cost += g.getOpenCost()
				# pf.Position <= 0 ? 0 : (g.Sum(n => n.PositionCost) / DicInstrumentField[pf.InstrumentID].VolumeMultiple / pf.Position);
				vm = self.DicInstrument[pf.InstrumentID].VolumeMultiple
				pf.Price = 0 if pf.Position <= 0 else cost / vm / pf.Position

			self.__posi.clear()

	def __OnRtnOrder(self, pOrder = CThostFtdcOrderField):
		""""""
		id = '{0}|{1}|{2}'.format(pOrder.getSessionID(), pOrder.getFrontID(), pOrder.getOrderRef())
		# of = OrderField()
		of = self.DicOrderField.get(id)
		if not of:
			of = OrderField()
			l = int(pOrder.getOrderRef())
			of.Custom = l % 1000000
			of.InstrumentID = pOrder.getInstrumentID()
			of.InsertTime = pOrder.getInsertTime()
			of.Direction = pOrder.getDirection()
			of.Offset = pOrder.getCombOffsetFlag()[0]
			of.Status = OrderStatus.Normal
			of.StatusMsg = pOrder.getStatusMsg()
			of.IsLocal = pOrder.getSessionID() == self.SessionID
			of.LimitPrice = pOrder.getLimitPrice()
			of.OrderID = id
			of.Volume = pOrder.getVolumeTotalOriginal()
			of.VolumeLeft = of.Volume
			self.DicOrderField[id] = of
			_thread.start_new_thread(self.OnRtnOrder, (of,))  # call client OnRtnOrder event
		elif pOrder.getOrderStatus() == OrderStatusType.Canceled:
			of.Status = OrderStatus.Canceled
			of.StatusMsg = pOrder.getStatusMsg()

			if of.StatusMsg.find('被拒绝') >= 0:
				info = InfoField()
				info.ErrorID = -1
				info.ErrorMsg = of.StatusMsg
				self.OnRtnErrOrder(of, info)
			else:
				self.OnRtnCancel(of)
		elif pOrder.getOrderSysID():
			self.__dic_orderid_sysid[pOrder.getOrderSysID()] = id  # 记录sysid与orderid关联,方便Trade时查找处理

	def __OnRtnTrade(self, f):
		""""""
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
		of = self.DicOrderField[id]
		tf.OrderID = id  # tradeid 与 orderid 关联
		of.TradeTime = tf.TradeTime
		# of.AvgPrice = (of.AvgPrice * (of.Volume - of.VolumeLeft) + pTrade.Price * pTrade.Volume) / (of.Volume - of.VolumeLeft + pTrade.Volume);
		of.AvgPrice = (of.AvgPrice * (of.Volume - of.VolumeLeft) + tf.Price * tf.Volume) / (of.Volume - of.VolumeLeft + tf.Volume)
		of.TradeVolume = tf.Volume
		of.VolumeLeft -= tf.Volume
		if of.VolumeLeft == 0:
			of.Status = OrderStatus.Filled
			of.StatusMsg = '全部成交'
		else:
			of.Status = OrderStatus.Partial
			of.StatusMsg = '部分成交'
		# 更新持仓 *****
		if tf.Offset == OffsetType.Open:
			key = '{0}_{1}'.format(tf.InstrumentID, int(tf.Direction))
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
			if pf:  # 有可能出现无持仓的情况
				if tf.Offset == OffsetType.CloseToday:
					pf.TdPosition -= tf.Volume
				else:
					tdclose = min(pf.TdPosition, tf.Volume)
					if pf.TdPosition > 0:
						pf.TdPosition -= tdclose
					pf.YdPosition -= max(0, tf.Volume - tdclose)
				pf.Position -= tf.Volume

		_thread.start_new_thread(self.OnRtnOrder, (of,))
		_thread.start_new_thread(self.OnRtnTrade, (tf,))

	def __OnRspOrder(self, pInputOrder = CThostFtdcInputOrderField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
		""""""
		info = InfoField()
		info.ErrorID = pRspInfo.getErrorID()
		info.ErrorMsg = pRspInfo.getErrorMsg()

		id = '{0}|{1}|{2}'.format(self.SessionID, '0', pInputOrder.getOrderRef())
		of = self.DicOrderField.get(id)
		if not of:
			of = OrderField()
			l = int(pInputOrder.getOrderRef())
			of.Custom = l % 1000000
			of.InstrumentID = pInputOrder.getInstrumentID()
			of.InsertTime = time.strftime('%Y%M%d %H:%M:%S', time.localtime())
			of.Direction = pInputOrder.getDirection()
			of.Offset = pInputOrder.getCombOffsetFlag()[0]
			# of.Status = OrderStatus.Normal
			# of.StatusMsg = f.getStatusMsg()
			of.IsLocal = True
			of.LimitPrice = pInputOrder.getLimitPrice()
			of.OrderID = id
			of.Volume = pInputOrder.getVolumeTotalOriginal()
			of.VolumeLeft = of.Volume
			self.DicOrderField[id] = of

		of.Status = OrderStatus.Error
		of.StatusMsg = '{0}:{1}'.format(info.ErrorID, info.ErrorMsg)
		_thread.start_new_thread(self.OnRtnErrOrder, (of, info))

	def __OnErrOrder(self, pInputOrder = CThostFtdcInputOrderField, pRspInfo = CThostFtdcRspInfoField):
		""""""
		id = '{0}|{1}|{2}'.format(self.SessionID, '0', pInputOrder.getOrderRef())
		of = self.DicOrderField.get(id)

		info = InfoField()
		info.ErrorID = pRspInfo.getErrorID()
		info.ErrorMsg = pRspInfo.getErrorMsg()

		if of and of.IsLocal:
			of.Status = OrderStatus.Error
			of.StatusMsg = '{0}:{1}'.format(pRspInfo.getErrorID(), pRspInfo.getErrorMsg())
			_thread.start_new_thread(self.OnRtnErrOrder, (of, info))


# ------------------


	def ReqConnect(self, pAddress=''):
		self.t.CreateApi()
		spi = self.t.CreateSpi()
		self.t.RegisterSpi(spi)

		self.t.OnFrontConnected = self.__OnFrontConnected
		self.t.OnRspUserLogin = self.__OnRspUserLogin
		self.t.OnFrontDisconnected = self.__OnFrontDisconnected
		self.t.OnRtnOrder = self.__OnRtnOrder
		self.t.OnRtnTrade = self.__OnRtnTrade
		self.t.OnRspOrderInsert = self.__OnRspOrder
		self.t.OnErrRtnOrderInsert = self.__OnErrOrder

		self.t.OnRtnInstrumentStatus = self.__OnRtnInstrumentStatus

		self.t.OnRspQryInstrument = self.__OnRspQryInstrument
		self.t.OnRspQryTradingAccount = self.__OnRspQryAccount
		self.t.OnRspQryInvestorPosition = self.__OnRspQryPosition

		self.t.RegCB()

		self.t.RegisterFront(pAddress)
		self.t.Init()

	def ReqUserLogin(self, user, pwd, broker):
		self.t.ReqUserLogin(
			BrokerID=broker,
			UserID=user,
			Password=pwd
		)

	def __OnRtnInstrumentStatus(self, pInstrumentStatus = CThostFtdcInstrumentStatusField):
		pass

	def ReqOrderInsert(self, pInstrument='', pDirection=DirectionType, pOffset=OffsetType, pPrice=0.0, pVolume=1, pType=OrderType, pCustom=0):
		""""""
		OrderPriceType = OrderPriceTypeType.AnyPrice
		TimeCondition = TimeConditionType.IOC
		LimitPrice = 0
		VolumeCondition = VolumeConditionType.AV

		for case in switch(pType):
			if case(OrderType.Market):  # 市价
				OrderPriceType = OrderPriceTypeType.AnyPrice
				TimeCondition = TimeConditionType.IOC
				LimitPrice = 0
				VolumeCondition = VolumeConditionType.AV
				break
			if case(OrderType.Limit):  # 限价
				OrderPriceType = OrderPriceTypeType.LimitPrice
				TimeCondition = TimeConditionType.GFD
				LimitPrice = pPrice
				VolumeCondition = VolumeConditionType.AV
				break
			if case(OrderType.FAK):  # FAK
				OrderPriceType = OrderPriceTypeType.LimitPrice
				TimeCondition = TimeConditionType.IOC
				LimitPrice = pPrice
				VolumeCondition = VolumeConditionType.AV
				break
			if case(OrderType.FOK):  # FOK
				OrderPriceType = OrderPriceTypeType.LimitPrice
				TimeCondition = TimeConditionType.IOC
				LimitPrice = pPrice
				VolumeCondition = VolumeConditionType.CV  # 全部数量
				break

		self._req += 1
		self.t.ReqOrderInsert(
			self.BrokerID,
			self.Investor,
			pInstrument,
			"%06d%06d" % (self._req, pCustom % 1000000),
			self.Investor,
			#此处ctp_enum与at_struct名称冲突
			Direction = DirectionType.Buy,
			CombOffsetFlag= chr(OffsetFlagType.Open if pOffset==OffsetType.Open else (OffsetFlagType.CloseToday if pOffset == OffsetType.CloseToday else OffsetFlagType.Close)),
			CombHedgeFlag=HedgeFlagType.Speculation.__char__(),
			IsAutoSuspend=0,
			ForceCloseReason= ForceCloseReasonType.NotForceClose,
			IsSwapOrder=0,
			ContingentCondition = ContingentConditionType.Immediately,
			VolumeCondition= VolumeCondition,
			MinVolume= 1,
			VolumeTotalOriginal=pVolume,
			OrderPriceType = OrderPriceType,
			TimeCondition = TimeCondition,
			LimitPrice=LimitPrice,
		)

	def ReqOrderAction(self, OrderID=''):
		""""""
		of = self.DicOrderField[OrderID]

		if not of:
			return -1
		else:
			pOrderId = of.OrderID
			f = CThostFtdcInputOrderActionField()
			f.ActionFlag = ActionFlagType.Delete
			f.BrokerID = self.BrokerID
			f.InstrumentID = of.InstrumentID
			f.InvestorID = of.InvestorID
			f.SessionID = int(pOrderId.Split('|')[0])
			f.FrontID = int(pOrderId.Split('|')[1])
			f.OrderRef = pOrderId.Split('|')[2]
			return self.t.ReqOrderAction(
				self.BrokerID,
				self.Investor,
				OrderRef=pOrderId.Split('|')[2],
				FrontID=int(pOrderId.Split('|')[1]),
				SessionID=int(pOrderId.Split('|')[0]),
				InstrumentID=of.InstrumentID,
				ActionFlag=ActionFlagType.Delete
			)

	def Release(self):
		self.t.Release()


#------------------
	def OnFrontConnected(self):
		""""""
		pass


	def OnFrontDisConnected(self, error = 0):
		""""""
		pass


	def OnRspUserLogin(self, info = InfoField):
		""""""
		pass


	def OnRtnOrder(self, f = OrderField):
		""""""
		pass


	def OnRtnTrade(self, f = TradeField):
		""""""
		pass


	def OnRtnCancel(self, f = OrderField):
		""""""
		pass


	def OnRtnErrOrder(self, f = OrderField, info = InfoField):
		""""""
		print(f)
		print(info)