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
            # 价格修正
            order.Price = order.Price // self.t.instruments[order.Instrument].PriceTick * self.t.instruments[order.Instrument].PriceTick

            if order.Offset != OffsetType.Open:
                key = '{0}_{1}'.format(order.Instrument, 'Sell' if order.Direction == DirectType.Buy else 'Buy')
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
                            self.t.ReqOrderInsert(order.Instrument, order.Direction, OffsetType.CloseToday, order.Price, tdClose, OrderType.Limit, order_id)
                            volClose -= tdClose
                    if volClose > 0:
                        self.t.ReqOrderInsert(order.Instrument, order.Direction, OffsetType.Close, order.Price, volClose, OrderType.Limit, order_id)
            else:
                self.t.ReqOrderInsert(order.Instrument, order.Direction, OffsetType.Open, order.Price, order.Volume, OrderType.Limit, order_id)

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

    def req_order(self, instrument: str, dire: DirectType, offset: OffsetType, price: float, volume: int, type: OrderType = OrderType.Limit, stra: Strategy = ''):
        """发送委托"""
        order_id = stra.ID * 1000 + len(stra.GetOrders()) + 1
        # 价格修正
        price = price // self.t.instruments[instrument].PriceTick * self.t.instruments[instrument].PriceTick
        self.t.ReqOrderInsert(instrument, dire, offset, price, volume, type, order_id)

    def cancel_all(self, stra):
        """撤销所有委托"""
        for order in self.get_notfill_orders(stra):
            self.t.ReqOrderAction(order.OrderID)

    def load_strategy(self):
        """加载../strategy目录下的策略"""
        """通过文件名取到对应的继承Data的类并实例"""
        for path in self.cfg.stra_path:
            for filename in self.cfg.stra_path[path]:
                f = os.path.join(sys.path[0], '../{0}/{1}.py'.format(path, filename))
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
                        for param in [p for p in params if p is not None]:  # 去除None的配置
                            if param['ID'] not in self.cfg.stra_path[path][filename]:
                                continue
                            stra: Strategy = c(param)
                            stra.ID = param['ID']
                            self.cfg.log.info("# strategy:{0}".format(stra))

                            for data in stra.Datas:
                                data.SingleOrderOneBar = self.cfg.single_order_one_bar
                            self.stra_instances.append(stra)
                else:
                    self.cfg.log.error("缺少对应的json文件{0}".format(file_name))

    def get_data_zmq(self, req: ReqPackage) -> []:
        ''''''
        # pip install pyzmq即可安装
        context = zmq.Context()
        socket = context.socket(zmq.REQ)  # REQ模式,即REQ-RSP  CS结构
        # socket.connect('tcp://localhost:8888')	# 连接本地测试
        socket.connect(self.cfg.cfg_zmq)  # 实际netMQ数据服务器地址

        p = req.__dict__()
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

    def read_bars_pg(self, req: ReqPackage)->[]:
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

    def read_bars(self, stra: Strategy)->[]:
        """netMQ"""
        bars = []
        for data in stra.Datas:
            # 请求数据格式
            req = ReqPackage()
            req.Type = BarType.Min
            req.Instrument = stra.Instrument
            req.Begin = stra.BeginDate
            req.End = stra.EndDate
            # __dict__返回diction格式,即{key,value}格式

            if self.cfg.engine_postgres:
                bars = bars + self.read_bars_pg(req)
            else:
                for bar in self.get_data_zmq(req):
                    bar['Instrument'] = data.Instrument
                    bar['DateTime'] = bar.pop('_id')
                    bars.append(bar)

            if stra.EndDate == time.strftime("%Y%m%d", time.localtime()):
                # 实时K线数据
                req.Type = BarType.Real
                if self.cfg.engine_postgres:
                    bars = bars + self.read_bars_pg(req)
                else:
                    for bar in self.get_data_zmq(req):
                        bar['Instrument'] = data.Instrument
                        bar['DateTime'] = bar.pop('_id')
                        bars.append(bar)

        bars.sort(key=lambda bar: bar['DateTime'])  # 按时间升序
        return bars

    def read_ticks(self, stra: Strategy, tradingday: str)->[]:
        """读取tick数据
        返回 list[Tick]"""
        ticks: list = []
        if self.cfg.engine_postgres is not None:
            conn = self.cfg.engine_postgres.raw_connection()
            cursor = conn.cursor()
            sql = "select count(1) from pg_tables where schemaname='future_tick' and tablename='{}'".format(tradingday)
            try:
                cursor.execute(sql)
                if cursor.fetchone()[0] == 0:
                    return []
                for data in stra.Datas:
                    sql = 'select "Actionday", "AskPrice", "AskVolume", "BidPrice", "BidVolume", "Instrument", "LastPrice", "OpenInterest", "UpdateMillisec", "UpdateTime", "Volume" from future_tick."{}" where "Instrument" = \'{}\''.format(
                        tradingday, data.Instrument)
                    cursor.execute(sql)
                    rows = cursor.fetchall()
                    for d in rows:
                        tick = Tick()
                        tick.Instrument = data.Instrument
                        tick.AskPrice = d[1]
                        tick.AskVolume = d[2]
                        tick.BidPrice = d[3]
                        tick.BidVolume = d[4]
                        tick.LastPrice = d[6]
                        tick.OpenInterest = d[7]
                        tick.UpdateMillisec = d[8]
                        tick.UpdateTime = d[0][0:4] + '-' + d[0][4:6] + '-' + d[0][6:] + ' ' + d[9]
                        tick.Volume = d[10]
                        ticks.append(tick)
            finally:
                conn.close()
        ticks.sort(key=lambda t: t.UpdateTime)
        return ticks

    def read_data_test(self):
        """取历史和实时K线数据,并执行策略回测"""
        stra: Strategy = None  # 只为后面的提示信息创建
        for stra in self.stra_instances:
            self.cfg.log.info('策略 {0} 正在加载历史数据'.format(stra.ID))
            if stra.TickTest:
                tradingday = stra.BeginDate
                tick: Tick = None
                while tradingday < time.strftime('%Y%m%d', time.localtime()):
                    for tick in self.read_ticks(stra, tradingday):
                        for data in stra.Datas:
                            if data.Instrument == tick.Instrument:
                                data.on_tick(tick, tradingday)
                    tradingday = datetime.strftime(datetime.strptime(tradingday, '%Y%m%d') + timedelta(days=1), '%Y%m%d')
            else:
                listBar = []
                bars = self.read_bars(stra)
                listBar = [Bar(b['DateTime'], b['Instrument'], b['High'], b['Low'], b['Open'], b['Close'], b['Volume'], b['OpenInterest'], b['Tradingday']) for b in bars]

                for bar in listBar:
                    for data in stra.Datas:
                        if data.Instrument == bar.Instrument:
                            data.__new_min_bar__(bar)  # 调Data的onbar
            # 生成策略的测试报告
            Report(stra)
        self.cfg.log.war("test history is end.")

    def link_fun(self):
        '''策略函数与ATP关联'''
        for stra in self.stra_instances:
            stra._data_order = self.on_order
            stra._get_orders = self.get_orders
            stra._get_lastorder = self.get_lastorder
            stra._get_notfill_orders = self.get_notfill_orders
            stra._req_order = self.req_order
            stra.ReqCancel = self.t.ReqOrderAction
            stra._req_cancel_all = self.cancel_all

            for data in stra.Datas:
                if self.q is not None and self.q.logined:
                    self.q.ReqSubscribeMarketData(data.Instrument)

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

    def get_stra(self, order: OrderField)->Strategy:
        lst = [stra for stra in self.stra_instances if stra.ID == order.Custom // 1000]
        if len(lst) > 0:
            return lst[0]
        return None

    def OnOrder(self, t: CtpTrade, order: OrderField):
        """"""
        if not order.IsLocal:
            return

        self.cfg.log.info(order)
        if order.VolumeLeft == 0:
            return

        stra = self.get_stra(order)
        if stra is None:
            return

        if self.cfg.chasing:
            threading.Thread(target=self.resend, args=(order,)).start()
        stra.OnOrder(order)

    def resend(self, order: OrderField):
        time.sleep(self.cfg.chasing['wait_seconds'])
        if order.VolumeLeft > 0:
            self.t.ReqOrderAction(order.OrderID)

    def OnCancel(self, t: CtpTrade, order: OrderField):
        """"""
        # self.cfg.log.info(order)
        if not order.IsLocal:
            return

        if order.VolumeLeft == 0:
            return

        stra = self.get_stra(order)
        if stra is None:
            return

        custom = order.Custom
        custom = custom + 100
        times = custom % 1000 // 100
        if times <= self.cfg.chasing['resend_times']:
            if order.Direction == DirectType.Buy:
                price = self.q.inst_tick[order.InstrumentID].AskPrice + self.cfg.chasing['offset_ticks'] * self.t.instruments[order.InstrumentID].PriceTick
            else:
                price = self.q.inst_tick[order.InstrumentID].BidPrice - self.cfg.chasing['offset_ticks'] * self.t.instruments[order.InstrumentID].PriceTick
        else:
            if order.Direction == DirectType.Buy:
                price = self.q.inst_tick[order.InstrumentID].UpperLimitPrice
            else:
                price = self.q.inst_tick[order.InstrumentID].LowerLimitPrice

        self.t.ReqOrderInsert(order.InstrumentID, order.Direction, order.Offset, price, order.VolumeLeft, OrderType.Limit, pCustom=custom)

        stra.OnCancel(order)

    def OnTrade(self, t: CtpTrade, trade: TradeField):
        """"""
        order = self.t.orders[trade.OrderID]
        if not order.IsLocal:
            return

        self.cfg.log.info(trade)
        stra = self.get_stra(order)
        if stra is None:
            return

        stra.OnTrade(trade)

    def OnRtnErrOrder(self, t: CtpTrade, order: OrderField, info: InfoField):
        """"""
        if not order.IsLocal:
            return

        self.cfg.log.info(order)
        stra = self.get_stra(order)
        if stra is None:
            return

        stra.OnErrOrder(order, info)

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
        # 接口未登录,不计算Actionday
        if self.TradingDay == '':
            return

        if self.cfg.engine_postgres:
            conn = self.cfg.engine_postgres.raw_connection()
            cursor = conn.cursor()
            cursor.execute('select _id from future_config.trade_date where trading = 1')
            self.trading_days = [c[0] for c in cursor.fetchall()]
        else:
            req = ReqPackage()
            req.Type = BarType.TradeDate
            self.trading_days = self.get_data_zmq(req)

        self.Actionday = self.TradingDay if self.trading_days.index(self.TradingDay) == 0 else self.trading_days[self.trading_days.index(self.TradingDay) - 1]
        self.Actionday1 = (datetime.strptime(self.Actionday, '%Y%m%d') + timedelta(days=1)).strftime('%Y%m%d')

    def CTPRun(self):
        """"""
        if self.cfg.front_trade == '' or self.cfg.front_quote == '':
            self.cfg.log.war('交易接口未配置')
            return
        if self.cfg.investor == '':
            self.cfg.investor = input('invesorid on {}:'.format(self.cfg.front_name))
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
