# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/9/13'
"""

import sys
import os
import _thread
from time import sleep

# sys.path.append('..')  #调用父目录下的模块
sys.path.append(os.path.join(sys.path[0], '..'))  # 调用父目录下的模块
sys.path.append(os.path.join(sys.path[0], '../..'))  # 调用父目录下的模块

from py_ctp.enums import OrderPriceTypeType, DirectionType, OffsetFlagType, HedgeFlagType, TimeConditionType, VolumeConditionType, ContingentConditionType, ForceCloseReasonType, OrderStatusType, ActionFlagType
from py_ctp.structs import CThostFtdcMarketDataField, CThostFtdcRspAuthenticateField, CThostFtdcRspInfoField, CThostFtdcSettlementInfoConfirmField, CThostFtdcInstrumentStatusField, CThostFtdcInputOrderField, CThostFtdcOrderField, CThostFtdcInvestorPositionField, CThostFtdcTradingAccountField, CThostFtdcSpecificInstrumentField
from py_ctp.trade import Trade
from py_ctp.quote import Quote


class Test:
    def __init__(self):
        """初始化 运行的目录下需要创建log目录"""
        """交易前置"""
        self.front_trade = ''
        # 行情前置
        self.front_quote = ''
        self.investor = ''
        self.pwd = ''
        self.broker = ''
        self.TradingDay = ''
        # self.log = open('orders.csv', 'w')
        # self.log.write('')  # 清空内容

        self.stra_instances = []

        self.Session = ''
        self.q = Quote()
        self.t = Trade()
        self.req = 0
        self.ordered = False
        self.needAuth = False

    def q_OnFrontConnected(self):
        print('connected')
        self.q.ReqUserLogin(
            BrokerID=self.broker, UserID=self.investor, Password=self.pwd)

    def q_OnRspUserLogin(self, rsp, info, req, last):
        print(info)
        self.q.SubscribeMarketData('rb1805')

    def q_OnRspSubMarketData(
            self,
            pSpecificInstrument=CThostFtdcSpecificInstrumentField,
            pRspInfo=CThostFtdcRspInfoField,
            nRequestID=int,
            bIsLast=bool):
        pass

    def q_OnTick(self, tick):
        f = CThostFtdcMarketDataField()
        f = tick

        if not self.ordered:
            print(tick)
            _thread.start_new_thread(self.Order, (f, ))
            self.ordered = True

    def Order(self, f):
        print("报单")
        self.req += 1
        self.t.ReqOrderInsert(
            BrokerID=self.broker,
            InvestorID=self.investor,
            InstrumentID=f.getInstrumentID(),
            OrderRef='{0:>12}'.format(self.req),
            UserID=self.investor,
            OrderPriceType=OrderPriceTypeType.LimitPrice,
            Direction=DirectionType.Buy,
            CombOffsetFlag=OffsetFlagType.Open.__char__(),
            CombHedgeFlag=HedgeFlagType.Speculation.__char__(),
            LimitPrice=f.getLastPrice() - 50,
            VolumeTotalOriginal=1,
            TimeCondition=TimeConditionType.GFD,
            # GTDDate=''
            VolumeCondition=VolumeConditionType.AV,
            MinVolume=1,
            ContingentCondition=ContingentConditionType.Immediately,
            StopPrice=0,
            ForceCloseReason=ForceCloseReasonType.NotForceClose,
            IsAutoSuspend=0,
            IsSwapOrder=0,
            UserForceClose=0)

    def OnFrontConnected(self):
        print('connected')
        if self.needAuth:
            self.t.ReqAuthenticate(self.broker, self.investor, '@haifeng',
                                   '8MTL59FK1QGLKQW2')
        else:
            self.t.ReqUserLogin(
                BrokerID=self.broker,
                UserID=self.investor,
                Password=self.pwd,
                UserProductInfo='@haifeng')

    def OnRspAuthenticate(self,
                          pRspAuthenticateField=CThostFtdcRspAuthenticateField,
                          pRspInfo=CThostFtdcRspInfoField,
                          nRequestID=int,
                          bIsLast=bool):
        print('auth：{0}:{1}'.format(pRspInfo.getErrorID(),
                                    pRspInfo.getErrorMsg()))
        self.t.ReqUserLogin(
            BrokerID=self.broker,
            UserID=self.investor,
            Password=self.pwd,
            UserProductInfo='@haifeng')

    def OnRspUserLogin(self, rsp, info, req, last):
        print(info)
        i = CThostFtdcRspInfoField()
        i = info

        if i.getErrorID() == 0:
            self.Session = rsp.getSessionID()
            self.t.ReqSettlementInfoConfirm(
                BrokerID=self.broker, InvestorID=self.investor)

    def OnRspSettlementInfoConfirm(
            self,
            pSettlementInfoConfirm=CThostFtdcSettlementInfoConfirmField,
            pRspInfo=CThostFtdcRspInfoField,
            nRequestID=int,
            bIsLast=bool):
        print('settle')
        _thread.start_new_thread(self.StartQuote, ())
        _thread.start_new_thread(self.Qry, ())

    def StartQuote(self):
        print('start quote')
        self.q.CreateApi()
        spi = self.q.CreateSpi()
        self.q.RegisterSpi(spi)

        self.q.OnFrontConnected = self.q_OnFrontConnected
        self.q.OnRspUserLogin = self.q_OnRspUserLogin
        self.q.OnRtnDepthMarketData = self.q_OnTick
        self.q.OnRspSubMarketData = self.q_OnRspSubMarketData
        self.q.RegCB()

        self.q.RegisterFront(self.front_quote)
        self.q.Init()
        # self.q.Join()

    def Qry(self):
        sleep(1.1)
        self.t.ReqQryInstrument()
        while True:
            sleep(1.1)
            self.t.ReqQryTradingAccount(self.broker, self.investor)
            sleep(1.1)
            self.t.ReqQryInvestorPosition(self.broker, self.investor)
            return

    def OnRtnInstrumentStatus(
            self, pInstrumentStatus=CThostFtdcInstrumentStatusField):
        pass

    def OnRspOrderInsert(self,
                         pInputOrder=CThostFtdcInputOrderField,
                         pRspInfo=CThostFtdcRspInfoField,
                         nRequestID=int,
                         bIsLast=bool):
        print(pRspInfo)
        print(pInputOrder)
        print(pRspInfo.getErrorMsg())

    def OnRtnOrder(self, pOrder=CThostFtdcOrderField):
        # print(pOrder)
        if pOrder.getSessionID() == self.Session and pOrder.getOrderStatus(
        ) == OrderStatusType.NoTradeQueueing:
            print("撤单")
            self.t.ReqOrderAction(
                self.broker,
                self.investor,
                InstrumentID=pOrder.getInstrumentID(),
                OrderRef=pOrder.getOrderRef(),
                FrontID=pOrder.getFrontID(),
                SessionID=pOrder.getSessionID(),
                ActionFlag=ActionFlagType.Delete)

    def OnRspInstrument(self, instrument, rspinfo, nreq, last):
        pass

    def OnRspPosition(self, pInvestorPosition=CThostFtdcInvestorPositionField, pRspInfo=CThostFtdcRspInfoField, nRequestID=int, bIsLast=bool):
        pass

    def OnRspAccount(self, pTradingAccount=CThostFtdcTradingAccountField, pRspInfo=CThostFtdcRspInfoField, nRequestID=int, bIsLast=bool):
        pass

    def CTPRun(self,
               front_trade='tcp://180.168.146.187:10001',
               front_quote='tcp://180.168.146.187:10011',
               broker='9999',
               investor='008109',
               pwd='1'):
        """"""

        self.front_trade = front_trade
        self.front_quote = front_quote
        self.broker = broker
        self.investor = investor
        self.pwd = pwd

        self.t.CreateApi()
        spi = self.t.CreateSpi()
        self.t.SubscribePrivateTopic(2)
        self.t.SubscribePublicTopic(2)
        self.t.RegisterSpi(spi)

        self.t.OnFrontConnected = self.OnFrontConnected
        self.t.OnRspUserLogin = self.OnRspUserLogin
        self.t.OnRspSettlementInfoConfirm = self.OnRspSettlementInfoConfirm
        self.t.OnRspQryInstrument = self.OnRspInstrument
        self.t.OnRtnInstrumentStatus = self.OnRtnInstrumentStatus
        self.t.OnRtnOrder = self.OnRtnOrder
        self.t.OnRspQryInvestorPosition = self.OnRspPosition
        self.t.OnRspQryTradingAccount = self.OnRspAccount
        # self.t.OnRtnTrade = self.OnRtnTrade
        # self.t.OnRtnCancel = self.OnRtnCancel
        # self.t.OnRtnErrOrder = self.OnRtnErrOrder

        self.t.RegCB()
        self.t.RegisterFront(self.front_trade)
        self.t.Init()


if __name__ == '__main__':
    p = Test()
    if len(sys.argv) == 1:
        p.CTPRun()
    else:
        p.CTPRun(investor=sys.argv[1], pwd=sys.argv[2])
    input()
