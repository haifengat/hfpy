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
    if p.cfg.config['ctp_front'] != '':
        p.cfg.log.war('connecting == ' + p.cfg.config['ctp_front'] + ' ==')
        ctp_cfg = p.cfg.config['ctp_config'][p.cfg.config['ctp_front']]
        if len(sys.argv) == 3:
            p.CTPRun(
                ctp_cfg['trade'],
                ctp_cfg['quote'],
                ctp_cfg['broker'],
                investor=sys.argv[1],
                pwd=sys.argv[2])
        else:
            investor = ''
            pwd = ''
            if 'investor' in p.cfg and p.cfg.config['investor'] != '':
                investor = p.cfg.config['investor']
            else:
                investor = input('invesorid:')
            if 'password' in p.cfg.config['password'] and p.cfg.config['password'] != '':
                pwd = p.cfg.config['password']
            else:
                pwd = getpass.getpass()
            p.CTPRun(ctp_cfg['trade'], ctp_cfg['quote'], ctp_cfg['broker'],
                     investor, pwd)
        while not p.q.IsLogin:
            time.sleep(1)
    p.load_strategy()
    p.read_data_test()

    # 注销148行
    stra = Strategy('')
    for stra in p.stra_instances:
        stra.EnableOrder = True
        stra._data_order = p.on_order
        stra._get_orders = p.get_orders
        stra._get_lastorder = p.get_lastorder
        stra._get_notfill_orders = p.get_notfill_orders
        stra._req_order = p.req_order
        stra.ReqCancel = p.t.ReqOrderAction
        stra._req_cancel_all = p.cancel_all

        p.t.OnRtnOrder = stra.OnOrder
        p.t.OnRtnTrade = stra.OnTrade
        p.t.OnRtnCancel = stra.OnCancel
        p.t.OnRtnErrOrder = stra.OnErrOrder
        p.t.OnErrCancel = stra.OnErrCancel

        for data in stra.Datas:
            data.SingleOrderOneBar = False
            if p.q and p.q.IsLogin:
                p.q.ReqSubscribeMarketData(data.Instrument)
    input()
