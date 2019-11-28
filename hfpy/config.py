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
        origin_cfg_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.yml')
        cfg_file = os.path.join(os.getcwd(), 'config.yml')
        if not os.path.exists(cfg_file):
            shutil.copy(origin_cfg_file, cfg_file)
        cfg = yaml.load(open(cfg_file, 'r', encoding='utf-8'), Loader=yaml.FullLoader)

        # 追单设置
        self.chasing = cfg['ctp_config']['chasing']

        self.stra_path = cfg['stra_path']
        self.cfg_zmq = ''
        if 'zmq_config' in cfg:
            self.cfg_zmq = cfg['zmq_config']

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
