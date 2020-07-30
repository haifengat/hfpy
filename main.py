#!/usr/bin/env python
# -*- coding: utf-8 -*-
__title__ = '主程序'
__author__ = 'HaiFeng'
__mtime__ = '20180822'

from hfpy.atp import ATP

if __name__ == '__main__':
    atp = ATP()

    # 测试
    # from hfpy.structs import ReqPackage, BarType
    # import sys
    # req = ReqPackage()
    # # req.Type = BarType.Real
    # req.Instrument = 'rb2005'
    # req.Type = BarType.Min
    # req.Begin = '20190301'
    # req.End = '20200701'
    # atp.get_data_zmq(req)
    # sys.exit()

    atp.Run()
    while input().lower() != 'q':
        continue
    atp.close_api()
