#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Author:  HaiFeng --<galaxy>
  Purpose: main function
  Created: 2016/5/31
"""

import sys
import os

import zmq  # netMQ
import gzip  # 解压
import json
import _thread
import time  # from time import sleep, strftime  # 可能前面的import模块对time有影响,故放在最后

sys.path.append(os.path.join(sys.path[0], '..'))  # 调用父目录下的模块

from py_at.bar import Bar
from py_at.data import Data
from py_at.order import OrderItem
from py_at.adapters.ctp_trade import CtpTrade
from py_at.adapters.ctp_quote import CtpQuote
from py_at.enums import DirectType, OffsetType, OrderType, OrderStatus
from py_at.structs import InfoField, OrderField, TradeField, ReqPackage
from py_at.tick import Tick
from py_at.strategy import Strategy
from py_at.Statistics import Statistics


class stra_test(object):
    """"""

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

        stra_cfg = json.load(open(sys.path[0] + '/stra_test.json'))
        self.stra_path_list = stra_cfg['stra_path']
        self.stra_instances = []

        self.q = CtpQuote()
        self.t = CtpTrade()

    def on_order(self, stra=Strategy(''), data=Data(), order=OrderItem()):
        """此处调用ctp接口即可实现实际下单"""
        # print('stra order')

        # self.log.write('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\n'.format(len(p.Orders), stra.Bars[0].D, _order.Direction, _order.Offset, _order.Price, _order.Volume, _order.Remark))

        if stra.EnableOrder:
            # print(order)
            order_id = stra.ID * 1000 + len(stra.GetOrders()) + 1

            # 平今与平昨;逻辑从C# 抄过来;没提示...不知道为啥,只能盲码了.
            if order.Offset != OffsetType.Open:
                key = '{0}_{1}'.format(order.Instrument, DirectType.Sell
                                       if order.Direction == DirectType.Buy
                                       else DirectType.Buy)
                # 无效,没提示...pf = PositionField()
                pf = self.t.DicPositionField.get(key)
                if not pf or pf.Position <= 0:
                    print('没有对应的持仓')
                else:
                    volClose = min(pf.Position, order.Volume)  # 可平量
                    instField = self.t.DicInstrument[order.Instrument]
                    if instField.ExchangeID == 'SHFE':
                        tdClose = min(volClose, pf.TdPosition)
                        if tdClose > 0:
                            self.t.ReqOrderInsert(
                                order.Instrument, order.Direction,
                                OffsetType.CloseToday, order.Price, tdClose,
                                OrderType.Limit, order_id)
                            volClose -= tdClose
                    if volClose > 0:
                        self.t.ReqOrderInsert(
                            order.Instrument, order.Direction,
                            OffsetType.Close, order.Price, volClose,
                            OrderType.Limit, order_id)
            else:
                self.t.ReqOrderInsert(order.Instrument, order.Direction,
                                      OffsetType.Open, order.Price,
                                      order.Volume, OrderType.Limit, order_id)

    def get_orders(self, stra):
        """获取策略相关的委托列表"""
        rtn = []
        for (k, v) in self.t.DicOrderField.items():
            if v.Custom // 1000 == stra.ID:
                rtn.append(v)
        return rtn

    def get_lastorder(self, stra):
        """获取最后一个委托"""
        rtn = self.get_orders(stra)
        if len(rtn) > 0:
            sorted(rtn, key=lambda o: o.Custom)
            return rtn[-1]
        return None

    def get_notfill_orders(self, stra):
        """获取未成交委托"""
        rtn = []
        orders = self.get_orders(stra)
        if len(orders) > 0:
            for order in orders:
                if order.Status == OrderStatus.Normal or order.Status == OrderStatus.Partial:
                    rtn.append(order)
        return rtn

    def req_order(self,
                  instrument='',
                  dire=DirectType.Buy,
                  offset=OffsetType.Open,
                  price=0.0,
                  volume=0,
                  type=OrderType.Limit,
                  stra=None):
        """发送委托"""
        order_id = stra.ID * 1000 + len(stra.GetOrders()) + 1
        self.t.ReqOrderInsert(instrument, dire, offset, price, volume, type,
                              order_id)

    def cancel_all(self, stra):
        """撤销所有委托"""
        for order in self.get_notfill_orders(stra):
            self.t.ReqOrderAction(order.OrderID)

    def load_strategy(self):
        """加载../strategy目录下的策略"""
        """通过文件名取到对应的继承Data的类并实例"""
        # for path in ['strategies', 'private']:
        for path in self.stra_path_list:
            files = os.listdir(os.path.join(sys.path[0], '../{0}'.format(path)))
            for f in files:
                if os.path.isdir(f) or os.path.splitext(f)[0] == '__init__' or os.path.splitext(f)[-1] != ".py":
                    continue
                # 目录结构???
                module_name = "{1}.{0}".format(os.path.splitext(f)[0], path)
                class_name = os.path.splitext(f)[0]

                module = __import__(module_name)  # import module

                c = getattr(getattr(module, class_name), class_name)  # 双层调用才是class,单层是为module

                if not issubclass(c, Strategy):  # 类c是Data的子类
                    continue

                # 与策略文件同名的json作为配置文件处理
                file_name = os.path.join(sys.path[0], '../{0}/'.format(path),
                                         '{0}.json'.format(class_name))
                if os.path.split(file_name)[1] in files:
                    with open(
                            file_name, encoding='utf-8') as stra_cfg_json_file:
                        cfg = json.load(stra_cfg_json_file)
                        # 是否启用此策略
                        if 'enable' in cfg and not cfg['enable']:
                            continue
                        for json_cfg in cfg['instance']:
                            if 'enable' in json_cfg and not json_cfg['enable']:
                                continue
                            obj = c(json_cfg)
                            print("# obj:{0}", obj)
                            self.stra_instances.append(obj)

    def read_from_mq(self, stra):
        """netMQ"""
        _stra = Strategy('')  # 为了下面的提示信息创建
        _stra = stra
        # pip install pyzmq即可安装
        context = zmq.Context()
        socket = context.socket(zmq.REQ)  # REQ模式,即REQ-RSP  CS结构
        # socket.connect('tcp://localhost:8888')	# 连接本地测试
        socket.connect('tcp://58.247.171.146:5055')  # 实际netMQ数据服务器地址
        bars = []
        for data in _stra.Datas:
            # 请求数据格式
            req = ReqPackage()
            req.Type = 0  # BarType.Min
            req.Instrument = _stra.Instrument
            req.Begin = _stra.BeginDate
            req.End = _stra.EndDate
            # __dict__返回diction格式,即{key,value}格式
            p = req.__dict__
            socket.send_json(p)  # 直接发送__dict__转换的{}即可,不需要再转换成str

            # msg = socket.recv_unicode()	# 服务器此处查询出现异常, 排除中->C# 正常
            # 用recv接收,但是默认的socket中并没有此提示函数(可能是向下兼容的函数),不知能否转换为其他格式
            bs = socket.recv()  # 此处得到的是bytes

            # gzip解压:decompress(bytes)解压,会得到解压后的bytes,再用decode转成string
            gzipper = gzip.decompress(bs).decode()  # decode转换为string

            # json解析:与dumps对应,将str转换为{}
            bs = json.loads(gzipper)  # json解析
            for bar in bs:
                bar['Instrument'] = data.Instrument
                bars.append(bar)

            if _stra.EndDate == time.strftime("%Y%m%d", time.localtime()):
                # 实时K线数据
                req.Type = 2  # BarType.Real
                p = req.__dict__
                socket.send_json(p)  # 直接发送__dict__转换的{}即可,不需要再转换成str
                bs = socket.recv()  # 此处得到的是bytes
                # gzip解压:decompress(bytes)解压,会得到解压后的bytes,再用decode转成string
                gzipper = gzip.decompress(bs).decode()  # decode转换为string
                # json解析:与dumps对应,将str转换为{}
                bs = json.loads(gzipper)  # json解析
                for bar in bs:
                    bar['Instrument'] = data.Instrument
                    bars.append(bar)

        bars.sort(key=lambda bar: bar['_id'])  # 按时间升序
        return bars

    def read_data_test(self):
        """取历史和实时K线数据,并执行策略回测"""
        stra = Strategy('')  # 只为后面的提示信息创建
        for stra in self.stra_instances:
            stra.EnableOrder = False
            # print params os strategy
            # stra.OnOrder = self.on_order
            for p in stra.Params:
                print("{0}:{1}".format(p, stra.Params[p]), end=' ')

            # 取数据
            bars = self.read_from_mq(stra)
            for doc in bars:
                bar = Bar(doc["_id"], doc["High"], doc["Low"], doc["Open"],
                          doc["Close"], doc["Volume"], doc["OpenInterest"])
                for data in stra.Datas:
                    if data.Instrument == doc["Instrument"]:
                        data.__new_min_bar__(bar)  # 调Data的onbar
            # 生成策略的测试报告
            stra = Statistics(stra)
            stra.EnableOrder = True

        print("\ntest history is end.")

    def OnFrontConnected(self):
        """"""
        print("t:connected by client")
        self.t.ReqUserLogin(self.investor, self.pwd, self.broker)

    def relogin(self):
        """"""
        self.t.Release()
        print('sleep 60 seconds to wait try connect next time')
        time.sleep(60)
        self.t.ReqConnect(self.front_trade)

    def OnRspUserLogin(self, info=InfoField()):
        """"""

        print('{0}:{1}'.format(info.ErrorID, info.ErrorMsg))
        if info.ErrorID == 7:
            _thread.start_new_thread(self.relogin, ())
        if info.ErrorID == 0:
            self.TradingDay = self.t.TradingDay
            if not self.q.IsLogin:
                self.q.OnFrontConnected = self.q_OnFrontConnected
                self.q.OnRspUserLogin = self.q_OnRspUserLogin
                self.q.OnRtnTick = self.q_Tick
                self.q.ReqConnect(self.front_quote)

    def OnOrder(self, order=OrderField):
        """"""
        print(order)

    def OnCancel(self, order=OrderField):
        """"""
        print(order)

    def OnTrade(self, trade=TradeField):
        """"""
        print(trade)

    def OnRtnErrOrder(self, order=OrderField, info=InfoField):
        """"""
        print(order)

    def q_OnFrontConnected(self):
        """"""
        print("q:connected by client")
        self.q.ReqUserLogin(self.broker, self.investor, self.pwd)

    def q_OnRspUserLogin(self, info=InfoField):
        """"""
        print(info)
        for stra in self.stra_instances:
            for data in stra.Datas:
                self.q.ReqSubscribeMarketData(data.Instrument)

    def q_Tick(self, tick=Tick):
        """"""
        # print(tick)
        for stra in self.stra_instances:
            for data in stra.Datas:
                if data.Instrument == tick.Instrument:
                    data.on_tick(tick)
                    # print(tick)

    def CTPRun(self,
               front_trade='tcp://180.168.146.187:10001',
               front_quote='tcp://180.168.146.187:10011',
               broker='9999',
               investor='008109',
               pwd='1'):
        """"""
        self.t.OnFrontConnected = self.OnFrontConnected
        self.t.OnRspUserLogin = self.OnRspUserLogin
        self.t.OnRtnOrder = self.OnOrder
        self.t.OnRtnTrade = self.OnTrade
        self.t.OnRtnCancel = self.OnCancel
        self.t.OnRtnErrOrder = self.OnRtnErrOrder

        self.front_trade = front_trade
        self.front_quote = front_quote
        self.broker = broker
        self.investor = investor
        self.pwd = pwd
        self.t.ReqConnect(front_trade)


if __name__ == '__main__':
    p = stra_test()
    if len(sys.argv) == 1:
        print("无参时将不登录接口")
    else:
        if len(sys.argv) == 3:
            p.CTPRun(investor=sys.argv[1], pwd=sys.argv[2])
        elif len(sys.argv) == 6:   # 包括前置
            p.CTPRun(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4],
                     sys.argv[5])
        else:
            sys.exit("参数数目不正确,程序退出.")
        while not p.q.IsLogin:
            time.sleep(1)
    p.load_strategy()
    p.read_data_test()

    # 注销148行
    stra = Strategy('')
    for stra in p.stra_instances:
        stra.EnableOrder = True
        stra._data_order = p.on_order
        stra._get_orders = p.get_orders
        stra._get_lastorder = p.get_lastorder
        stra._get_notfill_orders = p.get_notfill_orders
        stra._req_order = p.req_order
        stra.ReqCancel = p.t.ReqOrderAction
        stra._req_cancel_all = p.cancel_all

        p.t.OnRtnOrder = stra.OnOrder
        p.t.OnRtnTrade = stra.OnTrade
        p.t.OnRtnCancel = stra.OnCancel
        p.t.OnRtnErrOrder = stra.OnErrOrder
        p.t.OnErrCancel = stra.OnErrCancel

        for data in stra.Datas:
            data.SingleOrderOneBar = False
            if p.q and p.q.IsLogin:
                p.q.ReqSubscribeMarketData(data.Instrument)
    input()
