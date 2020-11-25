#!/usr/bin/env python
# -*- coding: utf-8 -*-
__title__ = '项目配置信息'
__author__ = 'HaiFeng'
__mtime__ = '20180820'

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
# import shutil
from color_log.logger import Logger
import redis, json, os


class Config(object):
    """"""

    def __init__(self):
        self.log = Logger()

        self.strategy_name = []
        '''策略配置json格式:stra_name:[stra_id]'''
        if 'strategy' in os.environ:
            self.strategy_name = os.environ['strategy'].split(',')

        self.single_order_one_bar = True
        '''是否每根K线只发一次指令'''
        if 'single_order_one_bar' in os.environ:
            self.single_order_one_bar = os.environ['single_order_one_bar']

        self.pg_min:Engine = None
        if 'pg_min' in os.environ:
            self.pg_min = create_engine(os.environ['pg_min'])        
            print(f"connecting pg min: {os.environ['pg_min']}")

        self.pg_order:Engine = None
        if 'pg_order' in os.environ:
            self.pg_order = create_engine(os.environ['pg_order'])  
            print(f"connecting pg min: {os.environ['pg_order']}")

        self.rds:redis.Redis = None
        '''实时行情库&实时order'''
        if 'redis_addr' in os.environ:
            host, port =  os.environ['redis_addr'].split(':')
            self.log.info(f'connecting redis: {host}:{port}')
            pool = redis.ConnectionPool(host=host, port=port, db=0, decode_responses=True)
            self.rds = redis.StrictRedis(connection_pool=pool)
