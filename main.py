#!/usr/bin/env python
# -*- coding: utf-8 -*-
__title__ = '主程序'
__author__ = 'HaiFeng'
__mtime__ = '20180822'

from py_at.a_t_p import ATP

if __name__ == '__main__':
    p = ATP()
    p.CTPRun()
    p.load_strategy()
    p.read_data_test()
    p.link_fun()

    input()
