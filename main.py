#!/usr/bin/env python
# -*- coding: utf-8 -*-
__title__ = '主程序'
__author__ = 'HaiFeng'
__mtime__ = '20180822'

import os
import sys
import time
import getpass
from py_at.a_t_p import ATP
from py_at.strategy import Strategy

if __name__ == '__main__':
    if not os.path.exists('log'):
        os.mkdir('log')
    p = ATP()
    p.CTPRun()
    p.load_strategy()
    p.read_data_test()

    # 注销148行
    stra: Strategy = None
    for stra in p.stra_instances:
        stra.EnableOrder = True
        stra._data_order = p.on_order
        stra._get_orders = p.get_orders
        stra._get_lastorder = p.get_lastorder
        stra._get_notfill_orders = p.get_notfill_orders
        stra._req_order = p.req_order
        stra.ReqCancel = p.t.ReqOrderAction
        stra._req_cancel_all = p.cancel_all

        for data in stra.Datas:
            data.SingleOrderOneBar = False
            if p.q and p.q.logined:
                p.q.ReqSubscribeMarketData(data.Instrument)
    input()
