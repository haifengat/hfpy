#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/9/22'
"""

import _thread
import itertools
import time

from py_at.switch import switch
from py_at.enums import OrderType
from py_at.structs import DirectType, InfoField, InstrumentField, OffsetType, OrderField, OrderStatus, PositionField, TradeField, TradingAccount
from py_at.adapters.trade import TradeAdapter
from py_ctp.trade import Trade
from py_ctp.structs import CThostFtdcInputOrderActionField, CThostFtdcInputOrderField, CThostFtdcInstrumentField, CThostFtdcInstrumentStatusField, CThostFtdcInvestorPositionField, CThostFtdcOrderField, CThostFtdcRspInfoField, CThostFtdcRspUserLoginField, CThostFtdcSettlementInfoConfirmField, CThostFtdcTradingAccountField
from py_ctp.enums import ActionFlagType, ContingentConditionType, DirectionType, OffsetFlagType, ForceCloseReasonType, HedgeFlagType, OrderPriceTypeType, PosiDirectionType, TimeConditionType, VolumeConditionType, OrderStatusType


class CtpTrade(TradeAdapter):
    """"""

    def __init__(self):
        super().__init__()
        self._req = 0
        '''防止重连时启用太多查询线程'''
        self.qryStart = False
        self.__dic_orderid_sysid = {}
        self.__posi = []
        self.t = Trade()

    def __qry(self):
        """查询帐号相关信息"""
        self.qryStart = True
        # restart 模式, 待rtnorder 处理完毕后再进行查询,否则会造成position混乱
        ord_cnt = 0
        while True:
            time.sleep(0.5)
            if len(self.DicOrderField) == ord_cnt:
                break
            ord_cnt = len(self.DicOrderField)
        self.t.ReqQryInstrument()
        time.sleep(1.1)
        while not self.Account or self.IsLogin:
            """查询持仓与权益"""
            time.sleep(1.1)
            self.t.ReqQryInvestorPosition(self.BrokerID, self.Investor)
            time.sleep(1.1)
            self.t.ReqQryTradingAccount(self.BrokerID, self.Investor)

    def __OnFrontConnected(self):
        self.OnFrontConnected()

    def __OnFrontDisconnected(self, nReason):
        self.IsLogin = False
        self.OnFrontDisConnected(nReason)

    def __OnRspUserLogin(self,
                         pRspUserLogin=CThostFtdcRspUserLoginField(),
                         pRspInfo=CThostFtdcRspInfoField,
                         nRequestID=int,
                         bIsLast=bool):

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
            if not self.qryStart:
                time.sleep(0.5)
                """查询持仓与权益"""
                _thread.start_new_thread(self.__qry, ())  # 开启查询

    def __OnRspQryInstrument(self,
                             pInstrument=CThostFtdcInstrumentField,
                             pRspInfo=CThostFtdcRspInfoField,
                             nRequestID=int,
                             bIsLast=bool):
        """"""
        inst = InstrumentField()
        inst.InstrumentID = pInstrument.getInstrumentID()
        inst.ProductID = pInstrument.getProductID()
        inst.ExchangeID = pInstrument.getExchangeID()
        inst.VolumeMultiple = pInstrument.getVolumeMultiple()
        inst.PriceTick = pInstrument.getPriceTick()
        inst.MaxOrderVolume = pInstrument.getMaxLimitOrderVolume()
        self.DicInstrument[inst.InstrumentID] = inst

    def __OnRspQryAccount(self,
                          pTradingAccount=CThostFtdcTradingAccountField,
                          pRspInfo=CThostFtdcRspInfoField,
                          nRequestID=int,
                          bIsLast=bool):
        """"""
        if not self.Account:
            self.Account = TradingAccount()
        self.Account.Available = pTradingAccount.getAvailable()
        self.Account.CloseProfit = pTradingAccount.getCloseProfit()
        self.Account.Commission = pTradingAccount.getCommission()
        self.Account.CurrMargin = pTradingAccount.getCurrMargin()
        self.Account.FrozenCash = pTradingAccount.getFrozenCash()
        self.Account.PositionProfit = pTradingAccount.getPositionProfit()
        self.Account.PreBalance = pTradingAccount.getPreBalance(
        ) + pTradingAccount.getDeposit() + pTradingAccount.getWithdraw()
        self.Account.Fund = self.Account.PreBalance + pTradingAccount.getCloseProfit(
        ) + pTradingAccount.getPositionProfit(
        ) - pTradingAccount.getCommission()
        self.Account.Risk = self.Account.CurrMargin / self.Account.Fund
        if not self.IsLogin:
            self.IsLogin = True
            info = InfoField()
            info.ErrorID = 0
            info.ErrorMsg = '正确'
            self.OnRspUserLogin(info)

    def __OnRspQryPosition(self,
                           pInvestorPosition=CThostFtdcInvestorPositionField,
                           pRspInfo=CThostFtdcRspInfoField,
                           nRequestID=int,
                           bIsLast=bool):
        """"""
        if pInvestorPosition.getInstrumentID() != '':  # 偶尔出现NULL的数据导致数据转换错误
            self.__posi.append(
                pInvestorPosition)  # Struct(**f.__dict__)) #dict -> object

        if bIsLast:
            # 先排序再group才有效
            self.__posi = sorted(self.__posi, key=lambda c: '{0}_{1}'.format(c.getInstrumentID(), DirectType.Buy if c.getPosiDirection() == PosiDirectionType.Long else DirectType.Sell))
            # direction需从posidiction转换为dictiontype
            for key, group in itertools.groupby(self.__posi, lambda c: '{0}_{1}'.format(c.getInstrumentID(), DirectType.Buy if c.getPosiDirection() == PosiDirectionType.Long else DirectType.Sell)):
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
                        pf.Direction = DirectType.Buy if g.getPosiDirection(
                        ) == PosiDirectionType.Long else DirectType.Sell
                    pf.Position += g.getPosition()
                    pf.TdPosition += g.getTodayPosition()
                    pf.YdPosition = pf.Position - pf.TdPosition
                    pf.CloseProfit += g.getCloseProfit()
                    pf.PositionProfit += g.getPositionProfit()
                    pf.Commission += g.getCommission()
                    pf.Margin += g.getUseMargin()
                    cost += g.OpenCost
                # pf.Position <= 0 ? 0 : (g.Sum(n => n.PositionCost) / DicInstrumentField[pf.InstrumentID].VolumeMultiple / pf.Position);
                vm = self.DicInstrument[pf.InstrumentID].VolumeMultiple
                pf.Price = 0 if pf.Position <= 0 else cost / vm / pf.Position
            self.__posi.clear()

    def __OnRtnOrder(self, pOrder=CThostFtdcOrderField):
        """"""
        id = '{0}|{1}|{2}'.format(pOrder.getSessionID(),
                                  pOrder.getFrontID(), pOrder.getOrderRef())
        # of = OrderField()
        of = self.DicOrderField.get(id)
        if not of:
            of = OrderField()
            if pOrder.getOrderRef().isdigit():
                of.Custom = int(pOrder.getOrderRef()) % 1000000
            of.InstrumentID = pOrder.getInstrumentID()
            of.InsertTime = pOrder.getInsertTime()
            of.Direction = DirectType.Buy if DirectionType(
                pOrder.getDirection()
            ) == DirectionType.Buy else DirectType.Sell
            ot = OffsetFlagType(ord(pOrder.getCombOffsetFlag()[0]))
            of.Offset = OffsetType.Open if ot == OffsetFlagType.Open else (
                OffsetType.CloseToday
                if ot == OffsetFlagType.CloseToday else OffsetType.Close)
            of.Status = OrderStatus.Normal
            of.StatusMsg = pOrder.getStatusMsg()
            of.IsLocal = pOrder.getSessionID() == self.SessionID
            of.LimitPrice = pOrder.getLimitPrice()
            of.OrderID = id
            of.Volume = pOrder.getVolumeTotalOriginal()
            of.VolumeLeft = of.Volume
            self.DicOrderField[id] = of
            self.OnRtnOrder(of)
            # _thread.start_new_thread(self.OnRtnOrder, (of,))  # call client OnRtnOrder event
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
        else:
            if pOrder.getOrderSysID():
                of.SysID = pOrder.getOrderSysID()
                self.__dic_orderid_sysid[pOrder.getOrderSysID(
                )] = id  # 记录sysid与orderid关联,方便Trade时查找处理
            # _thread.start_new_thread(self.OnRtnOrder, (of,))

    def __OnRtnTrade(self, f):
        """"""
        tf = TradeField()
        tf.Direction = DirectType.Buy if f.getDirection(
        ) == DirectionType.Buy else DirectType.Sell
        tf.ExchangeID = f.getExchangeID()
        tf.InstrumentID = f.getInstrumentID()
        tf.Offset = OffsetType.Open if f.getOffsetFlag(
        ) == OffsetFlagType.Open else OffsetType.Close if f.getOffsetFlag(
        ) == OffsetFlagType.Close else OffsetType.CloseToday
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
        of.AvgPrice = (of.AvgPrice *
                       (of.Volume - of.VolumeLeft) + tf.Price * tf.Volume) / (
                           of.Volume - of.VolumeLeft + tf.Volume)
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
            key = '{0}_{1}'.format(tf.InstrumentID, tf.Direction)
            pf = self.DicPositionField.get(key)
            if not pf:
                pf = PositionField()
                self.DicPositionField[key] = pf
            pf.InstrumentID = tf.InstrumentID
            pf.Direction = tf.Direction
            pf.Price = (pf.Price * pf.Position + tf.Price * tf.Volume) / (
                pf.Position + tf.Volume)
            pf.TdPosition += tf.Volume
            pf.Position += tf.Volume
        else:
            key = '{0}_{1}'.format(tf.InstrumentID, DirectType.Sell
                                   if tf.Direction == DirectType.Buy else
                                   DirectType.Buy)
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
        _thread.start_new_thread(self.__onRtn, (of, tf))
        # _thread.start_new_thread(self.OnRtnOrder, (of,))
        # _thread.start_new_thread(self.OnRtnTrade, (tf,))

    def __onRtn(self, of, tf):
        self.OnRtnOrder(of)
        self.OnRtnTrade(tf)

    def __OnRspOrder(self,
                     pInputOrder=CThostFtdcInputOrderField,
                     pRspInfo=CThostFtdcRspInfoField,
                     nRequestID=int,
                     bIsLast=bool):
        """"""
        info = InfoField()
        info.ErrorID = pRspInfo.getErrorID()
        info.ErrorMsg = pRspInfo.getErrorMsg()

        id = '{0}|{1}|{2}'.format(self.SessionID, '0',
                                  pInputOrder.getOrderRef())
        of = self.DicOrderField.get(id)
        if not of:
            of = OrderField()
            l = int(pInputOrder.getOrderRef())
            of.Custom = l % 1000000
            of.InstrumentID = pInputOrder.getInstrumentID()
            of.InsertTime = time.strftime('%Y%M%d %H:%M:%S', time.localtime())
            # 对direction需特别处理（具体见ctp_struct）
            of.Direction = DirectType.Buy if DirectionType(
                pInputOrder.getDirection()
            ) == DirectionType.Buy else DirectType.Sell
            ot = OffsetFlagType(ord(pInputOrder.getCombOffsetFlag()[0]))
            of.Offset = OffsetType.Open if ot == OffsetFlagType.Open else (
                OffsetType.CloseToday
                if ot == OffsetFlagType.CloseToday else OffsetType.Close)
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

    def __OnErrOrder(self,
                     pInputOrder=CThostFtdcInputOrderField,
                     pRspInfo=CThostFtdcRspInfoField):
        """"""
        id = '{0}|{1}|{2}'.format(self.SessionID, '0',
                                  pInputOrder.getOrderRef())
        of = self.DicOrderField.get(id)

        info = InfoField()
        info.ErrorID = pRspInfo.getErrorID()
        info.ErrorMsg = pRspInfo.getErrorMsg()

        if of and of.IsLocal:
            of.Status = OrderStatus.Error
            of.StatusMsg = '{0}:{1}'.format(pRspInfo.getErrorID(),
                                            pRspInfo.getErrorMsg())
            _thread.start_new_thread(self.OnRtnErrOrder, (of, info))

    def __OnRspOrderAction(self,
                           pInputOrderAction=CThostFtdcInputOrderActionField,
                           pRspInfo=CThostFtdcRspInfoField,
                           nRequestID=int,
                           bIsLast=bool):
        id = "{0}|{1}|{2}".format(pInputOrderAction.getSessionID(),
                                  pInputOrderAction.getFrontID(),
                                  pInputOrderAction.getOrderRef())
        if self.IsLogin and id in self.DicOrderField:
            info = InfoField()
            info.ErrorID = pRspInfo.ErrorID
            info.ErrorMsg = pRspInfo.ErrorMsg
            self.OnErrCancel(self.DicOrderField[id], info)

    def __OnRtnInstrumentStatus(
            self, pInstrumentStatus=CThostFtdcInstrumentStatusField):
        self.DicInstrumentStatus[pInstrumentStatus.getInstrumentID(
        )] = pInstrumentStatus.getInstrumentStatus()
        _thread.start_new_thread(self.OnRtnInstrumentStatus,
                                 (pInstrumentStatus.getInstrumentID(),
                                  pInstrumentStatus.getInstrumentStatus()))

    def __OnRspSettlementInfoConfirm(
            self,
            pSettlementInfoConfirm=CThostFtdcSettlementInfoConfirmField,
            pRspInfo=CThostFtdcRspInfoField,
            nRequestID=int,
            bIsLast=bool):
        pass

    def ReqConnect(self, pAddress=''):
        self.t.CreateApi()
        spi = self.t.CreateSpi()
        self.t.SubscribePrivateTopic(0)  # restart 同步处理order trade
        self.t.SubscribePublicTopic(0)
        self.t.RegisterSpi(spi)

        self.t.OnFrontConnected = self.__OnFrontConnected
        self.t.OnRspUserLogin = self.__OnRspUserLogin
        self.t.OnFrontDisconnected = self.__OnFrontDisconnected
        self.t.OnRspSettlementInfoConfirm = self.__OnRspSettlementInfoConfirm
        self.t.OnRtnOrder = self.__OnRtnOrder
        self.t.OnRtnTrade = self.__OnRtnTrade
        self.t.OnRspOrderInsert = self.__OnRspOrder
        self.t.OnErrRtnOrderInsert = self.__OnErrOrder
        self.t.OnRspOrderAction = self.__OnRspOrderAction

        self.t.OnRtnInstrumentStatus = self.__OnRtnInstrumentStatus

        self.t.OnRspQryInstrument = self.__OnRspQryInstrument
        self.t.OnRspQryTradingAccount = self.__OnRspQryAccount
        self.t.OnRspQryInvestorPosition = self.__OnRspQryPosition

        self.t.RegCB()

        self.t.RegisterFront(pAddress)
        self.t.Init()
        # self.t.Join()

    def ReqUserLogin(self, user, pwd, broker):
        self.t.ReqUserLogin(BrokerID=broker, UserID=user, Password=pwd)

    def ReqOrderInsert(self,
                       pInstrument='',
                       pDirection=DirectType,
                       pOffset=OffsetType,
                       pPrice=0.0,
                       pVolume=1,
                       pType=OrderType.Limit,
                       pCustom=0):
        """"""
        OrderPriceType = OrderPriceTypeType.AnyPrice
        TimeCondition = TimeConditionType.IOC
        LimitPrice = 0.0
        VolumeCondition = VolumeConditionType.AV

        for case in switch(pType):
            if case(OrderType.Market):  # 市价
                OrderPriceType = OrderPriceTypeType.AnyPrice
                TimeCondition = TimeConditionType.IOC
                LimitPrice = 0.0
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
            BrokerID=self.BrokerID,
            InvestorID=self.Investor,
            InstrumentID=pInstrument,
            OrderRef="%06d%06d" % (self._req, pCustom % 1000000),
            UserID=self.Investor,
            # 此处ctp_enum与at_struct名称冲突
            Direction=DirectionType.Buy
            if pDirection == DirectType.Buy else DirectionType.Sell,
            CombOffsetFlag=chr(
                OffsetFlagType.Open if pOffset == OffsetType.Open else
                (OffsetFlagType.CloseToday if pOffset == OffsetType.CloseToday
                 else OffsetFlagType.Close)),
            CombHedgeFlag=HedgeFlagType.Speculation.__char__(),
            IsAutoSuspend=0,
            ForceCloseReason=ForceCloseReasonType.NotForceClose,
            IsSwapOrder=0,
            ContingentCondition=ContingentConditionType.Immediately,
            VolumeCondition=VolumeCondition,
            MinVolume=1,
            VolumeTotalOriginal=pVolume,
            OrderPriceType=OrderPriceType,
            TimeCondition=TimeCondition,
            LimitPrice=LimitPrice,
        )

    def ReqOrderAction(self, OrderID=''):
        """"""
        of = self.DicOrderField[OrderID]

        if not of:
            return -1
        else:
            pOrderId = of.OrderID
            return self.t.ReqOrderAction(
                self.BrokerID,
                self.Investor,
                OrderRef=pOrderId.split('|')[2],
                FrontID=int(pOrderId.split('|')[1]),
                SessionID=int(pOrderId.split('|')[0]),
                InstrumentID=of.InstrumentID,
                ActionFlag=ActionFlagType.Delete)

    def Release(self):
        self.t.RegisterSpi(None)
        self.t.Release()

    def OnFrontConnected(self):
        """接口连接"""
        pass

    def OnFrontDisConnected(self, error=0):
        """接口断开"""
        pass

    def OnRspUserLogin(self, info=InfoField):
        """登录响应"""
        pass

    def OnRtnOrder(self, f=OrderField):
        """委托返回"""
        pass

    def OnRtnTrade(self, f=TradeField):
        """成交返回"""
        pass

    def OnRtnCancel(self, f=OrderField):
        """撤单响应"""
        pass

    def OnErrCancel(self, f=OrderField, info=InfoField):
        """撤单失败"""
        pass

    def OnRtnErrOrder(self, f=OrderField, info=InfoField):
        """委托错误响应"""
        print(f)
        print(info)

    def OnRtnInstrumentStatus(self, inst, status):
        pass
