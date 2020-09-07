#!/usr/bin/env python
# -*- coding: utf-8 -*-
__title__ = '项目配置信息'
__author__ = 'HaiFeng'
__mtime__ = '20180820'

import yaml
import os
# from sqlalchemy import create_engine
# from sqlalchemy.engine import Engine
import shutil
from color_log.logger import Logger


class Config(object):
    """"""

    def __init__(self):
        self.log = Logger()
        # 配置文件顺序：环境变量，工作目录
        config_path = os.getcwd()
        if 'config_path' in os.environ:
            config_path = os.environ['config_path']    
        cfg_file = os.path.join(config_path, 'config.yml')
        if not os.path.exists(cfg_file):
            with open(cfg_file, 'w') as f:
                f.write("""---
ctp_config:
    # 为空时不登录
    ctp_front: 'sim_now'
    investor: '008107'
    password: '1'
    product_info: ''
    app_id: 'simnow_client_test'
    auth_code: '0000000000000000'

    # 追单设置
    chasing:
        wait_seconds: 3
        offset_ticks: -2
        resend_times: 3
    # ctp前置配置: 请改用期货公司对应6.3.15(SE)的前置
    fronts:
        sim_now:
            trade: tcp://180.168.146.187:10101
            quote: tcp://180.168.146.187:10111
            broker: '9999'
        ebf:
            trade: tcp://180.166.65.114:31205
            quote: tcp://180.166.65.114:31213
            broker: '8060'
# 数据源 - zmq配置
zmq_config: tcp://service.haifengat.com:15555
# zmq_config: tcp://172.19.129.98:15555
# 开关
onoff:
    # 是否7*24
    running_as_server: true
    # 是否发送委托
    real_order_enable: true
    # 一根K线只发送一次指令
    single_order_one_bar: true
    # 是否打印行情时间
    show_tick_time: false
# 策略路径配置
stra_path:
    # 路径
    strategies:
        # 策略文件名
        SMACross:
        # 策略配置参数ID
        - 119


""")
        cfg = yaml.load(open(cfg_file, 'r', encoding='utf-8').read(), yaml.FullLoader)

        # 追单设置
        self.chasing = cfg['ctp_config']['chasing']

        self.stra_path = cfg['stra_path']
        self.cfg_zmq = ''
        if 'zmq_config' in cfg:
            self.cfg_zmq = cfg['zmq_config']
            self.log.info(f'zmq server: {self.cfg_zmq}')

        self.front_trade = ''
        self.front_quote = ''
        self.broker = ''
        self.investor = ''
        self.password = ''
        self.product_info = ''
        self.app_id = ''
        self.auth_code = ''

        cfg_ctp = cfg['ctp_config']
        if cfg_ctp['ctp_front'] != '':
            self.front_name = cfg_ctp['ctp_front']
            cfg_ctp_front = cfg_ctp['fronts'][self.front_name]
            self.front_trade = cfg_ctp_front['trade']
            self.front_quote = cfg_ctp_front['quote']
            self.broker = cfg_ctp_front['broker']
            for v in ['investor', 'password', 'product_info', 'app_id', 'auth_code']:
                if v in cfg_ctp and cfg_ctp[v] != '':
                    vars(self)[v] = cfg_ctp[v]
            # if 'password' in cfg_ctp and cfg_ctp['password'] != '':
            #     self.pwd = cfg_ctp['password']

        self.single_order_one_bar = False
        '''是否每根K线只发一次指令'''

        self.real_order_enable = False
        '''是否实际对接口发单'''

        self.running_as_server = False
        '''是否作为服务7*24运行'''

        self.show_tick_time = False
        '''是否打印行情时间'''

        if 'onoff' in cfg:
            cfg_of = cfg['onoff']
            if 'running_as_server' in cfg_of:
                self.running_as_server = cfg_of['running_as_server']
            if 'single_order_one_bar' in cfg_of:
                self.single_order_one_bar = cfg_of['single_order_one_bar']
            if 'real_order_enable' in cfg_of:
                self.real_order_enable = cfg_of['real_order_enable']
            if 'show_tick_time' in cfg_of:
                self.show_tick_time = cfg_of['show_tick_time']
