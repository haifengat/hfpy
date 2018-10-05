#!/usr/bin/env python
# -*- coding: utf-8 -*-
__title__ = '项目配置信息'
__author__ = 'HaiFeng'
__mtime__ = '20180820'

import yaml
import os
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from .color_log import Logger


class Config(object):
    """"""

    def __init__(self):
        self.log = Logger()
        cfg_file = os.path.join(os.getcwd(), 'py_at', 'config.yml')
        cfg = yaml.load(open(cfg_file, 'r', encoding='utf-8'))
        self.ctp_dll_path = cfg['ctp_config']['ctp_dll_path']
        self.stra_path = cfg['stra_path']
        self.cfg_zmq = ''
        if 'zmq_config' in cfg:
            self.cfg_zmq = cfg['zmq_config']
        self.engine_postgres: Engine = None
        if 'postgres_config' in cfg:
            self.engine_postgres = create_engine(cfg['postgres_config'])
        self.front_trade = ''
        self.front_quote = ''
        self.broker = ''
        self.investor = ''
        self.pwd = ''
        cfg_ctp = cfg['ctp_config']
        if cfg_ctp['ctp_front'] != '':
            cfg_ctp_front = cfg_ctp['fronts'][cfg_ctp['ctp_front']]
            self.front_trade = cfg_ctp_front['trade']
            self.front_quote = cfg_ctp_front['quote']
            self.broker = cfg_ctp_front['broker']
            if 'investor' in cfg_ctp and cfg_ctp['investor'] != '':
                self.investor = cfg_ctp['investor']
            if 'password' in cfg_ctp and cfg_ctp['password'] != '':
                self.pwd = cfg_ctp['password']

        self.single_order_one_bar = False
        self.real_order_enable = False
        if 'stra_onoff' in cfg:
            if 'single_order_one_bar' in cfg['stra_onoff']:
                self.single_order_one_bar = cfg['stra_onoff']['single_order_one_bar']
            if 'real_order_enable' in cfg['stra_onoff']:
                self.real_order_enable = cfg['stra_onoff']['real_order_enable']
