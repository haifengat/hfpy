#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/05/31 9:16
# @Author  : HaiFeng
# @Email   : 24918700@qq.com
# @File    : atp.py
# @Software: PyCharm

import os, json, yaml

from yaml import loader  # 可能前面的import模块对time有影响,故放在最后

from .bar import Bar
from .data import Data
from .order import OrderItem
from .structs import DirectType, OffsetType
from .strategy import Strategy
# from .report_stra import Report
from .config import Config

from sqlalchemy.engine import ResultProxy


class ATP(object):
    """"""

    def __init__(self):
        self.trading_days: list = []
        '''交易日序列'''
        self.real = False
        '''是否实时行情'''
        self.cfg = Config()
        self.stra_instances = []

    def on_order(self, stra: Strategy, data: Data, order: OrderItem):
        """此处调用ctp接口即可实现实际下单"""
       
        # 可通过环境配置作为开关
        if self.cfg.pg_order is not None:
            # 为app提供
            if 'app' in os.environ:
                color = 'red' if order.Direction == DirectType.Buy else 'green'
                sign = f'{{"color": "{color}", "price": "{order.Price:.4f}"}}'
                sql = f"""INSERT INTO public.strategy_sign
        (tradingday, order_time, instrument, "period", strategy_id, strategy_group, sign, remark, insert_time)
        VALUES('{data.Bars[-1].Tradingday}', '{stra.D[-1]}', '{data.Instrument}', {data.Interval}, '{stra.ID}', '{type(stra).__name__}','{sign}', '', now())"""
            else:
                js = json.dumps({
                    'Direction': str(order.Direction).split('.')[1],
                    'Offset': str(order.Offset).split('.')[1],
                    'Price': round(order.Price, 4),
                    'Volume': order.Volume
                })
                sql = f"""INSERT INTO public.strategy_sign
                (tradingday, order_time, instrument, "period", strategy_id, strategy_group, sign, remark, insert_time)
                VALUES('{data.Bars[-1].Tradingday}', '{stra.D[-1]}', '{data.Instrument}', {data.Interval}, '{stra.ID}', '{type(stra).__name__}', '{js}', '', now())"""
            self.cfg.pg_order.execute(sql)
        if self.real and self.cfg.rds is not None:
            js = json.dumps({
                'Instrument': order.Instrument,
                'Direction': str(order.Direction).split('.')[1],
                'Offset': str(order.Offset).split('.')[1],
                'Price': round(order.Price, 4),
                'Volume': order.Volume,
                "ID": stra.ID * 1000 + len(stra.Orders) + 1
                })
            self.cfg.rds.publish(f'order.{type(stra).__name__}', js)
            self.cfg.log.war(js)
                
    def load_strategy(self):
        """加载../strategy目录下的策略"""
        """通过文件名取到对应的继承Data的类并实例"""
        for stra_name in self.cfg.strategy_name:
            f = os.path.join('./strategies', f'{stra_name}.py')
            # 只处理对应的 py文件
            if not os.path.exists(f):
                self.cfg.log.info(f'{f} is not exists!')
                continue
            # 以目录结构作为 namespace
            module_name = f"{os.path.split(os.path.dirname(f))[1]}.{stra_name}"
            module = __import__(module_name)  # import module

            c = getattr(getattr(module, stra_name), stra_name)  # 双层调用才是class,单层是为module
            if not issubclass(c, Strategy):  # 类c是Data的子类
                continue

            # 与策略文件同名的 yaml 作为配置文件处理
            cfg_file = os.path.join(f'./strategies/{stra_name}.yml')
            if os.path.exists(cfg_file):
                # 清除策略信号
                if self.cfg.pg_order is not None:
                    self.cfg.pg_order.execute(f"DELETE FROM public.strategy_sign WHERE strategy_group='{stra_name}'")
                with open(cfg_file, encoding='utf-8') as stra_cfg_file:
                    params = yaml.load(stra_cfg_file, loader.FullLoader)
                    for param in [p for p in params if p is not None]:  # 去除None的配置
                        stra: Strategy = c(param)
                        stra.ID = param['ID']
                        self.cfg.log.info(f"load strategy:{stra_name}, id:{param['ID']}")

                        for data in stra.Datas:
                            data.SingleOrderOneBar = self.cfg.single_order_one_bar
                        # 由atp处理策略指令
                        stra._data_order = self.on_order
                        self.stra_instances.append(stra)
            else:
                self.cfg.log.error(f"缺少对应的 yaml 配置文件{cfg_file}")

    def read_bars_his(self, stra: Strategy) -> list:
        """PG"""
        bars = []
        if self.cfg.pg_min is not None:
            res:ResultProxy = self.cfg.pg_min.execute(f"""SELECT to_char("DateTime", 'YYYY-MM-DD HH24:MI:SS') AS datetime, "Instrument", "Open", "High", "Low","Close","Volume", "OpenInterest", "TradingDay"
FROM future.future_min
WHERE "TradingDay" >= '{stra.BeginDate}'
AND "Instrument" IN ('{"','".join([d.Instrument for d in stra.Datas])}')
ORDER BY "DateTime"
""")
            row = res.fetchone()
            while row is not None:
                bars.append( {
                    'DateTime':row[0],
                    'Instrument':row[1], 
                    'Open':row[2],
                    'High':row[3], 
                    'Low':row[4], 
                    'Close':row[5], 
                    'Volume':row[6], 
                    'OpenInterest':row[7], 
                    'Tradingday':row[8]
                })
                row = res.fetchone()
        bars.sort(key=lambda bar: bar['DateTime'])  # 按时间升序
        return bars

    def read_bars_cur(self, stra:Strategy):
        """取当日数据"""        
        bars = []
        # 取实时数据
        if self.cfg.rds is not None:
            for inst in [d.Instrument for d in stra.Datas]:
                json_mins = self.cfg.rds.lrange(inst, 0, -1)
                for min in json_mins:
                    bar = json.loads(min)
                    bar['Instrument'] = inst
                    bar['DateTime'] = bar.pop('_id')
                    bar['Tradingday'] = bar.pop('TradingDay')
                    bars.append(bar)
        return bars

    def read_data_test(self):
        """取历史和实时K线数据,并执行策略回测"""
        for stra in self.stra_instances:
            self.cfg.log.info(f'策略 {type(stra).__name__}.{stra.ID} 加载历史数据...')
            listBar = []
            bars = self.read_bars_his(stra)
            listBar = [Bar(b['DateTime'], b['Instrument'], b['High'], b['Low'], b['Open'], b['Close'], b['Volume'], b['OpenInterest'], b['Tradingday']) for b in bars]

            for bar in listBar:
                for data in stra.Datas:
                    if data.Instrument == bar.Instrument:
                        data.__new_min_bar__(bar)  # 调Data的onbar
            # 生成策略的测试报告
            # if len(stra.Orders) > 0:
            #     Report(stra)
        self.cfg.log.war("test history is end.")
        # 加载当日数据
        for stra in self.stra_instances:
            self.cfg.log.info(f'策略 {type(stra).__name__}.{stra.ID} 加载当日数据...')
            listBar = []
            bars = self.read_bars_cur(stra)
            listBar = [Bar(b['DateTime'], b['Instrument'], b['High'], b['Low'], b['Open'], b['Close'], b['Volume'], b['OpenInterest'], b['Tradingday']) for b in bars]

            for bar in listBar:
                for data in stra.Datas:
                    if data.Instrument == bar.Instrument:
                        data.__new_min_bar__(bar)  # 调Data的onbar
        self.cfg.log.war("today test is end.")

    def Run(self):
        """"""
        ########### 信号入库 ########################
        if self.cfg.pg_order is not None:
            # 清除策略信号
            res = self.cfg.pg_order.execute("select count(1) from pg_catalog.pg_tables where schemaname='public' and tablename = 'strategy_sign'")
            if res.fetchone()[0] ==  0:
                sqls = f"""
CREATE TABLE public.strategy_sign (
	id serial NOT NULL, -- 自增序列
	tradingday varchar(8) NOT NULL, -- 交易日
	order_time varchar(20) NOT NULL, -- 信号时间:yyyy-MM-dd HH:mm:ss
	strategy_group varchar(255) NULL, -- 策略组(名)
	strategy_id varchar(32) NOT NULL, -- 策略标识
	instrument varchar(32) NOT NULL, -- 合约
	"period" int4 NOT NULL, -- 周期(单位-分钟)
	sign varchar(512) NOT NULL, -- 信号内容:json
	remark varchar(512) NULL, -- 备注
	insert_time timestamp NULL DEFAULT now() -- 入库时间
);
CREATE INDEX newtable_instrument_idx ON public.strategy_sign USING btree (instrument, period);
CREATE INDEX newtable_strategy_id_idx ON public.strategy_sign USING btree (strategy_id);
CREATE INDEX newtable_tradingday_idx ON public.strategy_sign USING btree (tradingday);
COMMENT ON TABLE public.strategy_sign IS '策略信号';

-- Column comments

COMMENT ON COLUMN public.strategy_sign.tradingday IS '交易日';
COMMENT ON COLUMN public.strategy_sign.order_time IS '信号时间:yyyy-MM-dd HH:mm:ss';
COMMENT ON COLUMN public.strategy_sign.instrument IS '合约';
COMMENT ON COLUMN public.strategy_sign."period" IS '周期(单位-分钟)';
COMMENT ON COLUMN public.strategy_sign.strategy_id IS '策略标识';
COMMENT ON COLUMN public.strategy_sign.sign IS '信号内容:json';
COMMENT ON COLUMN public.strategy_sign.remark IS '备注';
COMMENT ON COLUMN public.strategy_sign.insert_time IS '入库时间';
COMMENT ON COLUMN public.strategy_sign.id IS '自增序列';
COMMENT ON COLUMN public.strategy_sign.strategy_group IS '策略组(名)';

-- Permissions

ALTER TABLE public.strategy_sign OWNER TO postgres;
GRANT ALL ON TABLE public.strategy_sign TO postgres;
"""
                for sql in sqls.split(';'):
                    if sql.strip('\n') == "":
                        continue
                    self.cfg.pg_order.execute(sql.strip('\n'))
        self.cfg.log.info('加载策略...')
        self.load_strategy()
        self.cfg.log.info('历史数据回测...')
        self.read_data_test()
        # 订阅行情
        if self.cfg.rds is not None:
            self.real = True
            ps = self.cfg.rds.pubsub()
            for datas in [stra.Datas for stra in self.stra_instances]:
                for data in datas:
                    ps.psubscribe(f'md.{data.Instrument}')
            for tick in ps.listen():
                if tick['type'] == 'pmessage':
                    dic = json.loads(tick['data'])
                    bar = Bar(dic['_id'],tick['channel'][3:],dic['High'],dic['Low'],dic['Open'],dic['Close'],dic['Volume'],dic['OpenInterest'],dic['TradingDay'])
                    # 分钟数据后，传给各个策略
                    for datas in [stra.Datas for stra in self.stra_instances]:
                        for data in datas:
                            if data.Instrument == bar.Instrument:
                                data.on_min(bar)

