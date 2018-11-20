# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2017/11/13'
"""
import time
from .structs import IntervalType
from .bar import Bar
from .data import Data
from .order import OrderItem
from py_ctp.enums import DirectType, OffsetType, OrderType
from py_ctp.structs import OrderField, TradeField, InfoField


class Strategy(object):
    '''策略类 '''

    def __init__(self, dict_cfg):
        '''初始化'''
        '''策略标识'''
        self.ID = 0
        '''数据序列'''
        self.Datas = []
        """起始测试时间
        格式:yyyyMMdd[%Y%m%d]
        默认:20170101"""
        self.BeginDate = '20170101'
        '''结束测试时间
        格式:yyyyMMdd[%Y%m%d]
        默认:当前时间'''
        self.EndDate = time.strftime("%Y%m%d", time.localtime())  # 默认值取当日期
        '''参数'''
        self.Params = []
        '''分笔测试'''
        self.TickTest = False

        if dict_cfg == '':
            return
        else:
            self.ID = dict_cfg['ID']
            self.Params = dict_cfg['Params']
            self.BeginDate = str(dict_cfg['BeginDate'])
            if 'TickTest' in dict_cfg:
                self.TickTest = dict_cfg['TickTest']
            if 'EndDate' in dict_cfg:
                self.EndDate = dict_cfg['EndDate']
            for data in dict_cfg['Datas']:
                newdata = Data(self.__BarUpdate, self.__OnOrder)
                newdata.Instrument = data['Instrument']
                newdata.Interval = data['Interval']
                newdata.IntervalType = IntervalType[data['IntervalType']]
                self.Datas.append(newdata)

    @property
    def Bars(self):
        '''k'''
        return self.Datas[0].Bars

    @property
    def Instrument(self):
        '''合约'''
        return self.Datas[0].Instrument

    @property
    def Interval(self):
        '''周期'''
        return self.Datas[0].Interval

    @property
    def IntervalType(self):
        '''周期类型'''
        return self.Datas[0].IntervalType

    @property
    def Tick(self):
        '''分笔数据
        Tick.Instrument用来判断是否有实盘数据'''
        return self.Datas[0].Tick

    @property
    def Orders(self):
        '''买卖信号'''
        return self.Datas[0].Orders

    @property
    def IndexDict(self):
        '''指标字典
        策略使用的指标保存在此字典中
        以便管理程序显示和处理'''
        return self.Datas[0].IndexDict

    @property
    def D(self):
        '''时间'''
        return self.Datas[0].D

    @property
    def H(self):
        '''最高价'''
        return self.Datas[0].H

    @property
    def L(self):
        '''最低价'''
        return self.Datas[0].L

    @property
    def O(self):
        '''开盘价'''
        return self.Datas[0].O

    @property
    def C(self):
        '''收盘价'''
        return self.Datas[0].C

    @property
    def V(self):
        '''交易量'''
        return self.Datas[0].V

    @property
    def I(self):
        '''持仓量'''
        return self.Datas[0].I

    @property
    def AvgEntryPriceShort(self):
        '''开仓均价-空'''
        return self.Datas[0].AvgEntryPriceShort

    @property
    def AvgEntryPriceLong(self):
        '''开仓均价-多'''
        return self.Datas[0].AvgEntryPriceLong

    @property
    def PositionLong(self):
        '''持仓-多'''
        return self.Datas[0].PositionLong

    @property
    def PositionShort(self):
        '''持仓-空'''
        return self.Datas[0].PositionShort

    @property
    def EntryDateLong(self):
        '''开仓时间-多'''
        return self.Datas[0].EntryDateLong

    @property
    def EntryPriceLong(self):
        '''开仓价格-多'''
        return self.Datas[0].EntryPriceLong

    @property
    def ExitDateShort(self):
        '''平仓时间-空'''
        return self.Datas[0].ExitDateShort

    @property
    def ExitPriceShort(self):
        '''平仓价-空'''
        return self.Datas[0].ExitPriceShort

    @property
    def EntryDateShort(self):
        '''开仓时间-空'''
        return self.Datas[0].EntryDateShort

    @property
    def EntryPriceShort(self):
        '''开仓价-空'''
        return self.Datas[0].EntryPriceShort

    @property
    def ExitDateLong(self):
        '''平仓时间-多'''
        return self.Datas[0].ExitDateLong

    @property
    def ExitPriceLong(self):
        '''平仓价-多'''
        return self.Datas[0].ExitPriceLong

    @property
    def LastEntryDateShort(self):
        '''最后开仓时间-空'''
        return self.Datas[0].LastEntryDateShort

    @property
    def LastEntryPriceShort(self):
        '''最后开仓价-空'''
        return self.Datas[0].LastEntryPriceShort

    @property
    def LastEntryDateLong(self):
        '''最后开仓时间-多'''
        return self.Datas[0].LastEntryDateLong

    @property
    def LastEntryPriceLong(self):
        '''最后开仓价-多'''
        return self.Datas[0].LastEntryPriceLong

    @property
    def IndexEntryLong(self):
        '''开仓到当前K线数量-多'''
        return self.Datas[0].IndexEntryLong

    @property
    def IndexEntryShort(self):
        '''开仓到当前K线数量-空'''
        return self.Datas[0].IndexEntryShort

    @property
    def IndexLastEntryLong(self):
        '''最后平仓到当前K线数量-多'''
        return self.Datas[0].IndexLastEntryLong

    @property
    def IndexLastEntryShort(self):
        '''最后平仓到当前K线数量-空'''
        return self.Datas[0].IndexLastEntryShort

    @property
    def IndexExitLong(self):
        '''平仓到当前K线数量-多'''
        return self.Datas[0].IndexExitLong

    @property
    def IndexExitShort(self):
        '''平仓到当前K线数量-空'''
        return self.Datas[0].IndexExitShort

    @property
    def Position(self):
        '''持仓净头寸'''
        return self.Datas[0].Position

    @property
    def CurrentBar(self):
        '''当前K线序号(0开始)'''
        return self.Datas[0].CurrentBar

    def Buy(self, price: float, volume: int, remark: str = ''):
        """买开"""
        self.Datas[0].Buy(price, volume, remark)

    def Sell(self, price, volume, remark):
        """买平"""
        self.Datas[0].Sell(price, volume, remark)

    def SellShort(self, price, volume, remark):
        """卖开"""
        self.Datas[0].SellShort(price, volume, remark)

    def BuyToCover(self, price, volume, remark):
        """买平"""
        self.Datas[0].BuyToCover(price, volume, remark)

    def OnBarUpdate(self, data: Data, bar: Bar):
        """行情触发
        历史行情:每分钟触发一次
        实时行情:每分钟触发一次"""
        pass

    def GetOrders(self) -> []:
        """获取策略相关委托,返回[]"""
        return self._get_orders(self)

    def _get_orders(self, stra) -> []:
        """获取策略相关委托,返回[]"""
        pass

    def GetLastOrder(self) -> OrderField:
        """获取最后一个委托"""
        return self._get_lastorder(self)

    def _get_lastorder(self, stra) -> OrderField:
        """获取最后一个委托"""
        pass

    def GetNotFillOrders(self) -> []:
        """获取未成交委托"""
        return self._get_notfill_orders(self)

    def _get_notfill_orders(self, stra) -> []:
        """获取未成交委托"""
        pass

    def ReqOrder(self, instrument: str, dire: DirectType, offset: OffsetType, price: float, volume: int, type: OrderType = OrderType.Limit):
        """发送委托"""
        self._req_order(instrument, dire, offset, price, volume, type, self)

    def _req_order(self, instrument, dire, offset, price, volume, type, stra):
        pass

    def ReqCancel(self, orderid: str):
        """发送撤单"""
        pass

    def ReqCancelAll(self):
        """撤销所有委托"""
        self._req_cancel_all(self, self)

    def _req_cancel_all(self, stra):
        """撤销所有委托"""
        pass

    def __BarUpdate(self, data: Data, bar: Bar):
        """调用策略的逻辑部分"""
        # self.OnBarUpdate(data, bar)
        if data.Interval == self.Interval and data.IntervalType == self.IntervalType:
            self.OnBarUpdate(data, bar)

    def __OnOrder(self, data: Data, order: OrderItem):
        """调用外部接口的reqorder"""
        self._data_order(self, data, order)

    # 外层接口调用
    def _data_order(self, stra, data: Data, order: OrderItem):
        """继承类中实现此函数,有策略信号产生时调用"""
        pass

    def OnOrder(self, order: OrderField()):
        """委托响应"""
        pass

    def OnTrade(self, trade: TradeField()):
        """成交响应"""
        pass

    def OnCancel(self, order: OrderField):
        """撤单响应"""
        pass

    def OnErrOrder(self, order: OrderField, info: InfoField):
        """委托错误"""
        pass

    def OnErrCancel(self, order: OrderField, info: InfoField):
        """撤单错误"""
        pass
