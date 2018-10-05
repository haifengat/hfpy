#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Author:  HaiFeng --<galaxy>
  Purpose: main function
  Created: 2016/5/31
"""

import sys
import os
import json
import yaml
import threading
import time  # from time import sleep, strftime  # 可能前面的import模块对time有影响,故放在最后
from datetime import datetime, timedelta
import getpass
import zmq  # netMQ
import gzip  # 解压

from .bar import Bar
from .data import Data
from .order import OrderItem
from .structs import BarType
from .structs import ReqPackage
from .strategy import Strategy
from .show_candle import show
from .report_stra import Report
from .config import Config

from py_ctp.trade import CtpTrade
from py_ctp.quote import CtpQuote
from py_ctp.enums import DirectType, OffsetType, OrderType, OrderStatus
from py_ctp.structs import InfoField, OrderField, TradeField, Tick


class ATP(object):
    """"""

    def __init__(self):
        self.TradingDay = ''
        self.ActionDay = ''
        self.ActionDay1 = ''
        self.tick_time = ''
        self.cfg = Config()
        self.stra_instances = []

        dllpath = os.path.join(os.getcwd(), self.cfg.ctp_dll_path)
        self.q = CtpQuote(dllpath)
        self.t = CtpTrade(dllpath)

    def on_order(self, stra: Strategy, data: Data, order: OrderItem):
        """此处调用ctp接口即可实现实际下单"""
        # print('stra order')

        self.cfg.log.war('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\n'.format(len(stra.Orders), stra.D[-1], order.Direction, order.Offset, order.Price, order.Volume, order.Remark))

        if self.cfg.real_order_enable:
            # print(order)
            order_id = stra.ID * 1000 + len(stra.GetOrders()) + 1

            # 平今与平昨;逻辑从C# 抄过来;没提示...不知道为啥,只能盲码了.
            if order.Offset != OffsetType.Open:
                key = '{0}_{1}'.format(order.Instrument, DirectType.Sell
                                       if order.Direction == DirectType.Buy
                                       else DirectType.Buy)
                # 无效,没提示...pf = PositionField()
                pf = self.t.positions.get(key)
                if not pf or pf.Position <= 0:
                    self.cfg.log.error('没有对应的持仓')
                else:
                    volClose = min(pf.Position, order.Volume)  # 可平量
                    instField = self.t.instruments[order.Instrument]
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
        for (k, v) in self.t.orders.items():
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

    def req_order(self, instrument: str, dire: DirectType, offset: OffsetType, price: float, volume: int, type: OrderType=OrderType.Limit, stra: Strategy=None):
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
        for path in self.cfg.stra_path:
            for filename in self.cfg.stra_path[path]:
                f = os.path.join(sys.path[0], '../{0}/{1}.py'.format(
                    path, filename))
                # 只处理对应的 py文件
                if os.path.isdir(f) or os.path.splitext(f)[0] == '__init__':
                    continue
                # 以目录结构作为 namespace
                module_name = "{0}.{1}".format(path, filename)
                class_name = filename

                module = __import__(module_name)  # import module

                c = getattr(getattr(module, class_name), class_name)  # 双层调用才是class,单层是为module

                if not issubclass(c, Strategy):  # 类c是Data的子类
                    continue

                # 与策略文件同名的json作为配置文件处理
                # file_name = os.path.join(os.getcwd(), path, '{0}.json'.format(class_name))
                # if os.path.exists(file_name):
                #     with open(file_name, encoding='utf-8') as stra_cfg_json_file:
                #         cfg = json.load(stra_cfg_json_file)
                file_name = os.path.join(os.getcwd(), path, '{0}.yml'.format(class_name))
                if os.path.exists(file_name):
                    with open(file_name, encoding='utf-8') as stra_cfg_json_file:
                        params = yaml.load(stra_cfg_json_file)
                        for param in params:
                            if param['ID'] not in self.cfg.stra_path[path][filename]:
                                continue
                            obj = c(param)
                            self.cfg.log.info("# obj:{0}".format(obj))
                            for data in obj.Datas:
                                data.SingleOrderOneBar = self.cfg.single_order_one_bar
                            self.stra_instances.append(obj)
                else:
                    self.cfg.log.error("缺少对应的json文件{0}".format(file_name))

    def read_data_pg(self, req: ReqPackage)->[]:
        """从postgres中读取数据"""
        if self.cfg.engine_postgres:
            conn = self.cfg.engine_postgres.raw_connection()
            cursor = conn.cursor()
            if req.Type == BarType.Min:
                sql = 'select "DateTime", \'{0}\' as "Instrument", "Tradingday", "High", "Low", "Open", "Close", "Volume", "OpenInterest" from future_min."{0}" where "Tradingday" between \'{1}\' and \'{2}\''.format(req.Instrument, req.Begin, req.End)
            if req.Type == BarType.Real:
                sql = 'select "DateTime", "Instrument", "Tradingday", "High", "Low", "Open", "Close", "Volume", "OpenInterest" from future_min.future_real where "Instrument" = \'{}\''.format(req.Instrument)
            cursor.execute(sql)
            data = cursor.fetchall()
            keys = ["DateTime", "Instrument", "Tradingday", "High", "Low", "Open", "Close", "Volume", "OpenInterest"]
            parsed_data = []
            for row in data:
                parsed_data.append(dict(zip(keys, row)))
            return parsed_data

    def read_data_zmq(self, req: ReqPackage) -> []:
        ''''''
        # pip install pyzmq即可安装
        context = zmq.Context()
        socket = context.socket(zmq.REQ)  # REQ模式,即REQ-RSP  CS结构
        # socket.connect('tcp://localhost:8888')	# 连接本地测试
        socket.connect(self.cfg.cfg_zmq)  # 实际netMQ数据服务器地址

        p = req.__dict__
        req['Type'] = req.Type.value
        socket.send_json(p)  # 直接发送__dict__转换的{}即可,不需要再转换成str

        # msg = socket.recv_unicode()	# 服务器此处查询出现异常, 排除中->C# 正常
        # 用recv接收,但是默认的socket中并没有此提示函数(可能是向下兼容的函数),不知能否转换为其他格式
        bs = socket.recv()  # 此处得到的是bytes

        # gzip解压:decompress(bytes)解压,会得到解压后的bytes,再用decode转成string
        gzipper = gzip.decompress(bs).decode()  # decode转换为string

        # json解析:与dumps对应,将str转换为{}
        bs = json.loads(gzipper)  # json解析
        return bs

    def read_bars_from_zmq(self, _stra: Strategy)->[]:
        """netMQ"""
        bars = []
        for data in _stra.Datas:
            # 请求数据格式
            req = ReqPackage()
            req.Type = BarType.Min
            req.Instrument = _stra.Instrument
            req.Begin = _stra.BeginDate
            req.End = _stra.EndDate
            # __dict__返回diction格式,即{key,value}格式

            if self.cfg.engine_postgres:
                bars = bars + self.read_data_pg(req)
            else:
                for bar in self.read_data_zmq(req):
                    bar['Instrument'] = data.Instrument
                    bars.append(bar)

            if _stra.EndDate == time.strftime("%Y%m%d", time.localtime()):
                # 实时K线数据
                req.Type = BarType.Real
                if self.cfg.engine_postgres:
                    bars = bars + self.read_data_pg(req)
                else:
                    for bar in self.read_data_zmq(req):
                        bar['Instrument'] = data.Instrument
                        bars.append(bar)

        if self.cfg.engine_postgres:
            bars.sort(key=lambda bar: bar['DateTime'])  # 按时间升序
        else:
            bars.sort(key=lambda bar: bar['_id'])  # 按时间升序
        return bars

    def read_data_test(self):
        """取历史和实时K线数据,并执行策略回测"""
        stra: Strategy = None  # 只为后面的提示信息创建
        for stra in self.stra_instances:
            stra.EnableOrder = False
            # path = 'data/{0}_{1}_{2}.pkl'.format(stra.ID, stra.BeginDate,
            #                                      stra.Datas[0].Instrument)
            # if os.path.exists(path):
            #     print('策略 {0} 正在从本地加载历史数据'.format(stra.ID))
            #     f = open(path, 'rb')
            #     listBar = pkl.load(f)
            # else:
            self.cfg.log.info('策略 {0} 正在从网络加载历史数据'.format(stra.ID))
            listBar = []
            bars = self.read_bars_from_zmq(stra)
            if self.cfg.engine_postgres:
                listBar = [Bar(b['DateTime'], b['Instrument'], b['High'], b['Low'], b['Open'], b['Close'], b['Volume'], b['OpenInterest'], b['Tradingday']) for b in bars]
            else:
                listBar = [Bar(b['_id'], b['Instrument'], b['High'], b['Low'], b['Open'], b['Close'], b['Volume'], b['OpenInterest'], b['Tradingday']) for b in bars]

            stra.OnOrder = self.on_order
            for bar in listBar:
                for data in stra.Datas:
                    if data.Instrument == bar.Instrument:
                        data.__new_min_bar__(bar)  # 调Data的onbar
            # 生成策略的测试报告
            # stra = Statistics(stra)
            Report(stra)
            bar_dict = [{'DateTime': b.D, 'Open': b.O, 'Close': b.C, 'Low': b.L, 'High': b.H} for b in data.Bars]
            show(bar_dict)
            stra.EnableOrder = True

        self.cfg.log.war("test history is end.")

    def OnFrontConnected(self, t: CtpTrade):
        """"""
        self.cfg.log.war("t:connected by client")
        if self.t.ReqUserLogin:
            self.t.ReqUserLogin(self.cfg.investor, self.cfg.pwd, self.cfg.broker)

    def relogin(self):
        """"""
        self.t.ReqUserLogout()
        self.cfg.log.info('sleep 60 seconds to wait try connect next time')
        time.sleep(60)
        self.t.ReqConnect(self.cfg.front_trade)

    def OnRspUserLogin(self, t: CtpTrade, info: InfoField):
        """"""

        self.cfg.log.info('{0}:{1}'.format(info.ErrorID, info.ErrorMsg))
        if info.ErrorID == 7:
            threading.Thread(target=self.relogin).start()
        if info.ErrorID == 0:
            self.TradingDay = self.t.tradingday
            self.get_actionday()  # 取得交易日后才能取actionday
            if not self.q.logined:
                self.q.OnConnected = self.q_OnFrontConnected
                self.q.OnUserLogin = self.q_OnRspUserLogin
                # self.q.OnTick = self.q_Tick
                self.q.OnTick = lambda o, f: threading.Thread(target=self.q_Tick, args=(o, f)).start()
                self.q.ReqConnect(self.cfg.front_quote)
                threading.Thread(target=self.showmsg).start()

    def showmsg(self):
        while self.t.logined:
            if self.tick_time != '':
                msg = ''
                stra: Strategy = None
                for stra in self.stra_instances:
                    msg += '{}[L={}; S={}]{}||'.format(type(stra).__name__, stra.PositionLong, stra.PositionShort, stra.Params)
                print(self.tick_time + '||' + msg, end='\r')
            time.sleep(1)

    def OnOrder(self, t: CtpTrade, order: OrderField):
        """"""
        self.cfg.log.info(order)

    def OnCancel(self, t: CtpTrade, order: OrderField):
        """"""
        self.cfg.log.info(order)

    def OnTrade(self, t: CtpTrade, trade: TradeField):
        """"""
        self.cfg.log.info(trade)

    def OnRtnErrOrder(self, t: CtpTrade, order: OrderField, info: InfoField):
        """"""
        self.cfg.log.info(order)

    def q_OnFrontConnected(self, q: CtpQuote):
        """"""
        self.cfg.log.info("q:connected by client")
        self.q.ReqUserLogin(self.cfg.broker, self.cfg.investor, self.cfg.pwd)

    def q_OnRspUserLogin(self, q: CtpQuote, info: InfoField):
        """"""
        self.cfg.log.info(info)
        for stra in self.stra_instances:
            for data in stra.Datas:
                self.q.ReqSubscribeMarketData(data.Instrument)

    def q_Tick(self, q: CtpQuote, tick: Tick):
        """"""
        # print(tick)
        # self.fix_tick(tick)
        actionday = self.TradingDay
        if tick.UpdateTime[0:2] > '20':
            actionday = self.Actionday
        elif tick.UpdateTime[0:2] < '04':
            actionday = self.Actionday1

        ut = actionday[0:4] + '-' + actionday[4:6] + '-' + actionday[6:] + ' ' + tick.UpdateTime
        tick.UpdateTime = ut
        for stra in self.stra_instances:
            for data in stra.Datas:
                if data.Instrument == tick.Instrument:
                    data.on_tick(tick, self.TradingDay)
        self.tick_time = ut

    def get_actionday(self):
        if not self.cfg.engine_postgres:
            self.cfg.log.error('postgres 数据库未连接!')
            return

        conn = self.cfg.engine_postgres.raw_connection()
        cursor = conn.cursor()
        cursor.execute('select _id from future_config.trade_date where trading = 1')
        self.trading_days = [c[0] for c in cursor.fetchall()]
        # 接口未登录,不计算Actionday
        if self.TradingDay == '':
            return
        self.Actionday = self.TradingDay if self.trading_days.index(self.TradingDay) == 0 else self.trading_days[self.trading_days.index(self.TradingDay) - 1]
        self.Actionday1 = (datetime.strptime(self.Actionday, '%Y%m%d') + timedelta(days=1)).strftime('%Y%m%d')

    def CTPRun(self):
        """"""
        if self.cfg.front_trade == '' or self.cfg.front_quote == '':
            self.cfg.log.war('交易接口未配置')
            return
        if self.cfg.investor == '':
            self.cfg.investor = input('invesorid:')
        else:
            self.cfg.log.war('{} loging by ctp'.format(self.cfg.investor))
        if self.cfg.pwd == '':
            self.cfg.pwd = getpass.getpass()
        self.t.OnConnected = self.OnFrontConnected
        self.t.OnDisConnected = lambda o, x: print('disconnected: {}'.format(x))
        self.t.OnUserLogin = self.OnRspUserLogin
        self.t.OnOrder = self.OnOrder
        self.t.OnTrade = self.OnTrade
        self.t.OnCancel = self.OnCancel
        self.t.OnErrOrder = self.OnRtnErrOrder
        self.t.OnInstrumentStatus = lambda x, y, z: str(z)  # print(z)  不再打印交易状态

        self.t.ReqConnect(self.cfg.front_trade)
        while not self.q.logined:
            time.sleep(1)
