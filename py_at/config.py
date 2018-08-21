#!/usr/bin/env python
# -*- coding: utf-8 -*-
__title__ = '项目配置信息'
__author__ = 'HaiFeng'
__mtime__ = '20180820'

import json
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
import platform
if 'Windows' in platform.system():
    from hf_log_win import Logger
else:
    from hf_log_linux import Logger


class Config(object):
    """"""

    def __init__(self):
        cfg_file = './stra_test.json'
        self.config = json.load(open(cfg_file, 'r', encoding='utf-8'))
        self.log = Logger()
        self.engine_postgres: Engine = None
        if 'postgres_config' in self.config:
            cfg = self.config['postgres_config']
            self.engine_postgres = create_engine('postgresql://{}:{}@{}:{}/{}'.format(cfg['user'], cfg['pwd'], cfg['host'], cfg['port'], cfg['db']))
