#!/usr/bin/env python
# -*- coding: utf-8 -*-
__title__ = '项目配置信息'
__author__ = 'HaiFeng'
__mtime__ = '20180820'

import json
import os
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from .color_log import Logger


class Config(object):
    """"""

    def __init__(self):
        self.log = Logger()
        cfg_file = os.path.join(os.getcwd(), 'py_at', 'config.json')
        cfg = json.load(open(cfg_file, 'r', encoding='utf-8'))
        self.ctp_dll_path = cfg['ctp_config']['ctp_dll_path']
        self.stra_path = cfg['stra_path']

        self.engine_postgres: Engine = None
        if 'postgres_config' in cfg:
            cfg_pg = cfg['postgres_config']
            self.engine_postgres = create_engine('postgresql://{}:{}@{}:{}/{}'.format(cfg_pg['user'], cfg_pg['pwd'], cfg_pg['host'], cfg_pg['port'], cfg_pg['db']))
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
