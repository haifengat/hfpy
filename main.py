#!/usr/bin/env python
# -*- coding: utf-8 -*-
__title__ = '主程序'
__author__ = 'HaiFeng'
__mtime__ = '20180822'

from hfpy.atp import ATP

if __name__ == '__main__':
    atp = ATP()
    atp.Run()
    while input().lower() != 'q':
        continue
    atp.close_api()
