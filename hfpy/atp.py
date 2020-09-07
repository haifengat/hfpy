#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/05/31 9:16
# @Author  : HaiFeng
# @Email   : 24918700@qq.com
# @File    : atp.py
# @Software: PyCharm

import os
import json
import yaml
import threading
import time  # 可能前面的import模块对time有影响,故放在最后
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
# from .report_stra import Report
from .config import Config

from py_ctp.trade import CtpTrade
from py_ctp.quote import CtpQuote
from py_ctp.enums import DirectType, OffsetType, OrderType, OrderStatus, InstrumentStatus
from py_ctp.structs import InfoField, OrderField, TradeField, Tick, InstrumentField


class ATP(object):
    """"""

    def __init__(self):
        self.TradingDay = ''
        '''交易日'''
        self.Actionday = ''
        '''自然日'''
        self.Actionday1 = ''
        '''隔夜自然日'''

        self.tick_time = ''
        '''最后tick的交易时间:yyyy-MM-dd HH:mm:ss'''

        self.trading_days: list = []
        '''交易日序列'''

        self.trade_time: dict = {}
        '''品种交易时间'''

        self.instrument_info = {}
        '''合约信息'''

        self.received_instrument: list = []
        '''已接收tick的合约'''

        self.cfg = Config()
        self.stra_instances = []

        self.q = CtpQuote()
        self.t = CtpTrade()

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
        if not self.cfg.stra_path:
            return
        for path in self.cfg.stra_path:
            for stra_name in self.cfg.stra_path[path]:
                f = os.path.join(path, '{}.py'.format(stra_name))
                # 只处理对应的 py文件
                if os.path.isdir(f) or os.path.splitext(f)[0] == '__init__':
                    continue
                # 以目录结构作为 namespace
                module_name = "{0}.{1}".format(os.path.split(os.path.dirname(f))[1], stra_name)

                module = __import__(module_name)  # import module

                c = getattr(getattr(module, stra_name), stra_name)  # 双层调用才是class,单层是为module

                if not issubclass(c, Strategy):  # 类c是Data的子类
                    continue

                # 与策略文件同名的 yaml 作为配置文件处理
                cfg_name = os.path.join(path, '{0}.yml'.format(stra_name))
                if os.path.exists(cfg_name):
                    with open(cfg_name, encoding='utf-8') as stra_cfg_json_file:
                        params = yaml.load(stra_cfg_json_file)
                        for param in [p for p in params if p is not None]:  # 去除None的配置
                            if param['ID'] not in self.cfg.stra_path[path][stra_name]:
                                continue
                            stra: Strategy = c(param)
                            stra.ID = param['ID']
                            self.cfg.log.info("# strategy:{0}".format(stra))

                            for data in stra.Datas:
                                data.InstrumentInfo = self.instrument_info[data.Instrument]
                                data.SingleOrderOneBar = self.cfg.single_order_one_bar
                            self.stra_instances.append(stra)
                else:
                    self.cfg.log.error("缺少对应的 yaml 配置文件{0}".format(cfg_name))

    def get_data_zmq(self, req: ReqPackage) -> dict:
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
        if len(gzipper) == 0:
            return {}
        bs = json.loads(gzipper)  # json解析
        return bs

    def read_bars(self, stra: Strategy) -> list:
        """netMQ"""
        bars = []
        for data in stra.Datas:
            # 请求数据格式
            req = ReqPackage()
            req.Type = BarType.Min
            req.Instrument = data.Instrument
            req.Begin = stra.BeginDate
            req.End = stra.EndDate
            # __dict__返回diction格式,即{key,value}格式

            for bar in self.get_data_zmq(req):
                bar['Instrument'] = data.Instrument
                bar['DateTime'] = bar.pop('_id')
                bars.append(bar)

            if stra.EndDate == time.strftime("%Y%m%d", time.localtime()):
                # 实时K线数据
                req.Type = BarType.Real
                for bar in self.get_data_zmq(req):
                    bar['Instrument'] = data.Instrument
                    bar['DateTime'] = bar.pop('_id')
                    bars.append(bar)

        bars.sort(key=lambda bar: bar['DateTime'])  # 按时间升序
        return bars

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
            # if len(stra.Orders) > 0:
            #     Report(stra)
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
        self.cfg.log.war("[trade] connected by client")
        if self.t.ReqUserLogin:
            self.t.ReqUserLogin(self.cfg.investor, self.cfg.password, self.cfg.broker, self.cfg.product_info, self.cfg.app_id, self.cfg.auth_code)

    def relogin(self):
        """"""
        self.t.ReqUserLogout()
        self.cfg.log.info('[trade] sleep 60 seconds to wait try connect next time')
        time.sleep(60)
        self.t.ReqConnect(self.cfg.front_trade)

    def OnRspUserLogin(self, t: CtpTrade, info: InfoField):
        """"""
        if info.ErrorID == 0:
            self.TradingDay = self.t.tradingday
            self.get_actionday()  # 取得交易日后才能取actionday
            self.received_instrument.clear()  # 记录收到的tick的合约
            self.get_trading_time()  # 取品种交易时间信息
            if not self.q.logined:
                self.q.OnConnected = self.q_OnFrontConnected
                self.q.OnUserLogin = self.q_OnRspUserLogin
                self.q.OnDisConnected = lambda o, x: self.cfg.log.war(f'[QUOTE]disconnected: {x}')
                # self.q.OnTick = self.q_Tick
                self.q.OnTick = lambda o, f: threading.Thread(target=self.q_Tick, args=(o, f)).start()
                self.q.ReqConnect(self.cfg.front_quote)
                if self.cfg.show_tick_time:
                    threading.Thread(target=self.showmsg).start()
            self.cfg.log.info('[trade] {}'.format(info))
        else:
            self.cfg.log.error('[trade] {}'.format(info))
            if info.ErrorID == 7:
                threading.Thread(target=self.relogin).start()

    def showmsg(self):
        while self.t.logined:
            if self.tick_time != '':
                msg = ''
                stra: Strategy = None
                for stra in self.stra_instances:
                    msg += '{}[L={}; S={}]{}||'.format(type(stra).__name__, stra.PositionLong, stra.PositionShort, stra.Params)
                print(self.tick_time + '||' + msg, end='\r')
            time.sleep(1)

    def get_stra(self, order: OrderField) -> Strategy:
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
        wait = self.cfg.chasing['wait_seconds']
        if wait > 0:
            time.sleep(wait)
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

    def OnInstrumentStatus(self, obj, inst: str, status: InstrumentStatus):
        """
        交易合约状态响应

        :param obj: Trade
            交易接口
        :param inst: str
            合约/品种
        :param status: InstrumentStatus
            状态

        :return:
        """
        # 夜盘结算or市场收盘自动退出
        if (datetime.now().strftime('%H%M%S') < '030000' and sum([1 if x == InstrumentStatus.Continous else 0 for x in self.t.instrument_status.values()]) == 0) or (sum([1 if x != InstrumentStatus.Closed else 0 for x in self.t.instrument_status.values()]) == 0):
            threading.Thread(target=self.close_api).start()

    def close_api(self):
        time.sleep(1)
        if self.t and self.t.logined:
            self.t.ReqUserLogout()
        if self.q and self.q.logined:
            self.q.ReqUserLogout()

    def q_OnFrontConnected(self, q: CtpQuote):
        """"""
        self.cfg.log.info("[quote] connected by client")
        self.q.ReqUserLogin(self.cfg.investor, self.cfg.password, self.cfg.broker)

    def q_OnRspUserLogin(self, q: CtpQuote, info: InfoField):
        """"""
        self.cfg.log.info('[quote] {}'.format(info))
        for stra in self.stra_instances:
            for data in stra.Datas:
                self.q.ReqSubscribeMarketData(data.Instrument)

    def q_Tick(self, q: CtpQuote, tick: Tick):
        """"""
        # 对tick时间进行修正处理
        ut = tick.UpdateTime[0:6] + '00'
        mins_dict = self.trade_time[tick.Instrument]
        # 由下面的 updatetime[-2:0] != '00' 处理
        if ut not in mins_dict['Mins']:
            # 开盘/收盘
            if ut in mins_dict['Opens']:
                tick.UpdateTime = (datetime.strptime(ut, '%H:%M:%S') + timedelta(minutes=1)).strftime('%H:%M:%S')
            elif ut in mins_dict['Ends']:
                # 重新登录会收到上一节的最后tick
                tick_dt = datetime.strptime('{} {}'.format(datetime.now().strftime('%Y%m%d'), tick.UpdateTime), '%Y%m%d %H:%M:%S')
                now_dt = datetime.now()
                diff_snd = 0
                if tick_dt > now_dt:
                    diff_snd = (tick_dt - now_dt).seconds
                else:
                    diff_snd = (now_dt - tick_dt).seconds
                if diff_snd > 30:
                    return
                tick.UpdateTime = (datetime.strptime(ut, '%H:%M:%S') + timedelta(seconds=-1)).strftime('%H:%M:%S')
            else:
                return
        # 首tick不处理(新开盘时会收到之前的旧数据)
        if tick.Instrument not in self.received_instrument:
            self.received_instrument.append(tick.Instrument)
            return

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

    def get_trading_time(self):
        self.trade_time.clear()
        req = ReqPackage()
        req.Type = BarType.Time
        times = self.get_data_zmq(req)
        # 按时间排序, 确保最后实施的时间段作为依据.
        # 根据时间段设置,生成 opens; ends; mins盘中时间
        for group in times:
            g_id = group['GroupId']  # list(group.keys())[0]
            section = json.loads(group['WorkingTimes'])  # list(group.values())[0]
            opens = []
            ends = []
            mins = []
            for s in section:
                opens.append((datetime.strptime(s['Begin'], '%H:%M:%S') + timedelta(minutes=-1)).strftime('%H:%M:00'))
                ends.append(s['End'])
                t_begin = datetime.strptime('20180101' + s['Begin'], '%Y%m%d%H:%M:%S')
                s_end = datetime.strptime('20180101' + s['End'], '%Y%m%d%H:%M:%S')
                if t_begin > s_end:  # 夜盘
                    s_end += timedelta(days=1)
                while t_begin < s_end:
                    mins.append(t_begin.strftime('%H:%M:00'))
                    t_begin = t_begin + timedelta(minutes=1)
            self.trade_time[g_id] = {'Opens': opens, 'Ends': ends, 'Mins': mins}
        # 品种交易时间==>合约交易时间
        for inst, info in self.t.instruments.items():
            proc = info.ProductID
            if proc in self.trade_time:
                self.trade_time[inst] = self.trade_time[proc]
            else:
                self.trade_time[inst] = self.trade_time['default']

    def get_actionday(self):
        # 取交易日历
        req = ReqPackage()
        req.Type = BarType.TradeDate
        self.trading_days = self.get_data_zmq(req)

        req.Type = BarType.Product
        products = self.get_data_zmq(req)
        proc_dict = {}
        for p in products:
            proc_dict[p['_id']] = p

        req.Type = BarType.InstrumentInfo
        insts = self.get_data_zmq(req)

        for inst_proc in insts:
            proc = proc_dict[inst_proc['ProductID']]
            f = InstrumentField()
            f.ExchangeID = proc['ExchangeID']
            f.InstrumentID = inst_proc['_id']
            f.PriceTick = proc['PriceTick']
            f.ProductID = inst_proc['ProductID']
            f.ProductType = proc['ProductType']
            f.VolumeMultiple = proc['VolumeTuple']
            if 'MAXLIMITORDERVOLUME' in proc:
                f.MaxOrderVolume = proc['MAXLIMITORDERVOLUME']
            self.instrument_info[inst_proc['_id']] = f

        # 接口未登录,不计算Actionday
        if self.TradingDay == '':
            return
        self.Actionday = self.TradingDay if self.trading_days.index(self.TradingDay) == 0 else self.trading_days[self.trading_days.index(self.TradingDay) - 1]
        self.Actionday1 = (datetime.strptime(self.Actionday, '%Y%m%d') + timedelta(days=1)).strftime('%Y%m%d')

    def Run(self):
        """"""
        if self.cfg.front_trade == '' or self.cfg.front_quote == '':
            self.cfg.log.war('**** 交易接口未配置 ****')
            self.get_actionday()
        else:
            if self.cfg.investor == '':
                self.cfg.investor = input('invesorid on {}:'.format(self.cfg.front_name))
            else:
                self.cfg.log.war('{} loging by ctp'.format(self.cfg.investor))
            if self.cfg.password == '':
                self.cfg.password = getpass.getpass()
            if self.cfg.running_as_server:
                self.cfg.log.war('7*24 as server ....')
                threading.Thread(target=self._run_seven, daemon=True).start()
            else:
                self.cfg.log.war('run once only')
                self.start_api()
            while not self.q.logined:
                time.sleep(1)
        self.cfg.log.info('加载策略...')
        self.load_strategy()
        self.cfg.log.info('历史数据回测...')
        self.read_data_test()
        self.link_fun()

    def start_api(self):
        '''启动接口'''
        self.t.OnConnected = self.OnFrontConnected
        self.t.OnDisConnected = lambda o, x: self.cfg.log.war(f'[TRADE]disconnected: {x}')
        self.t.OnUserLogin = self.OnRspUserLogin
        self.t.OnOrder = self.OnOrder
        self.t.OnTrade = self.OnTrade
        self.t.OnCancel = self.OnCancel
        self.t.OnErrOrder = self.OnRtnErrOrder
        self.t.OnInstrumentStatus = self.OnInstrumentStatus

        self.t.ReqConnect(self.cfg.front_trade)

    def _run_seven(self):
        '''7*24'''
        while True:
            day = datetime.now().strftime('%Y%m%d')
            left_days = list(filter(lambda x: x > day, self.trading_days))
            if len(left_days) == 0:
                self.cfg.log.info('读取交易日历...')
                self.get_actionday()
                left_days = list(filter(lambda x: x > day, self.trading_days))
            next_trading_day = left_days[0]
            has_hight = (datetime.strptime(next_trading_day, '%Y%m%d') - datetime.strptime(day, '%Y%m%d')).days in [1, 3]

            now_time = datetime.now().strftime('%H%M%S')
            if not self.t.logined:
                # 当前非交易日
                sleep_seconds = 0
                if day not in self.trading_days:
                    # 昨天有夜盘:今天凌晨有数据
                    if now_time <= '020000' and (datetime.today() + timedelta.days(-1)).strftime('%Y%m%d') in self.trading_days:
                        time.sleep(1)
                    else:
                        self.cfg.log.info('{} is not tradingday.'.format(day))
                        self.cfg.log.info('continue after {}'.format(next_trading_day + ' 08:30:00'))
                        sleep_seconds = (int)((datetime.strptime(next_trading_day + '08:31:00', '%Y%m%d%H:%M:%S') - datetime.now()).total_seconds())
                elif now_time <= '083000':
                    self.cfg.log.info('continue after {}'.format(day + ' 08:30:00'))
                    sleep_seconds = (int)((datetime.strptime(day + '08:31:00', '%Y%m%d%H:%M:%S') - datetime.now()).total_seconds())
                elif now_time >= '150000':
                    if has_hight:
                        if datetime.now().strftime('%H%M%S') < '203000':
                            self.cfg.log.info('continue after {}'.format(day + ' 20:30:00'))
                            sleep_seconds = (int)((datetime.strptime(day + '20:31:00', '%Y%m%d%H:%M:%S') - datetime.now()).total_seconds())
                    else:
                        self.cfg.log.info('continue after {}'.format(next_trading_day + ' 08:30:00'))
                        sleep_seconds = (int)((datetime.strptime(next_trading_day + '08:31:00', '%Y%m%d%H:%M:%S') - datetime.now()).total_seconds())
                if sleep_seconds > 0:
                    time.sleep(sleep_seconds)
                    sleep_seconds = 0
                # 启动接口
                self.start_api()
                time.sleep(10)
                # 已收盘
            # elif sum([1 if x != InstrumentStatus.Closed else 0 for x in self.t.instrument_status.values()]) == 0:
            #     self.t.ReqUserLogout()
            #     self.q.ReqUserLogout()
            #     if has_hight:
            #         self.cfg.log.info('continue after {}'.format(day + ' 20:30:00'))
            #         time.sleep((datetime.strptime(day + '20:31:00', '%Y%m%d%H:%M:%S') - datetime.now()).total_seconds())
            #     else:
            #         self.cfg.log.info('continue after {}'.format(next_trading_day + ' 08:30:00'))
            #         time.sleep((datetime.strptime(next_trading_day + '08:31:00', '%Y%m%d%H:%M:%S') - datetime.now()).total_seconds())
            # # 夜盘全部非交易
            # elif now_time < '030000' and sum([1 if x == InstrumentStatus.Continous else 0 for x in self.t.instrument_status.values()]) == 0:
            #     cur_trading_day = self.t.tradingday
            #     self.t.ReqUserLogout()
            #     self.q.ReqUserLogout()
            #     # cur_trading_day = self.trading_days[self.trading_days.index(next_trading_day) - 1] 周末时取值不对
            #     self.cfg.log.info('continue after {}'.format(cur_trading_day + ' 08:30:00'))
            #     time.sleep((datetime.strptime(cur_trading_day + '08:31:00', '%Y%m%d%H:%M:%S') - datetime.now()).total_seconds())
            else:
                time.sleep(60 * 10)
