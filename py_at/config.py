#!/usr/bin/env python
# -*- coding: utf-8 -*-
__title__ = '项目配置信息'
__author__ = 'HaiFeng'
__mtime__ = '20180820'

import json
import os
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
import platform
if 'Windows' in platform.system():
    from .hf_log_win import Logger
else:
    from .hf_log_linux import Logger


class Config(object):
    """"""

    def __init__(self):
        self.log = Logger()
        cfg_file = os.path.join(os.getcwd(), 'py_at', 'config.json')
        cfg = json.load(open(cfg_file, 'r', encoding='utf-8'))
        self.ctp_dll_path = cfg['ctp_dll_path']
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
        if cfg['ctp_front'] != '':
            ctp_cfg = cfg['ctp_config'][cfg['ctp_front']]
            self.front_trade = ctp_cfg['trade']
            self.front_quote = ctp_cfg['quote']
            self.broker = ctp_cfg['broker']
            if 'investor' in cfg and cfg['investor'] != '':
                self.investor = cfg['investor']
            if 'password' in cfg and cfg['password'] != '':
                self.pwd = cfg['password']
